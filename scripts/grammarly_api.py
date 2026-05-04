#!/usr/bin/env python3
"""Minimal CLI for Grammarly's AI Detection and Plagiarism APIs."""

from __future__ import annotations

import argparse
import json
import mimetypes
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any

TOKEN_ENDPOINT = "https://auth.grammarly.com/v4/api/oauth2/token"
ENV_FILES = (Path(".env.local"), Path(".env"))
USER_AGENT = "mestrado-grammarly-cli/1.0"
DEFAULT_TIMEOUT = 120
DEFAULT_POLL_INTERVAL = 2.0

API_CONFIG = {
    "ai-detection": {
        "base_url": "https://api.grammarly.com/ecosystem/api/v1/ai-detection",
        "read_scope": "ai-detection-api:read",
        "write_scope": "ai-detection-api:write",
    },
    "plagiarism": {
        "base_url": "https://api.grammarly.com/ecosystem/api/v1/plagiarism",
        "read_scope": "plagiarism-api:read",
        "write_scope": "plagiarism-api:write",
    },
}


class GrammarlyError(RuntimeError):
    pass


def load_local_env() -> None:
    for env_file in ENV_FILES:
        if not env_file.exists():
            continue
        for raw_line in env_file.read_text(encoding="utf-8").splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip("'\""))


def request_json(
    method: str,
    url: str,
    *,
    payload: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
) -> dict[str, Any]:
    data = None
    req_headers = {
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    if headers:
        req_headers.update(headers)
    if payload is not None:
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req_headers["Content-Type"] = "application/x-www-form-urlencoded"

    req = urllib.request.Request(url, data=data, headers=req_headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            error_data = json.loads(raw)
        except json.JSONDecodeError:
            error_data = {"message": raw}
        message = error_data.get("message") or error_data.get("error", {}).get("message") or raw
        raise GrammarlyError(f"HTTP {exc.code}: {message}") from exc
    except urllib.error.URLError as exc:
        raise GrammarlyError(f"Network error: {exc.reason}") from exc


def request_api_json(
    method: str,
    url: str,
    access_token: str,
    *,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    data = None
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "User-Agent": USER_AGENT,
    }
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        try:
            error_data = json.loads(raw)
        except json.JSONDecodeError:
            error_data = {"message": raw}
        message = error_data.get("message") or error_data.get("error", {}).get("message") or raw
        raise GrammarlyError(f"HTTP {exc.code}: {message}") from exc
    except urllib.error.URLError as exc:
        raise GrammarlyError(f"Network error: {exc.reason}") from exc


def upload_file(upload_url: str, file_path: Path) -> None:
    content_type = mimetypes.guess_type(file_path.name)[0] or "application/octet-stream"
    data = file_path.read_bytes()
    req = urllib.request.Request(
        upload_url,
        data=data,
        headers={
            "Content-Type": content_type,
            "Content-Length": str(len(data)),
            "User-Agent": USER_AGENT,
        },
        method="PUT",
    )
    try:
        with urllib.request.urlopen(req):
            return
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", errors="replace")
        raise GrammarlyError(f"Upload failed with HTTP {exc.code}: {raw}") from exc
    except urllib.error.URLError as exc:
        raise GrammarlyError(f"Upload failed: {exc.reason}") from exc


def get_client_credentials(
    explicit_id: str | None,
    explicit_secret: str | None,
) -> tuple[str, str]:
    client_id = explicit_id or os.environ.get("GRAMMARLY_CLIENT_ID")
    client_secret = explicit_secret or os.environ.get("GRAMMARLY_CLIENT_SECRET")
    if not client_id or not client_secret:
        raise GrammarlyError(
            "Missing Grammarly OAuth credentials. Set GRAMMARLY_CLIENT_ID and "
            "GRAMMARLY_CLIENT_SECRET in .env.local/.env or pass them explicitly."
        )
    return client_id, client_secret


def get_access_token(
    client_id: str,
    client_secret: str,
    scopes: list[str],
) -> str:
    if not scopes:
        raise GrammarlyError("At least one OAuth scope is required.")
    response = request_json(
        "POST",
        TOKEN_ENDPOINT,
        payload={
            "grant_type": "client_credentials",
            "client_id": client_id,
            "client_secret": client_secret,
            "scope": ", ".join(scopes),
        },
    )
    token = response.get("access_token")
    if not token:
        raise GrammarlyError("OAuth response did not include an access_token.")
    return token


def submit_score_request(api_name: str, access_token: str, file_path: Path) -> dict[str, Any]:
    config = API_CONFIG[api_name]
    payload = {"filename": file_path.name}
    return request_api_json("POST", config["base_url"], access_token, payload=payload)


def fetch_score_request(api_name: str, access_token: str, score_request_id: str) -> dict[str, Any]:
    config = API_CONFIG[api_name]
    url = f"{config['base_url']}/{urllib.parse.quote(score_request_id)}"
    return request_api_json("GET", url, access_token)


def wait_for_result(
    api_name: str,
    access_token: str,
    score_request_id: str,
    timeout: int,
    poll_interval: float,
) -> dict[str, Any]:
    deadline = time.time() + timeout
    while True:
        result = fetch_score_request(api_name, access_token, score_request_id)
        status = result.get("status")
        if status in {"COMPLETED", "FAILED"}:
            return result
        if time.time() >= deadline:
            raise GrammarlyError(
                f"Timed out while waiting for {api_name} result for {score_request_id}."
            )
        time.sleep(poll_interval)


def ensure_file(file_arg: str) -> Path:
    path = Path(file_arg)
    if not path.is_file():
        raise GrammarlyError(f"File not found: {path}")
    return path


def print_json(data: dict[str, Any]) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


def print_summary(api_name: str, result: dict[str, Any]) -> None:
    status = result.get("status", "unknown")
    score_request_id = result.get("score_request_id", "")
    print(f"API: {api_name}")
    print(f"Score request: {score_request_id}")
    print(f"Status: {status}")

    if status != "COMPLETED":
        if result.get("reason"):
            print(f"Reason: {result['reason']}")
        return

    score = result.get("score") or {}
    if api_name == "ai-detection":
        avg_conf = score.get("average_confidence")
        ai_pct = score.get("ai_generated_percentage")
        print(f"Average confidence: {avg_conf}")
        print(f"AI-generated percentage: {ai_pct}")
    elif api_name == "plagiarism":
        print(f"Originality: {score.get('originality')}")


def resolve_scopes(api_name: str, mode: str) -> list[str]:
    config = API_CONFIG[api_name]
    if mode == "read":
        return [config["read_scope"]]
    if mode == "write":
        return [config["write_scope"]]
    if mode == "read-write":
        return [config["read_scope"], config["write_scope"]]
    raise GrammarlyError(f"Unknown scope mode: {mode}")


def command_token(args: argparse.Namespace) -> int:
    client_id, client_secret = get_client_credentials(args.client_id, args.client_secret)
    scopes = args.scope or resolve_scopes(args.api, args.scope_mode)
    token = get_access_token(client_id, client_secret, scopes)
    if args.json:
        print_json({"access_token": token, "scopes": scopes})
    else:
        print(token)
    return 0


def command_submit(args: argparse.Namespace) -> int:
    file_path = ensure_file(args.file)
    client_id, client_secret = get_client_credentials(args.client_id, args.client_secret)
    access_token = get_access_token(
        client_id,
        client_secret,
        resolve_scopes(args.api, "read-write"),
    )
    submission = submit_score_request(args.api, access_token, file_path)
    upload_url = submission.get("file_upload_url")
    score_request_id = submission.get("score_request_id")
    if not upload_url or not score_request_id:
        raise GrammarlyError("Submission response did not include upload URL and request ID.")
    upload_file(upload_url, file_path)
    if args.json:
        print_json(submission)
    else:
        print(f"Submitted {file_path.name}")
        print(f"Score request: {score_request_id}")
    return 0


def command_get(args: argparse.Namespace) -> int:
    client_id, client_secret = get_client_credentials(args.client_id, args.client_secret)
    access_token = get_access_token(
        client_id,
        client_secret,
        resolve_scopes(args.api, "read"),
    )
    result = fetch_score_request(args.api, access_token, args.score_request_id)
    if args.json:
        print_json(result)
    else:
        print_summary(args.api, result)
    return 0


def command_check(args: argparse.Namespace) -> int:
    file_path = ensure_file(args.file)
    client_id, client_secret = get_client_credentials(args.client_id, args.client_secret)
    access_token = get_access_token(
        client_id,
        client_secret,
        resolve_scopes(args.api, "read-write"),
    )
    submission = submit_score_request(args.api, access_token, file_path)
    upload_url = submission.get("file_upload_url")
    score_request_id = submission.get("score_request_id")
    if not upload_url or not score_request_id:
        raise GrammarlyError("Submission response did not include upload URL and request ID.")
    upload_file(upload_url, file_path)
    result = wait_for_result(
        args.api,
        access_token,
        score_request_id,
        timeout=args.timeout,
        poll_interval=args.poll_interval,
    )
    if args.json:
        print_json(
            {
                "submission": submission,
                "result": result,
            }
        )
    else:
        print_summary(args.api, result)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="CLI for Grammarly AI Detection and Plagiarism APIs."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    token_parser = subparsers.add_parser("token", help="Request an OAuth access token.")
    token_parser.add_argument("--api", choices=sorted(API_CONFIG.keys()), required=True)
    token_parser.add_argument("--scope", action="append", default=[])
    token_parser.add_argument(
        "--scope-mode",
        choices=("read", "write", "read-write"),
        default="read-write",
        help="Used when --scope is not provided.",
    )
    token_parser.add_argument("--client-id")
    token_parser.add_argument("--client-secret")
    token_parser.add_argument("--json", action="store_true")
    token_parser.set_defaults(func=command_token)

    for api_name in sorted(API_CONFIG.keys()):
        api_parser = subparsers.add_parser(api_name, help=f"{api_name} operations.")
        api_parser.set_defaults(api=api_name)
        api_subparsers = api_parser.add_subparsers(dest="api_command", required=True)

        submit_parser = api_subparsers.add_parser("submit", help="Create a score request and upload a file.")
        submit_parser.add_argument("file")
        submit_parser.add_argument("--client-id")
        submit_parser.add_argument("--client-secret")
        submit_parser.add_argument("--json", action="store_true")
        submit_parser.set_defaults(func=command_submit)

        get_parser = api_subparsers.add_parser("get", help="Fetch an existing score request result.")
        get_parser.add_argument("score_request_id")
        get_parser.add_argument("--client-id")
        get_parser.add_argument("--client-secret")
        get_parser.add_argument("--json", action="store_true")
        get_parser.set_defaults(func=command_get)

        check_parser = api_subparsers.add_parser(
            "check",
            help="Submit a file, upload it, and wait for the final result.",
        )
        check_parser.add_argument("file")
        check_parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
        check_parser.add_argument("--poll-interval", type=float, default=DEFAULT_POLL_INTERVAL)
        check_parser.add_argument("--client-id")
        check_parser.add_argument("--client-secret")
        check_parser.add_argument("--json", action="store_true")
        check_parser.set_defaults(func=command_check)

    return parser


def main(argv: list[str] | None = None) -> int:
    load_local_env()
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except GrammarlyError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
