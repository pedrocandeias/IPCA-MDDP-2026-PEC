#!/usr/bin/env bash
#
# Install the repo's version-controlled git hooks.
#
# Points git at tools/hooks/ (instead of the default .git/hooks/, which is not
# version-controlled) so every clone shares the same hooks. Run once per clone:
#
#   ./tools/install_hooks.sh
#
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

chmod +x tools/hooks/* 2>/dev/null || true
git config core.hooksPath tools/hooks

echo "core.hooksPath -> $(git config core.hooksPath)"
echo "Installed hooks:"
ls -1 tools/hooks
