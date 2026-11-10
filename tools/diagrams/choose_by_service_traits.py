"""Diagrams for 2026-11-10-choose-by-service-traits. Run: py choose_by_service_traits.py && py shot.py choose-by-service-traits trait-map example-matrix"""
from gen import D, build


def trait_map(t):
    d = D(t)
    cols = [
        (16, "누가, 어디서 쓰나?", "나 혼자 · 소수 · 공개 / 웹 · 폰", [
            ("서버를 만들어 올리기", "모르는 사람도 써야 할 때", True),
            ("비용 계산과 사용 한도, 결제", "공개하거나 유료로 운영할 때", False),
            ("폰 앱 만들기", "폰 기능이 서비스의 핵심일 때", False),
        ]),
        (308, "틀리거나 멈추면?", "피해가 얼마나 큰가", [
            ("서버 두 대로 나눠 운영하기", "끊기면 바로 불편하거나 손해일 때", False),
            ("자동 테스트와 검토 후 올리기", "잘못 올라가면 피해가 클 때", False),
            ("기록을 남겨 두고 보기", "남이 쓰고, 이상한 답이 피해일 때", False),
            ("합격 기준을 정해 비교하기", "틀린 답의 피해가 클 때", False),
        ]),
        (600, "데이터는?", "남기나 · 민감한가", [
            ("데이터를 서버 밖 DB에 저장하기", "이어서 써야 할 때", False),
            ("개인정보를 기록에 남기지 않기", "개인정보나 사업 정보가 오갈 때", False),
        ]),
    ]
    for x, q, qsub, steps in cols:
        d.oval(x, 24, 276, 56, q, sub=qsub)
        for i, (name, sub, focal) in enumerate(steps):
            d.rect(x, 108 + 68 * i, 276, 56, name, sub=sub, sub_mono=False, focal=focal)
    d.label(196, 396, 500, "각 칸의 조건에 해당하지 않으면, 그 단계는 생략한다", accent=True)
    return d, 892, 424, "질문 세 가지로 나눈 운영 단계", "누가 어디서 쓰나, 틀리거나 멈추면 피해가 얼마나 큰가, 데이터를 남기나 세 질문 아래에 단계 아홉 개를 두고, 각 단계가 필요한 조건을 적은 지도"


ROWS = [
    ("서버를 만들어 올리기", "누가, 어디서 쓰나?", True, True),
    ("비용 계산과 사용 한도", "누가, 어디서 쓰나?", True, True),
    ("결제", "누가, 어디서 쓰나?", False, False),
    ("폰 앱 만들기", "누가, 어디서 쓰나?", False, True),
    ("서버 두 대로 나눠 운영하기", "틀리거나 멈추면?", True, False),
    ("자동 테스트와 검토 후 올리기", "틀리거나 멈추면?", True, False),
    ("기록을 남겨 두고 보기", "틀리거나 멈추면?", True, False),
    ("합격 기준을 정해 비교하기", "틀리거나 멈추면?", True, False),
    ("데이터를 서버 밖 DB에 저장하기", "데이터는?", False, True),
    ("개인정보를 기록에 남기지 않기", "데이터는?", True, True),
]


def example_matrix(t):
    d = D(t)
    d.oval(312, 24, 160, 48, "동네 가게 챗봇", sub="공개 · 웹")
    d.oval(488, 24, 160, 48, "영수증 폰 앱", sub="가족·친구 · 폰")
    for i, (name, grp, a, b) in enumerate(ROWS):
        y = 88 + 52 * i
        d.rect(16, y, 280, 44, name, sub=grp, sub_mono=False)
        for x, on in ((312, a), (488, b)):
            if on:
                d.rect(x, y, 160, 44, "붙임", focal=True)
            else:
                d.oval(x, y, 160, 44, "생략")
    return d, 664, 624, "예시 두 서비스의 붙일 것과 생략할 것", "동네 가게 문의 챗봇과 영수증 폰 앱에 같은 단계 열 개를 적용해 붙일 것과 생략할 것을 비교한 표"


if __name__ == "__main__":
    build([("trait-map", trait_map), ("example-matrix", example_matrix)])
