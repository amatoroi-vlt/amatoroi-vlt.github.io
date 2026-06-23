---
title: "Characterization of a multi-point scintillation dosimetry research platform for a low-field MR-Linac"
authors: ["Crosby, J.", "Ruff, C.", "Gregg, K.", "Turcotte, J.", "Glide-Hurst, C."]
year: 2024
venue: "Med. Phys."
doi: "10.1002/mp.17192"
arxiv: ""
paper_id: "crosby2024-multi-point-scintillation-dosimetry-mr-linac"
source_pdf: "[[117_nihms-2001734.pdf]]"
tags: [paper, paper/reviewed, topic/scintillation-dosimetry, topic/mr-linac]
aliases: ["Crosby 2024"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Crosby et al. (2024) — Characterization of a multi-point scintillation dosimetry research platform for a low-field MR-Linac

**Venue**: Med. Phys. 2024 Sep; 51(9): 6475–6484.
**DOI**: [10.1002/mp.17192](https://doi.org/10.1002/mp.17192)
**PDF**: ![[117_nihms-2001734.pdf#page=1]]

---

## Executive Summary

본 연구는 0.35T 저자기장 MR-Linac 환경에서 다채널 플라스틱 신틸레이션 검출기(PSD) 시스템인 HYPERSCINT RP-200의 성능을 종합적으로 평가하였다. [[117_nihms-2001734.pdf#page=1|p.1, Abstract]] 실험 결과, 단일 PSD의 반복 측정 표준편차는 0.13% 미만으로 우수한 재현성을 보였다. [[117_nihms-2001734.pdf#page=1|p.1, Results]] 심부선량백분율(PDD) 측정 결과는 기준 데이터와 1.12% 이내의 차이를 보였으며, 10-1000 MU 범위에서 우수한 선형성을 확인하였다. [[117_nihms-2001734.pdf#page=1|p.1, Results]] 결과적으로 이 시스템은 저자기장 MR-Linac 환경에서 실시간 선량 측정을 위한 신뢰할 수 있는 도구임을 입증하였다. [[117_nihms-2001734.pdf#page=1|p.1, Conclusions]]

---

## Problem & Motivation

MRI 유도 방사선 치료(MRgRT)는 연조직 대조도가 우수하고 실시간 게이팅이 가능하다는 장점이 있으나, 자기장 내 선량 측정 시 전자 복귀 효과(ERE) 및 검출기 호환성 문제 등 고유한 도전 과제가 존재한다. [[117_nihms-2001734.pdf#page=1|p.1, Abstract]] 기존의 전리함은 자기장 강도와 방향에 따라 반응이 크게 달라질 수 있어, 물과 등가이고 자기장의 영향을 거의 받지 않는 PSD가 대안으로 주목받고 있다. [[117_nihms-2001734.pdf#page=2|p.2, §1]] 특히 0.35T MR-Linac 시스템(ViewRay MRIdian)의 고유한 특성(90 cm SAD, 6X FFF)에서의 다채널 PSD 성능은 아직 충분히 검증되지 않았다. [[117_nihms-2001734.pdf#page=2|p.2, §1]]

---

## Methods

본 연구에서는 4채널 PSD 시스템(HYPERSCINT RP-200)을 사용하였으며, 각 채널은 광섬유로 연결된 신틸레이터와 하이퍼스펙트럴 광학 판독기로 구성된다. [[117_nihms-2001734.pdf#page=2|p.2, §2]] 
- **교정**: 체렌코프 광과 형광 발생을 보정하기 위한 분광 교정과 전리함(Exradin A28)을 이용한 절대 선량 교정을 수행하였다. [[117_nihms-2001734.pdf#page=3|p.3, §2]]
- **특성 평가**: 반복 측정(1, 5, 10, 14.3 Hz 통합 시간), PDD(9.96 및 6.64 cm² 필드 크기), 자기장에 대한 방향 의존성, 선형성(10-1000 MU) 및 출력 계수를 평가하였다. [[117_nihms-2001734.pdf#page=3|p.3-4, §2]]
- **3D 프린팅 홀더**: 다채널 검출기의 정확한 위치 고정을 위해 FormLabs Form 2 3D 프린터로 제작한 전용 홀더를 사용하였다. [[117_nihms-2001734.pdf#page=4|p.4, §2]]
- **게이팅 실험**: 4D 가동 팬텀(QUASAR MRI4D)을 사용하여 실시간 선량 측정 및 게이팅 정확도를 평가하였다. [[117_nihms-2001734.pdf#page=5|p.5, §2]]

---

## Results

- **반복성 및 PDD**: 1 Hz 통합 시간에서 반복 측정 오차는 -0.06%에서 0.52% 사이였으며, PDD는 전리함 측정값과 0.8 cm 깊이에서 최대 1.03%, 10 cm 깊이에서 1.12%의 차이를 보였다. [[117_nihms-2001734.pdf#page=5|p.5, §3]]
- **자기장 방향 의존성**: 자기장 방향에 따른 반응 차이는 90도에서 최대 -0.32%로 무시할 수 있는 수준이었다. [[117_nihms-2001734.pdf#page=6|p.6, §3]]
- **선형성 및 출력 계수**: 모든 채널에서 MU 전달량에 따른 결정계수 R² = 1.000의 우수한 선형성을 보였으며, 출력 계수 또한 기준 데이터와 잘 일치하였다. [[117_nihms-2001734.pdf#page=6|p.6, §3]]
- **게이팅 성능**: 게이팅 전달 실험에서 누적 선량 오차는 <0.8 cGy였으며, 실시간 측정을 통해 트래킹 알고리즘의 부정확성과 게이팅 파라미터가 전달 효율에 미치는 영향을 확인하였다. [[117_nihms-2001734.pdf#page=6|p.6, §3]]

---

## Critical Review

### 방법론·실험설계 타당성

본 연구는 다채널 PSD 시스템을 MR-Linac 환경에서 평가하기 위해 전용 3D 프린팅 홀더를 제작하여 검출기 위치의 재현성을 확보하려 노력하였다. [[117_nihms-2001734.pdf#page=4|p.4, §2]] 하지만 사용된 수조의 한계로 인해 PSD를 이용한 인라인(inline) 또는 크로스라인(crossline) 선량 프로파일을 효율적으로 획득하지 못한 점은 방법론적 한계로 언급되었다. [[117_nihms-2001734.pdf#page=7|p.7, §4]] 또한 0.35T라는 상대적으로 낮은 자기장에서의 결과이므로, 1.5T 등 고자기장 시스템으로의 직접적인 외삽에는 주의가 필요하다.

### 선행연구 대비 기여도·한계

기존 연구들이 주로 단일 PSD 또는 고자기장(1.5T) 환경에 집중했던 것과 달리, 본 연구는 0.35T MR-Linac에서 다채널 PSD 시스템의 실시간 게이팅 및 선량 측정 능력을 입증했다는 점에 의의가 있다. [[117_nihms-2001734.pdf#page=7|p.7, §4]] 저자들은 향후 소조사면 선량 측정 및 다중 타겟 사례에 대한 추가 평가가 필요함을 명시하였다. [[117_nihms-2001734.pdf#page=8|p.8, §5]]

---

## Implications for Our Research

본 연구에서 활용된 3D 프린팅 기술을 이용한 검출기 고정 장치 제작 및 다채널 PSD의 실시간 보정 방법론은 우리 프로젝트의 신틸레이션 센서 설계 및 검증 단계에서 직접적으로 벤치마킹할 수 있는 요소이다. 특히 자기장 환경에서의 안정적인 성능은 복합 환경용 센서 개발에 중요한 참고 자료가 된다.

---

## References

- [1] Hall WA, Paulson ES, van der Heide UA, et al. The transformation of radiation oncology using real-time magnetic resonance guidance: A review. Eur J Cancer. 2019; 122: 42–52.
- [2] Liney GP, Whelan B, Oborn B, Barton M, Keall P. MRI-Linear Accelerator Radiotherapy Systems. Clin Oncol. 2018; 30: 686–691.
- [3] Simiele F, Kapsch RP, Ankerhold U, Culberson W, DeWerd L. Spectral characterization of plastic scintillation detector response as a function of magnetic field strength. Phys Med Biol. 2018; 63: 085001.
- [4] Spindeldreier CK, Schrenk O, Bakenecker A, et al. Radiation dosimetry in magnetic field with Farmer-type ionization chambers: determination of magnetic field correction factors for different magnetic field strengths and field orientations. Phys Med Biol. 2017; 62(16): 6708–6728.
- [6] Stefanowicz S, Latzel H, Lindvold L, Anderson C, Jakel O, Greilich S. Dosimetry in clinical static magnetic fields using plastic scintillation detectors. Radiat Meas. 2013; 56: 357–360.
- [8] Timakova E, Bazalova-Carter M, Zavgorodni S. Characterization of a 0.8 mm³ Medscint plastic scintillator detector system for small field dosimetry. Phys Med Biol. 2023; 68: 175040.
- [11] Archambault L, Therriault-Proulx F, Beddar S, Beaulieu L. A mathematical formalism for hyperspectral, multipoint plastic scintillation detectors. Phys Med Biol. 2012; 57(21): 7133–7145.
