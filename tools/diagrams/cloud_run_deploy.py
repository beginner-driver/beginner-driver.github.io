"""Diagrams for 2026-10-19-cloud-run-deploy. Run: py cloud_run_deploy.py && py shot.py cloud-run-deploy deploy-pipeline request-timeline"""
from gen import D, build, SANS, esc


def deploy_pipeline(t):
    d = D(t)
    xs = [16, 166, 316, 466, 616, 766]
    w = 128
    # main row arrows y=76
    for x in xs[:-1]:
        d.line(f"M{x + w},76 H{x + w + 20}")
    # down to "where to look"
    for x in xs[1:5]:
        d.line(f"M{x + w / 2},104 V168", dashed=True)
    d.label(16, 182, 128, "", lines=["실패하면", "기록이 남는 곳"])
    d.oval(xs[0], 52, w, 48, "내 코드", sub="폴더 하나")
    d.rect(xs[1], 48, w, 56, "빌드", sub="Cloud Build", sub_mono=False)
    d.rect(xs[2], 48, w, 56, "이미지", sub="Artifact Registry", sub_mono=False)
    d.rect(xs[3], 48, w, 56, "리비전", sub="배포마다 남는 버전", sub_mono=False, focal=True)
    d.rect(xs[4], 48, w, 56, "인스턴스", sub="요청 따라 0~N개", sub_mono=False)
    d.oval(xs[5], 52, w, 48, "서비스 URL", sub="공개 주소")
    d.rect(xs[1], 170, w, 56, "빌드 기록", sub="buildpacks 판단", sub_mono=False)
    d.rect(xs[2], 170, w, 56, "저장된 이미지", sub="서비스 지워도 남음", sub_mono=False)
    d.rect(xs[3], 170, w, 56, "리비전 탭", sub="이미지·환경변수·설정", sub_mono=False)
    d.rect(xs[4], 170, w, 56, "로그 탭", sub="요청·컨테이너·시스템", sub_mono=False)
    return d, 910, 246, "배포 명령 하나가 만드는 것", "코드가 빌드, 이미지, 리비전, 인스턴스를 거쳐 공개 주소가 되고, 단계마다 실패 기록이 남는 곳이 따로 있다"


def request_timeline(t):
    d = D(t)
    # timeout bracket over the whole request
    c = t["accent"]
    d.arrows.append(f'<path d="M16,46 V36 H894 V46" fill="none" stroke="{c}" stroke-width="1.4"/>')
    d.label(355, 26, 200, "요청 타임아웃 안에 모두 끝나야 한다", accent=True)
    segs = [
        (16, 140, "콜드 스타트", "최소 0일 때만"),
        (176, 140, "도구 고르기", "LLM 호출 1"),
        (336, 210, "답 스트리밍", "LLM 호출 2 · 글자가 흘러감"),
        (566, 170, "기억 정리", "LLM 호출 3 · 답 보낸 뒤"),
        (756, 138, "done 신호", "화면이 끝을 확인"),
    ]
    for i, (x, w, name, sub) in enumerate(segs):
        if i:
            d.line(f"M{x - 20},84 H{x}")
        d.rect(x, 56, w, 56, name, sub=sub, sub_mono=False, focal=(name == "done 신호"))
    # cut markers
    for x in (441, 651):
        d.arrows.append(f'<path d="M{x},120 V150" fill="none" stroke="{c}" stroke-width="1.4" stroke-dasharray="4,3"/>')
    d.label(336, 156, 210, "", accent=True, lines=["여기서 끊기면", "답이 문장 중간에 잘린다"])
    d.label(556, 156, 190, "", accent=True, lines=["여기서 끊기면", "답은 보였는데 저장이 빠진다"])
    d.label(316, 206, 280, "둘 다 done이 오지 않는다 → 화면이 경고한다")
    return d, 910, 236, "AI 서비스 요청 하나의 시간", "콜드 스타트, 도구 고르기, 답 스트리밍, 기억 정리, done 신호가 모두 요청 타임아웃 안에 들어가야 하고, 중간에 끊기면 잘린 답이나 빠진 저장이 정상처럼 보인다"


if __name__ == "__main__":
    build([("deploy-pipeline", deploy_pipeline), ("request-timeline", request_timeline)])
