# -*- coding: utf-8 -*-
"""마크다운(방법3 문서) → HWPX. 기존 결정기준.hwpx의 header.xml(스타일)을 틀로 쓰고 section0.xml만 생성한다."""
import re, sys, zipfile, pathlib, html, io
from xml.etree import ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE.parent.parent / "AI-Ready_방법1_제안자선언형" / "4_보고서용" / "스키마와_참조구현_결정기준.hwpx"
_Z = zipfile.ZipFile(TEMPLATE)
class _RefFile:
    def __init__(self, rel): self.rel = rel
    def read_bytes(self): return _Z.read(self.rel)
    def read_text(self, encoding="utf-8"): return _Z.read(self.rel).decode(encoding)
class _Ref:
    def __truediv__(self, rel): return _RefFile(rel)
REF = _Ref()
SEC_HEAD = (REF / "Contents/section0.xml").read_text(encoding="utf-8")
SEC_NS = SEC_HEAD[:SEC_HEAD.index("<hp:p ")]                   # <?xml …><hs:sec …>
FIRST_P = SEC_HEAD[SEC_HEAD.index("<hp:p "):SEC_HEAD.index("</hp:p>") + 7]
SECPR_RUN = FIRST_P[FIRST_P.index("<hp:run charPrIDRef=\"1\"><hp:secPr"):FIRST_P.index("</hp:run>") + 9]

WIDTH = 49860
# charPr: 제목 32, h1 33, h2 38, h3 34(bold), 본문 1, 굵게 34, 인용 31, 인용굵게 34, 코드 39, 표머리 35(흰), 표본문 37, 표굵게 36, 표코드 39
C = dict(title=32, h1=33, h2=38, h3=34, body=1, bold=34, quote=31, qbold=34, code=39, th=35, td=37, tdb=36, small=15)
# paraPr: 본문 36(양쪽), 제목 38, 소제목 41, 인용 44, 목록 45, 코드 37, 표머리 39, 표본문 40, 표 컨테이너 23, 센터 35
P = dict(body=36, h=38, h3=41, quote=44, list=45, code=37, th=39, td=40, tbl=23, center=35)

VER = {"1": "V.2", "2": "V.1", "3": "V.2.1"}
def rename(s):
    s = re.sub(r"(?<![_\w])(?:AI-Ready (?:표준화 )?)?방법 ?([123])(?![\d_])", lambda m: f"AI Ready Data {VER[m.group(1)]}", s)
    s = s.replace("제안자 선언형 정합본", "제안자 선언형").replace(" (정합본)", "").replace("(정합본)", "")
    s = s.replace("정합본이다", "판이다").replace("정합본으로", "판으로").replace("정합본", "판")
    s = re.sub(r"V\.2(?!\.)과", "V.2와", s); s = re.sub(r"V\.2(?!\.)은", "V.2는", s); s = re.sub(r"V\.2(?!\.)을", "V.2를", s)
    return s

def esc(t): return html.escape(t, quote=False)

_tid = [1000]
def tid():
    _tid[0] += 1; return str(_tid[0])

# ── 인라인: **굵게**, `코드`, [텍스트](링크), *기울임*(무시)
def runs(text, base, bold, code):
    out = []
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    for part in re.split(r"(\*\*.+?\*\*|`[^`]+`)", text):
        if not part: continue
        if part.startswith("**") and part.endswith("**"): out.append((part[2:-2], bold))
        elif part.startswith("`") and part.endswith("`"): out.append((part[1:-1], code))
        else: out.append((part.replace("**", ""), base))
    return out

def p_xml(run_list, para, charsize=1815, first=None):
    rs = "".join(f'<hp:run charPrIDRef="{c}"><hp:t>{esc(t)}</hp:t></hp:run>' for t, c in run_list if t) or '<hp:run charPrIDRef="1"/>'
    pre = first or ""
    return (f'<hp:p id="0" paraPrIDRef="{para}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">{pre}{rs}'
            f'<hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="{charsize}" textheight="{charsize}" baseline="{int(charsize*0.745)}" spacing="600" horzpos="0" horzsize="{WIDTH}" flags="393216"/></hp:linesegarray></hp:p>')

def cell_paras(text, header):
    paras = []
    for line in re.split(r"<br\s*/?>", text):
        line = line.strip()
        if header: paras.append(p_xml(runs(line, C["th"], C["th"], C["th"]), P["th"]))
        else: paras.append(p_xml(runs(line, C["td"], C["tdb"], C["code"]), P["td"], 1643))
    return "".join(paras) or p_xml([], P["td"], 1643)

def table_xml(rows):
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    # 열 너비: 열별 최대 글자 수에 비례(최소 7%, 최대 55%)
    lens = [max(len(re.sub(r"<br\s*/?>|\*\*|`", "", r[i])) for r in rows) for i in range(ncol)]
    lens = [max(l, 2) for l in lens]
    w = [min(max(l / sum(lens), 0.07), 0.55) for l in lens]
    w = [x / sum(w) for x in w]
    widths = [int(WIDTH * x) for x in w]; widths[-1] = WIDTH - sum(widths[:-1])
    trs = []
    for ri, row in enumerate(rows):
        tcs = []
        for ci, cell in enumerate(row):
            bf = 7 if ri == 0 else 6
            tcs.append(f'<hp:tc name="" header="{1 if ri == 0 else 0}" hasMargin="0" protect="0" editable="0" dirty="0" borderFillIDRef="{bf}">'
                       f'<hp:subList id="" textDirection="HORIZONTAL" lineWrap="BREAK" vertAlign="TOP" linkListIDRef="0" linkListNextIDRef="0" textWidth="0" textHeight="0" hasTextRef="0" hasNumRef="0">'
                       f'{cell_paras(cell, ri == 0)}</hp:subList><hp:cellAddr colAddr="{ci}" rowAddr="{ri}"/><hp:cellSpan colSpan="1" rowSpan="1"/>'
                       f'<hp:cellSz width="{widths[ci]}" height="0"/><hp:cellMargin left="510" right="510" top="141" bottom="141"/></hp:tc>')
        trs.append("<hp:tr>" + "".join(tcs) + "</hp:tr>")
    tbl = (f'<hp:tbl id="{tid()}" zOrder="0" numberingType="TABLE" textWrap="TOP_AND_BOTTOM" textFlow="BOTH_SIDES" lock="0" dropcapstyle="None" pageBreak="CELL" repeatHeader="1" rowCnt="{len(rows)}" colCnt="{ncol}" cellSpacing="0" borderFillIDRef="6" noAdjust="0">'
           f'<hp:sz width="{WIDTH}" widthRelTo="ABSOLUTE" height="{2200*len(rows)}" heightRelTo="ABSOLUTE" protect="0"/>'
           f'<hp:pos treatAsChar="0" affectLSpacing="0" flowWithText="1" allowOverlap="0" holdAnchorAndSO="0" vertRelTo="PARA" horzRelTo="COLUMN" vertAlign="TOP" horzAlign="CENTER" vertOffset="0" horzOffset="0"/>'
           f'<hp:outMargin left="0" right="0" top="0" bottom="0"/><hp:inMargin left="540" right="540" top="0" bottom="0"/>{"".join(trs)}</hp:tbl>')
    return (f'<hp:p id="0" paraPrIDRef="{P["tbl"]}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0"><hp:run charPrIDRef="1">{tbl}</hp:run>'
            f'<hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="1815" textheight="1815" baseline="1352" spacing="600" horzpos="0" horzsize="{WIDTH}" flags="393216"/></hp:linesegarray></hp:p>')

def split_row(line):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    return cells

def convert(md_text, doc_title=None):
    md_text = rename(md_text)
    lines = md_text.split("\n")
    body = []; preview = []
    title = None
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s or s == "---":
            i += 1; continue
        # 코드 블록
        if s.startswith("```"):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                body.append(p_xml([(lines[i], C["code"])], P["code"], 1500)); preview.append(lines[i]); i += 1
            i += 1; continue
        # 표
        if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\|\s*:?-+", lines[i + 1].strip()):
            rows = [split_row(s)]; i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(split_row(lines[i].strip())); i += 1
            body.append(table_xml(rows)); preview.extend(" | ".join(r) for r in rows); continue
        # 인용 블록
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                t = lines[i].strip()[1:].strip()
                if t.startswith("|"):   # 인용 안의 표는 표로
                    if buf: body.append(p_xml(runs(" ".join(buf), C["quote"], C["qbold"], C["code"]), P["quote"], 1700)); preview.append(" ".join(buf)); buf = []
                    rows = []
                    while i < len(lines) and lines[i].strip().startswith(">") and lines[i].strip()[1:].strip().startswith("|"):
                        r = lines[i].strip()[1:].strip()
                        if not re.match(r"^\|\s*:?-+", r): rows.append(split_row(r))
                        i += 1
                    body.append(table_xml(rows)); continue
                if t == "":
                    if buf: body.append(p_xml(runs(" ".join(buf), C["quote"], C["qbold"], C["code"]), P["quote"], 1700)); preview.append(" ".join(buf)); buf = []
                else: buf.append(t)
                i += 1
            if buf: body.append(p_xml(runs(" ".join(buf), C["quote"], C["qbold"], C["code"]), P["quote"], 1700)); preview.append(" ".join(buf))
            continue
        # 제목
        m = re.match(r"^(#{1,4})\s+(.*)$", s)
        if m:
            lvl, t = len(m.group(1)), m.group(2).strip()
            if lvl == 1 and title is None:
                title = t; i += 1; continue
            if lvl == 1: body.append(p_xml([(t, C["h1"])], P["h"], 2335))
            elif lvl == 2: body.append(p_xml([(t, C["h2"])], P["h"], 2000))
            else: body.append(p_xml(runs(t, C["h3"], C["h3"], C["code"]), P["h3"]))
            preview.append(t); i += 1; continue
        # 목록
        m = re.match(r"^(\s*)([-*]|\d+[.)])\s+(.*)$", ln)
        if m:
            mark = "• " if m.group(2) in "-*" else m.group(2) + " "
            body.append(p_xml([(mark, C["body"])] + runs(m.group(3), C["body"], C["bold"], C["code"]), P["list"])); preview.append(mark + m.group(3)); i += 1; continue
        # 일반 단락 (연속 줄 병합; <br>는 단락 분리)
        buf = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r"^(#{1,4}\s|>|\||```|---|\s*([-*]|\d+[.)])\s)", lines[i]):
            buf.append(lines[i].strip()); i += 1
        for seg in re.split(r"<br\s*/?>", " ".join(buf)):
            if seg.strip():
                body.append(p_xml(runs(seg.strip(), C["body"], C["bold"], C["code"]), P["body"])); preview.append(seg.strip())
    title = doc_title or title or "문서"
    first = (f'<hp:p id="3121190098" paraPrIDRef="{P["center"]}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">{SECPR_RUN}'
             f'<hp:run charPrIDRef="1"/><hp:run charPrIDRef="{C["title"]}"><hp:t>{esc(title)}</hp:t></hp:run>'
             f'<hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="3114" textheight="3114" baseline="2319" spacing="2024" horzpos="0" horzsize="{WIDTH}" flags="393216"/></hp:linesegarray></hp:p>')
    sec = SEC_NS + first + "".join(body) + "</hs:sec>"
    return sec, title, "\n".join([title] + preview)[:4000]

def write_hwpx(sec_xml, prv_text, out_path):
    ET.fromstring(sec_xml.encode("utf-8"))  # 정형성 검사
    with zipfile.ZipFile(out_path, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), (REF / "mimetype").read_bytes(), compress_type=zipfile.ZIP_STORED)
        for rel in ["version.xml", "settings.xml", "META-INF/container.xml", "META-INF/container.rdf", "META-INF/manifest.xml",
                    "Contents/content.hpf", "Contents/header.xml", "Preview/PrvImage.png"]:
            z.writestr(rel, (REF / rel).read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/section0.xml", sec_xml.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Preview/PrvText.txt", prv_text.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)

if __name__ == "__main__":
    src, dst = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
    title = sys.argv[3] if len(sys.argv) > 3 else None
    sec, t, prv = convert(src.read_text(encoding="utf-8"), title)
    write_hwpx(sec, prv, dst)
    print(f"{dst.name}  ← {src.name}  [{t}]  {dst.stat().st_size//1024} KB")
