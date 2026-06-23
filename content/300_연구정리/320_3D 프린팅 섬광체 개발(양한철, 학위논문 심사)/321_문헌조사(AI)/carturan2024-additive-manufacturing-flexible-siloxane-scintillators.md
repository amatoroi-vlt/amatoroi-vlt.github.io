---
title: "Additive manufacturing of high-performance, flexible 3D siloxane-based scintillators through the sol-gel route"
authors: ["Carturan, S. M.", "Skliarova, H.", "Franchin, G.", "Bombardelli, G.", "Zanini, A.", "Pino Andrades, F. E.", "Delgado Alvarez, J. C.", "Moretto, S.", "Maggioni, G.", "Raniero, W.", "Maniglio, D.", "Caricato, A. P.", "Quaranta, A."]
year: 2024
venue: "Applied Materials Today"
doi: "10.1016/j.apmt.2024.102313"
arxiv: ""
paper_id: "carturan2024-additive-manufacturing-flexible-siloxane-scintillators"
source_pdf: "[[102_1-s2.0-S2352940724002580-main_compressed.pdf]]"
tags: [paper, paper/reviewed, topic/additive-manufacturing, topic/scintillators]
aliases: ["Carturan 2024"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 0.867
---

# Carturan et al. (2024) — Additive manufacturing of high-performance, flexible 3D siloxane-based scintillators through the sol-gel route

**Venue**: Applied Materials Today
**DOI**: [10.1016/j.apmt.2024.102313](https://doi.org/10.1016/j.apmt.2024.102313) · **arXiv**: []()
**PDF**: ![[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=1]]

---

## Executive Summary

본 논문은 자외선(UV) 경화가 가능한 메타크릴레이트(methacrylate) 기능기를 포함하는 페닐(phenyl) 기반 실록산(siloxane) 수지를 졸-겔(sol-gel) 합성법으로 제조하여 고성능의 유연한 3D 프린팅 섬광체(scintillator)를 생산하는 새로운 방법을 제안한다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=1|p.1, §Abstract]]. 가수분해(hydrolytic) 및 비가수분해(non-hydrolytic) 졸-겔 방식을 모두 탐색하여 디페닐(diphenyl) 함유 알콕시실란(alkoxysilane) 전구체의 반응성을 촉진하고 상분리(phase separation)를 제어하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=1|p.1, §Abstract]]. 합성된 수지에 적절한 형광체(fluorophores)를 첨가한 후 디지털 광 처리(Digital Light Processing, DLP) 3D 프린팅 기술을 적용하여 자이로이드(gyroid) 및 켈빈 셀(Kelvin cell)과 같은 복잡한 형상의 섬광체를 성공적으로 제작하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=1|p.1, §Abstract]]. 제작된 섬광체는 알파(α) 입자 조사 시 상용 플라스틱 섬광체(EJ-212) 대비 최대 44%의 광 수율(light yield)을 보였으며, 4.5 MeV 양성자(H+) 빔 조사에서도 우수한 섬광 성능과 방사선 내성을 입증하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=1|p.1, §Abstract]].

---

## Problem & Motivation

유기 섬광체는 방사선 치료(예: 양성자 치료) 시 선량 분포를 정밀하게 재구성하기 위해 조직 등가성(tissue equivalence)과 빠른 응답 속도를 제공하므로 선량계(dosimeter)로 널리 사용된다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=1|p.1, §1. Introduction]]. 기존의 강성(rigid) 고분자 매트릭스(예: 폴리스티렌, 폴리비닐톨루엔) 기반 플라스틱 섬광체는 복잡한 해부학적 구조를 모방하거나 환자 맞춤형 볼루스(bolus) 및 변형 가능한 팬텀(deformable phantom)으로 사용하기에 유연성이 부족하다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=2|p.2, §1. Introduction]]. 실리콘(silicone) 기반 시스템은 유연성을 제공하지만, 상용 수지의 제약으로 인해 광 수율이 낮아 다양한 응용 분야에 적용하기 어렵다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=2|p.2, §1. Introduction]]. 따라서 본 연구는 높은 광 수율, 유연성, 그리고 DLP 3D 프린팅을 통한 복잡한 형상 제작 능력을 동시에 갖춘 새로운 폴리실록산(polysiloxane) 수지를 개발하고자 한다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=2|p.2, §1. Introduction]].

---

## Methods

- **재료 및 합성 (Materials and Synthesis):**
  - 가수분해(Hydrolytic) 경로: MA-TMOS, DP-DMOS, DM-DES, M-TES 전구체를 HCl 촉매(0.1M, 0.5M, 1M) 하에 반응시켜 DPDMM_H-H, DPDMM_M-H, DPDMM_L-H 수지를 합성하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=3|p.3, §2.2.1. Hydrolytic sol-gel process]].
  - 비가수분해(Non-hydrolytic) 경로: MA-TMOS, DPSi(OH)2, DM-DES 전구체를 Ba(OH)2 촉매 하에 반응시켜 DPDM50-NH, DPDM60-NH, DP50-NH 수지를 합성하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=3|p.3, §2.2.2. Non-hydrolytic condensation]].
- **광경화성 제형 (Photocurable formulations):** 합성된 액상 수지에 광개시제(TPO, 1% wt.), 1차 염료(PPO, 1% wt.), 파장 천이기(Lumogen Violet, 0.02% wt.)를 첨가하여 60 °C에서 교반하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=4|p.4, §2.3. Photocurable formulations and UV curing]].
- **3D 프린팅 (3D Printing):** DLP 프린터(Pico 2, Asiga)를 사용하여 385 nm 파장, 30 mW/cm² 광 강도, 62 μm 픽셀 크기 조건에서 자이로이드(gyroid) 및 켈빈 셀(Kelvin cell) 구조(11.5 × 11.5 × 11.5 mm³)를 출력하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=5|p.5, §2.6. DLP printing of selected scintillator formulations]]. 층 두께(layer height)는 50~150 μm, 조사 시간은 3~16초로 최적화하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=11|p.11, Table 4]].
- **특성 평가 (Characterization):** FTIR 분광법으로 화학 구조를 분석하고, 회전 유변물성계(rotational rheometer)로 광유변학적(photorheological) 특성을 평가하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=4|p.4, §2.4. Analytical techniques]]. 인장 시험(tensile tests)을 통해 기계적 물성을 측정하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=5|p.5, §2.4. Analytical techniques]].
- **섬광 성능 평가 (Scintillation measurements):** 241Am 알파 소스(~5.5 MeV)를 사용하여 광 수율과 감쇠 시간(decay time)을 측정하고 상용 플라스틱 섬광체(EJ-212)와 비교하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=5|p.5, §2.5. Light yield measurements]]. 또한 4.5 MeV 양성자 빔을 조사하여 CCD 카메라로 빔 스팟 이미지를 획득하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=5|p.5, §2.7. Proton beam irradiation of disks and 3D printed shapes]].

---

## Results

- **광 수율 (Light Yield):** 비가수분해 경로로 합성된 DPDM50-NH 수지는 알파 입자 조사 시 상용 EJ-212 섬광체 대비 44 ± 5%의 가장 높은 광 수율을 기록하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=9|p.9, Table 2]]. 가수분해 경로의 DPDMM_L-H 수지는 33 ± 4%의 광 수율을 보였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=9|p.9, Table 2]].
- **감쇠 시간 (Decay Time):** 모든 샘플은 이중 지수 감쇠(bi-exponential decay) 특성을 보였으며, 빠른 성분(fast component)은 4.7~8.8 ns, 느린 성분(slow component)은 15.0~52.6 ns 범위로 측정되었다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=9|p.9, Table 2]].
- **기계적 물성 (Mechanical Properties):** DPDM60-NH 프린팅 샘플은 인장 강도 0.39 ± 0.22 MPa, 파단 연신율(strain at break) 22 ± 8%를 기록하여 엘라스토머(elastomeric) 특성을 나타냈다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=13|p.13, Table 5]]. 반면 DPDM50-NH 프린팅 샘플은 인장 강도 0.07 ± 0.01 MPa, 파단 연신율 25 ± 2%로 선형 탄성(linear elasticity) 거동을 보였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=13|p.13, Table 5]].
- **3D 프린팅 해상도 (3D Printing Resolution):** SEM 분석 결과, DPDM_M-H 자이로이드 구조의 벽 두께는 약 390 μm로 설계값(400 μm)과 잘 일치하여 약 20%의 균일한 선형 수축(linear shrinkage)을 보이며 우수한 프린팅 충실도를 입증하였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=12|p.12, §3.5. 3D printing of selected formulations through DLP]].
- **양성자 빔 조사 (Proton Beam Irradiation):** 4.5 MeV 양성자 빔 조사 시 3D 프린팅된 자이로이드 구조는 102초 동안 3 × 10^13 H+/cm²의 플루언스(fluence)에 노출된 후에도 신호 강도의 뚜렷한 저하 없이 강하고 안정적인 섬광 신호를 유지하여 우수한 방사선 내성을 보여주었다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=13|p.13, §3.6. Proton beam irradiation of disks and 3D printed shapes]].

---

## Critical Review

### 방법론·실험설계 타당성

- 저자들은 가수분해 및 비가수분해 졸-겔 합성법을 모두 체계적으로 비교 분석하였으며, FTIR, 광유변학, 인장 시험 등 다양한 분석 기법을 교차 검증하여 결론의 신뢰성을 높였다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=4|p.4, §2.4. Analytical techniques]].
- 평가자 해석: 3D 프린팅된 샘플과 캐스팅(casting)된 샘플 간의 기계적 물성 차이를 명확히 제시하고, 프린팅 과정에서 발생하는 층간 결함(defects between layers)이 물성 저하의 원인임을 객관적으로 분석한 점이 타당하다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=12|p.12, §3.5. 3D printing of selected formulations through DLP]].
- 다만, 양성자 빔 조사 실험에서 빔 전류의 불안정성(16~18 nA 변동)이 존재했음을 명시하였으나, 정량적인 광 수율 열화율(degradation rate) 수치가 부족한 점은 아쉽다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=13|p.13, §3.6. Proton beam irradiation of disks and 3D printed shapes]].

### 선행연구 대비 기여도·한계

- 기존의 강성 플라스틱 섬광체나 광 수율이 낮은 실리콘 섬광체의 한계를 극복하고, 높은 광 수율(EJ-212 대비 44%)과 유연성을 동시에 갖춘 3D 프린팅용 실록산 수지를 최초로 개발한 점에서 Novelty가 매우 높다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=2|p.2, §1. Introduction]].
- 저자 명시 한계: 비가수분해 졸-겔 반응에서 미반응 실란올(silanol) 그룹이 잔존하여 가교 네트워크의 결함을 유발할 수 있으며, 이는 기계적 강도에 영향을 미친다 [[102_1-s2.0-S2352940724002580-main_compressed.pdf#page=7|p.7, §3.1.2. Non hydrolytic sol-gel process]].
- 추가 식별 한계: 감쇠 시간(decay time)의 빠른 성분이 4.7~8.8 ns로 상용 EJ-212(3.7 ns)보다 다소 느려, 초고속 타이밍(ultra-fast timing)이 요구되는 응용 분야에는 추가적인 형광체 최적화가 필요할 수 ---
---

## Implications for Our Research

- 본 연구에서 제시된 비가수분해 졸-겔 기반의 폴리실록산 수지 합성법은 유연하면서도 높은 광 수율을 요구하는 환자 맞춤형 3D 프린팅 선량계 개발에 직접적으로 응용될 수 있다.
- 특히, 자이로이드와 같은 복잡한 다공성 구조를 높은 해상도로 프린팅할 수 있는 기술은 체내 삽입형 방사선 검출기나 복잡한 해부학적 구조를 모방한 팬텀 제작 연구에 중요한 기초 자료를 제공한다.
- 향후 우리 연구에서는 본 논문의 수지 제형을 바탕으로 감쇠 시간을 단축시킬 수 있는 새로운 형광체 조합을 탐색하거나, 프린팅 층간 결함을 최소화하기 위한 후처리(post-curing) 공정 최적화 연구를 진행할 수 있을 것이다.

---

## References

- [1] M. Pari, G. Ballerini, A. Berra, R. Boanta, M. Bonesini, C. Brizzolari, G. Brunetti, M. Calviani, S. Carturan, M.G. Catanesi, S. Cecchini, A. Coffani, F. Cindolo, G. Collazuol, E. Conti, F. Dal Corso, G. De Rosa, C. Delogu, A. Gola, R.A. Intonti, C. Jollet, Y. Kudenko, M. Laveder, A. Longhin, P.F. Loverre, L. Ludovici, L. Magaletti, G. Mandrioli, A. Margotti, V. Mascagna, N. Mauri, A. Meregaglia, M. Mezzetto, M. Nessi, A. Paoloni, E. Parozzi, L. Pasqualini, G. Paternoster, L. Patrizii, C. Piemonte, M. Pozzato, F. Pupilli, M. Prest, E. Radicioni, C. Riccio, A. C. Ruggeri, G. Sirri, M. Soldani, M. Tenti, M. Torti, F. Terranova, E. Vallazza, M. Vesco, L. Votano, Shashlik calorimeters: Novel compact prototypes for the ENUBET experiment, Nucl Instrum Methods Phys Res A (2019) 936, https://doi.org/10.1016/j.nima.2018.11.041.
- [2] A. Boyarintsev, A. De Roeck, S. Dolan, A. Gendotti, B. Grynyov, U. Kose, S. Kovalchuk, T. Nepokupnaya, A. Rubbia, D. Sgalaberna, T. Sibilieva, X.Y. Zhao, Demonstrating a single-block 3D-segmented plastic-scintillator detector, Journal of Instrumentation 16 (2021) P12010, https://doi.org/10.1088/1748-0221/16/12/P12010.
- [11] S. Berns, F. Boillat, A. Boyarintsev, A. De Roeck, S. Dolan, A. Gendotti, B. Grynyov, S. Hugon, U. Kose, S. Kovalchuk, B. Li, A. Rubbia, T. Sibilieva, D. Sgalaberna, T. Weber, J. Wuthrich, X.Y. Zhao, Additive manufacturing of fine-granularity optically-isolated plastic scintillator elements, Journal of Instrumentation 17 (2022), https://doi.org/10.1088/1748-0221/17/10/P10045.
- [19] S.M. Carturan, A. Quaranta, Polysiloxane-Based Scintillators, in: M. Hamel (Ed.), Plastic scintillators, Springer Cham, 2021, pp. 169–199, https://doi.org/10.1007/978-3-030-73488-6.