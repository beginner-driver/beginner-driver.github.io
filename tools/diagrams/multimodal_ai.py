"""Diagrams for 2026-08-09-multimodal-ai."""
from gen import D, build

ROWS = [
    ("문서", "스캔 · PDF", "값", "금액 · 날짜 · 항목", "검산", "합계 · 부가세 · 날짜가 실재하나"),
    ("사진", "카메라 · 현장", "위치 · 경계 · 자세", "박스 · 마스크 · 관절점", "정답 영역과 겹침", "IoU · 경계 IoU"),
    ("소리", "녹음", "글자 + 시각", "조각마다 시작 · 끝", "손으로 적은 정답과 대조", "글자 오류율(CER)"),
    ("공간", "걸으며 찍은 영상", "3D 점 · 알갱이", "사진이 버린 거리", "빼 둔 사진과 대조", "PSNR · SSIM · LPIPS"),
    ("생성", "프롬프트 · 참조", "새 이미지", "원본에 없던 픽셀", "정답 없음 → 사람이 고름", "라이선스 · 표시 · 용도"),
]


def output_types(t):
    d = D(t)
    d.label(16, 12, 120, "입력")
    d.label(178, 12, 260, "답의 자료형")
    d.label(480, 12, 300, "맞는지 확인하는 법")
    for i, (inp, inp_sub, out, out_sub, chk, chk_sub) in enumerate(ROWS):
        y = 44 + 68 * i
        cy = y + 26
        last = i == len(ROWS) - 1
        d.line(f"M136,{cy} H176")
        d.line(f"M438,{cy} H478", accent=last)
        d.oval(16, y, 120, 52, inp, sub=inp_sub)
        d.rect(178, y, 260, 52, out, sub=out_sub, sub_mono=False)
        d.rect(480, y, 300, 52, chk, sub=chk_sub, sub_mono=False, focal=last)
    return d, 800, 384, "입력별 답의 자료형과 확인 방법", "문서는 값을 검산하고, 사진은 정답 영역과 겹침을 재고, 소리는 손으로 적은 정답과 대조하고, 공간은 빼 둔 사진과 비교한다. 생성은 정답이 없어 사람이 고른다"


def pipeline_vs_omni(t):
    d = D(t)
    # row 1: pipeline
    d.label(16, 12, 150, "나눠 두기 (파이프라인)")
    d.line("M116,74 H156")
    d.line("M338,74 H378")
    d.line("M550,74 H590")
    d.line("M248,102 V142", accent=True, dashed=True)
    d.label(258, 112, 112, "제안 → 제한 발견", accent=True)
    d.oval(16, 50, 100, 48, "녹음")
    d.rect(158, 46, 180, 56, "받아쓰기", sub="조각별 시각 + 원문", focal=True, sub_mono=False)
    d.rect(380, 46, 170, 56, "회의록 정리", sub="의심 구간은 원문 그대로", sub_mono=False)
    d.oval(592, 46, 160, 56, "회의록", sub="원본 시각으로 되짚기")
    d.rect(168, 144, 160, 44, "사람이 중간 확인")
    # row 2: omni
    d.label(16, 214, 150, "한 번에 받기 (옴니)")
    d.line("M116,272 H156")
    d.line("M550,272 H590")
    d.oval(16, 248, 100, 48, "녹음")
    d.rect(158, 244, 392, 56, "옴니 모델", sub="듣고 바로 정리 · 확인할 중간 산출물 없음", sub_mono=False)
    d.oval(592, 244, 160, 56, "회의록", sub="오류가 매끄럽게 사라짐")
    return d, 768, 320, "파이프라인과 옴니 모델의 검증 자리", "받아쓰기와 정리를 나누면 중간 산출물에서 사람이 오류를 잡을 수 있고, 옴니 모델은 듣고 바로 정리해 확인할 자리가 없다"


if __name__ == "__main__":
    build([("output-types", output_types), ("pipeline-vs-omni", pipeline_vs_omni)])
