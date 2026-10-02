#!/usr/bin/env python3
"""
Paper Repository Dashboard Builder
==================================
외부 논문 저장소(ResearchHelper/papers)에서 index.json, INDEX.md, summaries/, transcribed/를 읽어와
Pensieve 블로그용 Master-Detail 대시보드 HTML(reports/Research/paper_repository.html)을 생성하고,
summaries.json 및 manifest.json을 자동으로 갱신합니다.
"""

import os
import sys
import json
import re
import shutil
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

# 기본 경로 설정
DEFAULT_SOURCE_DIR = Path("/Users/jeongsookang/Documents/dev/ResearchHelper/papers")
WORKSPACE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_HTML_PATH = WORKSPACE_DIR / "reports" / "Overwatch" / "paper_repository.html"
ASSETS_DEST_DIR = WORKSPACE_DIR / "reports" / "Overwatch" / "assets" / "papers"
SUMMARIES_JSON_PATH = WORKSPACE_DIR / "reports" / "summaries.json"
MANIFEST_SCRIPT_PATH = WORKSPACE_DIR / ".github" / "scripts" / "generate_manifest.py"


def parse_index_md(index_md_path: Path):
    """INDEX.md에서 논문별 한글 제목, 게재 학술지, 저자, 핵심 요약(Executive Takeaway)을 파싱합니다."""
    if not index_md_path.exists():
        return {}

    content = index_md_path.read_text(encoding="utf-8")
    papers_meta = {}

    # 1. 마스터 인벤토리 표 파싱
    table_rows = re.findall(
        r'\|\s*\*\*?(\d+)\*\*?\s*\|\s*(\d{4})\s*\|\s*\*\*?(.*?)\*\*?\s*\|\s*(.*?)\s*\|\s*\[.*?\]\((summaries/.*?\.md)\)',
        content
    )
    for num, year, title, main_author, summary_rel in table_rows:
        paper_id = Path(summary_rel).stem
        papers_meta[paper_id] = {
            "num": int(num),
            "year": year.strip(),
            "en_title": title.strip().replace('**', ''),
            "main_author": main_author.strip(),
            "ko_title": "",
            "journal": "",
            "takeaway": "",
            "tags": []
        }

    # 2. 섹션 2 논문별 핵심 요약 파싱
    sections = re.split(r'###\s+(\d+)\.\s+\[(\d{4})\]\s+(.*?)\n', content)
    # sections: [preamble, num1, year1, title1, body1, num2, year2, title2, body2, ...]
    for i in range(1, len(sections), 4):
        num = int(sections[i])
        year = sections[i+1].strip()
        ko_title = sections[i+2].strip()
        body = sections[i+3] if i+3 < len(sections) else ""

        # 학술지 추출
        journal_m = re.search(r'-\s*\*\*게재 학술지\*\*:\s*(.*?)\n', body)
        journal = journal_m.group(1).strip() if journal_m else ""

        # 핵심 요약 추출
        takeaway_m = re.search(r'-\s*\*\*핵심 요약.*?\*\*:\s*\n\s*>\s*(.*?)(?:\n\n|\n#|$)', body, re.DOTALL)
        takeaway = takeaway_m.group(1).strip().replace('\n> ', ' ') if takeaway_m else ""

        # 요약 파일명으로 ID 매칭
        summary_link_m = re.search(r'\[.*?\]\(summaries/(.*?)\.md\)', body)
        if summary_link_m:
            paper_id = summary_link_m.group(1)
            if paper_id in papers_meta:
                papers_meta[paper_id]["ko_title"] = ko_title
                papers_meta[paper_id]["journal"] = journal
                papers_meta[paper_id]["takeaway"] = takeaway
            else:
                papers_meta[paper_id] = {
                    "num": num,
                    "year": year,
                    "en_title": ko_title,
                    "main_author": "",
                    "ko_title": ko_title,
                    "journal": journal,
                    "takeaway": takeaway,
                    "tags": []
                }

    return papers_meta


def derive_tags(title: str, text: str):
    """제목 및 본문 텍스트로부터 유의미한 연구 분야 태그를 자동 도출합니다."""
    tag_keywords = {
        "NORM": ["NORM", "Naturally Occurring Radioactive", "천연방사성"],
        "건축자재": ["building materials", "건축자재", "콘크리트", "골재", "aggregate"],
        "감마분광": ["Gamma spectrometry", "감마선", "감마", "HPGe", "FEPE", "LabSOCS"],
        "숙련도시험": ["Intercomparison", "상호비교", "숙련도", "IAEA", "EEAE", "ISO/IEC 17025"],
        "체렌코프": ["Cherenkov", "체렌코프", "LSC", "액체섬광"],
        "이온성액체": ["Ionic Liquid", "이온성 액체", "Bmim", "Salicylate", "파장 시프터"],
        "Pb-210/Bi-210": ["210Pb", "210Bi", "Pb-210", "Bi-210", "납-210"],
        "효율교정": ["Efficiency calibration", "효율 교정", "FEPER", "검출 효율"],
        "방사평형": ["Equilibrium", "Disequilibrium", "영속평형", "방사평형 불평형"],
        "방사선안전/규제": ["EU-BSS", "Gamma Index", "방사선 기준치", "MDA", "먹는물"]
    }
    
    combined = (title + " " + text).lower()
    matched_tags = []
    for tag, patterns in tag_keywords.items():
        if any(p.lower() in combined for p in patterns):
            matched_tags.append(tag)
    return matched_tags[:5]  # 최대 5개 태그


def collect_paper_data(source_dir: Path):
    """외부 저장소에서 모든 논문 데이터를 수집하고 구조화합니다."""
    index_json_path = source_dir / "index.json"
    index_md_path = source_dir / "INDEX.md"
    summaries_dir = source_dir / "summaries"
    transcribed_dir = source_dir / "transcribed"
    images_dir = transcribed_dir / "images"
    raw_dir = source_dir / "raw"

    if not source_dir.exists():
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    # 1. index.json 로드
    raw_index_data = []
    if index_json_path.exists():
        with open(index_json_path, 'r', encoding='utf-8') as f:
            raw_index_data = json.load(f)

    # 2. INDEX.md 메타데이터 파싱
    md_meta = parse_index_md(index_md_path)

    # 3. 이미지 복사 대상 준비
    ASSETS_DEST_DIR.mkdir(parents=True, exist_ok=True)

    papers = []

    # raw_index_data를 기준으로 조합하거나, 파일 목록 기준 조합
    processed_ids = set()

    for item in raw_index_data:
        paper_id = item.get("id")
        if not paper_id:
            continue
        processed_ids.add(paper_id)

        meta = md_meta.get(paper_id, {})
        year = str(item.get("year", meta.get("year", "2024")))
        en_title = item.get("title", meta.get("en_title", paper_id))
        ko_title = meta.get("ko_title", "")
        journal = meta.get("journal", "")
        takeaway = meta.get("takeaway", "")
        authors = item.get("authors", [])
        if isinstance(authors, list):
            authors_str = ", ".join([a.replace('**', '').strip() for a in authors if a.strip()])
        else:
            authors_str = str(authors)

        # 요약문 Markdown 읽기
        summary_md = ""
        summary_file = summaries_dir / f"{paper_id}.md"
        if summary_file.exists():
            summary_md = summary_file.read_text(encoding="utf-8")

        # 전사본 Markdown 읽기
        transcribed_md = ""
        transcribed_file = transcribed_dir / f"{paper_id}.md"
        if transcribed_file.exists():
            transcribed_md = transcribed_file.read_text(encoding="utf-8")

        # 전사본 이미지 복사 및 경로 변환
        paper_img_src_dir = images_dir / paper_id
        if paper_img_src_dir.exists():
            paper_img_dest_dir = ASSETS_DEST_DIR / paper_id
            paper_img_dest_dir.mkdir(parents=True, exist_ok=True)
            for img_file in paper_img_src_dir.glob("*.png"):
                shutil.copy2(img_file, paper_img_dest_dir / img_file.name)
            # 마크다운 내 이미지 링크를 웹 상대 경로(assets/papers/<id>/<name>)로 변환
            # 원본: ![](images/<id>/<filename>.png) -> ![](assets/papers/<id>/<filename>.png)
            transcribed_md = re.sub(
                r'!\[(.*?)\]\(images/' + re.escape(paper_id) + r'/(.*?)\)',
                r'![\1](assets/papers/' + paper_id + r'/\2)',
                transcribed_md
            )

        # PDF 파일 존재 여부
        pdf_file = raw_dir / f"{paper_id}.pdf"
        has_pdf = pdf_file.exists()
        pdf_size_mb = f"{pdf_file.stat().st_size / (1024*1024):.1f} MB" if has_pdf else "N/A"

        # 태그 자동 도출
        tags = derive_tags(en_title + " " + ko_title, summary_md + " " + takeaway)

        papers.append({
            "id": paper_id,
            "year": year,
            "en_title": en_title,
            "ko_title": ko_title,
            "journal": journal,
            "authors": authors_str,
            "takeaway": takeaway,
            "tags": tags,
            "summary_md": summary_md,
            "transcribed_md": transcribed_md,
            "has_pdf": has_pdf,
            "pdf_name": f"{paper_id}.pdf",
            "pdf_size": pdf_size_mb,
            "converted_at": item.get("converted_at", "")
        })

    # 최신 연도순, ID순 정렬
    papers.sort(key=lambda p: (p["year"], p["id"]), reverse=True)
    return papers


def generate_dashboard_html(papers: list) -> str:
    """Master-Detail 인터랙티브 대시보드 HTML을 생성합니다."""
    papers_json = json.dumps(papers, ensure_ascii=False)
    total_count = len(papers)
    years = sorted(list(set(p["year"] for p in papers)), reverse=True)
    all_tags = sorted(list(set(tag for p in papers for tag in p["tags"])))

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>방사선 계측 및 NORM 연구 논문 아카이브 대시보드</title>
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600;700;800&family=Noto+Serif+KR:wght@400;600;700;900&display=swap" rel="stylesheet">
  
  <!-- KaTeX for Math Rendering -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>

  <!-- Marked.js for High-Performance Markdown Parsing -->
  <script src="https://cdn.jsdelivr.net/npm/marked@4.3.0/marked.min.js"></script>

  <style>
    :root {{
      --bg-ground: #0a0e17;
      --bg-panel: #111827;
      --bg-card: #172033;
      --bg-card-hover: #1e293b;
      --bg-card-active: #1e2d4a;
      --border-subtle: #2d3748;
      --border-focus: #3b82f6;
      --ink-base: #e2e8f0;
      --ink-muted: #94a3b8;
      --ink-heading: #f8fafc;
      --accent-primary: #38bdf8;
      --accent-subtle: rgba(56, 189, 248, 0.12);
      --accent-gold: #fbbf24;
      --accent-green: #34d399;
      --accent-purple: #c084fc;
      --tag-bg: #1e293b;
      --tag-border: #334155;
      --tag-text: #94a3b8;
      --tag-active-bg: rgba(56, 189, 248, 0.2);
      --tag-active-border: #38bdf8;
      --tag-active-text: #38bdf8;
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", sans-serif;
      --font-serif: 'Noto Serif KR', Georgia, serif;
      --font-mono: 'IBM Plex Mono', Menlo, Consolas, monospace;
      --header-height: 72px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: var(--bg-ground);
      color: var(--ink-base);
      font-family: var(--font-sans);
      height: 100vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }}

    /* Top Navigation / Header */
    header {{
      height: var(--header-height);
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 1.5rem;
      gap: 1.5rem;
      flex-shrink: 0;
      z-index: 20;
    }}

    .brand {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
    }}

    .brand-badge {{
      background: var(--accent-subtle);
      color: var(--accent-primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.3rem 0.65rem;
      border-radius: 6px;
      font-family: var(--font-mono);
      font-size: 0.75rem;
      font-weight: 600;
      letter-spacing: 0.05em;
    }}

    .brand-title {{
      font-family: var(--font-serif);
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--ink-heading);
      letter-spacing: -0.02em;
    }}

    .search-box-wrapper {{
      flex: 1;
      max-width: 460px;
      position: relative;
    }}

    .search-input {{
      width: 100%;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 0.6rem 1rem 0.6rem 2.4rem;
      color: var(--ink-heading);
      font-size: 0.9rem;
      outline: none;
      transition: all 0.2s ease;
    }}

    .search-input:focus {{
      border-color: var(--border-focus);
      background: #172642;
      box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.25);
    }}

    .search-icon {{
      position: absolute;
      left: 0.85rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--ink-muted);
      font-size: 0.95rem;
      pointer-events: none;
    }}

    .stats-bar {{
      display: flex;
      align-items: center;
      gap: 1rem;
      font-size: 0.85rem;
      color: var(--ink-muted);
    }}

    .stat-pill {{
      display: flex;
      align-items: center;
      gap: 0.4rem;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 0.35rem 0.75rem;
      border-radius: 20px;
      font-family: var(--font-mono);
    }}

    .stat-pill b {{
      color: var(--accent-primary);
    }}

    /* Main Container (Master - Detail Layout) */
    .app-container {{
      flex: 1;
      display: flex;
      overflow: hidden;
    }}

    /* Left Pane: Master List */
    .master-pane {{
      width: 380px;
      min-width: 320px;
      background: var(--bg-panel);
      border-right: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      overflow: hidden;
    }}

    .filter-bar {{
      padding: 1rem 1.25rem 0.75rem;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      background: rgba(17, 24, 39, 0.75);
      backdrop-filter: blur(8px);
    }}

    .filter-label {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--ink-muted);
    }}

    .chips-wrapper {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      max-height: 80px;
      overflow-y: auto;
      scrollbar-width: thin;
    }}

    .chip {{
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      font-size: 0.75rem;
      cursor: pointer;
      background: var(--tag-bg);
      border: 1px solid var(--tag-border);
      color: var(--tag-text);
      transition: all 0.15s ease;
      user-select: none;
    }}

    .chip:hover {{
      border-color: var(--ink-muted);
      color: var(--ink-base);
    }}

    .chip.active {{
      background: var(--tag-active-bg);
      border-color: var(--tag-active-border);
      color: var(--tag-active-text);
      font-weight: 600;
    }}

    .card-list {{
      flex: 1;
      overflow-y: auto;
      padding: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      scrollbar-width: thin;
    }}

    .paper-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 10px;
      padding: 1rem;
      cursor: pointer;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      position: relative;
    }}

    .paper-card:hover {{
      background: var(--bg-card-hover);
      border-color: rgba(56, 189, 248, 0.4);
      transform: translateY(-1px);
    }}

    .paper-card.active {{
      background: var(--bg-card-active);
      border-color: var(--accent-primary);
      box-shadow: 0 4px 20px rgba(56, 189, 248, 0.15);
    }}

    .paper-card.active::before {{
      content: "";
      position: absolute;
      left: 0;
      top: 12px;
      bottom: 12px;
      width: 4px;
      background: var(--accent-primary);
      border-radius: 0 4px 4px 0;
    }}

    .card-meta-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 0.5rem;
    }}

    .card-year-badge {{
      font-family: var(--font-mono);
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--accent-primary);
      background: var(--accent-subtle);
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
    }}

    .card-journal {{
      font-size: 0.75rem;
      color: var(--accent-gold);
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      font-style: italic;
    }}

    .card-title-ko {{
      font-family: var(--font-serif);
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ink-heading);
      line-height: 1.4;
    }}

    .card-title-en {{
      font-size: 0.8rem;
      color: var(--ink-muted);
      line-height: 1.35;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}

    .card-tags {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.35rem;
      margin-top: 0.25rem;
    }}

    .card-tag {{
      font-size: 0.68rem;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      color: var(--ink-muted);
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
      font-family: var(--font-mono);
    }}

    /* Right Pane: Detail View */
    .detail-pane {{
      flex: 1;
      background: var(--bg-ground);
      display: flex;
      flex-direction: column;
      overflow: hidden;
      position: relative;
    }}

    .detail-header {{
      padding: 1.5rem 2rem 1.25rem;
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      flex-shrink: 0;
    }}

    .detail-top-badges {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
      flex-wrap: wrap;
    }}

    .badge-year {{
      background: rgba(56, 189, 248, 0.15);
      color: var(--accent-primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      font-family: var(--font-mono);
      font-size: 0.8rem;
      font-weight: 700;
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
    }}

    .badge-journal {{
      color: var(--accent-gold);
      font-size: 0.85rem;
      font-style: italic;
      font-weight: 500;
    }}

    .detail-title-ko {{
      font-family: var(--font-serif);
      font-size: 1.5rem;
      font-weight: 800;
      color: var(--ink-heading);
      line-height: 1.35;
      letter-spacing: -0.01em;
    }}

    .detail-title-en {{
      font-size: 1rem;
      color: var(--ink-muted);
      line-height: 1.4;
      font-weight: 400;
    }}

    .detail-authors {{
      font-size: 0.85rem;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .detail-tabs-bar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
      background: var(--bg-panel);
      border-bottom: 1px solid var(--border-subtle);
      flex-shrink: 0;
    }}

    .tabs-nav {{
      display: flex;
      gap: 0.5rem;
    }}

    .tab-btn {{
      padding: 0.85rem 1.25rem;
      background: none;
      border: none;
      border-bottom: 2px solid transparent;
      color: var(--ink-muted);
      font-family: var(--font-sans);
      font-size: 0.9rem;
      font-weight: 600;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }}

    .tab-btn:hover {{
      color: var(--ink-base);
    }}

    .tab-btn.active {{
      color: var(--accent-primary);
      border-bottom-color: var(--accent-primary);
      background: rgba(56, 189, 248, 0.05);
    }}

    .tab-badge {{
      font-size: 0.72rem;
      background: rgba(255, 255, 255, 0.1);
      padding: 0.1rem 0.45rem;
      border-radius: 10px;
    }}

    .actions-group {{
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }}

    .action-btn {{
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      padding: 0.4rem 0.85rem;
      border-radius: 6px;
      font-size: 0.8rem;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      color: var(--ink-base);
      transition: all 0.15s ease;
    }}

    .action-btn:hover {{
      background: var(--bg-card-hover);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .action-btn.primary {{
      background: var(--accent-subtle);
      border-color: var(--accent-primary);
      color: var(--accent-primary);
    }}

    .action-btn.primary:hover {{
      background: rgba(56, 189, 248, 0.25);
    }}

    /* Detail Content Scroll Area */
    .detail-body {{
      flex: 1;
      overflow-y: auto;
      padding: 2.2rem 2.5rem 4rem;
      line-height: 1.75;
      scrollbar-width: thin;
    }}

    .content-pane {{
      display: none;
      max-width: 900px;
      margin: 0 auto;
    }}

    .content-pane.active {{
      display: block;
      animation: fadeIn 0.25s ease-out;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Markdown Rendered Typography */
    .markdown-body h1, .markdown-body h2, .markdown-body h3, .markdown-body h4 {{
      font-family: var(--font-serif);
      color: var(--ink-heading);
      margin-top: 2rem;
      margin-bottom: 0.85rem;
      line-height: 1.35;
    }}

    .markdown-body h1 {{ font-size: 1.6rem; border-bottom: 1px solid var(--border-subtle); padding-bottom: 0.6rem; }}
    .markdown-body h2 {{ font-size: 1.35rem; color: var(--accent-primary); border-left: 3px solid var(--accent-primary); padding-left: 0.75rem; margin-top: 2.5rem; }}
    .markdown-body h3 {{ font-size: 1.15rem; color: #f1f5f9; }}

    .markdown-body p {{
      margin-bottom: 1.15rem;
      color: #cbd5e1;
      font-size: 0.96rem;
    }}

    .markdown-body ul, .markdown-body ol {{
      margin-bottom: 1.25rem;
      padding-left: 1.6rem;
      color: #cbd5e1;
    }}

    .markdown-body li {{
      margin-bottom: 0.45rem;
    }}

    .markdown-body strong {{
      color: #f8fafc;
      font-weight: 700;
    }}

    .markdown-body blockquote {{
      background: rgba(30, 41, 59, 0.6);
      border-left: 4px solid var(--accent-primary);
      padding: 1rem 1.25rem;
      border-radius: 0 8px 8px 0;
      margin: 1.25rem 0;
      font-style: normal;
      color: #e2e8f0;
    }}

    .markdown-body table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.88rem;
      background: var(--bg-card);
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid var(--border-subtle);
    }}

    .markdown-body th {{
      background: #1e293b;
      color: var(--ink-heading);
      padding: 0.85rem 1rem;
      text-align: left;
      font-weight: 700;
      border-bottom: 2px solid var(--border-subtle);
    }}

    .markdown-body td {{
      padding: 0.75rem 1rem;
      border-bottom: 1px solid rgba(255, 255, 255, 0.05);
      color: #cbd5e1;
    }}

    .markdown-body tr:last-child td {{
      border-bottom: none;
    }}

    .markdown-body tr:hover td {{
      background: rgba(255, 255, 255, 0.02);
    }}

    .markdown-body img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      border: 1px solid var(--border-subtle);
      margin: 1.5rem 0;
      display: block;
      background: #0f172a;
    }}

    .markdown-body code {{
      font-family: var(--font-mono);
      background: #1e293b;
      color: var(--accent-gold);
      padding: 0.2rem 0.45rem;
      border-radius: 4px;
      font-size: 0.85em;
    }}

    .markdown-body pre {{
      background: #0f172a;
      border: 1px solid var(--border-subtle);
      padding: 1.2rem;
      border-radius: 8px;
      overflow-x: auto;
      margin: 1.25rem 0;
    }}

    .markdown-body pre code {{
      background: none;
      padding: 0;
      color: var(--ink-base);
    }}

    /* Raw PDF Tab Styling */
    .pdf-meta-box {{
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      padding: 2rem;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.2rem;
      max-width: 600px;
      margin: 2rem auto;
    }}

    .pdf-icon-large {{
      font-size: 3.5rem;
      color: #ef4444;
    }}

    .pdf-details {{
      text-align: left;
      width: 100%;
      background: rgba(0, 0, 0, 0.2);
      padding: 1rem 1.25rem;
      border-radius: 8px;
      font-family: var(--font-mono);
      font-size: 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }}

    /* Empty state */
    .empty-state {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      height: 100%;
      color: var(--ink-muted);
      text-align: center;
      gap: 1rem;
    }}

    /* Scrollbars */
    ::-webkit-scrollbar {{
      width: 6px;
      height: 6px;
    }}
    ::-webkit-scrollbar-track {{
      background: transparent;
    }}
    ::-webkit-scrollbar-thumb {{
      background: rgba(255, 255, 255, 0.15);
      border-radius: 3px;
    }}
    ::-webkit-scrollbar-thumb:hover {{
      background: rgba(255, 255, 255, 0.25);
    }}

    @media (max-width: 900px) {{
      .app-container {{
        flex-direction: column;
      }}
      .master-pane {{
        width: 100%;
        height: 40vh;
        border-right: none;
        border-bottom: 1px solid var(--border-subtle);
      }}
      .detail-pane {{
        height: 60vh;
      }}
    }}
  </style>
</head>
<body>

  <!-- Header -->
  <header>
    <div class="brand">
      <span class="brand-badge">RESEARCH ARCHIVE</span>
      <h1 class="brand-title">방사선 계측 &amp; NORM 연구 논문 저장소</h1>
    </div>

    <div class="search-box-wrapper">
      <span class="search-icon">🔍</span>
      <input type="text" id="searchInput" class="search-input" placeholder="논문 제목, 저자, 키워드, 내용 검색 (Ctrl + K)...">
    </div>

    <div class="stats-bar">
      <div class="stat-pill">총 보관 <b>{total_count}편</b></div>
    </div>
  </header>

  <!-- App Body -->
  <div class="app-container">
    
    <!-- Left Master List Pane -->
    <aside class="master-pane">
      <div class="filter-bar">
        <div class="filter-label">연도별 필터</div>
        <div class="chips-wrapper" id="yearFilterChips">
          <div class="chip active" data-filter-type="year" data-value="ALL">전체 ({total_count})</div>
          {"".join([f'<div class="chip" data-filter-type="year" data-value="{y}">{y}</div>' for y in years])}
        </div>

        <div class="filter-label" style="margin-top: 0.2rem;">주제별 태그</div>
        <div class="chips-wrapper" id="tagFilterChips">
          <div class="chip active" data-filter-type="tag" data-value="ALL">전체 태그</div>
          {"".join([f'<div class="chip" data-filter-type="tag" data-value="{t}">#{t}</div>' for t in all_tags])}
        </div>
      </div>

      <div class="card-list" id="cardListContainer">
        <!-- Rendered dynamically by JS -->
      </div>
    </aside>

    <!-- Right Detail Pane -->
    <main class="detail-pane" id="detailPane">
      
      <!-- Detail Header -->
      <div class="detail-header" id="detailHeader">
        <div class="detail-top-badges">
          <span class="badge-year" id="dhYear">2026</span>
          <span class="badge-journal" id="dhJournal">Journal Name</span>
        </div>
        <h2 class="detail-title-ko" id="dhTitleKo">논문 제목 (한글)</h2>
        <div class="detail-title-en" id="dhTitleEn">Paper Full Title in English</div>
        <div class="detail-authors" id="dhAuthors">
          <span>✍️</span> <span id="dhAuthorsText">저자 정보</span>
        </div>
      </div>

      <!-- Detail Tabs Bar -->
      <div class="detail-tabs-bar">
        <div class="tabs-nav">
          <button class="tab-btn active" data-tab="summary">
            💡 심층 구조화 요약 <span class="tab-badge">Tier 2</span>
          </button>
          <button class="tab-btn" data-tab="transcribed">
            📜 원문 전사본 전문 <span class="tab-badge">Full Text</span>
          </button>
          <button class="tab-btn" data-tab="raw">
            📄 원본 PDF 정보
          </button>
        </div>

        <div class="actions-group">
          <button class="action-btn" id="copyCitationBtn" title="인용 복사">
            📋 인용 정보 복사
          </button>
        </div>
      </div>

      <!-- Detail Content Body -->
      <div class="detail-body">
        
        <!-- Tab 1: Summary -->
        <div class="content-pane active markdown-body" id="paneSummary">
          <!-- Rendered Markdown -->
        </div>

        <!-- Tab 2: Full Transcribed -->
        <div class="content-pane markdown-body" id="paneTranscribed">
          <!-- Rendered Markdown -->
        </div>

        <!-- Tab 3: Raw PDF Meta -->
        <div class="content-pane" id="paneRaw">
          <div class="pdf-meta-box">
            <div class="pdf-icon-large">📄</div>
            <h3 style="color: var(--ink-heading); font-size: 1.25rem;">원본 연구 논문 (PDF)</h3>
            <p style="color: var(--ink-muted); font-size: 0.9rem;">
              본 논문의 원문 PDF는 연구 저장소의 <code>raw/</code> 디렉토리에 보관되어 있습니다.
            </p>
            <div class="pdf-details">
              <div><b>파일명:</b> <span id="rawPdfName">-</span></div>
              <div><b>파일크기:</b> <span id="rawPdfSize">-</span></div>
              <div><b>로컬보관경로:</b> <code>papers/raw/<span id="rawPdfPath">-</span></code></div>
            </div>
          </div>
        </div>

      </div>

    </main>

  </div>

  <!-- Data & Logic -->
  <script>
    const PAPERS = {papers_json};
    let currentPaperId = PAPERS.length > 0 ? PAPERS[0].id : null;
    let selectedYear = "ALL";
    let selectedTag = "ALL";
    let searchQuery = "";

    // DOM Elements
    const cardListContainer = document.getElementById("cardListContainer");
    const searchInput = document.getElementById("searchInput");
    const dhYear = document.getElementById("dhYear");
    const dhJournal = document.getElementById("dhJournal");
    const dhTitleKo = document.getElementById("dhTitleKo");
    const dhTitleEn = document.getElementById("dhTitleEn");
    const dhAuthorsText = document.getElementById("dhAuthorsText");
    const paneSummary = document.getElementById("paneSummary");
    const paneTranscribed = document.getElementById("paneTranscribed");
    const rawPdfName = document.getElementById("rawPdfName");
    const rawPdfSize = document.getElementById("rawPdfSize");
    const rawPdfPath = document.getElementById("rawPdfPath");
    const copyCitationBtn = document.getElementById("copyCitationBtn");

    // Initialize Marked & KaTeX
    marked.setOptions({{
      gfm: true,
      breaks: true
    }});

    function safeMarkdown(text) {{
      if (!text) return "*내용이 없습니다.*";
      if (window.marked && typeof marked.parse === "function") {{
        try {{
          return marked.parse(text);
        }} catch (e) {{
          console.warn("Markdown parsing error:", e);
        }}
      }}
      return "<div style='white-space: pre-wrap;'>" + text.replace(/</g, "&lt;").replace(/>/g, "&gt;") + "</div>";
    }}

    function renderMathInElementSafely(elem) {{
      if (typeof renderMathInElement === "function") {{
        try {{
          renderMathInElement(elem, {{
            delimiters: [
              {{left: "$$", right: "$$", display: true}},
              {{left: "$", right: "$", display: false}},
              {{left: "\\\\[", right: "\\\\]", display: true}},
              {{left: "\\\\(", right: "\\\\)", display: false}}
            ],
            throwOnError: false
          }});
        }} catch (err) {{
          console.warn("KaTeX render error:", err);
        }}
      }}
    }}

    function filterPapers() {{
      return PAPERS.filter(p => {{
        const matchYear = (selectedYear === "ALL" || p.year === selectedYear);
        const matchTag = (selectedTag === "ALL" || p.tags.includes(selectedTag));
        const q = searchQuery.toLowerCase().trim();
        const matchSearch = !q || (
          p.en_title.toLowerCase().includes(q) ||
          p.ko_title.toLowerCase().includes(q) ||
          p.authors.toLowerCase().includes(q) ||
          p.takeaway.toLowerCase().includes(q) ||
          p.summary_md.toLowerCase().includes(q)
        );
        return matchYear && matchTag && matchSearch;
      }});
    }}

    function renderCardList() {{
      const filtered = filterPapers();
      cardListContainer.innerHTML = "";

      if (filtered.length === 0) {{
        cardListContainer.innerHTML = `
          <div class="empty-state">
            <div style="font-size: 2rem;">🔍</div>
            <p>검색 조건과 일치하는 논문이 없습니다.</p>
          </div>
        `;
        return;
      }}

      // 현재 선택된 논문이 필터 결과에 없으면 첫 번째 논문으로 전환
      if (!filtered.some(p => p.id === currentPaperId)) {{
        currentPaperId = filtered[0].id;
      }}

      filtered.forEach(p => {{
        const card = document.createElement("div");
        card.className = `paper-card ${{p.id === currentPaperId ? "active" : ""}}`;
        card.onclick = () => selectPaper(p.id);

        const tagsHtml = p.tags.map(t => `<span class="card-tag">#${{t}}</span>`).join("");
        const displayKoTitle = p.ko_title || p.en_title;

        card.innerHTML = `
          <div class="card-meta-row">
            <span class="card-year-badge">${{p.year}}</span>
            <span class="card-journal">${{p.journal || ""}}</span>
          </div>
          <div class="card-title-ko">${{displayKoTitle}}</div>
          <div class="card-title-en">${{p.en_title}}</div>
          <div class="card-tags">${{tagsHtml}}</div>
        `;
        cardListContainer.appendChild(card);
      }});

      renderDetailPane();
    }}

    function selectPaper(paperId) {{
      currentPaperId = paperId;
      document.querySelectorAll(".paper-card").forEach(c => c.classList.remove("active"));
      renderCardList();
    }}

    function renderDetailPane() {{
      const paper = PAPERS.find(p => p.id === currentPaperId);
      if (!paper) return;

      dhYear.textContent = paper.year;
      dhJournal.textContent = paper.journal || "Journal / Conference";
      dhTitleKo.textContent = paper.ko_title || paper.en_title;
      dhTitleEn.textContent = paper.en_title;
      dhAuthorsText.textContent = paper.authors || "저자 정보 미기재";

      // 1. 심층 요약 마크다운 렌더링
      paneSummary.innerHTML = safeMarkdown(paper.summary_md || "*요약문이 없습니다.*");
      renderMathInElementSafely(paneSummary);

      // 2. 전사본 마크다운 렌더링
      paneTranscribed.innerHTML = safeMarkdown(paper.transcribed_md || "*전사본이 없습니다.*");
      renderMathInElementSafely(paneTranscribed);

      // 3. Raw PDF 정보 갱신
      rawPdfName.textContent = paper.pdf_name;
      rawPdfSize.textContent = paper.pdf_size;
      rawPdfPath.textContent = paper.pdf_name;
    }}

    // Tab Switching
    document.querySelectorAll(".tab-btn").forEach(btn => {{
      btn.addEventListener("click", () => {{
        document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
        document.querySelectorAll(".content-pane").forEach(p => p.classList.remove("active"));

        btn.classList.add("active");
        const tab = btn.dataset.tab;
        if (tab === "summary") document.getElementById("paneSummary").classList.add("active");
        else if (tab === "transcribed") document.getElementById("paneTranscribed").classList.add("active");
        else if (tab === "raw") document.getElementById("paneRaw").classList.add("active");
      }});
    }});

    // Chips Filter Events
    document.querySelectorAll(".chip").forEach(chip => {{
      chip.addEventListener("click", (e) => {{
        const type = chip.dataset.filterType;
        const val = chip.dataset.value;

        if (type === "year") {{
          document.querySelectorAll("#yearFilterChips .chip").forEach(c => c.classList.remove("active"));
          chip.classList.add("active");
          selectedYear = val;
        }} else if (type === "tag") {{
          document.querySelectorAll("#tagFilterChips .chip").forEach(c => c.classList.remove("active"));
          chip.classList.add("active");
          selectedTag = val;
        }}

        renderCardList();
      }});
    }});

    // Search Input Event
    searchInput.addEventListener("input", (e) => {{
      searchQuery = e.target.value;
      renderCardList();
    }});

    // Shortcut Ctrl+K
    window.addEventListener("keydown", (e) => {{
      if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {{
        e.preventDefault();
        searchInput.focus();
      }}
    }});

    // Citation Copy
    copyCitationBtn.addEventListener("click", () => {{
      const paper = PAPERS.find(p => p.id === currentPaperId);
      if (!paper) return;
      const citation = `${{paper.authors}} (${{paper.year}}). "${{paper.en_title}}". ${{paper.journal || ""}}`;
      navigator.clipboard.writeText(citation).then(() => {{
        const prevText = copyCitationBtn.textContent;
        copyCitationBtn.textContent = "✅ 인용 복사됨!";
        setTimeout(() => copyCitationBtn.textContent = prevText, 2000);
      }});
    }});

    // Immediate & Safe Initialization
    function initApp() {{
      renderCardList();
      setTimeout(() => {{
        renderMathInElementSafely(paneSummary);
        renderMathInElementSafely(paneTranscribed);
      }}, 300);
    }}

    if (document.readyState === "loading") {{
      window.addEventListener("DOMContentLoaded", initApp);
    }} else {{
      initApp();
    }}
  </script>
</body>
</html>
"""
    return html


def update_summaries_json(html_path: Path):
    """reports/summaries.json에 논문 아카이브 대시보드 요약을 등록합니다."""
    with open(html_path, 'rb') as f:
        file_hash = hashlib.sha1(f.read()).hexdigest()

    rel_path = str(html_path.relative_to(WORKSPACE_DIR))

    summaries = {}
    if SUMMARIES_JSON_PATH.exists():
        with open(SUMMARIES_JSON_PATH, 'r', encoding='utf-8') as f:
            summaries = json.load(f)

    summaries[rel_path] = {
        "hash": file_hash,
        "summary": "방사선 계측, NORM 특성평가, HPGe 검출기 효율 교정, 체렌코프 광 계측 등 보관된 연구 논문들을 연도별·주제별로 검색하고 2단계 심층 구조화 요약 및 전사본 전문을 한눈에 탐색할 수 있는 Master-Detail 아카이브 대시보드 리포트다."
    }

    with open(SUMMARIES_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(summaries, f, ensure_ascii=False, indent=2)
    print(f"✅ {SUMMARIES_JSON_PATH} 요약 등록 완료")


def regenerate_manifest():
    """generate_manifest.py를 실행하여 manifest.json을 갱신합니다."""
    if MANIFEST_SCRIPT_PATH.exists():
        res = subprocess.run([sys.executable, str(MANIFEST_SCRIPT_PATH)], cwd=WORKSPACE_DIR, capture_output=True, text=True)
        print(res.stdout.strip())
        if res.returncode != 0:
            print(f"⚠️ manifest.json 생성 실패: {res.stderr}")
    else:
        print("⚠️ generate_manifest.py 스크립트를 찾을 수 없습니다.")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Build Paper Repository Dashboard for Pensieve Blog")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE_DIR, help="Path to papers source directory")
    args = parser.parse_args()

    source_dir = args.source.resolve()
    print(f"🚀 논문 저장소 대시보드 빌드 시작: {source_dir}")

    papers = collect_paper_data(source_dir)
    print(f"📦 총 {len(papers)}편의 논문 데이터를 수집 및 처리하였습니다.")

    html_content = generate_dashboard_html(papers)
    OUTPUT_HTML_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_HTML_PATH.write_text(html_content, encoding="utf-8")
    print(f"✨ 대시보드 HTML 생성 완료: {OUTPUT_HTML_PATH}")

    update_summaries_json(OUTPUT_HTML_PATH)
    regenerate_manifest()
    print("🎉 논문 아카이브 대시보드 빌드가 성공적으로 완료되었습니다!")


if __name__ == "__main__":
    main()
