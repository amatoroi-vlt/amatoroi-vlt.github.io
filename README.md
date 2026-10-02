# Pensieve (amatoroi-vlt.github.io)

> **개인 연구, 방사선 계측, 퀀트/투자 전략 및 기업 분석을 위한 정적 지식 저장소 & 인터랙티브 대시보드 블로그**

---

## 📂 프로젝트 구조

```
amatoroi-vlt.github.io/
├── index.html                     # 블로그 메인 뷰어 (SPA / 사이드바 / 카드 그리드)
├── manifest.json                  # 전체 리포트 색인 (자동 생성)
├── README.md                      # 프로젝트 가이드 & 운영 매뉴얼
├── reports/
│   ├── summaries.json             # 각 리포트의 SHA1 해시 및 한글 요약문 메타데이터
│   ├── Overwatch/                 # 모니터링, 통합 대시보드 리포트
│   │   ├── paper_repository.html  # ⭐ 논문 저장소 Master-Detail 대시보드
│   │   ├── live_report.html       # 라이브 트레이딩 현황 리포트
│   │   └── assets/                # 논문 첨부 이미지 및 차트 리소스
│   ├── Research/                  # 방사선 계측, 불확도 평가, 연구 리포트
│   └── Invest/                    # 기업 재무 분석(Sankey), 트레이딩 전략 리포트
├── scripts/
│   ├── build_paper_repository.py  # 🚀 논문 아카이브 대시보드 빌더 / 동기화 스크립트
│   ├── publish_financial_report.py# 📊 재무 분석 리포트 발행 스크립트
│   └── publish_live_report.py     # 📡 라이브 리포트 동기화 데몬 스크립트
└── .github/
    └── scripts/
        └── generate_manifest.py   # manifest.json 자동 생성기
```

---

## 📑 1. 논문 저장소 대시보드 (Overwatch) 운영 가이드

외부 논문 저장소(`ResearchHelper/papers`)에 새로운 논문이 추가되거나 요약문/전사본이 업데이트되었을 때의 동기화 원칙입니다.

### 🤖 기본 운영 원칙 (Agent-Driven Workflow)
- **사용자가 말로 지시하면 에이전트(AI)가 실행하는 것이 기본(디폴트)입니다.**
- 대화창에 `"새 논문 추가되었으니 대시보드 업데이트해줘"` 또는 `"논문 저장소 동기화하고 배포해줘"`라고 말씀해 주시면, 에이전트가 빌드 스크립트 실행, 에셋 복사, 매니페스트 갱신 및 Git 커밋/푸시까지 일괄 자동으로 완결합니다.

### 📍 원천 논문 저장소 위치
- 경로: `/Users/jeongsookang/Documents/dev/ResearchHelper/papers/`
- 구조:
  - `INDEX.md`: 마스터 인벤토리 및 한글 핵심 요약
  - `index.json`: 논문 메타데이터 목록 (ID, 제목, 저자, 연도 등)
  - `summaries/`: Tier 2 심층 구조화 요약 마크다운 (`<ID>.md`)
  - `transcribed/`: 원문 전사본 마크다운 및 이미지 (`images/<ID>/*.png`)
  - `raw/`: 원본 PDF 파일 (`<ID>.pdf`)

### ⚡ 수동 실행 시 명령어 (참고용)
터미널에서 직접 실행할 경우 아래 명령어를 사용합니다:

```bash
# 기본 경로(/Users/jeongsookang/Documents/dev/ResearchHelper/papers)에서 빌드
/opt/homebrew/bin/uv run python3 scripts/build_paper_repository.py

# 또는 다른 경로를 지정하여 빌드할 경우:
/opt/homebrew/bin/uv run python3 scripts/build_paper_repository.py --source /경로/to/papers
```

### 🛠️ 빌드 스크립트(`scripts/build_paper_repository.py`) 자동화 내역
1. `index.json` 및 `INDEX.md`로부터 논문 메타데이터, 게재 학술지, 저자, 핵심 요약 추출
2. `summaries/*.md`와 `transcribed/*.md` 수집 및 KaTeX 수식/마크다운 렌더링 준비
3. 논문 첨부 이미지를 `reports/Overwatch/assets/papers/<paper_id>/`로 자동 복사 및 상대 경로 치환
4. 실시간 검색, 연도/주제 필터, 심층요약/원문전사본 탭 뷰어가 내장된 `reports/Overwatch/paper_repository.html` 생성
5. `reports/summaries.json`에 대시보드 요약 및 SHA1 해시 자동 등록
6. `manifest.json`을 자동 재생성하여 블로그 메인 화면의 `Overwatch` 섹션에 즉시 노출

---

## 📊 2. 재무 분석 (Invest) 리포트 발행 가이드

트레이딩/재무 분석 프로젝트(`TradingStrategy`) 등에서 생성된 마크다운 리포트와 Sankey 차트 에셋을 블로그로 배포할 때 사용합니다:

```bash
/opt/homebrew/bin/uv run python3 scripts/publish_financial_report.py \
  --ticker <TICKER> \
  --report tmp/output/<TICKER>/report.md \
  --output reports/Invest/<ticker>_financial_breakdown.html
```

---

## 🚀 3. Git 커밋 및 배포

```bash
git add reports/ manifest.json README.md scripts/
git commit -m "feat(overwatch): update paper repository dashboard and manifest"
git push origin main
```

---

## 💡 기술 스택 및 디자인 원칙

- **SPA 아키텍처**: 순수 바닐라 JS 기반의 정적 웹 앱으로, 외부 백엔드 서버 없이 동작
- **타이포그래피**: `Noto Serif KR` (한글 세리프), `Inter` (영문 산세리프), `IBM Plex Mono` (코드/데이터)
- **수식 렌더링**: KaTeX CDN (`$$...$$`, `$..$`, `\[...\]`, `\(...\)`)
- **마크다운 렌더링**: Marked.js (GFM 표, 취소선, 줄바꿈 지원)
