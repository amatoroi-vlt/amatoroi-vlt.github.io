---
title: "Development and Characterization of Low Cost Nanoscintillator-Based Radiation Detection Systems Using 3D Printing Technology"
authors: ["Raudabaugh, J. M."]
year: 2021
venue: "Duke University"
doi: ""
arxiv: ""
paper_id: "raudabaugh2021-development-characterization-low-cost-nanoscintillator"
source_pdf: "[[103_Raudabaugh_duke_0066D_16484.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing-radiation-detection]
aliases: ["Raudabaugh 2021"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 1.0
---

# Raudabaugh et al. (2021) — Development and Characterization of Low Cost Nanoscintillator-Based Radiation Detection Systems Using 3D Printing Technology

**Venue**: Duke University
**DOI**: []() · **arXiv**: []()
**PDF**: ![[103_Raudabaugh_duke_0066D_16484.pdf#page=1]]

---

## Executive Summary

이 학위 논문은 [Y1.9O3; Eu0.1, Li0.16] 섬광 나노 입자를 PETG 필라멘트에 혼합하여 3D 프린팅으로 제작한 방사선 검출기의 개발 및 특성 평가를 다룬다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=5|p.v, §2]]. 개발된 기술은 실시간 X선 이미징 스크린과 광섬유 프로브 선량계의 무기 섬광체 소자라는 두 가지 응용 분야에서 평가되었다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=5|p.v, §2]]. 이미징 스크린은 생물학적 샘플의 조직 두께와 물질 밀도 차이를 구별할 수 있음을 입증하였으며, 최대 14 kGy의 누적 선량에서도 섬광 강도의 저하가 관찰되지 않았다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=6|p.vi, §2-3]]. 광섬유 프로브 검출기는 80, 160, 240 kVp X선 환경에서 입사 선량률에 대해 강한 선형적 응답을 보였으며, 검출 하한(LLD)은 3.55 ~ 4.93 cGy/min 수준으로 측정되었다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=8|p.viii, §2]]. 또한, 기존 Nano-FOD 시스템을 활용하여 I-131과 같은 혼합 방출 동위원소 환경에서 두 개의 광섬유를 이용한 감산 기법으로 순수 베타선 선량을 실시간으로 분리 측정하는 방법을 성공적으로 시연하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=9|p.ix, §2-3]].

---

## Problem & Motivation

진단용 이미징 시스템은 주로 대형 무기 섬광체 결정 배열을 사용하지만, 이는 특수 장비가 필요하고 제작에 수개월이 소요되며 기하학적 형태가 제한적이라는 단점이 있다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=4|p.iv, §2]]. 플라스틱 섬광체는 생산 비용이 낮고 제작 기간이 짧지만, 압출이나 사출 성형 등 기존 제조 방식의 한계로 인해 여전히 복잡한 형태를 구현하기 어렵다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=4|p.iv, §2]]. 최근 3D 프린팅 기술의 발전은 방사선 검출기의 신속한 프로토타이핑과 복잡한 기하학적 구조의 자유로운 제작을 가능하게 하여, 기존 제조 방식의 시간적, 비용적 한계를 극복할 대안으로 주목받고 있다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=4|p.iv, §3]]. 한편, 소동물 실험 및 방사선 유도 수술(Radioguided Surgery) 분야에서는 I-131과 같이 베타선과 감마선을 동시에 방출하는 동위원소 환경에서 베타선 선량만을 서브밀리미터 정밀도로 실시간 측정할 수 있는 검출 시스템에 대한 수요가 존재한다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=23|p.8, §2-3]].

---

## Methods

- **이미징 스크린 제작:** 35 wt.% 농도의 [Y1.9O3; Eu0.1, Li0.16] 섬광 나노 입자가 혼합된 PETG 필라멘트를 사용하여 FDM(Fused Deposition Modeling) 방식의 3D 프린터로 2 cm x 2 cm 크기, 1 mm 두께의 스크린을 제작하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=28|p.13, §3]].
- **이미징 시스템 구성:** 스마트폰 카메라(Samsung Galaxy S6 및 Note 9)를 1차 X선 조사 영역 밖에 배치하고, 45도 각도로 기울어진 광학용 거울을 통해 스크린에서 발생하는 섬광 이미지를 획득하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=27|p.12, §2-3]].
- **공간 분해능 및 국소화 평가:** 130 kVp X선 환경에서 선형(1.5 mm 폭) 및 원형(3 mm 직경) 패턴이 뚫린 납 마스크를 스크린 위에 덮고 이미지를 촬영하여, 차폐된 영역과 노출된 영역 간의 국소 대비(Local Contrast)를 계산하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=30|p.15, §2-3]].
- **방사선 손상 평가:** Cs-137 선원을 사용하여 5개의 스크린 샘플에 각각 1.26, 2.43, 4.78, 5.97, 14.01 kGy의 누적 선량을 조사한 후, 대조군 대비 표면 섬광 강도의 변화를 측정하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=31|p.16, §2-3]].
- **생물학적 샘플 이미징:** 쥐의 대퇴골, CIRS 조직 등가 팬텀(폐, 유방, 연조직, 뇌, 뼈), 그리고 플라스티네이션 처리된 쥐 팬텀(PlastiMouse)을 40~120 kVp 조건에서 촬영하고 EBT3 라디오크로믹 필름 결과와 비교하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=35|p.20, §2-4]].
- **광섬유 프로브 검출기:** 1 cm 직경의 3D 프린팅 칩(두께 1 mm 및 2 mm, 나노 입자 농도 0~35 wt.%)을 아크릴 광도파로와 알루미늄 브레이스를 이용해 0.6 mm 직경의 광섬유에 결합하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=64|p.49, §2-3]].
- **프로브 특성 평가:** Precision X-ray X-Rad320 조사기를 사용하여 80, 160, 240 kVp 환경에서 선량 응답성과 검출 하한(LLD)을 측정하고 0.18 cc 이온 챔버 결과와 비교하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=68|p.53, §2-3]].
- **Nano-FOD I-131 선량 측정:** 103 mCi의 I-131 용액에 두 개의 Nano-FOD 검출기(하나는 아크릴 덮개로 베타선 차폐, 다른 하나는 비차폐)를 담그고 20일간 신호를 측정하여 감산 기법으로 베타선 성분을 분리하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=90|p.75, §2-3]].

---

## Results

- **이미징 국소화 성능:** 원형 패턴 마스크(직경 3 mm) 촬영 결과, 평균 반치폭(FWHM)은 2.9 mm ± 3.6%로 측정되었으며, 5개 샘플에 대한 노출 영역과 차폐 영역 간의 국소 대비는 평균 7.97 ± 5.4%로 나타나 우수한 신호 국소화를 보였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=42|p.27, §2-3]].
- **방사선 내구성:** 최대 14.01 kGy의 누적 선량을 조사한 후에도 3D 프린팅 이미징 스크린의 섬광 광량은 대조군 대비 유의미한 변화를 보이지 않았다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=44|p.29, §1]].
- **조직 밀도 분해능:** 이미징 시스템은 연조직과 1년 된 뼈(밀도 차이 0.40 g/cm³), 1년 된 뼈와 성인 뼈(밀도 차이 0.15 g/cm³)를 명확히 구분하였으나, 뇌 조직과 50/50 유방 조직(밀도 차이 0.08 g/cm³)은 구분하지 못했다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=47|p.32, §2]]. 이를 통해 시스템의 밀도 분해능 한계치가 0.08 ~ 0.15 g/cm³ 사이에 있음을 확인하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=62|p.47, §1]].
- **해부학적 이미징:** 플라스티네이션 쥐 팬텀 촬영 이미지에서 척추, 대퇴골, 경골 등 주요 골격 구조와 간, 소화관 등 감쇠가 증가된 장기 영역이 명확하게 관찰되었다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=56|p.41, §2-3]].
- **프로브 검출기 성능:** 칩의 나노 입자 농도가 35 wt.%에 이를 때까지 섬광 강도가 단조 증가하였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=70|p.55, §2]]. 80, 160, 240 kVp X선 환경에서 입사 선량률에 대해 강한 선형적 응답(R² > 0.99)을 보였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=73|p.58, §1]].
- **프로브 검출 하한(LLD):** 35% 칩을 장착한 프로브의 LLD는 80 kVp에서 3.55 ± 0.16 cGy/min, 160 kVp에서 4.09 ± 0.18 cGy/min, 240 kVp에서 4.93 ± 0.22 cGy/min으로 계산되었다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=74|p.59, §2]].
- **Nano-FOD I-131 선량 측정:** 비차폐 광섬유에서 분리된 베타선 신호는 7.73 ± 0.31일의 반감기로 붕괴하였으며, 이는 I-131의 실제 반감기인 8.02일과 4% 이내의 오차를 보였다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=100|p.85, §2]].

---

## Critical Review

### 방법론·실험설계 타당성
- 저자는 스마트폰 카메라와 45도 거울을 활용하여 방사선 조사 영역 밖에서 이미지를 획득하는 저비용 실시간 이미징 시스템을 성공적으로 구축하였으며, 이는 산란 방사선에 의한 카메라 센서 노이즈를 효과적으로 억제한 타당한 설계이다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=27|p.12, §2-3]].
- 방사선 손상 평가에서 최대 14 kGy의 누적 선량을 적용하여 내구성을 입증한 점은, 폴리머 기반 검출기의 임상 및 산업적 장기 활용 가능성을 뒷받침하는 강력한 근거가 된다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=44|p.29, §1]].
- 조직 등가 팬텀을 이용한 밀도 분해능 평가에서 0.08~0.15 g/cm³의 한계치를 명확히 제시하여 시스템의 성능 한계를 정량화한 점이 돋보인다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=62|p.47, §1]].
- 평가자 해석: FDM 3D 프린팅 방식의 특성상 필라멘트 압출 패턴(seam)이 이미지에 대각선 형태의 아티팩트로 남는 문제가 관찰되었으며, 이는 고해상도 이미징을 저해하는 주요 원인으로 작용할 수 있다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=62|p.47, §3]].

### 선행연구 대비 기여도·한계
- 기존의 고비용 무기 섬광체 결정을 대체할 수 있는 저비용 3D 프린팅 나노 섬광체 기반 이미징 스크린의 개념 증명(proof-of-concept)을 최초로 제시한 점에서 학술적 기여도가 크다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=63|p.48, §2]].
- 혼합 방출 동위원소(I-131) 환경에서 두 개의 광섬유(Nano-FOD)를 이용한 감산 기법으로 순수 베타선 선량을 실시간으로 분리 측정한 것은 소동물 생체 내 선량 측정 분야에 중요한 진전이다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=102|p.87, §2]].
- 저자 명시 한계: 프로브 검출기의 경우 1 cm 직경의 칩에서 발생한 빛을 0.6 mm 광섬유로 집광하는 과정에서 광 손실이 발생하여, 기존 Nano-FOD 시스템보다 검출 하한(LLD)이 약 2배 높게 나타나는 한계가 있다 [[103_Raudabaugh_duke_0066D_16484.pdf#page=77|p.62, §2]].
- 추가 식별 한계: 스마트폰 카메라를 이용한 광학적 이미징은 저조도 환경에서의 한계와 렌즈 왜곡 등의 문제가 있을 수 있으며, 임상 수준의 고해상도 이미징을 위해서는 SLA/DLP 프린팅 방식의 도입이나 고성능 광전자증배관(PMT)과의 결합 연구가 필요해 보인다.

---

## Implications for Our Research
- 이 연구에서 제시된 FDM 기반 나노 섬광체 필라멘트 제조 및 프린팅 기술은 환자 맞춤형 유연 선량계나 복잡한 3차원 구조의 방사선 검출기 제작 연구에 직접적으로 응용될 수 있다.
- 특히, 35 wt.%의 높은 나노 입자 로딩 농도에서도 프린팅이 가능함을 보여준 점은, 향후 고감도 플라스틱 섬광체 개발 시 첨가제 농도 최적화의 중요한 참고 자료가 될 것이다.
- I-131과 같은 혼합 방출 동위원소에 대한 두 광섬유 감산 측정 기법은, 향후 표적 방사성 동위원소 치료(Targeted Radionuclide Therapy) 시 실시간 생체 내 선량 모니터링 시스템 설계에 유용한 방법론적 통찰을 제공한다.

---

## References
- [1] Joshi, S.C. and A.A. Sheikh, 3D printing in aerospace and its long-term sustainability. Virtual and Physical Prototyping, 2015. 10(4): p. 175-185.
- [2] Armillotta, A. and R. Pelzer, Modeling of porous structures for rapid prototyping of tissue engineering scaffolds. The International Journal of Advanced Manufacturing Technology, 2008. 39(5): p. 501-511.
- [3] Kermer, C., et al., Colour stereolithography for planning complex maxillofacial tumour surgery. Journal of Cranio-Maxillofacial Surgery, 1998. 26(6): p. 360-362.
- [4] Khoshnevis, B., Automated construction by contour crafting—related robotics and information technologies. Automation in construction, 2004. 13(1): p. 5-19.
- [5] Lipton, J.I., et al., Additive manufacturing for the food industry. Trends in food science & technology, 2015. 43(1): p. 114-123.
- [6] Sun, J., et al., 3D food printing an innovative way of mass customization in food fabrication. International Journal of Bioprinting, 2015. 1(1).
- [7] Wegrzyn, T.F., M. Golding, and R.H. Archer, Food Layered Manufacture: A new process for constructing solid foods. Trends in Food Science & Technology, 2012. 27(2): p. 66-72.
- [8] Hazelaar, C., et al., Using 3D printing techniques to create an anthropomorphic thorax phantom for medical imaging purposes. Medical physics, 2018. 45(1): p. 92-100.
- [9] Fisher, T., et al., SU-E-T-328: 3D extrusion based printing of custom bolus using a non-invasive and low cost method. Medical physics, 2013. 40(6Part15): p. 280-280.
- [10] Kim, H., et al., Establishing a process of irradiating small animal brain using a CyberKnife and a microCT scanner. Medical physics, 2014. 41(2): p. 021715.
- [11] Cunha, J., et al., WE-F-16A-01: Commissioning and Clinical Use of PC-ISO for Customized, 3D Printed, Gynecological Brachytherapy Applicators. Medical Physics, 2014. 41(6Part30): p. 514-514.
- [12] Sethi, R., et al., Clinical applications of custom-made vaginal cylinders constructed using three-dimensional printing technology. Journal of contemporary brachytherapy, 2016. 8(3): p. 208.
- [13] Ding, X., et al., WE-F-16A-03: 3D Printer Application in Proton Therapy: A Novel Method to Deliver Passive-Scattering Proton Beams with a Fixed Range and Modulation for SRS and SRT. Medical Physics, 2014. 41(6Part30): p. 514-514.
- [14] Ju, S.G., et al., New technique for developing a proton range compensator with use of a 3-dimensional printer. International Journal of Radiation Oncology* Biology* Physics, 2014. 88(2): p. 453-458.
- [15] Farahani, R.D., et al., Direct-write fabrication of freestanding nanocomposite strain sensors. Nanotechnology, 2012. 23(8): p. 085502.
- [16] de la Osa, G., et al., Printing of graphene nanoplatelets into highly electrically conductive three-dimensional porous macrostructures. Chemistry of Materials, 2016. 28(17): p. 6321-6328.
- [17] Flowers, P.F., et al., 3D printing electronic components and circuits with conductive thermoplastic filament. Additive Manufacturing, 2017. 18: p. 156-163.
- [18] Mishnayot, Y., et al., Three-dimensional printing of scintillating materials. Review of Scientific Instruments, 2014. 85(8): p. 085102.
- [19] Dosovitskiy, G., et al., First 3D-printed complex inorganic polycrystalline scintillator. CrystEngComm, 2017. 19(30): p. 4260-4264.
- [20] Stowell, P., et al., 3D Printing Neutron Detectors using BN/ZnS Resin.
- [21] Kim, D.-g., et al., Performance of 3D printed plastic scintillators for gamma-ray detection. Nuclear Engineering and Technology, 2020. 52(12): p. 2910-2917.
- [22] Fargher, S., C. Steer, and L. Thompson. The use of 3D printing in the development of gaseous radiation detectors. in EPJ Web of Conferences. 2018. EDP Sciences.
- [23] Lynch, N., T. Monajemi, and J.L. Robar, Characterization of novel 3D printed plastic scintillation dosimeters. Biomedical Physics & Engineering Express, 2020. 6(5): p. 055014.
- [24] Rodnyi, P.A., Physical processes in inorganic scintillators. 2020: CRC press.
- [25] Nikl, M., Scintillation detectors for x-rays. Measurement Science and Technology, 2006. 17(4): p. R37.
- [26] Van Eijk, C.W., Inorganic scintillators in medical imaging. Physics in medicine and biology, 2002. 47(8): p. R85-R106.
- [27] Greskovich, C. and S. Duclos, Ceramic scintillators. Annual review of materials science, 1997. 27(1): p. 69-88.
- [28] Duclos, S.J., et al., Development of the HiLightTM scintillator for computed tomography medical imaging. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, 2003. 505(1-2): p. 68-71.
- [29] Greskovich, C.D., et al., Ceramic scintillators for advanced, medical X-ray detectors. American Ceramic Society Bulletin, 1992. 71(7): p. 1120-1130.
- [30] Wakefield, G., et al., Luminescence properties of nanocrystalline Y2O3: Eu. Advanced Materials, 2001. 13(20): p. 1557-1560.
- [31] Rahman, A.M., et al., Germanium-doped optical fiber for real-time radiation dosimetry. Radiation Physics and Chemistry, 2015. 116: p. 170-175.
- [32] Rahman, A.M., et al., Ge-doped silica optical fibres as RL/OSL dosimeters for radiotherapy dosimetry. Sensors and Actuators A: Physical, 2017. 264: p. 30-39.
- [33] Archambault, L., et al., Water-equivalent dosimeter array for small-field external beam radiotherapy. Medical physics, 2007. 34(5): p. 1583-1592.
- [34] Moon, J., et al., Water-equivalent one-dimensional scintillating fiber-optic dosimeter for measuring therapeutic photon beam. Applied Radiation and Isotopes, 2012. 70(11): p. 2627-2630.
- [35] Linares Rosales, H.M., et al., Optimization of a multipoint plastic scintillator dosimeter for high dose rate brachytherapy. Medical physics, 2019. 46(5): p. 2412-2421.
- [36] Suchowerska, N., et al., A fibre optic dosimeter customised for brachytherapy. Radiation measurements, 2007. 42(4-5): p. 929-932.
- [37] Johansen, J.G., et al., Time-resolved in vivo dosimetry for source tracking in brachytherapy. Brachytherapy, 2018. 17(1): p. 122-132.
- [38] Kertzscher, G. and S. Beddar, Ruby-based inorganic scintillation detectors for 192Ir brachytherapy. Physics in Medicine & Biology, 2016. 61(21): p. 7744.
- [39] Kertzscher, G. and S. Beddar, Inorganic scintillation detectors for 192Ir brachytherapy. Physics in Medicine & Biology, 2019. 64(22): p. 225018.
- [40] Belley, M.D., et al., Real-time dose-rate monitoring with gynecologic brachytherapy: results of an initial clinical trial. Brachytherapy, 2018. 17(6): p. 1023-1029.
- [41] Byrne, K., et al., Initial evaluation of the performance of novel inorganic scintillating detectors for small animal irradiation dosimetry. IEEE Sensors Journal, 2020. 20(9): p. 4704-4712.
- [42] Stanton, I.N., et al., Europium-and lithium-doped yttrium oxide nanocrystals that provide a linear emissive response with X-ray radiation exposure. Nanoscale, 2014. 6(10): p. 5284-5288.
- [43] Moore, B., Development and Validation of Precision in Small Animal Radiotherapy Dose Monitoring. 2018, Duke University.
- [44] Smiley, B.R., Validation of Isodose Curves for AIRO Mobile CT, P-32 Pure-Beta and I-131 Mixed. 2019, Duke University.
- [45] Schaal, J.L., et al., Injectable polypeptide micelles that form radiation crosslinked hydrogels in situ for intratumoral radiotherapy. Journal of Controlled Release, 2016. 228: p. 58-66.
- [46] Povoski, S.P., et al., A comprehensive overview of radioguided surgery using gamma detection probe technology. World journal of surgical oncology, 2009. 7(1): p. 1-63.
- [47] Collamati, F., et al., Toward radioguided surgery with β− decays: uptake of a somatostatin analogue, DOTATOC, in meningioma and high-grade glioma. Journal of Nuclear Medicine, 2015. 56(1): p. 3-8.
- [48] Stendahl, J.C., et al., Prototype device for endoventricular beta-emitting radiotracer detection and molecularly-guided intervention. Journal of Nuclear Cardiology, 2020: p. 1-14.
- [49] Daghighian, F., et al., Intraoperative beta probe: a device for detecting tissue labeled with positron or electron emitting isotopes during surgery. Medical physics, 1994. 21(1): p. 153-157.
- [50] Hong, S., et al., Feasibility study on development of a fiber-optic dual detector to measure beta-And gamma-rays simultaneously. The Transactions of The Korean Institute of Electrical Engineers, 2014. 63(2): p. 284-290.
- [51] Langloss, B., The Design, Synthesis and Characterization of Lanthanide-based Nanomaterials and Their Use in 3D Biological Imaging and Radiation Dosimetry. 2018, Duke University.
- [52] Behrens, R., A spectrometer for pulsed and continuous photon radiation. Journal of Instrumentation, 2009. 4(03): p. P03027.
- [53] Brady, S.L., Accurate Determination of Radiation Dose in Mice Using Orthovoltage X-ray and [Cs-137] Irradiators. 2007, Duke University.
- [54] Attix, F., Energy-absorption coefficients for γ-rays in compounds or mixtures. Physics in Medicine & Biology, 1984. 29(7): p. 869.
- [55] Nečas, D. and P. Klapetek, Gwyddion-Free SPM (AFM, SNOM/NSOM, STM, MFM,...) data analysis software.
- [56] Klapetek, P., et al., Methods for determining and processing 3D errors and uncertainties for AFM data analysis. Measurement Science and Technology, 2011. 22(2): p. 025501.
- [57] van Hoof, S.J., P.V. Granton, and F. Verhaegen, Development and validation of a treatment planning system for small animal radiotherapy: SmART-Plan. Radiotherapy and Oncology, 2013. 109(3): p. 361-366.
- [58] Le Deroff, C., et al., In vivo surface dosimetry with a scintillating fiber dosimeter in preclinical image-guided radiotherapy. Medical physics, 2020. 47(1): p. 234-241.
- [59] Woods, R.J. and A.K. Pikaev, Applied radiation chemistry: radiation processing. 1993: John Wiley & Sons.
- [60] El-Farahaty, K., A. Sadik, and A. Hezma, γ-Irradiation effects on opto-thermal and-mechanical properties of PET and PETG fibers. International Journal of Polymeric Materials, 2009. 58(7): p. 366-383.
- [61] Prasad, S.G., A. De, and U. De, Structural and optical investigations of radiation damage in transparent PET polymer films. International Journal of Spectroscopy, 2011. 2011.
- [62] Belley, M.D., et al., Fiber-optic detector for real time dosimetry of a micro-planar x-ray beam. Medical physics, 2015. 42(4): p. 1966-1972.
- [63] Desimoni, E. and B. Brunetti, About estimating the limit of detection by the signal to noise approach. 2015.
- [64] Currie, L.A., Nomenclature in evaluation of analytical methods including detection and quantification capabilities (IUPAC Recommendations 1995). Pure and applied chemistry, 1995. 67(10): p. 1699-1723.
- [65] Currie, L.A., Detection in analytical chemistry. Importance, theory, and practice. 1988.
- [66] Currie, L.A., Lower limit of detection: definition and elaboration of a proposed position for radiological effluent and environmental measurements. 1984, National Bureau of Standards, Washington, DC (USA).
- [67] Hyatt, S.P., Chest Phantom Development for Chest X-ray Radiation Protection Surveys, Internal. 2018, Duke University.
- [68] Hissoiny, S., et al., GPUMCD: a new GPU-oriented Monte Carlo dose calculation platform. Medical physics, 2011. 38(2): p. 754-764.
- [69] Dedulle, A., et al., Two-step validation of a Monte Carlo dosimetry framework for general radiology. Physica Medica, 2018. 53: p. 72-79.
- [70] Morales, J.E., et al., A comparison of surface doses for very small field size x-ray beams: Monte Carlo calculations and radiochromic film measurements. Australasian physical & engineering sciences in medicine, 2014. 37(2): p. 303-309.
- [71] Howard, D.M., et al., Comparison of I-131 radioimmunotherapy tumor dosimetry: unit density sphere model versus patient-specific Monte Carlo calculations. Cancer Biotherapy and radiopharmaceuticals, 2011. 26(5): p. 615-621.
- [72] Furhang, E.E., C.S. Chui, and G. Sgouros, A Monte Carlo approach to patient-specific dosimetry. Medical physics, 1996. 23(9): p. 1523-1529.
- [73] Furhang, E.E., G. Sgouros, and C.S. Chui, Radionuclide photon dose kernels for internal emitter dosimetry. Medical physics, 1996. 23(5): p. 759-764.
- [74] Neshasteh-Riz, A., et al., DNA damage induced in glioblastoma cells by I-131: a comparison between experimental data and Monte Carlo simulation. Cell Journal (Yakhteh), 2012. 14(1): p. 25.
- [75] Ferrari, A., et al., FLUKA: a multi-particle transport code. 2005, Citeseer.
- [76] Böhlen, T., et al., The FLUKA code: developments and challenges for high energy and medical applications. Nuclear data sheets, 2014. 120: p. 211-214.
- [77] Moore, B., et al., Patient Dose Comparison for Intraoperative Imaging Devices Used in Orthopaedic Lumbar Spinal Surgery. JAAOS Global Research & Reviews, 2018. 2(7).
- [78] Prestwich, W.V., J. Nunes, and C.S. Kwok, Beta dose point kernels for radionuclides of potential use in radioimmunotherapy. Journal of nuclear medicine, 1989. 30(6): p. 1036-1046.
- [79] Jang, K., et al., Fiber-optic radiation sensor for detection of tritium. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, 2011. 652(1): p. 928-931.
- [80] Azevedo, C., et al. TRITIUM-A Real-Time Tritium Monitor System for Water Quality Surveillance. in 2018 IEEE Nuclear Science Symposium and Medical Imaging Conference Proceedings (NSS/MIC). 2018. IEEE.
- [81] Azevedo, C., et al., Simulation results of a real-time in water tritium monitor. Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment, 2020. 982: p. 164555.
- [82] Pellegrin, S., C. Whitney, and C.G. Wilson. A multichannel nanoparticle scintillation microdevice with integrated waveguides for alpha, beta, gamma, x-ray, and neutron detection. in 19th IEEE International Conference on Micro Electro Mechanical Systems. 2006. IEEE.
- [83] Hong, S.-H., et al., Fabrication and characterization of a fiber-optic alpha/beta detector for nuclear medicine application. Journal of Sensor Science and Technology, 2012. 21(5): p. 367-373.
- [84] Park, C.H., J.H. Moon, and B.K. Seo, Development and characterization of the integrated fiber-optic sensor for remote detection of alpha radiation. Journal of the Korean Physical Society, 2013. 63(9): p. 1720-1723.
- [85] Mata, A., A.J. Fleischman, and S. Roy, Characterization of polydimethylsiloxane (PDMS) properties for biomedical micro/nanosystems. Biomedical microdevices, 2005. 7(4): p. 281-293.
- [86] Sackmann, E.K., A.L. Fulton, and D.J. Beebe, The present and future role of microfluidics in biomedical research. Nature, 2014. 507(7491): p. 181-189.
- [87] Amin, R., et al., 3D-printed microfluidic devices. Biofabrication, 2016. 8(2): p. 022001.
- [88] Ozbolat, V., et al., 3D printing of PDMS improves its mechanical and cell adhesion properties. ACS Biomaterials Science & Engineering, 2018. 4(2): p. 682-693.
- [89] Comina, G., A. Suska, and D. Filippini, PDMS lab-on-a-chip fabrication using 3D printed templates. Lab on a Chip, 2014. 14(2): p. 424-430.
- [90] Montazerian, H., et al., Permeability and mechanical properties of gradient porous PDMS scaffolds fabricated by 3D-printed sacrificial templates designed with minimal surfaces. Acta biomaterialia, 2019. 96: p. 149-160.