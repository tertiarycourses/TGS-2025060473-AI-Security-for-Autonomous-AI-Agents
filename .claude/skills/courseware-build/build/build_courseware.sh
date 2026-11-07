#!/usr/bin/env bash
# Single-command aligned build: labs + prompts page, deck, LP, LG; PDFs with page-numbered TOCs.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$HERE/../../../.." && pwd)"; CW="$REPO/courseware"; SOFFICE="${SOFFICE:-soffice}"
NAME=$(cd "$HERE" && python3 -c "import course_data as C;print(C.DECK_NAME)"); LP=$(cd "$HERE" && python3 -c "import course_data as C;print(C.LP_NAME)"); LG=$(cd "$HERE" && python3 -c "import course_data as C;print(C.LG_NAME)")
python3 "$HERE/build_labs.py"
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --window-size=1400,1000 --screenshot="$CW/assets/v5/prompts-page.png" "file://$REPO/prompts/index.html" >/dev/null 2>&1 || true
python3 "$HERE/build_slides.py"; python3 "$HERE/build_lesson_plan.py"; python3 "$HERE/build_learner_guide.py"
cd "$CW"
"$SOFFICE" --headless --convert-to pdf "$NAME.pptx" >/dev/null 2>&1
for f in "$LP" "$LG"; do "$SOFFICE" --headless --convert-to pdf "$f.docx" >/dev/null 2>&1; python3 "$HERE/inject_toc.py" "$f.docx" "$f.pdf" 2; "$SOFFICE" --headless --convert-to pdf "$f.docx" >/dev/null 2>&1; done
echo built; ls -la "$CW" | grep -E "v50|Lesson Plan|Learner Guide"
