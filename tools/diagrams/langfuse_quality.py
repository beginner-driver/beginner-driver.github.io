"""Diagrams for 2026-11-03-langfuse-quality. Run: py langfuse_quality.py && py shot.py langfuse-quality quality-loop prompt-labels"""
from gen import D, build


def quality_loop(t):
    d = D(t)
    xs = [16, 196, 376, 556, 736]
    for x in xs[:-1]:
        d.line(f"M{x + 160},54 H{x + 178}")
    d.line("M816,84 V130", accent=True)
    d.line("M736,160 H104 Q96,160 96,152 V86", dashed=True)
    d.label(316, 152, 200, "새 실패는 데이터셋 항목으로 더한다")
    steps = [("트레이스 읽기", "처음 어긋난 단계"), ("실패 유형표", "판정 기준 문장"),
             ("데이터셋·평가자", "실패+정상 · 앞 단계 고정"), ("실험 2~3회", "고친 유형 + 회귀"),
             ("내보내기", "라벨 옮기기 · 코드 PR")]
    for x, (name, sub) in zip(xs, steps):
        d.rect(x, 24, 160, 60, name, sub=sub, sub_mono=False, focal=(name == "내보내기"))
    d.oval(736, 132, 160, 56, "평가 게이트", sub="라벨 변경 전 · 머지 전")
    return d, 912, 208, "품질을 지키는 흐름", "실패한 트레이스를 읽어 유형과 판정 기준을 정하고, 데이터셋과 평가자로 고치기 전후를 두세 번 실험한 뒤 통과한 것만 내보내며, 평가 게이트가 다음 수정에도 같은 확인을 걸고 새 실패는 데이터셋으로 돌아간다"


def prompt_labels(t):
    d = D(t)
    d.line("M326,68 V128", accent=True)
    d.line("M546,68 V128")
    d.line("M236,46 H114 Q106,46 106,54 V128", dashed=True)
    d.label(118, 38, 110, "롤백: 되돌려 붙임")
    d.oval(236, 24, 180, 44, "production", sub="사용자가 받는 버전")
    d.oval(456, 24, 180, 44, "staging", sub="실험 · staging 서버")
    vers = [("버전 1", "코드에서 옮긴 문장"), ("버전 2", "규칙 두 줄 추가"), ("버전 3", "다음 수정안")]
    for i, (name, sub) in enumerate(vers):
        d.rect(16 + 220 * i, 130, 180, 56, name, sub=sub, sub_mono=False, focal=(i == 1))
    d.label(16, 212, 620, "버전은 고칠 수 없고 쌓이기만 한다 · 배포는 실험을 통과한 버전으로 라벨을 옮기는 일")
    return d, 652, 240, "프롬프트 버전과 라벨", "프롬프트 버전은 쌓이기만 하고, production과 staging 라벨이 버전 하나씩을 가리키며, 배포와 롤백은 코드 재배포 없이 라벨을 옮기는 일이다"


if __name__ == "__main__":
    build([("quality-loop", quality_loop), ("prompt-labels", prompt_labels)])
