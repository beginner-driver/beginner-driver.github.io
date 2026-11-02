"""Diagrams for 2026-09-27-agent-evaluation (light + dark)."""
from gen import D, build


def eval_loop(t):
    d = D(t)
    # arrows
    d.line("M160,80 H190")
    d.line("M328,80 H358")
    d.line("M504,80 H534")
    d.line("M608,104 V182")
    d.line("M536,208 H506")
    d.line("M432,184 V108", accent=True, dashed=True)
    # labels
    d.label(442, 132, 64, "다음 가설", accent=True)
    # nodes
    d.oval(16, 56, 144, 48, "평가셋 고정", sub="예시용·측정용 분리")
    d.rect(192, 56, 136, 48, "기준선 측정", sub="지금 버전의 점수", sub_mono=False)
    d.rect(360, 56, 144, 48, "한 조건만 변경", sub="나머지는 그대로", focal=True, sub_mono=False)
    d.rect(536, 56, 144, 48, "같은 자로 재측정", sub="분모 고정", sub_mono=False)
    d.rect(536, 184, 144, 48, "실패 원문 읽기", sub="숫자가 못 보는 것", sub_mono=False)
    d.oval(360, 184, 144, 48, "판정", sub="채택 · 축소 · 폐기")
    return d, 700, 256, "에이전트 품질을 재는 순서", "평가셋을 고정하고 기준선을 잰 뒤, 한 조건만 바꿔 같은 자로 다시 재고, 실패 원문을 읽어 판정하는 반복"


def grader_ladder(t):
    d = D(t)
    # arrows
    d.line("M196,80 H226")
    d.line("M408,80 H438")
    d.line("M620,80 H650")
    d.line("M16,156 H828")
    # labels
    d.label(232, 164, 380, "오른쪽으로 갈수록 비용이 들고, 같은 답에 같은 점수가 덜 나온다")
    # nodes
    d.rect(16, 52, 180, 56, "결정적 검사", sub="테스트 · 스키마 · forbid", sub_mono=False)
    d.rect(228, 52, 180, 56, "참조 답과 비교", sub="exact match · F1", sub_mono=False)
    d.rect(440, 52, 180, 56, "LLM 심판", sub="루브릭 + 원문 근거", focal=True, sub_mono=False)
    d.rect(652, 52, 180, 56, "사람 표본", sub="심판과의 일치율 확인", sub_mono=False)
    return d, 848, 200, "채점 방법의 사다리", "결정적 검사, 참조 답 비교, LLM 심판, 사람 표본 순으로 비용과 흔들림이 커지는 채점 방법"


if __name__ == "__main__":
    build([("eval-loop", eval_loop), ("grader-ladder", grader_ladder)])
