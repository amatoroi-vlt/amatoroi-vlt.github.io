# PdfAnalizer-Next: NotebookLM MCP 연동 프로젝트 가이드

> 이 문서는 기존 로컬 기반의 **PdfAnalizer** 아키텍처를 진화시켜, 구글의 **NotebookLM**을 백엔드 엔진으로 활용하는 완전히 새로운 파이프라인을 구축하기 위한 계획서입니다. 빈 디렉토리에서 시작하여 이 문서를 따라가면 자동화된 NotebookLM 파이프라인을 완성할 수 있습니다.

---

## 1. 아키텍처 개요 (The "Next" Architecture)

새로운 시스템은 로컬 모델이 직접 PDF를 읽고 분석하는 대신, **Gemini CLI의 MCP(Model Context Protocol) 클라이언트 기능**을 이용해 실제 웹 기반 NotebookLM 서비스에 PDF를 업로드하고 질문(Query)하여 환각이 완벽히 통제된 답변을 받아옵니다.

### 핵심 워크플로우
1. **업로드 (Ingestion)**: CLI 명령어를 통해 로컬 PDF를 NotebookLM의 새 노트북으로 업로드.
2. **질의 (Querying)**: MCP 서버를 통해 NotebookLM에 논문 분석 프롬프트를 전송.
3. **작성 (Generation)**: NotebookLM이 반환한 검증된 답변을 바탕으로 Obsidian 마크다운 노트 작성.
4. **확장 (Extension)**: 필요에 따라 NotebookLM의 특화 기능인 **Audio Overview (AI 팟캐스트)** 생성을 트리거.

---

## 2. 사전 요구 사항 및 환경 구성

이 프로젝트는 빈 디렉토리에서 시작합니다.

### 2.1. 필수 도구 설치
*   **Gemini CLI**: 최신 버전 (`npm install -g @google/gemini-cli`)
*   **uv**: 빠르고 강력한 Python 패키지 매니저 (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
*   **notebooklm-mcp-cli**: 커뮤니티에서 개발한 NotebookLM 연동용 MCP 서버.

### 2.2. MCP 서버 인증 및 초기화
새로운 프로젝트 디렉토리를 생성한 후, 터미널에서 다음 명령어를 실행하여 NotebookLM에 로그인합니다. (최초 1회 브라우저 창이 열리며 구글 계정 연동이 필요합니다.)

```bash
uv tool install notebooklm-mcp-cli
notebooklm-mcp-cli auth
```

---

## 3. 디렉토리 및 파일 구조 설계

```text
PdfAnalizer-Next/
├── pdfs/                    # 분석할 PDF 파일 보관
├── notes/                   # NotebookLM의 답변을 바탕으로 생성된 Obsidian 노트
├── podcasts/                # (선택) NotebookLM에서 생성된 Audio Overview 저장
├── .gemini/
│   ├── settings.json        # 에이전트 활성화 설정
│   ├── agents/
│   │   └── nlm-reviewer.md  # NotebookLM과 통신하는 핵심 에이전트
│   └── commands/
│       └── nlm-analyze.toml # 사용자 슬래시 명령어
└── README.md
```

---

## 4. 핵심 컴포넌트 구현 계획

### 4.1. 환경 설정 (`.gemini/settings.json`)
에이전트 기능을 활성화합니다.

```json
{
  "experimental": {
    "enableAgents": true
  }
}
```

### 4.2. 핵심 에이전트 (`.gemini/agents/nlm-reviewer.md`)
이 에이전트는 PDF를 직접 읽지 않고, MCP 도구를 통해 NotebookLM에 명령을 내립니다. 가장 중요한 부분은 `mcpServers` 블록을 통해 외부 도구를 연결하는 것입니다.

```yaml
---
name: nlm-reviewer
description: NotebookLM MCP를 사용하여 PDF를 업로드하고 완벽한 인용이 포함된 노트를 생성합니다.
tools:
  - read_file
  - write_file
mcpServers:
  notebooklm:
    command: uvx
    args:
      - notebooklm-mcp-cli
      - run
max_turns: 40
temperature: 0.1
---

당신은 NotebookLM을 제어하여 논문을 분석하는 연구 자동화 에이전트입니다.

## 핵심 임무
1. **MCP 도구 사용**: 제공된 MCP 도구(`notebooklm_*`)를 사용하여 새로운 노트북을 생성합니다. (이름: 입력받은 PDF의 파일명)
2. **소스 업로드**: 생성된 노트북에 대상 PDF 파일을 업로드합니다.
3. **질문 및 분석**: NotebookLM에 다음 구조로 질문(Query)을 던집니다.
   - "이 논문의 Executive Summary, Problem & Motivation, Methods, Results, Critical Review를 상세히 작성해줘. 모든 주장에 반드시 PDF 페이지 번호를 명시해."
4. **노트 작성**: NotebookLM의 답변을 바탕으로 Obsidian 포맷의 마크다운 노트를 `notes/<paper_id>.md` 경로에 생성합니다. (YAML 프론트매터 포함)
5. **(선택) 팟캐스트**: 작업 완료 후 Audio Overview 생성을 트리거할 수 있는지 확인합니다.
```

### 4.3. 사용자 명령어 (`.gemini/commands/nlm-analyze.toml`)
사용자가 터미널에서 직관적으로 파이프라인을 실행할 수 있도록 진입점을 만듭니다.

```toml
description = "NotebookLM을 활용하여 PDF 논문을 분석하고 노트를 생성합니다."

prompt = """
당신은 PdfAnalizer-Next의 오케스트레이터입니다. 인자 "{{args}}"는 분석할 PDF의 경로입니다.

1. 경로가 비어있거나 파일이 없으면 즉시 오류를 반환하세요.
2. @nlm-reviewer 에이전트를 호출하여 다음 지시를 내리세요:
   > PDF 경로: <입력받은 경로>
   > 이 PDF를 NotebookLM에 업로드하고, 상세 분석을 쿼리하여 notes/ 디렉토리에 마크다운 노트를 작성하세요.

3. 에이전트의 작업이 끝나면 사용자에게 생성된 노트의 경로와 NotebookLM 웹 링크(존재하는 경우)를 안내하세요.
"""
```

---

## 5. 기존 버전과의 차이점 및 기대 효과

| 항목 | 기존 (PdfAnalizer) | 신규 (PdfAnalizer-Next) |
| :--- | :--- | :--- |
| **분석 주체** | 로컬 Gemini 모델 (멀티모달 직접 읽기) | 구글 NotebookLM 클라우드 엔진 |
| **인용(Citation) 검증** | 별도의 `citation-verifier` 에이전트 필요 | 불필요 (NotebookLM이 100% 보장) |
| **속도 및 비용** | 토큰 소모량 높음, 로컬 자원 사용 | 웹 API 사용으로 가볍고 빠름 |
| **부가 기능** | 텍스트 분석에 한정 | **Audio Overview (팟캐스트) 생성 가능** |
| **접근성** | 로컬에만 파일 존재 | **모바일/웹 NotebookLM 앱과 동기화됨** |

## 6. 다음 단계 (Next Steps)
1. 새로운 폴더를 만들고 위 구조대로 파일을 세팅하세요.
2. `notebooklm-mcp-cli auth` 로 구글 계정을 연동하세요.
3. `gemini /nlm-analyze pdfs/sample.pdf` 를 실행하여 마법을 경험하세요.
