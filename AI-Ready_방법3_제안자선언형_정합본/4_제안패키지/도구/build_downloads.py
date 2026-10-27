# -*- coding: utf-8 -*-
"""제안패키지의 hwpx 사본과 부속서 ZIP을 docs/downloads/제안패키지/에 만들고, docs/downloads.html의
「파일럿 실증 5종 — 제안패키지」 표를 다시 쓴다. 실행: python 도구/build_downloads.py (저장소 어디에서든)
"""
import pathlib, shutil, zipfile, sys, urllib.parse, re
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parents[3]
PKG = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "downloads" / "제안패키지"
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir(parents=True)

META = {
 "0310_자율주행품질": ("TTAK.KO-11.0310", "자율주행 데이터 품질", "④ 품질 지표", "A @context · B SHACL · C DQV", "ISO/IEC 5259-2를 가리키기만 하여 인용 표준에 등재(6.5.3 단서)"),
 "0976_연구데이터메타": ("TTAK.KO-10.0976", "연구데이터 메타데이터", "① 지식정보", "A @context · B SHACL · C PROV-O · D ODRL", "종전 참고 문헌의 DataCite를 인용 표준으로 승격"),
 "1510_국토공통모델": ("TTAK.KO-10.1510", "국토 공통 데이터 모델", "② 자기기술형 레코드", "A @context · B SHACL · C PROV-O", "기하(WKT)·좌표계 제약을 SHACL로"),
 "1530_수산센서구조": ("TTAK.KO-10.1530", "수산 센서 데이터 구조", "② 자기기술형 레코드", "A @context · B SHACL · C 단위 · D PROV-O", "단위를 QUDT IRI + UCUM 코드로 이중 결합"),
 "1594_AI모델메타": ("TTAK.KO-10.1594", "AI 모델 메타데이터", "③ AI 데이터세트", "A @context · B SHACL · C 단위 · D PROV-O · E Croissant(참조형) · F DQV · G ODRL", "참조형·외부 공개·참조구현을 모두 선언 — 별표 10 제4부 3번·10번까지 실증"),
}
DOCS = [("1_별지제11-1호서식_기계가독산출물_선언서.hwpx", "선언서"),
        ("2_표준초안_AI-Ready개정부.hwpx", "표준초안"),
        ("3_별지제21-1호서식_AI-Ready_자가점검표.hwpx", "자가점검표")]
def q(p): return urllib.parse.quote(p, safe="/")

rows = []; n_hwpx = 0; n_annex = 0
all_zip = zipfile.ZipFile(OUT / "제안패키지_전체.zip", "w", zipfile.ZIP_DEFLATED)
all_zip.write(PKG / "README.md", "README.md")
for d in sorted(PKG.iterdir()):
    if not d.is_dir() or d.name == "도구": continue
    code, name, prof, annex, point = META[d.name]
    od = OUT / d.name; od.mkdir()
    links = []
    for fn, label in DOCS:
        shutil.copy2(d / fn, od / fn); n_hwpx += 1
        links.append(f'<a href="downloads/제안패키지/{q(d.name)}/{q(fn)}" download>⬇ {label}</a>')
        all_zip.write(d / fn, f"{d.name}/{fn}")
    for md in d.glob("*.md"): all_zip.write(md, f"{d.name}/{md.name}")
    zname = f"{d.name}_부속서.zip"
    with zipfile.ZipFile(od / zname, "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted((d / "부속서").iterdir()):
            z.write(f, f"부속서/{f.name}"); n_annex += 1
            all_zip.write(f, f"{d.name}/부속서/{f.name}")
    links.append(f'<a href="downloads/제안패키지/{q(d.name)}/{q(zname)}" download>⬇ 부속서 ZIP</a>')
    rows.append(
        f'<tr><td class="num">{code}</td>'
        f'<td><strong>{name}</strong><br><span style="color:var(--text-dim)">{prof} · 부속서 {annex}<br>{point}</span></td>'
        f'<td>{" · ".join(links)}</td></tr>')
all_zip.close()
print(f"hwpx {n_hwpx}, annex {n_annex}, zips {len(rows)+1}")

html = ROOT / "docs" / "downloads.html"
s = html.read_text(encoding="utf-8")
block = (
 '<h2 id="pkg">파일럿 실증 5종 — 제안패키지</h2>\n'
 '<div class="note why"><span class="note-t">무엇인가</span>위 서식(별지 제11-1호서식·제21-1호서식)과 작성지침 개정안(6.5.3·6.5.7·6.6·6.7)대로 실제 표준 다섯 종을 끝까지 작성해 본 결과물이다. '
 '표준마다 <strong>선언서</strong>(제안자)·<strong>표준초안 AI-Ready 개정부</strong>(에디터)·<strong>자가점검표</strong>(에디터) 한글 문서 세 벌과, 이용조건을 파일 안에 표시한 <strong>부속서 실물</strong>(JSON-LD·Turtle)을 ZIP으로 묶었다. '
 '정본(md)과 부속서 원본은 저장소 폴더 <code>AI-Ready_방법3_제안자선언형_정합본/4_제안패키지/</code>에 있다. 외부 공개 URL과 참조구현 위치는 예시이며 성명·일자란은 비워 두었다.</div>\n'
 '<div class="tablebox"><table>\n<thead><tr><th>표준</th><th>내용</th><th>내려받기</th></tr></thead>\n<tbody>' + "".join(rows) +
 '<tr><td class="num">전체</td><td><strong>제안패키지 전체</strong><br><span style="color:var(--text-dim)">다섯 표준의 한글 문서 15종 + md 정본 + 부속서 파일 21종 + README</span></td>'
 f'<td><a href="downloads/제안패키지/{q("제안패키지_전체.zip")}" download>⬇ 전체 ZIP</a></td></tr>'
 '</tbody></table></div>\n')
s = s.replace('<code>AI-Ready_방법3_제안자선언형_정합본/4_제안패키지/</code>', '<code>4_제안패키지/</code>')  # noop safety
block = block.replace('AI-Ready_방법3_제안자선언형_정합본/4_제안패키지/', 'AI Ready Data V.2.1 폴더의 4_제안패키지/')
s = re.sub(r'<h2 id="pkg">.*?</tbody></table></div>\n', '', s, flags=re.S)  # 재실행 대비
marker = '<div class="note warn"><span class="note-t">의결 전 확인할 것</span>'
assert marker in s
s = s.replace(marker, block + marker, 1)
html.write_text(s, encoding="utf-8")
print("downloads.html updated")
