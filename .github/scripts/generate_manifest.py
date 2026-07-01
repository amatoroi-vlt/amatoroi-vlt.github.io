#!/usr/bin/env python3
import hashlib, json, os, re, sys, subprocess
from datetime import datetime, timezone

SUMMARIES_PATH = os.path.join('reports', 'summaries.json')

def content_hash(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.sha1(f.read()).hexdigest()

def load_summaries():
    try:
        with open(SUMMARIES_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}

def extract_title(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(3000)
        match = re.search(r'<title[^>]*>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
        if match:
            title = match.group(1).strip()
            if title:
                return title
    except Exception:
        pass
    return None

def get_last_modified(filepath):
    try:
        result = subprocess.run(
            ['git', 'log', '-1', '--format=%cI', '--', filepath],
            capture_output=True, text=True, timeout=5
        )
        date_str = result.stdout.strip()
        if date_str:
            return date_str
    except Exception:
        pass
    try:
        ts = os.path.getmtime(filepath)
        return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()
    except Exception:
        return ''

reports_dir = 'reports'
groups = []
summaries = load_summaries()
missing_summaries = []

if not os.path.exists(reports_dir):
    print('reports/ 폴더가 없습니다')
    sys.exit(0)

for group in sorted(os.listdir(reports_dir)):
    group_path = os.path.join(reports_dir, group)
    if not os.path.isdir(group_path):
        continue
    files = []
    for f in sorted(os.listdir(group_path)):
        if not f.endswith('.html'):
            continue
        filepath = os.path.join(group_path, f)
        path = f'reports/{group}/{f}'
        title = extract_title(filepath) or f.replace('.html', '').replace('_', ' ')
        date = get_last_modified(filepath)
        cached = summaries.get(path)
        h = content_hash(filepath)
        summary = cached['summary'] if cached and cached.get('hash') == h else ''
        if not summary:
            missing_summaries.append(path)
        files.append({'name': title, 'path': path, 'date': date, 'summary': summary})
    files.sort(key=lambda x: x['date'], reverse=True)
    if files:
        groups.append({'name': group, 'files': files})

output = sys.argv[1] if len(sys.argv) > 1 else 'manifest.json'
with open(output, 'w', encoding='utf-8') as out:
    json.dump({'groups': groups}, out, ensure_ascii=False, indent=2)

total = sum(len(g['files']) for g in groups)
print(f'manifest.json 생성 완료: {len(groups)}개 그룹, {total}개 파일')
if missing_summaries:
    print(f'요약 없음 ({len(missing_summaries)}개) — Claude Code에게 "요약 생성해줘" 요청 필요:')
    for p in missing_summaries:
        print(f'  - {p}')
