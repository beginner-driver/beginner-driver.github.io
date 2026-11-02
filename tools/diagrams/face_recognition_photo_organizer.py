"""Diagrams for _posts/2026-08-12-face-recognition-photo-organizer.md"""
from gen import D, build


def face_pipeline(t):
    d = D(t)
    # row 1: 등록
    d.line("M156,64 H198")
    d.line("M380,64 H422")
    d.line("M584,64 H604 Q612,64 612,72 V111 Q612,119 620,119 H638")
    # row 2: 인덱싱
    d.line("M156,174 H198")
    d.line("M380,174 H422")
    d.line("M584,174 H604 Q612,174 612,166 V127 Q612,119 620,119 H638")
    # 결과
    d.line("M740,147 V200", accent=True)
    d.label(16, 12, 120, "① 인물 등록")
    d.label(16, 124, 120, "② 사진 인덱싱")
    d.label(560, 12, 280, "전부 내 컴퓨터 안에서 처리 (외부 전송 없음)", accent=True)
    d.label(748, 166, 108, "슬라이더로 조정")
    d.oval(16, 40, 140, 48, "기준 사진 3~5장")
    d.rect(200, 36, 180, 56, "얼굴 검출 + 임베딩", sub="buffalo_s · CPU")
    d.rect(424, 36, 160, 56, "기준 벡터", sub="SQLite")
    d.oval(16, 150, 140, 48, "정리된 사진 전체")
    d.rect(200, 146, 180, 56, "얼굴 검출 + 임베딩", sub="buffalo_s · CPU")
    d.rect(424, 146, 160, 56, "얼굴 벡터", sub="SQLite")
    d.rect(640, 91, 200, 56, "코사인 유사도 비교", sub="임계값 0.4 이상", focal=True, sub_mono=False)
    d.oval(660, 202, 160, 48, "그 사람이 나온 사진")
    return d, 860, 268, "얼굴 인식 사진 찾기 흐름", "기준 사진과 라이브러리 사진을 같은 모델로 얼굴 벡터로 바꿔 저장하고, 코사인 유사도가 임계값 이상인 사진을 보여주는 흐름. 모든 처리는 로컬에서 한다"


def poc_setup(t):
    d = D(t)
    d.line("M166,96 H186 Q194,96 194,88 V56 Q194,48 202,48 H218")
    d.line("M166,112 H186 Q194,112 194,120 V152 Q194,160 202,160 H218")
    d.line("M410,48 H537 Q545,48 545,56 V130")
    d.line("M410,160 H458")
    d.line("M630,160 H678", accent=True)
    d.label(432, 24, 90, "기준으로 등록")
    d.oval(16, 76, 150, 56, "LFW 공개 사진", sub="62명 · 3,023장")
    d.rect(220, 20, 190, 56, "기준 사진 4장", sub="사진이 가장 많은 1명", sub_mono=False)
    d.rect(220, 132, 190, 56, "검색 풀 400장", sub="그 사람 100 · 다른 사람 300", sub_mono=False)
    d.rect(460, 132, 170, 56, "검출 · 유사도 계산", sub="임계값 0.4", sub_mono=False)
    d.rect(680, 132, 170, 56, "결과", sub="맞힘 100 · 오탐 2 · 놓침 0", focal=True, sub_mono=False)
    return d, 866, 208, "PoC 실험 구성", "공개 얼굴 데이터에서 한 사람의 사진 4장을 기준으로 등록하고, 그 사람 100장과 다른 사람 300장을 섞은 400장에서 임계값 0.4로 찾은 결과"


if __name__ == "__main__":
    build([("face-pipeline", face_pipeline), ("poc-setup", poc_setup)])
