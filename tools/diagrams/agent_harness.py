"""Diagrams for 2026-09-02-agent-harness. Run: py agent_harness.py && py shot.py agent-harness harness-loop harness-experiment"""
from gen import D, build


def harness_loop(t):
    d = D(t)
    # row 1 (cy=100): 요청 -> 상태 -> 모델 -> 하네스 검사 -> 도구 실행
    d.line("M112,100 H142")
    d.line("M294,100 H324")
    d.line("M476,100 H506")
    d.line("M658,100 H688")
    # 도구 실행 -> 관측
    d.line("M765,128 V188")
    # 모델 -> 끝내기
    d.line("M401,128 V188")
    # 관측 -> 상태 (다음 호출의 입력)
    d.line("M765,246 V282 Q765,290 757,290 H227 Q219,290 219,282 V130", accent=True)
    # labels: functions on top, flow labels on arrows
    d.label(134, 40, 170, "컨텍스트 관리 · 경험 축적", accent=True)
    d.label(331, 40, 140, "행동 포맷 · 반성", accent=True)
    d.label(548, 40, 70, "권한", accent=True)
    d.label(730, 40, 70, "격리", accent=True)
    d.label(411, 150, 70, "답 · 한도")
    d.label(420, 280, 170, "관측을 다음 호출의 입력으로", accent=True)
    d.label(788, 256, 120, "평가 루프(궤적 기록)", accent=True)
    # nodes
    d.oval(16, 76, 96, 48, "요청")
    d.rect(144, 72, 150, 56, "상태", sub="대화 · 기록 · 스킬", sub_mono=False)
    d.rect(326, 72, 150, 56, "모델", sub="다음 행동 고르기", sub_mono=False)
    d.rect(508, 72, 150, 56, "하네스 검사", sub="형식 · 경로 · 승인", sub_mono=False, focal=True)
    d.rect(690, 72, 150, 56, "도구 실행", sub="작업 폴더 안에서", sub_mono=False)
    d.oval(326, 190, 150, 56, "끝내기", sub="완료 · 실패 · 한도 중단")
    d.rect(690, 190, 150, 56, "관측", sub="결과 · 오류 · 축약", sub_mono=False)
    return d, 920, 316, "하네스 한 바퀴와 일곱 기능", "요청이 상태, 모델, 하네스 검사, 도구 실행, 관측을 거쳐 다시 상태로 돌아오는 루프와, 각 기능이 작동하는 자리"


def harness_experiment(t):
    d = D(t)
    # row (cy=120): 불편 -> 병목 -> 가설 -> 실행 -> 판정
    d.line("M166,120 H190")
    d.line("M340,120 H364")
    d.line("M514,120 H538")
    d.line("M688,120 H712")
    # 판정 -> 병목 (기각되면 다음 가설)
    d.line("M787,92 V56 Q787,48 779,48 H273 Q265,48 265,56 V90", dashed=True)
    d.label(436, 38, 170, "기각도 다음 실험의 재료")
    # nodes
    d.oval(16, 92, 150, 56, "불편 하나", sub="장면으로 적기")
    d.rect(192, 92, 148, 56, "병목 기능 고르기", sub="세 질문 · 일곱 기능", sub_mono=False)
    d.rect(366, 92, 148, 56, "가설과 판정식", sub="결과를 보기 전에", sub_mono=False)
    d.rect(540, 92, 148, 56, "하나만 바꿔 실행", sub="고정 · 조작 · 측정", sub_mono=False)
    d.rect(714, 92, 148, 56, "판정", sub="결과 + 궤적", sub_mono=False, focal=True)
    return d, 880, 172, "하네스 개선 실험 순서", "불편 하나를 병목 기능으로 좁히고, 결과를 보기 전에 판정식을 쓴 뒤, 한 항목만 바꿔 실행하고 결과와 궤적으로 판정하는 순서"


if __name__ == "__main__":
    build([("harness-loop", harness_loop), ("harness-experiment", harness_experiment)])
