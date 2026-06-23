---
source_pdf: obsidian://open?vault=Obsidian%20Vault&file=300_%EC%97%B0%EA%B5%AC%EC%A0%95%EB%A6%AC%2F320_3D%20%ED%94%84%EB%A6%B0%ED%8C%85%20%EC%84%AC%EA%B4%91%EC%B2%B4%20%EA%B0%9C%EB%B0%9C(%EC%96%91%ED%95%9C%EC%B2%A0%2C%20%ED%95%99%EC%9C%84%EB%85%BC%EB%AC%B8%20%EC%8B%AC%EC%82%AC)%2F329_pdfs%2F116_1-s2.0-S0969806X25006206-main.pdf
authors:
  - claude
---

# 박사학위 심사 관점에서 본 "3D 프린팅 SIL 기반 피부선량평가" 연구의 보완 필요성 종합검토

Yang et al.(한양대, *Radiation Physics and Chemistry* 2025, S0969806X25006206)의 SIL 연구는 **DLP 3D 프린팅 플라스틱 신틸레이터**라는 한양대 김용균 교수 그룹의 10년 축적 기술을 피부선량평가로 확장한 의미 있는 성과지만, **박사학위 논문 단독 주제**로서는 재료·물리량 범위·검증 프로토콜·임상 실증의 네 축 모두에서 명백한 결손이 존재한다. 특히 **MCNPX 단독 검증, 광자(감마)선 4종에 국한된 실험, 이중 레이어만을 가진 단순 구조, 표준편차 33%에 달하는 두께 산포**는 국제 심사 기준(EURADOS SRA 2020의 "real-time skin dose with high spatial resolution modelling of the skin" 우선과제)과 정면으로 충돌한다. 본 보고서는 다섯 관점에서 각 결손을 정량·정성적으로 진단하고, 보완 실험 우선순위와 예상 심사질문 대응 전략을 제시한다.

## 1. Yang et al. 2025 RPC 연구의 자리매김

논문의 핵심은 **표피층(EL) 50 μm + 기저층(BL) 50 μm 이중 구조**를 DLP 3D 프린팅 광경화 레진(PPO/POPOP 도핑 photopolymer, 한양대가 2018년 Son et al., 2020년 Kim DG et al. NET 52(12):2910에서 검증한 레시피)으로 제작하고, **(1) 접촉·비접촉식 두께 측정, (2) MCNPX로 α·전자·광자 fluence-to-dose conversion을 ICRP 116과 비교, (3) subtraction 방식으로 EL 신호를 제거해 BL의 실시간 감마 응답을 분리**한 것이다. 저자 CRediT에서 Han Cheol Yang이 Methodology·Investigation·Conceptualization·Software·Writing을 모두 담당해 **사실상 1저자 박사과정 연구**의 구조를 가지며, Seung Beom Goh(Software/Conceptualization), Kihong Pak(Formal analysis), 지도교수 Yong Kyun Kim(Supervision) 체계가 전형적 한국 박사논문 paper-based thesis의 1개 챕터에 해당한다.

**선행 연구와의 기술적 연속성**은 강하다. Son et al.(2018, *JKPS* 73:887)은 acrylic monomer + naphthalene 레진으로 BC-408 대비 67% 광출력을, Kim DG et al.(2020, *NET* 52:2910)은 15.6 ns 감쇠시간·13.2% 에너지분해능을 확보했고, Kim et al.(2022, *RPC* S0969806X22006624)은 같은 레진을 10 MV X-선·45 MeV 양성자 FLASH RT 선량계로 확장했다. SIL 논문은 이 플랫폼을 피부로 옮긴 응용 논문이며, **그룹의 기술적 독창성은 "플라스틱 신틸레이터로 ICRP 70 μm 기저층을 실시간 측정"이라는 개념**에 집중된다.

그러나 한양대 ScholarWorks와 Elsevier Pure에서 확인되는 Han Cheol Yang의 독립 논문은 **현 단계에서 2025 RPC 1편과 SSRN(Kim HJ et al., NPP radiological impact) 공저 1편**에 그친다. 한양대 원자력공학과의 일반적 요구(주저자 SCI 2편 이상 + 공저 일부)를 충족하려면 최소 1편의 추가 주저자 SCI(E) 논문이 필요하며, 심사에서 "단일 RPC 논문 기반 박사학위"는 **paper count가 아닌 연구 깊이 측면에서도 취약**하다.

## 2. 재료·공정 측면의 결손과 보완 필요성

**단일 재료·단일 공정의 폐쇄성**이 가장 두드러진 한계다. 논문은 DLP 광경화 레진 하나만을 검증했으나, 3D 프린팅 조직등가 문헌은 **다종 재료 체계 비교**를 사실상 학위논문 수준의 요건으로 확립한 상태다. Savi et al.(2021, *RPC* 182:109365)은 PLA(SILK/Black/Bone), PETG, TPU, ABS 등 상용 FDM 필라멘트의 광자 감쇠를 ICRU 44 연조직과 비교해 "**30 keV 이상에서 PMMA·연조직 등가**"임을 정량화했고, Kunert et al.(2022, *Med Phys* 49:7766)은 70–140 kVp 진단영역에서 다수 FDM 필라멘트의 AKAC와 흡수선량을 MC로 교차검증했다. Alssabbagh et al.(2017)은 **9종 재료를 SEM-EDS로 원소조성 분석 후 ICRU 44 9개 장기와 매칭**했고, Depeng et al.(2022, *J Appl Clin Med Phys*)은 PLA/PA12/LCR의 Zeff·ρ를 비교했다.

심사 관점에서 Yang et al.의 결손은 구체적으로 다음과 같다. **첫째**, 광경화 레진의 정확한 원소조성(H/C/N/O 분율)이 SEM-EDS 또는 CHN 원소분석으로 확정되지 않았다. ICRU 44 피부조성(**H 10.0%, C 20.4%, N 4.2%, O 64.5%, 미량 Na/Mg/P/S/Cl/K**)과의 매스 분율 편차는 저에너지 광자 감쇠계수와 베타 stopping power에 직결되므로, 조성이 "**generally similar to ICRP 116**"라는 정성적 서술만으로는 박사논문 수준에 미달한다. **둘째**, PLA/PETG/TPU/PMMA/Formlabs Clear 등 최소 4–5종 재료에 대한 Zeff·ρ·linear attenuation coefficient·CSDA range 벤치마킹이 누락되었다. **셋째**, FDM vs SLA vs DLP vs PolyJet 공정별 층간 계면 void와 배치간 편차가 평가되지 않았다 — Tino et al.(2019 *PMB* 64:21NT05, gyroid 구조), Craft & Howell(MD Anderson) 연구에서 입증된 바와 같이 **공정 방향성이 dose에 5–10% 영향**을 준다.

**재현성·공정 안정성**은 더 심각하다. 논문이 보고한 EL 52.2 ± 18.5 μm, BL 51.1 ± 16.5 μm는 변동계수 35%, 32%로서, ICRP 59의 기저층 50–100 μm 범위 중앙값은 맞추지만 **배치간 품질관리 지표로는 허용 수준 이탈**이다. DLP의 공칭 Z축 해상도가 25–50 μm이므로 **단일 레이어가 50 μm 설계인 경우 ±1 voxel 편차가 곧 ±50% 편차**로 귀결된다. 저에너지 ¹⁴⁷Pm 베타(E_max 225 keV, CSDA ~60 mg/cm²)에서 이 두께 산포는 기저층 선량 불확도 40–100%를 유발한다(Bourgois et al. 2017 *RPD*의 민감도 분석과 일치). 박사논문 수준에서는 **최소 10개 배치(n=10) × 각 배치 5매(n=5) = 50매 산출 후 μ-CT와 백색광 간섭계로 Ra(표면 거칠기), Sq, void ratio를 정량화**하고, Process Capability Index(Cpk ≥ 1.33)를 제시해야 한다.

## 3. 선량평가 물리량 범위의 극단적 협소함

현 단계에서 가장 치명적인 결손이다. 논문은 **감마선 4종(¹³⁷Cs·⁶⁰Co 등 추정)**만 실험했다. 피부선량평가는 그 정의상 **베타선과 저에너지 광자가 주 관심 방사선**이며, 국제 표준 체계는 이를 다음과 같이 강제한다.

| 표준 | 요구사항 | Yang 2025 충족 여부 |
|---|---|---|
| **ISO 6980-1/-2/-3(2022)** | ¹⁴⁷Pm(E_max 0.225 MeV), ⁸⁵Kr(0.687), ⁹⁰Sr/⁹⁰Y(2.28) 3종 β 기준장, 0°–75° 각도 k계수 | **미충족** |
| **IEC 61526:2024 / IEC 62387** | 15 keV–1.25 MeV 광자, 상대응답 0.71–1.67 | 부분 충족 |
| **ICRP 59(1991)** | 기저층 50–100 μm, 대표 70 μm, 1 cm² 평균 | 50 μm 설계만 검증 |
| **ICRU 95(2020)** | Hp(0.07)→**Dlocal skin (Gy)** 운영량 전환 | **전혀 언급 없음** |
| **ICRP 118(2012)** | 홍반 역치 2 Gy, 습성탈락 20 Gy 재현 실험 | 미수행 |

**베타선 평가 부재**가 가장 크다. 피부선량이 임상적 쟁점이 되는 전형적 상황 — 원자력발전소 작업자 ⁹⁰Sr/⁹⁰Y 오염, 핵의학 ¹³¹I 오염, 산업용 ¹⁴⁷Pm 형광 도료, 후쿠시마·체르노빌형 β 낙진 — 은 모두 β 기준장 교정을 전제로 한다. ISO 6980 β 기준장이 빠진 피부선량계 박사논문은 KAERI·KINS·한양대 원자력공학과 기준 어느 것으로도 **본심사 통과가 의문시**되는 수준이다. 보완 실험은 KIRAMS 2차 표준연구실의 ¹⁴⁷Pm·⁸⁵Kr·⁹⁰Sr/⁹⁰Y beam-flattening filter 조사체계 또는 PTW 23392 extrapolation chamber와의 직접 교차교정이 필수다.

**ICRU Report 95 전환기 미반영**은 최소 "인지 서술"이라도 필수다. 2020년 ICRU/ICRP 공동 발행된 ICRU 95는 **Hp(0.07) [Sv] → Dlocal skin [Gy]**로 단위와 개념 모두를 변경했고, 2022년 EURADOS Report 2022-02(Gilvin et al.)와 2024년 Otto 리뷰(*Radiat Prot Dosim*)가 이행 방향을 제시했다. Behrens(2021, *RPD*)의 ISO 6980 β장→ICRU 95 변환계수가 이미 발표되어 있으므로, 박사논문에서 기존 Hp(0.07)과 새 Dlocal skin을 **병기 보고하고 변환 불확도를 정량화**하면 국제 수준으로 격상된다. 현 SIL 논문은 ICRU 116 phantom만 언급할 뿐 ICRU 95, ICRP 145(MRCP, 50 μm 방사선민감 기저세포층 명시), ICRP 147(용량 단위 Gy 권고) 어느 것도 인용하지 않아 **국제 동향 추종 실패**가 명백하다.

**에너지·각도·선량률 3차원 응답 매트릭스**도 없다. IEC 61526:2024 type test는 광자 최소 5종(N-40/60/80/100/S-Cs) × 각도 5개(0°/15°/30°/45°/60°) × 선량률 3–4 decade를 요구한다. 현 논문의 "감마 4종 응답성 확인"은 이 매트릭스의 극히 일부에 불과하며, 선형성·재현성·최소검출선량(MDL, ISO 11929 기준)은 아예 보고되지 않았다.

## 4. 시뮬레이션·검증 프로토콜의 단일성

**MCNPX 단독 검증의 이론적 취약성**이 박사논문 심사에서 반드시 도전받을 지점이다. MCNPX는 전자·광자 기본 컷오프가 1 keV로, 70 μm 이하 micro-scale 에너지침적에서 Penelope(50 eV), Geant4-Livermore(250 eV), Geant4-DNA(~7 eV)와 비교할 때 **저에너지 전자 스펙트럼 정확도에 구조적 한계**를 가진다. Uusijärvi-Lizana et al.(2009, *JNM*)은 PENELOPE 대비 MCNPX가 dose-point kernel 근거리(r/R_CSDA < 0.3)에서 최대 **14% 편차**를 보임을 정량화했는데, 이 영역이 정확히 70 μm 얕은 층에 해당한다. Seltzer et al.(2005, *Med Phys*)이 extrapolation chamber 벤치마크에서 **ESTEP 파라미터 미조정 시 0.6–1.2% 편차**를 보고한 것도 중요한데, Yang 2025는 step-size 민감도 분석을 보여주지 않았다.

박사논문 수준 보완책은 **이중 MC 코드 교차검증**이다. MCNPX 결과를 (1) PENELOPE로 재계산해 저에너지 β의 기준으로 삼고, (2) Geant4-Livermore와 Penelope physics list로 물리모델 의존성을 분리하며, (3) 선택적으로 Geant4-DNA로 기저세포(~10 μm) micro-dose를 계산해 **"같은 거시선량이라도 나노스케일 에너지침적이 다를 수 있음"을 이론적 기여**로 만들 수 있다. 코드간 편차 ≤5%, 실험과 ≤10% 목표가 합리적이다.

**실험 검출기 다중 비교** 역시 필수다. 현 논문은 SIL 자체가 신틸레이터이므로 **독립 기준 검출기와의 교차교정이 없으면 self-consistency 논문**에 머문다. 박사논문 수준 최소 4종 병행이 표준으로, 구체적으로 (1) **MOSkin**(UoW CMRP, 70 μm WED 실시간 gold standard — Kwan 2008, Safari 2015 *Med Phys*), (2) **EBT3 radiochromic film**(153 μm 효과 깊이, 2D 분포), (3) **nanoDot OSLD 또는 박형 TLD-100**(100 μm), (4) **PTW 23392 extrapolation chamber**(β primary standard)의 조합이 권장된다. Kron et al.(1996), Andreozzi et al.(2024, PMC11244671, MR-linac)의 모범사례는 MOSkin + EBT3 + nanoDot + microDiamond + TPS 5중 비교로서 이는 박사논문의 *de facto* 기준선이다.

**불확도 예산(Uncertainty Budget)**은 GUM(JCGM 100) 체계로 재구성해야 한다. 박사논문 수준에서는 MC 통계(Type A, 0.3–1.0%), β 스펙트럼(0.5–1.5%), 광자 cross-section(0.6–0.85%), 전자 stopping power(1.0–2.0%), 재료 조성(1.0%), 기하(0.5–1.3%), 선원 교정(1.5–2.5%), step-size(0.4–1.2%), **code-to-code(3–6%)**, tissue↔water 변환(0.5–2.0%), backscatter(0.6–2.0%), 제동복사(0.25–1.0%) 약 **12개 항목으로 조합불확도 u_c ≈ 4.5–7.5%, 확장불확도 U(k=2) ≈ 9–15%**가 전형적이다. 이 테이블이 없는 박사논문은 국제 저널 peer review 단계에서부터 거부될 가능성이 높다.

## 5. 구조·정밀도 및 임상·응용적 실증의 공백

**피부 다층 구조의 재현 수준**이 해부학적으로 부실하다. 실제 피부는 **stratum corneum 10–40 μm + stratum lucidum/granulosum/spinosum/basale로 구성된 epidermis 50–150 μm + dermis 1–3 mm + subcutis**의 적어도 3–4층 계층이며, Whitton & Everall(1973, *BJD*)과 Oltulu et al.(2018)이 보고한 체부별 epidermis는 44–440 μm로 큰 차이를 보인다. 단순 EL+BL 2층은 **ICRP 59 정의(50–100 μm basal depth)를 평균값으로만 만족**할 뿐, 손등·얼굴·발바닥 등 실제 임상 응용 부위의 다양성을 대표하지 못한다. μ-CT 3D 재구성, 광간섭단층촬영(OCT), 백색광 간섭계로 **층간 계면의 void·delamination·굴곡을 정량화**하고, 최소 2–3가지 해부학적 변이형(손등 70 μm, 가슴 80 μm, 손바닥 400 μm)을 구현해 민감도를 보여야 한다.

**응용·임상 실증**은 사실상 전무하다. 박사논문 "보완 연구 방향"으로 제시할 우선순위 실험은 다음과 같다.

첫째, **방사선 사고 시나리오 재현**이다. Goiânia 사고(IAEA Safety Report No. 2, ¹³⁷Cs 50.9 TBq)의 hot particle 피부 괴사 상황, 후쿠시마 작업자 β-발수 노출, 국내 2005년 KAERI 사고 등을 재구성 geometry로 SIL에 구현하고 VARSKIN+ 또는 ICRP 116 LSD와 비교해 **retrospective dosimetry tool로서의 타당성**을 입증해야 한다.

둘째, **중재시술 피부선량 실증**이다. EURADOS Report 2019-02(Knežević et al., WG12)가 중재방사선·중재심장학의 patient maximum skin dose를 전략 연구 과제로 지정했으므로, 관상동맥조영·TACE·RF ablation 등 실제 임상 환경에서 **MOSkin과 SIL 동시 in vivo/ex vivo 교차측정**이 현실적이고 임상 임팩트가 크다.

셋째, **다양한 오염형태(점선원·면오염·hot particle)** 시나리오다. Bourgois et al.(2017, *RPD*, MCNP6 + ICRP 116)이 제시한 1 cm² 면오염, 점선원 분포, 피부내 흡수(percutaneous) 각각에 대한 반응 특성이 필요하다.

넷째, **선량률 범위 확장**이다. 중재시술 실시간 모니터링(수 mGy/min)과 FLASH RT 표면선량(>40 Gy/s)까지 포괄하는 선량률 의존성 실험이 plastic scintillator의 quenching 특성과 Cherenkov 기여를 평가하는 핵심이다.

## 6. 박사학위 수준의 차별화·독창성 진단

**선행 연구 대비 차별점은 존재하나 불충분**하다. Savi 2021·Kunert 2022는 진단 에너지 소프트조직 phantom에 국한되고 μm 스케일 구조가 없으며, Miller 2020(pediatric torso), Tino 2019(gyroid) 역시 macroscopic 구조다. Yang 2025의 **"3D 프린팅 신틸레이터 + μm 이중층 + 실시간 광학 판독"** 조합은 국제적으로 신규하며 EURADOS SRA 2020의 "real-time skin dose with high spatial resolution modelling" 우선과제에 부합한다. 그러나 이 차별점을 박사논문 수준으로 확립하려면 (1) Wollongong MOSkin 그룹의 20년 축적(Kwan 2008~Thorpe 2016~Safari 2015 *Med Phys*)과의 **정량적 head-to-head 비교**, (2) plastic scintillator vs MOSFET의 에너지·각도·선량률 각각에서의 상대 우수성 matrix 증명, (3) Cherenkov/quenching/온도의존성 등 plastic scintillator 고유 체계적 편향의 교정 알고리즘 개발이 필요하다.

**이론적 기여**가 상대적으로 빈약하다. 현 SIL 논문은 "공학적 제작 + 벤치마크"에 머물러 있다. 박사논문은 최소 한 가지 이론적 독창성을 요구한다. 후보로는 (a) 얇은 신틸레이터 층에서의 Birks' law 확장 모델(dE/dx 의존 quenching을 저에너지 β에 대해 재보정), (b) Optical cross-talk 역문제 풀이(EL·BL subtraction을 정식 inverse problem으로 정립), (c) Micro-scale nonequilibrium energy deposition의 analytical model, (d) ICRU 95 Dlocal skin → plastic scintillator light output 변환계수의 범용 공식화 중 1–2개를 제시하면 이론적 깊이가 확보된다.

**SCI 논문 실적**: Yang의 주저자 SCI(E) 논문은 2025 RPC 1편만 확인된다. 한양대 원자력공학과 박사학위 규정은 대개 주저자 SCI(E) 2편 또는 주저자 1편 + 공저 2편을 요구하므로, **최소 1편의 추가 주저자 논문**(예: β 기준장 응답 특성을 별도 논문으로 분리, 또는 다중 MC 코드 교차검증 결과를 독립 논문화)이 본심사 전에 게재되어야 한다. 학위논문 paper-based thesis의 표준 구조는 3–4개 장의 독립 연구로서, 현 단계에서 유의미한 추가 2편이 필요하다.

## 7. 학위논문 챕터 구조 및 예상 심사 질문 대응

박사논문 목표 구조는 다음과 같이 제안된다. **Ch.1 Introduction**(피부선량 임상·규제 동기, ICRP/ICRU 체계), **Ch.2 Literature Review & Theoretical Background**(피부 다층 해부, ICRP 59/118/145/147, ICRU 95, ISO 6980, 3D 프린팅 조직등가 문헌, plastic scintillator 원리와 Birks' law), **Ch.3 SIL 설계·제작·특성분석**(현 2025 RPC + 재료 4–5종 비교 + QA: μ-CT, SEM-EDS, Ra, Cpk), **Ch.4 Monte Carlo 다중 코드 교차검증**(MCNPX + PENELOPE + Geant4, 불확도 예산 GUM), **Ch.5 다종 방사선 실험 검증**(광자 5종 + β 3종 × 각도 5개 × 선량률 매트릭스, MOSkin/EBT3/TLD/extrapolation chamber 4중 비교), **Ch.6 응용 시나리오**(방사선 사고 재구성, 중재시술 실증, hot particle), **Ch.7 Discussion**(ICRU 95 Dlocal skin 변환, Hp(0.07) 병기, 한계와 일반화), **Ch.8 Conclusion & Future Work**. 총 150–200페이지, 참고문헌 200–300건이 한국 공학 박사논문 표준이다.

**예상 심사 질문과 대응 전략**은 다음이 가장 개연성 높다. "**왜 MCNPX만 썼는가, 70 μm 얕은 층에서 1 keV 컷오프의 영향은?**" → 이중 MC 코드 결과와 step-size 민감도 테이블로 응답. "**ICRU 95 전환기에 구 Hp(0.07) 체계만 쓴 이유?**" → Hp(0.07)과 Dlocal skin 병기 보고, Behrens 2021 변환계수 인용, EURADOS 2022-02 이행 타임라인 서술. "**두께 CV 33%가 기저층 선량에 미치는 정량적 영향은?**" → 핵종별(¹⁴⁷Pm/⁹⁰Sr-Y/⁶⁰Co) 민감도 곡선 제시, α 핵종은 별도 취급. "**왜 PLA/PETG 대신 광경화 레진인가?**" → 신틸레이션 광출력과 μm 해상도의 trade-off, 4–5종 재료 Zeff·ρ·CSDA 비교 테이블. "**MOSkin 대비 우수성은?**" → 실시간성·각도의존성·제작비·재현성 각각에서의 정량 비교. "**이론적 기여는 무엇인가?**" → Birks 확장 모델 또는 cross-talk 역문제 풀이. "**임상 현장 도입 가능성?**" → 중재시술 in vivo 실증 데이터와 IRB 프로토콜.

## 결론 — 현재 상태와 박사학위 도달 거리의 간극

Yang et al.(2025) SIL 논문은 **개념적 독창성과 한양대 그룹의 기술 축적 면에서는 명백한 강점**을 가지나, 단독으로는 박사학위 논문의 3–4개 독립 연구 중 1개 장에 불과하며, **재료 다각화·β 기준장 교정·다중 MC 교차검증·4종 이상 검출기 벤치마크·ICRU 95 대응·임상 실증**의 여섯 축에서 체계적 보완이 필수다. 우선순위로 (1) **ISO 6980 β 3종 응답 실험 + MOSkin 교차교정**(별도 SCI 1편), (2) **PENELOPE/Geant4 이중 코드 검증 + GUM 불확도 예산**(Ch.4), (3) **재료 4–5종 조직등가 비교**(별도 단신 논문), (4) **중재시술 또는 사고 시나리오 응용 실증**(Ch.6)의 네 축 보완이면 한양대·KAIST·서울대 수준의 박사학위 심사를 무리 없이 통과할 것이다. EURADOS SRA 2020이 피부선량 실시간 측정을 유럽 전략 우선과제로 지정한 현 시점은 이 연구를 국제 수준으로 격상시킬 매우 유리한 타이밍이며, 보완만 이뤄진다면 **IAEA·ICRU 후속 권고에 기여할 수 있는 박사논문**이 될 잠재력이 분명하다.