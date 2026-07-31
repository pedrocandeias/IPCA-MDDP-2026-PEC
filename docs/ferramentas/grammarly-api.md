# Grammarly API Tools

Local CLI for Grammarly's official `AI Detection API (Beta)` and `Plagiarism Detection API (Beta)`.

Script:

- `tools/grammarly_api.py`

## Access requirements

These APIs are not generally open to all Grammarly accounts. According to Grammarly's official developer documentation, OAuth 2.0 credentials are available to admins with:

- `Grammarly Enterprise`
- `Grammarly for Education` with institution-wide licenses

Official docs:

- https://developer.grammarly.com/
- https://developer.grammarly.com/oauth-credentials.html
- https://developer.grammarly.com/ai-detection-api.html
- https://developer.grammarly.com/plagiarism-detection-api.html

## Required environment variables

Store credentials in `.env.local`, `.env`, or the shell environment:

```env
GRAMMARLY_CLIENT_ID=your_client_id
GRAMMARLY_CLIENT_SECRET=your_client_secret
```

## Usage

Request a token:

```bash
python3 tools/grammarly_api.py token --api ai-detection
python3 tools/grammarly_api.py token --api plagiarism
```

Run AI detection end-to-end:

```bash
python3 tools/grammarly_api.py ai-detection check path/to/file.docx
python3 tools/grammarly_api.py ai-detection check path/to/file.txt --json
```

Run plagiarism detection end-to-end:

```bash
python3 tools/grammarly_api.py plagiarism check path/to/file.docx
python3 tools/grammarly_api.py plagiarism check path/to/file.txt --json
```

Split the workflow into submit/get:

```bash
python3 tools/grammarly_api.py ai-detection submit path/to/file.docx
python3 tools/grammarly_api.py ai-detection get <score_request_id>

python3 tools/grammarly_api.py plagiarism submit path/to/file.docx
python3 tools/grammarly_api.py plagiarism get <score_request_id>
```

## Notes

- Supported file types in Grammarly's docs: `.doc`, `.docx`, `.odt`, `.txt`, `.rtf`
- File size limit: `4 MB`
- Text limit: `100,000` characters
- Minimum text length: `30` words
- Grammarly documents say uploaded content is retained no longer than `24 hours`
- Results are available for `30 days`

## What the script does

For `ai-detection` and `plagiarism`, the CLI:

1. Requests an OAuth access token using the client credentials flow.
2. Creates a score request.
3. Uploads the document to Grammarly's pre-signed upload URL.
4. Polls the result until `COMPLETED` or `FAILED` when using `check`.

## Output shape

AI detection returns:

- `average_confidence`
- `ai_generated_percentage`

Plagiarism detection returns:

- `originality`
