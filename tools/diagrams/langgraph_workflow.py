"""Diagrams for 2026-09-13-langgraph-workflow. Run: py langgraph_workflow.py && py shot.py langgraph-workflow graph-anatomy send-fanout"""
from gen import D, build


def graph_anatomy(t):
    d = D(t)
    # main row (y=172)
    d.line("M112,172 H148")
    d.line("M300,172 H338")
    d.line("M490,172 H531")
    d.line("M677,172 H742", accent=True)
    # loop back over the top
    d.line("M605,128 V68 Q605,60 597,60 H233 Q225,60 225,68 V146", dashed=True)
    # hand-off when the round limit is reached
    d.line("M605,216 V244")
    # nodes read the shared State
    d.line("M225,260 V198", dashed=True)
    d.line("M415,260 V198", dashed=True)
    # labels
    d.label(686, 148, 48, "통과", accent=True)
    d.label(355, 52, 120, "부족하면 다시")
    d.label(614, 224, 36, "상한")
    # nodes
    d.oval(16, 150, 96, 44, "START")
    d.rect(150, 148, 150, 48, "초안 작성", sub="draft")
    d.rect(340, 148, 150, 48, "점검", sub="check")
    d.diamond(605, 172, 72, 44, ["기준을", "넘었나?"])
    d.oval(744, 150, 96, 44, "END")
    d.oval(530, 246, 150, 48, "사람에게 넘김", sub="횟수 상한 도달")
    d.rect(150, 262, 340, 52, "State (공용 데이터)", sub="노드는 바꾼 키만 돌려주고, 그래프가 병합한다", sub_mono=False, focal=True)
    return d, 860, 332, "LangGraph 그래프의 구성", "노드가 공용 State를 읽고 바꾼 키만 돌려주며, 조건부 엣지가 통과·재시도·사람에게 넘김 중 다음 길을 고른다"


def send_fanout(t):
    d = D(t)
    d.line("M136,150 H168")
    # Send fan-out: one branch per item
    d.line("M300,150 H332 Q340,150 340,142 V70 Q340,62 348,62 H378", accent=True)
    d.line("M300,150 H378", accent=True)
    d.line("M300,150 H332 Q340,150 340,158 V230 Q340,238 348,238 H378", accent=True)
    # fan-in into the next node
    d.line("M530,62 H562 Q570,62 570,70 V142 Q570,150 578,150 H598")
    d.line("M530,150 H598")
    d.line("M530,238 H562 Q570,238 570,230 V158 Q570,150 578,150 H598")
    d.line("M750,150 H788")
    # labels
    d.label(16, 100, 284, "모아서 처리: 다른 기사를 봐야 답한다")
    d.label(370, 14, 170, "펼쳐서 처리: 한 건만 본다", accent=True)
    d.label(600, 100, 150, "리듀서로 이어 붙인다")
    d.label(256, 250, 76, "Send × N", accent=True)
    # nodes
    d.rect(16, 126, 120, 48, "수집", sub="중복 거르기", sub_mono=False)
    d.rect(170, 126, 130, 48, "선별", sub="상대평가", sub_mono=False)
    d.rect(380, 40, 150, 44, "요약 워커", sub="기사 1", sub_mono=False, focal=True)
    d.rect(380, 128, 150, 44, "요약 워커", sub="기사 2", sub_mono=False, focal=True)
    d.rect(380, 216, 150, 44, "요약 워커", sub="기사 N", sub_mono=False, focal=True)
    d.rect(600, 126, 150, 48, "검수", sub="모인 결과를 한 번에", sub_mono=False)
    d.oval(790, 128, 90, 44, "END")
    return d, 896, 284, "Send로 펼치고 리듀서로 모으기", "다른 항목을 봐야 하는 수집과 선별은 모아서 처리하고, 한 건만 보면 되는 요약은 Send로 기사 수만큼 워커를 띄운 뒤 리듀서로 결과를 합친다"


if __name__ == "__main__":
    build([("graph-anatomy", graph_anatomy), ("send-fanout", send_fanout)])
