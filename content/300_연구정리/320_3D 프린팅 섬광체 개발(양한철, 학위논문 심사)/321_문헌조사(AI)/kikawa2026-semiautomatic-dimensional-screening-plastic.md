---
title: "Semiautomatic dimensional screening of plastic scintillator cubes using image analysis and robotics"
authors: ["Kikawa, T.", "Tani, M.", "Ichikawa, A. K.", "Matsubara, T.", "Nakaya, T.", "Ogawa, T."]
year: 2026
venue: "Journal of Instrumentation (JINST)"
doi: "10.1088/1748-0221/21/01/P01001"
arxiv: "2603.26732"
paper_id: "kikawa2026-semiautomatic-dimensional-screening-plastic"
source_pdf: "[[111_2603.26732v1.pdf]]"
tags: [paper, paper/reviewed, topic/scintillators, topic/robotics, topic/quality-control]
aliases: ["Kikawa 2026"]
status: reviewed
analyzed_at: 2025-05-14
verification_pass_rate: 1.00
---

# Kikawa et al. (2026) — Semiautomatic dimensional screening of plastic scintillator cubes using image analysis and robotics

**Venue**: Journal of Instrumentation (JINST)
**DOI**: [10.1088/1748-0221/21/01/P01001](https://doi.org/10.1088/1748-0221/21/01/P01001) · **arXiv**: [2603.26732](https://arxiv.org/abs/2603.26732)
**PDF**: ![[111_2603.26732v1.pdf#page=1]]

---

## Executive Summary

대규모 입자 물리학 검출기는 종종 수백만 개의 반복되는 구성 요소를 포함하므로 정밀하고 효율적인 품질 관리가 필수적이다. 본 연구에서는 미래의 중성미자 검출기에 사용될 $1 \text{ cm}^3$ 플라스틱 섬광체 큐브의 치수 검사를 위한 반자동 시스템을 개발하였다 [[111_2603.26732v1.pdf#page=1|p.1]]. 이 시스템은 전동 회전 스테이지, 6개의 고해상도 카메라 및 이미지 분석 소프트웨어를 활용하여 큐브 크기, 표면 돌출부 및 광학 판독에 사용되는 파장 변환 섬유용 구멍의 위치를 측정한다 [[111_2603.26732v1.pdf#page=1|p.1]]. 프로토타입 시스템은 $10 \mu\text{m}$의 측정 정밀도를 달성했으며 수동 검사와 80% 이상의 일치성을 보였다 [[111_2603.26732v1.pdf#page=1|p.1]].

---

## Problem & Motivation

ATLAS, CMS 또는 Hyper-Kamiokande와 같은 현대 입자 물리학 실험에서 대규모 검출기는 정밀하게 제조된 수백만 개의 구성 요소로 구성되며, 이들의 기계적 정밀도는 검출기 성능에 결정적인 영향을 미칠 수 있다 [[111_2603.26732v1.pdf#page=1|p.1]]. 본 연구의 업그레이드 핵심 구성 요소인 SuperFGD는 러시아 UNIPLAST에서 제조한 1,956,864개의 플라스틱 섬광체 큐브(각 $1 \text{ cm}^3$)가 3차원 격자로 배열된 완전 활성 트래킹 검출기이다 [[111_2603.26732v1.pdf#page=2|p.2]]. 수백만 개의 부품을 수동으로 검사하는 것은 불가능에 가까우며, 따라서 정확성과 효율성을 동시에 갖춘 자동화된 품질 관리 시스템이 필요하다 [[111_2603.26732v1.pdf#page=2|p.2]].

---

## Methods

개발된 반자동 시스템은 섬광체 큐브의 6개 면 전체 이미지를 캡처하고 이미지 분석을 기반으로 각 큐브를 합격 또는 불합격으로 분류한다 [[111_2603.26732v1.pdf#page=3|p.3]].
- **광학 시스템**: 6개의 8메가픽셀 USB 카메라(ELP, ELPUSB8MP02G-SFV(5-50))가 큐브 이미징에 사용된다 [[111_2603.26732v1.pdf#page=4|p.4]]. 화학적 에칭(etching)으로 인한 표면 불규칙성 문제를 해결하기 위해 각 카메라에 링형 LED 조명을 장착하여 세 방향에서 균일한 조명을 제공하였다 [[111_2603.26732v1.pdf#page=4|p.4]].
- **이미지 분석**: 전처리, 허프 변환(Hough transform)을 이용한 형상 감지, 구멍 에지의 원형 피팅(circular fitting)을 포함하는 이미지 분석 절차를 수행한다 [[111_2603.26732v1.pdf#page=7|p.7,8]].
- **평가 파라미터**: 조명 및 정렬 효과를 보정한 후, 각 큐브 면은 구멍 위치($x_{hole}, y_{hole}$), 큐브 크기($L_x, L_y$), 그리고 돌출 지수($P_{bump}$)의 5가지 파라미터를 기반으로 평가된다 [[111_2603.26732v1.pdf#page=10|p.10]].
- **로봇 통합**: 구멍 위치에 따라 큐브를 48개 그룹으로 분류하면서 방향을 유지하기 위해 6축 로봇 팔(UFACTORY xArm 6)이 도입되었다 [[111_2603.26732v1.pdf#page=1,13|p.1,13]].

---

## Results

- **정밀도**: 시스템은 $10 \mu\text{m}$의 치수 측정 정밀도를 달성하였다 [[111_2603.26732v1.pdf#page=1|p.1]].
- **일치성**: 수동 검사 결과와 비교했을 때 80% 이상의 일치성을 확인하였다 [[111_2603.26732v1.pdf#page=1|p.1]].
- **불합격률**: 완성된 시스템을 통한 실제 검사 결과, 전체 큐브의 3.1%가 불합격 판정을 받았다 [[111_2603.26732v1.pdf#page=1|p.1]].
- **자동화 가능성**: 로봇 팔을 사용하여 플랫폼에 큐브를 배치하는 초기 공정을 자동화함으로써 완전 자동 검사 및 선별 프로세스의 토대를 마련하였다 [[111_2603.26732v1.pdf#page=15|p.15]].

---

## Critical Review

### 방법론·실험설계 타당성

6개의 카메라와 회전 스테이지를 조합하여 큐브의 전면을 사각지대 없이 검사하는 설계는 매우 타당하며 효율적이다 [[111_2603.26732v1.pdf#page=3|p.3]]. 특히 화학적 에칭으로 인한 반사 문제를 해결하기 위해 특수 조명을 설계한 점은 실질적인 제조 공정을 잘 고려한 결과이다 [[111_2603.26732v1.pdf#page=4|p.4]]. 다만, 이미지 분석 알고리즘이 표면의 미세한 스크래치와 실제 구조적 결함을 구별하는 임계값(threshold) 설정에 대한 상세한 논의가 부족하며, 이는 20%의 수동 검사와의 불일치 원인이 될 수 있다 [[111_2603.26732v1.pdf#page=10|p.10]].

### 선행연구 대비 기여도·한계

이 연구는 단순한 치수 측정을 넘어 로봇 팔을 이용한 정렬 및 분류까지 통합했다는 점에서 기존의 단순 영상 검사 시스템보다 진일보했다 [[111_2603.26732v1.pdf#page=13|p.13]]. 하지만 현재 시스템은 여전히 샘플을 로봇 팔이 집어올리기 전의 초기 배치는 수동 작업에 의존하는 '반자동' 상태이며, 진정한 의미의 완전 자동화를 위해서는 대량의 큐브를 자동으로 공급하는 장치가 추가되어야 한다 [[111_2603.26732v1.pdf#page=15|p.15]].

---

## Implications for Our Research

수백만 개의 섬광체 요소를 사용하는 대규모 프로젝트에서 품질 관리의 자동화는 선택이 아닌 필수이다. 본 연구에서 보여준 $10 \mu\text{m}$ 수준의 정밀도 제어와 로봇 팔을 이용한 분류 자동화는 우리 연구실의 검출기 제작 공정 효율화에도 직접적으로 적용 가능한 모델이다.

---

## References

- [1] ATLAS collaboration, The ATLAS Experiment at the CERN Large Hadron Collider, 2008 JINST 3 S08003.
- [2] CMS collaboration, The CMS experiment at the CERN LHC, 2008 JINST 3 S08004.
- [3] T2K collaboration, The T2K Experiment, Nucl. Instrum. Meth. A 659 (2011) 106 [arXiv:1106.1238].
- [4] A. Blondel et al., A fully active fine grained detector with three readout views, 2018 JINST 13 P02006 [arXiv:1707.01785].
- [5] S. Berns et al., Additive manufacturing of fine-granularity optically-isolated plastic scintillator elements, 2022 JINST 17 P10045 [arXiv:2202.10961].
