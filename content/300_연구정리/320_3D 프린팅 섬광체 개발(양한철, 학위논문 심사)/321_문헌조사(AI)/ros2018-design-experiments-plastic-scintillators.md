---
title: "On the design of experiments based on plastic scintillators using GEANT4 simulations"
authors: ["Ros, G.", "Sáez-Cano, G.", "Medina-Tanco, G. A.", "Supanitsky, A. D."]
year: 2018
venue: "Preprint submitted to Elsevier"
doi: ""
arxiv: "1804.08975v2"
paper_id: "ros2018-design-experiments-plastic-scintillators"
source_pdf: "[[004_1804.08975v2.pdf]]"
tags: [paper, paper/reviewed, topic/plastic-scintillators]
aliases: ["Ros 2018"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 1.0
---

# Ros et al. (2018) — On the design of experiments based on plastic scintillators using GEANT4 simulations

**Venue**: Preprint submitted to Elsevier
**DOI**: []() · **arXiv**: [1804.08975v2](https://arxiv.org/abs/1804.08975v2)
**PDF**: ![[004_1804.08975v2.pdf#page=1]]

---

## Executive Summary

이 논문은 GEANT4 시뮬레이션을 사용하여 플라스틱 섬광체 기반 실험의 최적 설계를 분석한다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]]. 1 MeV에서 1 GeV 범위의 전자 및 양성자의 등방성 플럭스에 대한 응답을 분석하며, 이는 우주선 또는 우주 기상 실험의 전형적인 시나리오이다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]]. 플라스틱 부피와 광검출기 면적의 비율, 그리고 플라스틱 주변의 반사 코팅 사용이 빛 수집 효율에 미치는 영향을 중점적으로 다룬다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]]. 코팅에서 손실된 에너지, 섬광체에 증착된 에너지, 광학적 흡수, 검출되지 않은 섬광 광자의 비율, 광검출기에서의 빛 수집, 펄스 모양 및 시간 매개변수 등 다양한 매개변수를 정량적으로 분석하였다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]].

---

## Problem & Motivation

플라스틱 섬광체는 의학, 입자 물리학, 천체 물리학 등 여러 분야에서 입자 검출기로 널리 사용된다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]]. 전통적으로 광전증폭관(PMT)과 결합되었으나, 실리콘 광증폭기(SiPM)가 유망한 대안으로 떠오르고 있으며, 특히 저궤도(LEO) 임무와 같은 우주 기반 실험에서 가벼운 옵션이 될 수 있다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]]. 기존 문헌에서는 의료 분야나 순수 시뮬레이션을 통한 섬광체 부피의 효과가 분석되었으나, 에너지 입력이 넓은 스펙트럼을 포괄하고 질량이 중요한 우주 임무의 천체 물리학적 시나리오에서는 충분히 분석되지 않았다 [[004_1804.08975v2.pdf#page=2|p.2, §1]]. 따라서 현실적인 조건에서 플라스틱 섬광체를 기반으로 한 실험의 최적 설계에 대한 포괄적이고 새로운 분석이 필요하다 [[004_1804.08975v2.pdf#page=1|p.1, §Abstract]].

---

## Methods

- **시뮬레이션 도구**: GEANT4 시뮬레이션 툴킷을 사용하여 매질 내부의 광자를 추적하고 섬광체 및 코팅의 모든 광학적 특성(방출, 흡수, 반사, 굴절 등)을 고려하였다 [[004_1804.08975v2.pdf#page=3|p.3, §1]].
- **기하학적 구조**: 광검출기는 1 cm 너비의 실리콘 평행육면체로 가정하고, 섬광체와의 접촉 면적은 $L \times L$ ($L=2$ cm)로 설정하였다 [[004_1804.08975v2.pdf#page=3|p.3, §2.1]]. 플라스틱 부피는 $(F \times L)^3$인 큐브로, 스케일 팩터 $F = 1, 3, 10$을 사용하였다 [[004_1804.08975v2.pdf#page=3|p.3, §2.1]].
- **재료 특성**: Fermilab에서 개발된 압출 방식의 플라스틱(밀도 1.08 g/cm³, 굴절률 1.58, 흡수 길이 250 cm, 섬광 수율 8000 ph./MeV, 감쇠 시간 3.6 ns)을 선택하였다 [[004_1804.08975v2.pdf#page=4|p.4, §2.1]] [[004_1804.08975v2.pdf#page=5|p.5, §Table 1]].
- **코팅**: TiO2 펠릿이 혼합된 공압출 반사 코팅을 사용하였으며, 두께는 0.25 mm 및 0.50 mm로 시뮬레이션하였다 [[004_1804.08975v2.pdf#page=5|p.5, §2.1]]. 코팅이 없는 경우도 비교하였다 [[004_1804.08975v2.pdf#page=5|p.5, §2.1]].
- **입력 플럭스**: 1, 10, 30, 100 MeV 및 1 GeV 에너지의 전자 및 양성자의 등방성 플럭스를 1차 입자로 사용하였다 [[004_1804.08975v2.pdf#page=6|p.6, §2.2]]. 각 조건당 200개의 이벤트를 시뮬레이션하여 총 18000개 이상의 시뮬레이션을 수행하였다 [[004_1804.08975v2.pdf#page=6|p.6, §2.2]].
- **광학 표면**: 플라스틱-코팅 인터페이스는 `dielectric-metal` 표면으로 설정하고 반사율을 90%로 지정하였다 [[004_1804.08975v2.pdf#page=7|p.7, §2.3]]. 표면 거칠기 매개변수는 0.5로 설정하였다 [[004_1804.08975v2.pdf#page=6|p.6, §2.3]].

---

## Results

- **코팅에서의 에너지 손실**: 0.25 mm 코팅의 경우, 1 MeV 전자는 에너지의 5-20%를 잃고, 10 MeV 미만의 양성자는 코팅을 통과하지 못한다 [[004_1804.08975v2.pdf#page=9|p.9, §3.3]]. 코팅 두께는 실험의 에너지 임계값에 하한을 부과한다 [[004_1804.08975v2.pdf#page=9|p.9, §3.3]].
- **플라스틱에 증착된 에너지**: 1 MeV 전자는 $F=1, 3, 10$에서 각각 85%, 89%, 89%의 에너지를 증착하지만, 1 GeV 전자는 0.2%, 0.3%, 2%만 증착한다 [[004_1804.08975v2.pdf#page=25|p.25, §Table 4]].
- **광학적 흡수**: 기술적 감쇠 길이(TAL)는 코팅이 없는 경우 $F=1, 3, 10$에 대해 각각 약 1.2, 7.5, 23.0 cm이며, 코팅이 있는 경우 3.5, 28.0, 81.8 cm로 증가한다 [[004_1804.08975v2.pdf#page=13|p.13, §4]].
- **빛 수집**: 기하학적 수집 계수($F_{geom}$)는 $F=1$에서 약 8%이지만 $F=10$에서는 $\le 0.05$%로 감소한다 [[004_1804.08975v2.pdf#page=25|p.25, §Table 4]]. 반사에 의한 수집 계수($F_{ref}$)는 $F=1, 3, 10$에서 각각 약 50%, 11%, 0.5%이다 [[004_1804.08975v2.pdf#page=25|p.25, §Table 4]].
- **광검출기에서의 펄스**: 코팅이 있는 경우 생성된 광자 중 검출되는 비율은 $F=1, 3, 10$에 대해 각각 70%, 12%, 0.8%이다 [[004_1804.08975v2.pdf#page=16|p.16, §7]]. 코팅이 없는 경우 이 비율은 38%, 3.5%, 0.3%로 감소하여, 코팅 사용 시 수집된 빛이 2-3배 증가함을 보여준다 [[004_1804.08975v2.pdf#page=16|p.16, §7]].
- **펄스 시간 매개변수**: 펄스 폭($t_{90}-t_{10}$)은 $F=1, 3, 10$에 대해 각각 7.8 ns, 8.9 ns, 13.0 ns로 플라스틱 부피가 커질수록 증가한다 [[004_1804.08975v2.pdf#page=25|p.25, §Table 4]].

---

## Critical Review

### 방법론·실험설계 타당성

- GEANT4를 활용하여 입자 상호작용부터 광학 광자의 생성, 전파, 검출까지 전체 과정을 상세히 시뮬레이션한 점은 매우 타당하다 [[004_1804.08975v2.pdf#page=3|p.3, §1]].
- 등방성 플럭스를 사용하여 우주 환경을 현실적으로 모사한 점이 돋보인다 [[004_1804.08975v2.pdf#page=6|p.6, §2.2]].
- 평가자 해석: 광검출기를 단순한 실리콘 블록으로 모델링하고 양자 효율(QE)이나 SiPM의 구체적인 특성(예: 다크 카운트, 크로스토크)을 포함하지 않은 점은 실제 실험 설계 시 추가적인 고려가 필요함을 시사한다.

### 선행연구 대비 기여도·한계

- 기존 연구들이 주로 의료용 선량계나 특정 빔 환경에 국한되었던 반면, 이 연구는 우주 임무를 위한 넓은 에너지 스펙트럼과 등방성 입력을 다루어 천체 입자 물리학 분야에 중요한 기여를 한다 [[004_1804.08975v2.pdf#page=2|p.2, §1]].
- 저자 명시 한계: 광검출기의 상세한 시뮬레이션은 복잡한 문제이며 이 연구의 범위를 벗어난다고 명시하였다 [[004_1804.08975v2.pdf#page=8|p.8, §3.1]].
- 추가 식별 한계: 시뮬레이션 결과에 대한 실험적 검증 데이터가 논문에 포함되지 않아, 시뮬레이션 모델의 정확성을 교차 검증하기 어렵다.

---

## Implications for Our Research

- 플라스틱 섬광체 기반 검출기를 설계할 때, 반사 코팅의 두께가 저에너지 입자의 검출 임계값에 미치는 영향을 반드시 고려해야 한다. 특히 저에너지 양성자 검출이 중요한 경우 코팅 두께를 최소화하거나 다른 방식을 모색해야 할 수 있다.
- 검출기 부피가 커질수록 빛 수집 효율이 급격히 감소하고 펄스 폭이 넓어지므로, 대면적 검출기가 필요한 경우 단일 큰 섬광체보다는 여러 개의 작은 섬광체 모듈을 배열하는 방식이 유리할 수 있다.
- GEANT4 시뮬레이션에서 광학 광자의 표면 반사 및 흡수 모델링(예: `glisur` 모델, 표면 거칠기)이 결과에 큰 영향을 미치므로, 우리 연구에서도 이러한 광학적 매개변수를 신중하게 설정하고 검증해야 한다.

---

## References

- [1] SPENVIS, ESA’s SPace ENVironment Information System, https://www.spenvis.oma.be/
- [2] P. Adamson, MINOS Collaboration. Technical Design Report. FERMILAB-DESIGN-1998-02 Experiment: FNAL-E-0875 NUMI-L-337 (1998).
- [3] OPERA Collaboration. Experiment Proposal. CERN/SPSC2000-028, CERN-SPSC-P318, LNGS-P25-00 (2000).
- [4] The Pierre Auger Collaboration. The Pierre Auger Observatory Upgrade - Preliminary Design Report. arxiv.org/1604.03637
- [5] Yu. N. Kharzheev. Scintillation Counters in Modern High Energy Physics Experiments (Review). Physics of Particles and Nuclei, Vol. 46, No. 4, (2015) 678-728.
- [6] Alan Owens. Scintillators on Interplanetary Space Missions. 1430 IEEE Transactions on Nuclear Science, Vol. 55, No. 3 (2008).
- [7] Ph. von Doetinchem et al. The AMS-02 Anticoincidence Counter. Nuclear Physics B (Proc. Suppl.) 197 (2009) 15-18. arxiv.org/abs/0811.4314
- [8] DAMPE Collaboration. The plastic scintillator detector for DAMPE. Astroparticle Physics 94 (2017) 1-10.
- [9] A. S. Beddar, T. R. Mackie, and F. H. Attix. Water-equivalent plastic scintillation detectors for high-energy beam dosimetry: I. Physical characteristics and theoretical consideration. Phys. Med. Biol. 37 (10), 1883-900 (1992).
- [10] K. R. Hogstrom and P. R. Almond. Review of electron beam therapy physics. Phys Med Biol., 51 (2006) 13.
- [11] W. D. Newhauser and Rui Zhang. The physics of proton therapy. Physics in Medicine and Biology, Vol. 60, No. 8 (2015).
- [12] CMS Collaboration. Technical Design Report. CERN/LHCC97-31 (1997).
- [13] L. Archambault et al. Plastic scintillation dosimetry: Optimal selection of scintillating fibers and scintillators. Med. Phys., 32 (2005) 2271-2278.
- [14] R. B. Galloway and H. Savalooni. The dependence on scintillator size of the response of NE213 to electrons and protons. Nuclear Instruments and Methods 199 (1982) 549-555.
- [15] N. Ghal-Eh. Light transport contribution to the timing characteristics of scintillation detectors. Radiation Physics and Chemistry 80 (2011) 365-368.
- [16] A. Dyshkant et al. Extruded scintillator for the Calorimetry applications. AIP Conference Proceedings 867, 513 (2006).
- [17] Riggi et al. GEANT4 simulation of plastic scintillator strips with embedded optical fibers for a prototype of tomographic system. Nuclear Instruments and Methods in Physics Research A, 624 (2010) 583590.
- [18] S. Agostinelli et al. Geant4 simulation toolkit. Nuclear Instruments and Methods in Physics Research A, 506-3 (2003) 250-303.
- [19] M. C. Espirito-Santo et al. Applications of GEANT4 in Astroparticle Experiments. IEEE Transactions on Nuclear Science, Vol. 51, No. 4 (2004).
- [20] Z. Kohley. Modeling interactions of intermediate-energy neutrons in a plastic scintillator array with GEANT4. Nuclear Instruments and Methods in Physics Research A, 682 (2012) 59-65.
- [21] Zhang Li-Ming. Simulation study for a single TOF scintillator using GEANT4. Meas. Sci. Technol., 15 (2004).
- [22] C. C. Guimaraes et al. Performance of GEANT4 in dosimetry applications. Radiation Measurements, Vol. 43, Issues 910 (2008) 1525-1531.
- [23] Jun Zhu et al. Preparation and characterization of a novel UV-curable plastic scintillator. Nuclear Instruments and Methods in Physics Research A, Vol. 817 (2016) 30-34.
- [24] L. Aliaga et al. Design, calibration, and performance of the MINERVA detector. Nuclear Instruments and Methods in Physics Research A, Vol. 743 (2014) 130-159.
- [25] A. D. Supanitsky et al. Underground Muon Counters as a Tool for Composition Analyses. Astroparticle Physics 29 (2008) 461-470.
- [26] R. Alfaro et al. Buried plastic scintillator muon telescope (BATATA). Nuclear Instruments and Methods in Physics Research A, Vol. 617 (2010) 511-514.
- [27] Anna Plau-Dalmau et al. Extruded Plastic Scintillation Detectors. FERMILAB-Conf-99/095. arXiv:physics/9904004
- [28] Jun Zhu et al. The impact of fluorescent dyes on the performances of polystyrene-based plastic scintillators. Nuclear Instruments and Methods in Physics Research A, Vol. 835 (2016) 136-141.
- [29] Tatsuya Kikawa. Measurement of Neutrino Interactions and Three Flavor Neutrino Oscillations in the T2K Experiment. Ph.D. Thesis (2015). Available at http://inspirehep.net/record/1358454/files/kikawa_thesis.pdf.
- [30] L. Torrisi. Plastic scintillator investigations for relative dosimetry in proton-therapy. Nuclear Instruments and Methods in Physics Research B, 170 (2000) 523-530.
- [31] A. Taheri and R. G. Peyvandi. The impact of wrapping method and reflector type on the performance of rod plastic scintillators. Measurement, 97 (2017) 100-110.
- [32] Erik Dietz-Laursonn. Diplom-Thesis (2016). Detailed Studies of Light Transport in Optical Components of Particle Detectors. Available at http://publications.rwth-aachen.de/record/667646/files/667646.pdf.
- [33] Calculator for Skin Effect Depth. http://chemandy.com/calculators/skin-effect-calculator.htm
- [34] A. Plau-Dalmau et al. Extruded Plastic Scintillator for MINERVA. IEEE Nuclear Science Symposium Conference, Record N35-25 (2005).
- [35] S. Lo Meo et al. A Geant4 simulation code for simulating optical photons in SPECT scintillation detectors. JINST, 4 P07002 (2009).