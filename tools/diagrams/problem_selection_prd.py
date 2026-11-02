"""Diagrams for 2026-07-11-problem-selection-prd."""
from gen import D, build


def prd_flow(t):
    d = D(t)
    # arrows (main row y=96)
    d.line("M100,96 H128")
    d.line("M270,96 H298")
    d.line("M472,96 H500")
    d.line("M642,96 H670")
    d.line("M788,96 H814", accent=True)
    d.line("M730,136 V196 H580 Q572,196 572,188 V126")  # 아니오 → PRD 고침
    # labels
    d.label(791, 68, 20, "예", accent=True)
    d.label(592, 186, 132, "아니오 · PRD 한 줄 고침")
    # nodes
    d.oval(12, 72, 88, 48, "아이디어")
    d.rect(130, 68, 140, 56, "문제 고르기", sub="매번 하는 귀찮은 일", sub_mono=False)
    d.rect(300, 68, 172, 56, "네 동작으로 쪼개기", sub="분해·패턴·추상화·알고리즘", sub_mono=False)
    d.rect(502, 68, 140, 56, "PRD 한 장", sub="Must만 · Won't 적기", focal=True, sub_mono=False)
    d.diamond(730, 96, 58, 40, ["AI 계획이", "맞나?"])
    d.oval(816, 72, 96, 48, "만들기", sub='"진행"')
    return d, 924, 224, "AI에게 맡기기 전의 흐름", "문제를 고르고 쪼개서 PRD 한 장으로 정리한 뒤, AI의 계획이 맞을 때만 진행시키고 다르면 PRD를 고치는 흐름"


def mvp_cut(t):
    d = D(t)
    # arrows
    d.line("M136,100 H182")
    d.line("M376,100 H470", accent=True)       # 아니오 → Must
    d.line("M652,100 H698")
    d.line("M280,156 V206")                     # 예·애매 → 다음 버전
    # labels
    d.label(401, 76, 44, "아니오", accent=True)
    d.label(290, 172, 92, "예 · 애매하면")
    # nodes
    d.oval(16, 76, 120, 48, "기능 후보", sub="떠오른 기능 전부")
    d.diamond(280, 100, 96, 56, ["이 기능 없이도", "핵심 문제를", "풀 수 있나?"])
    d.rect(472, 72, 180, 56, "Must", sub="MVP에서 만든다", focal=True, sub_mono=False)
    d.oval(700, 72, 200, 56, "첫 조각 (MVP)", sub="핵심 행동 하나가 끝까지 돈다")
    d.rect(170, 208, 220, 56, "다음 버전 목록", sub="Should · Could · Won't(5개 이상)", sub_mono=False)
    return d, 916, 288, "MVP 범위 자르기", "기능 후보마다 이 기능 없이도 핵심 문제를 풀 수 있는지 묻고, 꼭 필요한 Must만 첫 조각에 넣고 나머지는 다음 버전 목록으로 보내는 흐름"


if __name__ == "__main__":
    build([("prd-flow", prd_flow), ("mvp-cut", mvp_cut)])
