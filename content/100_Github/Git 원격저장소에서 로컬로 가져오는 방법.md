---
tags:
  - github
  - 깃헙
date: 2026-04-07
---
# 로컬로 가져오는 방법은 3가지
1. `git pull`
2. `git fetch`
3. `git clone

## git pull
원격저장소에 있는 프로젝트의 변경사항을 그대로 가져와서(fetch), 자동으로 병합(merge).
> **자동**으로 병합하기 때문에 무엇이 추가되고 병합되었는지 확인 불가
```bash
#예시
git pull
#로컬에 git을 설정해둔 상태라면 보통, origin = 원격, master = 로컬
git pull origin master
```
## git fetch
나중에 merge할때 수정한 부분을 확인하고 병합할 수 있음

## git clone
문자 그대로 가져와서 복사하기
```bash
#예시
git clone https://github.com/amatoroi-kins/Pb-210.git
```