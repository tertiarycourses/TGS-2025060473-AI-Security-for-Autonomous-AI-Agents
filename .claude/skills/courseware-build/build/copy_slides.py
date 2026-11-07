"""Copy slides verbatim from another deck built on the same ccdeck design (owner request, 7 Nov 2026:
Topic 1 reuses the Human-AI Workforce deck). Images are re-added as parts of this deck, external links and
online videos are re-related, notes and timing are carried over. Only identity text is rewritten (course code,
title, page number, instrument name), as the courseware gate requires."""
import copy, io, re
from lxml import etree
from pptx.oxml.ns import qn

RNS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"

def _fix_text(root, subs):
    for t in root.iter(qn("a:t")):
        if t.text:
            new = t.text
            for a, b in subs: new = new.replace(a, b)
            t.text = new

def copy_slide(D, src_slide, subs, link_subs, page_fix=True):
    s = D.new(dark=False)
    dst = s.part
    # map relationships
    rmap = {}
    for rId, rel in src_slide.part.rels.items():
        rt = rel.reltype
        if rt.endswith("/slideLayout") or rt.endswith("/notesSlide"):
            continue
        if rel.is_external:
            target = rel.target_ref
            for a, b in link_subs: target = target.replace(a, b)
            rmap[rId] = dst.relate_to(target, rt, is_external=True)
        elif rt.endswith("/image"):
            _, new_rId = dst.get_or_add_image_part(io.BytesIO(rel.target_part.blob))
            rmap[rId] = new_rId
        else:
            raise RuntimeError(f"unsupported relationship {rt}")
    # replace the whole slide body (background + shapes), timing and transition
    sld = s.element
    for tag in ("p:cSld", "p:timing", "p:transition"):
        old = sld.find(qn(tag))
        if old is not None: sld.remove(old)
    src = src_slide.element
    csld = copy.deepcopy(src.find(qn("p:cSld")))
    clr = sld.find(qn("p:clrMapOvr"))
    if clr is not None: clr.addprevious(csld)
    else: sld.insert(0, csld)
    for tag in ("p:transition", "p:timing"):
        el = src.find(qn(tag))
        if el is not None: sld.append(copy.deepcopy(el))
    for el in sld.iter():
        for k, v in list(el.attrib.items()):
            if k.startswith("{%s}" % RNS) and v in rmap:
                el.set(k, rmap[v])
    _fix_text(sld, subs)
    if page_fix:  # footer page number: a bare number at the bottom right
        for sp in s.shapes:
            if sp.has_text_frame and sp.text_frame.text.strip().isdigit() and sp.top and sp.top > 6.9 * 914400 and sp.left > 11.5 * 914400:
                runs = [r for p in sp.text_frame.paragraphs for r in p.runs]
                if runs: runs[0].text = str(D.n); [setattr(r, "text", "") for r in runs[1:]]
    if src_slide.has_notes_slide:
        note = src_slide.notes_slide.notes_text_frame.text
        for a, b in subs: note = note.replace(a, b)
        s.notes_slide.notes_text_frame.text = note
    return s
