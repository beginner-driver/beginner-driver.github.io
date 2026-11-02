"""Diagrams for 2026-09-21-orchestrator-worker. Run: py orchestrator_worker.py && py shot.py orchestrator-worker orchestration-flow context-isolation"""
from gen import D, build, SANS, esc


def box(d, x, y, w, h, title):
    """Container drawn under nodes, title at top-left."""
    t = d.t
    d.arrows.insert(0, f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{t["oval_fill"]}" stroke="{t["oval_stroke"]}" stroke-width="1" stroke-dasharray="4,3"/>')
    d.arrows.insert(1, f'<text x="{x + 14}" y="{y + 22}" fill="{t["muted"]}" font-size="12" font-weight="600" font-family="{SANS}">{esc(title)}</text>')


def orchestration_flow(t):
    d = D(t)
    box(d, 330, 16, 200, 288, "③ 조사 · 동시에")
    # main row y=160
    d.line("M96,160 H118")
    d.line("M238,160 H262")
    # fan-out from dispatch to three workers
    d.line("M318,160 H334 V82 H352", accent=True)
    d.line("M318,160 H352", accent=True)
    d.line("M318,160 H334 V238 H352", accent=True)
    # fan-in to review
    d.arrows.append(f'<path d="M508,82 H524 V160" fill="none" stroke="{t["muted"]}" stroke-width="1.3"/>')
    d.line("M508,160 H558")
    d.arrows.append(f'<path d="M508,238 H524 V160" fill="none" stroke="{t["muted"]}" stroke-width="1.3"/>')
    # review -> synthesize (done)
    d.line("M708,160 H732")
    d.line("M818,188 V230")
    # re-dispatch loop: review bottom -> dispatch bottom
    d.line("M633,190 V326 Q633,334 625,334 H298 Q290,334 290,326 V190", accent=True, dashed=True)
    # labels
    d.label(380, 318, 168, "부족한 절만 재위임", accent=True)
    d.label(708, 132, 30, "끝")
    # nodes
    d.oval(12, 136, 84, 48, "질문")
    d.rect(120, 132, 118, 56, "① 기획", sub="목차 · 역할 · 예산", sub_mono=False)
    d.rect(264, 132, 54, 56, "②", sub="배치", sub_mono=False)
    d.rect(352, 54, 156, 56, "워커 A", sub="읽고 절 원고 작성", sub_mono=False, focal=True)
    d.rect(352, 132, 156, 56, "워커 B", sub="읽고 절 원고 작성", sub_mono=False, focal=True)
    d.rect(352, 210, 156, 56, "워커 C", sub="읽고 절 원고 작성", sub_mono=False, focal=True)
    d.rect(560, 130, 148, 60, "④ 점검", sub="빈 칸? · 바퀴 상한", sub_mono=False)
    d.rect(734, 132, 168, 56, "⑤ 종합", sub="이어 붙이고 머리말만", sub_mono=False)
    d.rect(734, 232, 168, 56, "⑥ 평가", sub="근거 · 중복 · 편중", sub_mono=False)
    return d, 916, 352, "오케스트레이터-워커 한 바퀴", "질문을 받아 목차와 배정을 정하고, 워커 셋을 동시에 보내 절 원고를 받은 뒤, 점검에서 부족한 절만 다시 보내고 끝나면 이어 붙여 평가한다"


def context_isolation(t):
    d = D(t)
    box(d, 16, 132, 892, 112, "각자의 창")
    # docs -> workers
    for x in (100, 400, 700):
        d.line(f"M{x + 50},300 V246")
    # workers -> coordinator (only drafts go up)
    for x in (100, 400, 700):
        d.line(f"M{x + 50},150 V84", accent=True)
    d.label(160, 262, 180, "원문 수천~수만 자")
    d.label(460, 262, 180, "원문 수천~수만 자")
    d.label(760, 262, 180, "원문 수천~수만 자")
    d.label(158, 98, 180, "원고 + 인용 + 자기신고", accent=True)
    d.label(458, 98, 180, "원고 + 인용 + 자기신고", accent=True)
    d.label(758, 98, 180, "원고 + 인용 + 자기신고", accent=True)
    d.rect(100, 20, 800, 56, "오케스트레이터", sub="원고만 받는다 · 원문은 보지 않는다", sub_mono=False)
    for x, n in ((100, "워커 A"), (400, "워커 B"), (700, "워커 C")):
        d.rect(x, 152, 200, 56, n, sub="읽기 · 요약 · 집필", sub_mono=False, focal=True)
        d.oval(x, 302, 200, 44, "배정·탐색한 자료", sub_mono=False)
    return d, 916, 362, "컨텍스트 격리", "원문은 워커마다 자기 창 안에서만 읽히고, 오케스트레이터에게는 인용과 자기신고가 붙은 절 원고만 올라간다"


if __name__ == "__main__":
    build([("orchestration-flow", orchestration_flow), ("context-isolation", context_isolation)])
