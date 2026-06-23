---
date: 2026-04-07
tags:
  - 깃헙
  - github
  - gemini-cli
---

# GitHub CLI (gh) 사용자 계정 전용 설치 가이드 (macOS)

본 문서는 시스템 관리자 권한(`sudo`) 없이, macOS의 사용자 계정 폴더(`~/Applications`) 내에 GitHub CLI(`gh`)를 독립적으로 설치하고 관리하는 방법을 기록합니다. 옵시디언(Obsidian) 등 개인 지식 베이스에 보관하기 좋습니다.

---

## 1. 개요 (Overview)
*   **설치 경로**: `~/Applications/gh-cli`
*   **방식**: 전컴파일된(Pre-compiled) 바이너리 압축 해제 및 경로 직접 등록
*   **장점**: 
    - 시스템 폴더(`/usr/local/bin` 등)를 건드리지 않아 보안상 안전함.
    - macOS 업데이트 시에도 설정이 유지됨.
    - 삭제 시 해당 폴더만 지우면 깔끔하게 제거됨.

---

## 2. 단계별 설치 절차 (Step-by-Step)

### [Step 1] 설치 폴더 구조 생성
터미널을 열고 아래 명령어를 입력하여 계정 전용 설치 경로를 만듭니다.
```bash
mkdir -p ~/Applications/gh-cli/bin
mkdir -p ~/Applications/gh-cli/share/man/man1
```

### [Step 2] 실행 파일 및 매뉴얼 복사
다운로드하여 압축을 해제한 `gh` 폴더(예: `gh_2.xx.x_macOS_amd64`) 내부에서 다음 명령을 실행합니다.
```bash
# 1. 실행 파일(Binary) 복사
cp bin/gh ~/Applications/gh-cli/bin/

# 2. 매뉴얼(Man) 파일 복사
cp share/man/man1/*.1 ~/Applications/gh-cli/share/man/man1/
```

### [Step 3] 환경 변수 등록 (`~/.zshrc`)
맥 터미널이 `gh` 명령어와 매뉴얼의 위치를 자동으로 인식하도록 설정 파일에 경로를 추가합니다.
```bash
# 실행 파일 경로(PATH) 추가
echo 'export PATH="$HOME/Applications/gh-cli/bin:$PATH"' >> ~/.zshrc

# 매뉴얼 경로(MANPATH) 추가
echo 'export MANPATH="$HOME/Applications/gh-cli/share/man:$MANPATH"' >> ~/.zshrc

# 설정 즉시 적용
source ~/.zshrc
```

---

## 3. 초기 설정 및 인증 (Configuration)

### [Step 4] macOS 보안 경고 해결 (최초 1회)
최초로 `gh --version` 등을 실행했을 때 "확인되지 않은 개발자" 경고 창이 뜬다면:
1.  경고 창에서 **[취소]**를 누릅니다.
2.  `시스템 설정 > 개인정보 보호 및 보안`으로 이동합니다.
3.  맨 아래쪽의 **[확인 없이 열기]** 버튼을 클릭하여 실행을 허용합니다.

### [Step 5] 브라우저 기반 Google 로그인 인증
GitHub CLI를 사용하여 Git 작업을 수행하기 위해 인증을 진행합니다.
```bash
gh auth login
```
1.  **What account...?** → `GitHub.com` 선택
2.  **What is your preferred protocol...?** → `HTTPS` 선택 (추천)
3.  **Authenticate Git with your GitHub credentials?** → `Yes` 선택
4.  **How would you like to authenticate...?** → **`Login with a web browser`** 선택
5.  터미널에 표시된 **8자리 코드**를 복사한 후, 자동으로 열리는 브라우저 창에 입력합니다.
6.  GitHub 계정(또는 Google 로그인)으로 인증을 완료합니다.

---

## 4. 설치 확인 및 사용 (Verification)
설치가 완료되면 다음 명령어로 정상 작동 여부를 확인합니다.
*   **버전 확인**: `gh --version`
*   **인증 상태**: `gh auth status`
*   **매뉴얼 보기**: `man gh` (사용자 계정 매뉴얼이 정상 로드되는지 확인)
*   **푸시 테스트**: `git push -u origin main` (인증 정보 자동 사용)
