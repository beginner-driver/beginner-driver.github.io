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


def yt_feed(t):
    d = D(t)
    d.line("M112,64 H134")
    d.line("M264,64 H286")
    d.line("M416,64 H438")
    d.line("M568,64 H590")
    d.line("M720,64 H742")
    d.line("M352,92 V124", accent=True, dashed=True)
    d.label(222, 128, 260, "", accent=True, lines=["채널마다 최근 5개만 가져온다", "→ 오래된 즐겨찾기는 피드에서 빠진다"])
    d.oval(16, 40, 96, 48, "피드 열기")
    d.rect(136, 36, 128, 56, "내 채널", sub="DB · Channel")
    d.rect(288, 36, 128, 56, "최신 영상 5개", sub="playlistItems", focal=True)
    d.rect(440, 36, 128, 56, "영상 길이", sub="videos.list")
    d.rect(592, 36, 128, 56, "체크·하트", sub="DB · VideoStatus")
    d.oval(744, 40, 96, 48, "최신순 표시")
    return d, 856, 176, "카테고리 피드를 여는 순서", "DB에서 채널을 읽고 유튜브 API로 채널별 최신 영상 5개와 길이를 가져온 뒤 체크와 즐겨찾기 상태를 합쳐 최신순으로 보여주는 흐름"


if __name__ == "__main__":
    build([("yt-architecture", yt_architecture), ("yt-feed", yt_feed)])
