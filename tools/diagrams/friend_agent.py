"""Diagrams for _posts/2026-10-29-friend-agent.md"""
from gen import D, build


def deploy_gates(t):
    d = D(t)
    # row 1: PR → CI → staging → check → approval → promote
    d.line("M100,68 H122")
    d.line("M256,68 H278")
    d.line("M440,68 H462")
    d.line("M616,68 H638")
    d.line("M768,68 H790")
    d.line("M851,96 V150", accent=True)
    # row 2 (right to left): 0% deploy → probe → smoke → switch → serving
    d.line("M776,180 H706")
    d.line("M576,180 H534", accent=True)
    d.line("M376,180 H344", accent=True)
    d.line("M200,180 H164", accent=True)
    # failures keep the previous revision
    d.line("M640,218 V258")
    d.line("M454,208 V284 H578")
    # rollback after switch
    d.line("M270,208 V258", dashed=True)
    d.label(540, 156, 24, "예", accent=True)
    d.label(650, 228, 44, "아니오")
    d.label(462, 236, 32, "실패")
    d.label(280, 224, 72, "문제 생기면")
    # nodes
    d.oval(16, 44, 84, 48, "PR")
    d.rect(124, 40, 132, 56, "CI 테스트", sub="PR마다 pytest", sub_mono=False)
    d.rect(280, 40, 160, 56, "staging 배포", sub="이미지 빌드 · 커밋 태그", sub_mono=False)
    d.rect(464, 40, 152, 56, "staging 확인", sub="/version · OCR · QR", sub_mono=False)
    d.rect(640, 40, 128, 56, "production 승인", sub="사람이 누른다", sub_mono=False)
    d.rect(792, 40, 118, 56, "이미지 승격", sub="같은 다이제스트", sub_mono=False)
    d.rect(778, 152, 132, 56, "0% 배포", sub="green 태그", sub_mono=False)
    d.diamond(640, 180, 64, 38, ["/health", "프로브 통과?"])
    d.rect(378, 152, 156, 56, "스모크 테스트", sub="태그 URL 커밋 일치", sub_mono=False)
    d.rect(202, 152, 142, 56, "전환", sub="green 100%", focal=True, sub_mono=False)
    d.oval(40, 156, 124, 48, "새 버전 서비스")
    d.rect(580, 260, 156, 48, "이전 리비전 유지", sub="트래픽 그대로", sub_mono=False)
    d.rect(190, 260, 160, 48, "rollback 버튼", sub="직전 정상 리비전 100%", sub_mono=False)
    return d, 920, 324, "AI 친구 에이전트 배포 경로", "PR은 CI 테스트를 거쳐 staging에 이미지로 배포되고, 사람이 staging을 확인하고 production 배포를 승인하면 같은 다이제스트의 이미지가 승격된다. production에는 트래픽 0%로 먼저 올리고, /health 스타트업 프로브와 태그 URL 스모크 테스트를 통과해야 100%로 전환한다. 어느 단계든 실패하면 이전 리비전이 계속 응답하고, 전환 뒤 문제가 생기면 rollback 버튼으로 직전 정상 리비전에 트래픽을 돌린다"


if __name__ == "__main__":
    build([("deploy-gates", deploy_gates)])
