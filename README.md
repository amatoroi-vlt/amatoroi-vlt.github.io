# Pensieve

> 햇빛이여, 데이지여, 버터 멜로우여, 이 멍청한 인간이 기억하게 해라.

Claude 등으로 생성한 HTML 보고서를 그룹별로 보관하고 열람하는 개인 아카이브.

🔗 https://amatoroi-vlt.github.io

---

## 디렉토리 구조

```
/
├── index.html                  # 사이드바 + 뷰어 메인 페이지
├── reports/
│   └── 그룹이름/               # 폴더명 = 사이드바 그룹 제목
│       └── 보고서.html
├── manifest.json               # GitHub Actions가 자동 생성 (수동 편집 불필요)
├── .github/
│   ├── scripts/
│   │   └── generate_manifest.py
│   └── workflows/
│       └── deploy.yml
└── README.md
```

---

## 보고서 추가하기

1. `reports/그룹이름/` 폴더에 HTML 파일 넣기
2. 푸시

```bash
cp 보고서.html reports/연구분석/
git add reports/연구분석/보고서.html
git commit -m "add: 보고서 제목"
git push
```

GitHub Actions가 자동으로 `manifest.json`을 생성하고 배포합니다 (약 2분 소요).

---

## 그룹 추가하기

`reports/` 아래에 새 폴더를 만들면 사이드바에 자동으로 그룹이 추가됩니다.

```bash
mkdir reports/새그룹이름
```

그룹은 폴더명 알파벳 순으로 정렬됩니다.

---

## 현재 그룹

| 그룹 | 설명 |
|------|------|
| 연구분석 | 연구 및 데이터 분석 보고서 |

---

## 사이드바 표시 이름

HTML 파일의 `<title>` 태그 내용이 사이드바에 표시됩니다.
`<title>`이 없으면 파일명(밑줄 → 공백)으로 표시됩니다.

---

## 로컬 미리보기

```bash
npx serve .
# → http://localhost:3000
```

로컬에서 목록까지 보려면 먼저 manifest.json 생성:

```bash
python3 .github/scripts/generate_manifest.py
```
