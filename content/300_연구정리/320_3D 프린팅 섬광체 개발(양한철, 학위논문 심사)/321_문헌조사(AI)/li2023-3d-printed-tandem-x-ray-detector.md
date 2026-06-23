---
title: "3D Printed tandem X-Ray detector with halide perovskite-polymer composite semiconductor absorber"
authors: ["Li, H.", "Shan, X.", "Bao, S.", "Psulkowski, S.", "Guo, W.", "Dickens, T.", "Yu, Z."]
year: 2023
venue: "Adv. Manuf."
doi: "10.55092/am20230002"
arxiv: "2403.03142"
paper_id: "li2023-3d-printed-tandem-x-ray-detector"
source_pdf: "[[122_2023_3D Printed Tandem.pdf]]"
tags: [paper, paper/reviewed, topic/perovskite-detector, topic/3d-printing, topic/tandem-detector]
aliases: ["Li 2023"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Li et al. (2023) — 3D Printed tandem X-Ray detector with halide perovskite-polymer composite semiconductor absorber

**Venue**: Adv. Manuf.
**DOI**: [10.55092/am20230002](https://doi.org/10.55092/am20230002) · **arXiv**: [2403.03142](https://arxiv.org/abs/2403.03142)
**PDF**: ![[122_2023_3D Printed Tandem.pdf#page=1]]

---

## Executive Summary

본 연구는 CsPbBr₃ 할라이드 페로브스카이트 결정과 PLA(Polylactic Acid) 매트릭스를 혼합한 반도체-고분자 복합체를 이용한 3D 프린팅 탄뎀(tandem) X선 검출기를 제안한다 [[122_2023_3D Printed Tandem.pdf#page=1|p.1]]. 4개 층(총 두께 600 µm)으로 구성된 탄뎀 검출기는 383 µC Gy_air⁻¹ cm⁻²의 민감도를 달성하였으며, 이는 동일 두께의 단일 층 검출기 대비 23배 향상된 결과이다 [[122_2023_3D Printed Tandem.pdf#page=1|p.1, p.10]]. 이 구조는 기존 단일 층 검출기의 X선 흡수량과 전하 수집 효율 사이의 상충 관계(trade-off)를 효과적으로 극복할 수 있음을 입증하였다 [[122_2023_3D Printed Tandem.pdf#page=2|p.2]].

---

## Problem & Motivation

단일 반도체 흡수층을 사용하는 X선 검출기에서는 효과적인 X선 흡수를 위해 두꺼운 층이 필요하지만, 이는 전하 운반체의 이동 거리를 늘려 수집 효율을 저하시키고 민감도를 떨어뜨리는 딜레마를 초래한다 [[122_2023_3D Printed Tandem.pdf#page=2|p.2]]. 셀레늄(Se)이나 카드뮴 텔루라이드(CdTe)와 같은 기존 소재는 고진공 또는 고온 공정이 필요하여 대면적 다층 구조 제작에 한계가 있다 [[122_2023_3D Printed Tandem.pdf#page=2|p.2]]. 할라이드 페로브스카이트는 뛰어난 저지능과 전하 운반체 수송 특성을 가지며 용액 공정이 가능하여 이러한 문제를 해결할 유망한 대안으로 주목받고 있다 [[122_2023_3D Printed Tandem.pdf#page=2|p.2]].

---

## Methods

- **소재**: CsBr과 PbBr₂를 2:1 몰 비로 혼합하여 CsPbBr₃ 결정을 합성하고, 이를 PLA 수지와 혼합하여 복합 필라멘트를 제작하였다 [[122_2023_3D Printed Tandem.pdf#page=3|p.3]]. 페로브스카이트와 PLA의 중량비는 2:1(부피비 약 34.8%)로 설정되었다 [[122_2023_3D Printed Tandem.pdf#page=4|p.4-5]].
- **제조**: 상용 3D 프린터(LulzBot TAZ 6)를 사용하여 융합 퇴적 모델링(FDM) 방식으로 흡수층을 출력하였다 [[122_2023_3D Printed Tandem.pdf#page=4|p.4, p.10]]. 전극 단자에는 전도성 PLA 필라멘트(PROTOPASTA CDP12805)를 사용하였다 [[122_2023_3D Printed Tandem.pdf#page=10|p.10]].
- **탄뎀 구조**: 여러 개의 반도체 흡수층과 전하 수집 단자를 수직으로 쌓고 병렬로 연결한 구조를 설계하여, 각 층에서 생성된 전하가 짧은 거리만 이동해도 수집될 수 있도록 하였다 [[122_2023_3D Printed Tandem.pdf#page=2|p.2, p.10]].
- **측정**: 표준 미세 초점 구리 X선 튜브를 사용하여 검출 특성을 분석하였으며, 인가 전압에 따른 광전류 변화를 측정하였다 [[122_2023_3D Printed Tandem.pdf#page=3|p.3]].

---

## Results

- **탄뎀 층수별 민감도**: 90V 편향 전압에서 1개 층(216 µC Gy_air⁻¹ cm⁻²), 2개 층(326), 3개 층(367), 4개 층(383)으로 층수가 증가함에 따라 민감도가 일관되게 향상되었다 [[122_2023_3D Printed Tandem.pdf#page=12|p.12]].
- **단일 층 대비 성능**: 총 두께 600 µm인 4개 층 탄뎀 검출기의 광전류(52.9 nA·mm⁻²)는 동일 두께의 단일 층 검출기(2.3 nA·mm⁻²)보다 약 23배 높게 나타났다 [[122_2023_3D Printed Tandem.pdf#page=10|p.10]].
- **기계적 특성**: 2:1 비율의 CsPbBr₃-PLA 복합체는 인장 강도 66 MPa, 파단 신율 3.4%를 보여 3D 프린팅 공정에 적합한 기계적 내구성을 확인하였다 [[122_2023_3D Printed Tandem.pdf#page=4|p.4]].
- **시간 응답**: X선 조사 시 약 5-10초 이내에 최종 변화량의 75% 이상에 도달하는 안정적인 과도 응답 특성을 보였다 [[122_2023_3D Printed Tandem.pdf#page=12|p.12, Fig 5f]].

---

## Critical Review

### 방법론·실험설계 타당성

- XRD와 SEM을 통해 복합체 내 페로브스카이트 결정의 균일한 분포와 결정성을 성공적으로 입증하였다 [[122_2023_3D Printed Tandem.pdf#page=4|p.4, Fig 1-2]].
- 탄뎀 구조의 이점을 시뮬레이션(식 2)과 실험 데이터(그림 5e)를 통해 직접 비교 검증하여 논리적 타당성을 확보하였다 [[122_2023_3D Printed Tandem.pdf#page=10|p.10]].
- 다만, 시간 응답 곡선(Fig 5f)에서 나타나는 느린 상승 및 하강 시간은 페로브스카이트-PLA 계면의 전하 트래핑 효과 때문으로 분석되며, 이는 향후 고속 이미징 응용을 위해 개선이 필요한 지점이다 [[122_2023_3D Printed Tandem.pdf#page=12|p.12]].

### 선행연구 대비 기여도·한계

- 기존의 고가 진공 공정 대신 저비용 FDM 3D 프린팅을 사용하여 탄뎀 구조의 X선 검출기를 제작한 점이 독창적이다 [[122_2023_3D Printed Tandem.pdf#page=2|p.2]].
- 본 연구는 4개 층까지만 실험하였으나, 이론적으로는 더 많은 층을 쌓아 성능을 극대화할 수 있는 확장성을 제시하였다 [[122_2023_3D Printed Tandem.pdf#page=10|p.10]].
- 한계점으로는 페로브스카이트의 함량이 높아질수록 필라멘트가 취약(brittle)해져 프린팅이 어려워지는 문제가 있으며, 이로 인해 페로브스카이트 부피비를 34.8% 이상으로 높이지 못한 점이 언급되었다 [[122_2023_3D Printed Tandem.pdf#page=4|p.4]].

---

## Implications for Our Research

- 3D 프린팅을 통한 다층 구조(tandem) 구현 방식은 우리 프로젝트의 섬광체 기반 도지미터 설계 시 흡수 효율과 신호 수집 간의 상충 문제를 해결하는 데 중요한 힌트를 제공한다.
- 특히 전도성 필라멘트를 이용한 전극 일체형 출력 방식은 환자 맞춤형 팬텀 내부에 검출기를 직접 매립하는 복합 구조 제작에 응용 가능하다.

---

## References

- [1] Yaffe MJ, Rowlands JA. (1997). X-ray detectors for digital radiography. Phys Med Biol, 42(1):1-39.
- [2] Kim BJ, et al. (2007). A study on spatial resolution of pixelated CsI(Tl) scintillator. Nucl Instrum Meth A, 579(1):205-207.
- [5] Redus R, et al. (2004). Multielement CdTe stack detectors for gamma-ray spectroscopy. IEEE T Nucl Sci, 51(5):2386-2394.
- [10] Li JQ, et al. (2015). Single-layer light-emitting diodes using organometal halide perovskite/poly(ethylene oxide) composite thin films. Adv Mater, 27(35):5196-5202.
- [14] Loke G, et al. (2019). Structured multimaterial filaments for 3D printing of optoelectronics. Nat Commun, 10:4010.
- [19] Li X, et al. (2019). All-inorganic CsPbBr3 perovskite solar cells with 10.45% efficiency by evaporation-assisted deposition and setting intermediate energy levels. ACS Appl Mater Inter, 11(33):29746-29752.
- [21] Barrasa JO, et al. (2021). Characterisation and modelling of PLA filaments and 3D printed specimens. Polymers-Basel, 13(17):2899.
