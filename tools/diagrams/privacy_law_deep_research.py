"""Diagrams for _posts/2026-09-23-privacy-law-deep-research.md"""
from gen import D, build


def research_flow(t):
    d = D(t)
    # main row
    d.line("M108,120 H138")
    d.line("M290,120 H320")
    # fan-out to three researchers
    d.line("M442,120 L486,52")
    d.line("M442,120 H486")
    d.line("M442,120 L486,188")
    # back to review
    d.line("M658,50 L700,112")
    d.line("M658,120 H694")
    d.line("M658,190 L700,128")
    # loop: only short sections go back
    d.line("M760,80 V20 Q760,12 752,12 H390 Q382,12 382,20 V90", accent=True, dashed=True)
    d.label(500, 4, 160, "부족한 절만 · 최대 2바퀴", accent=True)
    # done -> synthesize -> report
    d.line("M760,160 V234")
    d.label(770, 186, 36, "충분")
    d.line("M680,264 H602")
    # nodes
    d.oval(16, 96, 92, 48, "질문")
    d.rect(140, 92, 150, 56, "① 기획 · 코디네이터", sub="목차 · 역할 · 시작 문서", sub_mono=False)
    d.rect(322, 92, 120, 56, "② 배치", sub="남의 구역 전달", sub_mono=False)
    d.rect(488, 28, 170, 44, "③ 조사관 1", sub="자기 구역만 읽고 집필", sub_mono=False)
    d.rect(488, 98, 170, 44, "③ 조사관 2", sub="동시 실행 · 결과 공유 없음", focal=True, sub_mono=False)
    d.rect(488, 168, 170, 44, "③ 조사관 N", sub="충분 / 부족 자기신고", sub_mono=False)
    d.diamond(760, 120, 64, 40, ["④ 점검", "빈 칸이 있나?"])
    d.rect(680, 236, 160, 56, "⑤ 종합 · 편집자", sub="머리말 · 맺음말만 새로", sub_mono=False)
    d.oval(458, 240, 144, 48, "보고서")
    return d, 856, 312, "딥리서치 파이프라인", "코디네이터가 질문을 내용 단위 절로 나눠 역할과 시작 문서를 배정하고, 배치 단계가 절마다 남의 구역을 알려 주며 조사관을 동시에 보낸다. 점검 단계는 부족하다고 신고한 절만 최대 두 바퀴까지 다시 보내고, 편집자는 절 원고를 그대로 두고 머리말과 맺음말만 써서 보고서로 잇는다"


def code_vs_prompt(t):
    d = D(t)
    # left column: code-enforced checks
    d.line("M200,68 V94")
    d.line("M200,140 V162")
    d.line("M200,208 V230")
    d.line("M200,276 V298", accent=True)
    # right column: prompt-only instruction
    d.line("M580,68 V94")
    d.line("M580,140 V298")
    d.label(590, 212, 84, "Q4 다시 실행")
    # nodes
    d.rect(40, 20, 320, 48, "코드로 강제한 장치", focal=True)
    d.rect(40, 96, 320, 44, "배정 검증", sub="없는 제목 · 겹치는 시작 문서는 코드가 교체", sub_mono=False)
    d.rect(40, 164, 320, 44, "JSON 파싱 여부", sub="파싱이 실패했을 때만 원문에서 다시 추출", sub_mono=False)
    d.rect(40, 232, 320, 44, "연도 대조", sub="절 제목 연도 밖 문서를 인용하면 재위임", sub_mono=False)
    d.oval(40, 300, 320, 44, "세 장치 모두 막혔다")
    d.rect(420, 20, 320, 48, "프롬프트로만 부탁한 지시")
    d.rect(420, 96, 320, 44, "범위 밖 문서 인용 금지", sub="절 지시에 연도 범위를 적어 둠", sub_mono=False)
    d.oval(420, 300, 320, 44, "같은 자리에서 다시 샜다")
    return d, 780, 360, "코드 강제와 프롬프트 지시", "배정 검증, JSON 파싱 여부, 연도 대조처럼 코드가 검사한 장치는 실패를 막았고, 절 지시에 연도 범위를 적어 둔 프롬프트 지시만으로는 Q4를 다시 돌렸을 때 같은 자리에서 범위 밖 내용이 다시 섞였다"


if __name__ == "__main__":
    build([("research-flow", research_flow), ("code-vs-prompt", code_vs_prompt)])
