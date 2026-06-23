#!/bin/bash
set -e

VAULT="/Users/jeongsookang/Documents/Obsidian Vault/"
CONTENT="./content"

echo "🔄 Obsidian vault → content/ 동기화 중..."

rsync -av --delete \
  --exclude='.obsidian/' \
  --exclude='.gitignore' \
  --filter='+ */' \
  --filter='+ *.md' \
  --filter='+ *.png' \
  --filter='+ *.jpg' \
  --filter='+ *.jpeg' \
  --filter='+ *.gif' \
  --filter='+ *.svg' \
  --filter='+ *.pdf' \
  --filter='- *' \
  "$VAULT" "$CONTENT/"

echo "📦 Git 커밋 & 푸시 중..."
git add -A
git diff --cached --stat

read -p "이대로 푸시할까요? (y/N) " confirm
if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
  git commit -m "sync: $(date '+%Y-%m-%d %H:%M')" || echo "변경사항 없음"
  git push
  echo "✅ 배포 완료! https://amatoroi-vlt.github.io"
else
  echo "❌ 취소됨 (git add는 이미 된 상태)"
fi
