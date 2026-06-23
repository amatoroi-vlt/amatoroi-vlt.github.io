---
title: "A new diffuse reflector filament for additive manufacturing of 3D printing finely-segmented plastic scintillator"
authors: ["Berns, S.", "Boillat, E.", "Hugon, S.", "Boyarintsev, A.", "Grynyov, B.", "Karavaeva, N.", "Krech, A.", "Minenko, S.", "Sibilieva, T.", "Sibilyev, M.", "De Roeck, A.", "Dieminger, T.", "Kose, U.", "Li, B.", "Rubbia, A.", "Sgalaberna, D.", "Weber, T.", "Wüthrich, J.", "Zhao, X."]
year: 2025
venue: "arXiv"
doi: ""
arxiv: "2509.01247v1"
paper_id: "berns2025-new-diffuse-reflector-filament"
source_pdf: "[[002_2509.01247v1.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing-scintillator]
aliases: ["Berns 2025"]
status: reviewed
analyzed_at: 2025-02-18
verification_pass_rate: 1.0
---

# Berns et al. (2025) — A new diffuse reflector filament for additive manufacturing of 3D printing finely-segmented plastic scintillator

**Venue**: arXiv
**DOI**: []() · **arXiv**: [2509.01247v1](https://arxiv.org/abs/2509.01247v1)
**PDF**: ![[002_2509.01247v1.pdf#page=1]]

---

## Executive Summary

본 연구는 3D 프린팅을 이용한 미세 분할 플라스틱 섬티레이터(plastic scintillator) 제작에 적합한 새로운 백색 반사 필라멘트의 개발 및 특성 분석을 수행하였다 [[002_2509.01247v1.pdf#page=1|p.1, Abstract]]. 폴리카보네이트(PC)와 폴리메틸 메타크릴레이트(PMMA)를 기본 폴리머로 사용하고, 반사율을 높이기 위해 이산화티타늄(TiO2)과 폴리테트라플루오로에틸렌(PTFE)을 첨가한 필라멘트를 제작하였다 [[002_2509.01247v1.pdf#page=1|p.1, Abstract]]. 개발된 필라멘트를 Fused Deposition Modeling (FDM) 방식으로 출력하여 반사층을 형성하고, Fused Injection Modeling (FIM) 방식으로 제작된 3D 분할 플라스틱 섬티레이터 프로토타입(SuperLayer)에 적용하여 우주선(cosmic rays)을 이용한 광량 및 광학적 누화(crosstalk) 테스트를 진행하였다 [[002_2509.01247v1.pdf#page=1|p.1, Abstract]]. 실험 결과, PMMA 기반 반사체를 사용한 프로토타입은 기존 상용 백색 반사 필라멘트를 사용한 검출기보다 더 높은 광량을 보였으며, 광학적 누화는 0.7%로 매우 낮게 측정되어 고해상도 열량계 및 입자 추적 응용 분야에 적합함을 입증하였다 [[002_2509.01247v1.pdf#page=7|p.7, §V]].

---

## Problem & Motivation

플라스틱 섬티레이터는 빠른 응답 속도와 제작의 용이성 덕분에 입자 검출기에 널리 사용되지만, 기존의 주조(cast polymerization), 사출 성형(injection molding), 압출(extrusion) 방식은 노동 집약적이며 복잡한 기하학적 구조를 구현하는 데 한계가 있다 [[002_2509.01247v1.pdf#page=1|p.1, §I]]. 최근 적층 제조(additive manufacturing) 기술의 발전으로 Fused Deposition Modeling (FDM)을 통해 섬티레이터와 반사 물질을 동시에 출력하여 미세 분할 검출기를 제작하는 방법이 도입되었다 [[002_2509.01247v1.pdf#page=1|p.1, §I]]. 그러나 대규모 검출기 응용을 위해 요구되는 투명성과 치수 정확도를 달성하는 데 어려움이 있었으며, 이를 극복하기 위해 Fused Injection Modeling (FIM)이라는 하이브리드 3D 프린팅 방식이 제안되었다 [[002_2509.01247v1.pdf#page=1|p.1, §I]]. FIM 방식은 약 230°C의 주입 온도에서 구조적 무결성을 유지해야 하는 반사 필라멘트에 엄격한 열적 요구 사항을 부과하므로, 고성능 3D 프린팅 섬티레이터 검출기를 위한 최적의 재료 조합을 식별하는 것이 필수적이다 [[002_2509.01247v1.pdf#page=2|p.2, §I]].

---

## Methods

- **필라멘트 제작:** 폴리카보네이트(PC)와 폴리메틸 메타크릴레이트(PMMA) 과립을 반사 첨가제 분말(TiO2, PTFE)과 혼합한 후, 데스크탑 압출기(Noztek ProHT)와 산업용 압출기(Battenfeld)를 사용하여 직경 1.75 ± 0.1 mm의 필라멘트를 열 압출 방식으로 제작하였다 [[002_2509.01247v1.pdf#page=2|p.2, §II.A]].
- **광학 특성 평가 샘플 제작:** Creatbot F430 듀얼 압출기 3D 프린터를 사용하여 0.2 mm, 0.4 mm, 1.0 mm 두께의 정사각형 샘플(20 × 20 mm)을 265°C의 프린팅 온도로 출력하였다 [[002_2509.01247v1.pdf#page=2|p.2, §II.A]].
- **광학 측정:** 적분구(integrating sphere)가 장착된 Shimadzu UV-2450 분광광도계를 사용하여 200~800 nm 파장 범위에서 광 반사율(R)과 광 투과율(T)을 측정하였다 [[002_2509.01247v1.pdf#page=2|p.2, §II.A]].
- **프로토타입 제작 및 테스트:** FIM 기술을 사용하여 4 × 4 × 1 플라스틱 섬티레이터 큐브(각 1 × 1 × 1 cm³)로 구성된 'SuperLayer' 프로토타입을 제작하였다. 각 큐브의 6개 면은 새로 개발된 3D 프린팅 필라멘트로 제작된 1 mm 두께의 반사벽으로 둘러싸여 있다 [[002_2509.01247v1.pdf#page=4|p.4, §IV]].
- **성능 평가:** 수직으로 통과하는 우주선(cosmic rays)을 이용하여 SuperLayer의 광량(light yield)과 큐브 간 광학적 누화(crosstalk)를 측정하였으며, 신호는 파장 변환(WLS) 파이버와 Hamamatsu S13360-1325 MPPC를 통해 수집 및 CAEN DT5202로 디지털화되었다 [[002_2509.01247v1.pdf#page=4|p.4, §IV]], [[002_2509.01247v1.pdf#page=6|p.6, §IV]].

---

## Results

- **분말 반사율:** 429 nm 파장에서 순수 PTFE 분말이 가장 높은 반사율을 보였으며, TiO2 분말도 기준 샘플(BaSO4, 100%) 대비 94.64%의 우수한 반사율을 나타냈다 [[002_2509.01247v1.pdf#page=2|p.2, §III.1]].
- **PC 기반 샘플:** PC + 10% TiO2 + 5% PTFE 조합이 0.4 mm 두께, 420 nm 파장에서 86.22%의 가장 높은 반사율과 0.55%의 낮은 광 투과율을 보여 최적의 구성으로 확인되었다 [[002_2509.01247v1.pdf#page=3|p.3, §III.2]], [[002_2509.01247v1.pdf#page=4|p.4, Table I]].
- **PMMA 기반 샘플:** PMMA + 15% TiO2 조합은 0.4 mm 두께, 420 nm 파장에서 92.53%의 매우 높은 반사율을 달성했으나, 광 투과율은 1.69%로 PC 기반 샘플보다 높았다 [[002_2509.01247v1.pdf#page=4|p.4, Table I]].
- **프로토타입 성능 (광량):** PMMA 기반 반사체를 사용한 SuperLayer는 채널당 약 32 p.e./MIP의 가장 높은 광량을 기록하여, PC 기반 반사체(약 25 p.e./MIP/channel) 및 상용 백색 반사 필라멘트를 사용한 기준 검출기 SuperCube(약 29 p.e./MIP/channel)보다 우수한 성능을 보였다 [[002_2509.01247v1.pdf#page=6|p.6, §IV]], [[002_2509.01247v1.pdf#page=7|p.7, §V]].
- **프로토타입 성능 (누화):** PMMA 및 PC 기반 반사체를 사용한 두 프로토타입 모두 평균 0.7%의 매우 낮은 큐브 간 광학적 누화를 보였으며, 이는 상용 백색 반사 필라멘트를 사용한 SuperCube의 평균 누화(4%)보다 현저히 낮은 수치이다 [[002_2509.01247v1.pdf#page=7|p.7, §IV]], [[002_2509.01247v1.pdf#page=7|p.7, §V]].

---

## Critical Review

### 방법론·실험설계 타당성

본 연구는 필라멘트의 재료 배합부터 광학적 특성 평가, 그리고 실제 검출기 프로토타입 제작 및 우주선 테스트까지 체계적인 실험 설계를 갖추고 있다 [[002_2509.01247v1.pdf#page=2|p.2, §II]], [[002_2509.01247v1.pdf#page=4|p.4, §IV]]. 다양한 두께(0.2, 0.4, 1.0 mm)와 재료 조합에 따른 반사율 및 투과율을 정량적으로 비교 분석한 점은 타당하다 [[002_2509.01247v1.pdf#page=4|p.4, Table I]]. 평가자 해석: 다만, 장기적인 방사선 조사에 따른 반사체의 광학적 특성 저하(radiation damage)나 기계적 내구성에 대한 평가는 포함되어 있지 않아, 실제 고에너지 물리 실험 환경에서의 장기 안정성 검증이 추가로 필요해 보인다.

### 선행연구 대비 기여도·한계

기존 상용 3D 프린팅 필라멘트의 한계를 극복하고, FIM 공정에 적합한 고반사율 맞춤형 필라멘트를 성공적으로 개발하여 광학적 누화를 4%에서 0.7%로 대폭 감소시킨 것은 중요한 기술적 진전이다 [[002_2509.01247v1.pdf#page=7|p.7, §V]]. 저자들은 PMMA의 연화 온도(softening temperature)가 85~105°C로 PC(약 140°C)보다 낮다는 점을 명시하며, 고온 공정에서의 적용 가능성에 대한 한계를 언급하였다 [[002_2509.01247v1.pdf#page=4|p.4, §III.4]]. 평가자 해석: PMMA 기반 반사체가 광량 측면에서는 우수하나 투과율이 상대적으로 높고 열적 안정성이 낮다는 트레이드오프(trade-off)가 존재하므로, 응용 분야의 요구 사항(예: 극단적인 광학적 격리 vs. 최대 광량 수집)에 따라 재료 선택이 달라져야 할 것이다.

---

## Implications for Our Research

본 연구에서 제시된 PC 및 PMMA 기반의 맞춤형 반사 필라멘트 배합 비율(예: PC + 10% TiO2 + 5% PTFE)은 향후 우리 연구실에서 3D 프린팅 기반의 고해상도 방사선 검출기나 의료용 영상 기기를 설계할 때 직접적으로 활용될 수 있는 중요한 레퍼런스 데이터를 제공한다. 특히, FIM(Fused Injection Modeling) 공정과 결합하여 복잡한 3D 구조의 섬티레이터 어레이를 제작하면서도 1% 미만의 낮은 광학적 누화를 달성할 수 있다는 결과는, 차세대 입자 추적기 및 열량계 개발에 있어 적층 제조 기술의 실효성을 강력히 뒷받침한다.

---

## References

- [1] C. Betancourt, A. Blondel, R. Brundler, A. Daetwyler, Y. Favre, D. Gascon, S. Gomez, A. Korzenev, P. Mermod, E. Noah, et al., JINST 12 (11), P11023, arXiv:arXiv:1709.08972 [physics.ins-det].
- [2] A. Korzenev et al., JINST 17 (01), P01016, arXiv:2109.03078 [physics.ins-det].
- [3] P.-A. Amaudruz et al., Nucl. Instrum. Meth. A 696, 1 (2012), arXiv:1204.3666 [physics.ins-det].
- [4] L. Aliaga et al. (MINERvA), Nucl. Instrum. Meth. A 743, 130 (2014), arXiv:arXiv:1305.5199 [physics.ins-det].
- [5] D. G. Michael et al. (MINOS), Nucl. Instrum. Meth. A 596, 190 (2008), arXiv:0805.3170 [physics.ins-det].
- [6] D. Allan et al., JINST 8, P10019, arXiv:1308.3445 [physics.ins-det].
- [7] C. Joram, U. Uwer, B. D. Leverington, T. Kirn, S. Bachmann, R. J. Ekelhof, and J. Müller, LHCb Scintillating Fibre Tracker Engineering Design Review Report: Fibres, Mats and Modules, Tech. Rep. (CERN, Geneva, 2015).
- [8] V. Andreev et al., Nucl. Instrum. Meth. A 564, 144 (2006).
- [9] Y. Abreu et al. (SoLid), JINST 12 (04), P04024, arXiv:1703.01683 [physics.ins-det].
- [10] A. Blondel et al., JINST 13 (02), P02006, arXiv:1707.01785 [physics.ins-det].
- [11] S. Gwon et al., Phys. Rev. D 107, 032012 (2023), arXiv:2211.17037 [hep-ex].
- [12] C. Harper and E. Petrie, Plastics Materials and Processes: A Concise Encyclopedia (2003).
- [13] R. Appel, G. Atoyan, B. Bassalleck, E. Battiste, D. Bergman, K. Bösiger, D. Brown, V. Castillo, N. Cheung, S. Dhawan, H. Do, J. Egger, S. Eilerts, C. Felder, H. Fischer, H. Gach, R. Giles, S. Gninenko, W. Herold, J. Hotmer, V. Issakov, O. Karavichev, H. Kaspar, D. Kraus, D. Lazarus, V. Lebedev, L. Leipuner, P. Lichard, J. Lowe, J. Lozano, T. Lu, H. Ma, B. Magurno, W. Majid, W. Menzel, C. Miller, M. Nickelson, I. Ober, P. Pile, S. Pislak, A. Poblaguev, P. Pomianowski, V. Postoev, A. Proskurjakov, P. Rehak, P. Robmann, B. Schmid, A. Sher, A. Sher, E. Shunko, S. Steiner, T. Stever, R. Stotzer, V. Suhov, J. Thompson, P. Truöl, C. Valine, H. Weyer, D. Wolfe, and M. Zeller, Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 479, 349 (2002).
- [14] J. Thevenin, L. Allemand, E. Locci, P. Micolon, S. Palanque, and M. Spiro, Nuclear Instruments and Methods 169, 53 (1980).
- [15] A. Pla-Dalmau, A. D. Bross, and K. L. Mellott, Nucl. Instrum. Meth. A 466, 482 (2001).
- [16] A. Boyarintsev et al., JINST 16 (12), P12010, arXiv:2108.11897 [physics.ins-det].
- [17] S. Berns, A. Boyarintsev, S. Hugon, U. Kose, D. Sgalaberna, A. De Roeck, A. Lebedynskiy, T. Sibilieva, and P. Zhmurin, JINST 15 (10), 10, arXiv:arXiv:2011.09859 [physics.ins-det].
- [18] T. Sibilieva et al., JINST 18 (03), P03007, arXiv:2212.13394 [physics.ins-det].
- [19] S. Berns, E. Boillat, A. Boyarintsev, A. D. Roeck, S. Dolan, A. Gendotti, B. Grynyov, S. Hugon, U. Kose, S. Kovalchuk, B. Li, A. Rubbia, T. Sibilieva, D. Sgalaberna, T. Weber, J. Wuthrich, X. Zhao, and T. D. Collaboration, Journal of Instrumentation 17 (10), P10045.
- [20] T. Sibilieva, A. Boyarintsev, A. Krech, et al., Functional Materials 31 (4), 646 (2024).
- [21] N. Lynch, T. Monajemi, and J. L. Robar, Biomedical Physics Engineering Express 6, 055014 (2020).
- [22] A. Barr, C. da Vià, M. T. B. Shawkat, S. Watts, J. Allison, and G. D’Amen, A neutron sensitive detector using 3d-printed scintillators (2025), arXiv:2507.08663 [physics.ins-det].
- [23] Y. Mishnayot, M. Layani, I. Cooperstein, S. Magdassi, and G. Ron, Review of Scientific Instruments 85, 085102 (2014), https://doi.org/10.1063/1.4891703.
- [24] Y. Kim, N. Zaitseva, M. J. Ford, L. Carman, A. Glenn, M. Febbraro, and P. Hausladen, Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 1055, 168537 (2023).
- [25] C. Chandler, D. H. Porcincula, M. J. Ford, C. Hook, X. Zhang, J. Brodsky, and A. Sellinger, ACS Applied Polymer Materials 4, 4069 (2022), https://doi.org/10.1021/acsapm.2c00316.
- [26] B. G. Frandsen, M. Febbraro, T. Ruland, T. W. Stephens, P. A. Hausladen, J. J. Manfredi, and J. E. Bevins, Journal of Nuclear Engineering 4, 241 (2023).
- [27] D. geon Kim, S. Lee, J. Park, J. Son, T. H. Kim, Y. H. Kim, K. Pak, and Y. K. Kim, Nuclear Engineering and Technology 52, 2910 (2020).
- [28] P. Stowell, Z. Kutz, S. Fargher, and L. Thompson, Journal of Instrumentation 16 (01), P01003.
- [29] T. D. Doležal, J. J. Manfredi, B. G. Frandsen, J. E. Bevins, C. Gautam, T. W. Stephens, T. Ruland, and M. T. Febbraro, Nuclear Instruments and Methods in Physics Research Section A: Accelerators, Spectrometers, Detectors and Associated Equipment 1056, 168602 (2023).
- [30] C. Chandler, D. H. Porcincula, M. J. Ford, T. J. Kolibaba, B. Fein-Ashley, J. Brodsky, J. P. Killgore, and A. Sellinger, Additive Manufacturing 73, 103688 (2023).
- [31] T. Weber, A. Boyarintsev, U. Kose, B. Li, D. Sgalaberna, T. Sibilieva, J. Wüthrich, S. Berns, E. Boillat, A. De Roeck, T. Dieminger, M. Franks, B. Grynyov, S. Hugon, C. Jaeschke, and A. Rubbia, Communications Engineering 4, 41 (2025).
- [32] B. Li et al., JINST 20 (04), P04008, arXiv:2412.10174 [physics.ins-det].
- [33] Extruder Noztek Pro HT, https://noztek.com/product/noztek-pro/.
- [34] Noztek Filament Winder 1.0, https://noztek.com/product/noztek-filament-winder-1-0/.
- [35] 3D printer Creatbot F430, https://www.creatbot.com/en/creatbot-f430.html.
- [36] CAEN DT5202, https://www.caen.it/products/dt5202/.