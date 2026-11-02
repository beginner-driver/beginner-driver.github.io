"""Diagrams for 2026-10-27-zero-downtime-deploy. Run: py zero_downtime_deploy.py && py shot.py zero-downtime-deploy deploy-strategies auto-deploy-flow"""
from gen import D, build

XS = (150, 338, 526, 714)  # stage columns, w=166


def deploy_strategies(t):
    d = D(t)
    rows = [
        ("롤링", [("v1 · v1 · v1", "구 버전 3대", False), ("v2 · v1 · v1", "한 대씩 교체", False),
                 ("v2 · v2 · v1", "두 버전이 함께 받음", False), ("v2 · v2 · v2", "교체 끝", True)]),
        ("블루그린", [("블루 100%", "그린은 0%로 띄워 확인", False), ("그린 100%", "한 번에 전환", True),
                   ("블루 켜 둠", "롤백할 자리", False), ("블루 정리", "확인 뒤 종료", False)]),
        ("카나리", [("새 버전 0%", "올려 두고 확인", False), ("10%", "오류율 · p95 확인", False),
                  ("50%", "다시 확인", False), ("100%", "전환 끝", True)]),
    ]
    for i, (name, stages) in enumerate(rows):
        y = 24 + i * 100
        cy = y + 28
        d.line(f"M128,{cy} H148")
        for j in range(3):
            d.line(f"M{XS[j] + 166},{cy} H{XS[j + 1] - 2}")
        d.oval(16, y, 112, 56, name)
        for x, (n, sub, focal) in zip(XS, stages):
            d.rect(x, y, 166, 56, n, sub=sub, focal=focal, sub_mono=False)
    return d, 900, 304, "무중단 배포 세 방식", "롤링은 서버를 한 대씩 바꾸고, 블루그린은 새 묶음을 0%로 띄워 확인한 뒤 한 번에 넘기며, 카나리는 새 버전으로 가는 비율을 조금씩 올린다"


def auto_deploy_flow(t):
    d = D(t)
    d.line("M116,88 H138")
    d.line("M316,88 H338")
    d.line("M520,88 H542")
    d.line("M656,88 H682", accent=True)
    d.line("M600,128 V198")
    d.line("M784,116 V198", dashed=True)
    d.label(656, 64, 28, "예", accent=True)
    d.label(610, 150, 44, "아니오")
    d.label(794, 146, 88, "문제가 보이면")
    d.oval(16, 64, 100, 48, "PR 머지")
    d.rect(140, 60, 176, 56, "새 리비전 0%", sub="--no-traffic --tag green")
    d.rect(340, 60, 180, 56, "스모크 테스트", sub="태그 URL /health · 커밋", sub_mono=False)
    d.diamond(600, 88, 56, 40, ["통과?"])
    d.rect(684, 60, 200, 56, "전환 100%", sub="이전 리비전 이름 기록", focal=True, sub_mono=False)
    d.rect(440, 200, 220, 56, "워크플로 실패", sub="트래픽은 이전 리비전 그대로", sub_mono=False)
    d.rect(684, 200, 200, 56, "원클릭 롤백", sub="버튼 한 번 → 이전 리비전 100%", sub_mono=False)
    return d, 900, 280, "머지 한 번으로 도는 무중단 배포", "머지하면 새 리비전을 트래픽 0%로 올리고, 태그 URL로 스모크 테스트를 통과했을 때만 100%로 전환하며, 실패하면 이전 리비전이 계속 요청을 받고 문제가 보이면 버튼 한 번으로 되돌린다"


if __name__ == "__main__":
    build([("deploy-strategies", deploy_strategies), ("auto-deploy-flow", auto_deploy_flow)])
