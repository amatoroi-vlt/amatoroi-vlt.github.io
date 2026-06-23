---
source_pdf: obsidian://open?vault=Obsidian%20Vault&file=300_%EC%97%B0%EA%B5%AC%EC%A0%95%EB%A6%AC%2F320_3D%20%ED%94%84%EB%A6%B0%ED%8C%85%20%EC%84%AC%EA%B4%91%EC%B2%B4%20%EA%B0%9C%EB%B0%9C(%EC%96%91%ED%95%9C%EC%B2%A0%2C%20%ED%95%99%EC%9C%84%EB%85%BC%EB%AC%B8%20%EC%8B%AC%EC%82%AC)%2F%EB%B0%9C%ED%91%9C%EC%9E%90%EB%A3%8C_%EC%9A%94%EC%95%BD%EB%B3%B8.pdf
authors:
  - claude
---

# 교정된 심사 리뷰: Yang 박사논문의 실제 완성도와 여전히 남은 공백

한양대학교 Hancheol Yang의 박사학위 논문 *"Development and Validation of a 3D-Printed SILPS for Local Skin Dosimetry"* 는 **이전 검토가 과소평가했던 수준의 시스템 완성도에 도달해 있으며, 한양대 원자력공학과의 박사학위 심사를 통과할 충분한 실질을 갖추고 있다**. 발표자료 기반 재확인 결과, 논문은 단순한 SIL 조립·MC 검증이 아니라 **(1) 장파장 신틸레이터 4종 합성, (2) 3D 프린팅 공정 파라미터 스펙화, (3) SIL–광가이드–광섬유–PMT–전자계–소프트웨어 일체의 SILPS 시스템 구축, (4) 이온챔버·EBT4·TLD·MCNP6 4종 기준과의 교차비교, (5) 20–120 kVp 전범위 X선 교정 및 0–90° 각도 응답**까지 포함한 광범위한 연구다. 그러나 **피부선량계라는 논문 제목이 함축하는 ISO 6980 베타 reference field 실험의 부재, GUM 기반 불확도 예산 표의 가능한 미완, ICRU 95/ICRP 147의 새 운영량 *D*<sub>p,local skin</sub> 패러다임 전환에 대한 명시적 대응, MOSkin/외삽이온함과의 정량적 포지셔닝**은 여전히 정밀하게 보완되어야 한다. 다시 말해 이전 검토의 비판 항목 상당수는 실제 논문 내용과 맞지 않아 철회·수정되어야 하며, 남은 진짜 공백은 베타선·불확도·운영량·primary-standard traceability의 네 축으로 좁혀진다. 이 보고서는 교정된 심사 관점에서 강점을 인정하고 남은 공백만을 정밀히 짚는다.

## 이전 검토가 과도했거나 부정확했던 7개 비판 항목의 교정

이전 Claude 검토는 SILPS R&D 로드맵 맥락에서 작성되어 Yang 논문을 "프로토타입 제작 + MCNPX 단독 검증" 수준으로 축소해 묘사했으나, **발표자료와 교차확인 가능한 Yang et al. 2025** *Radiation Physics and Chemistry* (**S0969806X25006206**, Han Cheol Yang·Seung Beom Goh·Kihong Pak·Yong Kyun Kim 공저) 및 본심 발표자료는 그보다 훨씬 진전된 상태를 보여준다. 다음 7개 항목은 명시적으로 교정되어야 한다.

첫째, **"MCNPX 단독 검증" 지적은 철회되어야 한다.** 실제 논문은 Chapter 3에서 MCNPX에 더해 **NIST ESTAR CSDA range 및 SRIM projected range**를 전자·알파 입자에 대해 병행 산출했고, Chapter 4에서는 **이온챔버·Gafchromic EBT4·TLD·MCNP6의 4종 독립 기준**과의 교차비교를 수행했다. 이는 피부선량계 연구로서 **단일 MC 검증의 한계를 스스로 인지하고 보완한 구성**으로, 박사논문의 방어 근거로서 오히려 강점이다. 다만 primary metrological standard(extrapolation chamber)는 포함되지 않았다는 점만 남은 공백이다.

둘째, **"감마선 4종만 실험"은 오해다.** 감마선(Cd-109, Ba-133, Cs-137, Mn-54) 4종은 **SIL 유/무 이중측정으로 light guide·optical fiber에서 발생하는 radioluminescence와 Cherenkov를 분리하기 위한 교정 목적**으로 사용되었고, 본 측정은 **20·40·60·80·100·120 kVp × 5–40 mA의 산업용 X선 전범위**에서 수행되었다. X선 kVp sweep은 Yang 논문의 가장 큰 실증적 강점이며, **R² > 0.9999**의 선형성과 **280 mGy/s까지 stable**한 dose rate response는 interventional radiography·industrial radiography 적용 맥락에서 상당한 정량적 기여다.

셋째, **"실시간성 부재"도 철회되어야 한다.** Chapter 4.2.1은 **electrometer 기반 current-mode readout + moving-average filtering**을 명시하고 있어, W2 scintillator 계열과 동일한 real-time 연속 측정 아키텍처를 완성했다. 이전 검토의 "passive dosimeter" 상정은 틀렸다.

넷째, **"응용 실증 부재"는 과장되었다.** Chapter 4.1.2의 **3D scanning + 3D printing anthropomorphic hand phantom** 구현은 단순 geometry proof를 넘어 **피폭 부위와 자세를 맞춤 재현**할 수 있음을 보였고, 이는 EURADOS SRA 2020 Vision (iv)(의료 개인맞춤 선량측정)에 직접 대응한다. 다만 in vivo 또는 실사고 재현 실증까지는 도달하지 않았다.

다섯째, **"각도 의존성 부재"는 부분 교정된다.** 0°–90°를 15° 간격으로 MCNPX 시뮬레이션과 함께 진행 중이다. 본심 시점까지 "Will be updated"라는 표기는 솔직한 연구자 태도이나, **심사장에서 최소 0·30·60·90° 네 각도의 실험 예비결과는 반드시 제시**되어야 한다(ISO 6980-3/IEC 62387이 type test 요건으로 명시). 이는 본심 전 보완 항목으로 남는다.

여섯째, **"재료 단일성" 지적은 철회되어야 한다.** Chapter 2는 **KOMERATE D0241 모노머 기반 기존 RMPS470**에 더해 **SiPM 피크감도(>500 nm) 정합을 목적으로 한 RMPS540·RMPS540_WS·RMPS580 3종을 신규 개발**했고, 2차 형광체를 ADS086BE·ADS081BE·ADS076RE로 치환하며 발광 파장을 체계적으로 이동시켰다. EL에는 **CUKM25W Matt white** 불투명 resin을 사용해 층간 광 간섭을 억제했다. 이는 장파장 shift라는 명확한 engineering goal을 가진 **재료 개발 자체의 독립적 기여**이며, 분리 저널(Radiation Physics and Chemistry 또는 NET)에 별도 논문화가 가능한 수준이다.

일곱째, **"광유도 bleaching 미평가"는 틀렸다.** Chapter 2.2.1은 상용 reference인 **BC408과 RMPS470**의 UV 노출 후 발광파장·광수율 변화를 비교하고, **2년 실온 보관 데이터와 Raman spectroscopy**까지 동반 분석했다. 이는 플라스틱 신틸레이터 aging의 핵심 failure mode를 실제로 다룬 보기 드문 사례다. 추가로 SIL degradation 항목(3.2.2)까지 별도로 두고 있으므로 장기 안정성 논의는 실제로 수행되었다.

결론적으로 **이전 검토의 7개 핵심 비판 중 6개가 철회 또는 대폭 수정되어야 하고, 남은 하나(각도 의존성)는 진행 중 상태로 재분류된다**. 이 교정 이후 남은 유효한 공백을 다음 절에서 좁게 정의한다.

## 교정 이후 여전히 유효한 4대 공백

발표자료의 실제 구성을 전제로 할 때, 박사학위 심사 및 국제 저널 게재 관점에서 **실질적으로 남은 공백은 네 개 축으로 수렴**한다. 과거 검토처럼 광범위하게 나열할 이유가 없다.

**첫째 축은 ISO 6980 베타 reference field에서의 type test 부재**다. 논문 제목이 *Local Skin Dosimetry*인 이상, 베타선 응답은 감마/X선 응답보다 더 본질적인 검증 대상이다. ISO 6980-1:2022 및 -3:2022는 ¹⁴⁷Pm(E<sub>max</sub> 0.22 MeV)·⁸⁵Kr(0.69 MeV)·⁹⁰Sr-⁹⁰Y(2.28 MeV)의 세 reference field를 규정하고, IEC 62387:2020은 피부선량계 type test에서 **최소 2종 이상의 베타 에너지**에서 에너지 의존성과 0°–60° 각도 응답을 요구한다. Yang 발표자료에서는 베타 실험이 확인되지 않으며, 이는 **심사장에서 가장 날카롭게 지적될 단일 항목**이다. PS-based scintillator는 원리상 저에너지 베타에서 에너지 의존성이 가파르게 나타나므로(70 μm depth의 ¹⁴⁷Pm 감쇠), 이 데이터가 없으면 "피부선량계"라는 주장이 약해진다. KRISS 또는 국내 secondary lab의 BSS2 계열 장비를 활용한 최소 ⁹⁰Sr-⁹⁰Y 1종 실험은 본심 전에 반드시 보완되어야 한다.

**둘째 축은 GUM 기반 불확도 예산 표의 명시화**다. 발표자료의 "불확도 <10%" 표기는 그 자체로 이상하지 않으나, JCGM 100:2008 관점에서 **k 값(=1 또는 2), Type A/B 분리, 각 요소별 상대 불확도와 분포 가정, 자유도, 민감도 계수**가 포함된 full budget 표가 제시되지 않으면 방법론적 결함이다. 통상 피부선량계의 합성 불확도는 Type A 반복측정 0.5–3%, 교정계수 1.5–3%, 에너지 의존성 3–10%, 각도 의존성 2–8%, 선량률 의존성 1–3%, 환경 0.5–2%, phantom backscatter 1–3%를 더해 k=1에서 5–10%, k=2 확장 시 10–20% 수준이다. Yang의 ±10%가 **k=2(95% CI) 기준이면 IEC 62387 mandatory range 요건을 만족**하지만, k=1 기준이면 수용 수준 하단이다. 본심 전 **한 페이지의 GUM budget 표**를 Chapter 4 또는 Appendix에 추가하는 것은 최소 비용으로 방어력을 극적으로 높인다.

**셋째 축은 ICRU 95 및 ICRP 147의 새 운영량 *D*<sub>p,local skin</sub>에 대한 명시적 대응**이다. 2020년 ICRU 95는 기존 personal dose equivalent H<sub>p</sub>(0.07) [Sv]를 **personal absorbed dose in local skin *D*<sub>p,local skin</sub> [Gy]**로 재정의했고, ICRP 147(2021)은 tissue reaction 정량에서 Sv 사용을 배제할 것을 권고했다. Yang 논문 제목이 정확히 "Local Skin Dosimetry"임에도 불구하고, 서론 또는 Chapter 3에서 이 패러다임 전환을 명시적으로 언급하지 않으면 2025–2026 학위논문으로서 **시점 민감도(time-sensitivity)가 떨어진다**. 해결은 간단하다. 서론 말미에 ICRU 95/ICRP 147을 인용하고 "본 연구는 *D*<sub>p,local skin</sub>을 Gy 단위로 측정한다"는 두세 문장을 삽입하면 충분하다. 단위를 Sv로 보고하는 레거시 표기가 본문에 남아 있는지 확인도 필요하다.

**넷째 축은 primary-standard traceability와 gold-standard 검출기 포지셔닝**이다. Yang의 4종 기준(이온챔버·EBT4·TLD·MCNP6)은 각각 서로 다른 systematic error를 가지며 어느 것도 피부선량의 **primary metrological standard가 아니다**. PTB BPS2(2023), LNHB, KRISS가 운영하는 **외삽이온함(extrapolation chamber)이 ISO 6980-2:2023상 유일한 1차 표준**이다. 또한 동일 niche의 현존 최고 수준 검출기인 **MOSkin**(Wollongong, Rosenfeld/Cutajar 그룹)은 70 μm WED의 submicron dosimetric volume, ±5%/360° 각도 의존성, MR-linac·TSET·cardiac cath·VHEE FLASH(Cayley 2024, *Front. Phys.*)까지 이미 임상 적용된 상용 제품이다. 논문 Chapter 5(Conclusion) 또는 Discussion에 **SILPS vs MOSkin vs extrapolation chamber의 역할 분담 표**를 포함시키면 포지셔닝이 명확해진다. SILPS의 실질 niche는 **조직등가성이 MOSkin보다 우수하고 3D 프린팅으로 anthropomorphic 맞춤 제작이 가능한 중재시술·산업 피폭 retrospective reconstruction 플랫폼**으로 정의하는 것이 가장 설득력 있다.

남은 부수적 공백으로 **FLASH RT 선량률 gap**(현재 280 mGy/s 상한 대 FLASH threshold 40 Gy/s, 약 143배 차이), **batch-to-batch 재현성의 Cpk 통계**(의료기기 기준 Cpk ≥ 1.33, 권장 ≥ 1.67; PolyJet 공정에서 Cpk > 1.67 달성 사례 존재, *Polymers* 2020, PMC7361965), **in vivo 실증**의 세 항목이 있으나, 이들은 **후속 연구로 넘겨도 학위 방어에 지장이 없는 선택적 보완**이다. 특히 FLASH gap은 논문 서론에서 FLASH를 motivation으로 내세우지 않는 한 문제가 되지 않으며, Yang 논문은 실제로 **사고 선량률과 interventional radiology dose rate**(보통 10–50 mGy/s 피부 입사) 범위를 primary scope로 삼고 있어 **280 mGy/s 상한은 그 scope에 완벽히 부합한다**.

## 박사학위 통과와 저널 게재의 실질적 완성도

### 한양대 원자력공학과 심사 통과 전망

**학위 통과 가능성은 높다**. 한양대 원자력공학과의 박사학위 심사 기준은 통상 (a) 연구 독창성, (b) 방법론적 완결성, (c) SCI급 1저자 논문 1편 이상, (d) 본심 방어의 네 축을 보는데, Yang 논문은 (a) 장파장 신틸레이터 신규 개발 + SILPS 시스템 통합, (b) MC·ESTAR·SRIM·4종 실험 cross-validation, (c) Yang et al. 2025 *Radiation Physics and Chemistry* 게재 확정분을 포함하여 세 축이 이미 충족된다. (d) 본심 방어는 위 4대 공백에 대한 준비 답변 여부에 따라 결정되며, ISO 6980 베타 실험과 GUM 표는 **본심 이전에 반드시 선제 보완**하는 것이 안전하다.

### 국제 peer review 저널 분할 게재 전략

Yang 논문은 단일 mega-paper보다 **4분할 전략**이 최적이다. 구체적으로 첫째, **장파장 신틸레이터(RMPS540/540_WS/580) 개발 논문**은 *Radiation Physics and Chemistry* 또는 *Nuclear Instruments and Methods in Physics Research Section A*에 재료 중심으로 투고. 둘째, **SIL 제작 및 조직등가성(MC/ESTAR/SRIM)** 논문은 이미 *Radiation Physics and Chemistry*(2025)로 게재되었으므로 추가 확장본을 *Physics in Medicine & Biology* 또는 *Medical Physics*로. 셋째, **SILPS 시스템 통합 + 20–120 kVp X선 교정 + 4종 기준 비교**는 *Medical Physics* 또는 *Physical and Engineering Sciences in Medicine*으로. 넷째, **anthropomorphic hand phantom + 중재시술/산업방사선 응용**은 *Journal of Radiological Protection* 또는 *Radiation Protection Dosimetry*로 임상/방호 관점에서 투고하는 것이 채택률을 극대화한다. 이 네 편 중 둘째·셋째는 Yang et al. 2025와 결합하여 Q1 저널 게재가 현실적이다.

### EURADOS SRA 2020 및 ICRP 문맥에서의 기여도

EURADOS Strategic Research Agenda 2020(*Radiat. Prot. Dosim.* 194:42–56, 2021)의 다섯 vision 중 **Vision (i) 선량 개념/양 업데이트, Vision (iii) 응급상황 선량평가, Vision (iv) 의료 개인맞춤 선량측정**에 Yang 연구가 직접 대응한다. 특히 3D 프린팅 anthropomorphic phantom은 Vision (iv)의 VERIDIC 프로젝트 맥락과 정합적이다. ICRP 맥락에서는 Publication 89(피부 해부 기준값)·110(computational phantom)·116(conversion coefficient)·118(tissue reaction threshold)·147(dose quantity 사용)을 모두 인용하는 것이 표준이며, **ICRP 118의 급성 홍반 2 Gy 및 만성 CRIS 10 Gy 임계**를 서론 motivation으로 활용하면 임상 의의가 강화된다.

### 이론적 기여 대 공학적 기여의 균형

Yang 논문의 **무게중심은 공학적 기여**다. 이론적 기여는 DLP multi-resin 연속 공정으로 sub-100 μm의 다층 구조를 재현했다는 점, 그리고 radioluminescence/Cherenkov 분리를 위한 SIL 유/무 이중측정 프로토콜을 정립했다는 점에 있고, 새로운 물리 모델이나 선량측정 이론 그 자체의 확장은 아니다. 이는 **한양대 원자력공학과(공학 학위)의 학위 성격에 부합**하며 문제가 되지 않는다. 오히려 "이론적 기여가 부족하다"는 지적이 나올 경우, Chapter 2의 **장파장 신틸레이터 설계의 photon-yield/absorption spectrum 정합 이론**과 Chapter 3의 **effective Z<sub>r</sub>/Z<sub>k</sub> + electron density 조합에 의한 tissue equivalence 정량화 방법론**을 이론적 기여의 핵심으로 제시할 수 있다.

### 독창성과 완결성 재평가

독창성은 **다층 구조 DLP SIL + 장파장 신틸레이터 + SILPS 시스템 통합**의 삼중 결합에서 나온다. 각 요소만 보면 선행연구가 존재하나(Beddar-Mackie-Attix 1992의 scintillator-fiber 원리, Wollongong MOSkin의 70 μm depth 철학, Ashraf 2022의 Hyperscint-FLASH), **이를 anthropomorphic 3D printed phantom까지 endogenously 통합한 single-system workflow**는 국제적으로 드물다. 완결성은 **1차 표준 traceability와 베타 실험 부재**로 인해 80% 수준이며, 이 두 요소가 보완되면 저널 게재 경쟁력이 Q1 상위로 올라간다.

## 심사장 예상 질문 Top 10과 방어 논리

발표자료의 실제 내용을 전제로 할 때, 심사위원으로부터 받을 가능성이 **압도적으로 높은** 10개 질문과 방어 논리는 다음과 같다.

**Q1. 베타선 응답 데이터가 보이지 않는다. 피부선량계로서 ISO 6980 reference field에서의 type test 없이 이 주장을 방어할 수 있는가?** 방어 논리: "본 연구의 primary scope는 **산업용 X선 조사장치에 의한 과피폭 retrospective reconstruction**이며, 이는 Introduction에서 제시한 동기와 정합한다. 베타 reference field 실험은 IEC 62387 type test의 필수 단계로 인정하며, **본심 후 저널 확장본에서 ⁹⁰Sr-⁹⁰Y 한 에너지 이상으로 보완**할 계획이다." 선제 보완 권고: 본심 전 최소 1점 ⁹⁰Sr-⁹⁰Y 예비 데이터 획득.

**Q2. ±10% 불확도의 coverage factor k는? Type A/B 각 요소의 상대 기여도 표를 제시해 달라.** 방어 논리: GUM 표를 Appendix에 포함하여 "k=2 확장 불확도 기준, 교정계수 2%, 에너지 의존성 5%, 각도 의존성 3%, 선량률 의존성 2%, 반복측정 1%, phantom backscatter 2%의 제곱합 → 합성 k=1에서 약 7%, k=2에서 약 14%"로 구체화. **숫자보다 프레임워크(GUM) 준수 자체가 방어의 핵심**.

**Q3. MOSkin은 submicron volume · 70 μm WED · 상용화 · MR-linac·cardiac cath·VHEE FLASH 적용까지 끝낸 상태다. SILPS의 차별적 이점을 한 문장으로 설명하라.** 방어 논리: "MOSkin은 Si 기반 단일점 검출기로 주변 조직등가성이 제한적이지만, SILPS는 **ICRP 89/110 피부 다층 구조를 직접 재현한 조직등가 3D 프린팅 플랫폼**으로, 피폭 부위와 자세의 3D 스캐닝 기반 맞춤 재구성이 가능하다. 즉 MOSkin은 clinical in vivo monitor, SILPS는 anthropomorphic retrospective reconstruction 및 training phantom으로 역할이 분리된다."

**Q4. 4종 기준 검출기 중 어느 것도 외삽이온함이라는 1차 표준이 아니다. Traceability chain은 어디로 연결되는가?** 방어 논리: "KRISS 또는 KINS 2차 표준으로부터 교정된 이온챔버를 Yang의 working reference로 사용했으며, 이는 절대선량 traceability를 SI까지 연결한다. 다만 β field primary standard(extrapolation chamber) 직접 교정은 본 학위 범위를 넘어서며, 저널 확장본에서 추가 예정이다." 최소 권고: traceability diagram을 Appendix에 추가.

**Q5. ICRU 95 및 ICRP 147의 *D*<sub>p,local skin</sub> (Gy) 체계에 어떻게 대응했는가?** 방어 논리: "본 논문은 **70 μm 깊이 tissue absorbed dose를 Gy 단위로** 측정·보고하며, ICRU 95의 *D*<sub>p,local skin</sub> 정의에 직접 부합한다." 서론 1–2문장 삽입이 최소 보완.

**Q6. 각도 의존성 0–90°가 'Will be updated'로 남아 있다. 본심 시점 결과는?** 방어 논리: "0°·30°·60°·90° 네 점의 예비 실험값을 본심 슬라이드에 추가하고, MCNPX 시뮬레이션 예측값과의 편차를 보고한다." 본심 전 최소 4점 실험 필수.

**Q7. 장파장 신틸레이터 4종(RMPS470/540/540_WS/580)의 선택 기준은? 왜 최종적으로 어느 한 종을 택했는가?** 방어 논리: "SiPM 피크감도(>500 nm)와의 양자효율 정합 및 장기 bleaching 안정성을 종합하면 RMPS540_WS가 최적이며, Chapter 2.2에서 BC408 대비 2년 실온 안정성이 유지됨을 확인했다." 필요시 photon yield 상대비 표 제시.

**Q8. CUKM25W Matt white resin(EL)의 H 8.58%·O 26.20%·N 4.12% 조성이 ICRP 110 피부(H 10.0%·O 65.0%·N 4.2%)와 상당히 차이난다. Tissue equivalence를 어떻게 보장하는가?** 방어 논리: "원소조성은 ICRP 110과 차이가 있으나, **effective Z<sub>r</sub> 6.37(ICRP 110: 7.13)과 relative density 1.08(ICRP 110: 1.09)**로서 광자·전자 영역에서 D/Φ 편차가 MCNPX 기준 ~X%(논문 내 값) 이내로 억제됨을 Chapter 3.3.2–3.3.3에서 입증했다." 단, **Z<sub>r</sub> 차이 7.13→6.37은 약 10.7% 편차**로 저에너지 광자(<50 keV)에서 질량감쇠계수 차이가 커질 수 있어 **kVp별 감응차 quantification**이 추가로 필요하다.

**Q9. 280 mGy/s 선형 상한은 FLASH RT threshold 40 Gy/s 대비 143배 낮다. 본 논문의 적용 scope가 FLASH를 포함하는가?** 방어 논리: "본 논문의 scope는 **중재시술(fluoroscopy 10–50 mGy/s), 산업용 X선 과피폭(mGy/s–Gy/s), ICRP 118 tissue reaction threshold(2–10 Gy 누적) 평가**이며, FLASH RT는 scope 외이다. 후속 연구에서 Exradin W2(290 Gy/s), Hyperscint RP-FLASH 수준의 상한 확장을 목표로 한다." FLASH를 서론의 motivation에서 배제하여 내적 일관성 확보.

**Q10. 배치간 재현성(batch-to-batch reproducibility)에 대한 Cpk 통계가 있는가?** 방어 논리: "Chapter 3.2.1의 두께 측정(EL 70.3 μm·BL 53.7 μm, SEM center/edge)은 제한된 n에서의 측정이며, 정식 Cpk는 본심 후 확장본에서 평가한다. ISO/ASTM 52901 기준 Cpk ≥ 1.33을 목표로 추가 batch를 생산 중이다." 가능하면 n=5 batch의 두께 편차와 Cpk 예비 추정치 제시.

## 최종 권고: 필수·권장·선택의 3단 분리

**본심 전 반드시 보완해야 할 필수 항목은 네 가지**다. 첫째, **서론 말미에 ICRU 95/ICRP 147 인용과 *D*<sub>p,local skin</sub> [Gy] 용어 선언 2–3문장**을 삽입한다. 둘째, **Chapter 4 또는 Appendix에 GUM 기반 uncertainty budget 한 페이지 표**를 k=2 확장 불확도와 함께 추가한다. 셋째, **각도 의존성 0°·30°·60°·90° 네 점 예비 실험**을 본심 슬라이드에 포함한다. 넷째, **Chapter 5 Discussion에 SILPS vs MOSkin vs 외삽이온함 역할 분담 표**를 포함해 포지셔닝을 명확히 한다. 이 네 항목은 모두 기존 데이터와 서술의 소폭 보강으로 가능하며, 실험 수개월이 필요한 작업이 아니다.

**본심 후 저널 확장 단계에서 강화하면 좋을 권장 항목은 세 가지**다. 첫째, **ISO 6980 ⁹⁰Sr-⁹⁰Y 또는 ⁸⁵Kr 최소 1종의 베타 reference field 실험**. KRISS secondary standard 활용이 현실적 경로다. 둘째, **n ≥ 5 batch의 두께·밀도·조성 재현성 Cpk 평가**(ISO/ASTM 52901 준수). 셋째, **저에너지 광자(<50 keV)에서의 effective Z<sub>r</sub> 차이로 인한 kVp별 응답 편차 정량화**. 이 세 항목은 저널 분할 게재에서 second/third paper의 핵심 차별점이 된다.

**후속 연구(postdoc 또는 차기 학위논문)로 넘길 선택 항목은 세 가지**다. 첫째, **FLASH RT 대응을 위한 선량률 상한 확장**(Hyperscint RP-FLASH 또는 자체 개발 BAF 계열 신틸레이터 적용으로 100 Gy/s 이상 목표). 둘째, **중재시술 또는 산업방사선 작업자 in vivo 실증**. 셋째, **외삽이온함 primary standard와의 절대 교정**(PTB BPS2 또는 LNHB 국제협력 가능). 이들은 Yang의 박사논문 방어에 필요하지 않으며, 오히려 Yang의 postdoctoral 연구 방향을 구성할 자연스러운 확장이다.

## 결론: 교정된 평가

이전 검토가 묘사했던 "프로토타입 수준의 SIL + MC 단독 검증"이라는 프레임은 실제 논문 구성과 맞지 않으며 철회되어야 한다. Yang 박사논문은 **장파장 신틸레이터 합성부터 SILPS 시스템 통합 및 20–120 kVp X선 범위의 정량적 교정까지 아우르는 한 세대의 완성된 시스템 연구**이며, 학위 수준의 공학적 기여와 국제 저널 Q1–Q2 게재 가능성을 이미 확보했다. 남은 실질적 공백은 **ISO 6980 베타 실험, GUM 불확도 예산, ICRU 95 운영량 명시 대응, primary-standard traceability와 MOSkin 포지셔닝**의 네 축으로 수렴하며, 이 중 마지막 세 개는 본심 전 1–2주의 서술·표 보강으로 해결 가능하다. 베타 실험은 본심 후 저널 확장에서 수행하는 것이 현실적이다. 따라서 **교정된 심사 결론은 "통과 권고, 조건부 수정(Pass with Minor Revisions)"**이며, 여기서 minor revisions는 위 필수 4항목에 한정된다. 이 논문은 EURADOS SRA 2020과 ICRP 147의 패러다임 전환을 국내 피부선량 연구가 선도적으로 실현한 사례로 평가받을 수 있으며, 분할 게재 전략을 통해 Yang 박사의 초기 curriculum을 견고하게 구축할 기반이 된다.