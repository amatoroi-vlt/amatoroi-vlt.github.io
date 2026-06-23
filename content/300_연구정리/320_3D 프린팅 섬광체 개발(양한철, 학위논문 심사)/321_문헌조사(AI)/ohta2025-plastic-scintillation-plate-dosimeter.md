---
title: "Characterization of a practically designed plastic scintillation plate dosimeter"
authors: ["Ohta, T.", "Nozawa, Y.", "Ohira, S.", "Nawa, K.", "Yamashita, H.", "Nakagawa, K."]
year: 2025
venue: "Medical Physics"
doi: "10.1002/mp.17904"
arxiv: ""
paper_id: "ohta2025-plastic-scintillation-plate-dosimeter"
source_pdf: "[[125_MP-52-0.pdf]]"
tags: [paper, paper/reviewed, topic/plastic-scintillation-dosimetry, topic/scintillator-plate]
aliases: ["Ohta 2025"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Ohta et al. (2025) — Characterization of a practically designed plastic scintillation plate dosimeter

**Venue**: Medical Physics
**DOI**: [10.1002/mp.17904](https://doi.org/10.1002/mp.17904)
**PDF**: ![[125_MP-52-0.pdf#page=1]]

---

## Executive Summary

본 연구는 선형 가속기의 X선 빔을 이용한 환자 맞춤형 품질 보증(QA)을 위해 설계된 0.2 cm 두께의 플라스틱 신틸레이터 플레이트 선량계의 특성을 평가하였다 [[125_MP-52-0.pdf#page=1|p.1, Abstract]]. CMOS 카메라를 사용하여 신틸레이션 광을 검출하며, 1~1000 MU 범위에서 최대 0.4%의 선형성 오차와 ±0.062%의 높은 재현성을 보였다 [[125_MP-52-0.pdf#page=1|p.1, Results]]. 체렌코프 광을 제거한 후 각도 의존성은 ±1.3% 이내였으며, 에너지 의존성은 -2.1%에서 +1.4% 사이로 나타났다 [[125_MP-52-0.pdf#page=1|p.1, Results]]. 이 시스템은 VMAT QA를 위한 고해상도 및 반복 사용 가능성을 입증하였다 [[125_MP-52-0.pdf#page=1|p.1, Conclusions]].

---

## Problem & Motivation

고정밀 방사선 치료가 증가함에 따라 고해상도, 넓은 측정 영역, 그리고 반복적인 선량 분포 측정의 필요성이 커지고 있으나, 기존 PSD 시스템은 다차원 실시간 측정에서 한계가 있다 [[125_MP-52-0.pdf#page=1|p.1, Abstract]]. 특히 VMAT QA를 위한 상용화된 고해상도 2D/3D 선량계가 부족한 상황에서, 실용적인 설계를 갖춘 신틸레이션 플레이트 기반 선량계의 개발이 요구된다 [[125_MP-52-0.pdf#page=2|p.2, §1]].

---

## Methods

- **장치 구성**: 0.2 cm 두께의 플라스틱 신틸레이터 플레이트(PS: polystyrene doped with 1% DPO and 0.08% red wavelength shifter)를 2.0 cm 두께의 PMMA 플레이트 사이에 샌드위치 구조로 배치 [[125_MP-52-0.pdf#page=2|p.2, §2.1]].
- **검출기**: Sony IMX585 CMOS 센서를 탑재한 카메라(Uranus-C)를 사용하여 신틸레이션 광을 획득하며, 픽셀 해상도는 0.0369 cm/pixel이다 [[125_MP-52-0.pdf#page=2|p.2, §2.1]].
- **체렌코프 분리**: RGB 채널 분석을 통해 체렌코프 광(주로 Blue/Green)과 신틸레이션 광(Red)을 수식적으로 분리하여 보정한다 [[125_MP-52-0.pdf#page=3|p.3, §2.2]].
- **실험 조건**: Elekta VersaHD 가속기를 사용하여 4, 6, 10 MV (FFF 포함) 에너지 빔에 대해 선형성, 재현성, 선량률 의존성, 온도 의존성, 각도 의존성 등을 평가하였다 [[125_MP-52-0.pdf#page=4|p.4, §2.3]].

---

## Results

- **선량 선형성**: 1~1000 MU 범위에서 최대 0.4%의 오차를 보이며 매우 높은 선형성($R^2=0.9999994$)을 기록하였다 [[125_MP-52-0.pdf#page=7|p.7, Fig 4]].
- **재현성**: 100 MU를 10회 조사했을 때 표준 편차는 ±0.062%로, 이온 전리함(PTW 31010, ±0.016%)에 필적하는 성능을 보였다 [[125_MP-52-0.pdf#page=7|p.7, §3.3]].
- **선량률 의존성**: 45~1900 MU/min 범위에서 선량률 변화에 따른 출력 변화는 최대 5.0% 이내였다 [[125_MP-52-0.pdf#page=8|p.8, §3.4]].
- **각도 의존성**: 체렌코프 광 보정 후 -180° ~ 180° 범위에서 각도 의존성은 ±1.3% 이내로 감소하였다 [[125_MP-52-0.pdf#page=9|p.9, §3.6]].
- **VMAT QA**: 임상 폐 SBRT VMAT 플랜에 대해 3%/2mm 감마 분석 통과율 99.91%를 달성하였다 [[125_MP-52-0.pdf#page=9|p.9, §3.8]].

---

## Critical Review

### 방법론·실험설계 타당성

본 연구는 상용 CMOS 카메라를 활용하여 고해상도 2D 선량 분포를 성공적으로 획득하였으며, 특히 체렌코프 광을 RGB 분석으로 분리한 방법론은 물리적 차폐 없이도 정밀한 측정을 가능케 한다 [[125_MP-52-0.pdf#page=3|p.3, §2.2]]. 그러나 카메라 온도가 평형에 도달하는 데 약 1시간이 소요된다는 점은 임상 적용 시 워밍업 시간이 필요함을 시사한다 [[125_MP-52-0.pdf#page=8|p.8, §3.5]].

### 선행연구 대비 기여도·한계

기존의 점 측정 방식 PSD나 저해상도 다이오드 어레이와 달리 0.369 mm의 높은 공간 해상도를 제공하며, MapCHECK(0.5%)이나 ArcCHECK(0.4%) 등 상용 기기와 대등한 선량 특성을 보였다 [[125_MP-52-0.pdf#page=10|p.10, Table 2]]. 한계점으로는 0.1 cm 정도의 미세한 에어 갭이 선량 노멀라이제이션에 영향을 줄 수 있으며, 현재는 2D 평면 측정에 국한되어 있다는 점이 언급되었다 [[125_MP-52-0.pdf#page=12|p.12, §4]].

---

## Implications for Our Research

신틸레이션 플레이트와 CMOS 카메라를 조합한 시스템은 저비용으로 고해상도 QA 시스템을 구축할 수 있는 효과적인 경로임을 보여준다. 특히 적색 파장 변환(red wavelength shifter)을 사용해 체렌코프 광의 간섭을 최소화한 설계는 우리 연구에서도 신호 대 잡음비(SNR) 개선을 위해 고려할 만한 요소이다.

---

## References

- [1] Beddar AS, Mackie TR, Attix FH. Water-equivalent plastic scintillation detectors for high-energy beam dosimetry: I. Physical characteristics and theoretical consideration. Phys Med Biol. 1992;37(10):1883-1900.
- [6] Frelin A-M, Fontbonne J-M, Ban G, et al. The DosiMap: a new 2D scintillating dosimeter for IMRT quality assurance: characterization of two Cerenkov discrimination methods. Med Phys. 2008;35:1661-1662.
- [8] Li JG, Yan G, Liu C. Comparison of two commercial detector arrays for IMRT quality assurance. J Appl Clin Med Phys. 2009;10(2):62-74.
- [14] Sadagopan RA, et al. Characterization and clinical evaluation of a novel IMRT quality assurance system. J Appl Clin Med Phys. 2009;10(2):104-119.
