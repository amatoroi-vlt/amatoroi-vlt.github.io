---
title: "Beam test results of a fully 3D-printed plastic scintillator particle detector prototype"
authors: ["Li, B.", "Weber, T.", "Kose, U.", "Franks, M.", "Wüthrich, J.", "Zhao, X.", "Sgalaberna, D.", "Boyarintsev, A.", "Sibilieva, T.", "Berns, S.", "Boillat, E.", "De Roeck, A.", "Dieminger, T.", "Grynyov, B.", "Hugon, S.", "Jaeschke, C.", "Rubbia, A."]
year: 2025
venue: "Journal of Instrumentation"
doi: "10.1088/1748-0221/20/04/P04008"
arxiv: "2412.10174"
paper_id: "li2025-beam-test-results-fully-3d-printed"
source_pdf: "[[008_Li_2025_J._Inst._20_P04008.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing-scintillator]
aliases: ["Li 2025"]
status: reviewed
analyzed_at: 2025-05-24
verification_pass_rate: 1.0
---

# Li et al. (2025) — Beam test results of a fully 3D-printed plastic scintillator particle detector prototype

**Venue**: Journal of Instrumentation
**DOI**: [10.1088/1748-0221/20/04/P04008](https://doi.org/10.1088/1748-0221/20/04/P04008) · **arXiv**: [2412.10174](https://arxiv.org/abs/2412.10174)
**PDF**: ![[008_Li_2025_J._Inst._20_P04008.pdf#page=1]]

---

## Executive Summary

이 연구는 Fused Injection Modeling (FIM) 적층 제조 기술을 사용하여 제작된 3D 프린팅 플라스틱 섬광체 입자 검출기 프로토타입의 빔 테스트 결과를 제시한다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=2|p.2, §Abstract]]. 프로토타입은 1 cm³ 크기의 광학적으로 분리된 플라스틱 섬광체 큐브 5×5×5 배열로 구성되며, CERN의 양성자 싱크로트론(PS) 시설에서 성능 평가를 거쳤다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=2|p.2, §Abstract]]. 테스트 결과, 채널당 약 27 광전자(p.e.)의 일관된 광량(Light Yield, LY)을 보였으며, 인접 큐브 간의 광학적 누화(crosstalk)는 평균 4-5% 수준으로 측정되었다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=2|p.2, §Abstract]]. 단일 큐브 내의 광량 균일성은 약 7%의 변동성을 보여, 새로운 적층 제조 기술이 고해상도 섬광체 검출기의 효율적이고 신뢰할 수 있는 생산에 적합함을 입증하였다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=2|p.2, §Abstract]].

---

## Problem & Motivation

최근 중성리자 상호작용과 같은 입자 궤적을 3D로 재구성하기 위해 고해상도의 3D 입상(granular) 섬광체 검출기가 개발되고 있다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=3|p.3, §1]]. 기존의 사출 성형(injection molding) 방식은 수백만 개의 큐브를 개별적으로 제작하고 조립해야 하므로 제조 및 조립 과정에서 막대한 시간과 노력이 요구된다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=4|p.4, §1]]. 이러한 복잡성을 해결하기 위해 Fused Injection Modeling (FIM)이라는 새로운 적층 제조 기술이 개발되었으며, 이는 광학적으로 분리된 미세 구조의 섬광체 블록을 단일 공정으로 자동 3D 프린팅할 수 있게 해준다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=4|p.4, §1]]. 본 연구는 이 FIM 기술로 제작된 프로토타입 검출기가 실제 하전 입자 빔 환경에서 기존 방식과 유사한 성능을 낼 수 있는지 검증하고자 한다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=5|p.5, §2]].

---

## Methods

프로토타입(SuperCube)은 FIM 기술로 제작된 5×5×5 배열의 1 cm³ 플라스틱 섬광체 복셀로 구성되며, 각 복셀은 직교하는 두 개의 파장 천이(WLS) 파이버로 판독된다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=4|p.4, §2]]. 실험은 CERN PS East Area의 T9 빔라인에서 10 GeV 뮤온 및 하드론 빔을 사용하여 기생적(parasitically)으로 수행되었다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=7|p.7, §3.4]]. 판독 시스템으로는 50개의 Kuraray Y11 이중 클래딩 WLS 파이버(직경 1 mm, 길이 9 cm)가 사용되었으며, Hamamatsu MPPC 13360-1325 CS(활성 영역 1.3×1.3 mm², PDE 25%)와 결합되었다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=5|p.5, §3.1]]. 단일 큐브 내 입자 위치에 따른 광량 균일성을 연구하기 위해 프로토타입 양쪽에 서브 밀리미터 공간 해상도를 제공하는 두 개의 보조 호도스코프(Hodoscope)를 설치하였다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=6|p.6, §3.2]]. 데이터 처리는 총 12,190,778개의 트리거 이벤트 중 단일 트랙 및 직선 트랙 선택 기준을 적용하여 1,180,787개(9.6%)의 이벤트를 분석에 사용하였다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=7|p.7, §4.1]].

---

## Results

단일 채널의 전형적인 광량(LY)은 약 28.8 p.e./MIP로 측정되었으며, 50개 채널 전체의 평균 광량은 28.1 p.e./channel/MIP (표준편차 3.7 p.e./channel/MIP)로 나타났다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=9|p.9, §4.2]]. 인접 큐브로의 광학적 누화(Optical Crosstalk)는 x 파이버 채널에서 평균 6.03% (피크 3.90%), y 파이버 채널에서 평균 5.56% (피크 3.50%)로 측정되었다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=11|p.11, §4.3]]. 이는 전체적으로 약 4-5% 수준에 해당한다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=12|p.12, §5]]. 단일 큐브 내 입자 상호작용 위치에 따른 광량의 불균일성(RMS)은 평균 약 7%로 측정되었으며, 큐브 간 변동성은 약 0.9%로 매우 낮아 우수한 재현성을 보였다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=12|p.12, §4.4]].

---

## Critical Review

### 방법론·실험설계 타당성

CERN의 실제 빔 환경에서 호도스코프를 결합하여 서브 밀리미터 수준의 정밀한 위치 추적을 수행한 점은 실험 설계의 신뢰성을 높인다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=6|p.6, §3.2]]. 단일 트랙 및 직선 트랙 필터링을 통해 노이즈를 효과적으로 제거하고 순도 높은 데이터를 확보한 데이터 처리 방식이 타당하다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=7|p.7, §4.1]]. 평가자 해석: 다만, 테스트된 프로토타입의 크기(5×5×5)가 실제 대규모 중성리자 검출기에 비해 매우 작으므로, 대형화 시 발생할 수 있는 구조적 안정성이나 대규모 광학적 균일성에 대한 추가 검증이 필요해 보인다.

### 선행연구 대비 기여도·한계

기존의 개별 사출 성형 및 수작업 조립 방식의 한계를 극복하고, FIM 기술을 통해 복잡한 3D 구조를 단일 공정으로 제작할 수 있음을 입증한 것이 가장 큰 기여이다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=4|p.4, §1]]. 측정된 광량(약 28 p.e.)과 누화율(약 4-5%)은 기존 표준 주조 중합(cast polymerization) 방식으로 제작된 샘플과 유사한 수준으로, 물리학적 요구사항을 충족한다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=12|p.12, §5]]. 저자들은 현재 사용된 반사 물질로 인해 큐브 간 빛 누출이 발생하며, 이를 개선하기 위한 새로운 반사 필라멘트 개발이 진행 중임을 한계 및 향후 과제로 명시하였다 [[008_Li_2025_J._Inst._20_P04008.pdf#page=13|p.13, §5]].

---

## Implications for Our Research

FIM(Fused Injection Modeling) 기술은 복잡한 형상의 플라스틱 섬광체를 빠르고 정밀하게 제작할 수 있는 강력한 도구로, 우리 연구실의 맞춤형 방사선 검출기 설계 및 프로토타이핑에 직접적으로 활용될 수 있다. 특히, 3D 프린팅 과정에서 광학적 격리벽(reflective walls)을 동시에 형성하는 기술은 다채널 배열 검출기의 조립 공정을 획기적으로 단축시킬 수 있는 아이디어를 제공한다. 향후 3D 프린팅 기반 섬광체 연구 시, 본 논문에서 제시된 호도스코프 기반의 서브 밀리미터 공간 분해능 광량 균일성 측정 기법을 벤치마킹할 수 있을 것이다.

---

## References

- [1] M.G. Schorr and F.L. Torney, Solid Non-Crystalline Scintillation Phosphors, Phys. Rev. 80 (1950) 474.
- [2] T2K ND280 FGD collaboration, The T2K Fine-Grained Detectors, Nucl. Instrum. Meth. A 696 (2012) 1 [arXiv:1204.3666].
- [3] MINERvA collaboration, Design, Calibration, and Performance of the MINERvA Detector, Nucl. Instrum. Meth. A 743 (2014) 130 [arXiv:1305.5199].
- [4] MINOS collaboration, The magnetized steel and scintillator calorimeters of the MINOS experiment, Nucl. Instrum. Meth. A 596 (2008) 190 [arXiv:0805.3170].
- [5] C. Joram et al., LHCb Scintillating Fibre Tracker Engineering Design Review Report: Fibres, Mats and Modules, LHCb-PUB-2015-008 (2015).
- [6] ATLAS collaboration, The ATLAS Experiment at the CERN Large Hadron Collider, 2008 JINST 3 S08003.
- [7] C. Betancourt et al., Application of large area SiPMs for the readout of a plastic scintillator based timing detector, 2017 JINST 12 P11023 [arXiv:1709.08972].
- [8] A. Korzenev et al., A 4π time-of-flight detector for the ND280/T2K upgrade, 2022 JINST 17 P01016 [arXiv:2109.03078].
- [9] T2K UK collaboration, The Electromagnetic Calorimeter for the T2K Near Detector ND280, 2013 JINST 8 P10019 [arXiv:1308.3445].
- [10] V. Andreev et al., A high-granularity plastic scintillator tile hadronic calorimeter with APD readout for a linear collider detector, Nucl. Instrum. Meth. A 564 (2006) 144.
- [11] SoLid collaboration, A novel segmented-scintillator antineutrino detector, 2017 JINST 12 P04024 [arXiv:1703.01683].
- [12] A. Blondel et al., A fully active fine grained detector with three readout views, 2018 JINST 13 P02006 [arXiv:1707.01785].
- [13] O. Mineev et al., Beam test results of 3D fine-grained scintillator detector prototype for a T2K ND280 neutrino active target, Nucl. Instrum. Meth. A 923 (2019) 134 [arXiv:1808.08829].
- [14] A. Blondel et al., The SuperFGD Prototype Charged Particle Beam Tests, 2020 JINST 15 P12003 [arXiv:2008.08861].
- [15] T2K collaboration, T2K ND280 Upgrade - Technical Design Report, arXiv:1901.03750.
- [16] T2K press release, https://www.kek.jp/en/press-en/202401171405/.
- [17] S. Fedotov et al., Scintillator cubes for 3D neutrino detector SuperFGD, J. Phys. Conf. Ser. 2374 (2022) 012106 [arXiv:2111.07305].
- [18] S. Alonso-Monsalve et al., Artificial intelligence for improved fitting of trajectories of elementary particles in dense materials immersed in a magnetic field, Commun. Phys. 6 (2023) 119 [arXiv:2211.04890].
- [19] Fdm technology, about fused deposition modeling (copyright by stratasys), http://www.stratasys.com/3d-printers/technologies/fdm-technology.
- [20] S. Berns et al., A novel polystyrene-based scintillator production process involving additive manufacturing, 2020 JINST 15 10 [arXiv:2011.09859].
- [21] 3DET collaboration, Additive manufacturing of fine-granularity optically-isolated plastic scintillator elements, 2022 JINST 17 P10045 [arXiv:2202.10961].
- [22] T. Weber et al., Additive manufacturing of a 3D-segmented plastic scintillator detector for tracking and calorimetry of elementary particles, arXiv:2312.04672.
- [23] A. Boyarintsev et al., Demonstrating a single-block 3D-segmented plastic-scintillator detector, 2021 JINST 16 P12010 [arXiv:2108.11897].
- [24] Hamamatsu, MPPC (multi-pixel photon counter) S13360 series.
- [25] Kuraray catalogue — plastic scintillating fibers, http://kuraraypsf.jp/psf/ws.html.
- [26] CAEN FERS DT5202, https://www.caen.it/products/dt5202/.
- [27] F. Iacob et al., ENUBET: a monitored neutrino beam for the precision era of neutrino physics, J. Phys. Conf. Ser. 2156 (2021) 012234.