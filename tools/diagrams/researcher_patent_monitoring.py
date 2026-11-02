"""Diagrams for _posts/2026-10-14-researcher-patent-monitoring.md"""
from gen import D, build


def search_flow(t):
    d = D(t)
    # main row y=80
    d.line("M152,80 H174")
    d.line("M332,80 H354")
    d.line("M496,80 H518")
    d.line("M692,80 H714")
    d.line("M254,150 V110")
    d.line("M810,108 V158", accent=True)
    d.rect(16, 52, 136, 56, "이름 표기", sub="자동 4가지 + 원어 이름", sub_mono=False)
    d.rect(176, 52, 156, 56, "OPS 검색", sub="이름 AND 분야 조건", sub_mono=False)
    d.rect(356, 52, 140, 56, "특허 묶음 확장", sub="번호만 조회", sub_mono=False)
    d.rect(520, 52, 172, 56, "근거 붙이기", sub="출원인 · 소속 · 공동발명", sub_mono=False)
    d.rect(716, 52, 188, 56, "근거 순 정렬", sub="강 · 중 · 없음", sub_mono=False)
    d.rect(176, 152, 156, 56, "분야 조건", sub="CPC 3 · IPC 3 · 키워드 5", sub_mono=False)
    d.rect(716, 160, 188, 56, "사람이 판단", sub="확정 · 기각은 도구가 안 함", focal=True, sub_mono=False)
    return d, 920, 236, "특허 검색 흐름", "이름 표기와 분야 조건으로 검색하고 특허 묶음으로 펼친 뒤, 출원인과 공동발명 근거를 붙여 정렬하고 판단은 사람이 한다"


def missing_steps(t):
    d = D(t)
    d.line("M222,84 H272")
    d.line("M486,84 H536", accent=True)
    d.label(226, 58, 44, "−35")
    d.label(490, 58, 44, "−2", accent=True)
    d.rect(16, 48, 206, 72, "누락 37건", sub="사람 검색식 조건 그대로", sub_mono=False)
    d.rect(274, 48, 212, 72, "누락 2건", sub="CPC 하위 코드 포함", sub_mono=False)
    d.rect(538, 48, 212, 72, "누락 0건", sub="IPC 3개 추가", focal=True, sub_mono=False)
    d.label(16, 140, 734, "", lines=["본인 특허 913건 기준 · 하위 코드만 붙은 문서 35건 · CPC가 비었거나 다른 코드인 문서 2건"])
    return d, 766, 172, "본인 특허 누락이 줄어든 과정", "사람 조건 그대로 37건, CPC 하위 코드를 포함하면 2건, IPC를 추가하면 0건으로 줄었다"


if __name__ == "__main__":
    build([("search-flow", search_flow), ("missing-steps", missing_steps)])
