"""Diagrams for 2026-09-20-rag-to-graphrag. Run: py rag_to_graphrag.py && py shot.py rag-to-graphrag index-vs-query query-routes"""
from gen import D, build


def raw(d, path, dashed=False):
    """Connector without arrowhead (for merging lines)."""
    dash = ' stroke-dasharray="5,4"' if dashed else ""
    d.arrows.append(f'<path d="{path}" fill="none" stroke="{d.t["muted"]}" stroke-width="1.3"{dash}/>')


def index_vs_query(t):
    d = D(t)
    raw(d, "M510,36 V300", dashed=True)  # 색인 | 질문 divider
    # row A: vector RAG
    d.line("M180,84 H208")
    d.line("M360,84 H382")
    d.line("M596,84 H618")
    d.line("M770,84 H792")
    d.line("M434,108 V128 H695 V110", dashed=True)
    # row B: GraphRAG
    d.line("M180,192 H194")
    d.line("M356,192 H370")
    d.line("M417,220 V248")
    d.line("M604,192 H622")
    d.line("M764,192 H782")
    d.line("M477,272 H694 V222", dashed=True, accent=True)
    # labels
    d.label(150, 10, 220, "색인할 때 (미리 한 번)")
    d.label(610, 10, 200, "질문할 때 (매번)")
    d.label(16, 76, 76, "벡터 RAG")
    d.label(16, 184, 76, "GraphRAG", accent=True)
    d.label(548, 280, 110, "그래프를 따라감", accent=True)
    # nodes
    d.oval(104, 60, 76, 48, "문서")
    d.rect(210, 60, 150, 48, "잘라서 임베딩", sub="LLM 호출 없음", sub_mono=False)
    d.oval(384, 60, 100, 48, "벡터 색인")
    d.oval(520, 60, 76, 48, "질문")
    d.rect(620, 60, 150, 48, "비슷한 문단 찾기")
    d.oval(794, 60, 110, 48, "답")
    d.oval(104, 168, 76, 48, "문서")
    d.rect(196, 164, 160, 56, "LLM으로 사실 추출", sub="청크마다 호출", sub_mono=False, focal=True)
    d.rect(372, 164, 90, 56, "정규화·병합")
    d.oval(357, 250, 120, 44, "지식 그래프")
    d.oval(528, 168, 76, 48, "질문")
    d.rect(624, 164, 140, 56, "선 따라 n홉 걷기", sub="끊기면 한 홉 더", sub_mono=False, focal=True)
    d.oval(784, 168, 120, 48, "답 + 탄 경로")
    return d, 920, 316, "벡터 RAG와 GraphRAG의 비용 위치", "벡터 RAG는 질문할 때 문단을 찾고, GraphRAG는 색인할 때 LLM으로 사실을 뽑아 그래프를 만들어 둔 뒤 질문할 때 선을 따라 걷는다"


def query_routes(t):
    d = D(t)
    d.line("M96,160 H112")
    d.line("M170,116 V88 Q170,80 178,80 H278")
    d.line("M226,160 H278", accent=True)
    d.line("M170,204 V232 Q170,240 178,240 H278")
    raw(d, "M460,80 H480 V160")
    raw(d, "M460,240 H480 V160")
    d.line("M460,160 H498")
    d.line("M620,160 H634")
    d.line("M764,160 H798")
    d.line("M700,204 V254")
    d.label(184, 56, 52, "local")
    d.label(228, 136, 44, "path", accent=True)
    d.label(184, 248, 56, "global")
    d.label(768, 136, 26, "예")
    d.label(708, 222, 44, "아니오")
    d.oval(16, 136, 80, 48, "질문")
    d.diamond(170, 160, 56, 44, ["어느", "길로?"])
    d.rect(280, 56, 180, 48, "직접 이웃만 조회", sub="《기생충》의 감독은?", sub_mono=False)
    d.rect(280, 136, 180, 48, "선 따라 n홉 걷기", sub="비슷한 영화 추천", sub_mono=False, focal=True)
    d.rect(280, 216, 180, 48, "커뮤니티 보고서 고르기", sub="어떤 집단이 있나?", sub_mono=False)
    d.rect(500, 136, 120, 48, "근거 모으기", sub="삼중항 · 보고서", sub_mono=False)
    d.diamond(700, 160, 64, 44, ["요구 관계가", "근거에 있나?"])
    d.oval(800, 136, 110, 48, "답 + 탄 경로")
    d.oval(620, 256, 160, 48, "근거가 부족합니다", sub="LLM을 부르지 않음")
    return d, 920, 324, "GraphRAG의 세 가지 질문 경로", "질문 유형에 따라 직접 조회, 선 따라 걷기, 커뮤니티 보고서 중 하나로 근거를 모으고, 요구한 관계가 근거에 없으면 LLM을 부르지 않는다"


if __name__ == "__main__":
    build([("index-vs-query", index_vs_query), ("query-routes", query_routes)])
