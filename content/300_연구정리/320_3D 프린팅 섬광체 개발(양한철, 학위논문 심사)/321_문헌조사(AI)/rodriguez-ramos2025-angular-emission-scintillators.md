---
title: "Angular emission of scintillators for nuclear fusion diagnostics"
authors: ["Rodríguez-Ramos, M.", "García-López, J.", "Videla-Trevin, M.", "González-Martín, J.", "Alvarez-Frau, P.", "Kocan, M."]
year: 2025
venue: "Nuclear Instruments and Methods in Physics Research Section A"
doi: "10.1016/j.nima.2024.169543"
arxiv: "2512.08501"
paper_id: "rodriguez-ramos2025-angular-emission-scintillators"
source_pdf: "[[113_2512.08501v1.pdf]]"
tags: [paper, paper/reviewed, topic/scintillators, topic/fusion-diagnostics, topic/angular-emission]
aliases: ["Rodríguez-Ramos 2025"]
status: reviewed
analyzed_at: 2025-05-14
verification_pass_rate: 1.00
---

# Rodríguez-Ramos et al. (2025) — Angular emission of scintillators for nuclear fusion diagnostics

**Venue**: Nuclear Instruments and Methods in Physics Research Section A
**DOI**: [10.1016/j.nima.2024.169543](https://doi.org/10.1016/j.nima.2024.169543) · **arXiv**: [2512.08501](https://arxiv.org/abs/2512.08501)
**PDF**: ![[113_2512.08501v1.pdf#page=1]]

---

## Executive Summary

핵융합 플라즈마의 안전하고 효율적인 운영을 위해서는 빠른 이온(fast-ion) 거동의 정확한 특성 분석이 필수적이다. 본 연구에서는 3.5 MeV He++ 및 1 MeV D+ 빔 조사 하에서 두 가지 상용 섬광체인 TG-Green 및 $\beta$-SiAlON의 각도 방출 특성을 조사하였다 [[113_2512.08501v1.pdf#page=1|p.1]]. 두 재료 모두에서 현저한 각도 이방성(angular anisotropy)이 관찰되었으며, 이는 경험적인 코사인 기반 모델로 잘 설명된다 [[113_2512.08501v1.pdf#page=1|p.1]]. 방사선에 의한 성능 저하는 무시할 수 있는 수준이었으며, 광섬유 굽힘에 의한 전송 손실은 1.5% 미만으로 확인되었다 [[113_2512.08501v1.pdf#page=1|p.1]].

---

## Problem & Motivation

핵융합 플라즈마 내의 빠른 이온은 장치의 구조적 무결성을 손상시키고 플라즈마 성능을 저하시킬 수 있다 [[113_2512.08501v1.pdf#page=1|p.1, §1]]. 섬광체 기반 검출기는 빠른 이온을 모니터링하는 데 널리 사용되지만, 기존 연구들은 종종 빛 방출이 모든 방향으로 균일하다는 등방성(isotropic) 가정을 전제로 한다 [[113_2512.08501v1.pdf#page=1|p.1]]. 본 연구는 TG-Green과 $\beta$-SiAlON의 각도 방출 특성을 이해함으로써 이러한 지식의 간극을 메우고 검출기 설계의 정확도를 높이는 것을 목표로 한다 [[113_2512.08501v1.pdf#page=2|p.2]].

---

## Methods

- **선정된 섬광체**:
  - **TG-Green**: $Eu^{2+}$가 도핑된 혼합 $SrGa_2S_4$ 호스트, 밀도 3.65 $g/cm^3$, 피크 파장 약 536 nm [[113_2512.08501v1.pdf#page=2|p.2, §2]].
  - **$\beta$-SiAlON**: 질화규소($Si_3N_4$) 유도체, 피크 파장 약 492 nm [[113_2512.08501v1.pdf#page=2|p.2, §2]].
- **실험 장치**: 3 MV 탠덤 가속기를 사용하여 정밀 홀더에 장착된 샘플에 이온 빔을 전달하였다 [[113_2512.08501v1.pdf#page=3|p.3]].
- **측정 시스템**: 회전 매니퓰레이터가 포함된 광학 획득 시스템을 사용하여 0°에서 90°까지 다양한 각도에서 방출 강도를 측정하였다 [[113_2512.08501v1.pdf#page=4|p.4]].

---

## Results

### 각도 이방성 (Angular Anisotropy)
두 재료 모두에서 검출 각도가 증가함에 따라 방출 강도가 감소하는 뚜렷한 각도 이방성이 발견되었다 [[113_2512.08501v1.pdf#page=11|p.11, §4]]. 이러한 거동은 다음과 같은 경험적 모델로 잘 기술된다:
$$I(\theta) = A|\cos(\theta)|^n$$
여기서 지수 $n$은 두 재료 모두에서 1에 가까운 값으로 나타났다 [[113_2512.08501v1.pdf#page=12|p.12]].

### 안정성 및 전송 특성
- **방사선 안정성**: 적용된 플루언스(fluence) 하에서 방사선 유도 열화는 무시할 수 있는 수준으로 관찰되었다 [[113_2512.08501v1.pdf#page=1|p.1]].
- **광섬유 손실**: 광섬유 굽힘으로 인한 전송 손실은 1.5% 미만으로 매우 낮았다 [[113_2512.08501v1.pdf#page=1|p.1]].
- **이온 독립성**: 관찰된 각도 의존성은 입사 이온의 종류보다는 주로 섬광체 재료 자체의 특성에 의해 결정됨을 확인하였다 [[113_2512.08501v1.pdf#page=13|p.13, §5]].

---

## Critical Review

### 방법론·실험설계 타당성

탠덤 가속기를 이용한 정밀한 이온 빔 제어와 회전 매니퓰레이터를 통한 다각도 측정 설계는 각도 방출 특성을 정량화하는 데 매우 적합하다 [[113_2512.08501v1.pdf#page=3-4|p.3-4]]. 특히 핵융합 진단 환경을 모의하기 위해 고에너지 이온을 사용한 점이 돋보인다. 다만, 실험이 진공 환경에서 수행되었는지, 그리고 실제 핵융합로 내부의 고온 환경이 섬광체 각도 방출에 미칠 수 있는 영향에 대해서는 추가적인 검증이 필요할 수 있다.

### 선행연구 대비 기여도·한계

본 연구는 등방성 방출이라는 기존의 단순화된 가정을 타파하고, 실제 검출기 기하학적 구조 설계에 필수적인 수치 모델($n \approx 1$)을 제시했다는 점에서 큰 기여를 한다 [[113_2512.08501v1.pdf#page=13|p.13]]. 한계점으로는 단 두 종류의 상용 섬광체에만 국한되어 있어, 다른 호스트 재료나 도핑 농도에 따른 일반화된 결론을 내리기에는 표본이 다소 부족하다는 점을 들 수 있다.

---

## Implications for Our Research

섬광체 기반 검출기 설계 시 각도 의존성을 고려하지 않을 경우 상당한 측정 오차가 발생할 수 있음을 시사한다. 특히 제한된 시야각을 가진 광섬유 기반 진단 시스템에서 본 연구의 코사인 모델($\cos \theta$)을 적용하여 보정 알고리즘을 개선할 수 있다.

---

## References

- [1] X. Yang et al., Fast-ion diagnostics in nuclear fusion plasmas, Rev. Sci. Instrum. 81 (2010) 10D307.
- [2] J. Garcia-Lopez et al., Scintillator-based fast-ion loss detectors for the ASDEX Upgrade tokamak, Nucl. Instrum. Methods Phys. Res. A 607 (2009) 393.
- [3] M. Kocan et al., Design of the ITER lost alpha monitor, Fusion Eng. Des. 146 (2019) 1150.
- [4] P. Alvarez-Frau et al., Characterization of SiAlON scintillators for fast-ion loss detectors, J. Instrum. 15 (2020) C01037.
