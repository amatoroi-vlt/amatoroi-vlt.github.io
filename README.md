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
│   │   ├── paper_review.html      # ⭐ 논문 아카이브 Master-Detail 대시보드 (심층 요약 전용)
│   │   └── live_report.html       # 라이브 트레이딩 현황 리포트
│   ├── Research/                  # 방사선 계측, 불확도 평가, 연구 리포트
│   └── Invest/                    # 기업 재무 분석(Sankey), 트레이딩 전략 리포트
├── scripts/
│   ├── publish_financial_report.py# 📊 재무 분석 리포트 발행 스크립트
│   └── publish_live_report.py     # 📡 라이브 리포트 동기화 데몬 스크립트
└── .github/
    └── scripts/
        └── generate_manifest.py   # manifest.json 자동 생성기
```

---

## 📑 1. 논문 아카이브 대시보드 (Overwatch) 운영 가이드

외부 논문 저장소(`/Users/jeongsookang/Documents/dev/ResearchHelper/papers/INDEX.html`)에서 생성된 단일 HTML 대시보드를 블로그로 반영하는 무수정(Zero-touch) 동기화 원칙입니다.

### 🤖 기본 운영 원칙
1. `ResearchHelper/papers/INDEX.html` 파일을 이 저장소의 `reports/Overwatch/paper_review.html`로 복사(덮어쓰기)합니다.
   - HTML 내부에 `const SHOW_SOURCE_LINKS = window.location.protocol === "file:";` 분기가 내장되어 있어, 로컬(`file://`)에서는 원문/전사본 버튼이 활성화되고 퍼블릭 블로그(`https://`) 배포 시에는 별도 수정 없이 자동으로 심층 요약 전용 모드로 동작합니다.
2. 대화창에 `"논문 아카이브 파일 업데이트했으니 확인해서 커밋·푸쉬해줘"`라고 요청하면, 에이전트가 해시(`reports/summaries.json`) 및 `manifest.json`(`.github/scripts/generate_manifest.py`)을 자동 갱신하여 커밋·푸시합니다.

### ⚡ 수동 갱신 명령어 (참고용)
```bash
/opt/homebrew/bin/uv run --with plotly --with kaleido --with resvg-py python3 .github/scripts/generate_manifest.py
```

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
