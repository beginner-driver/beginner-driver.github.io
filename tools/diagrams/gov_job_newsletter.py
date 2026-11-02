"""Diagrams for _posts/2026-09-15-gov-job-newsletter.md"""
from gen import D, build


def newsletter_flow(t):
    d = D(t)
    # sources -> collect
    d.line("M136,54 L178,92")
    d.line("M136,100 H178")
    d.line("M136,146 L178,108")
    # row 1
    d.line("M310,100 H348")
    d.line("M500,100 H538")
    d.line("M625,128 V218")
    # row 2 (right to left)
    d.line("M540,248 H502", accent=True)
    d.line("M350,248 H312")
    d.line("M425,276 V318")
    d.label(312, 224, 36, "통과")
    d.label(435, 288, 36, "탈락")
    # nodes
    d.oval(16, 36, 120, 36, "ALIO")
    d.oval(16, 82, 120, 36, "나라일터")
    d.oval(16, 128, 120, 36, "클린아이")
    d.rect(180, 72, 130, 56, "수집", sub="collect · 공통 형식", sub_mono=False)
    d.rect(350, 72, 150, 56, "중복 제거", sub="dedupe · 지문 비교", sub_mono=False)
    d.rect(540, 72, 170, 56, "선별", sub="select · 마감 임박순 5건", sub_mono=False)
    d.rect(540, 220, 170, 56, "요약", sub="AI · 요약 + 인사이트", focal=True, sub_mono=False)
    d.rect(350, 220, 150, 56, "검수", sub="AI · passed / reason", focal=True, sub_mono=False)
    d.oval(160, 224, 150, 48, "텔레그램 발행")
    d.oval(350, 320, 150, 44, "건너뜀", sub="다시 요약하지 않음")
    return d, 730, 380, "채용정보 뉴스레터 흐름", "ALIO, 나라일터, 클린아이 세 소스를 수집해 공통 형식으로 바꾸고, 중복을 지운 뒤 마감 임박순으로 다섯 건을 고른다. AI는 요약과 검수 두 단계에서만 쓰이고, 검수를 통과한 건만 텔레그램으로 발행되며 탈락한 건은 건너뛴다"


if __name__ == "__main__":
    build([("newsletter-flow", newsletter_flow)])
