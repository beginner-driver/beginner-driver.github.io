"""Diagrams for _posts/2026-07-22-youtube-channel-category.md"""
from gen import D, build


def yt_architecture(t):
    d = D(t)
    # arrows
    d.line("M120,170 H166")
    d.line("M318,170 H368")
    d.line("M530,160 H570 Q578,160 578,152 V72 Q578,64 586,64 H618")
    d.line("M530,170 H618")
    d.line("M530,180 H570 Q578,180 578,188 V268 Q578,276 586,276 H618")
    # where it broke (accent notes under each boundary)
    d.label(622, 96, 180, "① 환경변수 이름 불일치", accent=True)
    d.label(622, 202, 180, "③ 리전이 달라 왕복 지연", accent=True)
    d.label(622, 308, 180, "② 한글 채널 주소 해석", accent=True)
    # nodes
    d.oval(16, 146, 104, 48, "사용자", sub="브라우저")
    d.rect(168, 146, 150, 48, "화면 2개", sub="채널 관리 · 피드", sub_mono=False)
    d.rect(370, 146, 160, 48, "API Routes", sub="Next.js 서버", focal=True, sub_mono=False)
    d.rect(620, 40, 184, 48, "Google 로그인", sub="Auth.js")
    d.rect(620, 146, 184, 48, "Supabase Postgres", sub="Prisma")
    d.rect(620, 252, 184, 48, "YouTube Data API", sub="서버 API 키", sub_mono=False)
    return d, 820, 340, "서비스 구조와 깨진 지점", "화면과 API Routes는 Next.js 하나로 만들고, 바깥 서비스 세 곳과 만나는 경계에서 버그 세 개가 나온 구조"


if __name__ == "__main__":
    build([("yt-architecture", yt_architecture)])
