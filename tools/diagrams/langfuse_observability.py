"""Diagrams for 2026-11-02-langfuse-observability. Run: py langfuse_observability.py && py shot.py langfuse-observability trace-tree read-backward"""
from gen import D, build


def trace_tree(t):
    d = D(t)
    kids = [
        ("safety", "span · 위기 표현 감지 여부", False),
        ("choose-tools", "generation · 고른 도구 · 확신도 · 누가 정했나", False),
        ("tool:get_weather", "span · 인자 · 결과 · 성공 여부", False),
        ("reply", "generation · 받은 입력 · 답 · 토큰 · 첫 글자 시각", True),
        ("memory-update", "generation · 추가·수정·삭제한 기억", False),
    ]
    for i, _ in enumerate(kids):
        y = 120 + 68 * i
        d.line(f"M100,96 V{y + 26} H238")
    d.rect(16, 40, 170, 56, "chat-turn", sub="트레이스 · 메시지 하나", sub_mono=False, focal=True)
    for i, (name, sub, focal) in enumerate(kids):
        d.rect(240, 120 + 68 * i, 380, 52, name, sub=sub, sub_mono=False, focal=focal)
    return d, 640, 480, "한 턴의 트레이스 구조", "메시지 하나가 트레이스가 되고, 안전장치·도구 선택·도구 실행·답 만들기·기억 정리가 그 아래 관찰 단위로 붙으며 단계마다 남길 값이 다르다"


def read_backward(t):
    d = D(t)
    xs = [16, 236, 456, 676]
    d.line("M206,88 H234")
    d.line("M426,88 H454")
    d.line("M646,88 H674")
    d.line("M771,60 V40 Q771,32 763,32 H119 Q111,32 111,40 V58", accent=True)
    for x in xs:
        d.line(f"M{x + 95},116 V182", dashed=True)
    d.label(371, 24, 140, "거슬러 올라가며 읽기", accent=True)
    tops = [("choose-tools", "고른 도구 · 인자"), ("tool 실행", "결과 · 성공 여부"),
            ("reply 입력", "모델이 받은 도구 결과"), ("reply 출력", "사용자가 본 답")]
    for x, (name, sub) in zip(xs, tops):
        d.rect(x, 60, 190, 56, name, sub=sub, sub_mono=False, focal=(name == "reply 출력"))
    fixes = [("선택 프롬프트·규칙", "고른 도구가 틀렸다"), ("도구 코드", "도구가 실패했다"),
             ("답 만들기 프롬프트", "결과는 맞는데 답이 틀렸다"), ("몇 번 더 보내 보기", "한 번으로 단정하지 않는다")]
    for x, (name, sub) in zip(xs, fixes):
        d.oval(x, 184, 190, 60, name, sub=sub)
    return d, 882, 264, "거슬러 올라가며 읽기", "사용자가 본 답에서 시작해 답이 받은 입력, 도구 결과, 도구 선택 순으로 거슬러 올라가고, 처음 어긋난 단계에 따라 고칠 곳이 갈린다"


if __name__ == "__main__":
    build([("trace-tree", trace_tree), ("read-backward", read_backward)])
