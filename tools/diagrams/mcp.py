"""Diagrams for 2026-09-07-mcp. Run: py mcp.py && py shot.py mcp mcp-roles mcp-context-load"""
from gen import D, build, SANS, esc


def box(d, x, y, w, h, title):
    """Container drawn under nodes, title at top-left."""
    t = d.t
    d.arrows.insert(0, f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{t["oval_fill"]}" stroke="{t["oval_stroke"]}" stroke-width="1" stroke-dasharray="4,3"/>')
    d.arrows.insert(1, f'<text x="{x + 14}" y="{y + 22}" fill="{t["muted"]}" font-size="12" font-weight="600" font-family="{SANS}">{esc(title)}</text>')


def mcp_roles(t):
    d = D(t)
    box(d, 16, 40, 276, 236, "호스트 (Claude Code, OpenCode)")
    # host -> servers (MCP channel)
    d.line("M262,108 H430", accent=True)
    d.line("M262,220 H430", accent=True)
    # servers -> data (server's own access)
    d.line("M610,108 H700")
    d.line("M610,220 H700")
    # labels
    d.label(316, 84, 100, "stdio", accent=True)
    d.label(306, 196, 116, "Streamable HTTP", accent=True)
    d.label(282, 8, 160, "① 호스트 ↔ 서버: MCP 규약", accent=True)
    d.label(596, 8, 200, "② 서버 ↔ 업무 자료: 서버 구현")
    d.label(616, 84, 78, "파일 읽기")
    d.label(616, 196, 78, "API · DB")
    # nodes
    d.rect(40, 80, 222, 56, "MCP 클라이언트 A", sub="서버 하나와 대화", sub_mono=False)
    d.rect(40, 192, 222, 56, "MCP 클라이언트 B", sub="서버 하나와 대화", sub_mono=False)
    d.rect(432, 80, 178, 56, "로컬 MCP 서버", sub="호스트가 직접 시작", sub_mono=False, focal=True)
    d.rect(432, 192, 178, 56, "원격 MCP 서버", sub="https://…/mcp", focal=True)
    d.oval(702, 84, 190, 48, "내 컴퓨터의 자료", sub="data/week-one.json", sub_mono=True)
    d.oval(702, 196, 190, 48, "사내 시스템 · 외부 서비스")
    return d, 908, 296, "MCP의 세 역할과 두 통로", "호스트 안의 클라이언트가 서버마다 하나씩 붙어 stdio나 HTTP로 MCP 메시지를 주고받고, 서버가 업무 자료에 닿는 방식은 서버 구현이 정한다"


def mcp_context_load(t):
    d = D(t)
    xs = [16, 238, 460, 682]
    names = [("① 서버 연결", "tools/list로 목록 받기"), ("② 도구 정의 로드", "이름 · 설명 · 스키마"),
             ("③ 호출", "tools/call"), ("④ 결과 읽기", "반환된 업무 자료")]
    for x in xs[:-1]:
        d.line(f"M{x + 200},120 H{x + 220}")
    for i, (x, (n, s)) in enumerate(zip(xs, names)):
        d.rect(x, 92, 200, 56, n, sub=s, sub_mono=False, focal=i in (1, 3))
    # burden brackets
    d.line("M338,88 V60", accent=True)
    d.line("M782,88 V60", accent=True)
    d.label(222, 20, 232, "", accent=True, lines=["실행 전 부담: 안 쓸 도구의 설명", "→ Tool Search로 필요한 정의만"])
    d.label(630, 20, 270, "", accent=True, lines=["실행 후 부담: 너무 큰 결과", "→ 조회 범위 좁히기 · Code Mode로 거르기"])
    d.label(16, 166, 884, "지연 로딩은 ②만 줄인다. ④가 수천 줄이면 문맥 부담은 그대로다")
    return d, 916, 192, "도구가 많을 때 문맥 부담이 생기는 두 자리", "연결부터 결과 읽기까지 네 단계 중 도구 정의 로드는 실행 전 부담, 결과 읽기는 실행 후 부담이고, 줄이는 방법이 서로 다르다"


if __name__ == "__main__":
    build([("mcp-roles", mcp_roles), ("mcp-context-load", mcp_context_load)])
