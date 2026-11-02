"""Diagrams for 2026-10-30-cost-keys-prompt-injection. Run: py cost_keys_prompt_injection.py && py shot.py cost-keys-prompt-injection cost-guards key-paths"""
from gen import D, build


def cost_guards(t):
    d = D(t)
    d.line("M196,96 H238")
    d.line("M460,96 H528", accent=True)
    d.line("M350,124 V194", dashed=True)
    d.label(462, 72, 64, "부를 때마다")
    d.label(360, 150, 48, "알림만")
    d.label(530, 136, 240, "돈이 실제로 나가는 곳", accent=True)
    d.label(16, 136, 180, "최대 2대도 시간당 7만 건+")
    d.oval(16, 72, 180, 48, "공개 주소 요청", sub="자동 호출 포함")
    d.rect(240, 68, 220, 56, "Cloud Run", sub="최대 인스턴스 = 동시 처리량", sub_mono=False)
    d.rect(530, 68, 240, 56, "LLM 제공사", sub="월 사용 한도 = 총액 차단", sub_mono=False, focal=True)
    d.rect(240, 196, 220, 56, "예산 알림", sub="메일만 보낸다 · 지출은 계속", sub_mono=False)
    return d, 790, 276, "비용을 막는 장치", "공개 주소로 들어온 요청은 Cloud Run을 거쳐 LLM 제공사로 가고, 총액을 실제로 막는 것은 LLM 제공사의 월 사용 한도뿐이며 예산 알림은 메일만 보낸다"


def key_paths(t):
    d = D(t)
    rows = [
        ("에이전트 대화창 · 명령 기록", "붙여 넣은 값이 기록에 남는다", "콘솔에서 사람이 직접 입력", "명령과 대화에는 이름만 쓴다", False),
        ("서비스 설정 화면", "일반 환경변수면 값이 그대로 보인다", "Secret Manager 참조", "설정에는 시크릿 이름만 남는다", True),
        ("저장소 · 소스 배포", ".env가 함께 올라간다", ".gitignore · .gcloudignore", "키 파일은 로컬에만 둔다", False),
        ("컨테이너 이미지", "이미지가 나가면 키도 따라간다", ".dockerignore + 실행할 때 전달", "하위 폴더까지 막으려면 **/", False),
        ("로그 · 오류 메시지", "요청 본문을 통째로 남기면 키가 보인다", "원문·키를 남기지 않는 로그", "화면에는 끝 4자리만", False),
    ]
    y = 56
    for left, lsub, right, rsub, focal in rows:
        d.line(f"M340,{y + 24} H418", accent=focal)
        d.rect(40, y, 300, 48, left, sub=lsub, sub_mono=False)
        d.rect(420, y, 440, 48, right, sub=rsub, sub_mono=False, focal=focal)
        y += 64
    d.label(40, 24, 300, "키 값이 남는 자리")
    d.label(420, 24, 440, "막는 장치")
    return d, 900, y + 8, "키 값이 남는 자리", "키 값은 대화 기록, 서비스 설정, 저장소, 컨테이너 이미지, 로그에 남을 수 있고 자리마다 막는 장치가 다르며 그중 중심은 Secret Manager 참조다"


if __name__ == "__main__":
    build([("cost-guards", cost_guards), ("key-paths", key_paths)])
