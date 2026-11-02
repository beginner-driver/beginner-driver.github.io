"""Diagrams for _posts/2026-09-17-startup-package-agent.md"""
from gen import D, build


def startup_flow(t):
    d = D(t)
    # main row y=76
    d.line("M112,76 H142")
    d.line("M288,76 H306")
    d.line("M452,76 H478", accent=True)
    d.line("M656,76 H686")
    d.line("M788,104 V174")                                         # 통과
    d.line("M380,118 V174")                                         # 이관
    d.line("M540,104 V182 Q540,190 532,190 H462")                   # 도구 상한
    d.line("M704,104 V210 Q704,218 696,218 H462")                   # 재시도 소진
    d.line("M768,48 V36 Q768,30 762,30 H574 Q568,30 568,36 V46", dashed=True)  # 재시도
    # labels
    d.label(453, 68, 22, "예", accent=True)
    d.label(358, 136, 44, "아니오")
    d.label(766, 130, 44, "통과")
    d.label(496, 136, 88, "도구 4회 초과")
    d.label(596, 210, 76, "재시도 소진")
    d.label(572, 4, 200, "위반이면 이유를 알려 주고 1회 재시도")
    # nodes
    d.oval(16, 52, 96, 48, "문의 한 줄")
    d.rect(144, 48, 144, 56, "카테고리 판정", sub="6개 중 하나 + 확신도", sub_mono=False)
    d.diamond(380, 76, 74, 42, ["확신도 0.5 이상", "+ 범위 안?"])
    d.rect(480, 48, 176, 56, "근거 조회 후 답변", sub="그 카테고리 도구만 묶음", focal=True, sub_mono=False)
    d.rect(688, 48, 160, 56, "가드레일 검증", sub="답변 속 숫자의 출처", sub_mono=False)
    d.oval(728, 176, 120, 48, "답변")
    d.rect(300, 176, 160, 56, "이관 · 범위밖 안내", sub="담당 기관으로", sub_mono=False)
    return d, 870, 248, "창업패키지 문의 응대 흐름", "문의를 6개 카테고리 중 하나로 판정하고, 확신도가 0.5 이상이며 범위 안일 때만 그 카테고리의 도구로 근거를 조회해 답한다. 답변 속 숫자는 가드레일이 도구 결과와 대조하고, 위반이면 이유를 알려 한 번 다시 답하게 하며, 재시도를 다 쓰거나 도구 호출이 4회를 넘으면 이관한다"


if __name__ == "__main__":
    build([("startup-flow", startup_flow)])
