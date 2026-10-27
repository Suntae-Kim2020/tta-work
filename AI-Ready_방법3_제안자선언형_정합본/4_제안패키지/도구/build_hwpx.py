# -*- coding: utf-8 -*-
"""제안패키지의 md(정본) 3종 × 5표준 → hwpx. 변환기는 최종산출물/도구/md2hwpx.py를 그대로 쓴다.
실행: python 도구/build_hwpx.py  (저장소 어디에서든)
"""
import importlib.util, pathlib, sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
ROOT = PKG.parent.parent
spec = importlib.util.spec_from_file_location("md2hwpx", ROOT / "최종산출물" / "도구" / "md2hwpx.py")
m2h = importlib.util.module_from_spec(spec); spec.loader.exec_module(m2h)

sys.stdout.reconfigure(encoding="utf-8")
n = 0
for d in sorted(PKG.iterdir()):
    if not d.is_dir() or d.name == "도구": continue
    for md in sorted(d.glob("*.md")):
        sec, title, prv = m2h.convert(md.read_text(encoding="utf-8"))
        out = md.with_suffix(".hwpx"); m2h.write_hwpx(sec, prv, out); n += 1
        print(f"{d.name}/{out.name}  [{title[:40]}]  {out.stat().st_size // 1024} KB")
print(f"{n} files")
