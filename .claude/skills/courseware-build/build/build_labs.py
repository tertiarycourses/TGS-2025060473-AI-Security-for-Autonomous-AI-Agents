#!/usr/bin/env python3
"""Builds labs/labN-*/ (LAB-0N-Instructions.pdf + data/ + scripts/) and prompts/index.html.
House rule (user, 7 Nov 2026): each lab is one folder holding mock data, scripts and prompt instructions in PDF.
No Markdown files in lab folders. Prompts are copied from the one-click HTML page. Never deletes anything else."""
import html, os, shutil, stat, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS
import mock_data as M

def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env): return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")): return d
    raise SystemExit("repo not found")
REPO = _find_repo(HERE)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SYNTH = "All company data in these labs is fictional and generated for training: Kopi Kaki Co., its people, members, NRIC numbers, tickets and traces."
FOOT = f"Part of the WSQ course {C.TITLE} ({C.COURSE_CODE}) · © 2026 {C.ORG} · {C.UEN} · www.tertiarycourses.com.sg"
DESCR = {"seed-calendar.csv": "Five mock meetings, one clash. Your trainer seeds these into the training account.", "seed-emails.txt": "Three mock emails that go with the meetings.",
 "assistant-check-template.txt": "Fill this in to record what the agent really did.", "customer-feedback.csv": "24 mock reviews. One carries a planted instruction.",
 "pre-orders.xlsx": "Mock pre-order sales for the weak versus strong prompt warm-up.", "guardrail-rules.txt": "The guardrail text the fix uses.",
 "kaki-rules.txt": "Kaki's four rules.", "jailbreak-attempts.txt": "Four attacks to try on your own lab agent.", "loyalty-members.csv": "120 fictional members with NRIC, mobile, email and birth date.",
 "company-profile.txt": "Who Kopi Kaki is and what data it holds.", "ai-agent-register.csv": "The four agents it runs, their rights and owners.", "data-classification-starter.csv": "A starter list for the data tiers.",
 "agent-traces.jsonl": "146 mock trace events, 3 to 15 August 2026.", "helpdesk-tickets.csv": "The tickets that revealed the leak.", "phishing-email.txt": "The fake supplier email.", "incident-brief.txt": "Your assignment."}
SDESCR = {"clash_check.py": "Finds real calendar clashes, so you can check the agent's answer.", "check_injection.py": "Scores a saved summary: INJECTED or BLOCKED.", "sanitize_input.py": "Input guardrail: flags and removes instruction-like text before the model reads it.",
 "score_jailbreak.py": "Scores a saved reply: JAILBROKEN or HELD.", "voucher_gate.py": "A guardrail in code: only approved voucher codes pass.", "redact_pii.py": "Removes NRIC and birth date, masks the rest, before the agent reads the file.",
 "leak_scan.py": "Output guardrail: counts personal data in a reply.", "check_policy.py": "Checks your policy covers the five principles and names owners.", "trace_query.py": "Reads the traces yourself, so you can check the AI.", "check_report.py": "Checks your report states what the traces and the PDPA demand."}

CSS = """:root{--ink:#21201C;--muted:#6B6862;--acc:#C2603F;--rule:#E3DFD6;--bg:#FAF9F5;--panel:#FFFFFF;--code:#2B2924}
*{box-sizing:border-box}body{font-family:Calibri,'Segoe UI',Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.5;font-size:16px;margin:0}
h1,h2,h3{font-family:Cambria,Georgia,serif;line-height:1.2}h1{font-size:30px;margin:6px 0}h2{font-size:21px;margin:22px 0 8px;border-bottom:1px solid var(--rule);padding-bottom:4px}h3{font-size:16.5px;margin:0 0 6px}
.wrap{max-width:860px;margin:auto;padding:22px}.k{color:var(--acc);font-weight:700;font-size:12.5px;letter-spacing:.06em;text-transform:uppercase;margin:0}.meta{color:var(--muted);font-size:14px}
.hook{font-family:Cambria,Georgia,serif;font-size:18px;font-style:italic}.step{background:var(--panel);border:1px solid var(--rule);border-radius:9px;padding:12px 14px;margin:10px 0;break-inside:avoid}
pre{background:var(--code);color:#F1EDE4;padding:11px 13px;border-radius:7px;white-space:pre-wrap;word-wrap:break-word;font:12.5px/1.45 Menlo,Consolas,monospace;margin:7px 0}
.exp{color:#2D6664;font-size:14.5px;margin:6px 0 0}.shot{background:#F6E7DF;border-left:4px solid var(--acc);padding:7px 11px;border-radius:5px;font-weight:700;font-size:14px;margin:7px 0 0}
table{border-collapse:collapse;width:100%;font-size:14px;margin:6px 0}th{background:#21201C;color:#fff;text-align:left}th,td{border:1px solid var(--rule);padding:6px 8px;vertical-align:top;background:#fff}th{background:#21201C}
.card{background:#21201C;color:#E8E5DE;padding:10px 13px;border-radius:8px;margin:10px 0}.note{background:#fff;border:1px dashed var(--acc);padding:9px 12px;border-radius:8px;font-size:14px}.foot{color:var(--muted);font-size:12px;margin-top:20px;border-top:1px solid var(--rule);padding-top:8px}
code{font:13px Menlo,Consolas,monospace}a{color:var(--acc)}"""
PRINT = "@page{size:A4;margin:14mm}body{background:#fff;font-size:13.5px}.wrap{max-width:none;padding:0}.step{border-color:#ddd}"
def e(t): return html.escape(str(t))

def lab_html(L, dfiles, sfiles):
    p = [f"<!doctype html><html lang='en'><head><meta charset='utf-8'><title>{L['label']}: {e(L['title'])}</title><style>{CSS}{PRINT}</style></head><body><div class='wrap'>",
         f"<p class='k'>{C.COURSE_CODE} · Topic {L['topic']} · {L['label']} · {L['minutes']} min · {L['lo']} · {e(L['codes'])}</p><h1>{e(L['title'])}</h1><p class='meta'>{e(C.TITLE)} · Version {C.VERSION} · {C.VERSION_DATE}</p>",
         f"<p class='hook'>{e(L['hook'])}</p><h2>Your mission</h2><p>{e(L['scenario'])}</p>",
         "<h2>You will hand in</h2><ul>" + "".join(f"<li>{e(d)}</li>" for d in L["deliverables"]) + "</ul>",
         f"<p class='note'><b>Copy prompts in one click:</b> <a href='{C.PROMPTS_URL}#lab-{L['code']}'>{C.PROMPTS_URL}#lab-{L['code']}</a>, or open <code>prompts/index.html</code> in the course folder. It also works offline.</p>"]
    if L.get("tested"): p.append(f"<p class='note'><b>{e(L['tested'])}</b> Your numbers may differ: models change and results vary between runs. Record what you see.</p>")
    p += ["<h2>Before you start</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in L["prereq"]) + "</ul>",
          "<h2>What is in this folder</h2><table><tr><th>File</th><th>What it is</th></tr>" +
          "".join(f"<tr><td><code>data/{e(f)}</code></td><td>{e(DESCR.get(f, ''))}</td></tr>" for f in dfiles) +
          "".join(f"<tr><td><code>scripts/{e(f)}</code></td><td>{e(SDESCR.get(f, ''))}</td></tr>" for f in sfiles) + "</table>",
          "<p class='meta'>You do not write code. Your agent runs the scripts, and you read the result.</p><h2>Steps</h2>"]
    for i, st in enumerate(L["steps"], 1):
        p.append(f"<div class='step'><h3>{i}. {e(st['title'])}</h3>")
        if st.get("body"): p.append(f"<p>{e(st['body'])}</p>")
        if st.get("prompt"): p.append(f"<p class='k'>Prompt · paste into {e(st.get('where', 'Hermes Desktop'))}</p><pre>{e(st['prompt'])}</pre>")
        if st.get("expect"): p.append(f"<p class='exp'>✓ You should see: {e(st['expect'])}</p>")
        if st.get("shot"): p.append(f"<p class='shot'>📸 Screenshot for {e(L['shot'])}. Paste it into your Case Study paper as your answer.</p>")
        p.append("</div>")
    p += ["<h2>Check your work</h2><ul>" + "".join(f"<li>☐ {e(v)}</li>" for v in L["verify"]) + "</ul>", f"<div class='card'><b>Checkpoint:</b> {e(L['check'])}</div>",
          "<h2>If something goes wrong</h2><table><tr><th>What you see</th><th>What to do</th></tr>" + "".join(f"<tr><td>{e(a)}</td><td>{e(b)}</td></tr>" for a, b in L["trouble"]) + "</table>",
          f"<h2>Finished early?</h2><p>{e(L['challenge'])}</p><p class='foot'>{e(SYNTH)}<br>{e(FOOT)}</p></div></body></html>"]
    return "".join(p)

def to_pdf(txt, out):
    with tempfile.TemporaryDirectory() as td:
        src = os.path.join(td, "page.html"); open(src, "w", encoding="utf-8").write(txt)
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={out}", "file://" + src], check=True, capture_output=True)

def prompts_page():
    nav = "".join(f"<a href='#lab-{L['code']}'>{L['label']}</a>" for L in LABS)
    secs = []
    for L in LABS:
        rel = f"../labs/{L['slug']}"; blocks = []; n = 0
        for i, st in enumerate(L["steps"], 1):
            if st.get("prompt"):
                n += 1
                blocks.append(f"<div class='prompt'><header><div><b>Step {i}. {e(st['title'])}</b><span class='ptool'>Paste into {e(st.get('where', 'Hermes Desktop'))}</span></div><button class='copy' type='button' aria-label='Copy prompt for step {i}'>Copy</button></header>"
                              + (f"<p class='sb'>{e(st['body'])}</p>" if st.get("body") else "") + f"<pre>{e(st['prompt'])}</pre>" + (f"<p class='exp'>✓ {e(st['expect'])}</p>" if st.get("expect") else "") + "</div>")
            else:
                blocks.append(f"<div class='plain'><b>Step {i}. {e(st['title'])}</b><p>{e(st.get('body', ''))}</p>" + (f"<p class='exp'>✓ {e(st['expect'])}</p>" if st.get("expect") else "") + "</div>")
            if st.get("shot"): blocks.append(f"<p class='shot'>📸 Screenshot for {e(L['shot'])}: paste it into your Case Study paper.</p>")
        secs.append(f"<section class='lab' id='lab-{L['code']}'><p class='k'>{L['label']} · Topic {L['topic']} · {L['minutes']} min · {L['shot']}</p><h2>{e(L['title'])}</h2><p class='hook'>{e(L['hook'])}</p>"
                    f"<p class='files'><a href='{rel}/LAB-{L['code']}-Instructions.pdf'>Instructions PDF</a> · <a href='{rel}/data/'>Mock data</a> · <a href='{rel}/scripts/'>Scripts</a></p>" + "".join(blocks) +
                    f"<p class='check'><b>Checkpoint:</b> {e(L['check'])}</p><p><a href='#top'>Back to the top</a></p></section>")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lab Prompts | {e(C.TITLE)}</title><style>{CSS}
.wrap{{max-width:900px;padding:24px 16px 70px}}nav{{position:sticky;top:0;z-index:2;background:var(--bg);padding:10px 0;border-bottom:1px solid var(--rule);display:flex;gap:6px;flex-wrap:wrap}}
nav a{{padding:7px 14px;border:1.5px solid var(--rule);border-radius:22px;text-decoration:none;font-weight:600;color:var(--ink);background:#fff}}nav a:hover{{border-color:var(--acc)}}
.lab{{padding-top:26px;scroll-margin-top:50px}}.prompt{{background:var(--panel);border:1px solid var(--rule);border-left:4px solid var(--acc);border-radius:10px;margin:0 0 14px;overflow:hidden}}
.prompt header{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:10px 14px}}.ptool{{display:block;font-size:13px;color:var(--muted)}}.prompt pre{{margin:0 14px 12px}}.prompt .exp,.sb{{margin:0 14px 12px;font-size:14.5px}}
.plain{{background:#fff;border:1px solid var(--rule);border-radius:10px;padding:10px 14px;margin:0 0 14px}}.plain p{{margin:5px 0;font-size:14.5px}}
.copy{{font:inherit;font-weight:700;padding:9px 20px;min-height:42px;border:0;border-radius:8px;background:var(--acc);color:#fff;cursor:pointer;flex:none}}.copy:hover{{background:#A94F31}}.copy:focus-visible{{outline:3px solid #21201C;outline-offset:2px}}.copy.done{{background:#3A7D7B}}
.shot{{margin:-6px 0 14px}}.check{{background:#21201C;color:#E8E5DE;padding:10px 14px;border-radius:10px}}.intro{{margin:18px 0;padding:14px 18px;border:2px dashed var(--acc);border-radius:12px;background:#fff}}
#status{{position:fixed;bottom:16px;right:16px;background:#21201C;color:#fff;padding:8px 14px;border-radius:8px;opacity:0;transition:opacity .2s}}#status.on{{opacity:1}}
@media(max-width:600px){{nav{{flex-wrap:nowrap;overflow:auto}}nav a{{flex:none}}h1{{font-size:26px}}pre{{font-size:12.5px}}.prompt header{{align-items:flex-start}}}}
</style></head><body><main class="wrap" id="top">
<p class="k">{C.COURSE_CODE} · Version {C.VERSION}</p><h1>Lab Prompts: Copy, Paste, Attack, Fix</h1>
<p class="meta">{e(C.TITLE)}. You run six labs on {e(C.SCENARIO)}. Press <b>Copy</b>, paste into the place named, then read what comes back. This page also works offline: open <code>prompts/index.html</code> from the downloaded course folder.</p>
<div class="intro"><b>Get the lab folders first.</b> <a href="{C.REPO_URL}/archive/refs/heads/master.zip">Download the course ZIP</a> and unzip it. Each folder under <code>labs/</code> holds mock data, scripts and a PDF of instructions. In Hermes Desktop, attach the lab's folder with <b>+ → Folder…</b> in every new session.<br><b>Your answers are screenshots.</b> Look for 📸 and paste each one into your Case Study paper: Lab 1 for Q1, Labs 2 to 4 for Q2, Labs 5 and 6 for Q3.</div>
<nav aria-label="Labs">{nav}</nav>{''.join(secs)}
<p class="foot">{e(SYNTH)}<br>{e(FOOT)}</p></main><div id="status" role="status" aria-live="polite"></div>
<script>
function flash(m){{var s=document.getElementById('status');s.textContent=m;s.classList.add('on');setTimeout(function(){{s.classList.remove('on')}},1400)}}
function fb(t){{var a=document.createElement('textarea');a.value=t;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();var ok=false;try{{ok=document.execCommand('copy')}}catch(e){{}}a.remove();return ok}}
document.querySelectorAll('.copy').forEach(function(b){{b.addEventListener('click',function(){{var t=b.closest('.prompt').querySelector('pre').textContent;
var done=function(){{b.textContent='Copied';b.classList.add('done');flash('Copied. Now paste it.');setTimeout(function(){{b.textContent='Copy';b.classList.remove('done')}},1500)}};
var bad=function(){{flash('Copy blocked: select the text and copy it by hand')}};
if(navigator.clipboard&&window.isSecureContext){{navigator.clipboard.writeText(t).then(done,function(){{fb(t)?done():bad()}})}}else{{fb(t)?done():bad()}}}})}});
</script></body></html>"""

ROOT_INDEX = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta http-equiv="refresh" content="0; url=prompts/index.html"><title>{e(C.TITLE)}</title></head><body><p><a href="prompts/index.html">Open the Lab Prompts page</a></p></body></html>"""

def main(pdf=True):
    labs = os.path.join(REPO, "labs"); os.makedirs(labs, exist_ok=True)
    for L in LABS:
        d = os.path.join(labs, L["slug"]); os.makedirs(os.path.join(d, "data"), exist_ok=True); os.makedirs(os.path.join(d, "scripts"), exist_ok=True); os.makedirs(os.path.join(d, "outputs"), exist_ok=True)
        open(os.path.join(d, "outputs", ".gitkeep"), "w").close()
        for rel, txt in M.ALL[L["num"]]().items():
            open(os.path.join(d, rel), "w", encoding="utf-8", newline="").write(txt)
        if L["num"] == 2: M.preorders_xlsx(os.path.join(d, "data", "pre-orders.xlsx"))
        for f in os.listdir(os.path.join(HERE, "lab_scripts", f"lab{L['num']}")):
            if f.endswith(".py"):
                dst = os.path.join(d, "scripts", f); shutil.copyfile(os.path.join(HERE, "lab_scripts", f"lab{L['num']}", f), dst)
                os.chmod(dst, os.stat(dst).st_mode | stat.S_IXUSR)
        if pdf:
            to_pdf(lab_html(L, sorted(x for x in os.listdir(os.path.join(d, "data")) if not x.startswith(".")), sorted(x for x in os.listdir(os.path.join(d, "scripts")) if x.endswith(".py"))), os.path.join(d, f"LAB-{L['code']}-Instructions.pdf"))
        print("built", L["slug"])
    os.makedirs(os.path.join(REPO, "prompts"), exist_ok=True)
    open(os.path.join(REPO, "prompts", "index.html"), "w", encoding="utf-8").write(prompts_page())
    open(os.path.join(REPO, "index.html"), "w", encoding="utf-8").write(ROOT_INDEX)
    print("built prompts/index.html")

if __name__ == "__main__":
    main(pdf="--no-pdf" not in sys.argv)
