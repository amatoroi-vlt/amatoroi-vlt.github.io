---
title: "Characteristics of 3D Printed Plastic Scintillator"
authors: ["Kim, D.", "Lee, S.", "Park, J.", "Son, J.", "Kim, Y. H.", "Kim, Y. K."]
year: 2020
venue: "EPJ Web of Conferences"
doi: "10.1051/epjconf/202022501005"
arxiv: ""
paper_id: "kim2020-characteristics-3d-printed-plastic"
source_pdf: "[[107_epjconf_animma2019_01005.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing, topic/plastic-scintillator]
aliases: ["Kim 2020"]
status: reviewed
analyzed_at: 2025-05-14
verification_pass_rate: 1.00
---

# Kim et al. (2020) — Characteristics of 3D Printed Plastic Scintillator

**Venue**: EPJ Web of Conferences 225, 01005 (2020)
**DOI**: [10.1051/epjconf/202022501005](https://doi.org/10.1051/epjconf/202022501005)
**PDF**: ![[107_epjconf_animma2019_01005.pdf#page=1]]

---

## Executive Summary

DLP(Digital Light Processing) 3D 프린팅 기술을 사용하여 UV 경화 수지로 30 mm × 30 mm × 10 mm 크기의 플라스틱 섬광체를 제작하였다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §Abstract]]. 3D 프린팅된 섬광체는 상용 BC408의 18.3 ns보다 빠른 15.6 ns의 평균 감쇠 시간을 나타냈다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §Abstract]]. 에너지 분해능은 137Cs의 477 keV 컴프턴 에지(Compton edge)에서 15.4%로 측정되었다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §Abstract]]. 이러한 결과는 방사선 검출을 위한 3D 프린팅 플라스틱 섬광체 활용의 타당성을 입증한다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §Abstract]].

---

## Problem & Motivation

기존의 플라스틱 섬광체는 일반적으로 열중합법(thermal polymerization)을 통해 제작되는데, 이 공정은 일주일 이상 소요될 정도로 느리고 단순한 기하학적 형상으로 제한된다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §I]]. DLP와 같은 3D 프린팅 기술은 복잡하고 기하학적으로 최적화된 설계를 가능하게 하는 빠른 대안을 제공한다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §I]]. 본 연구는 실질적인 유용성을 평가하기 위해 DLP 프린팅된 샘플의 섬광 성능(감쇠 시간, 에너지 분해능, 효율)을 분석하는 것을 목표로 한다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §II]].

---

## Methods

섬광체는 ASIGA Pico2 HD DLP 프린터와 UV 경화 수지를 사용하여 프린팅되었다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §II]]. 감쇠 시간 프로파일은 수정된 TCSPC(Time Correlated Single Photon Counting) 셋업을 사용하여 측정되었으며, 재컨볼루션(reconvolution) 함수로 피팅되었다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §II]]. 에너지 분해능은 137Cs 선원으로부터 477 keV 컴프턴 최대 전자를 분리하기 위해 γ-γ 일치 실험 장치를 구성하여 결정되었다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §II]]. 성능은 표준 상용 섬광체인 BC408(Saint-Gobain)과 비교 분석되었다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §II]].

---

## Results

3D 프린팅된 샘플은 470 nm의 피크 파장을 보였으며, 이는 BC408의 425 nm보다 길다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, Table I]]. 광출력(Light output)은 7,000 ph/MeV로 BC408의 10,470 ph/MeV에 비해 상당히 낮았다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, Table I]]. 투과율 또한 56%로 BC408의 76%보다 낮게 측정되었다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, Table I]]. 그러나 평균 감쇠 시간은 15.6 ns로 BC408의 18.3 ns보다 우수한(빠른) 성능을 보였다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, Table I]]. 3D 프린팅 샘플의 에너지 분해능은 15.4%였으며, BC408은 9.7%를 달성하였다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, Table I]].

---

## Critical Review

### 방법론·실험설계 타당성

γ-γ 일치법은 명확한 광전피크(photopeak)가 없는 플라스틱 섬광체에서 컴프턴 에지를 추출하기 위한 견고한 방법이다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §II]]. 그러나 본 연구는 단일 기하 구조(30x30x10 mm)에만 집중하고 있으며, DLP 프린터의 해상도 한계나 다양한 프린팅 파라미터가 광학적 투명도에 미치는 영향은 탐구하지 않았다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, §III]]. 낮은 투과율(56%)은 주조(cast) 섬광체에 비해 3D 프린팅된 내부 체적 내에서 상당한 빛 산란이나 흡수가 발생함을 시사한다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, Table I]].

### 선행연구 대비 기여도·한계

이 연구는 UV 경화 수지에 관한 이전 연구들[3]을 바탕으로 구축되었으나, 더 상세한 타이밍 및 에너지 분해능 데이터를 제공한다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §I]]. 광출력이 BC408의 약 67% 수준이지만, 초기 프로토타입에 비하면 상당한 개선이다 [[107_epjconf_animma2019_01005.pdf#page=1|p.1, §Abstract]]. 주요 한계점으로는 여전히 상용 표준에 비해 상대적으로 낮은 투명도와 광출력이 꼽히며, 이는 고정밀 열량계(calorimetry)나 저배경 방사능 실험에서의 사용을 제한할 수 있다 [[107_epjconf_animma2019_01005.pdf#page=2|p.2, §IV]].

---

## Implications for Our Research

더 빠른 감쇠 시간(15.6 ns)은 에너지 분해능보다 타이밍 정밀도가 더 중요한 고선량율(high-rate) 환경에서 3D 프린팅 섬광체가 유리할 수 있음을 시사한다. 기하학적 유연성과 광학적 성능 사이의 절충안(trade-off)은 우리 자신의 설계에서 신중하게 관리되어야 한다.

---

## References

- [1] C. H. Lee, J. Son, T. H. Kim, and Y. K. Kim, “Characteristics of Plastic Scintillators Fabricated by a Polymerization Reaction,” Nucl. Eng. Technol., vol. 49, no. 3, pp. 592–597, 2017.
- [2] Y. Mishnayot, M. Layani, I. Cooperstein, S. Magdassi, and G. Ron, “3D Printing of Scintillating Materials,” no. June, pp. 1–4, 2014.
- [3] J. Son, D. G. Kim, S. Lee, J. Park, Y. Kim, T. Schaarschmidt, and Y. K. Kim, “Improved 3D Printing Plastic Scintillator Fabrication,” J. Korean Phys. Soc., vol. 73, no. 7, pp. 887–892, 2018.
- [4] S. Lee, J. Son, D. G. Kim, J. Choi, and Y. K. Kim, “Characterization of plastic scintillator fabricated by UV LED curing machine,” Nucl. Instruments Methods Phys. Res. Sect. A Accel. Spectrometers, Detect. Assoc. Equip., vol. 929, no. July 2018, pp. 23–28, 2019.
