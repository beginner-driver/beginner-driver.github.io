"""Diagrams for _posts/2026-09-10-issue-radar.md"""
from gen import D, build


def radar_flow(t):
    d = D(t)
    # row 1: fixed code steps
    d.line("M116,76 H146")
    d.line("M288,76 H318")
    d.line("M480,76 H510")
    d.line("M672,76 H788 Q796,76 796,84 V150", accent=True)
    d.label(806, 104, 60, "판단 구간", accent=True)
    # row 2: agent judgment, then back to code and human
    d.line("M704,180 H674")
    d.line("M600,218 V248")
    d.line("M690,274 H788 Q796,274 796,266 V210")
    d.line("M528,180 H498")
    d.line("M300,180 H272")
    d.line("M195,204 V248")
    d.label(610, 224, 44, "아니오")
    d.label(500, 156, 24, "예")
    # nodes
    d.oval(16, 52, 100, 48, "키워드 세트")
    d.rect(148, 48, 140, 56, "수집", sub="페이징 · 태그 정리", sub_mono=False)
    d.rect(320, 48, 160, 56, "제목 유사도로 묶기", sub="76건 → 63묶음", sub_mono=False)
    d.rect(512, 48, 160, 56, "이력 대조 · 라벨", sub="신규 · 후속 · 기존", sub_mono=False)
    d.rect(704, 152, 184, 56, "에이전트 판정", sub="A~F 항목 + 근거", focal=True, sub_mono=False)
    d.diamond(600, 180, 72, 38, ["제목·요약으로", "판단되나?"])
    d.rect(510, 250, 180, 48, "본문 조회", sub="필요할 때만 · 최대 3건", sub_mono=False)
    d.rect(300, 152, 196, 56, "등급 매핑 · 법령 대조", sub="법령명이 기사에 없으면 강등", sub_mono=False)
    d.oval(122, 156, 148, 48, "사람 승인", sub="틀린 것만 고친다")
    d.rect(110, 250, 170, 48, "확정 저장 · 엑셀", sub="승인 이후에만", sub_mono=False)
    return d, 904, 312, "이슈 레이더 흐름", "수집, 묶기, 이력 대조와 라벨은 코드가 정해진 순서로 처리하고, 에이전트는 A~F 항목과 근거만 판정하며 필요하면 본문을 최대 3건 조회한다. 등급 매핑과 법령명 대조는 다시 코드가 맡고, 사람이 승인한 뒤에만 저장과 엑셀 출력이 일어난다"


if __name__ == "__main__":
    build([("radar-flow", radar_flow)])
