"""Diagrams for _posts/2026-11-02-langfuse-friend-agent.md"""
from gen import D, build


def sampling_drop(t):
    d = D(t)
    # before (#36·#37): chat-turn inherits the sampled-out request span
    d.line("M136,68 H168")
    d.line("M340,68 H372")
    d.line("M524,68 H566")
    # after (#38): start the trace from an empty context, flush at turn end
    d.line("M136,198 H168")
    d.line("M340,198 H372", accent=True)
    d.line("M524,198 H556", accent=True)
    d.line("M688,198 H720", accent=True)
    d.label(16, 12, 200, "수정 전: 13건 중 6건만 도착")
    d.label(16, 142, 220, "수정 후: 로컬 재현 3건 모두 도착", accent=True)
    d.oval(16, 44, 120, 48, "채팅 요청", sub="traceparent …-00", sub_mono=True)
    d.rect(170, 40, 170, 56, "Cloud Run 요청 추적", sub="표본 제외 (sampled=0)", sub_mono=False)
    d.rect(374, 40, 150, 56, "chat-turn", sub="요청의 하위로 생성", sub_mono=False)
    d.oval(568, 44, 170, 48, "오류 없이 사라짐", sub="서버는 200", sub_mono=False)
    d.oval(16, 174, 120, 48, "채팅 요청", sub="traceparent …-00", sub_mono=True)
    d.rect(170, 170, 170, 56, "빈 컨텍스트", sub="요청 추적을 안 물려받음", sub_mono=False)
    d.rect(374, 170, 150, 56, "chat-turn", sub="새 트레이스의 시작", focal=True, sub_mono=False)
    d.rect(558, 170, 130, 56, "flush()", sub="턴이 끝나면 바로 전송", sub_mono=False)
    d.oval(722, 174, 140, 48, "Langfuse 도착")
    return d, 880, 248, "트레이스가 사라진 경로와 고친 경로", "수정 전에는 Cloud Run이 요청에 붙인 traceparent가 표본 제외(sampled=0)이면 그 하위로 만든 chat-turn 기록이 오류 없이 사라졌다. 수정 후에는 chat-turn을 빈 컨텍스트에서 새 트레이스로 시작하고, 턴이 끝날 때 flush로 바로 보내 Langfuse에 도착한다"


if __name__ == "__main__":
    build([("sampling-drop", sampling_drop)])
