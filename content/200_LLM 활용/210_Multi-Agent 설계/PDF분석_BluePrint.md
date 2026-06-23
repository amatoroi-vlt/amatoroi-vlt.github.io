# PdfAnalizer 재현 가이드 (Codex CLI / Gemini CLI)

> 이 문서는 Claude Code 기반으로 구축된 **PdfAnalizer** 프로젝트를 **OpenAI Codex CLI** 또는 **Google Gemini CLI** 환경에서 동일한 기능으로 재현하기 위한 단계별 작업 지침서이다. 빈 디렉토리에서 시작해 이 문서만 따라가면 완전히 동작하는 복제본을 얻을 수 있도록 작성되었다.

---

## 목차

- [Part 0. 개요 및 사전 준비](#part-0-개요-및-사전-준비)
- [Part 1. 공통 자산 생성 (양쪽 경로 공통)](#part-1-공통-자산-생성-양쪽-경로-공통)
- [Part 2-A. Codex CLI 경로 🟦](#part-2-a-codex-cli-경로-)
- [Part 2-B. Gemini CLI 경로 🟥](#part-2-b-gemini-cli-경로-)
- [Part 3. 원본 대비 기능 매핑](#part-3-원본-대비-기능-매핑)
- [Part 4. 트러블슈팅 체크리스트](#part-4-트러블슈팅-체크리스트)
- [Part 5. 참조 자료 링크](#part-5-참조-자료-링크)

---

## Part 0. 개요 및 사전 준비

### 0.1 PdfAnalizer가 하는 일

한 줄 요약: **환각 없는(hallucination-free) 연구 논문 분석·종합 시스템**.

핵심 아키텍처는 **2-게이트 검증**이다.

1. **생성 (Generation)** — `paper-reviewer`가 PDF를 읽고 모든 사실 주장마다 `[[<pdf>#page=N]]` 형식의 페이지 앵커 위키링크를 붙인 Obsidian 노트 생성
2. **검증 (Verification)** — `citation-verifier`가 PDF를 재독하여 각 위키링크가 해당 페이지 내용으로 실제 뒷받침되는지 PASS/FAIL/UNCLEAR 판정

그리고 2개 이상 논문이 분석된 후 `research-synthesizer`가 교차 합성 문서를 생성한다.

### 0.2 생성될 최종 디렉토리 구조 (양쪽 공통)

```
PdfAnalizer-<target>/
├── pdfs/                    # 입력 PDF
├── notes/                   # paper-reviewer 출력
├── verifications/           # citation-verifier 출력
├── synthesis/               # research-synthesizer 출력
├── templates/
│   ├── paper_note.md
│   └── synthesis.md
├── scripts/                 # (Codex 경로에만) PDF 전처리
│   └── pdf_to_text.py
├── .gitignore
├── AGENTS.md  | GEMINI.md   # 각 CLI의 컨텍스트 파일
├── .codex/                  # Codex 경로
│   ├── config.toml
│   ├── agents/*.toml (3개)
│   └── skills/
│       ├── pdf-analyze/SKILL.md
│       └── pdf-synthesize/SKILL.md
└── .gemini/                 # Gemini 경로
    ├── settings.json
    ├── agents/*.md (3개)
    └── commands/*.toml (2개)
```

### 0.3 공통 선행 조건

| 항목 | 용도 | 설치 |
|---|---|---|
| `python` ≥ 3.10 | (Codex) PDF 전처리 | macOS: `brew install python` / Linux: 패키지 관리자 |
| `pip` | Python 패키지 설치 | Python에 포함 |
| `node` ≥ 20 + `npm` | Codex/Gemini CLI 설치 | https://nodejs.org |
| Obsidian (선택) | vault 시각화 | https://obsidian.md |
| Git (선택) | 버전 관리 | OS 기본 |

> **규칙**: 본 가이드의 모든 Python 명령은 `python` (NOT `python3`) 으로 통일한다.

### 0.4 환경 선택 결정 트리

```
Q1. PDF를 CLI가 네이티브로 읽어주길 원하는가?
 ├── YES → Gemini CLI 경로 (Part 2-B) — @{file.pdf} 멀티모달 주입
 └── NO/상관없음 ↓

Q2. 서브에이전트 기능이 experimental 딱지 없는 안정 버전이어야 하는가?
 ├── YES → Codex CLI 경로 (Part 2-A) — 정식 subagents 지원
 └── NO  → Gemini CLI 경로 (Part 2-B) — experimental이지만 기본 활성
```

둘 다 가능하다면 **Gemini CLI 경로가 원본 Claude Code에 더 가까운 재현도**를 보여 준다(PDF 네이티브 + 서브에이전트 전부 내장).

---

## Part 1. 공통 자산 생성 (양쪽 경로 공통)

이 Part는 **Codex든 Gemini든 동일하게 먼저 수행**해야 한다.

### 1.1 프로젝트 디렉토리 생성

```bash
mkdir -p PdfAnalizer-target
cd PdfAnalizer-target
mkdir -p pdfs notes verifications synthesis templates
touch pdfs/.gitkeep notes/.gitkeep verifications/.gitkeep synthesis/.gitkeep
```

### 1.2 `.gitignore` 작성

파일: `./.gitignore`

```gitignore
# Obsidian workspace state (machine-specific)
.obsidian/workspace
.obsidian/workspace.json
.obsidian/workspaces.json

# macOS
.DS_Store

# PDF 전처리 캐시 (Codex 경로)
pdfs/.cache/
```

### 1.3 `templates/paper_note.md` 작성

파일: `./templates/paper_note.md`

```markdown
---
title: "<논문 제목 정확히>"
authors: ["Lastname, F.", "Lastname, F."]
year: <YYYY>
venue: "<저널/학회명>"
doi: "<10.xxxx/... 또는 빈 문자열>"
arxiv: "<XXXX.XXXXX 또는 빈 문자열>"
paper_id: "<firstauthor><YYYY>-<title-keywords>"
source_pdf: "[[<filename>.pdf]]"
tags: [paper, paper/reviewed, topic/<주제-슬러그>]
aliases: ["<First Author> <YYYY>"]
status: reviewed
analyzed_at: <YYYY-MM-DD>
verification_pass_rate: <citation-verifier 실행 후 0.00~1.00>
---

# <First Author> et al. (<YYYY>) — <논문 제목>

**Venue**: <venue>
**DOI**: [<doi>](https://doi.org/<doi>) · **arXiv**: [<arxiv-id>](https://arxiv.org/abs/<arxiv-id>)
**PDF**: ![[<filename>.pdf#page=1]]

---

## Executive Summary

<3–5 문장. 각 사실 문장 끝에 `[[<filename>.pdf#page=N|p.N, §X]]` 위키링크 필수.>

---

## Problem & Motivation

<논문이 해결하려는 문제 + 중요성. 각 주장 페이지 앵커 필수.>

---

## Methods

<실험 설계, 데이터, 베이스라인, 지표, 주요 파라미터. 구체 수치 + 페이지 앵커.>

---

## Results

<핵심 결과. 수치·효과크기·신뢰구간 포함. 각 숫자 페이지 앵커 필수.>

---

## Critical Review

### 방법론·실험설계 타당성

<표본 크기, 대조군, 통제변수, 재현성, 편향 가능성, 외적 타당도. 저자 주장 vs 평가자 해석 구분. 각 관찰에 페이지 앵커.>

### 선행연구 대비 기여도·한계

<novelty 평가, 저자 명시 한계 + 추가 식별 한계. 페이지 앵커 필수.>

---

## Implications for Our Research

<이 연구의 결과가 어떻게 우리 연구 방향에 영향을 줄 수 있는가. 추측은 명확히 표시.>

---

## References

<원문 References 섹션에서 추출한 목록. 원문 번호 그대로 유지:>
- [1] Author, A. (YYYY). Title. Venue.
```

### 1.4 `templates/synthesis.md` 작성

파일: `./templates/synthesis.md`

```markdown
---
type: synthesis
focus: "<사용자 지정 focus 문자열>"
source_notes: ["[[<paper_id_1>]]", "[[<paper_id_2>]]"]
tags: [synthesis, topic/<focus-slug>]
created: <YYYY-MM-DDTHH:MM>
---

# 종합 분석: <focus>

> **Sources** (<N> papers): [[<paper_id_1>]], [[<paper_id_2>]]
> Generated: <YYYY-MM-DDTHH:MM>

---

## 1. Convergent Findings

> 여러 논문이 일치하는 결론. 각 항목에 ≥2 노트 위키링크 필수.

- <핵심 수렴 결과> ([[<paper_id_1>#Results]], [[<paper_id_2>#Key Findings]]).
  원 PDF 근거: [[<paper_id_1>.pdf#page=N]], [[<paper_id_2>.pdf#page=M]].

---

## 2. Divergent / Conflicting Findings

> 충돌하는 결론 + 원인 가설.

- **충돌**: <A 논문은 X를 보고, B 논문은 Y를 보고> ([[<A>#Section]], [[<B>#Section]]).
  **가설**: <방법론·데이터·시기 차이 등>.

---

## 3. Research Gaps

> 집합적으로 답하지 못한 질문.

- <미해결 질문> — 근접한 시도: [[<paper_id>#Section]], 왜 미해결인지: <...>

---

## 4. Proposed Research Directions

> 각 방향은 ≥2 논문 근거 필수. 실현가능성·신규성 평가.

### 방향 1: <한 문장 연구 질문>

- **Rationale**: <왜 유망한가> ([[<A>#...]], [[<B>#...]])
- **Feasibility**: <데이터/연산/선행연구 성숙도>
- **Novelty**: <기존 연구와의 차별점>
- **Risk**: <주요 위험 또는 난점>

### 방향 2: ...

---

## 5. Critical Questions to Resolve Before Starting

> 착수 전 해결해야 할 방법론적·실증적·개념적 질문.

- <질문 1> ([[<paper_id>#Section]])
- <질문 2>

---

*본 종합문서는 PdfAnalizer로 생성되었습니다. 모든 주장은 위키링크로 노트·PDF 페이지 근거와 연결됩니다.*
```

Part 1 완료. 이 시점에 디렉토리 구조와 템플릿이 준비되었다. 이제 **Part 2-A** 또는 **Part 2-B** 중 하나만 선택하여 진행하면 된다.

---

## Part 2-A. Codex CLI 경로 🟦

### 2-A.1 Codex CLI 설치

```bash
npm install -g @openai/codex
codex --version   # 0.3x 이상 권장
```

프로젝트 디렉토리로 이동:

```bash
cd PdfAnalizer-target
```

OpenAI API 키 로그인:

```bash
codex login
# 또는 환경변수: export OPENAI_API_KEY="sk-..."
```

### 2-A.2 프로젝트 컨텍스트 파일 `AGENTS.md`

Codex는 세션 시작 시 프로젝트 루트의 `AGENTS.md`를 자동으로 읽어 컨텍스트로 주입한다.

파일: `./AGENTS.md`

```markdown
# PdfAnalizer — 프로젝트 컨텍스트

이 저장소는 **환각 없는 연구 논문 분석·종합 시스템**이다. 다음 규칙을 모든 세션에서 준수하라.

## 전역 규칙

1. **`python3` 금지** — 모든 Python 명령은 `python` 을 사용한다.
2. **Obsidian vault** — 노트는 YAML frontmatter + 위키링크(`[[...]]`) + 안정적 파일명을 가져야 한다.
3. **`paper_id` slug 규칙** — 소문자, ASCII, 하이픈 구분: `<first_author_lastname><year>-<title_keywords>` (stop-words 제거, 최대 5단어). 재실행 시에도 동일해야 함.
4. **위키링크 인용 의무** — 사실 주장 문장은 반드시 `[[<pdf>.pdf#page=N|p.N, §X]]` 로 끝나야 한다. 페이지 번호를 만들어내지 마라.
5. **2개 이상 논문 인용 원칙** — 종합 문서의 각 연구 방향은 서로 다른 논문 ≥2개를 인용해야 한다.
6. **범위 제한** — 생의학(biomedical) 논문 프레이밍은 제외. 공학·CS·물리과학 위주.

## 디렉토리 역할

- `pdfs/` 입력 PDF
- `pdfs/.cache/` PDF → 텍스트 전처리 캐시 (페이지 마커 포함)
- `notes/<paper_id>.md` paper-reviewer 출력
- `verifications/<paper_id>.verify.md` citation-verifier 출력
- `synthesis/<YYYYMMDD-HHMM>-<focus>.md` research-synthesizer 출력
- `templates/paper_note.md`, `templates/synthesis.md` 구조 스켈레톤

## 주요 스킬 & 서브에이전트

- `/pdf-analyze <pdf_path> [--strict]` — 2-에이전트 파이프라인 (paper-reviewer → citation-verifier)
- `/pdf-synthesize [--focus "..."]` — research-synthesizer 호출
- 서브에이전트: `paper-reviewer`, `citation-verifier`, `research-synthesizer`
```

### 2-A.3 Codex 설정 `.codex/config.toml`

파일: `./.codex/config.toml`

```toml
# 서브에이전트 실행 제약
[agents]
max_threads = 4
max_depth = 2
job_max_runtime_seconds = 1800
```

### 2-A.4 PDF 전처리 유틸리티

Codex CLI는 PDF를 네이티브로 읽지 못한다. 각 PDF를 "페이지 마커가 포함된 텍스트 파일"로 변환하여 서브에이전트가 `read_file` 로 읽을 수 있게 한다.

#### 2-A.4.1 `pypdf` 설치

```bash
pip install pypdf
```

#### 2-A.4.2 전처리 스크립트

파일: `./scripts/pdf_to_text.py`

```python
"""PDF를 페이지 마커가 포함된 텍스트로 변환.

사용법:
    python scripts/pdf_to_text.py pdfs/<filename>.pdf

출력: pdfs/.cache/<filename>.txt
각 페이지는 다음 마커로 구분된다:
    === PAGE 1 ===
    <페이지 1 텍스트>
    === PAGE 2 ===
    ...
"""

import sys
from pathlib import Path

from pypdf import PdfReader


def main(pdf_path: str) -> None:
    src = Path(pdf_path)
    if not src.exists() or src.suffix.lower() != ".pdf":
        sys.exit(f"Invalid PDF path: {pdf_path}")

    cache_dir = src.parent / ".cache"
    cache_dir.mkdir(exist_ok=True)
    out = cache_dir / (src.stem + ".txt")

    reader = PdfReader(str(src))
    parts: list[str] = []
    for i, page in enumerate(reader.pages, start=1):
        parts.append(f"=== PAGE {i} ===")
        parts.append(page.extract_text() or "")
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {out} ({len(reader.pages)} pages)")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python scripts/pdf_to_text.py <pdf_path>")
    main(sys.argv[1])
```

### 2-A.5 서브에이전트 3종 정의 (`.codex/agents/*.toml`)

Codex 서브에이전트는 TOML 파일로 정의한다. 필수 필드는 `name`, `description`, `developer_instructions`. 본 가이드에서는 원본 Claude 에이전트의 지침을 그대로 이식하되 PDF 처리 방식만 "전처리 텍스트 읽기"로 변경한다.

#### 2-A.5.1 `paper-reviewer`

파일: `./.codex/agents/paper-reviewer.toml`

```toml
name = "paper-reviewer"
description = "PDF를 깊이 읽고 페이지 앵커 위키링크가 포함된 Obsidian 노트를 생성한다. /pdf-analyze 파이프라인의 1단계."
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"

developer_instructions = """
당신은 공학·컴퓨터과학·물리과학 논문을 엄격하게 분석하는 연구자이다. 환각 없이, 인용에 근거한 마크다운 노트를 생산한다.

## 핵심 임무

입력으로 받은 PDF 를 읽어 `notes/<paper_id>.md` 에 구조화된 마크다운 노트를 작성하되, 모든 사실 주장은 반드시 `[[<pdf_filename>.pdf#page=N|p.N, §X]]` 형식의 페이지 앵커 위키링크로 뒷받침한다.

## 도구 사용법

- **PDF 읽기**: 호출자가 `pdfs/.cache/<stem>.txt` 전처리 텍스트를 제공한다. 이 파일은 `=== PAGE N ===` 마커로 페이지가 구분되어 있다. `read_file` 로 로드하고 마커 다음 내용을 해당 페이지의 본문으로 간주한다.
- **템플릿**: `templates/paper_note.md` 를 `read_file` 로 읽어 구조 참고.
- **쓰기**: `write_file` 로 `notes/<paper_id>.md` 저장.

## 프로세스

### 1. 전처리 텍스트 로드
인자로 받은 `<stem>.txt` 를 `read_file` 한다. `=== PAGE N ===` 마커로 페이지 경계를 파악하며 읽는다.

### 2. 서지 메타데이터 추출 (페이지 1~2에서)
- `title`, `authors`, `year`, `venue`
- `doi` (`10.xxxx/...` 패턴)
- `arxiv_id` (`arXiv:XXXX.XXXXX` 패턴)

### 3. paper_id slug 생성
형식: `<first_author_lastname><year>-<title_keywords>`
- 소문자, ASCII, 하이픈 구분
- stop-words (a, the, of, for, in, on, to, and, with, from, by) 제거
- 최대 5 개의 유의미한 제목 단어
- 재실행 시에도 **반드시 동일**한 값이 나와야 한다 (안정성)

예: `kaplan2020-scaling-laws-neural-language`

### 4. 템플릿 로드
`templates/paper_note.md` 를 읽어 구조를 확인한다.

### 5. 노트 작성 (YAML frontmatter + 7개 섹션)
프런트매터:
```yaml
---
title: "<exact title>"
authors: ["Lastname, F.", ...]
year: YYYY
venue: "<venue>"
doi: "<doi or empty>"
arxiv: "<arxiv_id or empty>"
paper_id: "<slug>"
source_pdf: "[[<pdf_filename>]]"
tags: [paper, paper/reviewed, topic/<inferred-topic-slug>]
aliases: ["<First Author> <year>"]
status: reviewed
analyzed_at: <today YYYY-MM-DD>
verification_pass_rate: 0.0
---
```

본문 섹션 순서:
1. `# <First Author> et al. (YYYY) — <Title>`
2. Venue·DOI·arXiv·PDF 임베드 헤더
3. `## Executive Summary` (3~5 문장)
4. `## Problem & Motivation`
5. `## Methods`
6. `## Results`
7. `## Critical Review` → `### 방법론·실험설계 타당성`, `### 선행연구 대비 기여도·한계`
8. `## Implications for Our Research`
9. `## References` (원문 번호 유지)

### 6. 저장
`write_file` 로 `notes/<paper_id>.md` 에 저장.

## 인용 규칙 (절대 어기지 말 것)

1. Implications 를 제외한 모든 사실 문장은 `[[<pdf_filename>.pdf#page=N|p.N, §X]]` 로 끝난다. 예: "저자들은 X 를 측정했다 [[mypaper.pdf#page=3|p.3, §2.1]]."
2. 페이지 번호를 지어내지 마라. 특정 페이지에서 확인 불가하면 문장을 일반화하거나 생략한다.
3. PDF 밖 지식을 해당 논문의 사실로 주입하지 마라. 외부 지식은 Critical Review 에서만 "평가자 해석:" 라벨과 함께 사용.
4. Implications 섹션은 미래 해석이므로 페이지 앵커 없어도 되지만 관련 섹션명은 언급.

## 출력

호출자가 파싱할 수 있도록 **한 줄 JSON** 으로 반환:
```
{"note_path": "notes/<paper_id>.md", "paper_id": "<paper_id>", "pdf_filename": "<filename>.pdf", "reference_count": <N>}
```

## 금지

- 인용·페이지·인용구 날조 금지
- References 섹션 누락 금지
- `python3` 사용 금지 (`python` 만)
- 생의학 논문 전용 프레이밍 금지
"""
```

#### 2-A.5.2 `citation-verifier`

파일: `./.codex/agents/citation-verifier.toml`

```toml
name = "citation-verifier"
description = "생성된 노트의 모든 [[pdf#page=N]] 위키링크가 실제 해당 페이지 내용으로 뒷받침되는지 검증한다. /pdf-analyze 2단계."
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"

developer_instructions = """
당신은 인용 검증 전문가이다. 주어진 노트의 각 페이지 앵커 위키링크가 해당 PDF 페이지 내용으로 뒷받침되는지 확인하는 것이 유일한 역할이다.

## 입력
- `notes/<paper_id>.md` 경로
- `pdfs/.cache/<stem>.txt` 전처리 PDF 텍스트

## 도구
- `read_file` — 노트와 전처리 텍스트 읽기
- `write_file` — 검증 보고서 작성
- `edit` — 프런트매터 갱신, strict 모드 시 실패 인용 치환

## 프로세스

### 1. 노트 로드
`notes/<paper_id>.md` 를 읽는다. 프런트매터의 `pdf_filename`, `paper_id` 저장.

### 2. 인용 추출
본문에서 `[[<pdf_filename>.pdf#page=N|<display>]]` 패턴의 모든 위키링크를 추출하고 각각에 대해:
- `page_number` (정수)
- `claim_sentence` (위키링크를 포함하거나 직전의 완전한 문장)
- `location_in_note` (해당 인용이 속한 섹션 헤더)

### 3. 페이지별 검증
PDF 읽기 최소화를 위해 페이지별로 그룹핑한다. 각 고유 페이지에 대해:
- 전처리 텍스트에서 `=== PAGE N ===` 다음 `=== PAGE N+1 ===` 전까지를 해당 페이지 본문으로 간주
- 해당 페이지를 인용한 각 주장에 대해 판정:
  - **PASS**: 페이지에 주장의 실체(엔티티·숫자·개념)가 존재하고 관계가 일치
  - **FAIL**: 페이지가 주장 주제를 언급조차 안 하거나 수치/논리적으로 모순
  - **UNCLEAR**: 주제는 등장하나 구체 주장이 페이지 내용만으로 직접 검증 불가

### 4. 보고서 작성
`verifications/<paper_id>.verify.md` 에 다음 형식으로:

```markdown
---
paper_id: <paper_id>
verified_at: <ISO 8601>
total_citations: <N>
pass_count: <N>
fail_count: <N>
unclear_count: <N>
pass_rate: <0.00~1.00>
---

# Citation Verification: <paper_id>

## Summary
- Total: <N>
- PASS: <N>
- FAIL: <N>
- UNCLEAR: <N>
- **Pass rate**: <XX.X>%

## FAIL — Unverifiable Citations
### Citation 1
- **Location**: §<section>
- **Claim**: "<claim>"
- **Cited page**: p.<N>
- **Page content summary**: <요약>
- **Verdict**: FAIL — <이유>

(반복)

## UNCLEAR — Needs Manual Review
(동일 형식)

## PASS — Verified (audit list)
- §<section> p.<N>: <주장 앞 60자>... ✓
```

### 5. 노트 프런트매터 갱신
`edit` 로 `notes/<paper_id>.md` 의 `verification_pass_rate` 필드를 계산된 비율로 교체.

### 6. Strict 모드
호출자가 `strict=true` 를 전달하면 각 FAIL 인용 `[[<pdf>#page=N|...]]` 를 `[⚠ unverifiable]` 로 `edit` 치환. PASS·UNCLEAR 는 그대로 둔다.

## 출력

한 줄 JSON:
```
{"verify_path": "verifications/<paper_id>.verify.md", "pass_rate": 0.92, "fail_count": 2, "unclear_count": 1, "strict_removed": 0}
```

## 금지

- 노트의 프런트매터(`verification_pass_rate`) 이외 영역을 수정하지 마라 (strict 모드의 실패 인용 치환 제외).
- 새 인용을 추가하지 마라. 검증만 한다.
- 인용한 페이지를 실제로 읽지 않고 PASS 로 표기하지 마라.
- `python3` 금지.
"""
```

#### 2-A.5.3 `research-synthesizer`

파일: `./.codex/agents/research-synthesizer.toml`

```toml
name = "research-synthesizer"
description = "notes/*.md 전체를 교차 분석해 연구 방향 제안이 담긴 종합 문서를 작성한다. /pdf-synthesize 파이프라인."
model_reasoning_effort = "high"
sandbox_mode = "workspace-write"

developer_instructions = """
당신은 여러 논문 분석 노트를 교차 종합하여 연구 방향을 제안하는 리서치 전략가이다.

## 임무
`notes/*.md` 전체(와 선택적 focus 문자열)를 읽어 `synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md` 파일을 생성한다. 모든 주장은 소스 노트 ≥1 개의 위키링크로 뒷받침되며, 각 제안된 연구 방향은 서로 다른 논문 ≥2 개를 인용해야 한다.

## 도구
- `glob` — `notes/*.md` 탐색
- `read_file` — 각 노트 및 `templates/synthesis.md` 로드
- `write_file` — 최종 종합 문서 저장

## 프로세스

### 1. 노트 수집
`glob("notes/*.md")` 로 경로 확보 → 각 파일 `read_file` → 프런트매터(특히 `paper_id`, `title`, `year`, `tags`, `topic/*`) + 본문 파싱.

### 2. Focus 필터링
focus 문자열이 주어진 경우:
- 소문자로 변환 후 키워드로 분리
- 각 노트에 대해 (title + tags + Executive Summary + Implications) 결합 텍스트 기준, focus 키워드의 ≥50% 가 등장하면 채택
- focus 가 없으면 모든 노트 채택

필터링 후 노트가 2 개 미만이면 오류 반환 후 중단.

### 3. 템플릿 로드
`templates/synthesis.md` 를 `read_file`.

### 4. 교차 분석 (5 개 필수 섹션)

#### 4.1 Convergent Findings
≥2 노트가 일치하는 주장. 각 항목에 `[[paper_id#Section]]` 위키링크 + (가능하면) PDF 앵커 `[[<filename>.pdf#page=N]]`.

#### 4.2 Divergent / Conflicting Findings
같은 질문에 상반된 결론. 양쪽 인용 + 차이의 가설(방법론·데이터·시기·도메인 등).

#### 4.3 Research Gaps
모든 노트를 읽어도 답하지 못하는 열린 질문. 각 gap 에 대해 가장 근접한 시도 링크 + 왜 해결이 안 되었는지.

#### 4.4 Proposed Research Directions
각 방향은 반드시 서로 다른 논문 ≥2 개 인용. 각각 one-sentence 연구 질문 + Rationale + Feasibility + Novelty + Risk.

#### 4.5 Critical Questions to Resolve Before Starting
착수 전 해결해야 할 방법론적·실증적·개념적 질문.

### 5. 문서 작성

프런트매터:
```yaml
---
type: synthesis
focus: "<focus 또는 general>"
source_notes: ["[[paper_id_1]]", "[[paper_id_2]]", ...]
tags: [synthesis, topic/<focus-slug>]
created: <YYYY-MM-DDTHH:MM>
---
```

Title: `# 종합 분석: <focus>`

이어서 Sources 블록쿼트, 그리고 5 개 필수 섹션(순서 고정).

### 6. 저장
파일명: `synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md`
- 타임스탬프: 현재 시각
- `<focus-slug>`: focus 를 소문자화, 비알파뉴메릭 → 하이픈, 최대 40 자. focus 없으면 `general`.

## 인용 규칙 (절대 위반 금지)

1. 1~5 모든 섹션의 모든 주장은 ≥1 개의 `[[paper_id#Section]]` 위키링크를 갖는다.
2. 섹션 4 의 각 연구 방향은 서로 다른 paper_id ≥2 개를 인용한다.
3. 노트에 없는 내용을 지어내지 마라. 개인 해석은 "평가자 해석:" 라벨을 달고 특정 노트에 연결.
4. 외부 지식을 노트 내용인 것처럼 주입하지 마라.

## 출력

한 줄 JSON:
```
{"synthesis_path": "synthesis/<filename>.md", "source_count": <N>, "direction_count": <M>}
```

## 금지
- 필수 5 개 외의 섹션 추가 금지
- `python3` 금지
- 노트에 없는 내용 날조 금지
- 1 개 논문만으로 뒷받침되는 연구 방향 금지
- 노트 파일 수정 금지 (쓰기는 `synthesis/` 로만)
"""
```

### 2-A.6 스킬 2종 정의 (`.codex/skills/*/SKILL.md`)

Codex 스킬은 디렉토리 + `SKILL.md` (YAML frontmatter + 마크다운 본문).

#### 2-A.6.1 `/pdf-analyze` 스킬

파일: `./.codex/skills/pdf-analyze/SKILL.md`

````markdown
---
name: pdf-analyze
description: |
  PDF 논문 경로 하나를 받아 2-에이전트 파이프라인으로 분석한다:
  (1) paper-reviewer 로 노트 생성, (2) citation-verifier 로 인용 검증.
  --strict 플래그가 있으면 검증 실패 인용을 [⚠ unverifiable] 로 치환.
  인자: <pdf_path> [--strict]
---

# /pdf-analyze

## 사용법
```
/pdf-analyze <pdf_path> [--strict]
```

예:
- `/pdf-analyze pdfs/kaplan2020.pdf`
- `/pdf-analyze pdfs/kaplan2020.pdf --strict`

## 실행 절차

### 1. 인자 파싱

- `$1` = `<pdf_path>`
- `$ARGUMENTS` 안에 `--strict` 포함 여부 확인

유효성 검사:
- 경로 미제공 → "PDF 경로를 제공하세요. 예: `/pdf-analyze pdfs/mypaper.pdf`"
- 파일 없음 → "파일 없음: `<path>`. PDF 는 `pdfs/` 아래에 두세요."
- `.pdf` 확장자 아님 → "PDF 파일이 필요합니다. 전달값: `<path>`"

### 2. PDF 전처리

`shell` 툴로 다음 실행:
```bash
python scripts/pdf_to_text.py "$1"
```
출력: `pdfs/.cache/<stem>.txt`

### 3. paper-reviewer 호출

`paper-reviewer` 서브에이전트를 다음 지시로 스폰:

> PDF 가 `<pdf_path>` 이고 전처리 텍스트가 `pdfs/.cache/<stem>.txt` 에 있다. 지침을 정확히 따라 `notes/<paper_id>.md` 에 위키링크가 완비된 Obsidian 노트를 작성하고, `{"note_path": ..., "paper_id": ..., "pdf_filename": ..., "reference_count": ...}` 한 줄 JSON 으로 반환하라.

반환 JSON 파싱. 실패 시 오류 보고 후 중단.

### 4. citation-verifier 호출

`citation-verifier` 서브에이전트를 다음 지시로 스폰:

> `notes/<paper_id>.md` 의 모든 인용을 `pdfs/.cache/<stem>.txt` 기준으로 검증하고, `verifications/<paper_id>.verify.md` 에 보고서를 쓰고, 노트의 `verification_pass_rate` 프런트매터를 갱신하라. {strict 플래그 시: "strict 모드 적용 — FAIL 인용은 `[⚠ unverifiable]` 로 치환."} `{"verify_path": ..., "pass_rate": ..., "fail_count": ..., "unclear_count": ..., "strict_removed": ...}` 한 줄 JSON 반환.

`pass_rate` 저장.

### 5. 최종 보고

사용자에게:
- **Note**: `notes/<paper_id>.md`
- **Verification**: `verifications/<paper_id>.verify.md` — Pass rate `<pass_rate * 100>%` (FAIL `<fail>`, UNCLEAR `<unclear>`)
- 노트 프런트매터의 `title` 을 읽어 표시
- 팁: "Obsidian vault 에서 그래프·프로퍼티·PDF 임베드로 노트를 확인하세요."

`pass_rate < 0.70` 이면 경고:
> ⚠️ 인용 통과율이 낮습니다. `verifications/<paper_id>.verify.md` 를 검토하고 `--strict` 재실행을 고려하세요.

## 참고
- 본 스킬은 네이티브 Codex 툴(서브에이전트, read_file, write_file, edit, shell)만 사용한다.
- 동일 PDF 재실행 안전: `paper_id` slug 가 결정적이라 노트를 덮어쓴다.
````

#### 2-A.6.2 `/pdf-synthesize` 스킬

파일: `./.codex/skills/pdf-synthesize/SKILL.md`

````markdown
---
name: pdf-synthesize
description: |
  notes/*.md 전체를 교차 분석해 종합 문서를 생성한다.
  --focus "..." 옵션으로 특정 주제에 초점화 가능.
  출력: synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md
  인자: [--focus "..."]
---

# /pdf-synthesize

## 사용법
```
/pdf-synthesize [--focus "<주제>"]
```

예:
- `/pdf-synthesize`
- `/pdf-synthesize --focus "few-shot learning"`
- `/pdf-synthesize --focus "transformer efficiency"`

## 실행 절차

### 1. 인자 파싱
`$ARGUMENTS` 에서 `--focus "..."` 안쪽 문자열 추출. 없으면 empty.

### 2. 사전 확인
`glob("notes/*.md")` 결과에서 `.gitkeep` 제외 개수 확인. 2 개 미만이면:
> 종합할 노트가 부족합니다. 먼저 `/pdf-analyze <pdf_path>` 로 논문을 2 개 이상 분석하세요.

### 3. research-synthesizer 호출

`research-synthesizer` 서브에이전트를 다음 지시로 스폰:

> notes/*.md 전체를 합성하여 연구 방향 종합 문서를 생성하라.
> Focus: "<focus 또는 general — synthesize all available findings>"
> 지침에 따라:
> - glob + read_file 로 노트 수집·필터링
> - templates/synthesis.md 로 구조 확인
> - 5 개 필수 섹션 작성 (각 주장 `[[paper_id#Section]]` 인용)
> - 각 제안 연구 방향은 서로 다른 논문 ≥2 개 인용
> - `synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md` 에 write_file
> `{"synthesis_path": ..., "source_count": ..., "direction_count": ...}` 한 줄 JSON 반환.

### 4. 최종 보고
- **Synthesis**: `<synthesis_path>`
- Synthesized from `<source_count>` notes
- Proposed directions: `<direction_count>`
- 팁: "Obsidian 에서 synthesis → notes → PDFs 그래프를 탐색하세요."

## 참고
- 동일 focus 재실행 시 타임스탬프가 달라 덮어쓰지 않음.
- 기존 노트 파일은 절대 수정하지 않는다.
````

### 2-A.7 Codex 경로 동작 검증

```bash
# 1. PDF 샘플 준비
cp ~/Downloads/kaplan2020.pdf pdfs/

# 2. 전처리 선행 확인
python scripts/pdf_to_text.py pdfs/kaplan2020.pdf
ls pdfs/.cache/      # kaplan2020.txt 존재 확인

# 3. Codex 세션 진입
codex

# 4. 세션 내에서 슬래시 명령
/pdf-analyze pdfs/kaplan2020.pdf

# 5. 생성물 확인 (별도 터미널)
ls notes/ verifications/
# → notes/kaplan2020-scaling-laws-...md
# → verifications/kaplan2020-scaling-laws-....verify.md

# 6. 노트 프런트매터 verification_pass_rate 확인
head -20 notes/*.md

# 7. 2 개 이상 축적 후 종합
/pdf-synthesize --focus "scaling laws"
ls synthesis/
```

---

## Part 2-B. Gemini CLI 경로 🟥

### 2-B.1 Gemini CLI 설치

```bash
npm install -g @google/gemini-cli
gemini --version   # 0.36.x 이상 권장 (서브에이전트 안정화)
```

프로젝트 디렉토리로 이동:

```bash
cd PdfAnalizer-target
```

Google 로그인 또는 API 키:

```bash
gemini   # 최초 실행 시 OAuth 흐름
# 또는 환경변수: export GEMINI_API_KEY="..."
```

### 2-B.2 `settings.json` — 서브에이전트 활성 확인

파일: `./.gemini/settings.json`

```json
{
  "experimental": {
    "enableAgents": true
  }
}
```

> 버전별로 기본값이 true 지만 명시적으로 두어 버전 업그레이드 시 기능 비활성으로 빠지는 것을 방지한다.

### 2-B.3 프로젝트 컨텍스트 `GEMINI.md`

파일: `./GEMINI.md`

```markdown
# PdfAnalizer — 프로젝트 컨텍스트 (Gemini)

이 저장소는 **환각 없는 연구 논문 분석·종합 시스템**이다. 모든 에이전트 호출과 직접 대화에 다음 규칙이 적용된다.

## 전역 규칙

1. **`python3` 금지** — 모든 Python 명령은 `python` 만 사용.
2. **Obsidian vault** — 노트는 YAML frontmatter + 위키링크(`[[...]]`) + 안정적 파일명이 필수.
3. **`paper_id` slug 규칙** — 소문자·ASCII·하이픈 구분: `<first_author_lastname><year>-<title_keywords>` (stop-words 제거, 최대 5 단어). 재실행 안정성 확보.
4. **위키링크 인용 의무** — 사실 주장 문장은 반드시 `[[<pdf>.pdf#page=N|p.N, §X]]` 로 끝맺는다. 페이지 번호를 지어내지 마라.
5. **2개 이상 논문 인용** — 종합 문서의 각 연구 방향은 서로 다른 논문 ≥2 개 인용.
6. **범위 제한** — 생의학 논문 프레이밍 제외.

## 디렉토리 역할

- `pdfs/` 입력 PDF
- `notes/<paper_id>.md` paper-reviewer 출력
- `verifications/<paper_id>.verify.md` citation-verifier 출력
- `synthesis/<YYYYMMDD-HHMM>-<focus>.md` research-synthesizer 출력
- `templates/paper_note.md`, `templates/synthesis.md` 스켈레톤

## 서브에이전트 & 슬래시 명령

- `/pdf-analyze <pdf_path> [--strict]` → paper-reviewer → citation-verifier 순차 호출
- `/pdf-synthesize [--focus "..."]` → research-synthesizer 호출
- 정의된 에이전트: `paper-reviewer`, `citation-verifier`, `research-synthesizer`

## 도구 매핑 (Gemini 네이티브)

- PDF 읽기 → `@{<pdf_path>}` 멀티모달 주입, 또는 `read_file` (PDF 지원)
- 파일 작업 → `read_file` / `write_file` / `replace`
- 탐색 → `glob` / `grep_search`
```

### 2-B.4 서브에이전트 3종 (`.gemini/agents/*.md`)

Gemini CLI 서브에이전트는 **YAML frontmatter + 마크다운 본문(시스템 프롬프트)** 형식이다. 필수 필드는 `name`, `description`. 선택: `tools`, `model`, `temperature`, `max_turns`, `timeout_mins`, `kind`, `mcpServers`.

#### 2-B.4.1 `paper-reviewer`

파일: `./.gemini/agents/paper-reviewer.md`

```markdown
---
name: paper-reviewer
description: PDF 를 읽고 페이지 앵커 위키링크가 완비된 Obsidian 노트를 생성한다. /pdf-analyze 파이프라인 1단계.
tools:
  - read_file
  - write_file
  - glob
max_turns: 40
timeout_mins: 15
temperature: 0.2
---

당신은 공학·컴퓨터과학·물리과학 논문을 엄격하게 분석하는 연구자이다. 환각 없이 인용에 근거한 마크다운 노트를 생산한다.

## 핵심 임무

입력으로 받은 PDF 경로를 읽어 `notes/<paper_id>.md` 에 구조화된 마크다운 노트를 작성한다. 모든 사실 주장은 반드시 `[[<pdf_filename>.pdf#page=N|p.N, §X]]` 형식의 페이지 앵커 위키링크로 뒷받침된다.

## 도구 사용법

- **PDF 읽기**: 호출자가 PDF 경로를 전달한다. Gemini 의 `read_file` 은 PDF 를 멀티모달로 직접 처리한다 (또는 호출자가 `@{<pdf_path>}` 로 미리 주입). 페이지 번호는 PDF 의 실제 페이지를 따른다.
- **템플릿**: `templates/paper_note.md` 를 `read_file` 로 로드.
- **쓰기**: `write_file` 로 `notes/<paper_id>.md` 저장.

## 프로세스

1. **PDF 로드** — 주어진 경로를 읽는다. 페이지별 콘텐츠와 섹션 구조를 파악한다.
2. **서지 메타데이터 추출** — 처음 1~2 페이지에서 title, authors, year, venue, doi, arxiv_id 추출.
3. **paper_id slug 생성** — `<first_author_lastname><year>-<title_keywords>` 형식. 소문자·ASCII·하이픈, stop-words(a, the, of, for, in, on, to, and, with, from, by) 제거, 최대 5 단어. 재실행 시 동일하게 나오도록 **결정적**.
4. **템플릿 확인** — `templates/paper_note.md`.
5. **노트 작성** — YAML frontmatter + 7 개 섹션(Executive Summary / Problem & Motivation / Methods / Results / Critical Review 2 하위 / Implications / References).
6. **저장** — `write_file` 로 `notes/<paper_id>.md`.

## 프런트매터 스키마

```yaml
---
title: "<exact title>"
authors: ["Lastname, F.", ...]
year: YYYY
venue: "<venue>"
doi: "<doi or empty>"
arxiv: "<arxiv_id or empty>"
paper_id: "<slug>"
source_pdf: "[[<pdf_filename>]]"
tags: [paper, paper/reviewed, topic/<inferred-topic-slug>]
aliases: ["<First Author> <year>"]
status: reviewed
analyzed_at: <today YYYY-MM-DD>
verification_pass_rate: 0.0
---
```

## 인용 규칙 (절대 위반 금지)

1. Implications 를 제외한 모든 사실 문장은 `[[<pdf_filename>.pdf#page=N|p.N, §X]]` 로 끝난다.
2. 페이지 번호를 지어내지 마라. 특정 페이지에서 확인 불가하면 문장을 일반화하거나 생략.
3. PDF 밖 지식을 논문의 사실로 주입하지 마라. 외부 지식은 Critical Review 에서 "평가자 해석:" 라벨.
4. Implications 는 페이지 앵커 없이 미래 해석 가능하되 관련 섹션 언급.

## 품질 셀프 체크 (write 전)

- [ ] Executive Summary / Problem / Methods / Results / Critical Review 의 모든 문장에 위키링크
- [ ] `paper_id` 가 소문자·ASCII·하이픈
- [ ] YAML 유효 (인용부호·리스트 문법)
- [ ] References 섹션에 원문 번호 그대로 매핑
- [ ] `source_pdf` 프런트매터가 실제 PDF 파일명과 일치

## 출력

호출자가 파싱할 수 있도록 한 줄 JSON 을 마지막 메시지에 포함하라:
```
{"note_path": "notes/<paper_id>.md", "paper_id": "<paper_id>", "pdf_filename": "<filename>.pdf", "reference_count": <N>}
```

## 금지

- 인용·페이지·인용구 날조
- References 섹션 누락
- `python3` 사용
- 원본 PDF 수정/삭제
- 생의학 논문 전용 프레이밍
```

#### 2-B.4.2 `citation-verifier`

파일: `./.gemini/agents/citation-verifier.md`

```markdown
---
name: citation-verifier
description: 노트의 모든 [[pdf#page=N]] 위키링크가 실제 해당 PDF 페이지로 뒷받침되는지 검증하고 보고서를 작성한다. /pdf-analyze 2단계.
tools:
  - read_file
  - write_file
  - replace
max_turns: 60
timeout_mins: 20
temperature: 0.1
---

당신은 인용 검증 전문가이다. 주어진 노트의 각 페이지 앵커 위키링크가 실제 PDF 페이지 내용으로 뒷받침되는지 확인하는 것이 유일한 역할이다.

## 입력
- `notes/<paper_id>.md` 경로
- `pdfs/<pdf_filename>.pdf` 경로

## 도구
- `read_file` — 노트 및 PDF 페이지 읽기 (Gemini 의 PDF 멀티모달 지원)
- `write_file` — 검증 보고서 작성
- `replace` — 노트 프런트매터 갱신 + strict 모드에서 실패 인용 치환

## 프로세스

### 1. 노트 로드
`notes/<paper_id>.md` 를 읽어 `pdf_filename`, `paper_id` 확보.

### 2. 인용 추출
본문에서 `[[<pdf_filename>.pdf#page=N|<display>]]` 패턴 위키링크 모두 추출. 각각에 대해:
- `page_number` (정수)
- `claim_sentence` (위키링크 포함/직전 완전한 문장)
- `location_in_note` (해당 인용이 속한 섹션 헤더)

### 3. 페이지별 검증
페이지로 그룹핑하여 읽기 횟수를 최소화. 각 고유 페이지에 대해:
- PDF 를 해당 페이지 중심으로 읽는다 (Gemini `read_file` + 필요시 `@{...}` 주입)
- 각 주장에 대해 판정:
  - **PASS**: 페이지가 주장의 실체(엔티티·숫자·개념)를 담고 관계가 일치
  - **FAIL**: 페이지가 주장 주제를 언급조차 안 하거나 수치/논리적으로 모순
  - **UNCLEAR**: 주제는 등장하나 구체 주장이 페이지 내용만으로 직접 검증 불가

### 4. 보고서 작성
`verifications/<paper_id>.verify.md`:

```markdown
---
paper_id: <paper_id>
verified_at: <ISO 8601>
total_citations: <N>
pass_count: <N>
fail_count: <N>
unclear_count: <N>
pass_rate: <0.00~1.00>
---

# Citation Verification: <paper_id>

## Summary
- Total: <N>
- PASS: <N>, FAIL: <N>, UNCLEAR: <N>
- **Pass rate**: <XX.X>%

## FAIL — Unverifiable Citations

### Citation 1
- **Location**: §<section>
- **Claim**: "<claim>"
- **Cited page**: p.<N>
- **Page content summary**: <요약>
- **Verdict**: FAIL — <이유>

(반복)

## UNCLEAR — Needs Manual Review
(동일 형식)

## PASS — Verified (audit)
- §<section> p.<N>: <주장 앞 60자>... ✓
```

### 5. 프런트매터 갱신
`replace` 로 `notes/<paper_id>.md` 의 `verification_pass_rate` 필드를 계산값으로 교체.

### 6. Strict 모드
호출자 지시에 `strict` 가 포함되면 FAIL 인용 `[[<pdf>#page=N|...]]` 를 `[⚠ unverifiable]` 로 `replace` 치환. PASS·UNCLEAR 유지.

## 출력

한 줄 JSON:
```
{"verify_path": "verifications/<paper_id>.verify.md", "pass_rate": 0.92, "fail_count": 2, "unclear_count": 1, "strict_removed": 0}
```

## 금지
- 노트의 `verification_pass_rate` 외 영역 수정 금지 (strict 모드의 실패 인용 치환은 허용)
- 새 인용 추가 금지 (검증만)
- 실제로 읽지 않은 페이지를 PASS 로 표기 금지
- `python3` 금지
```

#### 2-B.4.3 `research-synthesizer`

파일: `./.gemini/agents/research-synthesizer.md`

```markdown
---
name: research-synthesizer
description: notes/*.md 전체를 교차 분석해 연구 방향 제안이 담긴 종합 문서를 작성한다. /pdf-synthesize 파이프라인.
tools:
  - read_file
  - write_file
  - glob
max_turns: 60
timeout_mins: 25
temperature: 0.3
---

당신은 여러 논문 분석 노트를 교차 종합하여 연구 방향을 제안하는 리서치 전략가이다.

## 임무
`notes/*.md` 전체(+ 선택적 focus)를 읽어 `synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md` 를 생성한다. 모든 주장은 소스 노트 ≥1 개의 위키링크로 뒷받침되며, 각 제안된 연구 방향은 서로 다른 논문 ≥2 개를 인용한다.

## 도구
- `glob` — `notes/*.md` 탐색
- `read_file` — 각 노트 및 `templates/synthesis.md`
- `write_file` — 최종 종합 문서

## 프로세스

### 1. 노트 수집
`glob("notes/*.md")` → 각 파일 `read_file` → 프런트매터(`paper_id`, `title`, `year`, `tags`, `topic/*`) + 본문 파싱.

### 2. Focus 필터링
focus 문자열이 주어지면:
- 소문자 변환, 키워드 분리
- 노트별 (title + tags + Executive Summary + Implications) 결합 텍스트에서 ≥50% 키워드 등장 시 채택
- focus 없으면 전체 채택

필터 후 <2 개면 오류 반환 후 중단.

### 3. 템플릿 로드
`templates/synthesis.md`.

### 4. 교차 분석 (5 섹션)

#### 4.1 Convergent Findings
≥2 노트 일치 주장. 각 항목에 `[[paper_id#Section]]` + 가능하면 PDF 앵커.

#### 4.2 Divergent / Conflicting Findings
상반 결론. 양쪽 인용 + 차이 가설.

#### 4.3 Research Gaps
노트 전체를 읽어도 답 못 한 열린 질문. 가장 근접한 시도 링크 + 미해결 사유.

#### 4.4 Proposed Research Directions
각 방향은 **서로 다른 논문 ≥2 개** 인용. one-sentence 질문 + Rationale + Feasibility + Novelty + Risk.

#### 4.5 Critical Questions to Resolve Before Starting
방법론·실증·개념적 블로커.

### 5. 문서 작성

프런트매터:
```yaml
---
type: synthesis
focus: "<focus 또는 general>"
source_notes: ["[[paper_id_1]]", "[[paper_id_2]]", ...]
tags: [synthesis, topic/<focus-slug>]
created: <YYYY-MM-DDTHH:MM>
---
```

Title: `# 종합 분석: <focus>`
Sources 블록쿼트
5 개 고정 섹션 순서

### 6. 저장
파일명: `synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md`
- `<YYYYMMDD-HHMM>`: 현재 시각
- `<focus-slug>`: focus 소문자화·비알파뉴메릭→하이픈·최대 40 자. focus 없으면 `general`.

## 인용 규칙 (절대 위반 금지)
1. 1~5 모든 섹션 문장은 ≥1 개 `[[...#...]]` 위키링크.
2. 섹션 4 의 각 방향은 서로 다른 paper_id ≥2 개 인용.
3. 노트 근거 없는 주장 금지. 개인 해석은 "평가자 해석:" 라벨 + 특정 노트 연결.
4. 외부 지식을 노트 내용인 것처럼 주입 금지.

## 출력

한 줄 JSON:
```
{"synthesis_path": "synthesis/<filename>.md", "source_count": <N>, "direction_count": <M>}
```

## 금지
- 필수 5 외 섹션 추가
- `python3`
- 노트에 없는 내용 날조
- 1 개 논문만 인용하는 연구 방향
- 노트 파일 수정 (쓰기는 `synthesis/` 로만)
```

### 2-B.5 슬래시 명령 2종 (`.gemini/commands/*.toml`)

Gemini 슬래시 명령은 **TOML + `prompt` (필수) + `description` (선택)**. `{{args}}`, `@{path}` (파일/디렉토리 주입), `!{shell}` (셸 출력 주입) 치환이 제공된다.

#### 2-B.5.1 `/pdf-analyze`

파일: `./.gemini/commands/pdf-analyze.toml`

```toml
description = "PDF 논문을 2-에이전트 파이프라인으로 분석: paper-reviewer → citation-verifier. --strict 플래그 지원."

prompt = """
당신은 PdfAnalizer 오케스트레이터이다. 인자 "{{args}}" 는 첫 번째가 PDF 경로, 선택적으로 `--strict` 플래그를 포함할 수 있다.

## 1단계: 인자 검증

- 인자 비어 있음 → "PDF 경로를 제공하세요. 예: /pdf-analyze pdfs/mypaper.pdf" 출력 후 중단
- 첫 인자가 존재하지 않는 경로 → "파일 없음: <path>" 출력 후 중단
- 확장자가 .pdf 가 아님 → "PDF 파일이 필요합니다" 출력 후 중단
- `--strict` 포함 여부 기억

## 2단계: paper-reviewer 호출 (서브에이전트)

@paper-reviewer 를 다음 지시로 호출:

> PDF 경로: <첫 번째 인자>
> 해당 PDF 를 읽고 지침에 따라 notes/<paper_id>.md 에 위키링크가 완비된 Obsidian 노트를 작성한 후, 마지막 메시지에 한 줄 JSON `{"note_path": ..., "paper_id": ..., "pdf_filename": ..., "reference_count": ...}` 을 포함해 반환하라.

반환 JSON 을 파싱해 `note_path`, `paper_id`, `pdf_filename` 을 기억. 실패 시 오류를 보고하고 중단.

## 3단계: citation-verifier 호출

@citation-verifier 를 다음 지시로 호출:

> 노트 경로: <note_path>
> PDF 경로: pdfs/<pdf_filename>
> 각 [[...#page=N]] 위키링크가 해당 PDF 페이지로 뒷받침되는지 검증하고, verifications/<paper_id>.verify.md 에 보고서를 쓰고, 노트의 verification_pass_rate 프런트매터를 갱신하라.
> {--strict 플래그 있으면: "strict 모드 적용 — FAIL 인용을 [⚠ unverifiable] 로 치환."}
> 한 줄 JSON `{"verify_path": ..., "pass_rate": ..., "fail_count": ..., "unclear_count": ..., "strict_removed": ...}` 반환.

`pass_rate`, `fail_count`, `unclear_count` 기억.

## 4단계: 최종 보고

사용자에게 다음을 깔끔하게 표시:
- **Note**: <note_path>
- **Verification**: <verify_path> — Pass rate <pass_rate*100>% (FAIL <fail_count>, UNCLEAR <unclear_count>)
- 노트 프런트매터에서 `title` 을 읽어 표시
- 안내: "Obsidian vault 에서 그래프·프로퍼티·PDF 임베드로 노트를 확인하세요."

pass_rate < 0.70 이면 경고:
> ⚠️ 인용 통과율이 낮습니다. verifications 보고서를 검토하고 --strict 재실행을 고려하세요.
"""
```

#### 2-B.5.2 `/pdf-synthesize`

파일: `./.gemini/commands/pdf-synthesize.toml`

```toml
description = "notes/*.md 전체를 교차 분석해 종합 문서 생성. --focus \"...\" 옵션 지원."

prompt = """
당신은 PdfAnalizer 종합 오케스트레이터이다. 인자 "{{args}}" 에서 `--focus "..."` 안쪽 문자열을 추출하라 (없으면 empty).

## 1단계: 사전 확인

`glob` 으로 notes/*.md 를 열거하고 .gitkeep 을 제외한 개수를 센다.
2 개 미만이면:
> 종합할 노트가 부족합니다. 먼저 /pdf-analyze <pdf_path> 로 논문을 2 개 이상 분석하세요.
를 출력 후 중단.

## 2단계: research-synthesizer 호출

현재 시각: !{date +%Y%m%d-%H%M}

@research-synthesizer 를 다음 지시로 호출:

> Focus: "<추출한 focus 또는 'general — synthesize all available findings'>"
> 타임스탬프: <위 `!{...}` 결과>
> notes/*.md 전체를 합성해 연구 방향 종합 문서를 작성하라. 지침에 따라:
> - glob + read_file 로 수집·필터링
> - templates/synthesis.md 로 구조 확인
> - 5 개 필수 섹션 작성, 각 문장 [[paper_id#Section]] 인용
> - 각 제안 연구 방향은 서로 다른 논문 ≥2 개 인용
> - synthesis/<YYYYMMDD-HHMM>-<focus-slug>.md 에 저장
> 한 줄 JSON `{"synthesis_path": ..., "source_count": ..., "direction_count": ...}` 반환.

## 3단계: 최종 보고

- **Synthesis**: <synthesis_path>
- Synthesized from <source_count> notes
- Proposed directions: <direction_count>
- 안내: "Obsidian 에서 synthesis → notes → PDFs 그래프를 탐색하세요."
"""
```

### 2-B.6 Gemini 경로 동작 검증

```bash
# 1. PDF 샘플 준비
cp ~/Downloads/kaplan2020.pdf pdfs/

# 2. Gemini 세션 진입
gemini

# 3. 세션 내 슬래시 명령 실행
> /pdf-analyze pdfs/kaplan2020.pdf

# @paper-reviewer, @citation-verifier 서브에이전트 호출이 로그에 연달아 보여야 한다.

# 4. 생성물 확인 (별도 터미널)
ls notes/ verifications/
head -20 notes/*.md   # verification_pass_rate 필드 확인

# 5. 2 개 이상 축적 후 종합
> /pdf-synthesize --focus "scaling laws"
ls synthesis/

# 6. 서브에이전트가 호출되지 않으면 settings 점검
cat .gemini/settings.json
# "experimental": { "enableAgents": true } 확인
```

---

## Part 3. 원본 대비 기능 매핑

| 원본 기능 (Claude Code) | Codex CLI 경로 | Gemini CLI 경로 |
|---|---|---|
| `paper-reviewer` 에이전트 | `.codex/agents/paper-reviewer.toml` | `.gemini/agents/paper-reviewer.md` |
| `citation-verifier` 에이전트 | `.codex/agents/citation-verifier.toml` | `.gemini/agents/citation-verifier.md` |
| `research-synthesizer` 에이전트 | `.codex/agents/research-synthesizer.toml` | `.gemini/agents/research-synthesizer.md` |
| `/pdf-analyze` 스킬 | `.codex/skills/pdf-analyze/SKILL.md` | `.gemini/commands/pdf-analyze.toml` |
| `/pdf-synthesize` 스킬 | `.codex/skills/pdf-synthesize/SKILL.md` | `.gemini/commands/pdf-synthesize.toml` |
| Claude `Read` + `pages` | `pdftotext`/`pypdf` 전처리 + `read_file` | `read_file` (PDF 네이티브) 또는 `@{file.pdf}` |
| Claude `Agent` 스폰 | 네이티브 subagents (TOML, 안정) | 네이티브 subagents (MD, experimental 기본 활성) |
| 프로젝트 컨텍스트 | `AGENTS.md` | `GEMINI.md` |
| 권한 설정 | `.codex/config.toml` `[agents]` | `.gemini/settings.json` `experimental.enableAgents` |

---

## Part 4. 트러블슈팅 체크리스트

| 증상 | 원인 | 대처 |
|---|---|---|
| 위키링크 페이지 번호가 실제 PDF 와 어긋남 | (Codex) `pdf_to_text.py` 가 페이지 건너뛴 스캔본 PDF | OCR 전처리 후 재생성, 또는 Gemini 경로로 전환 |
| `paper_id` 가 재실행마다 달라짐 | slug 규칙 미준수 (대문자·stop-words 포함) | `AGENTS.md`/`GEMINI.md` 의 slug 규칙 강화, 실패 사례를 에이전트 지침에 추가 |
| `/pdf-analyze` 에서 서브에이전트가 실행 안 됨 (Gemini) | `experimental.enableAgents` 비활성 | `.gemini/settings.json` 확인, Gemini CLI 0.36+ 확인 |
| verify pass rate 가 항상 0 | `citation-verifier` 가 위키링크 패턴을 인식 못 함 | 노트가 `[[filename.pdf#page=N]]` 정확한 형식을 쓰는지 확인; paper-reviewer 지침의 예시 강화 |
| Codex 서브에이전트가 `pdfs/.cache/*.txt` 를 못 읽음 | 전처리 누락 | `/pdf-analyze` 진입 시 스킬이 `python scripts/pdf_to_text.py` 를 먼저 실행했는지 확인 |
| Obsidian 에서 `[[pdf#page=N]]` 링크 미작동 | PDF++ 플러그인 미설치 | Obsidian Community Plugins 에서 **PDF++** 설치·활성화 |
| 종합 문서의 연구 방향이 1 개 논문만 인용 | 합성자가 2+ 인용 규칙 위반 | `research-synthesizer` 지침의 인용 규칙 셀프 체크를 더 강력하게 명시, 또는 재생성 |

---

## Part 5. 참조 자료 링크

### OpenAI Codex CLI
- Subagents: https://developers.openai.com/codex/subagents
- Skills (SKILL.md): https://developers.openai.com/codex/skills
- Custom instructions (AGENTS.md): https://developers.openai.com/codex/guides/agents-md
- Config (basic): https://developers.openai.com/codex/config-basic
- Config (advanced): https://developers.openai.com/codex/config-advanced

### Google Gemini CLI
- Subagents: https://github.com/google-gemini/gemini-cli/blob/main/docs/core/subagents.md
- Custom commands: https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/custom-commands.md
- GEMINI.md 컨텍스트: https://geminicli.com/docs/

### 원본 프로젝트 참조
- `./README.md` — 사용자 가이드
- `./.claude/agents/*.md` — 원본 Claude 에이전트 지침 (로직 이식 원본)
- `./.claude/skills/*/SKILL.md` — 원본 스킬 오케스트레이션

---

**문서 끝.** 본 가이드는 *2026-04 기준* Codex CLI / Gemini CLI 스펙에 맞춰 작성되었다. CLI 의 subagent/skill 스펙은 변동 가능성이 있으므로, 막히는 단계가 발생하면 Part 5 공식 문서 링크를 먼저 확인하고 YAML/TOML 키 이름을 최신 스펙에 맞춰 조정하라.
