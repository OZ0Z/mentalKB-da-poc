#!/usr/bin/env bash
set -euo pipefail
ROOT=${1:-../legacy/java}

if ! command -v rg >/dev/null 2>&1; then
  echo "ripgrep (rg) is required" >&2
  exit 1
fi

echo "kind,scope,target,inputs,condition_snippet,file,line"

rg --no-heading --line-number --color=never -f patterns.txt "$ROOT" \
| awk -F: '
function trim(s) { gsub(/^[ \t]+|[ \t]+$/, "", s); return s }
{
  file=$1; line=$2;
  snippet=$0; sub("^" file ":" line ":", "", snippet)
  kind="unknown"; scope="unknown"; target=""; inputs="";
  s=tolower(snippet)

  if (s ~ /setvisible|visible|show|hide/) {
    kind="visibility"
  } else if (s ~ /next|previous|navigate|route|switch|case/) {
    kind="branching"
  } else if (s ~ /required|validate|validation|error|adderror|pattern\\.compile|matches\(/) {
    kind="validation"
  } else if (s ~ /equals|compareto|isafter|isbefore|age|difference/) {
    kind="computed"
  } else if (s ~ /options|choices|list|lookup|filter/) {
    kind="options"
  }

  match(snippet, /question_field\s*[:=]\s*"?([A-Za-z0-9_]+)"?/, m1);
  if (m1[1] != "") target=m1[1];
  match(snippet, /pagename\s*[:=]\s*"?([A-Za-z0-9_]+)"?/, m2);
  if (m2[1] != "") target=m2[1];

  gsub(/"/, """", snippet)
  printf("%s,%s,%s,%s,\"%s\",%s,%s\n", kind, scope, target, inputs, trim(snippet), file, line)
}'
