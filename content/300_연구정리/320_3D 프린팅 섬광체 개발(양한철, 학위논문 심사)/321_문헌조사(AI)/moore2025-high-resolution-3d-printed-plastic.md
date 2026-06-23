---
title: "High-resolution 3D-printed plastic scintillators with tertiary dye"
authors: ["Moore, C.J.", "Febbraro, M.", "Manfredi, J.J.", "Wood, A.", "Rutstrom, D.", "Ruland, T.", "Hackett, B.", "Hausladen, P.A."]
year: 2025
venue: "Journal of Instrumentation"
doi: "10.1088/1748-0221/20/10/P10043"
arxiv: ""
paper_id: "moore2025-high-resolution-3d-printed-plastic"
source_pdf: "[[003_Moore_2025_J._Inst._20_P10043.pdf]]"
tags: [paper, paper/reviewed, topic/scintillator-3d-printing]
aliases: ["Moore 2025"]
status: reviewed
analyzed_at: 2025-02-24
verification_pass_rate: 0.14
---

# Moore et al. (2025) — High-resolution 3D-printed plastic scintillators with tertiary dye

**Venue**: Journal of Instrumentation
**DOI**: [10.1088/1748-0221/20/10/P10043](https://doi.org/10.1088/1748-0221/20/10/P10043) · **arXiv**: []()
**PDF**: ![[003_Moore_2025_J._Inst._20_P10043.pdf#page=1]]

---

## Executive Summary

본 연구는 405 nm 경화광을 사용하는 광경화성 수지 기반 3D 프린팅에서 고해상도 플라스틱 섬광체를 제작하기 위해 3차 염료(tertiary dye)인 coumarin 450을 포함하는 새로운 배합을 제시한다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=2|p.2, §Abstract]] 3차 염료의 도입은 발광 스펙트럼과 광출력에 미치는 영향을 최소화하면서도 프린팅 해상도를 크게 향상시켜, 지지대 없는 구조물은 0.7 mm, 완전히 지지되는 구조물은 0.1 mm 이하의 해상도까지 구현 가능하게 하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=2|p.2, §Abstract]] 제작된 3D 프린팅 섬광체는 상용 EJ-200 섬광체 대비 최대 50%의 광출력을 보였으며, 0.9–1.1 MeVee 영역에서 최대 1.35의 펄스 파형 판별(PSD) 성능 지수(Figure of Merit, FoM)를 달성하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=2|p.2, §Abstract]]

---

## Problem & Motivation

광중합(photopolymerization) 방식을 이용한 플라스틱 섬광체의 적층 제조(Additive Manufacturing, AM)는 전통적으로 광출력(Light Output, LO)과 경화 속도 간의 상충 관계(trade-off)라는 문제에 직면해 있다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=3|p.3, §2]] 특히 표준적인 405 nm 파장의 경화광을 사용할 경우, 빛의 평균 자유 행로(mean free path)가 길어 수지 통 내부 깊숙이 빛이 침투하게 되고, 이는 의도한 층을 넘어선 과도한 중합 반응을 일으켜 프린팅 해상도를 심각하게 저하시킨다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=3|p.3, §2]] 기존에는 빛의 침투를 제한하기 위해 bis-MSB와 같은 2차 형광체의 농도를 조절하는 방식이 사용되었으나, 이는 섬광 효율을 희생시키는 결과를 초래하므로 경화 심도 제어와 섬광 성능 최적화를 분리할 수 있는 새로운 접근법이 필요하다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=4|p.4, §2]]

---

## Methods

연구진은 비방향족(non-aromatic) 아크릴레이트 기반 수지를 제조하기 위해 BR-541MB 올리고머, IBOA, HDDMA 단량체를 혼합하였으며, 1차 형광체로 PPO (20 wt.%), 2차 형광체로 exalite 416 (0.5 wt.%), 광개시제로 TPO (0.1 wt.%)를 사용하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=5|p.5, §3.1]] 여기에 405 nm 경화광을 특이적으로 흡수하면서도 라디칼 형성에는 기여하지 않는 coumarin 450을 3차 염료로 도입하여 0.01에서 0.1 wt.% 농도 범위에서 평가하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=5|p.5, §3.1]] 샘플은 Dymax BlueWave FX-1250을 이용한 벌크 광경화 방식과 Prusa SL1S LCD 프린터를 이용한 3D 프린팅 방식(2.2 mW/cm² 강도, 층당 20~45초 경화)으로 각각 제작되었다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=6|p.6, §3.2]] 프린팅 해상도는 3.5 mm에서 0.5 mm 직경의 외부 핀과 내부 구멍을 포함하는 맞춤형 CAD 모델을 통해 측정되었다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=7|p.7, §3.3]] 섬광 성능(광출력 및 PSD)은 Hamamatsu R6231-100 PMT를 사용하여 측정되었으며, 137Cs 선원으로 광교정을 수행하고 아메리슘-베릴륨(Am-Be) 선원으로 중성자/감마선 판별 능력을 상용 EJ-200 및 EJ-276D 섬광체와 비교 평가하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=8|p.8, §3.3]]

---

## Results

0.1 mm 층 두께 기준으로 coumarin 450의 최적 농도는 0.04 wt.%, 층당 경화 시간은 30초로 확인되었으며, 이 조건에서 최소 외부 비지지 구조 해상도 0.7 mm, 내부 구조 해상도 1.8 mm를 달성하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=14|p.14, §4.4]] 3차 염료 배합(three-dye formula)으로 출력된 복잡한 기하학적 구조(F-16 및 F-104 항공기 모델)는 2차 염료 배합(two-dye formula)에 비해 과중합 및 층간 번짐 현상이 현저히 감소하여 서브 밀리미터 수준의 미세 형상을 성공적으로 구현하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=16|p.16, §4.5]] 벌크 광경화된 2차 염료 샘플은 EJ-200 대비 48.5%의 상대 광출력을 보인 반면, 3D 프린팅된 2차 염료 및 3차 염료 샘플은 각각 36.4%와 35.2%의 광출력을 기록하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=18|p.18, §4.6]] 모든 샘플은 PSD 성능을 입증하였으며, 0.9–1.1 MeVee 컷 기준 FoM 값은 EJ-276D가 2.22, 벌크 광경화 2차 염료 샘플이 1.35, 3D 프린팅 2차 염료 샘플이 1.29, 3D 프린팅 3차 염료 샘플이 1.20으로 나타났다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=19|p.19, §4.6]] 프린팅 직후 PPO와 TPO의 상호작용으로 인해 모든 섬광체에서 뚜렷한 보라색 변색이 관찰되었으나, 이는 실온에서 14일에 걸쳐 자연적으로 소실되었다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=10|p.10, §4.2]]

---

## Critical Review

### 방법론·실험설계 타당성
- 저자들은 3D 프린팅 해상도를 정량적으로 평가하기 위해 외부 핀과 내부 구멍을 포함하는 맞춤형 테스트 객체를 설계하여 체계적으로 분석하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=7|p.7, §3.3]]
- 광출력 및 PSD 성능 평가 시 상용 섬광체(EJ-200, EJ-276D)를 대조군으로 사용하여 객관적인 비교 기준을 제공하였다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=8|p.8, §3.3]]
- 평가자 해석: 3D 프린팅 과정에서 발생하는 열과 산소 노출이 섬광 성능 저하의 주요 원인으로 지목되었으나, 이를 통제하기 위한 불활성 기체 환경이나 적극적인 냉각 시스템을 적용한 추가 실험이 수행되지 않은 점은 아쉽다.

### 선행연구 대비 기여도·한계
- 기존 연구들이 경화 심도 제어를 위해 2차 형광체의 농도를 조절하여 섬광 효율을 희생했던 것과 달리, 본 연구는 3차 염료(coumarin 450)를 독립적으로 도입하여 섬광 성능 저하 없이 프린팅 해상도를 획기적으로 개선했다는 점에서 독창적인 기여를 한다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=4|p.4, §2]]
- 저자 명시 한계: 비방향족(non-aromatic) 기반 수지를 사용함에 따라 상용 플라스틱 섬광체 대비 절대적인 광출력이 낮으며, 3D 프린팅 과정 중 산소 유입으로 인한 소광(quenching) 효과가 발생한다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=18|p.18, §4.6]]
- 추가 식별 한계: 프린팅 직후 발생하는 보라색 변색이 자연적으로 사라지기까지 14일이 소요되므로, 즉각적인 현장 적용이나 빠른 생산 주기에는 제약이 될 수 있다. [[003_Moore_2025_J._Inst._20_P10043.pdf#page=10|p.10, §4.2]]

---

## Implications for Our Research

- 3차 염료를 활용한 경화 심도 제어 기법은 복잡한 내부 구조를 갖는 맞춤형 방사선 선량계나 마이크로플루이딕스 기반 검출기 제작에 직접적으로 응용될 수 있다. (Methods 및 Results 섹션 참조)
- 비방향족 수지의 한계를 극복하기 위해, 향후 연구에서는 프린팅 해상도를 유지하면서도 방향족 단량체 비율을 높일 수 있는 새로운 광개시제 시스템이나 무산소 프린팅 환경 구축에 집중할 필요가 있다.

---

## References

- [1] M.G. Schorr and F.L. Torney, Solid Non-Crystalline Scintillation Phosphors, Phys. Rev. 80 (1950) 474.
- [2] J.B. Birks, Photophysics of aromatic molecules, Wiley monographs in chemical physics, Wiley-Interscience (1970).
- [3] Y. Kim et al., 3D printable polyvinyltoluene-based plastic scintillators with pulse shape discrimination, Nucl. Instrum. Meth. A 1055 (2023) 168537.
- [4] C. Chandler et al., Influence of fluorescent dopants on the vat photopolymerization of acrylate-based plastic scintillators for application in neutron/gamma pulse shape discrimination, Addit. Manuf. 73 (2023) 103688.
- [5] K.J. Glennon et al., 3D printed field-deployable microfluidic systems for the separation and assay of Pu in nuclear forensics, Lab Chip 22 (2022) 4493.
- [6] 3DET collaboration, Additive manufacturing of fine-granularity optically-isolated plastic scintillator elements, 2022 JINST 17 P10045 [arXiv:2202.10961].
- [7] T. Weber et al., Additive manufacturing of a 3D-segmented plastic scintillator detector for tracking and calorimetry of elementary particles, Commun. Eng. 4 (2025) 41 [arXiv:2312.04672].
- [8] B. Hackett et al., Light response of poly(ethylene 2,6-naphthalate) to neutrons, Nucl. Instrum. Meth. A 1069 (2024) 169900 [arXiv:2204.02866].
- [9] V. Anand et al., Development and Characterization of Digital Light Processing-Based 3D-Printed Plastic Scintillator for Radiation Detection, IEEE Trans. Nucl. Sci. 72 (2025) 1947.
- [10] A. Lim et al., Plastic scintillators with efficient light output and pulse shape discrimination produced via photoinitiated polymerization, J. Appl. Polymer Sci. 136 (2018) 47381.
- [11] B.G. Frandsen et al., Fast-, Light-Cured Scintillating Plastic for 3D-Printing Applications, J. Nucl. Eng. 4 (2023) 241.
- [12] T.D. Doležal et al., Manufacturing and characterization of a boron-loaded fast-cured plastic organic scintillator, Nucl. Instrum. Meth. A 1056 (2023) 168602.
- [13] Y. Mishnayot et al., Three-dimensional printing of scintillating materials, Rev. Sci. Instrum. 85 (2014) 085102 [arXiv:1406.4817].
- [14] J. Son et al., Improved 3D Printing Plastic Scintillator Fabrication, J. Korean Phys. Soc. 73 (2018) 887.
- [15] F.D. Brooks, A scintillation counter with neutron and gamma-ray discriminators, Nucl. Instrum. Meth. 4 (1959) 151.
- [16] N. Zaitseva et al., Plastic scintillators with efficient neutron/gamma pulse shape discrimination, Nucl. Instrum. Meth. A 668 (2012) 88.
- [17] C.J. Moore, Automated additive layering of vat polymerized plastic organic scintillators, M.Sc. thesis, Air Force Institute of Technology, Wright-Patterson AFB, OH, U.S.A. (2023).
- [18] formlabs, Guide to Resin 3D Printers: SLA vs. DLP vs. MSLA vs. LCD, https://formlabs.com/blog/resin-3d-printer-comparison-sla-vs-dlp/.
- [19] A. Novokhatska et al., Densification and rheological behaviors of 8YSZ powders for Vat photopolymerization-based additive manufacturing, Open Ceramics 18 (2024) 100615.
- [20] G. Dietze and H. Klein, Gamma-calibration of NE 213 scintillation counters, Nucl. Instrum. Meth. 193 (1982) 549.
- [21] U. Brackmann, Lambdachrome Laser Dyes, Lambda Physik AG, Göttingen, Germany (1986).
- [22] Luxottica Exciton, Laser Dyes — Laser & Fluorescent Dyes, https://exciton.luxottica.com/laser-dyes.html?dye_category=33.
- [23] Hamamatsu, Flat panel type multianode PMT assembly H12700 series / H14220 series https://www.hamamatsu.com/content/dam/hamamatsu-photonics/sites/documents/99_SALES_LIBRARY/etd/H12700_H14220_TPMH1379E.pdf.
- [24] Eljen Technology, Pulse Shape Discrimination — EJ-276D & EJ-276G, https://eljentechnology.com/products/plastic-scintillators/ej-276.
- [25] Hamamatsu, Photomultiplier Tubes — R928, R928P, R955, R955P, https://www.hamamatsu.com/content/dam/hamamatsu-photonics/sites/documents/99_SALES_LIBRARY/etd/R928_R928P_R955_R955P_TPMS1091E.pdf.
- [26] J.B. Birks, The scintillation process in organic materials — I, in The Theory and Practice of Scintillation Counting, J. Birks, ed., International Series of Monographs in Electronics and Instrumentation, Pergamon (1964), p. 39–67 [DOI:10.1016/b978-0-08-010472-0.50008-2].
- [27] A. Lintereur, J. Ely, J. Stave and B. McDonald, Neutron and Gamma Ray Pulse Shape Discrimination with Polyvinyltoluene, Pacific Northwest National Laboratory, Richland, WA, U.S.A. (2012) [DOI:10.2172/1059208].
- [28] Eljen Technology, Plastic Scintillators, https://eljentechnology.com/products/plastic-scintillators.
