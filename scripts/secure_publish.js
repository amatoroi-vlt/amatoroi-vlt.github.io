#!/usr/bin/env node

/**
 * scripts/secure_publish.js
 *
 * Interactive terminal utility for:
 * 1. Safely prompting for Research and General passwords (hidden input)
 * 2. Running multi-vault client-side encryption from reports_src/ to reports/
 * 3. Updating manifest.json and sanitizing summaries
 * 4. Cleaning plain image artifacts from reports/
 * 5. Optionally resetting Git history to a clean slate and force-pushing to GitHub
 */

const readline = require('readline');
const { execFileSync, execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..');

function promptHidden(question) {
  return new Promise((resolve) => {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    // Mute terminal stdout while typing password
    const stdin = process.stdin;
    process.stdout.write(question);

    let password = '';
    const oldRawMode = stdin.isRaw;
    if (stdin.isTTY) {
      stdin.setRawMode(true);
    }
    stdin.resume();

    const onData = (chunk) => {
      const char = chunk.toString();
      for (let i = 0; i < char.length; i++) {
        const c = char[i];
        if (c === '\n' || c === '\r' || c === '\u0004') {
          stdin.removeListener('data', onData);
          if (stdin.isTTY) stdin.setRawMode(oldRawMode || false);
          process.stdout.write('\n');
          rl.close();
          resolve(password);
          return;
        } else if (c === '\u0003') {
          // Ctrl+C
          process.stdout.write('\n');
          process.exit(1);
        } else if (c === '\b' || c === '\x7f') {
          // Backspace
          if (password.length > 0) {
            password = password.slice(0, -1);
          }
        } else {
          password += c;
        }
      }
    };

    stdin.on('data', onData);
  });
}

function promptNormal(question) {
  return new Promise((resolve) => {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer.trim());
    });
  });
}

async function main() {
  console.log('\n======================================================');
  console.log('🔒 Pensieve 개인 연구 포털 다중 보안 빌드 & 배포 도구');
  console.log('======================================================\n');
  console.log('※ 비밀번호 입력 시 터미널 화면에 글자가 노출되지 않습니다.');
  console.log('※ 쉘 히스토리(~/.zsh_history)에도 비밀번호가 기록되지 않습니다.\n');

  // 1. Prompt passwords
  let researchPass = await promptHidden('🔑 [Research 폴더] 전용 비밀번호 입력: ');
  while (!researchPass) {
    console.log('  ⚠️ 비밀번호는 비어 있을 수 없습니다.');
    researchPass = await promptHidden('🔑 [Research 폴더] 전용 비밀번호 입력: ');
  }

  let generalPass = await promptHidden('🔑 [Invest / Overwatch 등 일반 폴더] 비밀번호 입력: ');
  while (!generalPass) {
    console.log('  ⚠️ 비밀번호는 비어 있을 수 없습니다.');
    generalPass = await promptHidden('🔑 [Invest / Overwatch 등 일반 폴더] 비밀번호 입력: ');
  }

  console.log('\n⚙️  1. reports_src/ 원본을 읽어 다중 볼트 암호화를 시작합니다...');
  execFileSync('node', [
    path.join(__dirname, 'encrypt_reports.js'),
    `--research-password=${researchPass}`,
    `--general-password=${generalPass}`
  ], { stdio: 'inherit', cwd: ROOT_DIR });

  console.log('\n🧹 2. reports/ 내 불필요한 평문 이미지 에셋을 정리합니다...');
  const pngs = execSync('find reports -name "*.png" 2>/dev/null', { encoding: 'utf8', cwd: ROOT_DIR }).trim().split('\n').filter(Boolean);
  for (const p of pngs) {
    const fullP = path.join(ROOT_DIR, p);
    if (fs.existsSync(fullP)) fs.unlinkSync(fullP);
  }
  console.log(`  - 평문 PNG 파일 ${pngs.length}개 제거 완료 (HTML 내부 Base64 인라인 암호화 보존).`);

  console.log('\n📋 3. manifest.json 동기화 스크립트를 실행합니다...');
  execFileSync('/opt/homebrew/bin/uv', [
    'run', 'python3', '.github/scripts/generate_manifest.py'
  ], { stdio: 'inherit', cwd: ROOT_DIR });

  console.log('\n======================================================');
  console.log('✅ 로컬 암호화 빌드가 성공적으로 완료되었습니다!');
  console.log('======================================================\n');

  const doPush = await promptNormal('❓ 과거 모든 커밋 히스토리를 삭제하고 원격 저장소에 단일 보안 커밋으로 강제 푸시(git push -f)할까요? (y/N): ');

  if (doPush.toLowerCase() === 'y' || doPush.toLowerCase() === 'yes') {
    console.log('\n🚀 Git 히스토리 초기화 및 강제 푸시를 진행합니다...');
    
    // Create orphan branch
    execSync('git checkout --orphan secured-clean-slate', { stdio: 'inherit', cwd: ROOT_DIR });
    execSync('git add -A', { stdio: 'inherit', cwd: ROOT_DIR });
    execSync('git commit -m "feat: initialize secured personal research portal with client-side encryption"', { stdio: 'inherit', cwd: ROOT_DIR });
    
    // Switch to main
    try {
      execSync('git branch -D main', { stdio: 'inherit', cwd: ROOT_DIR });
    } catch(e) {}
    execSync('git branch -m main', { stdio: 'inherit', cwd: ROOT_DIR });

    console.log('\n📡 GitHub origin main으로 강제 푸시 중...');
    execSync('git push -f origin main', { stdio: 'inherit', cwd: ROOT_DIR });

    console.log('\n🎉 [성공] 과거 히스토리가 완전히 소거되었으며, 암호화된 최신 포털이 배포되었습니다!');
  } else {
    console.log('\n💡 원격 푸시를 건너뛰었습니다. 로컬에서 브라우저로 먼저 확인하신 후 원할 때 푸시하실 수 있습니다.');
    console.log('  - 수동 푸시 명령어:');
    console.log('    git checkout --orphan clean-init');
    console.log('    git add -A');
    console.log('    git commit -m "feat: initialize secured personal research portal"');
    console.log('    git branch -D main && git branch -m main');
    console.log('    git push -f origin main\n');
  }
}

main().catch(err => {
  console.error('\n❌ 오류 발생:', err.message);
  process.exit(1);
});
