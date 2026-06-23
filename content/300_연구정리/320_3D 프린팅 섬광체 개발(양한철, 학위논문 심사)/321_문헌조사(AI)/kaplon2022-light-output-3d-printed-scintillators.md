---
title: "Investigation of the light output of 3D-printed plastic scintillators for dosimetry applications"
authors: ["Kapłon, Ł.", "Kulig, D.", "Beddar, S.", "Fiutowski, T.", "Górska, W.", "Hajduga, J.", "Jurgielewicz, P.", "Kabat, D.", "Kalecińska, K.", "Minder, B.", "Moroń, J.", "Moskal, G.", "Niedźwiecki, S.", "Silarski, M.", "Sobczuk, F.", "Szumlak, T.", "Ruciński, A."]
year: 2022
venue: "Radiation Measurements"
doi: "10.1016/j.radmeas.2022.106864"
arxiv: ""
paper_id: "kaplon2022-light-output-3d-printed-scintillators"
source_pdf: "[[109_1-s2.0-S135044872200155X-main.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing, topic/scintillators, topic/dosimetry]
aliases: ["Kapłon 2022"]
status: reviewed
analyzed_at: 2026-04-16
verification_pass_rate: 1.00
---

# Kapłon et al. (2022) — Investigation of the light output of 3D-printed plastic scintillators for dosimetry applications

**Venue**: Radiation Measurements 158 (2022) 106864
**DOI**: [10.1016/j.radmeas.2022.106864](https://doi.org/10.1016/j.radmeas.2022.106864)
**PDF**: ![[109_1-s2.0-S135044872200155X-main.pdf#page=1]]

---

## Executive Summary

본 연구는 선량측정(dosimetry) 응용을 위한 디지털 광처리(DLP) 방식의 3D 프린팅 플라스틱 섬광체의 빛 출력 특성을 조사하였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=1|p.1, Abstract]]. 상용 섬광체 RP-408과 비교했을 때, 3D 프린팅된 바이올렛 및 블루 섬광체는 각각 49%, 43% 수준의 상대적 빛 출력을 보였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=1|p.1, Abstract]]. 반사체 래핑(PTFE 테이프 또는 ESR 호일)은 노출된 상태에 비해 빛 수집 효율을 약 2.6배 향상시켰다 [[109_1-s2.0-S135044872200155X-main.pdf#page=9|p.9, §4]]. 낮은 투명도에도 불구하고 3D 프린팅 섬광체는 높은 선량률 환경에서 충분한 신호대잡음비(SNR)를 제공하여 실시간 dosimetry에 활용될 가능성을 입증했다 [[109_1-s2.0-S135044872200155X-main.pdf#page=9|p.9, §5]].

---

## Problem & Motivation

플라스틱 섬광체는 선량측정에서 수질 등가성(water equivalence)과 높은 시간 분해능으로 인해 널리 사용되지만, 복잡한 기하학적 형상을 제작하기 위해서는 기계 가공이 필수적이다 [[109_1-s2.0-S135044872200155X-main.pdf#page=1|p.1, §1]]. 3D 프린팅 기술은 복잡한 형태의 맞춤형 검출기 제작을 가능하게 하나, 기존 연구들은 상용 섬광체 대비 현저히 낮은 빛 출력과 불투명성 문제를 겪고 있다 [[109_1-s2.0-S135044872200155X-main.pdf#page=2|p.2, §1]]. 따라서 3D 프린팅된 섬광체의 광학적 성능을 정량화하고 표면 처리 및 반사체 구성에 따른 최적화가 필요하다 [[109_1-s2.0-S135044872200155X-main.pdf#page=2|p.2, §1]].

---

## Methods

1.  **제작**: DLP 프린터를 사용하여 두 종류의 수지(3DPS violet, 3DPS blue)로 $10 \times 10 \times 10 \text{ mm}^3$ 큐브 샘플을 제작하였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=3|p.3, §2.2]].
2.  **표면 처리**: (i) 프린팅 직후 상태, (ii) P800 사포 연마, (iii) 광택제 폴리싱의 세 단계를 비교하였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=4|p.4, §2.3]].
3.  **반사체 구성**: 노출(bare), PTFE 테이프(3레이어), ESR 호일 래핑 조건을 적용하였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=4|p.4, §2.3]].
4.  **측정**: Cs-137 감마선 소스 하에서 PMT를 통해 컴프턴 엣지(Compton edge) 위치를 측정하여 빛 출력을 산출하였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=5|p.5, §2.4]].

---

## Results

- **상대적 빛 출력**: 폴리싱 및 PTFE 래핑 상태에서 RP-408(10,000 photons/MeV) 대비 3DPS violet은 5,302 photons/MeV(53%), 3DPS blue는 5,604 photons/MeV(56%)를 기록했다 [[109_1-s2.0-S135044872200155X-main.pdf#page=6|p.6, Table 3]].
- **반사체 효과**: 반사체 래핑은 연마되지 않은 샘플에서 광수집을 약 2.6배, 폴리싱된 샘플에서 약 2.1배 증가시켰다 [[109_1-s2.0-S135044872200155X-main.pdf#page=9|p.9, §4]].
- **투명도**: RP-408의 89.1%에 비해 3DPS violet(73.4%), 3DPS blue(66.3%)는 낮은 투명도를 보였으며, 이는 프린팅 레이어 구조와 기공에 기인한다 [[109_1-s2.0-S135044872200155X-main.pdf#page=8|p.8, Table 4]].
- **경시 변화**: 3D 프린팅 샘플은 제작 1년 후 약 20~35%의 빛 출력 저하가 관찰되었으며, 이는 잔류 단량체(monomers)나 불완전한 중합 과정에 의한 퇴화로 추정된다 [[109_1-s2.0-S135044872200155X-main.pdf#page=8|p.8, §4]].

---

## Critical Review

### 방법론·실험설계 타당성

본 연구는 Cs-137 소스와 가우시안 피팅을 통한 컴프턴 엣지 결정법을 사용하여 빛 출력을 객관적으로 비교하였다 [[109_1-s2.0-S135044872200155X-main.pdf#page=5|p.5, §2.5]]. 표면 거칠기와 반사체 종류를 체계적으로 조합하여 최적의 구성을 도출한 점이 강점이다 [[109_1-s2.0-S135044872200155X-main.pdf#page=5|p.5, Fig 3]]. 다만, 큐브 형태에 한정된 실험이므로 실제 복잡한 형상의 dosimetry 가이드나 광가이드로서의 성능(감쇄 길이 등)에 대한 데이터는 부족하다.

### 선행연구 대비 기여도·한계

Kim et al. (2020)의 초기 연구 대비 높은 빛 출력을 달성했으며, 표면 처리의 중요성을 정량적으로 입증했다 [[109_1-s2.0-S135044872200155X-main.pdf#page=9|p.9, §4]]. 그러나 1년 내 20% 이상의 성능 저하는 장기적인 임상 활용에 큰 제약이 되며, 저자들도 이를 해결하기 위한 추가 연구(안정적인 수지 개발)가 필요함을 명시했다 [[109_1-s2.0-S135044872200155X-main.pdf#page=8|p.8, §4]].

---

## Implications for Our Research

우리 프로젝트의 입장에서 이 논문은 **3D 프린팅 섬광체의 실용적 한계와 가능성**을 명확히 제시한다. 특히 반사체 래핑만으로도 낮은 투명도를 상당 부분 극복할 수 있다는 점은 복잡한 형상의 검출기 설계 시 반사 레이어 코팅이 필수적임을 시사한다. 또한, 제작 후 성능 저하 문제를 해결하기 위한 '에이징(aging)' 안정화 공정이나 밀봉(encapsulation) 전략이 우리 시스템 설계에 포함되어야 함을 시사한다.

---

## References

- [1] Beaulieu, L., Beddar, S. (2016). Review of plastic and liquid scintillation dosimetry for photon, electron, and proton therapy. Phys. Med. Biol. 61, R305–R343.
- [2] Kim, D.-G., et al. (2020). Characteristics of 3D-printed plastic scintillators for gamma-ray detection. Nucl. Eng. Technol. 52, 2910–2917.
- [3] Janecek, M. (2012). Reflectivity spectra for commonly used reflectors. IEEE Trans. Nucl. Sci. 59, 490–497.
- [4] Son, J., et al. (2018). Characteristics of 3D printed plastic scintillator fabricated by UV LED curing machine. Nucl. Instrum. Methods Phys. Res. Sect. A 929, 23–28.
