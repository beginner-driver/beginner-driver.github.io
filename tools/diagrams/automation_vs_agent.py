"""Diagrams for 2026-09-01-automation-vs-agent. Run: py automation_vs_agent.py && py shot.py automation-vs-agent who-decides if-vs-agent"""
from gen import D, build


def who_decides(t):
    d = D(t)
    # request -> three deciders
    d.line("M128,180 H156 Q164,180 164,172 V78 Q164,70 172,70 H198")
    d.line("M128,180 H198")
    d.line("M128,180 H156 Q164,180 164,188 V282 Q164,290 172,290 H198")
    # deciders -> same result
    d.line("M520,70 H552 Q560,70 560,78 V172 Q560,180 568,180 H598")
    d.line("M520,180 H598")
    d.line("M520,290 H552 Q560,290 560,282 V188 Q560,180 568,180 H598")
    # nodes
    d.oval(16, 156, 112, 48, "같은 요청")
    d.rect(200, 40, 320, 60, "사람이 하나씩 시킨다", sub="볼 곳: 입력과 판단 기준", sub_mono=False)
    d.rect(200, 150, 320, 60, "그래프가 순서를 정한다 (워크플로)", sub="볼 곳: 어느 조건에서 갈렸나", sub_mono=False)
    d.rect(200, 260, 320, 60, "모델이 다음을 고른다 (에이전트)", sub="볼 곳: 도구 · 관측 결과 · 반복 한도 · 승인",
           sub_mono=False, focal=True)
    d.oval(600, 152, 160, 56, "결과는 같다", sub="\"알림 보냄\"")
    return d, 776, 344, "다음 행동을 누가 정하나", "같은 요청과 같은 결과라도 사람, 그래프, 모델 중 누가 다음 행동을 골랐는지에 따라 문제가 생겼을 때 볼 곳이 다르다"


def if_vs_agent(t):
    d = D(t)
    d.line("M156,96 H196")
    d.line("M342,96 H410", accent=True)
    d.line("M562,96 H620")
    d.line("M270,140 V196")
    d.line("M487,120 V196", dashed=True)
    # labels
    d.label(364, 72, 24, "예", accent=True)
    d.label(280, 156, 44, "아니오")
    d.label(210, 16, 120, "규칙이 고른다")
    d.label(427, 16, 120, "모델이 고른다", accent=True)
    d.label(497, 150, 120, "새 사실이 필요할 때만")
    # nodes
    d.rect(16, 72, 140, 48, "HTTP Request", sub="공개 API 읽기", sub_mono=False)
    d.diamond(270, 96, 72, 44, ["제목·설명이", "모두 있나?"])
    d.rect(412, 72, 150, 48, "AI Agent", sub="의도 해석 · 요약", sub_mono=False, focal=True)
    d.oval(622, 72, 140, 48, "한 문장 요약")
    d.oval(190, 198, 160, 48, "확인 필요", sub="담당자 검토")
    d.rect(402, 198, 170, 48, "읽기 전용 도구", sub="외부 상태를 안 바꾼다", sub_mono=False)
    return d, 780, 268, "IF 노드와 AI Agent 노드", "값을 검사하는 IF 노드가 먼저 경로를 나누고, 통과한 것만 AI Agent가 해석하며 필요할 때만 읽기 전용 도구를 부른다"


if __name__ == "__main__":
    build([("who-decides", who_decides), ("if-vs-agent", if_vs_agent)])
