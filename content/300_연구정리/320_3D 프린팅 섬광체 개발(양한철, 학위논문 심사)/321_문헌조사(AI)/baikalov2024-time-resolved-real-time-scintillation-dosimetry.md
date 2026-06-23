---
title: "Characterization of a novel time-resolved, real-time scintillation dosimetry system for ultra-high dose rate radiation therapy applications"
authors: ["Baikalov, A.", "Tho, D.", "Liu, K.", "Bartzsch, S.", "Beddar, S.", "Schüler, E."]
year: 2024
venue: "International Journal of Radiation Oncology * Biology * Physics"
doi: "10.1016/j.ijrobp.2024.11.092"
arxiv: "2403.03142"
paper_id: "baikalov2024-time-resolved-real-time-scintillation-dosimetry"
source_pdf: "[[120_nihpp-2403.03142v1.pdf]]"
tags: [paper, paper/reviewed, topic/scintillation-dosimetry, topic/flash-rt, topic/uhdr]
aliases: ["Baikalov 2024"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Baikalov et al. (2024) — Characterization of a novel time-resolved, real-time scintillation dosimetry system for ultra-high dose rate radiation therapy applications

**Venue**: International Journal of Radiation Oncology * Biology * Physics
**DOI**: [10.1016/j.ijrobp.2024.11.092](https://doi.org/10.1016/j.ijrobp.2024.11.092) · **arXiv**: [2403.03142](https://arxiv.org/abs/2403.03142)
**PDF**: ![[120_nihpp-2403.03142v1.pdf#page=1]]

---

## Executive Summary

본 연구는 FLASH 방사선 치료(RT)에서 요구되는 초고선량률(UHDR) 환경에 최적화된 새로운 시간 분해능 기반의 실시간 섬광 선량계 시스템을 평가하였다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §Abstract]]. 개발된 시스템은 최대 1341 Gy/s의 평균 선량률과 7.68 Gy의 펄스당 선량 범위 내에서 +/- 3% 이내의 우수한 선형성을 보였다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §Abstract]]. 특히 최대 120 Hz의 주파수로 전달되는 개별 펄스의 선량을 정확하게 측정할 수 있음을 입증하였다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §Abstract]]. 이를 통해 FLASH-RT의 정밀한 선량 검증을 위한 실시간 밀리초 단위의 측정이 가능해졌다 [[120_nihpp-2403.03142v1.pdf#page=13|p.13, §Conclusions]].

---

## Problem & Motivation

기존의 방사선 선량계들은 FLASH-RT에서 사용되는 초고선량률(UHDR) 환경에서 높은 입자 플럭스로 인해 신호 포화(saturation) 현상을 겪으며 신뢰도가 급격히 떨어진다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §1]]. 특히 100 Gy/s 이상의 평균 선량률($\overline{DR}$)과 1.5 Gy를 초과하는 펄스당 선량($D_p$) 환경에서 호환성을 유지하는 시스템이 부족한 상황이다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §Abstract]]. 따라서 UHDR 전자 빔라인의 펄스 형태와 선량을 실시간으로 추적할 수 있는 높은 시간 분해능을 가진 새로운 선량계의 개발과 검증이 필수적이다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §1]].

---

## Methods

본 연구에서는 MedScint 사의 Hyperscnt RP-FLASH 프로토타입 섬광 선량계를 사용하였다. 이 시스템은 직경 1mm, 길이 3mm의 원통형 유기 섬광체 프로브와 스펙트로미터를 광섬유로 연결한 구조이다 [[120_nihpp-2403.03142v1.pdf#page=3|p.3, §Methods]]. 실험은 MD Anderson 암센터의 Mobetron(9 MeV 전자선 가속기)에서 수행되었으며, 물-등가 보루스 재질 사이에 프로브를 위치시켜 측정하였다 [[120_nihpp-2403.03142v1.pdf#page=4|p.4, §Measurement Setup]]. 주요 파라미터로는 샘플링 주파수($f_s$)를 최대 1000 Hz까지 설정하여 시간 분해능을 확보하였다 [[120_nihpp-2403.03142v1.pdf#page=4|p.4, §Measurement Setup]].

---

## Results

1. **선량 선형성 및 독립성**: 시스템은 1.8-1341 Gy/s의 평균 선량률과 0.005-7.68 Gy의 펄스당 선량 범위에서 선형적인 반응을 보였으며, 선량률에 따른 감도 변화는 +/- 3% 이내로 억제되었다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §Abstract]].
2. **펄스 분해능**: 최대 120 Hz의 펄스 반복 주파수(PRF)에서 개별 펄스를 명확히 구분하여 측정할 수 있었으며, 이는 펄스별 선량 관리에 매우 유용하다 [[120_nihpp-2403.03142v1.pdf#page=13|p.13, §Conclusions]].
3. **포화 저항성**: 펄스당 선량률($DR_p$)이 8.9e4 Gy/s에서 1.8e6 Gy/s로 급격히 증가할 때 단위 선량당 신호가 약 6% 감소하는 경향을 보였으나, 이를 보정 계수로 관리할 수 있음을 확인하였다 [[120_nihpp-2403.03142v1.pdf#page=2|p.2, §Abstract]].

---

## Critical Review

### 방법론·실험설계 타당성

실험 설계는 Mobetron 가속기를 이용해 실제 FLASH 치료 환경을 잘 모사하였으며, 라디오크로믹 필름(Gafchromic EBT3)과 이온화 챔버를 이용한 교차 검증을 통해 신뢰도를 높였다 [[120_nihpp-2403.03142v1.pdf#page=5|p.5, §Methods]]. 다만, 광학 검출기의 동적 범위 한계로 인해 통합 윈도우당 선량($D_{iw}$)이 0.028-11.56 Gy 범위를 유지해야 하는 제약 조건이 존재한다 [[120_nihpp-2403.03142v1.pdf#page=7|p.7, §Results]].

### 선행연구 대비 기여도·한계

이전 연구들이 주로 낮은 선량률 환경에 집중했던 것과 달리, 본 연구는 1341 Gy/s에 달하는 초고선량률까지 확장 검증하였다는 점에서 독보적인 기여를 한다 [[120_nihpp-2403.03142v1.pdf#page=11|p.11, §Discussion]]. 한계점으로는 샘플링 주파수가 펄스 주파수의 2배보다 낮을 때 발생하는 '분할 펄스(split pulses)' 현상이 있으며, 이는 소프트웨어적 보정이 필요하다 [[120_nihpp-2403.03142v1.pdf#page=10|p.10, §Pulse Discrimination]].

---

## Implications for Our Research

본 연구에서 사용된 Hyperscnt RP-FLASH 시스템은 우리 프로젝트의 FLASH 선량 측정 연구에 직접적인 벤치마킹 대상이 될 수 있다. 특히 실시간 펄스별 선량 추적 기능은 FLASH 치료의 안정성 확보에 핵심적인 요소이며, $D_{iw}$ 범위를 유지하기 위한 샘플링 주파수 설정 기법을 참고할 필요가 있다.

---

## References

- [1] Romano, F., et al. (2022). Ultra-high dose rate dosimetry: challenges and opportunities for FLASH radiation therapy. Medical physics.
- [2] Di Martino, F., et al. (2021). Corrigendum: FLASH radiotherapy with electrons: Issues related to the production, monitoring, and dosimetric characterization of the beam. Frontiers in Physics.
- [3] Liu, K., et al. (2024). A Comprehensive Investigation of the Performance of the Exradin W2 Scintillator System for Applications in Electron FLASH radiotherapy. Medical physics.
- [16] Favaudon, V., et al. (2019). Time-resolved dosimetry of pulsed electron beams in very high dose-rate, FLASH irradiation for radiotherapy preclinical studies. Nuclear Instruments and Methods in Physics Research Section A.
