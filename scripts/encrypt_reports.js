#!/usr/bin/env node

/**
 * scripts/encrypt_reports.js
 *
 * Client-side AES-256-GCM Self-Decrypting Report Builder
 * Supports multi-vault / folder-level password separation:
 *  - Research folder: --research-password / RESEARCH_PASSWORD
 *  - General/Invest/Overwatch: --general-password / GENERAL_PASSWORD
 *  - Fallback master password: --password / REPORTS_PASSWORD
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const ROOT_DIR = path.resolve(__dirname, '..');
const SRC_DIR = path.join(ROOT_DIR, 'reports_src');
const DEST_DIR = path.join(ROOT_DIR, 'reports');

// Load local .env if available
const envPath = path.join(ROOT_DIR, '.env');
if (fs.existsSync(envPath)) {
  const envContent = fs.readFileSync(envPath, 'utf8');
  for (const line of envContent.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#')) continue;
    const eqIdx = trimmed.indexOf('=');
    if (eqIdx !== -1) {
      const key = trimmed.slice(0, eqIdx).trim();
      let val = trimmed.slice(eqIdx + 1).trim();
      if ((val.startsWith('"') && val.endsWith('"')) || (val.startsWith("'") && val.endsWith("'"))) {
        val = val.slice(1, -1);
      }
      if (!process.env[key]) {
        process.env[key] = val;
      }
    }
  }
}

// Parse CLI arguments
const args = process.argv.slice(2);
let masterPassword = process.env.REPORTS_PASSWORD || '';
let researchPassword = process.env.RESEARCH_PASSWORD || '';
let generalPassword = process.env.GENERAL_PASSWORD || '';

for (let i = 0; i < args.length; i++) {
  const arg = args[i];
  if (arg === '--password' || arg === '-p') {
    masterPassword = args[++i] || '';
  } else if (arg.startsWith('--password=')) {
    masterPassword = arg.split('=')[1] || '';
  } else if (arg === '--research-password' || arg === '-rp') {
    researchPassword = args[++i] || '';
  } else if (arg.startsWith('--research-password=')) {
    researchPassword = arg.split('=')[1] || '';
  } else if (arg === '--general-password' || arg === '-gp') {
    generalPassword = args[++i] || '';
  } else if (arg.startsWith('--general-password=')) {
    generalPassword = arg.split('=')[1] || '';
  }
}

// Fallbacks
if (!researchPassword) researchPassword = masterPassword;
if (!generalPassword) generalPassword = masterPassword;

if (!researchPassword && !generalPassword) {
  console.error('Error: Passwords are required.');
  console.error('Usage: node scripts/encrypt_reports.js --research-password="<PASS1>" --general-password="<PASS2>"');
  console.error('   or: node scripts/encrypt_reports.js --password="<SINGLE_MASTER_PASS>"');
  process.exit(1);
}

function getAllFiles(dir, fileList = []) {
  if (!fs.existsSync(dir)) return fileList;
  const files = fs.readdirSync(dir);
  for (const file of files) {
    if (file === '.DS_Store' || file === 'summaries.json') continue;
    const fullPath = path.join(dir, file);
    if (fs.statSync(fullPath).isDirectory()) {
      getAllFiles(fullPath, fileList);
    } else {
      fileList.push(fullPath);
    }
  }
  return fileList;
}

function extractTitle(htmlContent) {
  const match = htmlContent.match(/<title[^>]*>(.*?)<\/title>/i);
  if (match) {
    return match[1].replace(/<[^>]+>/g, '').trim();
  }
  return '보호된 보고서';
}

function inlineLocalAssets(htmlContent, htmlFilePath) {
  const htmlDir = path.dirname(htmlFilePath);
  
  return htmlContent.replace(/<img([^>]+)src=["']([^"']+)["']([^>]*)>/gi, (match, prefix, src, suffix) => {
    if (src.startsWith('data:') || src.startsWith('http://') || src.startsWith('https://')) {
      return match;
    }
    const resolvedPath = path.resolve(htmlDir, src);
    if (fs.existsSync(resolvedPath) && fs.statSync(resolvedPath).isFile()) {
      const ext = path.extname(resolvedPath).toLowerCase();
      let mime = 'image/png';
      if (ext === '.jpg' || ext === '.jpeg') mime = 'image/jpeg';
      else if (ext === '.svg') mime = 'image/svg+xml';
      else if (ext === '.gif') mime = 'image/gif';
      else if (ext === '.webp') mime = 'image/webp';
      
      const fileBuffer = fs.readFileSync(resolvedPath);
      const base64Data = fileBuffer.toString('base64');
      const dataUri = `data:${mime};base64,${base64Data}`;
      return `<img${prefix}src="${dataUri}"${suffix}>`;
    }
    return match;
  });
}

function encryptAesGcm(text, pass) {
  const salt = crypto.randomBytes(16);
  const iv = crypto.randomBytes(12);
  const key = crypto.pbkdf2Sync(pass, salt, 100000, 32, 'sha256');
  
  const cipher = crypto.createCipheriv('aes-256-gcm', key, iv);
  const encrypted = Buffer.concat([cipher.update(text, 'utf8'), cipher.final()]);
  const tag = cipher.getAuthTag();
  
  const combined = Buffer.concat([salt, iv, encrypted, tag]);
  return combined.toString('base64');
}

function generateLockedHtml(title, base64Payload, vaultType) {
  const escapedTitle = title.replace(/"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  
  let vaultBadge = '보호된 연구 및 분석 보고서';
  let storageKey = '__pensieve_vault_pass__';
  let accentColor = '#38bdf8';
  let accentGradient = 'linear-gradient(135deg, #0284c7 0%, #0369a1 100%)';
  let accentHover = 'linear-gradient(135deg, #0369a1 0%, #075985 100%)';

  if (vaultType === 'Research') {
    vaultBadge = '🔬 Research Vault (연구 기밀 문서)';
    storageKey = '__pensieve_research_vault_pass__';
    accentColor = '#818cf8'; // Indigo
    accentGradient = 'linear-gradient(135deg, #6366f1 0%, #4f46e5 100%)';
    accentHover = 'linear-gradient(135deg, #4f46e5 0%, #4338ca 100%)';
  } else if (vaultType === 'Invest') {
    vaultBadge = '📈 Invest Vault (투자 분석 문서)';
    storageKey = '__pensieve_invest_vault_pass__';
    accentColor = '#34d399'; // Emerald
    accentGradient = 'linear-gradient(135deg, #059669 0%, #047857 100%)';
    accentHover = 'linear-gradient(135deg, #047857 0%, #065f46 100%)';
  } else {
    vaultBadge = '🛡️ Overwatch Vault (보안 모니터링 문서)';
    storageKey = '__pensieve_general_vault_pass__';
  }

  return `<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${escapedTitle}</title>
  <style>
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html, body {
      height: 100%;
      background: #090d16;
      color: #e6edf3;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }
    .background-glow {
      position: absolute;
      width: 600px;
      height: 600px;
      background: radial-gradient(circle, rgba(99, 102, 241, 0.08) 0%, rgba(15, 23, 42, 0.03) 50%, transparent 70%);
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      z-index: 0;
      pointer-events: none;
    }
    .card {
      position: relative;
      z-index: 1;
      width: 90%;
      max-width: 450px;
      padding: 38px 32px;
      background: rgba(17, 24, 39, 0.88);
      backdrop-filter: blur(24px);
      -webkit-backdrop-filter: blur(24px);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 20px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6), 0 0 0 1px rgba(255, 255, 255, 0.05);
      text-align: center;
      animation: fadeIn 0.4s ease-out;
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(12px) scale(0.98); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }
    @keyframes shake {
      0%, 100% { transform: translateX(0); }
      20%, 60% { transform: translateX(-8px); }
      40%, 80% { transform: translateX(8px); }
    }
    .shake {
      animation: shake 0.35s ease-in-out;
    }
    .lock-icon {
      width: 58px;
      height: 58px;
      margin: 0 auto 18px;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: ${accentColor};
    }
    .lock-icon svg {
      width: 28px;
      height: 28px;
      stroke-width: 2;
    }
    .vault-tag {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.04em;
      color: ${accentColor};
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 4px 10px;
      border-radius: 20px;
      margin-bottom: 12px;
    }
    h1 {
      font-size: 1.15rem;
      font-weight: 600;
      color: #f3f4f6;
      margin-bottom: 8px;
      line-height: 1.4;
      word-break: keep-all;
    }
    p.desc {
      font-size: 0.85rem;
      color: #94a3b8;
      margin-bottom: 24px;
      line-height: 1.5;
    }
    .input-group {
      position: relative;
      margin-bottom: 16px;
      text-align: left;
    }
    input[type="password"], input[type="text"] {
      width: 100%;
      padding: 13px 44px 13px 16px;
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 12px;
      color: #ffffff;
      font-size: 0.95rem;
      outline: none;
      transition: all 0.2s ease;
    }
    input:focus {
      border-color: ${accentColor};
      box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.25);
      background: rgba(15, 23, 42, 0.95);
    }
    .toggle-pw {
      position: absolute;
      right: 12px;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      color: #64748b;
      cursor: pointer;
      padding: 4px;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: color 0.15s;
    }
    .toggle-pw:hover {
      color: #94a3b8;
    }
    .btn-unlock {
      width: 100%;
      padding: 13px;
      background: ${accentGradient};
      color: #ffffff;
      border: none;
      border-radius: 12px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      transition: all 0.2s;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
    }
    .btn-unlock:hover {
      background: ${accentHover};
      transform: translateY(-1px);
    }
    .btn-unlock:active {
      transform: translateY(0);
    }
    .btn-unlock:disabled {
      opacity: 0.6;
      cursor: not-allowed;
      transform: none;
    }
    .error-msg {
      margin-top: 14px;
      font-size: 0.82rem;
      color: #f87171;
      min-height: 18px;
      opacity: 0;
      transition: opacity 0.2s;
    }
    .error-msg.visible {
      opacity: 1;
    }
    .spinner {
      display: none;
      width: 18px;
      height: 18px;
      border: 2px solid rgba(255, 255, 255, 0.3);
      border-top-color: #ffffff;
      border-radius: 50%;
      animation: spin 0.8s linear infinite;
    }
    @keyframes spin {
      to { transform: rotate(360deg); }
    }
  </style>
</head>
<body>
  <div class="background-glow"></div>
  <div class="card" id="lockCard">
    <div class="lock-icon">
      <svg fill="none" viewBox="0 0 24 24" stroke="currentColor">
        <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/>
      </svg>
    </div>
    <div class="vault-tag">${vaultBadge}</div>
    <h1>${escapedTitle}</h1>
    <p class="desc">보호된 문서입니다.<br>열람하려면 비밀번호를 입력하세요.</p>
    
    <div class="input-group">
      <input type="password" id="pwInput" placeholder="비밀번호 입력" autocomplete="current-password" autofocus>
      <button type="button" class="toggle-pw" id="togglePw" title="비밀번호 보기">
        <svg id="eyeIcon" width="18" height="18" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/>
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"/>
        </svg>
      </button>
    </div>

    <button class="btn-unlock" id="unlockBtn">
      <span class="spinner" id="btnSpinner"></span>
      <span id="btnText">열람하기</span>
    </button>
    <div class="error-msg" id="errorMsg">비밀번호가 올바르지 않습니다.</div>
  </div>

  <script>
    const CIPHERTEXT = "${base64Payload}";
    const STORAGE_KEY = "${storageKey}";

    const pwInput = document.getElementById('pwInput');
    const unlockBtn = document.getElementById('unlockBtn');
    const lockCard = document.getElementById('lockCard');
    const errorMsg = document.getElementById('errorMsg');
    const btnSpinner = document.getElementById('btnSpinner');
    const btnText = document.getElementById('btnText');
    const togglePw = document.getElementById('togglePw');

    togglePw.addEventListener('click', () => {
      const isPw = pwInput.type === 'password';
      pwInput.type = isPw ? 'text' : 'password';
    });

    pwInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') unlock();
    });
    unlockBtn.addEventListener('click', unlock);

    async function decryptPayload(base64Payload, password) {
      const binaryString = atob(base64Payload);
      const bytes = new Uint8Array(binaryString.length);
      for (let i = 0; i < binaryString.length; i++) {
        bytes[i] = binaryString.charCodeAt(i);
      }
      
      const salt = bytes.slice(0, 16);
      const iv = bytes.slice(16, 28);
      const data = bytes.slice(28);
      
      const pwBytes = new TextEncoder().encode(password);
      const keyMaterial = await crypto.subtle.importKey(
        'raw', pwBytes, { name: 'PBKDF2' }, false, ['deriveKey']
      );
      
      const aesKey = await crypto.subtle.deriveKey(
        { name: 'PBKDF2', salt: salt, iterations: 100000, hash: 'SHA-256' },
        keyMaterial,
        { name: 'AES-GCM', length: 256 },
        false,
        ['decrypt']
      );
      
      const decryptedBuf = await crypto.subtle.decrypt(
        { name: 'AES-GCM', iv: iv },
        aesKey,
        data
      );
      
      return new TextDecoder().decode(decryptedBuf);
    }

    function renderDecrypted(html) {
      document.open();
      document.write(html);
      document.close();
    }

    async function unlock() {
      const pass = pwInput.value;
      if (!pass) {
        pwInput.focus();
        return;
      }

      setLoading(true);
      errorMsg.classList.remove('visible');
      lockCard.classList.remove('shake');

      try {
        const decryptedHtml = await decryptPayload(CIPHERTEXT, pass);
        try {
          sessionStorage.setItem(STORAGE_KEY, pass);
        } catch (e) {}
        renderDecrypted(decryptedHtml);
      } catch (err) {
        setLoading(false);
        lockCard.classList.add('shake');
        errorMsg.classList.add('visible');
        pwInput.value = '';
        pwInput.focus();
      }
    }

    function setLoading(isLoading) {
      unlockBtn.disabled = isLoading;
      pwInput.disabled = isLoading;
      btnSpinner.style.display = isLoading ? 'inline-block' : 'none';
      btnText.textContent = isLoading ? '복호화 중...' : '열람하기';
    }

    // Auto-unlock with session cache
    window.addEventListener('DOMContentLoaded', async () => {
      let cached = null;
      try {
        cached = sessionStorage.getItem(STORAGE_KEY);
      } catch (e) {}
      
      if (cached) {
        setLoading(true);
        try {
          const decryptedHtml = await decryptPayload(CIPHERTEXT, cached);
          renderDecrypted(decryptedHtml);
        } catch (e) {
          try { sessionStorage.removeItem(STORAGE_KEY); } catch(err) {}
          setLoading(false);
        }
      }
    });
  </script>
</body>
</html>`;
}

function run() {
  console.log('====================================================');
  console.log('🔒 Pensieve Multi-Vault Encrypted Report Builder');
  console.log('====================================================');
  console.log(`Source: ${SRC_DIR}`);
  console.log(`Output: ${DEST_DIR}\n`);

  if (!fs.existsSync(SRC_DIR)) {
    console.error(`Error: Source directory '${SRC_DIR}' does not exist.`);
    process.exit(1);
  }

  const allFiles = getAllFiles(SRC_DIR);
  const htmlFiles = allFiles.filter(f => f.endsWith('.html'));

  console.log(`Found ${htmlFiles.length} HTML reports to encrypt.`);
  console.log(`- Research Vault: [Configured]`);
  console.log(`- General/Invest Vault: [Configured]\n`);

  let encryptedCount = 0;

  for (const srcFile of htmlFiles) {
    const relPath = path.relative(SRC_DIR, srcFile);
    const destFile = path.join(DEST_DIR, relPath);
    const destSubdir = path.dirname(destFile);

    if (!fs.existsSync(destSubdir)) {
      fs.mkdirSync(destSubdir, { recursive: true });
    }

    // Determine vault type and corresponding password
    let vaultType = 'General';
    let targetPassword = generalPassword;
    if (relPath.startsWith('Research' + path.sep)) {
      vaultType = 'Research';
      targetPassword = researchPassword;
    } else if (relPath.startsWith('Invest' + path.sep)) {
      vaultType = 'Invest';
      targetPassword = generalPassword;
    } else if (relPath.startsWith('Overwatch' + path.sep)) {
      vaultType = 'Overwatch';
      targetPassword = generalPassword;
    }

    let originalHtml = fs.readFileSync(srcFile, 'utf8');
    const docTitle = extractTitle(originalHtml);

    // Inline local image assets into HTML before encrypting
    originalHtml = inlineLocalAssets(originalHtml, srcFile);

    // Encrypt payload with the vault-specific password
    const cipherPayload = encryptAesGcm(originalHtml, targetPassword);

    // Generate wrapped locked HTML
    const wrappedHtml = generateLockedHtml(docTitle, cipherPayload, vaultType);

    fs.writeFileSync(destFile, wrappedHtml, 'utf8');
    encryptedCount++;
    console.log(`  [OK] Encrypted: [${vaultType}] ${relPath}`);
  }

  // Handle summaries.json
  const srcSummaries = path.join(SRC_DIR, 'summaries.json');
  const destSummaries = path.join(DEST_DIR, 'summaries.json');
  if (fs.existsSync(srcSummaries)) {
    try {
      const summaries = JSON.parse(fs.readFileSync(srcSummaries, 'utf8'));
      const maskedSummaries = {};
      for (const [key, val] of Object.entries(summaries)) {
        const targetPath = path.join(ROOT_DIR, key);
        let newHash = val.hash;
        if (fs.existsSync(targetPath)) {
          const buf = fs.readFileSync(targetPath);
          newHash = crypto.createHash('sha1').update(buf).digest('hex');
        }
        maskedSummaries[key] = {
          hash: newHash,
          summary: '🔒 암호화된 보호 보고서입니다. 열람하려면 비밀번호가 필요합니다.'
        };
      }
      fs.writeFileSync(destSummaries, JSON.stringify(maskedSummaries, null, 2), 'utf8');
      console.log(`\n  [OK] Generated sanitized summaries.json with updated hashes.`);
    } catch (e) {
      console.warn(`  [WARN] Failed to process summaries.json:`, e.message);
    }
  }

  console.log(`\n🎉 Successfully encrypted ${encryptedCount} reports into ${DEST_DIR}!`);
}

run();
