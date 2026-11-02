"""Render diagram HTML to PNG: py shot.py <post-slug> <name>... -> assets/img/posts/<post-slug>/<name>-{light,dark}.png"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).parent
post, names = sys.argv[1], sys.argv[2:]
out = HERE.parents[1] / "assets/img/posts" / post
out.mkdir(parents=True, exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1000, "height": 600}, device_scale_factor=2)
    for n in names:
        for skin in ("light", "dark"):
            pg.goto((HERE / f"{n}-{skin}.html").as_uri())
            pg.wait_for_timeout(800)  # web fonts
            pg.locator("svg").screenshot(path=str(out / f"{n}-{skin}.png"))
            print("png", out / f"{n}-{skin}.png")
    b.close()
