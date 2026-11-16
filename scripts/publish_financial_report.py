#!/usr/bin/env python3
"""
scripts/publish_financial_report.py

tmp/output/ (또는 지정된 경로)의 재무 분석 마크다운 보고서와 Sankey 시각화 에셋을
Pensieve 고품질 HTML 보고서로 컴파일하고 reports/Invest/ 로 자동 배포하는 관리 도구.

주요 동작:
  1. tmp/output/<TICKER>/ 내의 .md 보고서 및 이미지/인터랙티브 HTML 에셋 탐색
  2. 에셋을 reports/Invest/assets/<TICKER>/ 로 격리 복사
  3. 마크다운을 Pensieve 프리미엄 디자인(다크/라이트모드, 반응형 테이블, 차트 액션 툴바) HTML로 변환
  4. reports/Invest/<filename>.html 로 배포
  5. reports/summaries.json 에 요약문 및 SHA1 해시 자동 등록
  6. .github/scripts/generate_manifest.py 를 실행하여 manifest.json 갱신
  7. 배포 완료 후 tmp/output/<TICKER>/ 임시 파일 자동 정리
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SRC = os.path.join(REPO_ROOT, "tmp", "output")
DEFAULT_DEST = os.path.join(REPO_ROOT, "reports", "Invest")
SUMMARIES_PATH = os.path.join(REPO_ROOT, "reports", "summaries.json")
MANIFEST_SCRIPT = os.path.join(REPO_ROOT, ".github", "scripts", "generate_manifest.py")


def compute_sha1(filepath):
    with open(filepath, "rb") as f:
        return hashlib.sha1(f.read()).hexdigest()


def load_summaries():
    if os.path.exists(SUMMARIES_PATH):
        try:
            with open(SUMMARIES_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def save_summaries(data):
    with open(SUMMARIES_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def md_to_html_body(md_text, ticker):
    """
    재무 마크다운을 스타일링된 HTML 섹션으로 변환한다.
    """
    lines = md_text.splitlines()
    html_out = []
    
    title = ""
    subtitle = ""
    source_info = ""
    
    i = 0
    in_table = False
    table_lines = []
    in_list = False
    
    def flush_table(tbl_lines):
        if not tbl_lines:
            return ""
        header = tbl_lines[0]
        data_rows = tbl_lines[2:] if len(tbl_lines) > 2 else []
        
        headers = [c.strip() for c in header.split("|")[1:-1]]
        
        res = ['<div class="tbl-wrap"><table class="fin-tbl">']
        res.append("  <thead><tr>")
        for h in headers:
            h_clean = re.sub(r"\*\*(.*?)\*\*", r"\1", h)
            res.append(f"    <th>{h_clean}</th>")
        res.append("  </tr></thead>")
        res.append("  <tbody>")
        for row in data_rows:
            cols = [c.strip() for c in row.split("|")[1:-1]]
            if not any(cols):
                continue
            res.append("    <tr>")
            for idx, c in enumerate(cols):
                is_num = bool(re.search(r"[\$\%0-9\.\+\-]", c)) and idx in (1, 2, 3, 4)
                cls_attr = ' class="n"' if is_num else ""
                
                c_fmt = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", c)
                res.append(f"      <td{cls_attr}>{c_fmt}</td>")
            res.append("    </tr>")
        res.append("  </tbody>")
        res.append("</table></div>")
        return "\n".join(res)

    while i < len(lines):
        line = lines[i].strip()
        
        # 1. H1 (Title)
        if line.startswith("# ") and not title:
            title = line[2:].strip()
            i += 1
            continue
            
        # 2. Blockquote (Subtitle / Source)
        if line.startswith("> "):
            bq_text = line[2:].strip()
            bq_lines = [bq_text]
            while i + 1 < len(lines) and lines[i + 1].strip().startswith("> "):
                i += 1
                bq_lines.append(lines[i].strip()[2:].strip())
            
            combined_bq = " ".join(bq_lines)
            combined_bq = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", combined_bq)
            html_out.append(f'<div class="meta-card"><div class="meta-desc">{combined_bq}</div></div>')
            i += 1
            continue

        # 3. Table detection
        if "|" in line and (line.startswith("|") or line.endswith("|")):
            table_lines.append(line)
            in_table = True
            i += 1
            continue
        elif in_table:
            html_out.append(flush_table(table_lines))
            table_lines = []
            in_table = False

        # 4. Horizontal rule
        if line in ("---", "***", "___"):
            html_out.append('<hr class="sep">')
            i += 1
            continue

        # 5. H2
        if line.startswith("## "):
            h2_text = line[3:].strip()
            h2_text = re.sub(r"\*\*(.*?)\*\*", r"\1", h2_text)
            html_out.append(f'<h2 class="sec-title">{h2_text}</h2>')
            i += 1
            continue

        # 6. H3
        if line.startswith("### "):
            h3_text = line[4:].strip()
            h3_text = re.sub(r"\*\*(.*?)\*\*", r"\1", h3_text)
            html_out.append(f'<h3 class="sub-title">{h3_text}</h3>')
            i += 1
            continue

        # 7. Images
        img_match = re.match(r"!\[(.*?)\]\(\./(.*?)\)", line)
        if img_match:
            alt_text = img_match.group(1)
            img_file = img_match.group(2)
            asset_path = f"./assets/{ticker}/{img_file}"
            
            html_out.append(f'''
<div class="infographic-card">
  <div class="card-img-wrap">
    <img src="{asset_path}" alt="{alt_text}" loading="lazy" class="sankey-img">
  </div>
''')
            # Check if next line is interactive chart links
            if i + 1 < len(lines) and ("인터랙티브 차트" in lines[i + 1] or "고해상도 이미지" in lines[i + 1]):
                i += 1
                link_line = lines[i].strip()
                html_link_m = re.search(r"\[인터랙티브 차트.*?\]\(\./(.*?)\)", link_line)
                png_link_m = re.search(r"\[.*?이미지 다운로드.*?\]\(\./(.*?)\)", link_line)
                
                actions = []
                if html_link_m:
                    h_file = html_link_m.group(1)
                    actions.append(f'<a href="./assets/{ticker}/{h_file}" target="_blank" class="action-btn btn-interactive">📊 인터랙티브 차트 열기 (Plotly)</a>')
                if png_link_m:
                    p_file = png_link_m.group(1)
                    actions.append(f'<a href="./assets/{ticker}/{p_file}" target="_blank" download class="action-btn btn-download">💾 4K 고해상도 이미지 다운로드 (PNG)</a>')
                
                if actions:
                    html_out.append(f'  <div class="card-actions">{" ".join(actions)}</div>')
            html_out.append('</div>')
            i += 1
            continue

        # 8. List items (bullet / numbered)
        if line.startswith("- ") or line.startswith("* "):
            item_text = line[2:].strip()
            item_fmt = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", item_text)
            
            if lines[i].startswith("  - ") or lines[i].startswith("    - "):
                html_out.append(f'<li class="sub-item">{item_fmt}</li>')
            else:
                html_out.append(f'<li class="list-item">{item_fmt}</li>')
            i += 1
            continue

        if re.match(r"^\d+\.\s+", line):
            num_match = re.match(r"^(\d+)\.\s+(.*)", line)
            num_idx = num_match.group(1)
            item_text = num_match.group(2).strip()
            item_fmt = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", item_text)
            html_out.append(f'''
<div class="insight-card">
  <div class="insight-num">0{num_idx}</div>
  <div class="insight-content">{item_fmt}</div>
</div>
''')
            i += 1
            continue

        # 9. Plain paragraph
        if line:
            p_fmt = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", line)
            p_fmt = re.sub(r"\*(.*?)\*", r"<em>\1</em>", p_fmt)
            html_out.append(f'<p class="prose">{p_fmt}</p>')
            
        i += 1

    if in_table:
        html_out.append(flush_table(table_lines))

    return title, "\n".join(html_out)


def build_full_html(title, body_content, ticker):
    """
    Pensieve 디자인 시스템에 맞춘 단일 HTML 문서를 생성한다.
    """
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Serif+KR:wght@300;400;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=Inter:wght@400;500;600;700&display=swap">
<style>
:root {{
  color-scheme: light dark;
  --bg:          #fafaf8;
  --panel:       #ffffff;
  --panel-alt:   #f4f5f7;
  --ink:         #1a1d24;
  --ink-2:       #48505e;
  --ink-3:       #747d8c;
  --rule:        #e1e4ea;
  --rule-2:      #cbcfd8;
  --accent:      #1f6feb;
  --accent-soft: #e7f0fd;
  --success:     #16a34a;
  --success-bg:  #f0fdf4;
  --card-shadow: 0 4px 14px rgba(0, 0, 0, 0.05);
  --wide:        1020px;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg:          #0f1117;
    --panel:       #161922;
    --panel-alt:   #1e222d;
    --ink:         #e6edf3;
    --ink-2:       #9da7b3;
    --ink-3:       #6e7681;
    --rule:        #2b313c;
    --rule-2:      #3b4352;
    --accent:      #58a6ff;
    --accent-soft: #16263b;
    --success:     #3fb950;
    --success-bg:  #13251a;
    --card-shadow: 0 4px 14px rgba(0, 0, 0, 0.35);
  }}
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
body {{
  background: var(--bg);
  color: var(--ink);
  font-family: "Noto Serif KR", Georgia, serif;
  font-size: 15.5px;
  line-height: 1.85;
  -webkit-font-smoothing: antialiased;
}}
.container {{
  max-width: var(--wide);
  margin: 0 auto;
  padding: 50px 24px 100px;
}}
header.rep-header {{
  border-bottom: 2px solid var(--rule);
  padding-bottom: 28px;
  margin-bottom: 36px;
}}
.tag-bar {{
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 14px;
}}
.tag-pill {{
  font-family: "IBM Plex Mono", monospace;
  font-size: 11.5px;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 3px 9px;
  border-radius: 4px;
  background: var(--accent);
  color: #fff;
}}
.tag-ticker {{
  font-family: "IBM Plex Mono", monospace;
  font-size: 12px;
  font-weight: 600;
  color: var(--ink-2);
}}
h1.main-title {{
  font-family: "Inter", "Noto Serif KR", sans-serif;
  font-size: clamp(23px, 3.8vw, 32px);
  font-weight: 700;
  line-height: 1.35;
  color: var(--ink);
  letter-spacing: -0.015em;
}}
.meta-card {{
  background: var(--panel-alt);
  border: 1px solid var(--rule);
  border-left: 3px solid var(--accent);
  border-radius: 0 6px 6px 0;
  padding: 14px 18px;
  margin: 20px 0 28px;
  font-size: 13.5px;
  color: var(--ink-2);
  line-height: 1.65;
}}
h2.sec-title {{
  font-family: "Inter", sans-serif;
  font-size: 21px;
  font-weight: 700;
  color: var(--ink);
  margin: 44px 0 18px;
  padding-bottom: 8px;
  border-bottom: 1px solid var(--rule);
}}
h3.sub-title {{
  font-family: "Inter", sans-serif;
  font-size: 16.5px;
  font-weight: 600;
  color: var(--ink);
  margin: 28px 0 14px;
}}
hr.sep {{
  border: 0;
  border-top: 1px solid var(--rule);
  margin: 48px 0;
}}
.infographic-card {{
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 8px;
  padding: 16px;
  margin: 24px 0 32px;
  box-shadow: var(--card-shadow);
}}
.card-img-wrap {{
  border-radius: 6px;
  overflow: hidden;
  background: #000;
  display: flex;
  justify-content: center;
}}
.sankey-img {{
  width: 100%;
  height: auto;
  display: block;
}}
.card-actions {{
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid var(--rule);
}}
.action-btn {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 5px;
  font-family: "Inter", sans-serif;
  font-size: 12.5px;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.12s ease;
}}
.btn-interactive {{
  background: var(--accent);
  color: #fff;
}}
.btn-interactive:hover {{
  opacity: 0.9;
  transform: translateY(-1px);
}}
.btn-download {{
  background: var(--panel-alt);
  color: var(--ink-2);
  border: 1px solid var(--rule-2);
}}
.btn-download:hover {{
  color: var(--ink);
  background: var(--rule);
}}
.tbl-wrap {{
  width: 100%;
  overflow-x: auto;
  margin: 20px 0 28px;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-radius: 6px;
  box-shadow: var(--card-shadow);
}}
table.fin-tbl {{
  width: 100%;
  border-collapse: collapse;
  font-family: "IBM Plex Mono", sans-serif;
  font-size: 13px;
}}
table.fin-tbl th, table.fin-tbl td {{
  padding: 10px 14px;
  border-bottom: 1px solid var(--rule);
  text-align: left;
}}
table.fin-tbl thead th {{
  background: var(--panel-alt);
  color: var(--ink-3);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 600;
}}
table.fin-tbl td.n {{
  text-align: right;
  font-variant-numeric: tabular-nums;
}}
table.fin-tbl tr:last-child td {{
  border-bottom: none;
}}
table.fin-tbl tr:hover {{
  background: var(--panel-alt);
}}
.insight-card {{
  display: flex;
  gap: 16px;
  background: var(--panel);
  border: 1px solid var(--rule);
  border-left: 3px solid var(--success);
  border-radius: 0 6px 6px 0;
  padding: 16px 20px;
  margin: 14px 0;
  box-shadow: var(--card-shadow);
}}
.insight-num {{
  font-family: "IBM Plex Mono", monospace;
  font-size: 15px;
  font-weight: 700;
  color: var(--success);
  flex-shrink: 0;
}}
.insight-content {{
  font-size: 14.5px;
  line-height: 1.7;
  color: var(--ink);
}}
li.list-item {{
  margin: 6px 0 6px 24px;
  font-size: 14.5px;
}}
li.sub-item {{
  margin: 4px 0 4px 44px;
  font-size: 13.5px;
  color: var(--ink-2);
}}
p.prose {{
  margin-bottom: 14px;
  text-align: justify;
}}
footer.rep-footer {{
  border-top: 1px solid var(--rule);
  margin-top: 60px;
  padding-top: 24px;
  text-align: center;
  font-family: "IBM Plex Mono", monospace;
  font-size: 12px;
  color: var(--ink-3);
}}
</style>
</head>
<body>

<div class="container">
  <header class="rep-header">
    <div class="tag-bar">
      <span class="tag-pill">Earnings Visual Breakdown</span>
      <span class="tag-ticker">{ticker} · Form 10-Q & 10-K SEC EDGAR</span>
    </div>
    <h1 class="main-title">{title}</h1>
  </header>

  <main>
{body_content}
  </main>

  <footer class="rep-footer">
    SEC EDGAR Financial Flowchart & Infographics · Pensieve Investment Analysis Ser.
  </footer>
</div>

</body>
</html>
"""


def process_ticker_folder(ticker_dir, dest_dir, clean=True):
    ticker = os.path.basename(ticker_dir.rstrip("/"))
    print(f"==> [{ticker}] 처리 시작...")
    
    # 1. 마크다운 파일 찾기
    md_files = [f for f in os.listdir(ticker_dir) if f.endswith(".md")]
    if not md_files:
        print(f"    [SKIP] 마크다운(.md) 파일 없음 — {ticker_dir}")
        return None
        
    md_file = md_files[0]
    md_path = os.path.join(ticker_dir, md_file)
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    # 2. 에셋 격리 폴더 생성 및 복사 (reports/Invest/assets/<TICKER>/)
    asset_dest_dir = os.path.join(dest_dir, "assets", ticker)
    os.makedirs(asset_dest_dir, exist_ok=True)
    
    copied_assets = []
    for f in os.listdir(ticker_dir):
        if f.endswith((".png", ".html", ".svg")) and f != md_file:
            src_f = os.path.join(ticker_dir, f)
            dst_f = os.path.join(asset_dest_dir, f)
            shutil.copy2(src_f, dst_f)
            copied_assets.append(f)
    print(f"    - 에셋 {len(copied_assets)}개 복사 완료 -> reports/Invest/assets/{ticker}/")

    # 3. HTML 변환 및 빌드
    title, body_html = md_to_html_body(md_text, ticker)
    full_html = build_full_html(title, body_html, ticker)
    
    # 출력 파일명 결정
    base_slug = md_file.replace(".md", "")
    base_slug = re.sub(r"_(visual_)?financial_breakdown$", "", base_slug)
    base_slug = re.sub(r"_(visual_)?breakdown$", "", base_slug)
    slug = f"{base_slug}_financial_breakdown.html"
    out_html_path = os.path.join(dest_dir, slug)
    
    with open(out_html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"    - 메인 보고서 생성 완료 -> {out_html_path}")

    # 4. 요약문 생성 및 등록 (summaries.json)
    rel_path = f"reports/Invest/{slug}"
    file_hash = compute_sha1(out_html_path)
    
    m_rev = re.search(r"총 매출액 \(Total Revenue\).*?\|.*?\| (.*?) \|", md_text)
    m_inc = re.search(r"당기순이익 \(Net Income\).*?순이익률 \*\*(.*?)\*\*", md_text)
    
    summary_text = f"{title} 보고서다. SEC Form 10-Q 및 10-K 공식 공시 데이터를 기반으로 부문별 매출 구조와 손익 흐름을 App Economy Insights 스타일 Sankey 다이어그램 및 정량 표로 종합 정리했다."
    if m_rev and m_inc:
        summary_text = f"{title} 보고서다. SEC Form 10-Q 및 10-K 공식 공시 데이터를 기반으로 최신 분기 총매출({m_rev.group(1).strip()})과 순이익률({m_inc.group(1).strip()}) 등 손익 흐름을 Sankey 인포그래픽과 부문별 데이터로 분석했다."
        
    summaries = load_summaries()
    summaries[rel_path] = {
        "hash": file_hash,
        "summary": summary_text
    }
    save_summaries(summaries)
    print(f"    - 요약문 등록 완료 -> reports/summaries.json")

    # 5. 임시 파일 정리
    if clean:
        shutil.rmtree(ticker_dir)
        print(f"    - 임시 폴더 삭제 완료 -> {ticker_dir}")

    return rel_path


def main():
    parser = argparse.ArgumentParser(description="재무 인포그래픽 보고서 배포 관리 도구")
    parser.add_argument("--src", default=DEFAULT_SRC, help="입력 staging 폴더 (기본: tmp/output)")
    parser.add_argument("--dest", default=DEFAULT_DEST, help="출력 reports 폴더 (기본: reports/Invest)")
    parser.add_argument("--ticker", nargs="*", help="특정 티커만 처리 (생략 시 src 내 전체 처리)")
    parser.add_argument("--no-clean", action="store_true", help="배포 후 staging 임시 폴더 유지")
    args = parser.parse_args()

    if not os.path.exists(args.src):
        print(f"ERROR: 소스 폴더가 존재하지 않습니다: {args.src}")
        return 1

    os.makedirs(args.dest, exist_ok=True)

    subdirs = []
    if args.ticker:
        for t in args.ticker:
            p = os.path.join(args.src, t)
            if os.path.isdir(p):
                subdirs.append(p)
            else:
                print(f"경고: 티커 폴더 없음 - {p}")
    else:
        for item in sorted(os.listdir(args.src)):
            p = os.path.join(args.src, item)
            if os.path.isdir(p):
                subdirs.append(p)

    if not subdirs:
        print(f"처리할 보고서 폴더가 없습니다: {args.src}")
        return 0

    published = []
    for sdir in subdirs:
        res = process_ticker_folder(sdir, args.dest, clean=not args.no_clean)
        if res:
            published.append(res)

    # manifest.json 자동 갱신
    if published:
        print("\n==> manifest.json 재생성 중...")
        subprocess.run([sys.executable, MANIFEST_SCRIPT], cwd=REPO_ROOT, check=True)
        print(f"\n총 {len(published)}개 보고서 배포 및 정리가 완료되었습니다.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
