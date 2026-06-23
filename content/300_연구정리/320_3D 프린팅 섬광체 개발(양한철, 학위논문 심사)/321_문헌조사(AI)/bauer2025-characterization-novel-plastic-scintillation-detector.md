---
title: "Characterization of a novel plastic scintillation detector for in vivo electron dosimetry"
authors: ["Bauer, C. J.", "Schneider, F.", "Göbel, I. D.", "Oppitz, H.", "Giordano, F. A.", "Fleckenstein, J."]
year: 2025
venue: "arXiv"
doi: ""
arxiv: "2509.04933v1"
paper_id: "bauer2025-characterization-novel-plastic-scintillation-detector"
source_pdf: "[[100_2509.04933v1.pdf]]"
tags: [paper, paper/reviewed, topic/dosimetry, topic/scintillation-detector]
aliases: ["Bauer 2025"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 0.87
---

# Bauer et al. (2025) — Characterization of a novel plastic scintillation detector for in vivo electron dosimetry

**Venue**: arXiv
**DOI**: []() · **arXiv**: [2509.04933v1](https://arxiv.org/abs/2509.04933v1)
**PDF**: ![[100_2509.04933v1.pdf#page=1]]

---

## Executive Summary

본 연구는 생체 내(in vivo) 전자선 선량 측정을 위해 고안된 새로운 플라스틱 섬광 검출기(Plastic Scintillation Detector, PSD)인 Blue Physics Model 11의 선량학적 특성을 평가하였다. [[100_2509.04933v1.pdf#page=2|p.2, §Abstract]] 기준 이온화 챔버와 비교하여 선형성, 선량률 독립성, 등방성 및 재현성을 검증한 결과, 총 변동성이 2% 미만으로 임상적으로 수용 가능한 수준임을 확인하였다. [[100_2509.04933v1.pdf#page=2|p.2, §Abstract]] 특히 표면 선량 측정에서 기준 검출기 대비 2% 이내의 오차를 보여, 전자선 치료 시 실시간 생체 내 선량 측정에 활용될 잠재력이 높음을 입증하였다. [[100_2509.04933v1.pdf#page=2|p.2, §Abstract]]

---

## Problem & Motivation

방사선 치료에서 환자에게 전달되는 에너지를 정확히 파악하는 것은 치료 효과를 보장하고 정상 조직을 보호하기 위해 필수적이며, 특히 전자선 치료의 경우 환자 설정 및 빔 콜리메이션이 총 선량과 심부선량분포(depth-dose curve)에 큰 영향을 미치므로 생체 내 선량 측정이 중요하다. [[100_2509.04933v1.pdf#page=3|p.3, §1]] 기존의 방사선 변색 필름, MOSFET, 다이오드 등은 선량률, 에너지, 방향에 독립적이면서 실시간 비섭동적(non-perturbative) 측정을 제공하지 못하는 한계가 있다. [[100_2509.04933v1.pdf#page=3|p.3, §1]] 이온화 챔버는 정확하지만 빔을 교란시켜 환자 표면 측정에 부적합하다. [[100_2509.04933v1.pdf#page=3|p.3, §1]] 플라스틱 섬광 검출기(PSD)는 물과 등가성을 지녀 빔 교란을 최소화하고 높은 공간 분해능을 제공하지만, 체렌코프(Cherenkov) 방사선에 대한 보정이 필요하다. [[100_2509.04933v1.pdf#page=3|p.3, §1]] Blue Physics Model 11 PSD는 광자선에서 유망한 결과를 보였으나, 전자선 및 표면 선량 측정에 대한 특성 평가는 아직 발표되지 않아 본 연구에서 이를 최초로 검증하고자 하였다. [[100_2509.04933v1.pdf#page=3|p.3, §1]]

---

## Methods

본 연구는 0.785 mm³ (길이 및 직경 1 mm)의 민감 체적을 갖는 Blue Physics Model 11 플라스틱 섬광 검출기(SD)를 사용하였다. [[100_2509.04933v1.pdf#page=4|p.4, §2.1]] 체렌코프 빛을 보정하기 위해 인접 채널 비율(Adjacent Channel Radio, ACR)을 이용한 이중 채널 접근법을 적용하였다. [[100_2509.04933v1.pdf#page=3|p.3, §2.1]] 실험은 Elekta Synergy 선형 가속기(Linac)를 사용하여 6~12 MeV의 전자선 에너지와 50~400 MU/min의 선량률 조건에서 수행되었다. [[100_2509.04933v1.pdf#page=4|p.4, §2.1]] 기준 검출기로는 Advanced Markus 이온화 챔버(AM), Semiflex3D 이온화 챔버, Gafchromic EBT-XD 방사선 변색 필름(RF)이 사용되었다. [[100_2509.04933v1.pdf#page=4|p.4, §2.1]] 선량 선형성(1~1000 MU), 선량률 의존성, 단기 재현성(10회 반복), 등방성(90도 간격 회전)을 평가하였다. [[100_2509.04933v1.pdf#page=5|p.5, §2.2.2]] 또한 심부선량백분율(PDD), 횡단 프로파일(inline 및 crossline), 소조사면 출력 계수(3x3 ~ 7x7 cm²), 그리고 RW3 슬랩 및 인체 모형 팬텀을 이용한 표면 선량을 측정하여 기준 검출기와 비교하였다. [[100_2509.04933v1.pdf#page=5|p.5, §2.3-2.5]]

---

## Results

측정된 ACR 값은 0.916 ± 0.013으로 제조사 사양과 일치하였다. [[100_2509.04933v1.pdf#page=6|p.6, §3.1]] 선량 선형성은 1.3% (5 cGy 이상에서는 1.0% 미만), 선량률 의존성은 1.0%, 단기 재현성은 0.3%, 등방성은 0.8%로 나타났으며, 총 표준 편차는 1.8%였다. [[100_2509.04933v1.pdf#page=6|p.6, §3.1]] PDD 측정 결과, SD와 AM 간의 R50 및 R80 차이는 1.0 mm 미만이었으나, 12 MeV에서 Rmax는 최대 3.4 mm의 차이를 보였다. [[100_2509.04933v1.pdf#page=7|p.7, §3.3]] 횡단 프로파일 측정에서 SD와 이온화 챔버 간의 평균 절대 오차(MAE)는 0.5%에서 1.5% 사이였다. [[100_2509.04933v1.pdf#page=8|p.8, §3.4]] 소조사면 출력 계수는 모든 에너지에서 SD와 AM이 평균 (0.4 ± 0.8)%의 편차로 잘 일치하였다. [[100_2509.04933v1.pdf#page=9|p.9, §3.5]] 표면 선량 측정 시 RW3 팬텀에서는 AM 대비 0.9%의 MAE를 보였고, 인체 모형 팬텀에서는 RF 대비 2.6%의 상대적 MAE를 기록하였다. [[100_2509.04933v1.pdf#page=10|p.10, §3.6]]

---

## Critical Review

### 방법론·실험설계 타당성

본 연구는 선형성, 선량률 의존성, 등방성, PDD, 프로파일 등 포괄적인 선량학적 특성을 평가하기 위해 이온화 챔버 및 방사선 변색 필름과 같은 확립된 기준 검출기를 사용하여 높은 내적 타당도를 확보하였다. [[100_2509.04933v1.pdf#page=4|p.4, §2.1]] 이중 채널 체렌코프 보정 방법은 일관된 ACR 값을 통해 효과적으로 구현되었음이 입증되었다. [[100_2509.04933v1.pdf#page=6|p.6, §3.1]] 평가자 해석: 단순한 슬랩 팬텀뿐만 아니라 복잡한 곡면을 가진 인체 모형 팬텀을 표면 선량 측정에 도입한 것은 임상적 적용 가능성을 높이는 훌륭한 실험 설계이다.

### 선행연구 대비 기여도·한계

이 연구는 Blue Physics Model 11 PSD를 전자선 및 표면 선량 측정에 적용하여 특성을 평가한 최초의 문헌으로, 기존 연구의 공백을 메우는 중요한 기여를 한다. [[100_2509.04933v1.pdf#page=3|p.3, §1]] 저자들은 5 cGy 미만의 저선량에서 선형성 변동이 더 크게 나타남을 명시하였으며, 이는 선형 가속기의 성능에 기인할 수 있다고 분석하였다. [[100_2509.04933v1.pdf#page=11|p.11, §4.1]] 평가자 해석: 검출기가 우수한 물 등가성을 보임에도 불구하고, 1 mm의 물리적 크기로 인해 표면 근처의 PDD 측정에서 미세한 이동(shift)이 발생하므로 정밀한 생체 내 적용 시 이를 고려한 모델링이 필요할 수 있다.

---

## Implications for Our Research

본 연구에서 입증된 Blue Physics PSD의 높은 정확도와 최소한의 빔 교란 특성은 향후 우리 연구팀의 전자선 기반 실시간 생체 내 선량 측정 시스템 개발에 중요한 참고 자료가 될 수 있다. 특히 이중 채널 체렌코프 보정 기법의 성공적인 적용 사례는 자체적인 섬광 검출기 보정 알고리즘 설계 시 비교 및 검증 모델로 활용될 수 있다. 또한 인체 모형 팬텀에서의 유효성 검증 결과는 임상 환경과 유사한 복잡한 실험 셋업으로 연구를 확장할 수 있는 근거를 제공한다.

---

## References

- [1] Hogstrom KR, Almond PR. Review of electron beam therapy physics. Phys Med Biol. 2006;51(13):R455-489. doi:10.1088/0031-9155/51/13/R25
- [2] Wolfe CM, Green WH, Hatfield HK, Shakar TJ, Baniahmad O, Cognetta AB. Multiple secondary cutaneous tumours following electron beam radiotherapy for cutaneous malignancies of the scalp. Australas J Dermatol. 2012;53(3):233-238. doi:10.1111/j.1440-0960.2012.00917.x
- [3] Wang D, Polignani JA. Quantitative approaches in electron skin collimation for the practical benefits. J Appl Clin Med Phys. 2024;25(4):e14236. doi:10.1002/acm2.14236
- [4] Gerbi BJ, Antolak JA, Deibel FC, et al. Recommendations for clinical electron beam dosimetry: supplement to the recommendations of Task Group 25. Med Phys. 2009;36(7):3239-3279. doi:10.1118/1.3125820
- [5] Sipilä P, Ojala J, Kaijaluoto S, Jokelainen I, Kosunen A. Gafchromic EBT3 film dosimetry in electron beams - energy dependence and improved film read-out. J Appl Clin Med Phys. 2016;17(1):360-373. doi:10.1120/jacmp.v17i1.5970
- [6] 18. Bufacchi A, Carosi A, Adorante N, et al. In vivo EBT radiochromic film dosimetry of electron beam for Total Skin Electron Therapy (TSET). Phys Med. 2007;23(2):67-72. doi:10.1016/j.ejmp.2007.03.003
- [7] Nakajima E, Sato H. Characterization of a new radiochromic film (LD-V1) using mammographic beam qualities. Z Med Phys. 2025;35(2):169-176. doi:10.1016/j.zemedi.2023.05.004
- [8] Amin MN, Heaton R, Norrlinger B, Islam MK. Small field electron beam dosimetry using MOSFET detector. J Appl Clin Med Phys. 2010;12(1):3267. doi:10.1120/jacmp.v12i1.3267
- [9] Ciocca M, Piazzi V, Lazzari R, et al. Real-time in vivo dosimetry using micro-MOSFET detectors during intraoperative electron beam radiation therapy in early-stage breast cancer. Radiother Oncol. 2006;78(2):213-216. doi:10.1016/j.radonc.2005.11.011
- [10] Meiler RJ, Podgorsak MB. Characterization of the response of commercial diode detectors used for in vivo dosimetry. Med Dosim. 1997;22(1):31-37. doi:10.1016/s0958-3947(96)00152-5
- [11] Ade N, Du Plessis FCP. Electron beam dose perturbations caused by diode detectors used for in vivo dosimetry: Gafchromic film dose measurements in a realistic pelvic prosthesis phantom. Radiation Physics and Chemistry. 2018;151:232-238.
- [12] Pearce J, Thomas R, Dusautoy A. The characterization of the Advanced Markus ionization chamber for use in reference electron dosimetry in the UK. Phys Med Biol. 2006;51(3):473-483. doi:10.1088/0031-9155/51/3/001
- [13] Beddar AS, Mackie TR, Attix FH. Water-equivalent plastic scintillation detectors for high-energy beam dosimetry: I. Physical characteristics and theoretical consideration. Phys Med Biol. 1992;37(10):1883-1900. doi:10.1088/0031-9155/37/10/006
- [14] Beddar AS, Mackie TR, Attix FH. Water-equivalent plastic scintillation detectors for high-energy beam dosimetry: II. Properties and measurements. Phys Med Biol. 1992;37(10):1901-1913. doi:10.1088/0031-9155/37/10/007
- [15] Beaulieu L, Beddar S. Review of plastic and liquid scintillation dosimetry for photon, electron, and proton therapy. Phys Med Biol. 2016;61(20):R305-R343. doi:10.1088/0031-9155/61/20/R305
- [16] Dimitriadis A, Patallo IS, Billas I, Duane S, Nisbet A, Clark CH. Characterisation of a plastic scintillation detector to be used in a multicentre stereotactic radiosurgery dosimetry audit. Radiat Phys Chem. 2017;140:373-378.
- [17] Ciarrocchi E, Ravera E, Cavalieri A, et al. Plastic scintillator-based dosimeters for ultra-high dose rate (UHDR) electron radiotherapy. Phys Med. 2024;121:103360. doi:10.1016/j.ejmp.2024.103360
- [18] Vanreusel V, Gasparini A, Galante F, et al. Point scintillator dosimetry in ultra-high dose rate electron “FLASH” radiation therapy: A first characterization. Phys Med. 2022;103:127-137. doi:10.1016/j.ejmp.2022.10.005
- [19] Liu K, Holmes S, Schüler E, Beddar S. A comprehensive investigation of the performance of a commercial scintillator system for applications in electron FLASH radiotherapy. Med Phys. 2024;51(6):4504-4512. doi:10.1002/mp.17030
- [20] Baikalov A, Tho D, Liu K, Bartzsch S, Beddar S, Schüler E. Characterization of a Time-Resolved, Real-Time Scintillation Dosimetry System for Ultra-High Dose-Rate Radiation Therapy Applications. Int J Radiat Oncol Biol Phys. 2025;121(5):1372-1383. doi:10.1016/j.ijrobp.2024.11.092
- [21] Clift MA, Sutton RA, Webb DV. Dealing with Cerenkov radiation generated in organic scintillator dosimeters by bremsstrahlung beams. Phys Med Biol. 2000;45(5):1165-1182. doi:10.1088/0031-9155/45/5/307
- [22] Beddar AS, Law S, Suchowerska N, Mackie TR. Plastic scintillation dosimetry: optimization of light collection efficiency. Phys Med Biol. 2003;48(9):1141-1152. doi:10.1088/0031-9155/48/9/305
- [23] Blue Physics LLC. Blue Physics model 11: instructions for use. Version 1.1. 2023
- [24] Das IJ, Sohn JJ, Lim SN, Sengupta B, Feijoo M, Yadav P. Characteristics of a plastic scintillation detector in photon beam dosimetry. J Appl Clin Med Phys. 2024;25(1):e14209. doi:10.1002/acm2.14209
- [25] Jacqmin DJ, Miller JR, Barraclough BA, Labby ZE. Commissioning an Exradin W2 plastic scintillation detector for clinical use in small radiation fields. J Appl Clin Med Phys. 2022;23(8):e13728. doi:10.1002/acm2.13728
- [26] Almond PR, Biggs PJ, Coursey BM, et al. AAPM’s TG-51 protocol for clinical reference dosimetry of high-energy photon and electron beams. Med Phys. 1999;26(9):1847-1870. doi:10.1118/1.598691
- [27] Schneider F, Bauer CJ, Göbel ID, et al. Rapid and reversible adaptation of a clinical linear accelerator for electron FLASH radiotherapy. Phys Med. 2025;136:105032. doi:10.1016/j.ejmp.2025.105032
- [28] Oolbekkink S, van Asselen B, Woodings SJ, et al. Influence of magnetic field on a novel scintillation dosimeter in a 1.5 T MR-linac. J Appl Clin Med Phys. 2024;25(1):e14180. doi:10.1002/acm2.14180
- [29] Ferrer C, Huertas C, García D, Sáez M. Dosimetric characterization of a novel commercial plastic scintillation detector with an MR-Linac. Med Phys. 2023;50(4):2525-2539. doi:10.1002/mp.16204
- [30] Klein EE, Hanley J, Bayouth J, et al. Task Group 142 report: quality assurance of medical accelerators. Med Phys. 2009;36(9):4197-4212. doi:10.1118/1.3190392
- [31] Galavis PE, Hu L, Holmes S, Das IJ. Characterization of the plastic scintillation detector Exradin W2 for small field dosimetry. Med Phys. 2019;46(5):2468-2476. doi:10.1002/mp.13501
- [32] Carrasco P, Jornet N, Jordi O, et al. Characterization of the Exradin W1 scintillator for use in radiotherapy. Med Phys. 2015;42(1):297-304. doi:10.1118/1.4903757
- [33] Miéville FA, Pitteloud N, Achard V, et al. Post-mastectomy radiotherapy: Impact of bolus thickness and irradiation technique on skin dose. Z Med Phys. 2024;34(4):542-554. doi:10.1016/j.zemedi.2023.03.004
- [34] Kong D, Wu J, Kong X, et al. Effect of bolus materials on dose deposition in deep tissues during electron beam radiotherapy. J Radiat Res. 2024;65(2):215-222. doi:10.1093/jrr/rrae001
- [35] Arunkumar T, Supe SS, Ravikumar M, Sathiyan S, Ganesh M. Electron beam characteristics at extended source-to-surface distances for irregular cut-outs. J Med Phys. 2010;35(4):207-214. doi:10.4103/0971-6203.71763
- [36] Schulz JB, Gibson C, Dubrowski P, et al. Shaping success: clinical implementation of a 3D-printed electron cutout program in external beam radiation therapy. Front Oncol. 2023;13:1237037. doi:10.3389/fonc.2023.1237037
- [37] Gingras L, Cervantes Y, Beaulieu F, et al. Field output correction factors using a scintillation detector. Med Phys. 2025;52(6):4844-4861. doi:10.1002/mp.17729