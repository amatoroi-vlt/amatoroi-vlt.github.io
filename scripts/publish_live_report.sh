#!/bin/bash
#
# TraderX가 생성한 라이브 리포트를 Pensieve로 가져와 커밋·푸시한다.
# launchd(com.pensieve.publish)가 소스 파일 변경을 감지해 실행한다.
#
# 이 스크립트가 공개 사이트에 올리는 것은 아래 SRC 한 파일과 그로 인해
# 재생성되는 manifest.json 뿐이다. 그 외 경로는 절대 스테이징하지 않는다.

set -euo pipefail

SRC="/Users/jeongsookang/Documents/dev/TraderX/deeptrx_trial/runs/live_report.html"
REPO="/Users/jeongsookang/Documents/dev/GitHub_blog"
DEST_REL="reports/Overwatch/live_report.html"

GIT=/usr/bin/git
PYTHON=/usr/bin/python3

log() { echo "[$(date '+%F %T')] $*"; }

if [ ! -f "$SRC" ]; then
    log "ERROR: 소스 파일 없음 — $SRC"
    exit 1
fi

cd "$REPO"

# 브랜치 확인 — main이 아니면 손대지 않는다
branch=$($GIT rev-parse --abbrev-ref HEAD)
if [ "$branch" != "main" ]; then
    log "ERROR: 현재 브랜치가 '$branch' — main이 아니므로 중단"
    exit 1
fi

# 작업 트리에 다른 미커밋 변경이 있으면 중단.
# 자동 커밋이 사람이 작업 중인 내용을 함께 삼키는 것을 막는다.
dirty=$($GIT status --porcelain -- "$DEST_REL" manifest.json reports/summaries.json)
if [ -n "$dirty" ]; then
    log "WARN: 대상 파일에 미커밋 변경 존재 — 그대로 진행"
    log "$dirty"
fi

cp "$SRC" "$DEST_REL"

$PYTHON .github/scripts/generate_manifest.py

# WatchPaths는 중복·오탐으로 뜰 수 있다. 실제 변경이 없으면 조용히 종료.
if $GIT diff --quiet -- "$DEST_REL" manifest.json; then
    log "변경 없음 — 건너뜀"
    exit 0
fi

$GIT add "$DEST_REL" manifest.json
$GIT commit -q -m "update: Overwatch 라이브 리포트 자동 갱신 ($(date '+%Y-%m-%d'))"
log "커밋 완료"

# 원격이 앞서 있으면 리베이스. 충돌하면 커밋을 로컬에 남기고 중단해
# 다음 대화형 세션에서 사람이 확인할 수 있게 한다.
$GIT fetch -q origin main
if ! $GIT rebase -q origin/main; then
    $GIT rebase --abort || true
    log "ERROR: 리베이스 충돌 — 커밋은 로컬에 남겨둠. 수동 확인 필요"
    exit 1
fi

$GIT push -q origin main
log "푸시 완료 → origin/main"
