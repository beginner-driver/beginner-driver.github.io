"""Diagrams for _posts/2026-09-22-yellow-envelope-graphrag.md"""
from gen import D, build


def graph_pipeline(t):
    d = D(t)
    # row 1: build the graph
    d.line("M136,100 H152 Q156,100 156,96 V66 Q156,62 160,62 H174")
    d.line("M136,100 H152 Q156,100 156,104 V134 Q156,138 160,138 H174")
    d.line("M356,62 H374 Q378,62 378,66 V96 Q378,100 382,100 H398")
    d.line("M356,138 H374 Q378,138 378,134 V104 Q378,100 382,100 H398")
    d.line("M580,100 H622")
    d.line("M714,128 V194")
    # row 2: answer a question (right to left)
    d.line("M624,224 H582")
    d.line("M400,224 H358", accent=True)
    d.line("M176,224 H138")
    d.line("M520,252 V274 Q520,280 514,280 H466 Q460,280 460,274 V254", accent=True)
    d.label(436, 286, 108, "3홉까지 반복", accent=True)
    # nodes
    d.oval(16, 76, 120, 48, "자료 51건", sub="법안 · 회의록 · 인물")
    d.rect(176, 36, 180, 52, "규칙으로 추출", sub="발의 · 심사", sub_mono=False)
    d.rect(176, 112, 180, 52, "LLM으로 추출", sub="입장 표명 · 회의당 1회", sub_mono=False)
    d.rect(400, 72, 180, 56, "정규화", sub="별칭 병합 · 속성 보강", sub_mono=False)
    d.rect(624, 72, 180, 56, "지식그래프", sub="노드 44 · 엣지 66", sub_mono=False)
    d.rect(624, 196, 180, 56, "시작 개체 찾기", sub="이름 매칭 → LLM 폴백", sub_mono=False)
    d.rect(400, 196, 180, 56, "홉 확장", sub="허브는 상위 10개만", focal=True, sub_mono=False)
    d.rect(176, 196, 180, 56, "답변 생성", sub="모은 근거만 사용", sub_mono=False)
    d.oval(16, 200, 120, 48, "답 + 경로")
    return d, 824, 316, "노란봉투법 지식그래프 파이프라인", "법안·회의록·인물 문서 51건에서 발의와 심사 관계는 규칙으로, 입장 표명 관계는 LLM으로 뽑아 정규화한 뒤 노드 44개·엣지 66개의 지식그래프를 만든다. 질문이 오면 시작 개체를 찾고 최대 3홉까지 확장하며, 허브 노드에서는 상위 10개 이웃만 남긴다. 모은 근거만으로 답을 쓰고 경로를 함께 돌려준다"


def failure_layers(t):
    d = D(t)
    # fan out from the first run to four independent fixes, then merge into the rerun
    for y in (46, 110, 174, 238):
        turn = "Q166,142 166,138" if y < 142 else "Q166,142 166,146"
        end = f"V{y + 4} Q166,{y} 170,{y}" if y < 142 else f"V{y - 4} Q166,{y} 170,{y}"
        d.line(f"M136,142 H162 {turn} {end} H194")
        back = f"Q446,{y} 446,{y + 4} V138" if y < 142 else f"Q446,{y} 446,{y - 4} V146"
        d.line(f"M416,{y} H442 {back} Q446,142 450,142 H478")
    d.line("M640,142 H678", accent=True)
    d.oval(16, 118, 120, 48, "1차 평가", sub="6/13")
    d.rect(196, 20, 220, 52, "색인: 이름 없는 질문", sub="LLM 폴백 + 재시도 3회", sub_mono=False)
    d.rect(196, 84, 220, 52, "색인: 스키마 밖 사실", sub="위원회에 위원장 속성", sub_mono=False)
    d.rect(196, 148, 220, 52, "탐색: 방문 = 기록", sub="방문 처리와 엣지 기록 분리", sub_mono=False)
    d.rect(196, 212, 220, 52, "탐색: 허브 양자택일", sub="힌트 우선 + 빈자리 채우기", sub_mono=False)
    d.rect(480, 118, 160, 48, "재평가", sub="9/13 · 수동 10/13", sub_mono=False)
    d.rect(680, 116, 200, 52, "남은 오답 4건", sub="생성 3 · 판정관 오류 1", focal=True, sub_mono=False)
    return d, 896, 284, "실패 층별 수정", "1차 평가 6/13에서 색인 실패 두 가지(이름이 없는 질문, 스키마에 없는 사실)와 탐색 실패 두 가지(방문 처리와 엣지 기록을 한 집합으로 처리한 버그, 허브에서 관계 하나만 남기던 방식)를 각각 고쳐 재평가 9/13, 수동 확인 10/13이 됐다. 남은 오답 4건은 생성 실패 3건과 판정관 오류 1건이다"


if __name__ == "__main__":
    build([("graph-pipeline", graph_pipeline), ("failure-layers", failure_layers)])
