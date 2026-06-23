---
title: "Development and validation of a 3D-printed skin imitation layer for real-time localized skin dose assessment"
authors: ["Yang, H. C.", "Goh, S. B.", "Pak, K.", "Kim, Y. K."]
year: 2026
venue: "Radiation Physics and Chemistry"
doi: "10.1016/j.radphyschem.2025.113128"
arxiv: ""
paper_id: "yang2026-3d-printed-skin-imitation"
source_pdf: "[[116_1-s2.0-S0969806X25006206-main.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing, topic/scintillation-dosimetry, topic/skin-dose]
aliases: ["Yang 2026"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Yang et al. (2026) — Development and validation of a 3D-printed skin imitation layer for real-time localized skin dose assessment

**Venue**: Radiation Physics and Chemistry
**DOI**: [10.1016/j.radphyschem.2025.113128](https://doi.org/10.1016/j.radphyschem.2025.113128)
**PDF**: ![[116_1-s2.0-S0969806X25006206-main.pdf#page=1]]

---

## Executive Summary

- 실시간 국소 피부 선량 평가를 위해 3D 프린팅 기술을 활용한 피부 모사층(Skin Imitation Layer, SIL)을 개발함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=1|p.1, §Abstract]].
- SIL은 각각 50 µm 두께의 표피층(EL)과 기저층(BL)으로 구성되며, BL에 플라스틱 신틸레이터를 적용함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=1|p.1, §Abstract]].
- Monte Carlo 시뮬레이션(MCNPX)을 통해 알파 입자, 전자, 광자에 대한 조직 등가성을 검증함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=1|p.1, §Abstract]].
- 4종의 감마선원을 이용한 실험을 통해 배경 방사선 및 체렌코프 방사선으로부터 신틸레이션 신호를 성공적으로 분리함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=1|p.1, §Abstract]].

---

## Problem & Motivation

- 피부 방사선 노출은 흡수 선량에 따라 결정론적 영향을 미치며, 국소 피부 증상은 발현까지 수개월이 걸릴 수 있어 신속한 선량 평가가 필수적임 [[116_1-s2.0-S0969806X25006206-main.pdf#page=1|p.1, §1]].
- 기존의 TL/OSL이나 EPR 방식은 평가 시간이 길고 직접적인 실시간 선량 측정을 제공하지 못하는 한계가 있음 [[116_1-s2.0-S0969806X25006206-main.pdf#page=1|p.1, §1]].
- ICRP 103 보고서에 따르면 피부 표면에서 약 50–100 µm 깊이의 기저 세포층에서의 선량 평가를 권고하고 있음 [[116_1-s2.0-S0969806X25006206-main.pdf#page=2|p.2, §2.1]].

---

## Methods

- **제작**: DLP(Digital Light Processing) 방식의 3D 프린터(Carima, IMD-C)를 사용하여 EL(CUKM25W Matt white 레진)과 BL(RMPS470 플라스틱 신틸레이터 레진)을 순차적으로 적층함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=2|p.2, §2.1]].
- **두께 측정**: 접촉식 프로파일러(Detak-XT)와 SEM을 사용하여 각 층의 두께를 검증함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=2|p.2, §2.2]].
- **시뮬레이션**: MCNPX(version 2.7.0)를 사용하여 SIL 팬텀과 ICRP 116 팬텀 간의 단위 플루언스당 흡수 선량($D/\Phi$)을 비교 분석함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=3|p.3, §2.5]].
- **실험**: PMT(H10721-20, Hamamatsu)와 4종의 감마선원(Cd-109, Ba-133, Cs-137, Mn-54)을 사용하여 방사선 응답 특성을 평가함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=3|p.3, §2.6]].

---

## Results

- **두께**: EL은 52.2 ± 18.5 µm, BL은 51.1 ± 16.5 µm로 설계치인 50 µm에 근접하게 제작됨 [[116_1-s2.0-S0969806X25006206-main.pdf#page=3|p.3, §3.1]].
- **조직 등가성**: BL의 실효 원자 번호($Z_{eff}$)는 광전 효과 영역에서 6.18, 콤프턴 산란 영역에서 5.75로 계산되어 ICRP 116 팬텀(7.07, 6.28)과 유사한 수준을 보임 [[116_1-s2.0-S0969806X25006206-main.pdf#page=5|p.5, §3.2, Table 3]].
- **선량 반응**: MCNPX 결과, 7 MeV 이상의 알파 입자와 50 keV~2 MeV 영역의 광자에 대해 SIL과 ICRP 116 팬텀 간의 높은 일치성을 확인함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=5|p.5, §3.2]].
- **감마 응답**: 차감법(Subtraction method)을 통해 배경 신호와 체렌코프 광을 분리하고, 감마 에너지 증가에 따른 유의미한 신틸레이션 신호 증가를 확인하였으며 Mn-54(0.835 MeV)에서 가장 높은 0.31 nC의 신호를 기록함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=7|p.7, §3.3]].

---

## Critical Review

### 방법론·실험설계 타당성

- 3D 프린팅의 적층 오차(표준편차 약 18 µm)가 존재하지만, 실제 인간 표피의 두께 변동성(~30%)을 고려할 때 수용 가능한 수준으로 판단됨 [[116_1-s2.0-S0969806X25006206-main.pdf#page=4|p.4, §3.1]].
- 시뮬레이션에서 SIL 팬텀과 ICRP 116 팬텀 간의 조성 차이(C/O 비율 등)로 인해 저에너지 광자 영역에서 최대 40% 이상의 선량 차이가 발생할 수 있음을 명시함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=5|p.5, §3.2]].

### 선행연구 대비 기여도·한계

- 기존의 고정형 신틸레이션 검출기와 달리 유연하고 얇은 층 구조를 3D 프린팅으로 구현하여 직접적인 피부 선량 평가 가능성을 제시함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=7|p.7, §4]].
- 다만, 실제 웨어러블 플랫폼으로의 통합과 선량 전환 계수(DCC)의 정량적 산출을 위한 추가 연구가 필요함 [[116_1-s2.0-S0969806X25006206-main.pdf#page=7|p.7, §4]].

---

## Implications for Our Research

- 50 µm 수준의 극박막 신틸레이터를 3D 프린팅으로 안정적으로 제작할 수 있는 공정 파라미터(DLP 방식, 25 µm 적층)를 참고할 수 있음.
- 배경 방사선 및 체렌코프 광 분리를 위한 차감법 실험 설계는 향후 우리 연구의 고에너지 방사선 측정 시 신호 무결성 확보에 중요한 기반이 될 수 있음.

---

## References

- [1] ICRP, 2007. The 2007 Recommendations of the International Commission on Radiological Protection. ICRP Publication 103.
- [2] Kim, Y.K., et al., 2020. Characteristics of 3D-printed plastic scintillator for radiation measurement. Radiat. Phys. Chem. 170.
- [3] Petoussi-Henss, N., et al., 2010. ICRP Publication 116: Conversion coefficients for radiological protection quantities for external radiation exposures.
- [4] Carima, IMD-C, User Manual.
