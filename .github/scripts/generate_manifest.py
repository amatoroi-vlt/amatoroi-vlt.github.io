#!/usr/bin/env python3
import json, os, re, sys

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

reports_dir = 'reports'
groups = []

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
        title = extract_title(filepath) or f.replace('.html', '').replace('_', ' ')
        files.append({'name': title, 'path': f'reports/{group}/{f}'})
    if files:
        groups.append({'name': group, 'files': files})

output = sys.argv[1] if len(sys.argv) > 1 else 'manifest.json'
with open(output, 'w', encoding='utf-8') as out:
    json.dump({'groups': groups}, out, ensure_ascii=False, indent=2)

total = sum(len(g['files']) for g in groups)
print(f'manifest.json 생성 완료: {len(groups)}개 그룹, {total}개 파일')
