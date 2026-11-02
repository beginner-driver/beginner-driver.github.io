"""Diagrams for _posts/2026-08-27-rfp-document-checker.md"""
from gen import D, build


def rfp_tool_flow(t):
    d = D(t)
    d.line("M136,96 H168")
    d.line("M370,96 H408")
    d.line("M610,96 H648")
    d.line("M750,124 V214", accent=True)
    d.label(170, 22, 200, "", lines=["“제출서류 뭐야?”", "→ ①까지"])
    d.label(410, 22, 200, "", lines=["“이거면 충분해?”", "→ ①②까지"])
    d.label(650, 22, 200, "", lines=["“유효기간 괜찮아?”", "→ ②③까지"])
    d.label(170, 140, 440, "①~③ 읽기 전용 — 승인 없이 호출")
    d.label(760, 152, 112, "", accent=True, lines=["확인필요 반복 시", "사용자 확인 후"])
    d.oval(16, 72, 120, 48, "사용자 질문")
    d.rect(170, 68, 200, 56, "① 요건 조회", sub="get_rfp_requirements")
    d.rect(410, 68, 200, 56, "② 보유 서류 대조", sub="check_document_checklist")
    d.rect(650, 68, 200, 56, "③ 세부조건 확인", sub="validate_document_detail")
    d.rect(650, 216, 200, 56, "④ 담당자 이관", sub="escalate_to_reviewer", focal=True)
    return d, 880, 292, "제출서류 검증 챗봇의 도구 흐름", "질문의 깊이에 따라 요건 조회, 보유 서류 대조, 세부조건 확인 도구를 필요한 만큼만 부르고, 확인필요가 반복되면 사용자 확인을 받아 담당자에게 넘기는 흐름"


def approval_gate(t):
    d = D(t)
    # 설계안
    d.line("M126,68 H158")
    d.line("M380,68 H678")
    d.label(16, 12, 260, "설계: 승인 여부를 인자로 받는다")
    d.label(440, 44, 180, "인자 값만 보고 실행")
    # 이론의 권장
    d.line("M126,188 H158")
    d.line("M380,188 H418")
    d.line("M620,188 H678", accent=True)
    d.label(16, 132, 330, "이론의 권장: 실행 직전에 하네스가 사람에게 묻는다", accent=True)
    d.oval(16, 40, 110, 56, "모델")
    d.rect(160, 40, 220, 56, "이관 호출", sub="user_confirmed=true")
    d.oval(680, 40, 160, 56, "티켓 생성")
    d.oval(16, 160, 110, 56, "모델")
    d.rect(160, 160, 220, 56, "이관 호출", sub="escalate_to_reviewer")
    d.rect(420, 160, 200, 56, "사람 승인", sub="클라이언트 승인 창", focal=True, sub_mono=False)
    d.oval(680, 160, 160, 56, "티켓 생성")
    return d, 860, 236, "승인을 어디서 거는가", "설계안은 모델이 채우는 user_confirmed 인자로 승인 여부를 받고, 이론은 실행 직전에 하네스가 사람에게 직접 확인하도록 권한다"


if __name__ == "__main__":
    build([("rfp-tool-flow", rfp_tool_flow), ("approval-gate", approval_gate)])
