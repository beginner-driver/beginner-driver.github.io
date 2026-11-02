"""Diagrams for 2026-09-16-routing-grounding. Run: py routing_grounding.py && py shot.py routing-grounding routing-flow grounding-layers"""
from gen import D, build


def routing_flow(t):
    d = D(t)
    # row 1 (cy=130): 문의 -> 분류 -> 판정 -> 근거 조립 -> 조회
    d.line("M112,130 H142")
    d.line("M304,130 H342")
    d.line("M456,130 H486")
    d.line("M640,130 H670")
    d.line("M400,86 V60")                                   # OTHER -> 범위 밖
    d.line("M400,174 V222 Q400,230 392,230 H104 Q96,230 96,238 V264")  # 확신도 낮음 -> 이관
    # row 2 (cy=290): 조회 -> 답변 -> 검사 -> 고객
    d.line("M748,158 V260")
    d.line("M672,290 H642")
    d.line("M488,290 H374", accent=True)                    # 통과
    d.line("M604,318 V338 Q604,346 612,346 H740 Q748,346 748,338 V320", dashed=True)  # 다시 생성
    d.line("M528,318 V364 Q528,372 520,372 H104 Q96,372 96,364 V316")  # 다시 위반 -> 이관
    # labels
    d.label(457, 106, 28, "처리")
    d.label(410, 62, 52, "OTHER")
    d.label(184, 222, 100, "확신도 < 0.5")
    d.label(413, 282, 36, "통과", accent=True)
    d.label(620, 338, 112, "위반 → 다시 생성")
    d.label(250, 364, 112, "다시 위반 → 이관")
    # nodes
    d.oval(16, 106, 96, 48, "문의")
    d.rect(144, 102, 160, 56, "분류 (모델)", sub="라우트 · 확신도 · 근거", sub_mono=False)
    d.diamond(400, 130, 56, 44, ["판정", "(정책)"])
    d.oval(330, 14, 140, 44, "범위 밖 안내")
    d.rect(488, 102, 152, 56, "근거 조립", sub="라우트에 맞는 장만", sub_mono=False)
    d.rect(672, 102, 152, 56, "값 조회", sub="도구가 조회 · 계산", sub_mono=False)
    d.rect(672, 262, 152, 56, "근거로만 답변", sub="조회 결과 + 매뉴얼", sub_mono=False)
    d.rect(488, 262, 152, 56, "숫자 출처 검사", sub="가드레일", sub_mono=False, focal=True)
    d.oval(232, 266, 140, 48, "고객에게 답변")
    d.oval(16, 266, 160, 48, "사람에게 이관")
    return d, 840, 396, "라우팅과 그라운딩의 흐름", "모델이 분류하고 정책이 판정한 뒤, 처리 경로에서는 라우트별 근거를 조립하고 값을 조회해 답하며, 답변의 숫자 출처를 검사해 통과하면 내보내고 거듭 위반하면 사람에게 넘긴다"


def grounding_layers(t):
    d = D(t)
    layers = [
        ("① 필요한 정책만 넣는다 — 답을 쓰기 전", "라우트에 맞는 장만 조립 · 배송 프롬프트에는 반품 배송비가 아예 없다", False),
        ("② 값은 조회한다 — 답을 쓰기 전", "공통 값은 매뉴얼에서 · 건마다 다른 값은 도구로 · 계산도 도구가 · 대상을 모르면 되묻기", False),
        ("③ 출처 없는 숫자를 잡는다 — 답을 쓴 뒤", "답변 속 숫자를 조회 결과 + 매뉴얼 고정값과 대조 · 위반이면 다시 생성, 거듭 위반이면 이관", True),
    ]
    h, gap, y = 56, 24, 52
    ys = []
    for _ in layers:
        ys.append(y)
        y += h + gap
    for y0, y1 in zip(ys, ys[1:]):
        d.line(f"M460,{y0 + h} V{y1 - 2}")
    d.label(330, 16, 260, "모델이 빈칸을 지어내지 못하게")
    for (name, sub, focal), y0 in zip(layers, ys):
        d.rect(40, y0, 840, h, name, sub=sub, focal=focal, sub_mono=False)
    return d, 920, y - gap + 24, "그라운딩의 세 겹", "필요한 정책만 넣고, 값은 조회하고, 답변 속 숫자의 출처를 조회 결과와 고정값에 대조해 검사하는 세 겹 장치"


if __name__ == "__main__":
    build([("routing-flow", routing_flow), ("grounding-layers", grounding_layers)])
