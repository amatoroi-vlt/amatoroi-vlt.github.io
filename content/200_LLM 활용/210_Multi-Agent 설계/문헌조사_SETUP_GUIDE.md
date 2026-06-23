---
tags:
  - gemini-cli
  - multi-agents
  - skills
  - research
  - automation
  - 문헌조사
date: 2026-04-14
---

# ResearchAssist 환경 구축 절차서

> 이 문서는 `ResearchAssist` 프로젝트의 환경을 새 머신 또는 새 디렉토리에서 재구성하기 위한 단계별 절차서입니다.

---

## 개요

`ResearchAssist`는 Gemini CLI 멀티에이전트를 이용한 **학술 논문 자동 수집·검증·보고서 생성 파이프라인**입니다.

```
사용자 지시
    │
    ▼
[Conductor (GEMINI.md)]  ← 파이프라인 총괄 지휘자
    │
    ├─► @data_researcher   → 학술 API 호출 → CANDIDATE_LIST.md 생성
    ├─► @fact_checker      → HTTP 검증 → 실존 논문 확인 + PDF 수집
    └─► @report_synthesizer → 검증 데이터 기반 최종 보고서 생성
```

**핵심 원칙:** LLM은 논문 메타데이터(제목·저자·DOI·URL)를 직접 생성하지 않는다. 모든 서지정보는 외부 학술 API 응답에서만 추출한다.

---

## 사전 요구사항

| 항목         | 버전     | 확인 방법              |
| ---------- | ------ | ------------------ |
| Python     | 3.8 이상 | `python --version` |
| curl       | 시스템 기본 | `curl --version`   |
| Gemini CLI | 최신     | `gemini --version` |
* [필수] amatoroi's mac에서는 python3 대신 python을 활용한다
---

## STEP 1: 디렉토리 생성

```bash
mkdir -p ResearchAssist
cd ResearchAssist
```

---

## STEP 2: 디렉토리 구조 생성

```bash
mkdir -p .gemini/agents
mkdir -p .claude
```

완성 후 구조:

```
ResearchAssist/
├── .claude/
│   └── settings.local.json       # Claude Code 권한 설정
├── .gemini/
│   ├── config.yaml               # Gemini 도구 권한 설정
│   └── agents/
│       ├── data_researcher.md    # 서브에이전트: 논문 수집
│       ├── fact_checker_v3.md    # 서브에이전트: 논문 검증
│       └── report_synthesizer.md # 서브에이전트: 보고서 작성
├── GEMINI.md                     # 메인 에이전트 (Conductor) 지침
├── PROJECT_RULES.md              # 파이프라인 공통 규칙
├── CURRENT_JOB.md                # 현재 작업 상태 (런타임 파일)
└── generate_candidate_list.py    # CANDIDATE_LIST 생성 보조 스크립트
```

---

## STEP 3: Gemini 도구 권한 설정

`.gemini/config.yaml` 파일을 생성한다.

```yaml
tools:
  bash:
    enabled: true
    allow_all: true  # curl, jq, python3, mkdir 등 사용 필수
  read_file:
    enabled: true
  write_file:
    enabled: true
  google_search:
    enabled: true  # 검색 쿼리 보조용 (메타데이터 생성 금지)
```

---

## STEP 4: Claude Code 권한 설정

`.claude/settings.local.json` 파일을 생성한다.

```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:github.com)"
    ]
  }
}
```

---

## STEP 5: 공통 규칙 파일 생성

`PROJECT_RULES.md` 파일을 생성한다. 모든 서브에이전트가 이 파일을 읽고 규칙을 따른다.

```markdown
# 과학기술 연구 파이프라인 글로벌 지침

## 0. 핵심 원칙 (절대 위반 금지)

**LLM은 논문 메타데이터(제목, 저자, DOI, URL)를 절대 직접 생성하지 않는다.**
모든 서지 정보는 반드시 외부 학술 API 응답에서 추출한다.
API 응답 없이 논문 정보를 기록하는 것은 환각으로 간주하고 즉시 폐기한다.

## 1. 경로 및 변수 관리

- 모든 서브에이전트는 작업 시작 전 반드시 루트의 `./CURRENT_JOB.md`를 읽어
  `BASE_PATH`와 `RESEARCH_NAME`을 확정한다.
- 모든 파일 작업은 `${BASE_PATH}`를 접두어로 사용하여 경로 충돌을 방지한다.

## 2. 데이터 수집 전략 (API 우선)

우선순위 순서로 시도하며, 성공 시 하위 우선순위는 건너뛴다.

| 우선순위 | 소스 | API 엔드포인트 | 대상 분야 |
|----------|------|----------------|-----------|
| 1 | arXiv | https://export.arxiv.org/api/query | 물리/CS/수학 |
| 2 | Semantic Scholar | https://api.semanticscholar.org/graph/v1/paper/search | 전 분야 |
| 3 | OpenAlex | https://api.openalex.org/works | 전 분야 |
| 4 | PubMed | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi | 의학/생명과학 |

Google Search는 검색 쿼리 아이디어 생성 보조에만 사용한다.
Google Search 결과에서 논문 메타데이터를 직접 추출하지 않는다.

## 3. 증거 확보 전략

- **우선순위 1 (PDF 물리 확보):** `curl -L`로 오픈액세스 PDF를 `${BASE_PATH}/sources/`에 저장.
- **우선순위 2 (URL 기록):** 다운로드 불가 시 검증된 URL/DOI를 `${BASE_PATH}/sources/[파일명].url.txt`에 기록.

## 4. CANDIDATE_LIST.md 형식

| INDEX | TITLE | AUTHORS | YEAR | SOURCE | ARXIV_ID | DOI | PDF_URL | STATUS |
|-------|-------|---------|------|--------|----------|-----|---------|--------|

STATUS 값: `PENDING` / `VERIFIED` / `FAILED_NOTFOUND` / `FAILED_IRRELEVANT`

## 5. 자동 종료 조건

- `FAIL_DOWNLOAD_STREAK`이 **5**에 도달 시 → STATUS: TERMINATED_DOWNLOAD
- `FAIL_QUALITY_STREAK`이 **3**에 도달 시 → STATUS: TERMINATED_QUALITY
- 두 조건 모두 미달 시 전체 CANDIDATE 처리 완료 후 → STATUS: COMPLETED

## 6. 동시성 제어

CURRENT_JOB.md의 LOCK 필드를 확인하여 다른 에이전트가 쓰고 있으면 대기한다.
파일 쓰기 시작 전 LOCK을 자신의 이름으로 설정하고, 완료 후 NONE으로 해제한다.
```

---

## STEP 6: 메인 에이전트(Conductor) 지침 생성

`GEMINI.md` 파일을 생성한다. Gemini CLI는 이 파일을 자동으로 읽어 메인 에이전트 지침으로 사용한다.

```markdown
# 연구 자동화 파이프라인 - 메인 에이전트 (Conductor)

너는 연구 파이프라인 총괄 지휘자다.
`./PROJECT_RULES.md`를 읽어 모든 규칙을 숙지하고 아래 절차를 따른다.

---

## 파이프라인 시작 절차

사용자가 "연구 명칭은 'XXX'야. 작업을 시작해줘." 라고 하면:

### 초기화

1. `RESEARCH_NAME`을 사용자 입력에서 추출한다.
2. 디렉토리를 생성한다:
   ```bash
   mkdir -p ${RESEARCH_NAME}/sources ${RESEARCH_NAME}/workspace
   ```
3. `CURRENT_JOB.md`를 해당 연구에 맞게 초기화한다.

### 파이프라인 실행 순서

```
[1단계] @data_researcher 호출
        → CANDIDATE_LIST.md 생성 완료 대기
        → CANDIDATE_COUNT 확인

[2단계] 루프 시작 (CURRENT_INDEX < CANDIDATE_COUNT 동안 반복)
        a. @fact_checker 호출
        b. fact_checker 보고 수신
        c. CURRENT_JOB.md 읽어 STATUS 확인
           - TERMINATED_* → 루프 중단, [3단계]로 이동
           - RUNNING → 루프 계속

[3단계] @report_synthesizer 호출
        → final_report.md 생성 완료 대기

[4단계] 사용자에게 완료 보고
        - 보고서 경로
        - 검증된 논문 수
        - 파이프라인 종료 사유 (정상완료 / 조기종료)
```

---

## 주의사항

- 서브에이전트가 논문 메타데이터를 직접 생성하려는 시도를 발견하면 즉시 중단시킨다.
- `CURRENT_JOB.md`의 STATUS가 TERMINATED_*이면 report_synthesizer를 즉시 호출한다.
- 각 서브에이전트 호출 후 반드시 완료 보고를 받고 다음 단계를 진행한다.
```

---

## STEP 7: 서브에이전트 파일 생성

### 7-A: data_researcher 에이전트

`.gemini/agents/data_researcher.md` 파일을 생성한다.

파일 내용은 기존 `.gemini/agents/data_researcher.md`를 그대로 복사한다. 핵심 구조:

```
---
name: data_researcher
description: 학술 API를 직접 호출하여 실재하는 논문의 메타데이터를 수집하고 CANDIDATE_LIST.md를 생성합니다.
parameters:
  type: object
  properties:
    query:
      type: string
    BASE_PATH:
      type: string
  required: [query, BASE_PATH]
tools:
  - run_shell_command
  - read_file
  - write_file
  - google_web_search
---
[에이전트 본문: arXiv → Semantic Scholar → OpenAlex → PubMed 순서로 API 호출 및 파싱]
```

호출하는 API 엔드포인트:
- `https://export.arxiv.org/api/query`
- `https://api.semanticscholar.org/graph/v1/paper/search`
- `https://api.openalex.org/works`
- `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`

### 7-B: fact_checker 에이전트

`.gemini/agents/fact_checker_v3.md` 파일을 생성한다.

```
---
name: fact_checker
description: CANDIDATE_LIST.md의 각 항목에 대해 DOI/URL HTTP 요청으로 실존 여부를 기계적으로 검증합니다.
parameters:
  type: object
  properties:
    BASE_PATH:
      type: string
  required: [BASE_PATH]
tools:
  - run_shell_command
  - read_file
  - write_file
---
[에이전트 본문: PENDING 항목을 1건씩 HTTP(curl) 검증 → VERIFIED/FAILED 판정 → PDF 다운로드 또는 URL 기록]
```

### 7-C: report_synthesizer 에이전트

`.gemini/agents/report_synthesizer.md` 파일을 생성한다.

```
---
name: report_synthesizer
description: fact_checker가 검증한 실재 논문 데이터만을 바탕으로 연구 동향 보고서를 작성합니다.
parameters:
  type: object
  properties:
    BASE_PATH:
      type: string
  required: [BASE_PATH]
tools:
  - read_file
  - write_file
  - google_web_search
---
[에이전트 본문: 02_verified_data.md 로드 → 연도별/주제별 분석 → final_report.md 작성]
```

---

## STEP 8: CURRENT_JOB.md 초기 템플릿 확인

새 연구를 시작할 때마다 파이프라인이 아래 형식으로 `CURRENT_JOB.md`를 초기화한다. 수동으로 만들 경우 아래 형식을 사용한다.

```markdown
# 현재 작업 상태 (RESEARCH_NAME)

- RESEARCH_NAME: [연구 이름]
- BASE_PATH: ./[연구 이름]
- CANDIDATE_COUNT: 0
- CURRENT_INDEX: 0
- VERIFIED_COUNT: 0
- FAIL_DOWNLOAD_STREAK: 0
- FAIL_QUALITY_STREAK: 0
- LOCK: NONE
- STATUS: INITIALIZED

## 핵심 요구사항
- [연구의 핵심 목표 및 특이사항 기술]
```

---

## STEP 9: 보조 Python 스크립트 생성 (선택)

`generate_candidate_list.py`는 `/tmp/` 의 파싱 결과 파일을 합쳐 `CANDIDATE_LIST.md`를 직접 생성하는 보조 스크립트다. 에이전트 내부에 동일 코드가 포함되어 있으므로, 수동 디버깅 시 사용한다.

```python
# generate_candidate_list.py
lines = []
seen_keys = set()

for fname in ['/tmp/arxiv_parsed.txt', '/tmp/s2_parsed.txt', '/tmp/oa_parsed.txt']:
    try:
        with open(fname) as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('PARSE_ERROR'):
                    continue
                parts = line.split('|')
                if len(parts) < 7:
                    continue
                source, title, authors, year, arxiv_id, doi, pdf_url = parts[:7]
                key = doi if doi != 'N/A' else arxiv_id
                if key == 'N/A' or key in seen_keys:
                    continue
                seen_keys.add(key)
                lines.append((source, title, authors, year, arxiv_id, doi, pdf_url))
    except FileNotFoundError:
        pass

header = "| INDEX | TITLE | AUTHORS | YEAR | SOURCE | ARXIV_ID | DOI | PDF_URL | STATUS |\n"
header += "|-------|-------|---------|------|--------|----------|-----|---------|--------|\n"

rows = []
for i, (source, title, authors, year, arxiv_id, doi, pdf_url) in enumerate(lines, 1):
    idx = f"{i:03d}"
    short_title = (title[:80] + ('...' if len(title) > 80 else '')) if title else "No Title"
    rows.append(f"| {idx} | {short_title} | {authors} | {year} | {source} | {arxiv_id} | {doi} | {pdf_url} | PENDING |")

print(f"총 수집 건수: {len(rows)}")
# BASE_PATH를 실제 연구 디렉토리로 변경할 것
with open('[RESEARCH_NAME]/CANDIDATE_LIST.md', 'w') as f:
    f.write(header)
    f.write('\n'.join(rows))
```

---

## STEP 10: 환경 검증

모든 파일이 올바르게 생성되었는지 확인한다.

```bash
# 필수 파일 존재 여부 확인
ls -la .gemini/config.yaml
ls -la .gemini/agents/data_researcher.md
ls -la .gemini/agents/fact_checker_v3.md
ls -la .gemini/agents/report_synthesizer.md
ls -la GEMINI.md
ls -la PROJECT_RULES.md

# Gemini CLI 정상 동작 확인
gemini --version
```

---

## STEP 11: 파이프라인 실행

환경 구축 완료 후 Gemini CLI에서 아래와 같이 실행한다.

```bash
cd ResearchAssist
gemini
```

Gemini 프롬프트에서:

```
연구 명칭은 'My_Research_Topic'야. 작업을 시작해줘.
```

파이프라인이 자동으로 아래 순서를 실행한다:

```
1. My_Research_Topic/sources/ 및 workspace/ 디렉토리 생성
2. CURRENT_JOB.md 초기화
3. @data_researcher → CANDIDATE_LIST.md 생성
4. @fact_checker 루프 → 논문별 HTTP 검증 + PDF 수집
5. @report_synthesizer → final_report.md 생성
6. 완료 보고
```

---

## 연구 결과물 디렉토리 구조

파이프라인 완료 후 각 연구별로 아래 구조가 생성된다.

```
[RESEARCH_NAME]/
├── CANDIDATE_LIST.md        # 수집된 논문 목록 (STATUS 포함)
├── final_report.md          # 최종 연구 동향 보고서
├── sources/
│   ├── 001.pdf              # 다운로드된 PDF (오픈액세스)
│   ├── 002.url.txt          # 다운로드 불가 논문의 DOI/URL 기록
│   └── ...
└── workspace/
    └── 02_verified_data.md  # 검증 완료 논문 데이터 누적
```

---

## 파이프라인 상태 코드 참조

| STATUS 값 | 의미 |
|-----------|------|
| `INITIALIZED` | 파이프라인 시작 전 |
| `RUNNING` | 검증 루프 진행 중 |
| `COMPLETED` | 전체 CANDIDATE 처리 완료 |
| `TERMINATED_DOWNLOAD` | FAIL_DOWNLOAD_STREAK ≥ 5 (다운로드 연속 실패) |
| `TERMINATED_QUALITY` | FAIL_QUALITY_STREAK ≥ 3 (품질 연속 실패) |

| CANDIDATE STATUS | 의미 |
|-----------------|------|
| `PENDING` | 검증 대기 |
| `VERIFIED` | 실존 확인 + 관련성 있음 |
| `FAILED_NOTFOUND` | HTTP 404 / 실존 불가 |
| `FAILED_IRRELEVANT` | 실존하나 연구 주제와 무관 |

---

## 트러블슈팅

### API 호출 실패 시

```bash
# curl 타임아웃 테스트
curl -s --max-time 30 "https://api.semanticscholar.org/graph/v1/paper/search?query=test&limit=1"

# arXiv API 테스트
curl -s "https://export.arxiv.org/api/query?search_query=all:test&max_results=1"
```

### LOCK 해제가 필요한 경우 (에이전트 비정상 종료 시)

`CURRENT_JOB.md`를 직접 열어 `LOCK: NONE`으로 수정한다.

### CANDIDATE_LIST.md 수동 재생성

```bash
# /tmp/ 에 파싱 파일이 남아 있는 경우
python3 generate_candidate_list.py
```
