# -*- coding: utf-8 -*-
"""운영요령·작성지침 원문에 AI Ready Data V.2.1 개정안을 반영한 통합본(개정 전문) HWPX 생성.
   신설·추가 문안은 붉은 글씨. 원문은 PDF(pdftotext -raw/-layout)에서 추출한다."""
import re, sys, subprocess, pathlib, zipfile, html, importlib.util
from xml.etree import ElementTree as ET

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE.parent
spec = importlib.util.spec_from_file_location("md2hwpx", HERE / "md2hwpx.py"); m2h = importlib.util.module_from_spec(spec); spec.loader.exec_module(m2h)
esc = m2h.esc
WIDTH = m2h.WIDTH

# ── 붉은 글자 charPr 추가 (43 본문, 44 굵게, 45 표, 46 표굵게, 47 제목1, 48 제목2)
RED = dict(body=43, bold=44, td=45, tdb=46, h1=47, h2=48)
def red_header():
    h = (m2h.REF / "Contents/header.xml").read_text()
    def clone(src_id, new_id):
        m = re.search(r'<hh:charPr id="%s" .*?</hh:charPr>' % src_id, h, flags=re.S)
        x = m.group(0).replace(f'id="{src_id}"', f'id="{new_id}"', 1)
        return re.sub(r'textColor="#[0-9A-Fa-f]{6}"', 'textColor="#C00000"', x, count=1)
    add = clone(1, 43) + clone(34, 44) + clone(37, 45) + clone(36, 46) + clone(33, 47) + clone(38, 48)
    h = h.replace("</hh:charProperties>", add + "</hh:charProperties>", 1)
    h = re.sub(r'<hh:charProperties itemCnt="\d+"', '<hh:charProperties itemCnt="49"', h, count=1)
    return h

def _fix(s, table):
    for k, v in table.items(): s = s.replace(k, v)
    return s

def pdftext(pdf, first, last, mode="-raw"):
    return subprocess.run(["pdftotext", "-enc", "UTF-8", mode, "-f", str(first), "-l", str(last), str(pdf), "-"],
                          capture_output=True, check=True).stdout.decode("utf-8").replace(chr(12), chr(10))

# ── 단락 생성 도우미
P, C = m2h.P, m2h.C
def para(text, pp=P["body"], red=False, bold=False, size=1815):
    c = (RED["bold"] if bold else RED["body"]) if red else (C["bold"] if bold else C["body"])
    return m2h.p_xml([(text, c)], pp, size)
def mixed(parts, pp=P["body"]):
    """parts: [(text, red?, bold?)]"""
    rl = []
    for t, r, b in parts:
        rl.append((t, (RED["bold"] if b else RED["body"]) if r else (C["bold"] if b else C["body"])))
    return m2h.p_xml(rl, pp)
def heading(text, level=1, red=False):
    if level == 1: return m2h.p_xml([(text, RED["h1"] if red else C["h1"])], P["h"], 2335)
    return m2h.p_xml([(text, RED["h2"] if red else C["h2"])], P["h"], 2000)
def note(text):
    return m2h.p_xml(m2h.runs(text, C["quote"], C["qbold"], C["code"]), P["quote"], 1700)
def table(rows, red_rows=()):
    """rows[0]=머리. red_rows: 붉게 칠할 행 인덱스(1부터)."""
    xml = m2h.table_xml(rows)
    if red_rows:
        trs = re.findall(r"<hp:tr>.*?</hp:tr>", xml, flags=re.S)
        for i in red_rows:
            tr = trs[i]
            tr2 = tr.replace(f'charPrIDRef="{C["td"]}"', f'charPrIDRef="{RED["td"]}"').replace(f'charPrIDRef="{C["tdb"]}"', f'charPrIDRef="{RED["tdb"]}"')
            xml = xml.replace(tr, tr2, 1)
    return xml

# md 본문을 전부 붉은 글씨로 렌더링(신설 별표·별지 실물)
def md_body_red(md_path, drop_quotes=False):
    saved = dict(C)
    C.update(body=RED["body"], bold=RED["bold"], quote=RED["body"], qbold=RED["bold"], td=RED["td"], tdb=RED["tdb"], h1=RED["h1"], h2=RED["h2"], h3=RED["bold"], th=C["th"])
    txt = md_path.read_text(encoding="utf-8")
    if drop_quotes: txt = "\n".join(l for l in txt.split("\n") if not l.lstrip().startswith(">"))
    sec, title, _ = m2h.convert(txt)
    C.clear(); C.update(saved)
    i = sec.index("</hp:p>") + 7
    return title, sec[i:sec.rindex("</hs:sec>")]

# ══════════════════════════════════════════════════════════════════════════
# 1. 운영요령 통합본
# ══════════════════════════════════════════════════════════════════════════
def build_yoryeong():
    pdf = ROOT / "정보통신표준화 운영요령.pdf"
    raw = pdftext(pdf, 1, 14)
    lines = [l.rstrip() for l in raw.split("\n") if l.strip() and not l.startswith("SBG-0030/R13")]
    # 토큰 말뭉치(줄 잇기 판단용)
    corpus = set()
    for txt in (raw, pdftext(ROOT / "정보통신표준화 운영규정.pdf", 1, 30), pdftext(ROOT / "[TTA]정보통신단체표준 작성지침(TTAR-09.0040R1).pdf", 1, 44, "-layout")):
        corpus.update(re.split(r"\s+", txt))
    START = re.compile(r"^(제\d+조(의\d+)?\s?\(|제\d+장\s|제\d+절\s|[①-⑮]|\d{1,2}\.\s|[가-힣]\.\s|부칙$|\(기관장|제정 :|개정 :)")
    paras = []
    for ln in lines:
        if START.match(ln) or not paras:
            paras.append(ln); continue
        prev = paras[-1]
        a = prev.split(" ")[-1]; b = ln.split(" ")[0]
        joined = a + b
        glue = ""
        if prev.endswith(("다.", "다", ".", ")", "」", "”", ",")) or a in corpus and b in corpus:
            glue = " "
        if joined in corpus or any(t.startswith(joined) for t in corpus if len(t) <= len(joined) + 3):
            glue = ""
        elif a in corpus and b in corpus: glue = " "
        else: glue = " "
        if prev.endswith("「") or ln.startswith(("」", ")", "」")): glue = ""
        paras[-1] = prev + glue + ln
    # PDF 줄바꿈이 낱말 가운데를 가른 곳 — 원문 대조로 확인한 교정 목록
    FIX = {"충족하였 는지": "충족하였는지", "있 다고": "있다고", "전문위원 회의": "전문위원회의", "프로젝트조정위 원회": "프로젝트조정위원회",
           "제23조제1항제2 호": "제23조제1항제2호", "신 설되는": "신설되는", "정상적 인": "정상적인", "제 5호까지": "제5호까지", "합동실무 반의": "합동실무반의",
           "이 해관계인": "이해관계인", "이루어 지지": "이루어지지", "선정 하여야": "선정하여야", "폐지하 지": "폐지하지", "유지 할": "유지할",
           "참조 하여": "참조하여", "제·개 정일": "제·개정일", "작성 지침」": "작성지침」", "제40조 제3항제2호": "제40조제3항제2호", "제20호서식 의": "제20호서식의",
           "제14조제2항 에": "제14조제2항에", "국가 표준으로": "국가표준으로", "제24조 까지": "제24조까지", "추가 적인": "추가적인", "관리 방안을": "관리방안을",
           "제 15조부터": "제15조부터", "국민 들은": "국민들은", "용어 표준화가": "용어표준화가", "데이 터베이스": "데이터베이스", "기반으로「": "기반으로 「"}
    paras = [_fix(p, FIX) for p in paras]
    # 머리(제목·개정 이력) 분리
    head_end = next(i for i, p in enumerate(paras) if p.startswith("제1장"))
    header, body = paras[:head_end], paras[head_end:]

    # ── 개정 내용 삽입
    A = []  # (조건함수, 삽입 단락 리스트[(text, level)], 위치 'after' | 'append')
    def after(pred, items): A.append((pred, items, "after"))
    def append_to(pred, text): A.append((pred, text, "append"))
    after(lambda p: p.startswith("5. “표준용어”라 함은"), [
        ("6. “AI-Ready 표준”이란 데이터의 의미·구조·출처·품질·이용조건을 사람과 기계가 함께 읽을 수 있도록, 데이터 요소를 전역 어휘 식별자(IRI)에 매핑하고 기계가독 형식으로 기술한 표준을 말한다.", "ho"),
        ("7. “AI-Ready 적용 대상”이란 데이터의 의미, 구조, 값, 품질 중 어느 하나 이상을 기술하는 표준을 말한다. 다만, 기술규격(제19조제1항제2호에 따라 앞표지와 원문으로 구성되는 것을 말한다)은 제외한다. 기능·통신 절차·인터페이스를 규정하는 표준은 이에 해당하지 아니하며, 적용 대상 여부는 그 표준이 기술하는 내용으로 판정한다.", "ho"),
        ("8. “기계가독 산출물”이란 표준이 정의하는 데이터 요소를 기계가 처리할 수 있는 형식(JSON Schema, XML Schema, RDF 어휘, JSON-LD @context 등)으로 기술한 것을 말한다. 기계가독 산출물은 표준의 규범 내용이다.", "ho"),
        ("9. “참조구현”이란 기계가독 산출물을 이용하는 프로그램 코드로서, 표준의 이해와 구현을 돕기 위하여 선택적으로 공개하는 것을 말한다. 참조구현은 표준의 일부가 아니다.", "ho")])
    after(lambda p: p.startswith("④ 개인 또는 중소기업이"), [
        ("⑤ 제1항에 따라 별지 제11호서식의 제안서를 제출하는 경우로서 AI-Ready 적용 대상 표준의 제정 또는 개정을 제안하는 때에는, 제안자는 별지 제11-1호서식의 기계가독 산출물 선언서를 함께 첨부한다. 선언서에는 다음 각 호를 기재한다.", "hang"),
        ("1. 규범적으로 사용하는 외부 어휘와 그 전역 어휘 식별자(IRI)", "ho"), ("2. 제공하려는 기계가독 산출물의 형식과 목표 수준", "ho"),
        ("3. 외부 저장소에 공개하려는 경우 그 위치", "ho"), ("4. 기계가독 산출물의 이용조건(라이선스)", "ho"), ("5. 참조구현을 공개하려는 경우 그 위치", "ho")])
    append_to(lambda p: p.startswith("② 제1항에 따라 선정된 기술위원회등의 의장은"), " 이때 제안된 과제의 AI-Ready 적용 대상 여부와 제13조제5항에 따른 선언 내용의 타당성을 확인하여 검토결과서(별지 제15호서식)에 기재한다.")
    after(lambda p: p.startswith("8. 다른 표준화기구에서 표준으로 완료되지 않고"), [
        ("9. AI-Ready 적용 대상 표준의 표준초안은 데이터 요소를 정규 컬럼표로 정의하고, 요소와 전역 어휘 식별자의 매핑을 포함하여 작성한다. 규범적으로 사용하는 외부 어휘·스키마는 인용 표준에 등재한다. 구체적인 작성 방법은 「정보통신단체표준 작성지침」에 따른다.", "ho")])
    after(lambda p: p.startswith("④ 에디터는 프로젝트그룹등에서 합의된 사항을"), [
        ("제19조의3(기계가독 산출물의 제출·제공·보관 및 점검) ① 에디터는 AI-Ready 적용 대상 표준의 기계가독 산출물을 표준초안과 함께 사무국에 제출한다. 이 경우 제13조제5항에 따른 선언 내용에 따른다.", "jo"),
        ("② 기계가독 산출물은 표준초안의 부속서로 수록하고, 사무국은 이를 표준과 함께 별도의 파일로 제공한다. 부속서 수록본과 제공 파일의 내용이 다른 경우에는 부속서 수록본에 따른다.", "hang"),
        ("③ 다음 각 호의 어느 하나에 해당하는 경우에는 제2항의 수록을 부속서의 규범적 참조 명세로 갈음할 수 있다.", "hang"),
        ("1. 산출물의 분량이 많아 문서에 수록하기 곤란한 경우", "ho"), ("2. 산출물이 표준 문서와 다른 주기로 개정되는 경우", "ho"), ("3. 산출물이 다른 파일을 인용·포함하여 단일 파일로 완결되지 아니하는 경우", "ho"),
        ("④ 제3항의 규범적 참조 명세에는 다음 각 호를 기재한다.", "hang"),
        ("1. 공개 위치", "ho"), ("2. 판 또는 버전", "ho"), ("3. 무결성 확인 값", "ho"), ("4. 이용조건", "ho"), ("5. 협회 보관본의 위치", "ho"),
        ("⑤ 제안자 또는 에디터는 기계가독 산출물을 외부 저장소에 공개할 수 있다.", "hang"),
        ("⑥ 사무국은 표준 채택 시점의 기계가독 산출물 사본을 보관하고, 표준과 함께 공개한다. 보관본과 외부 공개본의 내용이 다른 경우에는 보관본에 따른다.", "hang"),
        ("⑦ 에디터는 기계가독 산출물에 이용조건을 명시하여야 한다. 이용조건은 그 산출물을 복제·배포·개작할 수 있는지를 이용자가 파일 자체에서 확인할 수 있도록 표시한다. 부속서에 수록한 경우에도 같다.", "hang"),
        ("⑧ 참조구현을 공개하는 경우 그 위치를 표준초안의 부록에 기재할 수 있다. 참조구현은 표준의 일부가 아니며, 협회는 그 내용에 대하여 보증하지 아니한다.", "hang"),
        ("⑨ 사무국은 제1항에 따라 제출된 기계가독 산출물에 대하여 형식 정합성(구문 유효성, 요소 정의표와의 일치, 인용 어휘 식별자의 해석 가능 여부)을 전자적 방법으로 점검할 수 있다.", "hang"),
        ("⑩ 기계가독 산출물은 표준초안의 일부로 보아 제19조제1항제1호에 따른 지식재산권 확인 대상에 포함한다. 제5항에 따라 외부 저장소에 공개하는 경우에도 같다.", "hang")])
    after(lambda p: p.startswith("④ 기술위원회등 의장은 부결되어 재논의된"), [
        ("⑤ AI-Ready 적용 대상 표준안을 상정하는 경우, 기술위원회등 의장은 별표 10의 기준에 따른 AI-Ready 자가점검표(별지 제21-1호서식)를 함께 제출한다. 자가점검표에는 제13조제5항의 선언 내용과 제19조의3에 따라 제출된 산출물의 일치 여부를 포함한다.", "hang")])
    after(lambda p: p.startswith("⑤ 제2항의 검토 결과, 표준을 개정 또는 폐지하기로"), [
        ("⑥ 제1항에 따른 유지보수 시, AI-Ready 적용 대상 표준은 다음 각 호를 함께 확인하여 검토결과서(별지 제23호서식 또는 별지 제24호서식)에 기재한다.", "hang"),
        ("1. 별표 10의 기준에 따른 AI-Ready 자가점검 결과", "ho"),
        ("2. 제19조의3제3항에 따른 규범적 참조가 있는 경우, 그 공개 위치의 접근 가능 여부 및 보관본과의 일치 여부", "ho")])
    NEW_BUCHIK = [("부칙 〈AI-Ready 표준 지원 개정〉", "buchik"),
                  ("제1조(시행일) 이 운영요령은 공포한 날부터 시행한다.", "jo"),
                  ("제2조(적용례) ① 제2조·제13조·제15조·제19조·제19조의3·제21조와 별표 10·별지 제11-1호서식·제15호서식·제21-1호서식의 개정 규정은 이 운영요령 시행 후 최초로 제안하는 표준화과제부터 적용한다.", "jo"),
                  ("② 이 운영요령 시행 당시 이미 공고된 표준에 대해서는 제26조제6항과 별지 제23호서식·제24호서식의 개정 규정을 그 표준의 다음 유지보수 시부터 적용한다.", "hang")]

    PP = {"jo": P["body"], "hang": 42, "ho": 11, "mok": 12, "buchik": P["h"]}
    def level_of(p):
        if re.match(r"^제\d+조", p): return "jo"
        if re.match(r"^[①-⑮]", p): return "hang"
        if re.match(r"^\d{1,2}\. ", p): return "ho"
        if re.match(r"^[가-힣]\. ", p): return "mok"
        return "jo"
    out = []
    # 표제
    out.append(heading("정보통신표준화 운영요령 (AI-Ready 개정 전문)", 1))
    out.append(note("원문 SBG-0030/R13(2025. 6. 13. 시행)에 AI Ready Data V.2.1 개정(안)을 반영한 통합본이다. **붉은 글씨가 신설·추가되는 문안**이고, 검은 글씨는 현행과 같다. 삭제되는 현행 문안은 없다. 원문은 PDF에서 추출한 것이므로 의결 전 원본과 최종 대조가 필요하다."))
    for h in header[1:]:
        out.append(para(h, 37, size=1500))
    out.append(para("개정(안) : 공포일 (AI-Ready 표준 지원)", 37, red=True, size=1500))
    buchik_done = False
    for p in body:
        if p == "부칙" and not buchik_done:
            for t, lv in NEW_BUCHIK: out.append(para(t, PP[lv], red=True) if lv != "buchik" else heading(t, 2, red=True))
            buchik_done = True
        if re.match(r"^제\d+장\s", p): out.append(heading(p, 1)); continue
        if re.match(r"^제\d+절\s", p): out.append(heading(p, 2)); continue
        if p == "부칙": out.append(heading("부칙", 2)); continue
        appended = next((t for pred, t, mode in A if mode == "append" and pred(p)), None)
        if appended: out.append(mixed([(p, False, False), (appended, True, False)], PP[level_of(p)]))
        else: out.append(para(p, PP[level_of(p)]))
        for pred, items, mode in A:
            if mode == "after" and pred(p):
                for t, lv in items: out.append(para(t, PP[lv], red=True))
    # ── 별표 목록
    out.append(heading("별표 목록", 1))
    rows = [["No.", "별표 내용", "관련 운영요령"]]
    for ln in pdftext(pdf, 15, 15).split("\n"):
        s = ln.strip()
        m = re.match(r"^(\d+)\s+(<별표 \d+>)\s+(.*)$", s)
        if not m: continue
        no, tag, rest = m.groups()
        if "<삭 제>" in rest: rows.append([no, f"{tag} <삭 제>", ""]); continue
        m2 = re.match(r"^(.*?)\s+(제\d+조(?:의\d+)?)$", rest)
        rows.append([no, f"{tag} {m2.group(1)}", m2.group(2)] if m2 else [no, f"{tag} {rest}", ""])
    rows.append(["10", "<별표 10> AI-Ready 수준 요건", "제21조"])
    out.append(table(rows, red_rows=[len(rows) - 1]))
    # ── 별지 서식 목록
    out.append(heading("별지 서식 목록", 1))
    txt = pdftext(pdf, 27, 28)
    frows = [["No.", "서식", "관련 운영규정", "관련 운영요령"]]
    cur = None; tails = []
    def flush():
        if not cur: return
        if "<삭 제>" in cur[1]: reg, yo = "", ""
        elif len(tails) >= 2: reg, yo = "".join(tails[:-1]).replace(",,", ","), tails[-1]
        elif len(tails) == 1: reg, yo = "", tails[0]
        else: reg, yo = "", ""
        frows.append([cur[0], cur[1], reg, yo])
    TAIL = re.compile(r"^(제[\d,]+(조(의\d+)?)?,?|[\d,]+(조(의\d+)?)?,?|-)$")
    for ln in txt.split("\n"):
        s = ln.strip()
        m = re.match(r"^(\d+(?:-\d+)?)\s+(<별지 제[\d\-]+호서식>)\s+(.*)$", s)
        if m:
            flush()
            no, tag, rest = m.groups()
            toks = rest.split(" "); tails = []
            while toks and TAIL.match(toks[-1]): tails.insert(0, toks.pop())
            cur = [no, f"{tag} {' '.join(toks)}"]
        elif cur and TAIL.match(s):
            tails.append(s)
    flush()
    # 신설 서식 삽입
    def insert_after(no, row):
        for i, r in enumerate(frows):
            if r[0] == no: frows.insert(i + 1, row); return i + 1
    i1 = insert_after("11", ["11-1", "<별지 제11-1호서식> 기계가독 산출물 선언서", "제35조", "제13조"])
    i2 = insert_after("21", ["21-1", "<별지 제21-1호서식> AI-Ready 자가점검표", "-", "제21조"])
    out.append(note("별지 서식 목록의 「분류」 열(위원회 운영·표준화 절차 등)은 원문 표에서 세로로 병합되어 있어 추출 과정에서 생략했다. 신설 서식 두 행만 붉은 글씨로 표시한다. 제15·23·24호서식은 제목이 바뀌지 않으므로 목록 변경이 없다."))
    out.append(table(frows, red_rows=[i for i in (i1, i2) if i]))
    # ── 신설 별표·별지 실물 (전부 신설이므로 붉은 글씨)
    for mdp, ttl in [(ROOT / "AI-Ready_방법3_제안자선언형_정합본/2_서식/별표_10_AI-Ready수준요건_안.md", "[별표 10] AI-Ready 수준 요건 (신설)"),
                     (ROOT / "AI-Ready_방법3_제안자선언형_정합본/2_서식/별지_제11-1호서식_기계가독산출물_선언서_안.md", "[별지 제11-1호서식] 기계가독 산출물 선언서 (신설)"),
                     (ROOT / "AI-Ready_방법3_제안자선언형_정합본/2_서식/별지_제21-1호서식_자가점검표_안.md", "[별지 제21-1호서식] AI-Ready 자가점검표 (신설)")]:
        out.append(heading(ttl, 1, red=True))
        _, body_xml = md_body_red(mdp, drop_quotes=True)
        out.append(body_xml)
    # ── 개정 서식 3종: 추가 문안
    out.append(heading("[별지 제15호·제23호·제24호서식] 확인란 추가 (개정)", 1, red=True))
    out.append(note("세 서식의 제목과 기존 항목은 그대로 두고 아래 확인란만 추가한다. 추가 위치와 문안은 06번 문서(신구대비)와 같다."))
    out.append(para("별지 제15호서식 — 「2. 검토 결과」의 파. 기타 의견 다음에 추가", P["body"], bold=True))
    for t in ["하. AI-Ready 적용 대상 여부 및 선언 타당성",
              "· 적용 대상 여부 : □ 해당 □ 비해당 (판정 근거 — 표준이 기술하는 내용 : □ 의미 □ 구조 □ 값 □ 품질 / □ 기능·절차·인터페이스)",
              "· 기계가독 산출물 선언서(별지 제11-1호서식) 첨부 : □ 있음 □ 없음",
              "· 선언 내용의 타당성 : □ 타당 □ 보완 필요 (보완 요청 사항 : )"]:
        out.append(para(t, 42, red=True))
    out.append(para("별지 제23호서식·제24호서식 — 「기타 의견(필요 조치사항 등)」 다음에 추가", P["body"], bold=True))
    for t in ["· AI-Ready 자가점검 결과 (별표 10 기준) : □ 적용 대상 아님 / □ 적용 대상 — AI-Ready 수준 : □ 충족 □ 미충족 / 산출물 요건 : □ 충족 □ 미충족 (자가점검표 별지 제21-1호서식 첨부)",
              "· 규범적 참조 점검 (제19조의3제3항) : □ 규범적 참조 없음(병행형만 사용) / □ 규범적 참조 있음 — 공개 위치 : □ 접근 가능 □ 접근 불가 / 보관본과 : □ 일치 □ 불일치 (조치 사항 : )",
              "· (제23호서식) 첨부 자료에 「□ AI-Ready 자가점검표(별지 제21-1호서식)」 추가"]:
        out.append(para(t, 42, red=True))
    return "정보통신표준화 운영요령 — AI-Ready 개정 전문(안)", out

# ══════════════════════════════════════════════════════════════════════════
# 2. 작성지침 통합본 (개정 절 전문)
# ══════════════════════════════════════════════════════════════════════════
def build_jichim():
    out = []
    out.append(heading("정보통신단체표준 작성지침(TTAR-09.0040) — AI-Ready 개정 절 전문", 1))
    out.append(note("원문 TTAR-09.0040/R1(2025. 5. 23.)에 AI Ready Data V.2.1 개정(안)을 반영한 통합본이다. **붉은 글씨가 신설·추가되는 문안**이고, 검은 글씨는 현행과 같다. 개정이 닿는 절(6.5.3, 6.5.7, 6.6, 6.7, 부속서 B, 부록 Ⅰ.4)만 전문을 싣고, 그 밖의 절(1~5, 6.1~6.4, 6.5.1·6.5.2·6.5.4~6.5.6, 6.8, 부속서 A, 부록 Ⅰ.1~Ⅰ.3·Ⅰ.5)은 현행과 같으므로 생략한다. 원문의 그림(그림 6-9, 6-10 등)은 글로 옮기지 않았다."))
    out.append(table([["절", "개정 성격", "내용"], ["6.5.3 인용 표준", "보강", "IRI 참조 단서 신설, 규범적 의존 어휘의 인용 표준 등재, 인용과 전재의 구분"],
                      ["6.5.7 요소 정의표", "신설", "14개 정규 컬럼, 에디터가 전역 어휘 식별자 매핑까지 작성"],
                      ["6.6 부속서", "보강", "기계가독 산출물 부속서 — 병행형(원칙)·참조형(예외), 이용조건 표시"],
                      ["6.7 부록", "보강", "참조구현 위치 안내(자유 작성 부록)"],
                      ["부속서 B", "신설(선택)", "어휘 매핑·단위 결합 지침"],
                      ["부록 Ⅰ.4", "보강", "본문 오류 사례 2건 추가"]]))
    # 6.5.3
    out.append(heading("6.5 본문", 1)); out.append(para("6.5.1 본문 일반 사항 · 6.5.2 적용 범위 — (현행과 같음)", P["body"]))
    out.append(heading("6.5.3 인용 표준", 2))
    out.append(para("표준의 주요 내용을 구성하기 위해 직접 인용한 표준에 대하여 작성하며, 단순 출처 및 근거 등의 정보를 나타내기 위한 표준 또는 문서는 작성하지 않는다. 용어 정의, 계산식, 그림 등을 인용하는 경우는 부록의 ‘x-4 참고 문헌’에 기재한다."))
    out.append(mixed([("모든 표준을 다 인용할 수 있는 것은 아니므로, 해당 표준화기구나 단체의 저작권 정책을 확인하여야 한다. 예를 들어 ISO/IEC, KS 표준은 일부, 전부 모두 직접 인용할 수 없다. ", False, False),
                      ("다만, 그 표준이 정의한 용어·클래스·속성·데이터 타입을 전역 어휘 식별자(IRI)로 가리키기만 하고 그 정의문을 옮겨 적지 아니하는 경우에는 직접 인용에 해당하지 아니하며, 이 경우 해당 표준을 인용 표준에 등재한다. ", True, False),
                      ("TTA와 준용 협약을 맺은 기관 중 IEEE와 ETSI는 본 기술보고서 부속서 A에 해당 내용이 정리되어 있으므로, 이를 참조한다.", False, False)]))
    for t in ["표준이 본문 또는 부속서에서 외부 어휘 또는 스키마(예: W3C DCAT·SKOS·DCMI Terms, W3C XML Schema 데이터 타입, ISO/IEC 표준 등)의 클래스, 속성, 데이터 타입 중 어느 하나 이상을 규범적으로 사용하는 경우에는, 해당 어휘 또는 표준을 인용 표준에 등재한다. 규범적으로 의존하면서 ‘인용 표준 해당없음’으로 기재하지 아니한다.",
              "인용 표준과 참고 문헌은 규범적 의존 여부로 구분한다. 따르지 않으면 이 표준에 적합하다고 할 수 없는 문서는 인용 표준에, 이해를 돕는 정보 제공에 그치는 문서는 참고 문헌에 둔다.",
              "외부 어휘를 전역 어휘 식별자(IRI)로 가리키는 것과 그 정의문을 이 표준에 옮겨 적는 것은 구분한다. 식별자로 가리키기만 하는 경우에는 저작권 확인 대상이 아니며, 정의문·요소 설명 등을 옮겨 적는 경우에만 해당 기구의 저작권 정책을 확인한다."]:
        out.append(para(t, red=True))
    for t in ["본문의 내용은 서문 3절에 기재한 내용과 동일하게 작성해야 한다. 인용 표준 작성 시 발행 기관, 표준번호, 표준명, 발행 연도 등을 기재한다.",
              "발행 연도가 표기된 인용 표준은 인용된 판만을 적용하며, 발행연도가 표기되지 않은 인용 표준은 최신판(모든 추록을 포함)을 적용한다.",
              "(예) IETF RFC 1034, Domain names - Concepts and facilities, 1987 : 1987년 판만을 적용함 / TTAK.KO-06.0343/R2, 기지국 전자파 인체 노출량 예측 방법 : 2023년 최신판을 적용함",
              "인용하는 표준의 일부를 제외한 경우 제외한 항목을 표기하고, 일부만 인용한 경우, 해당 항목을 표기한다.",
              "(예) ITU-T X.509(2005), 정보 기술 ― 개방형 시스템 간 상호접속 ― 디렉터리: ~ (Part 1과 Part 3은 국내 적용에서 제외함) / TTAK.KO-06.0496/R3, 재난안전통신망(PS-LTE) 단말기 기술 규격(부속서 A를 인용함)"]:
        out.append(para(t))
    out.append(para("6.5.4 용어 정의 · 6.5.5 약어 · 6.5.6 그림과 표, 수식 — (현행과 같음)", P["body"]))
    # 6.5.7 신설
    out.append(heading("6.5.7 요소 정의표 (신설)", 2, red=True))
    for t in ["데이터의 요소(항목)를 정의하는 표준은 각 요소를 아래 정규 컬럼을 갖춘 표(이하 “요소 정의표”)로 작성한다. 요소 정의표는 사람이 읽을 수 있도록 작성하며, 기계가독 형식으로의 변환은 6.6에 따른다.",
              "요소 정의표의 정규 컬럼은 다음 14개로 한다. 요소 이름, 표시명, 정의, 데이터 유형, 값 영역, 다중성, 필수 여부, 기본값, 예시, 비고, 단위, 출처, 버전, 전역 어휘 식별자(IRI).",
              '각 컬럼의 작성 방법은 <표 6-5>와 같고, 작성 예는 <표 6-6>과 같다. 요소 정의표는 컬럼이 많으므로 필요하면 쪽을 가로로 놓거나 표를 나누어 작성할 수 있다.',
              "표준초안 에디터는 14개 컬럼을 모두 작성하며, 해당하지 않는 컬럼에는 '해당 없음'으로 적는다. 작성한 매핑은 「정보통신표준화 운영요령」 제13조제5항에 따라 제안 단계에서 선언한 어휘와 일치하여야 한다."]:
        out.append(para(t, red=True))
    out.append(para('<표 6-5> 요소 정의표의 컬럼 작성 방법', red=True, bold=True))
    out.append(table([["컬럼", "작성 방법", "작성"]] + [['요소 이름', '요소를 가리키는 영문 이름. 낱말을 붙여 쓰고 공백을 두지 않는다. 기계가독 산출물의 키로 쓰인다', '필수'], ['표시명', '사람이 읽는 국문 이름', '필수'], ['정의', '이 표준의 말로 쓴 정의. 외부 어휘의 정의문을 옮겨 적지 않는다(6.5.3)', '필수'], ['데이터 유형', '문자열, 정수, 실수, 날짜, 날짜시간, 불리언, 식별자(IRI), 코드 중 하나', '필수'], ['값 영역', "허용 범위(예: 0~50), 형식(예: YYYY) 또는 코드 목록의 이름. 제한이 없으면 '제한 없음'", '필수'], ['다중성', '1, 0..1, 1..n, 0..n 중 하나', '필수'], ['필수 여부', '필수, 선택, 조건부 중 하나. 조건부이면 조건을 비고에 적는다', '필수'], ['기본값', '값이 주어지지 않을 때 쓰는 값', '해당 시'], ['예시', '실제 값의 예 하나 이상', '필수'], ['비고', '조건부 필수의 조건, 다른 요소와의 관계 등', '해당 시'], ['단위', '측정값을 기술하는 요소에 한하여, 단위 기호와 함께 단위의 전역 식별자(QUDT 단위 IRI 또는 UCUM 코드)를 적는다(부속서 B.4)', '측정값 요소'], ['출처', "이 요소의 개념을 가져온 표준·어휘. 이 표준에서 새로 정의하면 '이 표준'", '필수'], ['버전', '이 요소가 처음 생기거나 마지막으로 바뀐 이 표준의 판(예: R1)', '필수'], ['전역 어휘 식별자(IRI)', "해당 요소가 기존 전역 어휘의 용어에 대응하면 그 IRI 전체를 적고, 대응하는 용어가 없어 새로 정의하면 '자체 정의'로 적는다", '필수']], red_rows=range(1, 15)))
    out.append(para('<표 6-6> 요소 정의표 작성 예', red=True, bold=True))
    out.append(table([['요소 이름', '표시명', '정의', '데이터 유형', '값 영역', '다중성', '필수 여부', '기본값', '예시', '비고', '단위', '출처', '버전', '전역 어휘 식별자(IRI)']] + [['Title', '제목', '데이터세트를 식별하는 이름', '문자열', '제한 없음', '1..n', '필수', '해당 없음', 'Nucleosome positioning on genomic DNA', '언어별로 반복할 수 있다', '해당 없음', 'DCMI Metadata Terms', 'R1', 'http://purl.org/dc/terms/title'], ['PublicationYear', '공개 연도', '데이터세트를 처음 공개한 해', '날짜', 'YYYY', '1', '필수', '해당 없음', '2016', '해당 없음', '해당 없음', 'DCMI Metadata Terms', 'R1', 'http://purl.org/dc/terms/issued'], ['waterTemperature', '수온', '수조 물의 온도 측정값', '실수', '0~50', '1', '필수', '해당 없음', '18.4', '센싱 주기마다 1건', '℃ (http://qudt.org/vocab/unit/DEG_C)', '이 표준', 'R1', '자체 정의']], red_rows=range(1, 4)))
    out.append(para('작성 예의 앞 두 행은 연구데이터 메타데이터 표준의 요소를, 셋째 행은 센서 데이터 표준의 측정값 요소를 가져와 컬럼 쓰임을 보인 것이다.', red=True))
    # 6.6
    out.append(heading("6.6 부속서", 1))
    for t in ["부속서는 내용으로서는 본래 표준의 본문에 포함시켜도 되는 사항이지만, 표준의 구성상 특별히 추려서 본문에 준하여 정리한 것을 말한다.",
              "부속서 제목은 부속서 첫 번째 쪽 중앙 맨 위쪽에 위치하여야 하며, 부속서 번호 밑에 ‘(본 부속서는 표준 내용의 일부임)’을 표기한다.",
              "부속서는 A, B, C 순으로 작성하며, 항목 번호 앞에 부속서 번호(알파벳)를 붙인다.",
              "그림, 표, 수식 등의 항목 번호는 (그림 6-9)의 예와 같이 대항목 절별로 부여한다. [(그림 6-9) 부속서 항목 번호 체계 — 현행과 같음]",
              "그 외 부속서를 작성하는 방법은 본문과 동일하며 6.5를 참조한다."]:
        out.append(para(t))
    for t in ["기계가독 산출물은 부속서로 작성한다. 부속서 번호는 6.6의 A, B, C 순 부여 원칙에 따르되, 기계가독 산출물이라 하여 특정 알파벳을 고정하지 아니한다. 기술규격은 제외한다.",
              "a) 병행형(원칙) — 부속서에 전문 수록하고, 같은 내용을 별도 파일로도 제공한다. 요소↔전역 어휘 식별자 매핑(JSON-LD @context), 소규모 JSON Schema 등 문서에 수록할 수 있는 분량인 경우에 적용한다. 부속서 수록본이 정본이며, 제공 파일은 기계가 직접 처리할 수 있도록 하기 위한 것이다.",
              "b) 참조형(예외) — 부속서에 규범적 참조 명세를 두고, 산출물 실물은 외부 저장소에 둔다. 분량이 많아 수록이 곤란하거나, 표준 문서와 다른 주기로 개정되거나, 다른 파일을 인용·포함하여 단일 파일로 완결되지 아니하는 경우에 적용한다(운영요령 제19조의3제3항). 명세에는 다음을 기재한다.",
              "1) 공개 위치(URL)  2) 판 또는 버전  3) 무결성 확인 값  4) 이용조건(라이선스)  5) 협회 보관본의 위치",
              "참조형인 경우에도 「정보통신표준화 운영요령」 제19조의3제6항에 따라 협회가 보관하는 사본이 정본이다.",
              "어느 형태이든 산출물 파일에는 이용조건을 표시한다. 부속서에 수록한 경우에도 파일에 별도로 표시한다 — 표준 문서의 저작권 문구가 산출물에 자동으로 미친다고 볼 수 없기 때문이다. 표시 방법은 형식에 따른다.",
              "- XML Schema·Turtle·Protobuf: 주석으로 파일 머리말에 기재",
              "- JSON Schema: 주석을 쓸 수 없으므로 최상위 $comment 키에 기재",
              "- RDF 어휘: dcterms:license 트리플로 기재하여 기계가 해석할 수 있게 한다"]:
        out.append(para(t, red=True))
    # 6.7
    out.append(heading("6.7 부록", 1))
    for t in ["부록은 표준으로 규정하고자 하는 사항은 아니나 표준을 보충하기 위해 작성한다. 표준 본문 내용을 설명하는 부록인 자유 작성 부록과 표준 관련 정보를 기재하는 필수 작성 부록이 있다. 부속서가 있을 경우에는 부속서 이후부터 작성하며 부속서가 없을 경우에는 본문 이후부터 작성한다.",
              "부록 제목은 부록 첫 번째 쪽 중앙 맨 위쪽에 위치하여야 하며, 표준 규정 사항이 아닌, 보충 사항이라는 이해도 향상을 위해 번호 밑에 ‘(본 부록은 표준을 보충하기 위한 내용으로 표준의 일부는 아님)’을 같이 명시한다.",
              "자유 작성 부록은 Ⅰ, Ⅱ, Ⅲ 순으로 작성하며, 항목 번호 앞에 부속서 번호(로마자 대문자)를 붙인다. ‘x-1’의 항목 번호 체계는 필수 작성 부록에만 사용하므로 항목 번호 작성 시 유의하여야 한다. (그림 6-10)에서 필수 작성 부록 번호를 보면 ‘x-1’의 형식을 사용할 경우에는 그림, 표, 수식의 번호가 굉장히 복잡해지므로, 필수 작성 부록에서는 가급적 그림, 표, 수식을 포함하지 않도록 한다.",
              "자유 작성 부록이 없는 경우는 양식을 삭제하고 필수 작성 부록 번호를 Ⅰ-1~6으로 앞당겨 사용한다. [(그림 6-10) 부록 항목 번호 체계 — 현행과 같음]"]:
        out.append(para(t))
    for t in ["참조구현을 공개하는 경우 그 위치를 자유 작성 부록에 기재할 수 있다. 이 경우 다음 문구를 함께 적는다.",
              "“참조구현은 표준의 일부가 아니며, 협회는 그 내용에 대하여 보증하지 아니한다.”"]:
        out.append(para(t, red=True))
    for t in ["필수 작성 부록은 6개의 항목으로 구성된다. 해당 사항이 없는 경우라도, 양식을 삭제하지 않으며, ‘해당 사항 없음.’으로 기재한다.",
              "a) 지식재산권 확약서 정보 — 표준 발간 이전에 접수된 지식재산권 확약서에 대해 작성하며, 모든 항목을 빠짐 없이 작성해야 한다. 발간 이후 오류정정서를 통해 추가할 수 있다. 본문 시작에 있는 정형 문구를 삭제하지 않는다. 단, ETSI 표준을 준용한 경우에는 부속서 A에 따라 정형 문구를 작성한다. [(그림 6-11) — 현행과 같음]",
              "b) 시험인증 관련 사항 — 시험인증 대상 여부, 시험표준 제정 현황 등 시험인증 관련 사항이 있는 경우에 작성하며, 해당 표준 발간 이후 시험 관련 표준이 제정되는 등의 변동이 있는 경우, 오류정정서를 통해 변경할 수 있다.",
              "c) 본 표준의 연계(family) 표준 — 본 표준의 연계 표준으로서 부로 나뉘어 발간된 표준을 작성하며, 기술보고서도 적을 수 있다. 부로 나뉜 연계 표준이 아니어도 본 표준을 이용함에 있어 필수적으로 이용 또는 참고해야 하는 표준이 있는 경우 작성할 수 있다. 항목 번호를 매기고 표준번호, 표준명을 작성한다. 해당 표준 발간 이후 연계 표준이 제·개정되는 등의 변동이 있는 경우, 오류정정서를 통해 변경할 수 있다.",
              "d) 참고 문헌 — 표준을 기술하기 위해 인용 및 참고된 관련 자료가 있는 경우 작성한다. 발간일이 기재된 경우, 해당 표준(문서)의 해당 버전에 대해서만 유효하며, 해당 표준의 최신판을 따르도록 하고자 하는 경우에는 연도를 표기하지 않는다. 본문 시작에 있는 정형 문구를 삭제하지 않는다. 또한 참고 문헌은 넘버링을 하여 작성하되, 본문에서 해당 참고 문헌을 언급할 때는 넘버링이 아닌 참고 문헌명(표준번호 등)을 본문에 직접 작성하거나, [출처: 참고 문헌]의 형식으로 작성해야 한다. (예 1) KS A 0001:2023, 4.3.1에 따라 (예 2) [출처: TTAK.KO-09.0002/R2, ICT 통합 분류 체계]",
              "e) 영문표준 해설서 — 영문표준에 한해 작성하며, 인용하는 표준의 대항목별(1절, 2절 등)로 주요 내용의 요약을 작성한다. 한 줄 요약이 아닌 해당 표준의 내용을 알 수 있는 수준으로 작성하도록 한다. 해설서의 절 번호는 원문 표준과 동일하게 작성한다.",
              "f) 표준의 이력 — 표준의 판수별 채택일, 표준번호, 내용과 담당 위원회를 작성한다. 개정된 표준일 경우 공헌자를 제정 및 개정 표준별로 구분하여 병기할 수 있다."]:
        out.append(para(t))
    out.append(para("6.8 기타 — (현행과 같음)", P["body"]))
    # 부속서 B
    out.append(heading("부속서 A 표준화기구별 영문 준용 지침 — (현행과 같음)", 1))
    out.append(heading("부속서 B 어휘 매핑·단위 결합 지침 (신설, 선택)", 1, red=True))
    out.append(para("(본 부속서는 기술보고서 내용의 일부임)", red=True))
    for t in ["B.1 전역 어휘 선택 — 기존 어휘 우선 사용 원칙. 자체 정의는 대응하는 용어가 없을 때로 한정한다.",
              "B.2 어휘별 이용조건 — 주요 어휘의 라이선스 상태는 아래 표와 같다.",
              "B.3 @context 작성 — 요소 이름을 키로, 전역 어휘 식별자를 값으로 하는 JSON-LD @context를 6.6에 따라 부속서로 제공한다.",
              "B.4 단위 결합 — 측정값 요소의 단위 식별자(QUDT/UCUM) 결합 방법."]:
        out.append(para(t, red=True))
    rows = [["어휘", "이용조건", "확인 위치", "전재 시 유의"],
            ["W3C DCAT", "CC BY 4.0", "dcat.ttl에 dcterms:license 트리플로 선언", "출처 표시로 가능"],
            ["DCMI Terms", "CC BY 4.0", "DCMI 문서 고지", "출처 표시로 가능"],
            ["W3C PROV-O", "W3C 문서·소프트웨어 라이선스", "어휘 파일에 선언 없음, 권고안 고지 참조", "확인 후 사용"],
            ["W3C SKOS", "어휘 파일에 선언 없음", "W3C 문서 라이선스에 종속", "확인 후 사용"],
            ["W3C XML Schema 데이터 타입", "© W3C, All Rights Reserved + document use rules", "권고안 고지", "확인 후 사용"],
            ["Schema.org", "CC BY-SA 3.0", "docs/terms.html", "동일조건변경허락(SA) — IRI로 가리키는 방식을 권장"],
            ["ISO/IEC (예: 19115-3)", "파일에 표시 없음", "standards.iso.org 이용약관에 종속", "정의문을 전재하지 아니한다. IRI로 가리키기만 하고 6.5.3 단서에 따라 인용 표준에 등재한다"]]
    out.append(table(rows, red_rows=range(1, len(rows))))
    # 부록 Ⅰ.4
    out.append(heading("부록 Ⅰ 빈번한 오류 사례", 1))
    out.append(para("Ⅰ.1 표지 오류 · Ⅰ.2 서문 오류 · Ⅰ.3 목차 오류 — (현행과 같음)"))
    out.append(heading("Ⅰ.4 본문 오류", 2))
    for t in ["<표 Ⅰ.4-1> 항목 및 단락 작성 오류 사례 — 항목 번호와 항목명 사이는 2칸 띄어쓰기한다. 숫자나 영어로 항목명이 시작되는 경우, 띄어쓰기를 1칸만 할 경우에 항목 번호와 제목 간 구분이 어렵다. 항목 번호 뒤에는 온점(.)을 찍지 않고 2칸 띄어쓰기로 작성한다. 또한 항목과 항목, 항목과 본문 사이는 1행을 띄어 쓰도록 한다.",
              "<표 Ⅰ.4-2> 용어 정의 오류 사례 — 용어 정의만 예외적으로 가독성을 위해 항목과 본문 사이에 1행을 띄지 않고 붙여 적는다. 용어 정의는 국어 표제어(약어, 영어 표제어) 순으로 작성해야 한다. 또한 정의된 내용이 본문에서 해당 용어를 대체할 수 있어야 하므로 정의하는 용어를 반복해서 작성하지 않고, 명사형으로 적는 것을 기본으로 한다.",
              "<표 Ⅰ.4-3> 약어 오류 사례 — 약어는 알파벳 순으로 작성하며, 약어에 해당하는 글자는 대문자로 작성해야 한다.",
              "<표 Ⅰ.4-4> 그림 오류 사례 1 — 그림 번호는 (소괄호)를 사용하여 작성한다. <홑화살괄호>는 표 번호를 나타낼 때 쓰므로 수정이 필요하다. 그림 번호는 대항목 절별로 부여하며 중복되지 않도록 작성해야 한다. 출처가 있는 경우는 누락하지 않고 작성해야 하며, 양식에 맞도록 [대괄호] 안에 작성한다.",
              "<표 Ⅰ.4-5> 그림 오류 사례 2 — 그림은 해상도가 너무 낮아 알아볼 수 없는 경우가 없도록 주의해야 한다. 출처가 불분명한 그림은 사용하지 않아야 하며, 저작권 문제가 발생하지 않는 그림을 사용해야 한다.",
              "<표 Ⅰ.4-6> 표 오류 사례 — 표 작성 시 발견되는 흔한 오류는 제목 셀 작성과 관련된 부분이다. 특히 음영 설정을 하지 않도록 유의한다. 제목 셀 내의 글자는 굵게 표기하여 내용 셀의 글자와 구분한다. 위의 오류 사례에서는 표 번호에 ‘표’가 누락되어 있으므로 추가하여 작성해야 한다."]:
        out.append(para(t))
    out.append(para('<표 Ⅰ.4-7> 규범적으로 사용하는 외부 어휘의 인용 표준 누락 사례', red=True, bold=True))
    out.append(table([["잘못 작성된 예시", "올바르게 작성된 예시"], ['2 인용 표준<br>해당 사항 없음.<br>(본문 요소 정의표의 IRI 컬럼에는 dct:title, dcat:Dataset을 사용)<br>부록 Ⅱ-4 참고 문헌<br>[1] DCMI Metadata Terms<br>[2] W3C DCAT 3', '2 인용 표준<br>DCMI, DCMI Metadata Terms, 2020<br>W3C, Data Catalog Vocabulary (DCAT) – Version 3, 2024']], red_rows=[1]))
    out.append(para('본문이나 부속서에서 외부 어휘·스키마의 클래스·속성·데이터 타입을 규범적으로 사용하면, 그 어휘는 이 표준을 따르기 위해 반드시 필요한 문서이므로 인용 표준에 적는다(6.5.3). 참고 문헌에만 적으면 그 어휘를 따르지 않아도 되는 것으로 읽힌다. 요소 정의표의 전역 어휘 식별자(IRI) 컬럼(6.5.7)에 나오는 어휘가 인용 표준에 모두 있는지 확인하면 이 오류를 줄일 수 있다.', red=True))
    out.append(para('이 사례는 외부 어휘를 IRI로 가리키는 경우를 다룬다. KS·ISO/IEC 표준의 정의문을 옮겨 적은 경우는 Ⅰ.2 a)에 따라 참고 문헌에 적는다. 다만 ISO/IEC 표준이 정의한 용어를 IRI로 가리키기만 하는 경우에는 직접 인용에 해당하지 않으므로 인용 표준에 적는다(6.5.3 단서).', red=True))
    out.append(para('<표 Ⅰ.4-8> 인용과 전재를 혼동한 사례', red=True, bold=True))
    out.append(table([["잘못 작성된 예시", "올바르게 작성된 예시"], ['요소 정의표의 "정의" 컬럼에 ISO 19115-3의 정의문을 영문 그대로 옮겨 적고 출처만 표기함', '"정의" 컬럼은 이 표준의 말로 쓰고, "전역 어휘 식별자(IRI)" 컬럼에 ISO 19115-3 요소의 IRI를 적음']], red_rows=[1]))
    out.append(para('IRI로 가리키는 것은 인용이고, 정의문을 옮겨 적는 것은 전재다. 가리키기만 하는 경우에는 저작권 확인이 필요하지 않다. 옮겨 적는 경우에는 해당 기구의 저작권 정책을 확인해야 하며, ISO/IEC·KS 표준의 정의문은 옮겨 적을 수 없다(6.5.3). 반대로 IRI만 적으면서 저작권 확인 절차를 밟을 필요는 없다.', red=True))
    out.append(para("Ⅰ.5 부록 오류 — (현행과 같음)"))
    return "정보통신단체표준 작성지침 — AI-Ready 개정 절 전문(안)", out

def write(title, body, out_path):
    first = (f'<hp:p id="3121190098" paraPrIDRef="{P["center"]}" styleIDRef="0" pageBreak="0" columnBreak="0" merged="0">{m2h.SECPR_RUN}'
             f'<hp:run charPrIDRef="1"/><hp:run charPrIDRef="{C["title"]}"><hp:t>{esc(title)}</hp:t></hp:run>'
             f'<hp:linesegarray><hp:lineseg textpos="0" vertpos="0" vertsize="3114" textheight="3114" baseline="2319" spacing="2024" horzpos="0" horzsize="{WIDTH}" flags="393216"/></hp:linesegarray></hp:p>')
    sec = m2h.SEC_NS + first + "".join(body) + "</hs:sec>"
    ET.fromstring(sec.encode("utf-8"))
    hdr = red_header(); ET.fromstring(hdr.encode("utf-8"))
    prv = re.sub(r"<[^>]+>", " ", sec)[:3000]
    with zipfile.ZipFile(out_path, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), (m2h.REF / "mimetype").read_bytes(), compress_type=zipfile.ZIP_STORED)
        for rel in ["version.xml", "settings.xml", "META-INF/container.xml", "META-INF/container.rdf", "META-INF/manifest.xml", "Contents/content.hpf", "Preview/PrvImage.png"]:
            z.writestr(rel, (m2h.REF / rel).read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/header.xml", hdr.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Contents/section0.xml", sec.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr("Preview/PrvText.txt", prv.encode("utf-8"), compress_type=zipfile.ZIP_DEFLATED)
    print(out_path.name, "OK", out_path.stat().st_size // 1024, "KB", "red runs:", sum(sec.count(f'charPrIDRef="{v}"') for v in RED.values()))

if __name__ == "__main__":
    t, b = build_yoryeong(); write(t, b, OUT / "09_정보통신표준화_운영요령_개정전문_통합본(붉은글씨=개정).hwpx")
    t, b = build_jichim();   write(t, b, OUT / "10_정보통신단체표준_작성지침_개정절전문_통합본(붉은글씨=개정).hwpx")
    if "--dump" in sys.argv:
        # 검토용: 운영요령 본문 단락 텍스트 출력
        pass
