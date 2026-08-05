#!/usr/bin/env python3
"""
TraderX가 생성한 라이브 리포트를 Pensieve로 가져와 커밋·푸시한다.
launchd(com.pensieve.publish)가 매 거래일 09:10에 실행한다.

파이썬으로 작성한 이유는 취향이 아니라 TCC 때문이다. ~/Documents는 보호
경로라 launchd 에이전트가 접근하려면 실행 바이너리에 권한이 있어야 하는데,
/bin/bash 와 /usr/bin/python3 은 거부되고 deeptrx venv의 python 은 허용된다.
그래서 plist가 `caffeinate -i uv run python` 으로 이 파일을 실행한다.

공개 사이트에 올리는 것은 아래 DEST_REL 한 파일과 그로 인해 재생성되는
manifest.json 뿐이다. 그 외 경로는 절대 스테이징하지 않는다.
"""

import os
import shutil
import subprocess
import sys
from datetime import datetime

SRC = "/Users/jeongsookang/Documents/dev/TraderX/deeptrx_trial/runs/live_report.html"
REPO = "/Users/jeongsookang/Documents/dev/GitHub_blog"
DEST_REL = "reports/Overwatch/live_report.html"
PUBLISH_PATHS = [DEST_REL, "manifest.json"]

# 반드시 homebrew git이어야 한다. keychain 접근 권한(ACL)은 바이너리 경로
# 단위로 붙는데, 대화형 푸시에서 승인 이력이 쌓인 것은 homebrew git이 쓰는
# helper다. /usr/bin/git(Apple CLT)은 다른 경로의 helper를 호출하므로 승인이
# 없어 프롬프트를 띄우려 하고, UI가 없는 launchd에서는 그대로 취소된다(-128).
GIT = "/opt/homebrew/bin/git"


def log(msg):
    print(f"[{datetime.now():%Y-%m-%d %H:%M:%S}] {msg}", flush=True)


def git(*args, check=True):
    return subprocess.run(
        [GIT, *args], cwd=REPO, check=check,
        capture_output=True, text=True,
    )


def main():
    if not os.path.isfile(SRC):
        log(f"ERROR: 소스 파일 없음 — {SRC}")
        return 1

    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if branch != "main":
        log(f"ERROR: 현재 브랜치가 '{branch}' — main이 아니므로 중단")
        return 1

    shutil.copyfile(SRC, os.path.join(REPO, DEST_REL))

    manifest = subprocess.run(
        [sys.executable, ".github/scripts/generate_manifest.py"],
        cwd=REPO, capture_output=True, text=True,
    )
    if manifest.returncode != 0:
        log(f"ERROR: manifest 생성 실패\n{manifest.stderr}")
        return 1
    log(manifest.stdout.strip())

    # 소스가 그대로면(리뷰 잡 실패로 어제 파일이 남아있는 경우 포함) 무동작.
    # 이미 발행된 내용과 같으므로 헌 파일을 다시 밀어넣을 위험이 없다.
    if git("diff", "--quiet", "--", *PUBLISH_PATHS, check=False).returncode == 0:
        log("변경 없음 — 건너뜀")
        return 0

    git("add", *PUBLISH_PATHS)
    git("commit", "-q", "-m",
        f"update: Overwatch 라이브 리포트 자동 갱신 ({datetime.now():%Y-%m-%d})")
    log("커밋 완료")

    # 원격이 앞서 있을 때만 리베이스한다. 무조건 돌리면, 리베이스는 작업
    # 트리가 깨끗하길 요구하므로 이 레포와 무관한 미커밋 변경(.claude/*.lock 등)
    # 때문에 불필요하게 실패한다. --autostash로 그 경우도 넘긴다.
    git("fetch", "-q", "origin", "main")
    behind = int(git("rev-list", "--count", "HEAD..origin/main").stdout.strip())
    if behind:
        log(f"원격이 {behind}커밋 앞섬 — 리베이스")
        if git("rebase", "--autostash", "-q", "origin/main", check=False).returncode != 0:
            git("rebase", "--abort", check=False)
            log("ERROR: 리베이스 충돌 — 커밋은 로컬에 남겨둠. 수동 확인 필요")
            return 1

    push = git("push", "-q", "origin", "main", check=False)
    if push.returncode != 0:
        log(f"ERROR: 푸시 실패 — 커밋은 로컬에 남겨둠\n{push.stderr.strip()}")
        return 1

    log("푸시 완료 → origin/main")
    return 0


if __name__ == "__main__":
    sys.exit(main())
