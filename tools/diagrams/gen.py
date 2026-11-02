"""Generate HITL blog diagrams (light + dark) as self-contained HTML. Tokens = Chirpy blog theme."""
from pathlib import Path

OUT = Path(__file__).parent

SKINS = {
    "light": dict(paper="#f6f8fa", node="#ffffff", ink="#34343c", muted="#585858", soft="#6b6b6b",
                  accent="#0056b2", tint="rgba(0,86,178,0.08)",
                  oval_fill="rgba(52,52,60,0.04)", oval_stroke="rgba(52,52,60,0.35)"),
    "dark": dict(paper="#1e1e1e", node="#26262a", ink="#cccccc", muted="#a7a7a7", soft="#9a9a9a",
                 accent="#8ab4f8", tint="rgba(138,180,248,0.12)",
                 oval_fill="rgba(204,204,204,0.05)", oval_stroke="rgba(204,204,204,0.35)"),
}

SANS = "'Source Sans 3', 'Noto Sans KR', 'Malgun Gothic', sans-serif"
MONO = "'Geist Mono', ui-monospace, monospace"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class D:
    """Tiny SVG builder. Arrows are appended to `arrows`, nodes to `nodes`, so arrows render first."""

    def __init__(self, t):
        self.t, self.arrows, self.labels, self.nodes = t, [], [], []

    def line(self, d, accent=False, dashed=False):
        t = self.t
        color = t["accent"] if accent else t["muted"]
        marker = "arrow-accent" if accent else "arrow"
        dash = ' stroke-dasharray="5,4"' if dashed else ""
        self.arrows.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{1.6 if accent else 1.3}"{dash} marker-end="url(#{marker})"/>')

    def label(self, x, y, w, text, accent=False, lines=None):
        """Mask rect at (x, y) width w, centered Korean text, 12px."""
        t = self.t
        lines = lines or [text]
        h = 16 * len(lines)
        self.labels.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{t["paper"]}"/>')
        for i, ln in enumerate(lines):
            self.labels.append(
                f'<text x="{x + w / 2}" y="{y + 12 + 16 * i}" fill="{t["accent"] if accent else t["muted"]}" font-size="12" '
                f'font-weight="500" font-family="{SANS}" text-anchor="middle">{esc(ln)}</text>')

    def _texts(self, cx, cy, name, sub, sub_mono):
        t = self.t
        if sub:
            out = [f'<text x="{cx}" y="{cy - 2}" fill="{t["ink"]}" font-size="14" font-weight="600" font-family="{SANS}" text-anchor="middle">{esc(name)}</text>']
            fam, size = (MONO, 11) if sub_mono else (SANS, 12)
            out.append(f'<text x="{cx}" y="{cy + 15}" fill="{t["soft"]}" font-size="{size}" font-family="{fam}" text-anchor="middle">{esc(sub)}</text>')
            return out
        return [f'<text x="{cx}" y="{cy + 5}" fill="{t["ink"]}" font-size="14" font-weight="600" font-family="{SANS}" text-anchor="middle">{esc(name)}</text>']

    def rect(self, x, y, w, h, name, sub=None, focal=False, sub_mono=True):
        t = self.t
        fill, stroke = (t["tint"], t["accent"]) if focal else (t["node"], t["ink"])
        self.nodes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{t["paper"]}"/>')
        self.nodes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{stroke}" stroke-width="{1.4 if focal else 1}"/>')
        self.nodes += self._texts(x + w / 2, y + h / 2, name, sub, sub_mono)

    def oval(self, x, y, w, h, name, sub=None, sub_mono=False):
        t = self.t
        self.nodes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{t["paper"]}"/>')
        self.nodes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="20" fill="{t["oval_fill"]}" stroke="{t["oval_stroke"]}" stroke-width="1"/>')
        self.nodes += self._texts(x + w / 2, y + h / 2, name, sub, sub_mono)

    def diamond(self, cx, cy, hw, hh, lines):
        t = self.t
        pts = f"{cx},{cy - hh} {cx + hw},{cy} {cx},{cy + hh} {cx - hw},{cy}"
        self.nodes.append(f'<polygon points="{pts}" fill="{t["node"]}" stroke="{t["ink"]}" stroke-width="1"/>')
        y0 = cy + 5 - 9 * (len(lines) - 1)
        for i, ln in enumerate(lines):
            self.nodes.append(f'<text x="{cx}" y="{y0 + 18 * i}" fill="{t["ink"]}" font-size="13" font-weight="600" font-family="{SANS}" text-anchor="middle">{esc(ln)}</text>')

    def svg(self, slug, w, h, title, desc):
        t = self.t
        defs = (f'<marker id="{slug}-arrow" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{t["muted"]}"/></marker>'
                f'<marker id="{slug}-arrow-accent" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto"><polygon points="0 0, 8 3, 0 6" fill="{t["accent"]}"/></marker>')
        body = "\n".join(self.arrows + self.labels + self.nodes)
        body = body.replace("url(#arrow)", f"url(#{slug}-arrow)").replace("url(#arrow-accent)", f"url(#{slug}-arrow-accent)")
        return (f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="{slug}-title {slug}-desc">\n'
                f'<title id="{slug}-title">{esc(title)}</title>\n<desc id="{slug}-desc">{esc(desc)}</desc>\n'
                f'<defs>{defs}</defs>\n<rect width="100%" height="100%" fill="{t["paper"]}"/>\n{body}\n</svg>')


def hitl_concept(t):
    d = D(t)
    # arrows
    d.line("M116,80 H146")
    d.line("M292,80 H326")
    d.line("M456,80 H582")
    d.line("M392,120 V166", accent=True)
    d.line("M472,196 H652 Q660,196 660,188 V110")
    d.line("M392,224 V262")
    # labels
    d.label(498, 56, 44, "아니오")
    d.label(402, 136, 20, "예", accent=True)
    d.label(542, 172, 36, "승인")
    d.label(402, 236, 36, "반려")
    # nodes
    d.oval(16, 56, 100, 48, "요청")
    d.rect(148, 56, 144, 48, "AI가 결과 생성")
    d.diamond(392, 80, 64, 40, ["위험한가?"])
    d.oval(584, 52, 152, 56, "바깥으로 내보내기", sub="게시 · 발송 · 송금")
    d.rect(312, 168, 160, 56, "멈추고 사람 확인", sub="interrupt()", focal=True)
    d.oval(312, 264, 160, 48, "내보내지 않음")
    return d, 760, 336, "HITL 흐름", "위험한 결과만 멈춰서 사람의 승인을 받고, 안전한 결과는 바로 내보내는 흐름"


def hitl_pipeline(t):
    d = D(t)
    # arrows (main row y=96)
    d.line("M112,96 H142")
    d.line("M256,96 H286")
    d.line("M424,96 H458")
    d.line("M580,96 H662")
    d.line("M520,136 V190", accent=True)                         # 예
    d.line("M600,220 H716 Q724,220 724,212 V122")                 # 승인
    d.line("M520,248 V294")                                       # 반려
    d.line("M440,220 H364 Q356,220 356,212 V122")                 # 다시 판정
    d.line("M724,72 V48 Q724,40 716,40 H364 Q356,40 356,48 V70", dashed=True)  # 게시본 충돌
    # labels
    d.label(600, 72, 44, "아니오")
    d.label(530, 154, 20, "예", accent=True)
    d.label(632, 150, 80, "", lines=["승인", "수정 후 승인"])
    d.label(530, 264, 36, "반려")
    d.label(366, 196, 64, "다시 판정")
    d.label(476, 16, 128, "게시본이 바뀌었으면")
    # nodes
    d.oval(16, 72, 96, 48, "수정 요청")
    d.rect(144, 72, 112, 48, "지시 분석", sub="parse_request")
    d.rect(288, 72, 136, 48, "수정안 작성", sub="draft_edit")
    d.diamond(520, 96, 60, 40, ["위험 기준에", "걸리나?"])
    d.rect(664, 72, 120, 48, "공고에 반영", sub="apply_edit")
    d.rect(440, 192, 160, 56, "멈추고 사람 확인", sub="review · interrupt()", focal=True)
    d.oval(440, 296, 160, 48, "원문 유지", sub="hold", sub_mono=True)
    return d, 800, 368, "공고문 수정 에이전트 흐름", "수정안을 만들고 위험 기준에 걸린 건만 멈춰 사람이 승인, 반려, 다시 판정을 고르는 파이프라인"


PAGE = """<!DOCTYPE html>
<html lang="ko"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&family=Geist+Mono:wght@400;500&family=Noto+Sans+KR:wght@400;500;600&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
body{{background:{paper};color:{ink};font-family:{sans};padding:2rem}}
.diagram-container{{width:100%;overflow-x:auto}}
svg{{width:100%;min-width:{w}px;display:block}}
@media print{{.diagram-container{{overflow-x:visible}}svg{{min-width:0}}}}
</style></head>
<body><div class="diagram-container">
{svg}
</div></body></html>
"""

for name, fn in [("hitl-concept", hitl_concept), ("hitl-pipeline", hitl_pipeline)]:
    for skin, t in SKINS.items():
        d, w, h, title, desc = fn(t)
        slug = f"{name}-{skin}"
        html = PAGE.format(title=title, paper=t["paper"], ink=t["ink"], sans=SANS, w=w,
                           svg=d.svg(slug, w, h, title, desc))
        (OUT / f"{slug}.html").write_text(html, encoding="utf-8")
        print("wrote", slug)
