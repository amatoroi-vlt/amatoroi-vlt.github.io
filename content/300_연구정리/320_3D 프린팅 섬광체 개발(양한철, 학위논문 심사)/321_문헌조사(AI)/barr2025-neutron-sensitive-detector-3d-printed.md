---
title: "A Neutron Sensitive Detector Using 3D-Printed Scintillators"
authors: ["Barr, A.", "Da Vià, C.", "Binte Shawkat, M. T.", "Taylor, M. J.", "Watts, S.", "Allison, J.", "D'Amen, G.", "Gao, T."]
year: 2025
venue: "arXiv"
doi: ""
arxiv: "2507.08663"
paper_id: "barr2025-neutron-sensitive-detector-3d-printed"
source_pdf: "[[108_2507.08663v3.pdf]]"
tags: [paper, paper/reviewed, topic/scintillator, topic/3d-printing, topic/neutron-detection]
aliases: ["Barr 2025"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Barr et al. (2025) — A Neutron Sensitive Detector Using 3D-Printed Scintillators

**Venue**: arXiv
**arXiv**: [2507.08663](https://arxiv.org/abs/2507.08663)
**PDF**: ![[108_2507.08663v3.pdf#page=1]]

---

## Executive Summary

이 연구는 FDM(Fused-Deposition Modelling) 방식의 적층 제조를 이용한 새로운 중성자 민감형 플라스틱 신틸레이션 검출기 제작 및 성능 평가를 보고한다 [[108_2507.08663v3.pdf#page=1|p.1, §Abstract]]. 중성자 민감도를 확보하기 위해 폴리스티렌 베이스에 PTP와 POPOP 형광체를 첨가하고 6LiF 분말을 농축시킨 필라멘트를 자체 제작하였다 [[108_2507.08663v3.pdf#page=5|p.5, §4.1]]. 제작된 신틸레이터는 TimePix3 카메라와 결합되어 높은 공간 및 시간 분해능을 제공하며, 이벤트 판별 알고리즘을 통해 감마선 배경 신호로부터 중성자 신호를 효과적으로 분리해냈다 [[108_2507.08663v3.pdf#page=7|p.7, §4.3]]. 실험 결과, 6LiF가 충진된 공동(cavity) 구조를 가진 신틸레이터가 일반적인 입체 구조보다 중성자 검출 효율이 약 2배 높음을 확인하였다 [[108_2507.08663v3.pdf#page=9|p.9, §5]].

---

## Problem & Motivation

기존의 플라스틱 신틸레이터 제작 방식인 주조(casting)나 가공(machining)은 복잡한 기하학적 구조를 구현하기 어렵고 비용이 많이 든다 [[108_2507.08663v3.pdf#page=2|p.2, §1]]. 특히 중성자 검출은 핵 안보 및 법의학 분야에서 중요하지만, 복잡한 검출기 시스템 요구사항을 충족하기 위한 유연한 제작 기술이 필요하다 [[108_2507.08663v3.pdf#page=1|p.1, §1]]. 3D 프린팅 기술은 저렴한 비용으로 맞춤형 형상과 복잡한 내부 구조를 가진 신틸레이터를 제작할 수 있는 대안을 제공한다 [[108_2507.08663v3.pdf#page=3|p.3, §2.2]].

---

## Methods

본 연구에서는 FDM 방식에 적합한 신틸레이팅 필라멘트를 생산하기 위해 폴리스티렌(PS)을 베이스로 PTP(primary fluorophore)와 POPOP(secondary fluorophore)를 혼합하였다 [[108_2507.08663v3.pdf#page=5|p.5, §4.1]]. 중성자 반응성을 위해 6LiF 분말을 필라멘트 무게의 7.5% 비율로 첨가하였다 [[108_2507.08663v3.pdf#page=5|p.5, §4.1]]. 3D 프린팅은 Prusa i3 프린터를 사용하여 100% infill, 0.05 mm 층 높이, 255°C 노즐 온도로 수행되었다 [[108_2507.08663v3.pdf#page=5|p.5, §4.2]]. 검출기 시스템은 TimePix3 기반의 TPX3Cam과 Cricket 이미지 강화기(image intensifier)를 결합하여 구성되었다 [[108_2507.08663v3.pdf#page=7|p.7, §4.3]].

---

## Results

제작된 3D 프린팅 신틸레이터의 광출력은 MeV당 30 ± 5 photons로 측정되었다 [[108_2507.08663v3.pdf#page=5|p.5, §4.1]]. 252Cf 선원을 이용한 성능 테스트에서 클러스터 크기와 에너지를 기반으로 중성자와 감마선 신호를 명확히 구분할 수 있음을 입증하였다 [[108_2507.08663v3.pdf#page=10|p.10, §5.1]]. 특히 6LiF 분말이 채워진 공동 구조(2 x 2 x 1 cm)를 가진 검출기는 동일 크기의 일반 입체 구조보다 약 2배 높은 중성자 검출 감도를 보였다 [[108_2507.08663v3.pdf#page=9|p.9, §5]]. Geant4 시뮬레이션 결과와 실험 데이터가 잘 일치함을 확인하였다 [[108_2507.08663v3.pdf#page=14|p.14, §6]].

---

## Critical Review

### 방법론·실험설계 타당성

FDM 방식에서 흔히 발생하는 기포(gas bubbles) 문제를 해결하기 위해 100% infill과 고온 출력을 채택하여 투명도를 확보한 점이 우수하다 [[108_2507.08663v3.pdf#page=6|p.6, §4.2]]. 그러나 필라멘트 제조 과정에서 6LiF 분말의 균일한 분산 여부에 대한 구체적인 분석이 부족하며, 이는 검출 효율의 불확실성을 초래할 수 있다. TimePix3 카메라를 이용한 판별 알고리즘은 효과적이지만, 대면적 검출기로 확장 시의 데이터 처리 부하에 대한 고려가 필요하다.

### 선행연구 대비 기여도·한계

Berns 등(2020)의 선행 연구를 확장하여 6LiF를 이용한 중성자 민감성을 성공적으로 구현한 점이 주요 기여이다 [[108_2507.08663v3.pdf#page=3|p.3, §2.2]]. 기존의 주조 방식 대비 제작 유연성을 확보했음에도 불구하고, 여전히 상용 신틸레이터(EJ-200 등) 대비 광출력이 낮다는 점(30 photons/MeV vs 수천 photons/MeV)은 실용화의 한계로 남는다 [[108_2507.08663v3.pdf#page=9|p.9, §5]].

---

## Implications for Our Research

FDM 기반의 필라멘트 제작 기술은 맞춤형 선량계나 복잡한 형상의 중성자 검출기 연구에 직접적으로 활용 가능하다. 특히 공동 구조를 통한 감도 향상 기법은 검출기 설계 최적화에 중요한 참고 자료가 된다. 향후 연구에서는 광출력을 높이기 위한 형광체 농도 최적화 및 페로브스카이트와 같은 신소재 도입을 고려할 필요가 있다 [[108_2507.08663v3.pdf#page=14|p.14, §6]].

---

## References

- [1] M.G. Schorr and F.L. Torney, Phys. Rev. 80 (1950) 474.
- [2] M. Hamel, Plastic Scintillators: Chemistry and Applications, Springer, 2021.
- [3] Y. Abreu et al., J. Inst. 13 (2018) P05005.
- [15] Y. Yoshimura et al., Nucl. Instrum. Meth. A 406 (1998) 435.
- [24] S. Berns et al., J. Inst. 15 (2020) P10019.
- [26] T. Sibilieva et al., J. Inst. 18 (2023) P03007.
- [32] N. Zaitseva et al., Nucl. Instrum. Meth. A 729 (2013) 747.
- [36] Prusa Research a.s., Original Prusa i3 MK3, 2025.
- [44] Eljen Technology, EJ-270, 2025.
