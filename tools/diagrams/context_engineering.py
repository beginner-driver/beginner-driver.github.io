"""Diagrams for 2026-08-25-context-engineering. Run: py context_engineering.py && py shot.py context-engineering context-budget strategy-map"""
from gen import D, build, SANS, esc


def _txt(x, y, s, color, anchor="middle", size=13, weight=500):
    return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" '
            f'font-family="{SANS}" text-anchor="{anchor}">{esc(s)}</text>')


def context_budget(t):
    d = D(t)
    # storage -> window arrows
    d.line("M75,76 V148")
    d.line("M189,76 V148")
    d.line("M348,76 V148", accent=True)
    d.line("M502,76 V148")
    d.line("M611,76 V148")
    d.label(266, 104, 164, "이번 판단에 필요한 조각만", accent=True)
    # storage (top)
    d.oval(20, 20, 224, 56, "고정 지시 · 도구 정의", sub="버전 · 소유자가 분명한 것")
    d.oval(248, 20, 200, 56, "문서 저장소", sub="정책 · 매뉴얼 · 원문")
    d.oval(452, 20, 100, 56, "메모리", sub="요약 · 결정")
    d.oval(556, 20, 110, 56, "대화 기록", sub="전체 이력")
    # one call = one window (bottom)
    d.rect(20, 150, 110, 56, "지시", sub="역할 · 금지 · 형식", sub_mono=False)
    d.rect(134, 150, 110, 56, "도구 목록", sub="이름 · 매개변수", sub_mono=False)
    d.rect(248, 150, 200, 56, "문서", sub="답의 근거", sub_mono=False, focal=True)
    d.rect(452, 150, 100, 56, "메모리", sub="확정 · 가정", sub_mono=False)
    d.rect(556, 150, 110, 56, "대화 이력", sub="최근 원문", sub_mono=False)
    d.nodes.append(f'<rect x="670" y="150" width="230" height="56" rx="6" fill="{t["paper"]}" stroke="{t["muted"]}" stroke-width="1.2" stroke-dasharray="5,4"/>')
    d.nodes.append(_txt(785, 176, "출력 예산", t["ink"], size=14, weight=600))
    d.nodes.append(_txt(785, 193, "답을 쓸 자리를 먼저 남긴다", t["soft"], size=12))
    d.nodes.append(_txt(460, 240, "한 번의 호출 = 하나의 컨텍스트 창. 입력과 출력이 같은 한도를 나눠 쓰고, 다음 호출에는 다시 조립된다", t["muted"], size=12))
    return d, 920, 260, "같은 창을 나눠 쓰는 다섯 재료", "저장소에서 이번 판단에 필요한 조각만 꺼내 지시, 도구 목록, 문서, 메모리, 대화 이력으로 창을 채우고, 출력 예산은 미리 남겨 둔다"


def strategy_map(t):
    d = D(t)
    for gx in (12, 592):
        d.nodes.append(f'<rect x="{gx}" y="36" width="316" height="316" rx="12" fill="{t["oval_fill"]}" stroke="{t["oval_stroke"]}" stroke-width="1"/>')
    d.nodes.append(_txt(170, 22, "선택 연산 · 이번 호출에 넣을 것", t["ink"], size=14, weight=600))
    d.nodes.append(_txt(750, 22, "상태 정책 · 여러 턴을 잇는 방식", t["ink"], size=14, weight=600))
    d.line("M328,206 H368", accent=True)
    d.line("M592,206 H552", accent=True)
    left = [("전체 투입", "실패: 무관한 규정이 핵심을 밀어낸다"),
            ("RAG (검색해서 넣기)", "실패: 예외 조항이 검색되지 않는다"),
            ("압축", "실패: 예외 · 가정이 사실처럼 남는다"),
            ("폐기", "실패: 필요한 근거까지 사라진다")]
    right = [("누적", "실패: 정정 전후가 함께 남아 충돌한다"),
             ("슬라이딩 윈도 (최근 N턴)", "실패: 오래된 금지 조건을 잃는다"),
             ("요약", "실패: 원문 연결이 끊긴다"),
             ("러닝 서머리", "정해진 칸을 갱신, 철회한 가정도 적는다")]
    for i, (name, sub) in enumerate(left):
        d.rect(28, 56 + i * 72, 284, 56, name, sub=sub, sub_mono=False)
    for i, (name, sub) in enumerate(right):
        d.rect(608, 56 + i * 72, 284, 56, name, sub=sub, sub_mono=False, focal=(i == 3))
    d.rect(370, 170, 180, 72, "이번 호출의 입력", sub="컨텍스트 창", sub_mono=False, focal=True)
    return d, 920, 370, "맥락 전략의 두 축", "이번 호출에 무엇을 넣을지 정하는 선택 연산 네 가지와, 여러 턴의 이력을 어떻게 이을지 정하는 상태 정책 네 가지가 함께 이번 호출의 입력을 만든다"


if __name__ == "__main__":
    build([("context-budget", context_budget), ("strategy-map", strategy_map)])
