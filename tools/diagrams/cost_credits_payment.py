"""Diagrams for 2026-11-04-cost-credits-payment and 2026-11-04-friend-agent-credits.
Run: py cost_credits_payment.py && py shot.py cost-credits-payment ledger-vs-balance payment-confirm && py shot.py friend-agent-credits credit-guards"""
from gen import D, build


def ledger_vs_balance(t):
    d = D(t)
    d.label(16, 12, 300, "잔액 칸 하나: 덮어쓴다")
    d.label(376, 12, 300, "원장: 쌓기만 한다", accent=True)
    d.rect(16, 40, 300, 56, "남은 크레딧: 19", sub="이전 값은 사라진다", sub_mono=False)
    d.oval(16, 116, 300, 52, "두 요청이 동시에 1을 읽으면", sub="둘 다 통과할 수 있다")
    d.oval(16, 188, 300, 52, "잔액이 틀어지면", sub="왜 그런지 알 수 없다")
    rows = [("+20 · 가입", "signup:사용자"), ("−1 · 메시지", "chat:무작위"), ("+100 · 결제", "order:주문번호")]
    for i, (name, sub) in enumerate(rows):
        d.rect(376, 40 + 64 * i, 300, 52, name, sub=sub, sub_mono=False)
    d.line("M526,228 V244", accent=True)
    d.rect(376, 246, 300, 52, "잔액 = 줄의 합계 119", sub="참조가 겹치면 DB가 거절", sub_mono=False, focal=True)
    return d, 692, 314, "잔액 칸과 원장", "잔액 칸 하나는 값을 덮어써서 이력이 없고 동시 요청에 약하다. 원장은 늘고 준 기록을 참조와 함께 한 줄씩 쌓고, 잔액은 줄의 합계이며 같은 참조는 DB가 두 번 받지 않는다"


def payment_confirm(t):
    d = D(t)
    xs = [16, 196, 376, 556, 736]
    for x in xs[:-1]:
        d.line(f"M{x + 160},64 H{x + 178}")
    steps = [("① 주문 저장", "서버 · 대기 상태"), ("② 결제 인증", "PG 결제창 · 카드사"),
             ("③ successUrl", "주문번호 · 금액 · 키"), ("④ 확인 후 승인", "금액·상태 비교 → 승인 API"),
             ("⑤ 크레딧 지급", "원장 order:주문번호")]
    for x, (name, sub) in zip(xs, steps):
        d.rect(x, 34, 160, 60, name, sub=sub, sub_mono=False, focal=(x == 556))
    d.label(196, 104, 340, "①~③만으로는 돈이 들어오지 않는다")
    d.line("M636,94 V138", accent=True)
    d.oval(536, 140, 200, 52, "시크릿 키는 서버에만", sub="같은 주문은 같은 멱등키")
    return d, 912, 208, "결제 인증과 승인", "서버가 주문을 대기로 저장한 뒤 사용자가 PG 결제창에서 인증하고, successUrl로 돌아온 값을 서버가 저장한 금액·상태와 비교한 뒤 시크릿 키로 승인 API를 불러 성공했을 때만 원장에 크레딧을 쌓는다"


def credit_guards(t):
    d = D(t)
    d.line("M136,64 H166")
    d.line("M346,64 H376")
    d.line("M526,64 H556", accent=True)
    d.line("M76,88 V138")
    d.line("M257,92 V138")
    d.line("M636,92 V138")
    d.label(86, 106, 64, "위기 표현")
    d.label(267, 106, 50, "잔액 0")
    d.label(646, 106, 56, "답 실패")
    d.oval(16, 40, 120, 48, "메시지")
    d.rect(168, 36, 178, 56, "spend_credit()", sub="잠금 안에서 확인+차감", sub_mono=False)
    d.rect(378, 36, 148, 56, "−1 줄", sub="chat:무작위", sub_mono=False)
    d.rect(558, 36, 156, 56, "답 생성", sub="스트리밍", sub_mono=False, focal=True)
    d.oval(6, 140, 140, 52, "안전 응답", sub="차감하지 않음")
    d.oval(177, 140, 160, 52, "402 거절", sub="메시지는 입력창에")
    d.oval(556, 140, 160, 52, "+1 되돌림", sub="refund:참조")
    return d, 732, 208, "메시지 한 건의 크레딧 흐름", "메시지가 오면 DB 함수가 잠금 안에서 잔액 확인과 차감을 한 번에 하고, 잔액이 0이면 402로 거절하며 메시지를 입력창에 남기고, 답을 못 만들면 되돌리는 +1 줄을 쌓는다. 위기 표현은 차감 없이 안전 응답을 받는다"


if __name__ == "__main__":
    build([("ledger-vs-balance", ledger_vs_balance), ("payment-confirm", payment_confirm), ("credit-guards", credit_guards)])
