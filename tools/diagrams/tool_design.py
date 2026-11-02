"""Diagrams for 2026-08-26-tool-design. Run: py tool_design.py && py shot.py tool-design tool-call-loop safety-layers"""
from gen import D, build


def tool_call_loop(t):
    d = D(t)
    # row 1: request -> model -> harness -> tool  (cy=96)
    d.line("M136,96 H168")
    d.line("M372,96 H418")
    d.line("M632,96 H688")
    # result back: tool -> model row 2
    d.line("M790,124 V218 Q790,226 782,226 H374", accent=True)
    # chained call: model row 2 -> model row 1
    d.line("M300,198 V126", dashed=True)
    # model row 2 -> final answer
    d.line("M170,226 H138")
    # labels
    d.label(380, 72, 34, "②")
    d.label(638, 72, 44, "③ 실행")
    d.label(500, 202, 150, "④ 결과를 모델 입력으로", accent=True)
    d.label(310, 150, 64, "연쇄 호출")
    d.label(170, 36, 200, "실패 1 · 잘못 고름", accent=True)
    d.label(170, 262, 200, "실패 2 · 잘못 읽음", accent=True)
    d.label(420, 136, 210, "실패 3 · 같은 실수 반복", accent=True)
    # nodes
    d.oval(16, 72, 120, 48, "요청", sub="① 도구 정의 포함")
    d.rect(170, 68, 202, 56, "모델: 도구 고르기", sub="호출 요청(JSON)만 쓴다", sub_mono=False)
    d.rect(420, 68, 212, 56, "하네스", sub="허용 목록 · 인자 검사", sub_mono=False, focal=True)
    d.rect(690, 68, 200, 56, "도구", sub="get_inventory(...)")
    d.rect(170, 198, 202, 56, "모델: 결과 읽고 답", sub="⑤ 반환값을 근거로", sub_mono=False)
    d.oval(16, 202, 120, 48, "최종 답")
    return d, 906, 290, "도구 호출 한 바퀴", "모델은 호출 요청만 쓰고, 하네스가 검사하고 실행해 결과를 모델에 돌려주며, 실패는 고르기·읽기·반복 세 순간에 생긴다"


def safety_layers(t):
    d = D(t)
    layers = [
        ("① 입력층", "구분자 · 격리 — 문서 속 문장을 명령으로 읽지 않게 가른다", False, 48),
        ("② 모델층", "지시 위계 학습 — 시스템 지시를 바깥 문장보다 우선한다", False, 48),
        ("③ 하네스층 — 가장 두꺼운 실행 경계", "최소 권한 · 서버에서 다시 검사 · 되돌리기 어려운 동작은 승인 게이트", True, 64),
        ("④ 운영층", "평가 세트 · 회귀 확인 · 감시", False, 48),
    ]
    y = 56
    ys = []
    for name, sub, focal, h in layers:
        ys.append((y, h))
        y += h + 24
    for (y0, h0), (y1, _) in zip(ys, ys[1:]):
        d.line(f"M460,{y0 + h0} V{y1 - 2}")
    d.label(330, 16, 260, "모델의 호출 제안이 실행되기까지")
    for (name, sub, focal, h), (y0, _) in zip(layers, ys):
        d.rect(40, y0, 840, h, name, sub=sub, focal=focal, sub_mono=False)
    return d, 920, y, "안전 4층", "모델의 호출 제안은 입력층, 모델층, 하네스층, 운영층을 거쳐 실행되고, 그중 하네스층이 가장 두꺼운 실행 경계다"


if __name__ == "__main__":
    build([("tool-call-loop", tool_call_loop), ("safety-layers", safety_layers)])
