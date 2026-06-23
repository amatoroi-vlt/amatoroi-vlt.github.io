---
title: "Scintillation dosimetry for FLASH radiotherapy"
authors: ["Ciarrocchi, E.", "Veronese, I."]
year: 2026
venue: "Radiation Measurements"
doi: "10.1016/j.radmeas.2026.107625"
arxiv: ""
paper_id: "ciarrocchi2026-scintillation-dosimetry-flash-radiotherapy"
source_pdf: "[[105_Ciarrocchi_RM_2026_final.pdf]]"
tags: [paper, paper/reviewed, topic/scintillation-dosimetry]
aliases: ["Ciarrocchi 2026"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 1.0
---

# Ciarrocchi et al. (2026) — Scintillation dosimetry for FLASH radiotherapy

**Venue**: Radiation Measurements
**DOI**: [10.1016/j.radmeas.2026.107625](https://doi.org/10.1016/j.radmeas.2026.107625) · **arXiv**: []()
**PDF**: ![[105_Ciarrocchi_RM_2026_final.pdf#page=1]]

---

## Executive Summary

이 논문은 초고선량률(UHDR) 빔을 사용하는 FLASH 방사선 치료(FLASH RT) 환경에서 섬광체 기반 선량계(scintillation dosimeters)의 연구 및 개발 현황을 종합적으로 검토한 리뷰 논문이다 [[105_Ciarrocchi_RM_2026_final.pdf#page=1|p.1, §Abstract]]. FLASH RT는 기존 방사선 치료 대비 정상 조직의 손상을 줄이면서 종양 제어 효과를 유지하는 장점이 있으나, 40 Gy/s 이상의 초고선량률을 측정하기 위한 새로운 선량 측정 기술이 요구된다 [[105_Ciarrocchi_RM_2026_final.pdf#page=1|p.1, §1]]. 섬광체 선량계는 높은 공간 및 시간 분해능, 선량률 선형성, 방사선 등가성 등의 장점을 지녀 FLASH 선량 측정에 유망한 기술로 평가받고 있다 [[105_Ciarrocchi_RM_2026_final.pdf#page=2|p.2, §1]]. 본 리뷰는 유기, 무기 및 하이브리드 섬광체의 특성, 점(point) 및 2차원(2D) 검출기 기하학, 선량률 선형성, 시간 분해능, 방사선 손상(radiation damage) 및 체렌코프 방사선(Cerenkov radiation)과 같은 스퓨리어스 발광(spurious luminescence) 보정 방법 등 핵심적인 측면을 분석한다 [[105_Ciarrocchi_RM_2026_final.pdf#page=2|p.2, §1]].

---

## Problem & Motivation

최근 대두된 FLASH 효과는 100~200 ms 이내의 극히 짧은 시간 동안 40 Gy/s 이상의 초고선량률(UHDR)로 방사선을 조사할 때 정상 조직의 손상을 유의미하게 줄이는 현상이다 [[105_Ciarrocchi_RM_2026_final.pdf#page=1|p.1, §1]]. 이러한 UHDR 빔의 생물학적 상관관계를 규명하고 임상에 안전하게 적용하기 위해서는 빔 파라미터에 대한 표준화되고 정량적인 특성화가 필수적이다 [[105_Ciarrocchi_RM_2026_final.pdf#page=1|p.1, §1]]. 그러나 이온화 챔버(ionization chambers)와 같은 기존의 표준 선량계는 UHDR 빔에 노출될 경우 이온 재결합(ion recombination) 및 포화 효과(saturation effects)로 인해 심각한 한계에 직면한다 [[105_Ciarrocchi_RM_2026_final.pdf#page=2|p.2, §1]]. 따라서 펄스당 선량(DPP) 및 순간 선량률(IDR)과 같은 빔의 시간 구조(time-structure)를 실시간으로 측정할 수 있는 빠르고 정확한 새로운 선량계의 개발이 시급히 요구되며, 섬광체 선량계가 그 대안으로 주목받고 있다 [[105_Ciarrocchi_RM_2026_final.pdf#page=2|p.2, §1]].

---

## Methods

본 연구는 2020년부터 2025년 8월까지 Web of Science 플랫폼에서 "scintillator", "flash", "dosimeter", "radiotherapy" 등의 키워드를 조합하여 문헌 검색을 수행한 체계적 문헌 고찰(systematic review)이다 [[105_Ciarrocchi_RM_2026_final.pdf#page=6|p.6, §3]]. 검색된 69편의 논문 중 스크리닝을 거쳐 51편의 기록을 분석 대상으로 선정하였으며, 이 중 37편은 연구 논문(article), 3편은 프로시딩 논문(proceeding paper), 3편은 리뷰 논문(review article)으로 분류되었다 [[105_Ciarrocchi_RM_2026_final.pdf#page=6|p.6, §3]]. 분석은 주로 점 검출기(point detectors)와 2D 검출기(2D detectors)로 나누어 진행되었으며, 선량 및 선량률에 대한 선형성(linearity), 시간 및 공간 성능(time and spatial performance), 방사선 손상(radiation damage), 그리고 스퓨리어스 발광(spurious luminescence)의 네 가지 주요 기준에 따라 기존 연구 결과들을 종합하고 비교 평가하였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=6|p.6, §3]]. 특히, 유기 섬광체(organic scintillators), 무기 섬광체(inorganic scintillators), 하이브리드 섬광체(hybrid scintillators)의 재료적 특성과 광전자 증폭관(PMT), 광다이오드(PD), 실리콘 광전자 증폭기(SiPM), CCD/CMOS 카메라 등 다양한 판독 시스템(readout systems)의 성능을 교차 분석하였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=3|p.3, §2.3]].

---

## Results

- **선형성 (Linearity):** 유기 섬광체 중 플라스틱 섬광 파이버(예: SCSF-78J, SCSF-3HF)는 약 10 Gy의 펄스당 선량(DPP) 및 2.4 × 10^6 Gy/s의 순간 선량률(IDR)까지 선형적인 응답을 보였으며, 무기 섬광체(예: Yb-admixed YAG, ZnS:Ag)는 최대 1.5 × 10^6 Gy/s의 IDR까지 선형성을 유지하는 것으로 나타났다 [[105_Ciarrocchi_RM_2026_final.pdf#page=9|p.9, §3.1.1]].
- **시간 및 공간 성능 (Time and spatial performance):** 무기 및 하이브리드 섬광체는 펄스 간 간격이 짧은 UHDR 전자 빔(예: 최대 245 Hz 펄스 반복 주파수)의 단일 펄스를 구별할 수 있는 서브 밀리초(sub-millisecond) 수준의 시간 분해능을 입증하였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=10|p.10, §3.2.1]]. 2D 섬광체 스크린은 양성자 PBS 빔의 시공간적 선량 분포를 밀리미터 이하(sub-millimetric)의 공간 분해능으로 실시간 이미징하는 데 성공하였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=11|p.11, §3.2.2]].
- **방사선 손상 (Radiation damage):** 상용 플라스틱 섬광체(예: BCF-12, Medscint, EJ-212)는 37.2 kGy의 누적 선량 조사 후 초기 발광량의 30~43% 수준으로 신호가 감소하였으며, 손상률은 누적 선량 1.4 kGy ~ 2.1 kGy 구간에서 20% 이상으로 가장 높게 나타났다 [[105_Ciarrocchi_RM_2026_final.pdf#page=13|p.13, §3.3.1]].
- **스퓨리어스 발광 (Spurious luminescence):** 광섬유 기반 점 검출기에서 발생하는 체렌코프 방사선(Cerenkov radiation)을 보정하기 위해 광학 필터링(optical filtering), 스펙트럼 분석(spectral analysis), 이중 파이버 방법(twin-fibre method) 등이 적용되었으며, 2D 스크린의 경우 얇은 두께를 사용하여 체렌코프 기여도를 최소화하거나 스펙트럼 분석을 통해 보정하는 방법이 제안되었다 [[105_Ciarrocchi_RM_2026_final.pdf#page=13|p.13, §3.4.1]].

---

## Critical Review

### 방법론·실험설계 타당성
본 리뷰는 명확한 검색어와 기간(2020-2025)을 설정하여 체계적인 문헌 고찰을 수행하였으므로, 최근 급성장하는 FLASH 선량 측정 분야의 동향을 파악하는 데 매우 적절한 방법론을 취했다 [[105_Ciarrocchi_RM_2026_final.pdf#page=6|p.6, §3]]. 다양한 섬광체 재료(유기, 무기, 하이브리드)와 기하학적 구조(점, 2D)에 따른 성능 지표를 표(Tables 1-4)로 체계적으로 정리하여 비교 분석의 타당성을 높였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=7|p.7, §Table 1]]. 평가자 해석: 다만, 리뷰에 포함된 개별 연구들이 서로 다른 가속기 환경(전자, 양성자, X-선), 빔 파라미터(DPP, IDR, PRF), 그리고 판독 시스템을 사용하였기 때문에, 섬광체 자체의 순수한 성능만을 독립적으로 비교 평가하는 데에는 내재적인 한계가 존재한다. 저자들 역시 이러한 교란 변수(confounding variables)의 영향을 지적하며 표준화된 조사 조건의 필요성을 강조하였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=14|p.14, §4]].

### 선행연구 대비 기여도·한계
기존 리뷰 논문들이 FLASH 방사선 치료 전반이나 다양한 선량계 기술을 포괄적으로 다루었던 반면, 본 연구는 '섬광체 기반 선량계(scintillation dosimeters)'에만 초점을 맞추어 재료 특성부터 임상 적용 가능성까지 심층적으로 분석했다는 점에서 독창적인 기여를 한다 [[105_Ciarrocchi_RM_2026_final.pdf#page=2|p.2, §1]]. 저자들은 3D 선량 측정(3D dosimetry) 분야의 연구가 아직 초기 단계에 머물러 있으며, 방사선 손상(radiation damage)에 대한 데이터가 주로 유기 섬광체에 편중되어 무기 및 하이브리드 섬광체에 대한 장기적인 내방사선성 연구가 부족하다는 점을 명확한 한계로 지적하였다 [[105_Ciarrocchi_RM_2026_final.pdf#page=14|p.14, §4]]. 평가자 해석: 체렌코프 방사선 보정 기술과 관련하여, 기존 CONV RT에서 사용되던 방법들이 UHDR 환경에서도 유효한지에 대한 실험적 검증 데이터가 아직 충분하지 않다는 점이 추가적인 한계로 식별된다. 특히, 고선량률로 인한 광섬유의 굴절률 변화나 투과도 저하가 보정 알고리즘에 미치는 동적 영향에 대한 심도 있는 논의가 향후 요구된다.

---

## Implications for Our Research

이 리뷰는 FLASH 방사선 치료 환경에서 실시간 선량 모니터링 시스템을 구축하고자 하는 우리 연구에 중요한 가이드라인을 제공한다. 특히, 서브 밀리초 수준의 시간 분해능이 요구되는 펄스 빔 환경에서는 감쇠 시간(decay time)이 짧은 유기 섬광체나 특정 무기 섬광체(예: YAG:Ce)의 도입을 우선적으로 고려해야 함을 시사한다. 방사선 손상으로 인한 민감도 저하 문제가 심각하므로, 장기적인 안정성이 요구되는 임상 환경 적용을 위해서는 내방사선성이 우수한 무기 섬광체 기반의 2D 스크린 개발이나, 실시간 자가 보정(self-calibration) 알고리즘을 통합한 하이브리드 판독 시스템 설계가 필수적인 연구 방향이 될 것이다.

---

## References

- [1] Anand, A., Zaffalon, M.L., Erroi, A., Cova, F., Carulli, F., Brovelli, S., 2024. Advances in perovskite nanocrystals and nanocomposites for scintillation applications. ACS Energy Lett. 9 (3), 1261–1287.
- [2] Ashraf, M.R., Rahman, M., Cao, X., Duval, K., Williams, B.B., Jack Hoopes, P., Gladstone, D.J., Pogue, B.W., Zhang, R., Bruza, P., 2022. Individual pulse monitoring and dose control system for pre-clinical implementation of FLASH-RT. Phys. Med. Biol. 67 (9).
- [3] Beddar, A.S., Beaulieu, L. (Eds.), 2016. Scintillation Dosimetry, first ed. CRC Press.
- [4] Ciarrocchi, E., Belcari, N., 2017. Cerenkov luminescence imaging: physics principles and potential applications in biomedical sciences. EJNMMI Phys. 4 (1).
- [5] Favaudon, V., Caplier, L., Monceau, V., Pouzoulet, F., Sayarath, M., Fouillade, C., Poupon, M.-F., Brito, I., Hupé, P., Bourhis, J., Hall, J., Fontaine, J.-J., Vozenin, M.-C., 2014. Ultrahigh dose-rate FLASH irradiation increases the differential response between normal and tumor tissue in mice. Sci. Transl. Med. 6 (245), 245ra93.