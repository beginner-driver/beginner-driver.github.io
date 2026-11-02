"""Diagrams for 2026-08-02-cloud-api-vs-local-llm. Run: py cloud_api_vs_local_llm.py && py shot.py cloud-api-vs-local-llm run-locations memory-budget"""
from gen import D, build, SANS, esc


def run_locations(t):
    d = D(t)
    # data -> three destinations
    d.line("M168,150 Q220,150 220,100 V66 Q220,56 230,56 H290")
    d.line("M168,150 H290")
    d.line("M168,150 Q220,150 220,200 V234 Q220,244 230,244 H290", accent=True)
    # destination -> where data goes
    for y in (56, 150, 244):
        d.line(f"M470,{y} H508", dashed=True)
    d.oval(16, 126, 152, 48, "내 입력 데이터", sub="프롬프트 · 문서")
    d.rect(292, 28, 178, 56, "공개 클라우드 API", sub="키 발급 후 몇 분", sub_mono=False)
    d.rect(292, 122, 178, 56, "관리형 프라이빗 배포", sub="계약 · 리전 · 권한", sub_mono=False)
    d.rect(292, 216, 178, 56, "로컬 · 온프레미스", sub="공개 가중치 모델", sub_mono=False, focal=True)
    d.rect(510, 28, 390, 56, "제공사 공용 인프라로 간다", sub="확인: 처리 리전 · 로그 보관 · 학습 사용", sub_mono=False)
    d.rect(510, 122, 390, 56, "지정 리전의 전용 환경으로 간다", sub="확인: 배포 유형마다 처리 리전이 다르다", sub_mono=False)
    d.rect(510, 216, 390, 56, "내 장비 밖으로 나가지 않는다", sub="대신 패치 · 업데이트 · 가동률이 내 몫", sub_mono=False)
    return d, 916, 300, "실행 위치 세 갈래", "같은 입력이 공개 API, 관리형 프라이빗 배포, 로컬 중 어디로 가느냐에 따라 데이터가 머무는 곳과 확인할 항목이 달라진다"


def memory_budget(t):
    d = D(t)
    x0, s = 130, 30          # px per GB
    rows = [("4K 토큰", 0.52, "약 5.1 GB"), ("32K 토큰", 4.19, "약 8.8 GB"), ("128K 토큰", 16.78, "약 21.4 GB")]
    w_gb = 4.6
    txt = lambda x, y, s_, color, anchor="start", size=13, weight=500: (
        f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}" font-weight="{weight}" font-family="{SANS}" text-anchor="{anchor}">{esc(s_)}</text>')
    # legend
    d.nodes.append(f'<rect x="{x0}" y="18" width="16" height="12" rx="2" fill="{t["node"]}" stroke="{t["ink"]}"/>')
    d.nodes.append(txt(x0 + 22, 29, "가중치 (8B · 4비트)", t["muted"], size=12))
    d.nodes.append(f'<rect x="{x0 + 170}" y="18" width="16" height="12" rx="2" fill="{t["tint"]}" stroke="{t["accent"]}"/>')
    d.nodes.append(txt(x0 + 192, 29, "KV cache (입력이 길수록 커짐)", t["muted"], size=12))
    # 16GB line
    lx = x0 + 16 * s
    d.arrows.append(f'<path d="M{lx},48 V230" stroke="{t["muted"]}" stroke-width="1.2" stroke-dasharray="5,4"/>')
    d.nodes.append(txt(lx, 246, "16 GB 메모리", t["muted"], anchor="middle", size=12))
    for i, (name, kv, total) in enumerate(rows):
        y = 64 + i * 56
        d.nodes.append(txt(x0 - 14, y + 22, name, t["ink"], anchor="end", size=13, weight=600))
        ww, kw = w_gb * s, kv * s
        d.nodes.append(f'<rect x="{x0}" y="{y}" width="{ww}" height="32" rx="3" fill="{t["node"]}" stroke="{t["ink"]}"/>')
        d.nodes.append(f'<rect x="{x0 + ww}" y="{y}" width="{kw}" height="32" rx="3" fill="{t["tint"]}" stroke="{t["accent"]}"/>')
        d.nodes.append(txt(x0 + ww + kw + 10, y + 21, total, t["accent"] if i == 2 else t["muted"], size=13, weight=600))
    return d, 920, 264, "필요 메모리는 가중치에 KV cache를 더한 값", "같은 8B 4비트 모델이라도 입력 길이가 4K, 32K, 128K로 늘면 KV cache가 커져 128K에서는 16GB를 넘는다"


if __name__ == "__main__":
    build([("run-locations", run_locations), ("memory-budget", memory_budget)])
