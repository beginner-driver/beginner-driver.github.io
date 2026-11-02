"""Diagrams for 2026-10-16-ai-feature-to-service. Run: py ai_feature_to_service.py && py shot.py ai-feature-to-service design-sequence channel-ladder"""
from gen import D, build


def design_sequence(t):
    d = D(t)
    # top row
    for x in (156, 328, 500, 672):
        d.line(f"M{x},68 H{x + 30}")
    d.line("M774,96 V142")
    # branch
    d.line("M710,180 H642", accent=True)
    d.line("M460,180 H410")
    d.line("M774,216 V244 Q774,252 766,252 H306 Q298,252 298,244 V210")
    d.label(664, 156, 24, "예", accent=True)
    d.label(784, 222, 44, "아니오")
    # nodes
    d.rect(16, 40, 140, 56, "사용 맥락", sub="언제 · 무엇을 쓰나", sub_mono=False)
    d.rect(188, 40, 140, 56, "제공 채널", sub="어디에 내놓나", sub_mono=False)
    d.rect(360, 40, 140, 56, "처리 방식", sub="동기 · 비동기 · 스케줄", sub_mono=False)
    d.rect(532, 40, 140, 56, "오류 대응", sub="영향도별 장치", sub_mono=False)
    d.rect(704, 40, 140, 56, "코드 없는 테스트", sub="행동을 관찰", sub_mono=False)
    d.diamond(774, 180, 64, 36, ["웹앱인가?"])
    d.rect(460, 152, 180, 56, "문서 세 장", sub="시퀀스 · 아키텍처 · 데이터", sub_mono=False)
    d.rect(188, 152, 220, 56, "PRD 한 장", sub="접근 · 데이터 · 비용 · 파일럿", sub_mono=False, focal=True)
    return d, 860, 276, "AI 기능을 서비스로 설계하는 순서", "사용 맥락에서 출발해 채널, 처리 방식, 오류 대응을 정하고 코드 없이 확인한 뒤, 웹앱이면 문서 세 장을 더해 PRD 한 장으로 모은다"


def channel_ladder(t):
    d = D(t)
    for x in (176, 354, 532, 710):
        d.line(f"M{x},72 H{x + 16}")
    d.line("M16,132 H884")
    d.label(16, 142, 200, "빨리 만든다 · 제어 범위가 작다")
    d.label(688, 142, 200, "오래 걸린다 · 직접 제어한다")
    d.label(260, 178, 380, "이 중 하나가 생기면 오른쪽 채널로 옮긴다", accent=True)
    d.rect(16, 40, 160, 64, "기성 AI 도구", sub="몇 시간", sub_mono=False)
    d.rect(194, 40, 160, 64, "워크플로 자동화", sub="하루 안팎", sub_mono=False)
    d.rect(372, 40, 160, 64, "메신저 봇", sub="며칠", sub_mono=False)
    d.rect(550, 40, 160, 64, "확장 프로그램", sub="며칠", sub_mono=False)
    d.rect(728, 40, 160, 64, "웹앱", sub="몇 주 이상", sub_mono=False, focal=True)
    d.oval(16, 206, 280, 48, "계정 없는 사용자도 써야 할 때")
    d.oval(312, 206, 280, 48, "비용을 직접 관리해야 할 때")
    d.oval(608, 206, 280, 48, "결과를 자동으로 이어야 할 때")
    return d, 904, 272, "다섯 가지 제공 채널", "기성 AI 도구부터 웹앱까지 오른쪽으로 갈수록 개발 기간과 직접 제어 범위가 커지고, 세 가지 전환 조건 중 하나가 생기면 오른쪽 채널로 옮긴다"


if __name__ == "__main__":
    build([("design-sequence", design_sequence), ("channel-ladder", channel_ladder)])
