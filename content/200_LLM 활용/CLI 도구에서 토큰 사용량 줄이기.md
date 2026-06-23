---
tags:
  - claude_code
  - gemini-cli
  - "#rtk-ai"
---
[rtk-ai](https://github.com/rtk-ai/rtk)는 각종 명령어 `git`, `cat` 등을 사용할 때 *hook* 해서 불필요한 주석 등을 제거한 뒤 agent에게 전달

> (예) `git` 대신 `rtk git`을 쓰는 방식

설치 후 전역 설정하고, 필요하면 `claude.md`나 `gemini.md`에 실행 규정을 삽입하면 효과적으로 활용 가능하다고 함.

```bash
# 토큰 절감량 확인
rtk gain
```