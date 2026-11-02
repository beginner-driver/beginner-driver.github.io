"""Diagrams for _posts/2026-08-29-claude-code-rag-bot.md"""
from gen import D, build, esc, SANS


def rag_pipeline(t):
    d = D(t)
    d.line("M108,76 H134")
    d.line("M296,76 H322")
    d.line("M484,76 H518")
    d.line("M648,76 H688", accent=True)
    d.line("M584,116 V170")
    d.line("M785,104 V170")
    d.label(656, 52, 24, "예", accent=True)
    d.label(594, 132, 44, "아니오")
    d.label(240, 14, 420, "전부 방문자의 브라우저와 컴퓨터 안에서 실행 (서버 없음)", accent=True)
    d.oval(16, 52, 92, 48, "질문")
    d.rect(136, 48, 160, 56, "질문 임베딩", sub="embeddinggemma · 브라우저", sub_mono=False)
    d.rect(324, 48, 160, 56, "하이브리드 검색", sub="코사인 10 + BM25 5", sub_mono=False)
    d.diamond(584, 76, 64, 40, ["최고 유사도", "0.55 이상?"])
    d.rect(690, 48, 190, 56, "상위 5개 청크로 답변", sub="qwen3.5:2b · 로컬 Ollama", focal=True, sub_mono=False)
    d.oval(504, 172, 160, 52, "답변 보류", sub="LLM 호출 없음")
    d.rect(690, 172, 190, 52, "자동 채점 (judge)", sub="같은 모델 · JSON 6필드", sub_mono=False)
    return d, 896, 244, "Claude Code 안내봇 흐름", "질문을 브라우저에서 임베딩하고 하이브리드 검색한 뒤, 최고 유사도가 0.55 미만이면 답변을 보류하고, 이상이면 상위 5개 청크로 로컬 Ollama가 답한 뒤 같은 모델이 채점하는 흐름"


def score_strip(t):
    d = D(t)
    x = lambda s: 170 + (s - 0.45) * 1750  # 0.45 -> 170, 0.85 -> 870
    inside = [0.789, 0.767, 0.654, 0.819, 0.803, 0.834, 0.724, 0.745, 0.767, 0.829,
              0.737, 0.776, 0.701, 0.729, 0.813, 0.717, 0.710, 0.836, 0.721, 0.723]
    outside = [(0.471, "날씨", "0.47"), (0.585, "파이썬 정렬", "0.59"), (0.662, "Messages API", "0.66")]
    tx = lambda px, py, s, c, size=12, w=500, anchor="middle": d.nodes.append(
        f'<text x="{px}" y="{py}" fill="{c}" font-size="{size}" font-weight="{w}" font-family="{SANS}" text-anchor="{anchor}">{esc(s)}</text>')
    # threshold
    tl = x(0.55)
    d.arrows.append(f'<path d="M{tl},30 V176" stroke="{t["accent"]}" stroke-width="1.4" stroke-dasharray="5,4" fill="none"/>')
    tx(tl, 22, "임계값 0.55", t["accent"], w=600)
    # axis
    d.arrows.append(f'<path d="M{x(0.45)},176 H{x(0.85)}" stroke="{t["muted"]}" stroke-width="1"/>')
    for s in (0.5, 0.6, 0.7, 0.8):
        d.arrows.append(f'<path d="M{x(s)},176 V182" stroke="{t["muted"]}" stroke-width="1"/>')
        tx(x(s), 198, f"{s:.1f}", t["soft"], size=11)
    tx(x(0.65), 220, "질문과 가장 가까운 청크의 코사인 유사도", t["soft"], size=11)
    # rows
    tx(16, 74, "범위 안 질문 20개", t["ink"], size=13, w=600, anchor="start")
    tx(16, 140, "범위 밖 질문 3개", t["ink"], size=13, w=600, anchor="start")
    placed = []
    for s in sorted(inside):
        dy = sum(abs(s - p) < 0.007 for p in placed)
        placed.append(s)
        d.nodes.append(f'<circle cx="{x(s)}" cy="{70 - dy * 10}" r="5" fill="{t["node"]}" stroke="{t["ink"]}" stroke-width="1.2"/>')
    tx(x(0.654), 96, "최저 0.654", t["soft"], size=11)
    for s, name, shown in outside:
        d.nodes.append(f'<circle cx="{x(s)}" cy="136" r="5.5" fill="{t["accent"]}"/>')
        tx(x(s), 160, f"{name} {shown}", t["muted"], size=11)
    return d, 900, 236, "범위 안과 밖 질문의 최고 유사도", "범위 안 질문 20개의 최고 유사도는 0.654에서 0.836 사이이고, 범위 밖 질문 3개는 0.471, 0.585, 0.662였다. 임계값 0.55는 날씨 질문 하나만 걸렀고 Messages API 질문은 범위 안 최저값보다 높았다"


if __name__ == "__main__":
    build([("rag-pipeline", rag_pipeline), ("score-strip", score_strip)])
