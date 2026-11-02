"""Diagrams for 2026-10-23-cicd-docker (light + dark)."""
from gen import D, build


def gate_pipeline(t):
    d = D(t)
    # arrows
    d.line("M144,80 H174")
    d.line("M336,80 H366")
    d.line("M528,80 H558")
    d.line("M704,80 H734", accent=True)
    d.line("M448,104 V168 H800 V106", accent=True, dashed=True)
    # labels
    d.label(176, 120, 160, "실패하면 머지가 막힌다")
    d.label(560, 120, 144, "써 봐야 보이는 문제")
    d.label(520, 160, 220, "main에서 다시 빌드하지 않는다", accent=True)
    # nodes
    d.oval(16, 56, 128, 48, "작업 브랜치", sub="PR")
    d.rect(176, 56, 160, 48, "CI 테스트", sub="PR마다 · 서버와 같은 환경", sub_mono=False)
    d.rect(368, 56, 160, 48, "이미지 한 번 빌드", sub="태그 = 커밋 SHA", focal=True, sub_mono=False)
    d.rect(560, 56, 144, 48, "staging", sub="직접 써 보기", sub_mono=False)
    d.oval(736, 56, 128, 48, "production", sub="승인 후 승격")
    return d, 880, 200, "작업 브랜치에서 production까지의 품질 게이트", "PR마다 CI 테스트를 통과하고, 한 번 만든 이미지를 staging에서 써 본 뒤 승인을 거쳐 같은 이미지를 production으로 승격하는 흐름"


def image_trace(t):
    d = D(t)
    # arrows
    d.line("M166,80 H194")
    d.line("M346,80 H374")
    d.line("M526,80 H554")
    d.line("M706,80 H734")
    d.line("M811,104 V148 H91 V106", dashed=True)
    # labels
    d.label(326, 140, 260, "거꾸로 따라가면 되돌릴 커밋이 나온다")
    # nodes
    d.rect(16, 56, 150, 48, "커밋", sub="a1b2c3d")
    d.rect(196, 56, 150, 48, "이미지 태그", sub=":a1b2c3d")
    d.rect(376, 56, 150, 48, "다이제스트", sub="sha256:…", focal=True)
    d.rect(556, 56, 150, 48, "리비전", sub="다이제스트로 고정", sub_mono=False)
    d.rect(736, 56, 150, 48, "/version", sub="commit: a1b2c3d")
    return d, 902, 176, "커밋에서 실행 중인 버전까지 잇는 연결", "커밋 SHA를 이미지 태그로 붙이고, 리비전은 다이제스트로 고정되며, 앱의 /version이 같은 커밋을 돌려주는 연결"


if __name__ == "__main__":
    build([("gate-pipeline", gate_pipeline), ("image-trace", image_trace)])
