---
title: "Fast-, Light-Cured Scintillating Plastic for 3D-Printing Applications"
authors: ["Frandsen, B. G.", "Febbraro, M.", "Ruland, T.", "Stephens, T. W.", "Hausladen, P. A.", "Manfredi, J. J.", "Bevins, J. E."]
year: 2023
venue: "Journal of Nuclear Engineering"
doi: "10.3390/jne4010019"
arxiv: ""
paper_id: "frandsen2023-fast-light-cured-scintillating-plastic"
source_pdf: "[[106_jne-04-00019-v3.pdf]]"
tags: [paper, paper/reviewed, topic/scintillator-3d-printing]
aliases: ["Frandsen 2023"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 1.0
---

# Frandsen et al. (2023) — Fast-, Light-Cured Scintillating Plastic for 3D-Printing Applications

**Venue**: Journal of Nuclear Engineering
**DOI**: [10.3390/jne4010019](https://doi.org/10.3390/jne4010019) · **arXiv**: []()
**PDF**: ![[106_jne-04-00019-v3.pdf#page=1]]

---

## Executive Summary

본 연구는 고속 중성자 검출기의 3D 프린팅을 지원하기 위해 중성자-감마 펄스 형태 판별(PSD)이 가능한 광경화성 신틸레이터 레진 배합을 개발하였다. [[106_jne-04-00019-v3.pdf#page=1|p.1, Abstract]] 시행착오 방식과 2수준 요인 매개변수 연구를 통해 방사선 검출 성능, 광학적 투명도 및 경도를 최적화하였다. [[106_jne-04-00019-v3.pdf#page=1|p.1, Abstract]] 그 결과, 405 nm 빛을 사용하여 10초 이내에 고체로 경화되는 단단하고 투명한 PSD 가능 플라스틱 신틸레이터를 제작하였다. [[106_jne-04-00019-v3.pdf#page=1|p.1, Abstract]] 가장 성능이 우수한 신틸레이터는 상용 EJ-276 대비 83%의 광량(light yield)과 450–550 keVee 범위에서 1.28의 PSD 성능 지수(Figure of Merit, FoM)를 달성하였다. [[106_jne-04-00019-v3.pdf#page=1|p.1, Abstract]]

---

## Problem & Motivation

플라스틱 신틸레이터는 저렴한 비용, 제작의 용이성, 빠른 응답 시간으로 인해 방사선 검출에 널리 사용되지만, 기존 제조 방식으로는 복잡한 기하학적 구조나 다중 재료 복합체를 만들기 어렵거나 비용이 많이 든다. [[106_jne-04-00019-v3.pdf#page=1|p.1, §1]] 적층 제조(3D 프린팅) 기술은 이러한 한계를 극복할 잠재력이 있으나, 기존 신틸레이터와 유사한 기계적, 화학적, 광학적 특성을 지닌 프린팅용 원료(feedstock) 개발이 필수적이다. [[106_jne-04-00019-v3.pdf#page=1|p.1, §1]] 기존의 광기반 3D 프린팅용 신틸레이터는 상용 제품 대비 광량이 낮거나(~35%), PSD 성능이 보고되지 않았으며, 경화 시간이 수십 분에 달해 실용성이 떨어지는 문제가 있었다. [[106_jne-04-00019-v3.pdf#page=2|p.2, §1]] 따라서 본 연구는 상용 PSD 플라스틱 신틸레이터(예: EJ-276)와 유사한 광량을 가지면서도 수 초 내에 빠르게 경화되어 DLP 또는 SLA 방식의 3D 프린팅에 적합한 기계적으로 단단하고 광학적으로 투명한 PSD 플라스틱 신틸레이터를 개발하는 것을 목표로 한다. [[106_jne-04-00019-v3.pdf#page=2|p.2, §1]]

---

## Methods

레진 배합은 단량체(monomer), 가교제(crosslinker), 광개시제(photo-initiator), 1차 및 2차 형광 염료(fluorescent dyes)의 5가지 기본 구성 요소로 이루어졌다. [[106_jne-04-00019-v3.pdf#page=2|p.2, §2.1]] 단량체로는 광학적 투명도, 저비용, 높은 끓는점 및 유리 전이 온도를 고려하여 Isobornyl acrylate (IBOA)를 선택하였다. [[106_jne-04-00019-v3.pdf#page=2|p.2, §2.1]] 가교제로는 HDDMA, BPADMA 등을 테스트하였으며, 광개시제로는 405 nm 빛에 반응하는 TPO를 사용하였다. [[106_jne-04-00019-v3.pdf#page=2|p.2, §2.1]] 형광체로는 EJ-309, DIN, PPO를 1차 염료로, Bis-MSB, DPS, Exalite 416을 파장 천이제로 평가하였다. [[106_jne-04-00019-v3.pdf#page=3|p.3, §2.1]] 혼합물은 산소 소광을 줄이기 위해 질소로 10분간 스파징(sparging)한 후, Formlabs Form Cure (405 nm, ~25 mW/cm²)와 Dymax BlueWave AX-550 VisiCure (800 mW/cm²)를 사용하여 경화시켰다. [[106_jne-04-00019-v3.pdf#page=3|p.3, §2.1]] 방사선 검출 성능은 2인치 Hamamatsu R7724 PMT와 CAEN DT5730 디지타이저(500 MS/s, 14-bit)를 사용하여 측정하였으며, 상대 광량은 22Na 및 137Cs 감마선의 콤프턴 에지(Compton edge)를 이용하여 상용 EJ-276과 비교하였다. [[106_jne-04-00019-v3.pdf#page=3|p.3, §2.2]] PSD 성능은 전하 적분(charge integration) 방식을 사용하여 450–550 keVee 범위의 PSD 히스토그램에서 이중 가우시안 피팅을 통해 FoM을 계산하였다. [[106_jne-04-00019-v3.pdf#page=4|p.4, §2.2]] 최적의 배합을 찾기 위해 BPADMA 가교제와 PPO의 양을 변화시키는 2수준 요인 매개변수 연구를 수행하였으며, PPO 침출(leaching) 문제를 해결하기 위해 경화 후 1시간 동안 에탄올 배스(bath) 처리를 적용하였다. [[106_jne-04-00019-v3.pdf#page=7|p.7, §2.4]] [[106_jne-04-00019-v3.pdf#page=13|p.13, §3.5]]

---

## Results

경화 과정 분석 결과, Form Cure에서 5분, BlueWave에서 4분 경화 후 최대 광발광(photoluminescence) 수율을 얻었으며, 샘플은 약 10~20초 후에 고체로 굳어 빠른 경화 속도를 입증하였다. [[106_jne-04-00019-v3.pdf#page=8|p.8, §3.1]] PPO 농도가 높을수록 표면 균열은 감소했으나 침출 현상(뿌연 막 형성)이 증가하는 경향이 관찰되었다. [[106_jne-04-00019-v3.pdf#page=8|p.8, §3.2]] 또한, 경화광 노출 시 일부 신틸레이터에서 보라색 변색(purpling)이 발생했으나, 이는 시간이 지남에 따라 또는 열처리를 통해 소산되었다. [[106_jne-04-00019-v3.pdf#page=9|p.9, §3.2.1]] 방사선 검출 성능 평가에서 가장 우수한 기본 배합(AFIT101: 30 wt% PPO, 0.2 wt% Exalite 416, 49 wt% IBOA, 21 wt% HDDMA, 0.1 wt% TPO)은 EJ-276 대비 78%의 상대 광량과 1.31의 PSD FoM을 기록하였다. [[106_jne-04-00019-v3.pdf#page=11|p.11, §3.3]] 노화(aging) 테스트 결과, AFIT101은 4.5개월 동안 상대 광량이 4.3% 감소하여 같은 기간 EJ-276의 감소율(5.5%)과 유사한 안정성을 보였다. [[106_jne-04-00019-v3.pdf#page=12|p.12, §3.4]] 에탄올 처리 후, 침출 현상이 성공적으로 방지되었으며, 처리된 최적 배합(AFIT225B: 5 wt% DIN, 25 wt% PPO, 21 wt% HDDMA, 0.2 wt% Exalite 416, 0.1 wt% TPO)은 EJ-276 대비 83%의 상대 광량과 1.28의 PSD FoM을 달성하여 광량 및 PSD 성능 저하 없이 문제를 해결하였다. [[106_jne-04-00019-v3.pdf#page=14|p.14, §4]]

---

## Critical Review

### 방법론·실험설계 타당성

탐색적 배합 연구에서 시작하여 2수준 요인 설계(2-level factorial design)를 통해 체계적으로 레진을 최적화한 접근 방식은 타당하다. [[106_jne-04-00019-v3.pdf#page=7|p.7, §2.4]] 상용 EJ-276을 광량 및 PSD 성능 비교의 베이스라인으로 설정하여 새로운 배합의 성능을 객관적으로 평가할 수 있는 기준을 마련하였다. [[106_jne-04-00019-v3.pdf#page=3|p.3, §2.2]] 변색(purpling) 및 침출(leaching)과 같은 실제적인 문제점을 명확히 식별하고, 에탄올 처리라는 구체적인 해결책을 제시 및 검증한 점은 연구의 완성도를 높인다. [[106_jne-04-00019-v3.pdf#page=13|p.13, §3.5]]
평가자 해석: 노화(aging) 연구의 경우 4.5개월이라는 기간은 상용 검출기의 일반적인 수명에 비해 짧은 편이므로, 장기적인 안정성에 대한 결론을 내리기에는 다소 한계가 있다. 더 긴 기간의 추적 관찰이 필요해 보인다.

### 선행연구 대비 기여도·한계

이 연구의 가장 큰 기여는 기존 3D 프린팅용 신틸레이터의 느린 경화 시간과 낮은 광학적 성능을 극복하고, SLA/DLP 프린팅에 적합한 10~20초의 빠른 경화 시간과 높은 광량(EJ-276의 83%), 우수한 PSD 성능(FoM 1.28)을 동시에 달성한 레진을 개발한 것이다. [[106_jne-04-00019-v3.pdf#page=14|p.14, §4]] 저자들이 명시한 한계점으로는 고농도 PPO 사용 시 발생하는 침출 문제이며, 이를 해결하기 위해 에탄올 배스라는 추가적인 후처리 공정이 요구된다는 점이다. [[106_jne-04-00019-v3.pdf#page=14|p.14, §4]] 또한, TPO와 PPO의 상호작용으로 추정되는 일시적인 변색 현상은 프린팅 직후 즉각적인 사용을 제한할 수 있어, 광화학적 메커니즘에 대한 추가적인 최적화가 필요함을 시사한다. [[106_jne-04-00019-v3.pdf#page=9|p.9, §3.2.1]]

---

## Implications for Our Research

이 연구에서 제시된 IBOA 기반의 빠른 광경화 수지 배합은 3D 프린팅을 이용한 복잡한 형상의 방사선 검출기 제작 연구에 직접적으로 활용될 수 있다. 특히 10~20초의 짧은 경화 시간은 SLA/DLP 방식의 프린팅 속도를 크게 향상시킬 수 있는 중요한 요소이다. 또한, PPO 농도 증가에 따른 침출(leaching) 문제와 이를 해결하기 위한 에탄올 처리 방법은 향후 고농도 형광체를 포함하는 레진 개발 시 반드시 고려해야 할 후처리 공정으로 참고할 만하다.

---

## References

- [1] Hamel, M.; Chapter Introduction—Overview on Plastic and Inorganic Scintillators. In Plastic Scintillators; Springer Nature: Cham, Switzerland, 2021; pp. 3–33.
- [2] Hausladen, P.; Blackston, M. Passive and active fast-neutron imaging in support of AFCI safeguards campaign. In Oak Ridge National Laboratory; Report No. ORNL/TM-2009/210; Oak Ridge National Laboratory: Oak Ridge, TN, USA, 2009.
- [3] Beddar, S.; Tendler, I.; Therriault-Proulx, F.; Archambault, L.; Beaulieu, L., Recent Advances and Clinical Applications of Plastic Scintillators in the Field of Radiation Therapy. In Plastic Scintillators: Chemistry and Applications; Hamel, M., Ed.; Springer International Publishing: Cham, Switzerland, 2021; pp. 425–460.
- [4] Gibson, I.; Rosen, D.B.S. Additive Manufacturing Technologies:3D Printing, Rapid Prototyping, and Direct Digital Manufacturing; Springer: Berlin/Heidelberg, Germany, 2015.
- [5] Ligon, S.C.; Liska, R.; Stampfl, J.; Gurr, M.; Mülhaupt, R. Polymers for 3D Printing and Customized Additive Manufacturing. Chem. Rev. 2017, 117, 10212–10290.
- [6] Mishnayot, Y.; Layani, M.; Cooperstein, I.; Magdassi, S.; Ron, G. Three-dimensional printing of scintillating materials. Rev. Sci. Instrum. 2014, 85, 085102.
- [7] Zhu, J.; Ding, Y.; Zhu, J.; Qi, D.; Su, M.; Xu, Y.; Bi, Y.; Lin, R.; Zhang, L. Preparation and characterization of a novel UV-curable plastic scintillator. Nucl. Instrum. Methods Phys. Res. Sect. A 2016, 817, 30–34.
- [8] Lee, S.; Son, J.; Kim, D.G.; Choi, J.; Kim, Y.K. Characterization of plastic scintillator fabricated by UV LED curing machine. Nucl. Instrum. Methods Phys. Res. Sect. A 2019, 929, 23–28.
- [9] Kim, D.G.; Lee, S.; Kim, Y.H.; Seon, S.J.; Sejin, J.; Jeong, J.Y.; Kim, Y.K. Scintillation Light Output of 3D Printed Plastic Scintillators. In Proceedings of the Transactions of the Korean Nuclear Society Spring Meeting, Jeju, Korea, 17–18 May 2018.
- [10] Kim, D.G.; Lee, S.; Park, J.; Son, J.; Kim, T.H.; Kim, Y.H.; Pak, K.; Kim, Y.K. Performance of 3D printed plastic scintillators for gamma-ray detection. Nucl. Eng. Technol. 2020, 52, 2910–2917.
- [11] Kim, K.; Kim, D.G.; Lee, S.; Park, J.; Son, J.; Kim, Y.K. Neutron-Gamma Pulse Shape Discrimination Using 3D-Printed Plastic Scintillator with High-Concentration PPO. In Proceedings of the 2020 IEEE Nuclear Science Symposium and Medical Imaging Conference (NSS/MIC), Boston, MA, USA, 31 October–7 November 2020; pp. 1–3.
- [12] Lim, A.; Mahl, A.; Latta, J.; Yemam, H.A.; Greife, U.; Sellinger, A. Plastic scintillators with efficient light output and pulse shape discrimination produced via photoinitiated polymerization. J. Appl. Polym. Sci. 2019, 136, 47381.
- [13] Eljen Technology. Pulse Shape Discrimination EJ-276 & EJ-276G. Available online: https://eljentechnology.com/products/plastic-scintillators/ej-276 (accessed on 4 November 2021).
- [14] Zaitseva, N.; Rupert, B.L.; PaweLczak, I.; Glenn, A.; Martinez, H.P.; Carman, L.; Faust, M.; Cherepy, N.; Payne, S. Plastic scintillators with efficient neutron/gamma pulse shape discrimination. Nucl. Instrum. Methods Phys. Res. Sect. A 2012, 668, 88–93.
- [15] Zaitseva, N.; Glenn, A.; Mabe, A.; Carman, M.; Hurlbut, C.; Inman, J.; Payne, S. Recent developments in plastic scintillators with pulse shape discrimination. Nucl. Instrum. Methods Phys. Res. Sect. A 2018, 889, 97–104.
- [16] Febbraro, M. 3D Printing of Photocurable Scintillating and Low-Background Materials. Presented at the CPAD Instrumentation Frontier Workshop, Stony Brook, NY, USA, 18–22 March 2021.
- [17] Frandsen, B.G. Capability Development for Advanced (n,x) Nuclear Data Measurements. Ph.D Thesis, Air Force Institute of Technology, Fort Belvoir, VA, USA, 2022.
- [18] van Loef, E.V.; Markosyan, G.; Shirwadkar, U.; Shah, K.S. Plastic Scintillators With Neutron/Gamma Pulse Shape Discrimination. IEEE Trans. Nucl. Sci. 2014, 61, 467–471.
- [19] Laplace, T.; Goldblum, B.; Bevins, J.; Bleuel, D.; Bourret, E.; Brown, J.; Callaghan, E.; Carlson, J.; Feng, P.; Gabella, G.; et al. Comparative scintillation performance of EJ-309, EJ-276, and a novel organic glass. J. Instrum. 2020, 15, P11020.
- [20] McCormack, O.; Giacomelli, L.; Croci, G.; Muraro, A.; Gorini, G.; Grosso, G.; Pasqualotto, R.; Cippo, E.P.; Rebai, M.; Rigamonti, D.; et al. Characterization and operational stability of EJ276 plastic scintillator-based detector for neutron spectroscopy. J. Instrum. 2021, 16, P10002.
- [21] Chikkur, G.; Umakantha, N. A new method of determining the compton edge in liquid scintillators. Nucl. Instrum. Methods 1973, 107, 201–202.
- [22] Dietze, G.; Klein, H. Gamma-calibration of NE 213 scintillation counters. Nucl. Instrum. Methods Phys. Res. 1982, 193, 549–556.
- [23] Brown, J.A.; Goldblum, B.L.; Laplace, T.A.; Harrig, K.P.; Bernstein, L.A.; Bleuel, D.L.; Younes, W.; Reyna, D.; Brubaker, E.; Marleau, P. Proton light yield in organic scintillators using a double time-of-flight technique. J. Appl. Phys. 2018, 124, 045101.
- [24] Pawełczak, I.; Ouedraogo, S.; Glenn, A.; Wurtz, R.; Nakae, L. Studies of neutron−γ pulse shape discrimination in EJ-309 liquid scintillator using charge integration method. Nucl. Instrum. Methods Phys. Res. Sect. A 2013, 711, 21–26.
- [25] Winyard, R.; Lutkin, J.; McBeth, G. Pulse shape discrimination in inorganic and organic scintillators. I. Nucl. Instrum. Methods 1971, 95, 141–153.
- [26] Sasano, M.; Nishioka, H.; Okuyama, S.; Nakazawa, K.; Makishima, K.; Yamada, S.; Yuasa, T.; Okumura, A.; Kataoka, J.; Fukazawa, Y.; et al. Geometry dependence of the light collection efficiency of BGO crystal scintillators read out by avalanche photo diodes. Nucl. Instrum. Methods Phys. Res. Sect. A 2013, 715, 105–111.