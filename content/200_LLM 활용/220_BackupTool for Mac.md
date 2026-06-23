---
tags:
  - claude_code
  - backup
date: 2026-06-09
---

# ResticMenuBar — macOS 자동 백업 도구

restic을 백엔드로 사용하는 macOS 메뉴바 백업 앱.
12시간마다 자동 백업하고, 메뉴바에서 모든 기능을 마우스로 조작합니다.

---

## 구성

```
BackupTool_for_Mac/
  make-app.sh              전체 설치 스크립트
  scripts/
    backup.sh              백업 실행 (12시간마다 앱이 호출)
    restic-prune.sh        공간 회수 + 무결성 검사 (주 1회 launchd)
    restic-cmd.sh          스냅샷 조회·복원 래퍼
  launchd/
    com.user.resticprune.plist  주 1회 prune 스케줄러
  ResticMenuBar/           Swift 앱 소스 (SPM)
```

설치 후 운영 위치:

| 역할     | 경로                                 |
| ------ | ---------------------------------- |
| 메뉴바 앱  | `~/Applications/ResticMenuBar.app` |
| 셸 스크립트 | `~/restic-backup/`                 |
| 설정 파일  | `~/.config/restic/config.json`     |
| 상태 파일  | `~/.config/restic/status.json`     |
| 로그     | `~/Library/Logs/resticbackup/`     |

---

## 사전 준비

### 1. 의존성 설치
```sh
brew install restic jq
```

### 2. 저장소 비밀번호 등록
```sh
security add-generic-password -a restic -s restic-backup -w '강력한-비밀번호'
```
> ⚠️ 이 비밀번호를 잃으면 백업을 복구할 수 없습니다. 1Password 등에 반드시 보관하세요.

---

## 설치

```sh
cd ~/Documents/dev/BackupTool_for_Mac
./make-app.sh
```

스크립트가 자동으로 처리합니다:
- Swift 앱 빌드 → `~/Applications/ResticMenuBar.app`
- 셸 스크립트 → `~/restic-backup/`
- prune 스케줄러 launchd 등록 (매주 일요일 03:00)

### Full Disk Access 부여 (필수)

앱이 백업 대상 폴더에 접근하려면 한 번 권한을 부여해야 합니다:

**System Settings → Privacy & Security → Full Disk Access → `+` → ResticMenuBar.app 추가**

### 로그인 시 자동 시작

메뉴바 아이콘 클릭 → **설정 → 로그인 시 자동 시작**

---

## 초기 설정

### 백업 소스 추가
메뉴바 아이콘 클릭 → **백업 소스 → + 소스 추가** → Finder에서 폴더 선택

### 저장소 설정
메뉴바 아이콘 클릭 → **저장소 → 저장소 변경** → Finder에서 저장소 폴더 선택

설정은 `~/.config/restic/config.json`에 저장됩니다:
```json
{
  "sources": ["/Users/username/Documents/Obsidian Vault"],
  "repository": "/Volumes/WD My Book/MacOS_BKUP",
  "backup_interval_hours": 12
}
```

> 저장소는 첫 백업 시 자동으로 초기화(`restic init`)됩니다.

---

## 메뉴바 기능

| 항목 | 설명 |
|------|------|
| 상태 / 마지막 실행 | 현재 백업 상태와 시각 |
| ▶ 지금 백업 실행 | 즉시 백업 |
| 🗂 스냅샷 목록 | 최근 5개 스냅샷, 클릭 시 복원 |
| 백업 소스 | 소스 목록 확인, 추가, 제거 |
| 저장소 | 현재 경로 확인, 변경 |
| 유지관리 → 🧹 Prune | 수동 공간 회수 |
| 유지관리 → 🔍 무결성 검사 | 저장소 상태 확인 |
| 로그 → 로그 폴더 열기 | `~/Library/Logs/resticbackup/` |
| 로그 → 최근 백업 로그 | 가장 최근 로그 파일 열기 |
| 설정 → 로그인 시 자동 시작 | 켜기/끄기 토글 |

---

## 상태 아이콘

| 아이콘 | 의미 |
|--------|------|
| 🟢 백업 | 마지막 백업 성공 |
| 🔵 백업 중… | 백업 진행 중 |
| 🔴 백업 | 오류 발생 (macOS 알림 전송) |
| ⚪ 백업 | 디스크 미연결 / 대기 |

---

## 보관 정책

| 단위 | 보관 |
|------|------|
| 시간별 | 24개 (최근 24시간) |
| 일별 | 14개 (최근 2주) |
| 주별 | 8개 (최근 2개월) |
| 월별 | 12개 (최근 1년) |

수동으로 생성한 스냅샷(`--tag auto` 없는 것)은 자동 정리 대상 제외.
`prune`은 매주 일요일 새벽 3시 launchd가 자동 실행합니다.

---

## 복구

### 메뉴에서 복구
메뉴바 → **🗂 스냅샷 목록** → 원하는 시점 클릭 → Finder에 복구 폴더 자동 열림

복구 위치: `~/restore-<snapshot-id>/`

> 복구된 파일은 원본 절대경로 구조를 유지합니다.
> 예: `~/restore-1e06e65e/Users/username/Documents/Obsidian Vault/...`

### 터미널에서 복구
```sh
export RESTIC_REPOSITORY="/Volumes/WD My Book/MacOS_BKUP"
export RESTIC_PASSWORD_COMMAND="security find-generic-password -a restic -s restic-backup -w"

restic snapshots                                    # 스냅샷 목록
restic restore <snapshot-id> --target ~/restore     # 특정 시점 복원
restic mount ~/mnt                                  # Finder로 탐색
```

---

## 로그

```
~/Library/Logs/resticbackup/
  backup-YYYYMMDD-HHMMSS.log   백업 실행 로그 (30일 후 자동 삭제)
  prune-YYYYMMDD.log           주간 prune 로그
  check-YYYYMMDD.log           무결성 검사 로그
```

---

## 업데이트 (재빌드)

소스 수정 후:
```sh
cd ~/Documents/dev/BackupTool_for_Mac
./make-app.sh
open ~/Applications/ResticMenuBar.app
```
