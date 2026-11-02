"""Diagrams for 2026-07-21-coding-agent-skills-rules. Run: py coding_agent_skills_rules.py && py shot.py coding-agent-skills-rules rules-skills-loading skill-calls-cli"""
from gen import D, build


def rules_skills_loading(t):
    d = D(t)
    # arrows
    d.line("M128,92 H158")
    d.line("M350,92 H380")
    d.line("M572,92 H602")
    d.line("M674,116 V164")
    d.line("M604,210 H574", accent=True)                 # 예
    d.line("M382,210 H352", accent=True)
    d.line("M674,256 V296")                              # 아니오
    # labels
    d.label(578, 186, 20, "예", accent=True)
    d.label(684, 266, 44, "아니오")
    # nodes
    d.oval(16, 68, 112, 48, "새 대화 시작")
    d.rect(160, 64, 190, 56, "규칙 파일 전부 읽기", sub="CLAUDE.md · AGENTS.md")
    d.rect(382, 64, 190, 56, "스킬은 목록만 읽기", sub="이름 + 한 줄 설명", sub_mono=False)
    d.oval(604, 68, 140, 48, "사용자 요청")
    d.diamond(674, 210, 70, 46, ["맞는 스킬이", "있나?"])
    d.rect(382, 182, 190, 56, "스킬 본문 읽기", sub="SKILL.md · 필요할 때만", focal=True, sub_mono=False)
    d.rect(160, 182, 190, 56, "스크립트·명령 실행", sub="scripts/ · CLI")
    d.oval(594, 298, 160, 48, "규칙만 지키며 작업")
    return d, 760, 368, "규칙 파일과 스킬이 읽히는 순서", "대화를 시작하면 규칙 파일은 전부, 스킬은 이름과 설명만 읽고, 요청이 스킬 설명과 맞을 때만 스킬 본문을 읽어 실행하는 흐름"


def skill_calls_cli(t):
    d = D(t)
    d.line("M216,96 H246")
    d.line("M418,96 H448", accent=True)
    d.line("M620,96 H636 Q642,96 642,90 V56 Q642,50 648,50 H658")
    d.line("M620,96 H636 Q642,96 642,102 V132 Q642,138 648,138 H658")
    d.oval(16, 68, 200, 56, "사용자 한마디", sub="깃허브 폴더 추가해줘 <경로>")
    d.rect(248, 68, 170, 56, "스킬 지침", sub="github-init.md", focal=True)
    d.rect(450, 68, 170, 56, "실행 스크립트", sub="github_init.py")
    d.rect(660, 24, 200, 52, "저장소 만들기", sub="GitHub API", sub_mono=False)
    d.rect(660, 112, 200, 52, "파일 올리기", sub="git init → commit → push")
    return d, 880, 188, "스킬이 스크립트를 불러 주는 구조", "사용자 한마디가 스킬 지침을 깨우고, 지침이 실행 스크립트를 불러 GitHub 저장소를 만들고 파일을 올리는 흐름"


if __name__ == "__main__":
    build([("rules-skills-loading", rules_skills_loading), ("skill-calls-cli", skill_calls_cli)])
