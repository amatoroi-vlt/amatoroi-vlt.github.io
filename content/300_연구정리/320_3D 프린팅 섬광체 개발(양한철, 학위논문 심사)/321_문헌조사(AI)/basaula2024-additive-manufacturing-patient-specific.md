---
title: "Additive manufacturing of patient specific bolus for radiotherapy: large scale production and quality assurance"
authors: ["Basaula, D.", "Hay, B.", "Wright, M.", "Hall, L.", "Easdon, A.", "McWiggan, P.", "Yeo, A.", "Ungureanu, E.", "Kron, T."]
year: 2024
venue: "Physical and Engineering Sciences in Medicine"
doi: "10.1007/s13246-024-01385-1"
arxiv: ""
paper_id: "basaula2024-additive-manufacturing-patient-specific"
source_pdf: "[[101_13246_2024_Article_1385.pdf]]"
tags: [paper, paper/reviewed, topic/3d-printing-bolus]
aliases: ["Basaula 2024"]
status: reviewed
analyzed_at: 2024-05-24
verification_pass_rate: 1.0
---

# Basaula et al. (2024) — Additive manufacturing of patient specific bolus for radiotherapy: large scale production and quality assurance

**Venue**: Physical and Engineering Sciences in Medicine
**DOI**: [10.1007/s13246-024-01385-1](https://doi.org/10.1007/s13246-024-01385-1) · **arXiv**: []()
**PDF**: ![[101_13246_2024_Article_1385.pdf#page=1]]

---

## Executive Summary

이 논문은 대형 암 센터에서 50개월(2018년 11월 ~ 2023년 2월) 동안 2000개 이상의 환자 맞춤형 3D 프린팅 볼루스(bolus)를 생산한 경험과 품질 보증(QA) 프로그램을 문서화한 연구이다 [[101_13246_2024_Article_1385.pdf#page=1|p.1, §Abstract]]. Fused Deposition Modeling (FDM) 방식의 3D 프린터와 Polylactic Acid (PLA) 소재를 사용하여 매끄럽고 재현성 있는 볼루스를 대규모로 생산할 수 있음을 입증하였다 [[101_13246_2024_Article_1385.pdf#page=1|p.1, §Abstract]]. 특히, 초기 전수 검사에서 표준화된 QC 웨지(wedge)를 이용한 정기 검사로 QA 프로세스를 간소화하여 임상 워크플로우의 효율성을 크게 향상시켰다 [[101_13246_2024_Article_1385.pdf#page=4|p.4, §Materials and methods]]. 다양한 PLA 소재 테스트 결과, Spidermaker PLA가 균일성과 CT 번호 일관성(80 HU +/- 8HU) 측면에서 가장 우수한 성능을 보였다 [[101_13246_2024_Article_1385.pdf#page=1|p.1, §Abstract]].

---

## Problem & Motivation

방사선 치료 시 유방암이나 두경부암 환자의 피부 선량을 최적화하기 위해 볼루스가 널리 사용되며, 환자 개인의 해부학적 구조에 맞춘 맞춤형 볼루스의 필요성이 증가하고 있다 [[101_13246_2024_Article_1385.pdf#page=1|p.1, §Introduction]]. 이에 따라 많은 의료 기관에서 3D 프린팅 기술을 도입하여 볼루스를 제작하고 있으나, 볼루스가 방사선 치료 과정의 중요한 부분으로 자리 잡으면서 정확성과 재현성을 보장하기 위한 체계적인 품질 보증(QA) 프로그램의 확립이 필수적으로 요구된다 [[101_13246_2024_Article_1385.pdf#page=2|p.2, §Introduction]]. 본 연구는 대규모 암 센터에서의 장기간 3D 프린팅 볼루스 생산 경험을 공유하고, 추가적인 작업 부담을 합리화하면서도 효과적인 자체 QA 시스템을 구축 및 평가하는 것을 목적으로 한다 [[101_13246_2024_Article_1385.pdf#page=2|p.2, §Introduction]].

---

## Methods

본 연구는 호주 빅토리아주에 위치한 Peter MacCallum Cancer Centre의 5개 캠퍼스에서 수행되었다 [[101_13246_2024_Article_1385.pdf#page=2|p.2, §Materials and methods]]. 최대 5대의 산업용 FDM 3D 프린터(Raise 3D Technologies Inc.)를 운용하였으며, 비용, 가용성, 표면 매끄러움, 기포 발생 여부 등을 기준으로 다양한 제조사의 PLA 기반 소재를 평가하였다 [[101_13246_2024_Article_1385.pdf#page=2|p.2, §Materials and methods]]. 주요 프린팅 파라미터는 내부 채움(Infill) 100%, 노즐 직경 0.4 mm, 압출기 온도 210 °C, 출력 속도 60 mm/sec, 압출 폭 0.48 mm, 레이어 높이 0.2 mm로 설정되었다 [[101_13246_2024_Article_1385.pdf#page=2|p.2, §Materials and methods]]. 볼루스 제작 워크플로우는 Varian Eclipse 치료 계획 시스템(TPS)에서 설계 후 STL 파일로 내보내고, Netfabb 소프트웨어로 메쉬를 수정 및 평활화한 뒤, Simplify3D(버전 5.1.2)로 슬라이싱하여 출력하는 과정을 거쳤다 [[101_13246_2024_Article_1385.pdf#page=3|p.3, §Materials and methods]]. 초기에는 모든 볼루스에 대해 CT 스캔을 통해 두께, 균일성, CT 번호(HU)를 전수 검사하였으나(허용 오차: 광자선 볼루스 두께 +/- 1 mm, 전자선 볼루스 두께 +/- 0.5 mm, 광자선 HU +/- 100, 전자선 HU +/- 50), 50개의 샘플 검사 후 2018년 12월부터는 3단계 두께(5, 10, 15 mm)를 가진 QC 웨지를 매월 또는 주요 변경 사항 발생 시 출력하여 평가하는 방식으로 QA 프로세스를 간소화하였다 [[101_13246_2024_Article_1385.pdf#page=4|p.4, §Materials and methods]].

---

## Results

2018년 11월 8일부터 2023년 2월 28일까지 총 2089개의 볼루스가 출력되었으며, 이는 연간 약 500개에 달하는 생산량이다 [[101_13246_2024_Article_1385.pdf#page=4|p.4, §Results]]. 전체 볼루스의 93.6%는 광자선 치료(주로 VMAT)에, 6.3%는 전자선 치료에 사용되었으며, 치료 부위별로는 두경부암(n=1400)과 유방/피부암(n=674)이 대부분을 차지했다 [[101_13246_2024_Article_1385.pdf#page=5|p.5, §Results]]. 볼루스 두께는 5 mm가 85.8%, 10 mm가 12.6%로 가장 흔했다 [[101_13246_2024_Article_1385.pdf#page=5|p.5, §Results]]. 출력 시간은 볼루스의 무게에 비례하여 증가했으며, 500 g의 소재를 출력하는 데 약 24시간이 소요되었고, 최대 1966 g의 볼루스는 출력에 최대 5일이 걸렸다 [[101_13246_2024_Article_1385.pdf#page=1|p.1, §Abstract]] [[101_13246_2024_Article_1385.pdf#page=5|p.5, §Results]]. 소재 평가 결과, 프리미엄 소재인 Spidermaker PLA (Fair skin)가 환자 볼루스(평균 80 HU, SD=9) 및 QC 웨지(평균 78 HU, SD=7) 모두에서 가장 우수한 HU 번호 재현성을 보였으며, 스캔된 볼루스의 HU 값과도 가장 잘 일치했다 [[101_13246_2024_Article_1385.pdf#page=6|p.6, §Table 1]]. Spidermaker PLA로 출력한 QC 웨지의 두께 측정 결과, 표준 편차가 0.1~0.2 mm 수준으로 매우 높은 품질과 재현성을 나타냈다 [[101_13246_2024_Article_1385.pdf#page=7|p.7, §Table 2]]. 주요 실패 유형으로는 5 mm 미만의 얇은 볼루스 출력 시 발생하는 해상도 한계 및 불균일한 HU 값, 그리고 볼루스 내부의 저밀도 영역(air gap) 발생 등이 보고되었다 [[101_13246_2024_Article_1385.pdf#page=7|p.7, §Results]] [[101_13246_2024_Article_1385.pdf#page=10|p.10, §Discussion]].

---

## Critical Review

### 방법론·실험설계 타당성

이 연구는 50개월이라는 장기간에 걸쳐 2000개 이상의 대규모 실제 임상 데이터를 수집하고 분석했다는 점에서 통계적 신뢰성과 외적 타당도가 매우 높다 [[101_13246_2024_Article_1385.pdf#page=4|p.4, §Results]]. 초기 전수 검사 방식에서 3단계 QC 웨지를 활용한 표본 검사 방식으로 QA 프로세스를 전환한 과정이 합리적인 근거와 함께 제시되었으며, 이는 실제 임상 환경에서의 작업 부하를 줄이면서도 품질을 유지할 수 있는 현실적이고 타당한 접근이다 [[101_13246_2024_Article_1385.pdf#page=4|p.4, §Materials and methods]]. 또한, 다양한 PLA 재료를 비교 분석하여 최적의 재료(Spidermaker)를 선정한 과정은 HU 값, 두께 편차 등 객관적인 정량적 데이터에 기반하고 있어 방법론적으로 견고하다 [[101_13246_2024_Article_1385.pdf#page=6|p.6, §Table 1]].
평가자 해석: 비록 단일 기관(여러 캠퍼스 포함)의 경험에 국한된 후향적 연구라는 한계가 있으나, 사용된 3D 프린터(Raise 3D)와 소프트웨어(Eclipse, Netfabb, Simplify3D)가 범용적인 상용 제품이므로 다른 방사선 치료 기관에도 충분히 적용 및 재현 가능한 결과로 판단된다.

### 선행연구 대비 기여도·한계

기존의 많은 연구들이 주로 소규모 환자군을 대상으로 하거나 특정 부위에 대한 3D 프린팅 볼루스의 선량학적 적용 가능성을 탐색하는 데 그친 반면, 이 연구는 대규모 생산 시스템 구축과 장기적이고 체계적인 품질 관리(QA) 가이드라인 확립에 초점을 맞추었다는 점에서 임상적 기여도가 크다 [[101_13246_2024_Article_1385.pdf#page=2|p.2, §Introduction]]. 저자들은 5 mm 미만의 얇은 볼루스 제작 시 발생하는 윤곽 해상도 문제와 불균일한 밀도 등의 한계를 명확히 식별하고, 이를 바탕으로 최소 권장 두께를 5 mm로 설정하는 실질적인 가이드라인을 제시하였다 [[101_13246_2024_Article_1385.pdf#page=10|p.10, §Discussion]].
평가자 해석: FDM 방식의 근본적인 특성상 출력 시간이 오래 걸린다는 점(500g에 약 24시간)은 여전히 극복해야 할 한계로 남아 있으며, 긴급하게 치료를 시작해야 하는 환자를 위한 대안(예: superflab 임시 사용)이 병행되어야 함을 시사한다. 또한, 연간 120 kg에 달하는 PLA 폐기물 문제와 관련하여 재활용 가능성을 언급하였으나, 이에 대한 구체적인 방법론이나 결과가 포함되지 않은 점은 아쉽다.

---

## Implications for Our Research

대규모 3D 프린팅 볼루스 생산 시스템을 구축하거나 운영할 때, 이 논문에서 제시한 표준화된 QC 웨지 기반의 정기적인 QA 프로세스를 도입하면 품질 관리의 효율성을 크게 높이고 임상 인력의 작업 부담을 경감할 수 있을 것이다.
볼루스 제작용 3D 프린팅 재료를 선정할 때는 단순히 출력의 용이성이나 비용뿐만 아니라, 방사선 치료 계획 시스템과의 호환성(HU 값의 일관성 및 재현성) 및 광학 표면 유도 시스템(SGRT)과의 호환성(표면 반사율, 색상 등)을 종합적으로 고려해야 함을 강력히 시사한다.
특히 5 mm 미만의 얇은 볼루스 제작 시 발생할 수 있는 오류(내부 기포, 불균일한 밀도)를 방지하기 위해, 프린팅 파라미터(extrusion multiplier 등)의 세밀한 최적화가 필요하며, 해상도 한계를 극복하기 위해 SLA나 PolyJet 등 다른 방식의 3D 프린팅 기술 도입을 비교 검토해 볼 필요가 있다.

---

## References

- [1] Fujimoto K, Shiinoki T, Yuasa Y, Hanazawa H, Shibuya K (2017) Efficacy of patient-specific bolus created using three-dimensional printing technique in photon radiotherapy. Phys Med 38:1–9
- [2] Su S, Moran K, Robar JL (2014) Design and production of 3D printed bolus for electron radiation therapy. J Appl Clin Med Phys 15:4831
- [3] Rossi M, Boman E, Kapanen M (2019) Optimal selection of optimization bolus thickness in planning of VMAT breast radiotherapy treatments. Med Dosim 44:266–273
- [4] Kudchadker RJ, Hogstrom KR, Garden AS, McNeese MD, Boyd RA, Antolak JA (2002) Electron conformal radiotherapy using bolus and intensity modulation. Int J Radiat Oncol Biol Phys 53:1023–1037
- [5] Tino R, Leary M, Yeo A, Kyriakou E, Kron T, Brandt M (2020) Additive manufacturing in radiation oncology: a review of clinical practice, emerging trends and research opportunities. Int J Extreme Manuf 2:012003
- [6] Tino R, Yeo A, Leary M, Brandt M, Kron T (2019) A systematic review on 3D-Printed imaging and Dosimetry Phantoms in Radiation Therapy. Technol Cancer Res Treat 18:1533033819870208
- [7] Asfia A, Novak JI, Mohammed MI, Rolfe B, Kron T (2020) A review of 3D printed patient specific immobilisation devices in radiotherapy. Phys Imaging Radiat Oncol 13:30–35
- [8] Biltekin F, Yazici G, Ozyigit G (2021) Characterization of 3D-printed bolus produced at different printing parameters. Med Dosim 46:157–163
- [9] Burleson S, Baker J, Hsia AT, Xu Z (2015) Use of 3D printers to create a patient-specific 3D bolus for external beam therapy. J Appl Clin Med Phys 16:5247
- [10] Lee VWY, Liu ACH, Cheng KW, Chiang CL, Lee VH (2023) Dosimetric benefits of 3D-printed modulated electron bolus following lumpectomy and whole-breast radiotherapy for left breast cancer. Med Dosim 48:37–43
- [11] Ricotti R, Ciardo D, Pansini F, Bazani A, Comi S, Spoto R et al (2017) Dosimetric characterization of 3D printed bolus at different infill percentage for external photon beam radiotherapy. Phys Med 39:25–32
- [12] Wang X, Zhao J, Xiang Z, Wang X, Zeng Y, Luo T et al (2022) 3D-printed bolus ensures the precise postmastectomy chest wall radiation therapy for breast cancer. Front Oncol 12:964455
- [13] Zhang Y, Huang Y, Ding S, Liang J, Kuang J, Mao Q et al (2022) A clinical trial to compare a 3D-printed bolus with a conventional bolus with the aim of reducing cardiopulmonary exposure in postmastectomy patients with volumetric modulated arc therapy. Cancer Med 11:1037–1047
- [14] Maxwell SK, Charles PII, Cassim N, Kairn T, Crowe SB (2020) Assessing the fit of 3D printed bolus from CT, optical scanner and photogrammetry methods. Phys Eng Sci Med 43:601–607
- [15] Kang D, Wang B, Peng Y, Liu X, Deng X (2020) Low-cost Iphone-assisted Processing to obtain Radiotherapy Bolus using Optical Surface Reconstruction and 3D-Printing. Sci Rep 10:8016
- [16] Brown K, Kupfer T, Harris B, Penso S, Khor R, Moseshvili E (2022) Not all 3D-printed bolus is created equal: variation between 3D-printed polylactic acid (PLA) bolus samples sourced from external manufacturers. J Med Radiat Sci 69:348–356
- [17] Kairn T, Talkhani S, Charles PH, Chua B, Lin CY, Livingstone AG et al (2021) Determining tolerance levels for quality assurance of 3D printed bolus for modulated arc radiotherapy of the nose. Phys Eng Sci Med 44:1187–1199
- [18] Ungureanu E, Yeo A, Antony R, Zhu L, Geddes V, Hay B et al (2019) Validation of 3D printed bolus for external beam radiation therapy. Abstract of a paper given at EPSM 2018, Adelaide. Australas Phys Eng Sci Med 42:398
- [19] Gopan O, Wu Q (2012) Evaluation of the accuracy of a 3D surface imaging system for patient setup in head and neck cancer radiotherapy. Int J Radiat Oncol Biol Phys 84:547–552
- [20] Krengli M, Gaiano S, Mones E, Ballare A, Beldi D, Bolchini C et al (2009) Reproducibility of patient setup by surface image registration system in conformal radiotherapy of prostate cancer. Radiat Oncol 4:9
- [21] Malone C, Gill E, Lott T, Rogerson C, Keogh S, Mousli M et al (2022) Evaluation of the quality of fit of flexible bolus material created using 3D printing technology. J Appl Clin Med Phys 23:e13490
- [22] Ehler E, Sterling D, Dusenbery K, Lawrence J (2018) Workload implications for clinic workflow with implementation of three-dimensional printed customized bolus for radiation therapy: a pilot study. PLoS ONE 13:e0204944
- [23] Dipasquale G, Poirier A, Sprunger Y, Uiterwijk JWF, Miralbell R (2018) Improving 3D-printing of megavoltage X-rays radiotherapy bolus with surface-scanner. Radiat Oncol 13:203
- [24] Canters RA, Lips IM, Wendling M, Kusters M, van Zeeland M, Gerritsen RM et al (2016) Clinical implementation of 3D printing in the construction of patient specific bolus for electron beam radiotherapy for non-melanoma skin cancer. Radiother Oncol 121:148–153
- [25] Zou W, Fisher T, Zhang M, Kim L, Chen T, Narra V et al (2015) Potential of 3D printing technologies for fabrication of electron bolus and proton compensators. J Appl Clin Med Phys 16:4959
- [26] Michiels S, Barragan AM, Souris K, Poels K, Crijns W, Lee JA et al (2018) Patient-specific bolus for range shifter air gap reduction in intensity-modulated proton therapy of head-and-neck cancer studied with Monte Carlo based plan optimization. Radiother Oncol 128:161–166