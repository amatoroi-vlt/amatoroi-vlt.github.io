---
title: "Additive manufacturing of fine-granularity optically-isolated plastic scintillator elements"
authors: ["Berns, S.", "Boillat, E.", "Boyarintsev, A.", "De Roeck, A.", "Dolan, S.", "Gendotti, A.", "Grynyov, B.", "Hugon, S.", "Kose, U.", "Kovalchuk, S.", "Li, B.", "Rubbia, A.", "Sibilieva, T.", "Sgalaberna, D.", "Weber, T.", "Wuthrich, J.", "Zhao, X.Y."]
year: 2022
venue: "Journal of Instrumentation"
doi: "10.1088/1748-0221/17/10/P10045"
arxiv: "2202.10961"
paper_id: "berns2022-additive-manufacturing-fine-granularity"
source_pdf: "[[007_Berns_2022_J._Inst._17_P10045.pdf]]"
tags: [paper, paper/reviewed, topic/additive-manufacturing]
aliases: ["Berns 2022"]
status: reviewed
analyzed_at: 2024-05-21
verification_pass_rate: 1.0
---

# Berns et al. (2022) — Additive manufacturing of fine-granularity optically-isolated plastic scintillator elements

**Venue**: Journal of Instrumentation
**DOI**: [10.1088/1748-0221/17/10/P10045](https://doi.org/10.1088/1748-0221/17/10/P10045) · **arXiv**: [2202.10961](https://arxiv.org/abs/2202.10961)
**PDF**: ![[007_Berns_2022_J._Inst._17_P10045.pdf#page=1]]

---

## Executive Summary

3DET 콜라보레이션은 용융 적층 모델링(FDM)을 사용하여 광학적으로 분리된 플라스틱 섬광체 큐브 매트릭스를 3D 프린팅하는 기술을 시연하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=2|p.2, Abstract]]. 폴리스티렌 기반의 섬광 필라멘트와 FDM에 최적화된 새로운 백색 반사체 필라멘트를 개발하고 그 특성을 평가하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=4|p.4, §1]]. 3D 프린팅된 섬광체는 19.0 cm의 기술적 감쇠 길이(technical attenuation length)를 달성하였으며, 반사체 필라멘트는 420 nm 파장에서 92.5%의 반사율을 기록하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=6|p.6, §2.1]] [[007_Berns_2022_J._Inst._17_P10045.pdf#page=8|p.8, §2.2]]. 약 1 mm 두께의 반사체 벽으로 분리된 10 mm 큐브 3×3 매트릭스를 동시 출력하는 데 성공하였고, 균일한 광량(큐브당 약 45 p.e.)과 2% 미만의 낮은 광학적 크로스토크(optical crosstalk)를 확인하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=9|p.9, §3]] [[007_Berns_2022_J._Inst._17_P10045.pdf#page=11|p.11, §3.1-3.2]].

---

## Problem & Motivation

플라스틱 섬광체 검출기는 고에너지 물리학, 의료 영상, 선량 측정 등 다양한 분야에서 입자 추적 및 열량 측정에 사용된다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=3|p.3, §1]]. 미세한 입도(fine-granularity)를 갖는 3차원 분할 활성 물질을 만들기 위해 수백만 개의 작은 섬광체 복셀을 생산하고 조립하는 기존 방식(압출, 사출 성형, 기계 가공 등)은 비용이 많이 들고 정밀한 조립이 어렵다는 한계가 있다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=3|p.3, §1]]. 적층 제조(Additive Manufacturing, AM), 특히 용융 적층 모델링(FDM)은 복잡한 기하학적 구조를 높은 자유도로 빠르고 저렴하게 제작할 수 있는 대안으로 떠오르고 있다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=3|p.3, §1]]. 본 연구는 3DET 콜라보레이션의 일환으로, 광학적으로 분리된 섬광체 큐브 매트릭스를 FDM 방식으로 3D 프린팅하기 위해 섬광체 및 반사체 필라멘트를 개발하고 그 성능을 특성화하는 것을 목표로 한다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=4|p.4, §1]].

---

## Methods

- **섬광체 필라멘트 제작**: 폴리스티렌(Polystyrene)에 2% p-terphenyl (pTP)와 0.05% POPOP를 도핑하고, 필라멘트 끊어짐을 방지하기 위해 가소제로 5% biphenyl을 첨가하여 최적의 조성을 얻었다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=4|p.4, §2]].
- **반사체 필라멘트 제작**: ABS, HIPS, PC, PMMA, PS 등의 폴리머 펠릿에 이산화티타늄(TiO2), 황산바륨(BaSO4), 산화마그네슘(MgO) 등의 반사 안료를 5~30% 중량비로 혼합하여 압출하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=7|p.7, §2.2]].
- **3D 프린팅 장비**: 상용 프린터인 "Roboze One+400"과 "CreatBot Dx2", "CreatBot F430" (다중 재료 출력용)을 사용하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=4|p.4, §2.1]] [[007_Berns_2022_J._Inst._17_P10045.pdf#page=9|p.9, §3]].
- **투명도 및 감쇠 길이 측정**: 10×10×50 mm³ 크기의 3D 프린팅된 섬광체 바를 90Sr 선원에 노출시키고 SiPM(Hamamatsu S13360-1350CS)을 사용하여 거리에 따른 광량을 측정하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=6|p.6, §2.1]].
- **반사율 측정**: 20×20×1 mm³ 크기의 반사체 샘플을 제작하여 420 nm 파장에서의 반사율을 측정하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=8|p.8, §2.2]].
- **매트릭스 성능 평가**: 10 mm 큐브와 ~1 mm 두께의 반사체 벽으로 구성된 3×3 매트릭스를 동시 출력한 후, 우주선 뮤온(cosmic muons)을 이용하여 각 큐브의 광량(Light yield)과 인접 큐브로의 광학적 크로스토크(Optical crosstalk)를 측정하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=9|p.9, §3]] [[007_Berns_2022_J._Inst._17_P10045.pdf#page=10|p.10, §3.1]].

---

## Results

- **섬광체 감쇠 길이**: 3D 프린팅된 섬광체 바의 기술적 감쇠 길이는 19.0 ± 1.4 cm로 측정되었으며, 이는 미세 분할 입자 검출기에 허용 가능한 수준이다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=6|p.6, §2.1]].
- **반사체 반사율**: 20% TiO2를 PMMA 또는 PS와 혼합하여 만든 1 mm 두께의 반사체 층은 420 nm 파장에서 91% 이상의 반사율을 보였으며, 프린팅 파라미터 최적화를 통해 최대 92.5%의 반사율을 달성하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=8|p.8, §2.2]].
- **매트릭스 광량 및 균일성**: 3×3 매트릭스의 각 큐브에서 우주선 뮤온에 의해 생성된 평균 광량은 약 45 광전자(p.e.)로 측정되었으며, 큐브 간 광량이 상당히 균일하게 나타났다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=11|p.11, §3.1]].
- **광학적 크로스토크**: 인접한 큐브로 누출되는 광학적 크로스토크 비율은 2% 미만으로 측정되어, 입자 추적 및 열량 측정을 결합한 응용 분야에 적합함을 확인하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=11|p.11, §3.2]].

---

## Critical Review

### 방법론·실험설계 타당성

저자들은 상용 3D 프린터와 자체 제작한 필라멘트를 사용하여 FDM 방식의 가능성을 성공적으로 입증하였다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=4|p.4, §2.1]]. 감쇠 길이 측정 시 90Sr 선원과 SiPM을 사용하고, 프론트엔드 전자장치(FEE)의 임계값을 조정하여 시스템적 불확실성을 최소화하려 한 점은 타당하다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=6|p.6, §2.1]]. 평가자 해석: 다만, 3×3 매트릭스라는 비교적 소규모의 프로토타입에 대한 결과이므로, 실제 대규모 검출기로 확장할 때의 구조적 안정성이나 대량 생산 시의 품질 균일성에 대한 추가 검증이 필요해 보인다.

### 선행연구 대비 기여도·한계

기존의 기계 가공 및 조립 방식의 한계를 극복하기 위해 섬광체와 반사체를 동시에 3D 프린팅하는 단일 공정을 제시한 것은 큰 기여이다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=3|p.3, §1]] [[007_Berns_2022_J._Inst._17_P10045.pdf#page=11|p.11, §4]]. 저자들도 명시했듯이, 매트릭스 외곽 부분의 기하학적 정밀도가 완벽하지 않으며, 압출기 교체 시 발생하는 반사체 잔여물 문제 등 3D 프린팅 전략의 추가적인 튜닝이 필요하다 [[007_Berns_2022_J._Inst._17_P10045.pdf#page=9|p.9, §3]]. 평가자 해석: 또한, 장기적인 노화 효과(ageing effects)나 방사선 손상에 대한 저항성 평가는 향후 과제로 남아 있다.

---

## Implications for Our Research

이 연구는 복잡한 기하학적 구조를 가진 플라스틱 섬광체 검출기를 FDM 3D 프린팅으로 일체형 제작할 수 있는 가능성을 보여준다. 우리 연구에서 미세 분할 선량계나 복잡한 형태의 방사선 검출기를 설계할 때, 섬광체와 반사체를 동시 출력하는 다중 재료 3D 프린팅 기법을 도입하여 조립 공정을 생략하고 제작 비용을 절감하는 방안을 고려할 수 있다. 특히, TiO2와 PMMA/PS 혼합 필라멘트의 높은 반사율 결과는 자체적인 반사체 필라멘트 개발에 중요한 참고 자료가 될 것이다 (Methods 및 Results 섹션 참조).

---

## References

- [1] A. Blondel et al., A fully active fine grained detector with three readout views, 2018 JINST 13 P02006 [arXiv:1707.01785].
- [2] SoLid collaboration, Performance of a full scale prototype detector at the BR2 reactor for the SoLid experiment, 2018 JINST 13 P05005 [arXiv:1802.02884].
- [3] V. Andreev et al., A high-granularity plastic scintillator tile hadronic calorimeter with APD readout for a linear collider detector, Nucl. Instrum. Meth. A 564 (2006) 144.
- [4] K.V. Wong and A. Hernandez, A review of additive manufacturing, ISRN Mech. Eng. 2012 (2012) 208760.
- [5] FDM Technology, Industrial Manufacturing 3D Printing, http://www.stratasys.com/3d-printers/technologies/fdm-technology.
- [6] The 3D Printed Detector (3DET) project, https://threedet.web.cern.ch.
- [7] S. Berns, A. Boyarintsev, S. Hugon, U. Kose, D. Sgalaberna, A. De Roeck et al., A novel polystyrene-based scintillator production process involving additive manufacturing, 2020 JINST 15 P10019 [arXiv:2011.09859].
- [8] Roboze 3D printer, https://www.roboze.com/en/3d-printers/roboze-one-400.html.
- [9] Creatbot 3D printer, https://www.creatbot.fr.
- [10] LiquidO collaboration, Neutrino Physics with an Opaque Detector, Commun. Phys. 4 (2021) 273 [arXiv:1908.02859].
- [11] R. Tayloe, H.O. Meyer, D.C. Cox, J. Doskow, A. Ferguson, T. Katori et al., A large-volume detector capable of charged-particle tracking, Nucl. Instrum. Meth. A 562 (2006) 198.
- [12] A. Boyarintsev et al., Demonstrating a single-block 3D-segmented plastic-scintillator detector, 2021 JINST 16 P12010 [arXiv:2108.11897].
- [13] CAEN DT5207. 32 channel sipm readout board for cosmic rays veto, https://www.caen.it/products/dt5702.
