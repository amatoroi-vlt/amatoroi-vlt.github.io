#!/usr/bin/env node

/**
 * scripts/secure_build_and_sync.js
 *
 * One-stop automated secure build pipeline:
 * 1. Reads local .env (RESEARCH_PASSWORD, GENERAL_PASSWORD)
 * 2. Encrypts reports_src/ -> reports/
 * 3. Cleans plain image assets from reports/
 * 4. Syncs manifest.json and sanitizes summaries.json
 */

const { execFileSync, execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

console.log('🔄 [Pensieve Secure Build] 자동 암호화 및 동기화 파이프라인 시작...');

// 1. Run encryption
execFileSync('node', [path.join(__dirname, 'encrypt_reports.js')], {
  stdio: 'inherit',
  cwd: ROOT_DIR
});

// 2. Clean plain PNG assets from reports/
const pngs = execSync('find reports -name "*.png" 2>/dev/null', {
  encoding: 'utf8',
  cwd: ROOT_DIR
}).trim().split('\n').filter(Boolean);

for (const p of pngs) {
  const fullP = path.join(ROOT_DIR, p);
  if (fs.existsSync(fullP)) fs.unlinkSync(fullP);
}
if (pngs.length > 0) {
  console.log(`🧹 평문 PNG 파일 ${pngs.length}개 제거 완료.`);
}

// 3. Sync manifest.json
execFileSync('/opt/homebrew/bin/uv', [
  'run', 'python3', '.github/scripts/generate_manifest.py'
], {
  stdio: 'inherit',
  cwd: ROOT_DIR
});

console.log('✅ [Pensieve Secure Build] 전체 암호화 및 매니페스트 동기화 완료!');
