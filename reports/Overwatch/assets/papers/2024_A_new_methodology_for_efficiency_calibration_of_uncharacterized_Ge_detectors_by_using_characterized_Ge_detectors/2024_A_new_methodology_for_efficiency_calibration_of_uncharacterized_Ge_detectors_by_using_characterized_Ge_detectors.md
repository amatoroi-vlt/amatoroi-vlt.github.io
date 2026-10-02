---
title: "A new methodology for efficiency calibration of uncharacterized Ge detectors by using characterized Ge detectors"
authors: ["A. Barba-Lobo"]
year: "2024"
source_pdf: "papers/raw/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf"
converted_at: "2026-10-02T14:59:38.257748"
abstract: "| |---|---| |Handling editor: Chris Chantler<br>|The measurement of gamma emitters natural radionuclides is a very relevant subject in environmental radio-<br>activity in many fields. For this, a valid calibration based on the full-energy peak efficiency (_FEPE_) is essential,| |_Keywords:_<br>LabSOCS<br>Efficiency calibration<br>Gamma-ra sectrometr|which can be carried out for gamma-ray spectrometry using Monte Carlo codes (Geant4, LabSOCS, MNCP, etc.)<br>without needing a source preparation and with much less time consuming compared to experimental method-<br>ologies. Therefore, this work aims to develop a methodology for the_FEPE_determination of uncharacterized Ge| |y py<br>Characterized Ge detectors<br>Uncharacterized<br>Natural radionuclides|detectors by using characterized Ge detectors with known_FEPE_. For this, a general relationship was found be-<br>tween the simulated_FEPE_(_ε_<sup>_sim_</sup>) for characterized Ge detectors by LabSOCS and the experimental one (_ε_<sup>_exp_</sup>) for<br>uncharacterized Ge detectors obtained for a problem sample (phosphate rock (PR) in our case), where_ε_<sup>_sim_</sup>and<br>_ε_<sup>_exp_</sup>were factorized using three correction fa"
---

Radiation Physics and Chemistry 221 (2024) 111763 

Contents lists available at ScienceDirect 

# Radiation Physics and Chemistry 

journal homepage: www.elsevier.com/locate/radphyschem 

## A new methodology for efficiency calibration of uncharacterized Ge detectors by using characterized Ge detectors 

### A. Barba-Lobo<sup>a,c,*</sup> , V.M. Exposito-Su´ arez´<sup>b</sup> , J.A. Suarez-Navarro´<sup>b</sup> , J.P. Bolívar<sup>a</sup> 

a _Radiation Physics and Environment Group (FRYMA), Department of Integrated Sciences, Center for Natural Resources, Health and Environment (RENSMA), University of Huelva, 21071, Huelva, Spain_ 

b _Environmental Radioactivity and Radiological Surveillance Unit (URAyVR), Department of Environment, CIEMAT, Av. Complutense 40, 28040, Madrid, Spain_ 

c _Department of Medical Radiation Sciences, Institute of Clinical Sciences, Sahlgrenska Academy at University of Gothenburg, Gothenburg, SE, 413 45, Sweden_ 

|A R T I C L E I N F O|A B S T R A C T|
|---|---|
|Handling editor: Chris Chantler<br>|The measurement of gamma emitters natural radionuclides is a very relevant subject in environmental radio-<br>activity in many fields. For this, a valid calibration based on the full-energy peak efficiency (_FEPE_) is essential,|
|_Keywords:_<br>LabSOCS<br>Efficiency calibration<br>Gamma-ra sectrometr|which can be carried out for gamma-ray spectrometry using Monte Carlo codes (Geant4, LabSOCS, MNCP, etc.)<br>without needing a source preparation and with much less time consuming compared to experimental method-<br>ologies. Therefore, this work aims to develop a methodology for the_FEPE_determination of uncharacterized Ge|
|y py<br>Characterized Ge detectors<br>Uncharacterized<br>Natural radionuclides|detectors by using characterized Ge detectors with known_FEPE_. For this, a general relationship was found be-<br>tween the simulated_FEPE_(_ε_<sup>_sim_</sup>) for characterized Ge detectors by LabSOCS and the experimental one (_ε_<sup>_exp_</sup>) for<br>uncharacterized Ge detectors obtained for a problem sample (phosphate rock (PR) in our case), where_ε_<sup>_sim_</sup>and<br>_ε_<sup>_exp_</sup>were factorized using three correction factors: geometrical, photon self-absorption and true coincidence<br>summing (TCS) effects. Thus, the_ε_<sup>_sim_</sup>/_ε_<sup>_exp_</sup>ratio (_FEPER_) was obtained for two couples of Ge detectors (2 char-<br>acterized and 1 uncharacterized detectors), using 4 different cylindrical geometries (C) and 2 Marinelli (M) ones,<br>and varying the sample thickness (_h_), and gamma energy (_Eγ_) (from 46 keV (<sup>210</sup>Pb) to 1765 keV (<sup>214</sup>Bi)). The<br>consistency obtained for the_FEPER_s for C geometries suggested a constant geometric factor, finding some de-<br>viations for M geometries only at_Eγ <_150 keV. Given a pair of detectors, the behavior of the_FEPER_s was found<br>to be very similar for all geometries, and_h_at each specific_Eγ_. Moreover, a constat relationship between the<br>_FEPERs_of both detector couples versus_Eγ _was found. Then, the influence of the TCS effects was also studied<br>varying the distance between the geometry bottom and detector window. The developed methodology was also<br>validated confirming the consistency of the_FEPERs_, which were found to be independent on the chemical<br>composition and apparent density of the sample, supporting our theoretical hypothesis. Consequently, given that<br>the_FEPER_was found to be independent on the sample type and_h_, using our developed methodology it is possible<br>to obtain_ε_<sup>_exp_</sup>for any sample, geometry and_h_using the_FEPER_, previously obtained at each_Eγ _for the sample<br>selected for methodology development (PR in our case), and the_ε_<sup>_sim_</sup>that is obtained for the desired case.|

#### **1. Introduction
The measurement of natural radionuclides such as<sup>234,228</sup> Th, 228,226Ra, 214,212,210Pb, 214,212,210Bi and 40K is essential for multiple fields of research in environmental radioactivity, and can be applied to radiological control, tracing and residence times of atmospheric aerosol masses, sediment dating, declassification of building materials, among many other applications (Abril, 2023; Appleby and Oldfieldz, 1983; Barba-Lobo, et al., 2023a; Barba-Lobo et al., 2022; Baskaran, 2011). For 

this, it is necessary to choose an appropriate radiometric technique, being gamma-ray spectrometry one of the most used worldwide. The full-energy peak efficiency ( _FEPE_ ) needs to be determined with precision and accuracy for a wide variety of sample matrix types and geometries, as well as for a wide range of energies. 

In the case of the efficiency calibration to obtain the _FEPE_ in the calibration matrix ( _εc_ ) and, subsequently, in any problem sample ( _ε_ ), the use of different types of software in gamma-ray spectrometry has become widespread such as Geant4 (Arce et al., 2014; Dziri et al., 2012; 

* Corresponding author. Radiation Physics and Environment Group (FRYMA), Department of Integrated Sciences, Center for Natural Resources, Health and Environment (RENSMA), University of Huelva, 21071, Huelva, Spain. 

_E-mail address:_ alejandro.barba-lobo@gu.se (A. Barba-Lobo). 

https://doi.org/10.1016/j.radphyschem.2024.111763 Received 15 February 2024; Received in revised form 6 April 2024; Accepted 10 April 2024 Available online 18 April 2024 0969-806X/© 2024 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

Quintana and Montes, 2014), LabSOCS (Suarez-Navarro et al., 2020´ ), MCNP (Maurotto et al., 2009), EFFTRAN (Vidmar et al., 2011), PENELOPE (Guerra J et al., 2018; Guerra J et al., 2015; Peyres and García-Torano, 2007˜ ) and DETEFF (Diaz and Vargas, 2010; Díaz and Vargas, 2008), are generally based on Monte Carlo code. One of the great advantages offered by the use of those software compared to experimental methodologies for the efficiency calibration is the possibility of obtaining _εc_ for a wide variety of geometries and types of matrices in much less time. This is because to obtain _εc_ in a simulated way, the preparation and experimental measurement of calibration standards are not necessary. In order to obtain the _FEPE_ in a simulated way using the software mentioned above, it is necessary to carry out a prior characterization of the gamma detector. 

Furthermore, using those software, it is also possible to transform _εc_ to _ε_ , for which various types of _εc_ corrections are usually used due to: 1. The geometric conditions for which the efficiency calibration is being carried out, 2. the differences in photon attenuation caused by differences in compositions and apparent densities between the calibration standard and problem sample, and 3. the true coincidence summing (TCS) effects present for various gamma emissions belonging to natural radionuclides, especially those corresponding to<sup>214</sup> Bi and<sup>208</sup> Tl (Gilmore and Hemingway, 1995; Tedjani et al., 2016; Venegas-Argumedo and Montero-Cabrera, 2015). 

Taking into account everything previously mentioned, the main objective of this study is to develop an efficiency calibration for uncharacterized Ge detectors by using Ge detectors characterized with analogous technology and geometry (that is, detectors of extended range (XtRa) type and coaxial in our case) for a wide variety of geometries and types of matrices, as well as for a wide range of energies, using LabSOCS in the case of the simulated _FEPEs_ (characterized detectors). Calibrating a Ge detector for many geometries is an expensive process, both in operator time and materials. To do this, given a specific geometry and a pair of detectors (characterized and un-characterized), we establish the hypothesis of the existence of a functional relationship between the _FEPEs_ of both detectors. To the best of our knowledge, this is the first study to carry out this type of efficiency calibration for uncharacterized gamma detectors, where this study has a great applicability worldwide for numerous laboratories dedicated to the measurement of environmental radioactivity. 

background and interference term, respectively, _ac_ and _mc_ are the activity concentration of each radionuclide and the mass in the case of the calibration standard, respectively, _t_ is the counting time and _Pγ_ is the gamma emission probability of each _Eγ_ , which were taken from DDEP, 2017. 

In the case of the _fa_ factor used in Eq. (2), the Cutshall model was applied in our case (Cutshall et al., 1983). In Eq. (2), _fg_ = 1 since _εc_<sup>_exp_and</sup> _ε_<sup>_exp_</sup> were obtained for the same detector (DET-3 in our case) and under the same geometrical conditions. In addition, it is important to clarify that the calculation of _ε_<sup>_exp_</sup> was carried out without including corrections due to TCS effects ( _fs_ ) since in the case of the _ε_<sup>_sim_</sup> , they were not included, where _fs_ = 1 for energies not affected by TCS effects. 

In the case of the _ε_<sup>_sim_</sup> calculations, the Geometry Composer software (version 4.4.1) from Mirion Industries was used (Canberra Industries, 2012), with the Beaker Editor option being employed to define the outline of each geometry used in this study. From this measurement geometry, the _FEPE_ was calculated as a function of energy, taking into account both the exact dimensions of the cylindrical containers and the chemical compositions of these containers, together with the selected experimental matrices. 

The methodologies used to obtain the _FEPEs_ through LabSOCS as well as through experimental methodologies have been developed by Barba-Lobo et al. (2023b) and Barba-Lobo et al. (2021a), respectively. 

Taking into account Eq. (1), the ratio of _FEPEs_ ( _FEPER_ ), _ε_<sup>_sim_</sup> / _ε_<sup>_exp_</sup> , for a specific energy, _Eγ_ , could be written as follows: 

where it has been assumed that _fg_<sup>_sim_</sup> _/fg_<sup>_exp_</sup> = _cte_ = _Cg_ for each geometry and _fa_<sup>_sim_</sup> = _fa_<sup>_exp_</sup> . This is possible if the measurements with the characterized and uncharacterized detectors are made under the same geometric conditions (same distance between geometry bottom and detector window). The second assumption is possible if the same sample is used, that is, the same apparent density ( _ρ_ ), thickness ( _h_ ) and chemical composition. Moreover, note that, in the case of corrections due to TCS effects, it is not possible to assume equality between _fs_<sup>_sim_</sup> and _fs_<sup>_exp_</sup> , since this correction type depends on the gamma detector used. 

In the case of energies that are not affected by TCS effects, it is possible to rewrite Eq. (3) as follows: 

#### **2. Methods and materials
#### _2.1. Method_ 

In the case of the _FEPE_ for any problem sample ( _ε_ ), the hypothesis that it can be factored can be established: 

where _εc_ is the _FEPE_ obtained in the calibration sample matrix, and _fg_ , _fa_ and _fs_ are the corrections due to geometric conditions, photon selfabsorption effects and true coincidence summing (TCS) effects, respectively. Thus, in Eq. (1) it is assumed that it is possible to carry out the factorization of the different corrections of _εc_ , which is a valid assumption as proven in previous works (Barba-Lobo and Bolívar, 2022). 

The _FEPE_ obtained for any problem sample using LabSOCS (characterized detectors) and through experimental methodologies (uncharacterized detectors) could be denoted as _ε_<sup>_sim_</sup> and _ε_<sup>_exp_</sup> , respectively. In the case of the _ε_<sup>_exp_</sup> determination with the same geometry, the following equation was employed: 

Taking into account Eq. (3) for the same energy, _ε_<sup>_sim_</sup> _/ε_<sup>_exp_</sup> would be independent of the problem sample selected for the measurement, as well as its thickness ( _h_ ) for the same geometry. Consequently, it is necessary to find the existing _ε_<sup>_sim_</sup> _/ε_<sup>_exp_</sup> relationship considering a great diversity of sample matrix types and geometries. 

Consequently, by Eqs. (3) and (4) it possible to observe that the _FEPER_ obtention for any problem sample with any thickness ( _h_ ) will not require any application of experimental self-absorption correction ( _fa_<sup>_exp_</sup> ), which is one of the several advantages offered by the methodology developed in this study. 

In the case of Eqs. (3) and (4), they have been shown in order to theoretically prove the initial hypothesis, which is experimentally demonstrate in Section 3. Thus, in the case of the _ε_<sup>_exp_</sup> calculation, it is possible to be carried out directly by the following simpler version of Eq. (2): 

where _a_ and _m_ are the activity concentration of each radionuclide and the mass, respectively, in the case of the problem sample. 

where _G_ , _B_ , _F_ and _I_ are the total number (gross) of counts for the fullenergy peak of interest whose centroid is _Eγ_ , Compton continuum, 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

#### _2.2. Materials_ 

Regarding the type of sample used in this study, a phosphate rock sample (code PR) was selected, composed mainly of fluorapatite (Ca5(PO4)3F) and with _ρ_ around 1.6 g cm<sup>−3</sup> , whose activity concentration of the radionuclides belonging to the<sup>238</sup> U series is 1569(26) Bq kg<sup>−1</sup> , with all radionuclides of the<sup>238</sup> U series in secular equilibrium, as expected for this type of sample (P´erez-Moreno et al., 2002). 

In addition, with regard to the validation of the methodology developed in this study, a certified reference material (CRM) (code RGU1) was used, provided by the IAEA (International Atomic Energy Agency), with a majority composition of SiO2, with _ρ_ about 1.6 g cm<sup>−3</sup> and a reference activity concentration of 4940(15) Bq kg<sup>−1</sup> for radionuclides belonging to the<sup>238</sup> U series (IAEA, 1987; IAEA, 2020). 

Moreover, in order to carry out the validation of the developed methodology, a non-certified sample (code Sn) was also employed which is a tin sample mainly formed by Sn (53%), O (24%), W (7%), Zr (5%), Fe (3%) and Co (3%), whose apparent density is about 3.5 g cm<sup>−3</sup> and reference activity concentration for the<sup>238</sup> U-series radionuclides is 4989(58) Bq kg<sup>−1</sup> (Barba-Lobo and Bolívar, 2022). 

For the methodology validation, another sample was employed, a phosphogypsum (code PG), which was employed for a proficiency test (CSN-CIEMAT, 2008), whose reference concentrations of<sup>238</sup> U,<sup>226</sup> Ra and<sup>210</sup> Pb (in Bq kg<sup>−1</sup> ) are 48.6(1.2), 634(13) and 781(15), respectively. The chemical composition of PG is mainly formed by H (2%), O (55%), S (18%), Ca (22%), Si (1%), Al (1%), P (0.5%) and F (0.5%), with _ρ_ around 1.3 g cm<sup>−3</sup> . CSN and CIEMAT are the acronyms for the Spanish Nuclear Safety Council (“Consejo de Seguridad Nuclear”) and the Centre for Energy, Environment and Technology Research (“Centro de Investigaciones Energ´eticas, Medioambientales y Tecnologicas´ ”), respectively. 

The different types of geometries used were cylindrical (C) and Marinelli (M) type. See Appendix A (Supplementary Material) for detailed information on the appearance and dimensions of each geometry, as well as the thicknesses used for each geometry. The code for each of them, as well as their respective external diameters ( _D_ ) and heights ( _H_ ), are specified below: 

#### _Cylindrical type_ 

**C72** : _D_ = 71.8 mm and _H_ = 83.9 mm; **C50:** _D_ = 50.3 mm and _H_ = 10.0 mm; **C36** : _D_ = 36.1 mm and _H_ = 65.1 mm; **C29** : _D_ = 29.0 mm and _H_ = 69.9 mm. 

#### _Marinelli type_ 

**M128** : _D_ = 127.6 mm and _H_ = 129.1 mm; **M121** : _D_ = 120.7 mm and _H_ = 118.1 mm. 

For both the cylindrical type (C) and the Marinelli type (M) geometries, _ε_<sup>_sim_</sup> _/ε_<sup>_exp_</sup> was obtained for the PR sample, varying the thickness of the sample ( _h_ ) and fixing the energy ( _Eγ_ ) at the following values corresponding to<sup>238</sup> U series radionuclides: 46 keV (<sup>210</sup> Pb), 63 keV (<sup>234</sup> Th), 186 keV (<sup>226</sup> Ra +<sup>235</sup> U), 295 keV (<sup>214</sup> Pb), 352 keV (<sup>214</sup> Pb), 609 keV (<sup>214</sup> Bi), 1120 keV (<sup>214</sup> Bi) and 1765 keV (<sup>214</sup> Bi), thus being able to cover a wide range of thicknesses and energies for each geometry. 

#### _2.3. Gamma detectors_ 

Regarding the gamma detectors used in this study, high purity germanium (HPGe) detectors are selected for both characterized and uncharacterized detectors provided by Mirion Industries. Three extended range (XtRa) detectors were employed, where the characterized ones have the codes DET-1 and DET-2, and DET-3 for the uncharacterized one, whose relative efficiencies with respect to a 3″x3″ NaI(Tl) detector at 1332 keV are 42.1% and 115.7%, and 38.4%, respectively. Regarding the electronic chain connected to each detector, these were of conventional type, using the Genie 2000 software (Canberra Industries, 

2004) for data acquisition and spectrum analysis for the three detectors. DET-3 is not characterized, but _εc_<sup>_exp_</sup> is known. 

The methodology was developed using the different geometries and energies previously mentioned in Section 2.2, selecting the PR sample in this case. Thus, the calculations of the _FEPE_ ratios ( _FEPER_ ), _ε_<sup>_sim_</sup> _/ε_<sup>_exp_</sup> were carried out for both couples of detectors, that is, DET-1 and DET-3, and DET-2 and DET-3, obtaining _FEPER1_ and _FEPER2_ , respectively. 

#### **3. Results and discussion
#### _3.1. Obtention of the FEPE ratios_ 

The _FEPERs_ were calculated using Eq. (3) for the geometries C72, C50, C36, C29, M128 and M121 in the case of the PR reference sample, varying the thickness ( _h_ ) and energy ( _Eγ_ ). Thus, 5 _h_ values were selected for each geometry, which are well distributed throughout each geometry, excepting for C50 geometry, for which only 1 _h_ value was selected due to its relatively low height. In the case of the M128 and M121 geometries, a _h_ value was selected just over the detector window and another _h_ value under the detector window (see Appendix A in Supplementary Material) in order to test the methodology validity for extreme geometric cases. 

As can be seen in Fig. 1 (on the left), the _FEPER1_ values obtained varying _h_ for C29 geometry were very similar from each other for each _Eγ_ in the case of the couple of detectors DET-1 – DET-3. The similar behavior of _FEPER1_ for all the _h_ values for each _Eγ_ can be explained by using Eq. (4). The average _FEPER1_ value were also shown for each energy in order to make easier the visualization of the similarity previously mentioned. Thus, by using Eq. (4), the ratio of _FEPERs_ for a specific energy and for two different thicknesses ( _h1_ and _h2_ ) would be written as 

_ε_<sup>_sim_</sup> _<u>c</u>_<sup><u>(</u></sup><sup>_h_2)</sup> _ε_<sup>_sim_</sup> _<u>c</u>_<sup><u>(</u></sup><sup>_h_1)</sup> _ε_<sup>_~~exp~~_</sup> _c_ ( _h_ 2)<sup>_~~/~~_</sup> _ε_<sup>_~~exp~~_</sup> _c_ ( _h_ 1)<sup>~~,~~that is, as the ratio of</sup><sup>_FEPERs_obtained in the calibration</sup> matrix. Therefore, the _εc_<sup>_exp_</sup> and _ε_<sup>_sim_</sup> _c_ curves versus _h_ must have a similar behavior making that the relative difference _ε_<sup>_exp_</sup> _c_<sup>(</sup><sup>_h_)and</sup><sup>_εsim_</sup> _c_<sup>(</sup><sup>_h_)be the</sup> same for each _h_ value. This explains why the behavior of _FEPER1_ is the same at each specific _Eγ_ regardless of the _h_ value selected. 

In addition, the _FEPER1_ values varying _Eγ_ are very similar from each other which is consistent due to DET-1 and DET-3 have very similar relative efficiencies (42.1% and 38.4%, respectively). Note that for 609 keV, 1120 keV and 1765 keV the _FEPER1_ values are some different from those obtained for the other _Eγ_ , which is due to the presence of true coincidence summing (TCS) effects for these three energies. In addition, note that for low energies (46 keV and 63 keV), the _FEPER1_ values are less than 1, while relative efficiency for DET-1 is higher than DET-3 one. This can be explained due to the self-absorption that occurs in the Ge detector itself, where the self-absorption in the Ge detector itself for the DET-1 must be higher than for the DET-3, causing the higher selfabsorption for low energies (Barba-Lobo et al., 2021b; Bonczyk, 2018 Długosz-Lisiecka and Ziomek, 2015) and, consequently, _FEPER1 <_ 1 for 46 keV and 63 keV. 

For the other couple of detectors, that is, DET-2 – DET-3, in the case of geometry C29 (Fig. 1 on the right), the _FEPER2_ have also similar values for each specific _Eγ_ regardless of the _h_ value selected, as previously occurred for _FEPER1_ . However, the _FEPER2_ values obtained varying _Eγ_ are very different from each other, unlike that occurs for _FEPER1_ . This is consistent since the relative efficiencies of DET-2 and DET-3 are very different from each other (115.7% and 38.4%, respectively), causing this dependence of the _FEPER2_ on _Eγ_ . 

Regarding the geometries C36, C50 and C72 (Figs. 2–4, respectively), the behavior of the _FEPER1_ and _FEPER2_ versus _Eγ_ for each _h_ value is very similar to that previously found and discussed for geometry C29. The obtained _FEPER1_ and _FEPER2_ values were very similar from each other for all the geometries, where _FEPER1_ and _FEPER2_ were ranged from about 0.9 (46 keV and 63 keV) to 1.2 (609 keV and 1120 keV), and from about 1.1 (46 keV and 63 keV) to 2.8 (609 keV and 1120 keV), respectively. Only for _FEPER2_ in the case of C50 geometry (Fig. 3 on the 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0004-02.png)

**Fig. 1.** _FEPE_ ratios ( _FEPER_ ) obtained at specific thicknesses ( _h_ ) varying the energy ( _Eγ_ ), using cylindrical geometry C29. The _FEPER_ ( _FEPER_ 1 (a) and _FEPER_ 2 (b)) were obtained comparing the _FEPEs_ simulated by LabSOCS for characterized detectors (DET-1 and DET-2, respectively) to the experimental _FEPEs_ obtained for a noncharacterized detector (DET-3). In the case of the average _FEPER_ (solid line), its uncertainty at 1 sigma level was also shown (dashed line). 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0004-04.png)

**Fig. 2.** _FEPE_ ratios ( _FEPER_ ) obtained at specific thicknesses ( _h_ ) varying the energy ( _Eγ_ ), using cylindrical geometry C36. The _FEPER_ ( _FEPER_ 1 (a) and _FEPER_ 2 (b)) were obtained comparing the _FEPEs_ simulated by LabSOCS for characterized detectors (DET-1 and DET-2, respectively) to the experimental _FEPEs_ obtained for a noncharacterized detector (DET-3). In the case of the average _FEPER_ (solid line), its uncertainty at 1 sigma level was also shown (dashed line). 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0004-06.png)

**Fig. 3.** _FEPE_ ratios ( _FEPER_ ) obtained at specific thicknesses ( _h_ = 7.29 mm) varying the energy ( _Eγ_ ), using cylindrical geometry C50. The _FEPER_ ( _FEPER_ 1 (a) and _FEPER_ 2 (b)) were obtained comparing the _FEPEs_ simulated by LabSOCS for characterized detectors (DET-1 and DET-2, respectively) to the experimental _FEPEs_ obtained for a non-characterized detector (DET-3). 

right), the _FEPER2_ range was somehow different from that found for the other 3 geometries, reaching a maximum _FEPER2_ value about 4 for C50 geometry. The fact that the obtained _FEPER1_ and _FEPER2_ values were very similar in general for the cylindrical geometries means that the constant _Cg_ related to the geometrical factor that was shown in Eq. (4) must have a similar value for these geometries regardless of the selected _h_ and _Eγ_ . 

Then, with respect to the geometries of Marinelli type, that is, M121 and M128, the _FEPER1_ and _FEPER2_ are shown in Figs. 5 and 6, respectively. Note that in the case of the M121, the _FEPER2_ was not calculated due to the M121 geometry was not possible to be used for DET-2 because of incompatibilities between their dimensions. 

For geometry M121, the _FEPER1_ behavior was similar to that found 

for the cylindrical geometries, excepting for the lowest thickness ( _h_ = 35.45 mm), for which it is possible to observe that the _FEPER1_ values deviated from the average when varying the energy. This is consistent since for this extreme geometrical case, _h_ is so low that it is very complicated that the gamma photons reach the detector in the same way than for the other thicknesses. Consequently, the _FEPER1_ values deviated from the average for _h_ = 35.45 mm, where the _FEPER1_ values were lower the average for low energies (46 keV and 63 keV), while for high energies ( _>_ 150 keV) the _FEPER1_ values were upper the average. This agrees well with the discussion previously provided for the cylindrical geometries in relation to the higher self-absorption for 46 keV and 63 keV in the case of the DET-1 window compared to the DET-3. 

Regarding the geometry M128, the _FEPER1_ followed the same 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0005-02.png)

**Fig. 4.** _FEPE_ ratios ( _FEPER_ ) obtained at specific thicknesses ( _h_ ) varying the energy ( _Eγ_ ), using cylindrical geometry C72. The _FEPER_ ( _FEPER_ 1 (a) and _FEPER_ 2 (b)) were obtained comparing the _FEPEs_ simulated by LabSOCS for characterized detectors (DET-1 and DET-2, respectively) to the experimental _FEPEs_ obtained for a noncharacterized detector (DET-3). In the case of the average _FEPER_ (solid line), its uncertainty at 1 sigma level was also shown (dashed line). 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0005-04.png)

**Fig. 5.** _FEPE_ ratios ( _FEPER_ ) obtained at specific thicknesses ( _h_ ) varying the energy ( _Eγ_ ), using Marinelli geometry M121. The _FEPER_ ( _FEPER_ 1) were obtained comparing the _FEPEs_ simulated by LabSOCS for characterized detectors (DET-1) to the experimental _FEPEs_ obtained for a non-characterized detector (DET-3). In the case of the average _FEPER_ (solid line), its uncertainty at 1 sigma level was also shown (dashed line). 

behavior than that obtained for geometry M121, where for the lowest thickness ( _h_ = 41.28 mm in this case), the _FEPER1_ values deviated again from the average in the same way than that occurred for M121, that is, the _FEPER1_ values were lower and upper the average for low and high energies, respectively. This agrees well with the explanation previously 

carried out for geometry M121. Furthermore, the _FEPER1_ values were similar to those obtained for geometry M121 as well as for the cylindrical geometries, ranging from about 0.8 (46 keV and 63 keV) to 1.2 (609 keV and 1120 keV) for geometry M128. Then, for the _FEPER2_ values obtained for geometry M128, they were also out of the average for _h_ = 41.28 mm. In addition, the _FEPER2_ behavior found for geometry M128 for the other _h_ values was very similar to that observed for the _FEPER2_ in the case of the cylindrical geometries. 

#### _3.2. Obtention of a general FEPER for each energy_ 

Due to the similarity found among the _FEPERs_ previously obtained in Section 3.1 varying the geometry and thickness, this Section is focused on finding a general _FEPER_ for each energy that can be used for any thickness and geometry. 

Firstly, in order to prove the similarity among the _FEPERs_ obtained for the different cylindrical and Marinelli geometries, the average _FEPERs_ values obtained over all the thicknesses for each geometry, _<FEPER_<sup>_j_</sup> _>_ , were divided between the average _FEPERs_ obtained in the case of the geometry C36, _<FEPER_<sup>_C36_</sup> _>_ . The geometry C36 was fixed in this case in order to make the comparison, obtaining _<FEPERj1 >_ / _<FEPER1C36>_ and _<FEPER2j >_ / _<FEPER2C36>_ for each couple of detectors, respectively (see Fig. 7). As can be seen in Fig. 7, the _<FEPERj1 >_ / _<FEPER1C36>_ values were statistically compatible with 1 for all the energies. Then, in the case of the _<FEPERj2 >_ / _<FEPER2C36>_ , the geometries C29, and C72 were more similar to the geometry C36 for all the energies, finding some differences between geometries C50 and C36, occurring the same between geometries M128 and C36. In addition, it is also possible to observe that the _<FEPER2C50>_ / _<FEPERC362 >_ and _<FEPER2M128>_ / _<FEPER2C36>_ values were very similar form each other for high energies, which agrees well with the _FEPER2_ ranges previously 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0005-11.png)

**Fig. 6.** _FEPE_ ratios ( _FEPER_ ) obtained at specific thicknesses ( _h_ ) varying the energy ( _Eγ_ ), using Marinelli geometry M128. The _FEPER_ ( _FEPER_ 1 (a) and _FEPER_ 2 (b)) were obtained comparing the _FEPEs_ simulated by LabSOCS for characterized detectors (DET-1 and DET-2, respectively) to the experimental _FEPEs_ obtained for a noncharacterized detector (DET-3). In the case of the average _FEPER_ (solid line), its uncertainty at 1 sigma level was also shown (dashed line). 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0006-02.png)

**Fig. 7.** Comparison between the average _FEPE_ ratios ( _<FEPER_ j1 _>_ (a), _<FEPER_ 2j _>_ (b)), obtained for each geometry (j) and the geometry C36 ( _<FEPERC361 >_ , _<FEPER2C36>_ ), varying the energy ( _Eγ_ ), where the average _FEPE_ ratios were calculated over all the thicknesses ( _h_ ) used for each geometry. In addition, the average _FEPE_ ratios were also obtained over all the geometries used for each couple of detectors ( _<FEPER1>_ (c) and _<FEPER2>_ (d), respectively) at each specific _Eγ_ , as well as their respective relative uncertainties ( _σr_ ( _<FEPER1>_ ) and _σr_ ( _<FEPER2>_ ), respectively), using an alphanumeric scale for the _Eγ_ in this case. Moreover, _<FEPER2>_ versus _<FEPER1>_ and their corresponding linear fit (e) were also shown. 

obtained in Section 3.1 for geometries C50 and M128. 

Then, after obtaining the average _FEPERs_ over all the thicknesses for each geometry, the _FEPERs_ were obtained, in turn, averaging over all the and geometries for each specific energy achieving _<FEPER1> <FEPER2>_ for each couple of detectors, respectively (see Fig. 7). Furthermore, in order to observe the deviation from the average _FEPER_ obtained for each energy, the relative standard deviation of the average ( _σr_ (%)) was also plotted for each energy. As can be seen in Fig. 7, the _σr_ values achieved for each energy were less than 7% for _<FEPER1>_ , which were between 1% and 3% for the great majority of the energies. In the case of the _σr_ values obtained for _<FEPER2>_ , they were ranged from 6% 

to 10%. Consequently, considering the _σr_ values obtained for _<FEPER1>_ and _<FEPER2>_ , it is possible to conclude that there is significant dependence of the _FEPERs_ on the geometry type. 

Furthermore, a relationship was also found between _<FEPER1>_ and _<FEPER2>_ as can also be seen in Fig. 7. Thus, this relationship was of linear type proving a constant behavior of _<FEPER2>_ / _<FEPER1>_ versus the energy, as well as making it possible to find a general _FEPER2_ function depending on _FEPER1_ . 

As can be seen in Fig. 7, there is certain dependence of the _FEPER_ on the energy due to the _Eγ_ values that are affected by TCS effects, that is, 609 keV, 1120 keV and 1765 keV, where the _ε_<sup>_exp_</sup> and _ε_<sup>_sim_</sup> obtained 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

experimentally and by LabSOCS, respectively, are not corrected by TCS effects. However, it is possible to correct the _ε_<sup>_exp_</sup> and _ε_<sup>_sim_</sup> by TCS effects at the same time by using the methodology developed by Barba-Lobo and Bolívar (2022). For this, the distance between the geometry bottom and the detector window ( _d_ ) was varied, selecting in this case _d_ values ranged from 25 mm to 65 mm. For the TCS corrections applying this methodology, it was employed the CRM with code RGU-1 for a fixed _h_ value of 25 mm and for geometry C36 since the _ε_<sup>_exp_</sup> values obtained by Barba-Lobo and Bolívar (2022) were calculated using these conditions. Thus, the _ε_<sup>_sim_</sup> were also calculated by LabSOCS for the same _d_ and _h_ values in the case of the RGU-1 using the detectors DET-1 and DET-2. 

As can be seen in Fig. 8, the _FEPER1(RGU-1)_ and _FEPER2(RGU-1)_ were plotted versus _d_ for each specific energy previously selected in Sections 3.1 and 3.2. Thus, the average _FEPER1(RGU-1)_ and _FEPER2(RGU-1)_ obtained over all the _d_ values were also plotted in Fig. 8 ( _<FEPER1(RGU-1)>_ and _<FEPER2(RGU-1)>_ , respectively), and they were shown together with the average _FEPER_ values obtained, in turn, over all the energies (solid lines in Fig. 8). Thus, it is possible to observe that _<FEPER1(RGU-1)>_ values were statistically compatible with the average value obtained over all the energies, excepting in the case of 186 keV. However, since 186 keV is an energy not affected by TCS effects, it is not relevant that _<FEPER1(RGU-1)>_ was not statistically compatible with the average. Then, in the case of the _<FEPER2(RGU1)>_ , it was possible to note that after applying the methodology developed by Barba-Lobo and Bolívar (2022) to correct TCS effects, the _<FEPER2(RGU-1) >_ continues having a dependence on _Eγ_ . Thus, in the 

case of the _FEPER2_ the dependence on _Eγ_ is related to the very significant differences between the relative efficiencies of detectors DET-2 and DET-3, as previously explained in Section 3.1. 

#### _3.3. Validation of the methodology developed for the FEPERs_ 

In Sections 3.1 and 3.2, for the methodology developed for the _FEPERs_ , a phosphate rock (PR) sample was selected. Thus, in this Section a CRM, non-CRM and a sample used for a proficiency test, whose codes are RGU-1, Sn and PG, respectively, were chosen to test this methodology, where the Sn sample was selected due to the very high difference of its chemical composition and apparent from those related to the RGU1 standard, allowing us to properly validate the developed methodology. For this, the geometries C36 and M128 were selected, because of the great differences between their characteristics, for the RGU-1 and Sn, and PG, respectively, according to the amount of sample available for each case. The _FEPERs_ for the RGU-1, Sn and PG samples were calculated for four, five and three thicknesses, respectively ( _h_ = 5 mm, 15 mm, 20 mm and 40 mm (for RGU-1), _h_ = 3 mm, 6 mm, 12 mm, 24 mm and 48 mm (for Sn sample) and _h_ = 41.25 mm, 86.1 mm and 122.1 mm (for PG)), and then an average _FEPER_ over all the _h_ values was found for each energy using both couples of detectors, obtaining _<FEPERC361 (RGU1)>_ and _<FEPER2C36(RGU-1)>_ , _<FEPERC361 (Sn)>_ and _<FEPER2C36(Sn)>_ , and _<FEPER1M128(PG)>_ and _<FEPER2M128(PG)>_ , respectively. The _<FEPER1C36(i)>_ and _<FEPERC362 (i)>_ were divided between _<FEPER1C36(RGU-1)>_ and _<FEPER2C36(RGU-1)>_ , respectively, for each 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0007-07.png)

**Fig. 8.** Obtention of the _FEPER_ values varying the distance between the detector window and the sample bottom ( _d_ ) for each specific energy ( _Eγ_ ), using the RGU-1 compacted at a fixed thickness ( _h_ = 25 mm) in the case of the geometry C36. These _FEPER_ calculations were carried out for both couples of detectors, that is, the characterized detectors (DET-1 and DET-2) with the non-characterized detector (DET-3), obtaining _FEPERC361 (RGU-1)_ (a) and _FEPER2C36(RGU-1)_ (b), respectively. Then, the average _FEPER_ values ( _<FEPERC361 (RGU-1)>_ (c) and _<FEPER2C36(RGU-1)>_ (d)) were obtained over all the _d_ values, which were plotted together the average _FEPER_ value obtained over all the _Eγ_ values. 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

energy selected, where _<FEPERC361 (i)>_ and _<FEPERC362 (i)>_ are the _FEPER1_ and _FEPER2_ obtained for the geometry C36 in the case of the samples _i_ ( _i_ = PR, Sn) averaging over the five thicknesses used for each sample in the case of each couple of detectors (see Sections 3.1 and 3.2 for the thicknesses employed for the PR sample and Section 3.3 in the case of the Sn sample). In the case of the _<FEPERM1281 (PG)>_ and _<FEPER2M128(PG)>_ , they were divided between _<FEPERM1281 (PR)>_ and _<FEPER2M128(PR)>_ , respectively, because the PR and PG were the two samples for which was possible to fill the M128 according to the amount of sample available. 

As can be seen in Fig. 9, the _<FEPERC361 (i)>_ / _<FEPERC361 (RGU-1)>_ and _<FEPER2C36(i)>_ / _<FEPERC362 (RGU-1)>_ as well as _<FEPER1M128(PG)>_ / _<FEPERM1281 (PR)>_ and _<FEPERM1282 (PG)>_ / _<FEPER2M128(PR)>_ were all of them statistically compatible with 1 for both samples ( _i_ = PR, Sn). This is consistent according to the hypothesis established in Section 2.1, where it was theoretically proven that when calculating the _FEPER_ (Eqs. (1), (3) and (4)), it was not dependent on the chemical composition or apparent density of the sample. Consequently, the _FEPER_ must be the same regardless of the selected sample since the self-absorption corrections are not needed. In addition, note that the _<FEPER1,2C36(i)>_ and _<FEPER1,2C36(RGU-1)>_ as well as _<FEPERM1281,2 (PG)>_ and _<FEPERM1281,2 (PR)>_ were calculated using different _h_ values, as previously mentioned, therefore, the non-dependence of the _FEPER_ on _h_ is also proven again. 

In order to further validate the methodology, the concentrations of radionuclides were calculated for the RGU-1, Sn and PG samples using the average _FEPERs_ obtained for PR sample (Section 3.2). Thus, average _FEPERs_ obtained for each energy, and given that the _ε_<sup>_sim_</sup> is known for each one of the three previous samples for each _h_ , it is possible to obtain the _ε_<sup>_exp_</sup> for each case using the relationship _FEPER_ = _ε_<sup>_sim_</sup> / _ε_<sup>_exp_</sup> , where _FEPER_ is the average _FEPER_ value obtained in Section 3.2 for each energy and geometry in the case of the PR sample. Thus, knowing the _ε_<sup>_exp_</sup> for each sample at each respective _h_ , it was possible to obtain the concentrations of radionuclides using Eq. (5). Then, the _zscore_ values were obtained comparing the calculated activity concentrations with the reference values for a proper statistical analysis of the methodology validation. As can be seen in Fig. 10, the _zscore_ values were generally less than 2 for each sample, geometry and energy, using both couples of detectors (DET-1 and DET-3 on the left, and DET-2 and DET-3 on the right), which further proves the good validation of the developed methodology. This also proves again the non-dependence of the _FEPER_ on the sample type and thickness since for the RGU-1, Sn and PG samples, the concentrations of radionuclides were calculated using the _FEPER_ obtained for the PR sample. In addition, note that the _zscore_ values were well distributed between the positive and negative panels demonstrating that there is no systematicity associated to the developed methodology. 

#### **4. Conclusions
This work has carried out a development of a novel and general efficiency calibration for uncharacterized gamma detectors by using characterized gamma detectors, based on the ratio of full-energy peak efficiencies ( _FEPER_ ) of characterized detectors ( _ε_<sup>_sim_</sup> , DET-1 and DET-2) and uncharacterized detectors ( _ε_<sup>_exp_</sup> , DET-3), where _ε_<sup>_sim_</sup> and _ε_<sup>_exp_</sup> were factorized into three correction factors: geometrical, photon selfabsorption and true coincidence effects (TCS). The developed methodology was applied to different cylindrical (C) and Marinelli (M) geometries using a rock phosphate (PR) sample, varying its thickness ( _h_ ) and for a wide range of energy ( _Eγ_ ). When applying the developed methodology, it is only necessary to carry out the experimental efficiency calibration of the uncharacterized Ge detector for a single sample, thickness and geometry, since the _FEPER_ was proven to be independent on sample type, thickness and geometry. 

The main conclusions of this work are the following: 

1. The _FEPER1_ and _FEPER2_ values obtained for C geometries were found to be independent on _h_ at each _Eγ_ , with values generally ranging from about 0.9 to 1.2, and from about 1.1 to 2.8, respectively. For M geometries, _FEPER1_ followed similar patterns, while for _FEPER2_ some differences were found but only at low energies ( _Eγ <_ 150 keV). 

2. An insignificant dependence of the _FEPERs_ on geometry type was found, where the relative standard deviations obtained for average _FEPER_ over all the C and M geometries at each _Eγ_ were all of them below 7% for _<FEPER1>_ and between 6% and 10% for _<FEPER2>_ . In addition, a linear relationship was found between _<FEPER1>_ and _<FEPER2>_ , allowing to obtain a general function for _<FEPER2>_ as a function of _<FEPER1>_ . 

3. After applying the corrections due to TCS effects varying the distance between the bottom geometry and detector window, _FEPER1_ was observed to be independent on _Eγ_ , while _FEPER2_ still shew a dependence on _Eγ._ 

4. The methodology was validated using a certified reference material (RGU-1), a non-certified reference material (Sn) and sample employed for a proficiency test (PG). The _FEPERs_ obtained using the RGU-1 were statistically compatible with those obtained in the case of the PR and Sn samples, analogously occurring between the PR and PG samples. In addition, the concentrations of radionuclides were calculated for the RGU-1, Sn and PG samples using the average _FEPERs_ obtained for the PR sample, obtaining _zscore_ values generally less than 2 for each sample, geometry and energy, using both couples of detectors. This supports the theoretical hypothesis established in this study about the _FEPER_ independence on sample composition or density, confirming the no need for corrections for self-absorption. Therefore, the robustness and validity of the method has been 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0008-11.png)

**Fig. 9.** Validation of the methodology developed in this study. The average _FEPER_ values obtained for the phosphate rock (PR) and the tin sample (Sn) were compared with those obtained for a certified reference material (RGU-1), where the geometry C36 was used. In the case of the sample employed for a proficiency test (PG), the comparison was carried out with respect to the phosphate rock (PR) using the geometry M128. This validation was carried out for both couples of detectors, that is, the characterized detectors (DET-1 and DET-2) with the non-characterized detector (DET-3), obtaining _<FEPERC361 (i)>_ / _<FEPERC361 (RGU-1)>_ ( _<FEPER1M128(PG)>_ / _<FEPER1M128(PR)>_ ) (a) and _<FEPER2C36(i)>_ / _<FEPER2C36(RGU-1)>_ ( _<FEPER2M128(PG)>_ / _<FEPER2M128(PR)>_ ) (b), respectively, where _i_ = PR, Sn. 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

![](images/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors/2024_A_new_methodology_for_efficiency_calibration_of_uncharacterized_Ge_detectors_by_using_characterized_Ge_detectors.pdf-0009-02.png)

**Fig. 10.** Validation of the methodology developed in this study. The concentrations of radionuclides present in the RGU-1, Sn and PG samples were calculated using the average _FEPER_ values obtained in the case of the PR sample for each geometry (C36 for RGU-1 and Sn, and M128 for PG). The _zscore_ values were obtained by using both couples of detectors (DET-1 and DET-3 (a), and DET-2 and DET-3 (b)). 

demonstrated for a wide range of thicknesses, geometries and energies using different samples. 

#### **CRediT authorship contribution statement A. Barba-Lobo:** Writing – review & editing, Writing – original draft, Validation, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. **V.M. Exposito-Su** ´ **arez:** ´ Methodology, Formal analysis, Data curation, Conceptualization. **J.A. Suarez-Navarro:** ´ Writing – review & editing, Writing – original draft, Validation, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. **J.P. Bolívar:** Writing – review & editing, Writing – original draft, Validation, Methodology, Investigation, Formal analysis, Data curation, Conceptualization. 

#### **Declaration of competing interest
The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

#### **Data availability
Data will be made available on request. 

#### **Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi. org/10.1016/j.radphyschem.2024.111763. 

#### **References
- Appleby, P.G., Oldfieldz, F., 1983. The assessment of<sup>210</sup> Pb data from sites with varying sediment accumulation rates. Hydrobiologia 103, 29–35. https://link.springer. com/article/10.1007/BF00028424. 

- Arce, P., Ignacio, J., Harkness, L., P´erez-Astudillo, D., Canadas, M., Rato, P., de ˜ Prado, M., Abreu, Y., de Lorenzo, G., Kolstein, M., Díaz, A., 2014. A framework to do Geant4 simulations in different physics fields with an user-friendly interface. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 735, 304–313. https://doi.org/10.1016/j.nima.2013.09.036. 

- Barba-Lobo, A., Bolívar, J.P., 2022. A practical and general methodology for efficiency calibration of coaxial Ge detectors. Measurement 197, 111295. https://doi.org/ 10.1016/j.measurement.2022.111295. 

- Barba-Lobo, A., Mosqueda, F., Bolívar, J.P., 2021a. An upgraded Lab-based method to determine natural γ-ray emitters in NORM samples by using Ge detectors. Measurement 186, 110153. https://doi.org/10.1016/j.measurement.2021.110153. 

- Barba-Lobo, A., Mosqueda, F., Bolívar, J.P., 2021b. A general function for determining mass attenuation coefficients to correct self-absorption effects in samples measured by gamma spectrometry. Radiat. Phys. Chem. 179, 109247 https://doi.org/ 10.1016/j.radphyschem.2020.109247. 

- Barba-Lobo, A., Gazquez, M.J., Bolívar, J.P., 2022. A practical procedure to determine ´ natural radionuclides in solid materials from mining. Minerals 12, 611. https://doi. org/10.3390/min12050611. 

- Barba-Lobo, A., Guti´errez-Alvarez, I., San Miguel, E.G., Bolívar, J.P., 2023a.<sup>´</sup> A methodology to determine<sup>212</sup> Pb,<sup>212</sup> Bi,<sup>214</sup> Pb and<sup>214</sup> Bi in atmospheric aerosols; Application to precisely obtain aerosol residence times and Rn-daughters’ equilibrium factors. J. Hazard Mater. 445, 130521 https://doi.org/10.1016/j. jhazmat.2022.130521. 

- Barba-Lobo, A., Exposito-Su´ arez, V.M., Su´ arez-Navarro, J.A., Bolívar, J.P., 2023b. ´ Robustness of LabSOCS calculating Ge detector efficiency for the measurement of radionuclides. Radiat. Phys. Chem. 205, 110734 https://doi.org/10.1016/j. radphyschem.2022.110734. 

- Baskaran, M., 2011. Po-210 and Pb-210 as atmospheric tracers and global atmospheric Pb-210 fallout: a Review. J. Environ. Radioact. 102, 500–513. https://doi.org/ 10.1016/j.jenvrad.2010.10.007. 

- Bonczyk, M., 2018. Determination of<sup>210</sup> Pb concentration in NORM waste – an application of the transmission method for self-attenuation corrections for gammaray spectrometry. Radiat. Phys. Chem. 148, 1–4. https://doi.org/10.1016/j. radphyschem.2018.02.011. 

- Canberra Industries, 2004. Genie 2000 Spectroscopy Software: Customization Tools, Printed in the United States of America. 

- Canberra Industries, 2012. Geometry Composer User’s Manual. Canberra Industries, Meriden. 

- Cutshall, H., Larsen, I.L., Olsen, C.R., 1983. Direct analysis of<sup>210</sup> Pb in sediment samples: self-absorption corrections. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 206, 309–312. https://doi.org/10.1016/0167-5087 

   - (83)91273-5. 

- DDEP, 2017. The decay data evaluation project. http://www.nucleide.org/DDE 

   - P_WG/DDEPdata.htm. 

- Díaz, N.C., Vargas, M.J., 2008. DETEFF: an improved Monte Carlo computer program for evaluating the efficiency in coaxial gamma-ray detectors. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 586 (2), 204–210. https:// doi.org/10.1016/j.nima.2007.11.072. 

- Diaz, N.C., Vargas, M.J., 2010. Improving the trade-off between simulation time and accuracy in efficiency calibrations with the code DETEFF. Appl. Radiat. Isot.: including data, instrumentation and methods for use in agriculture, industry and medicine 68 (7–8), 1413–1417. https://doi.org/10.1016/j.apradiso.2009.11.021. 

- Długosz-Lisiecka, M., Ziomek, M., 2015. Direct determination of radionuclides in building materials with self-absorption correction for the 63 and 186 keV γ-energy lines. J. Environ. Radioact. 150, 44–48. https://doi.org/10.1016/j. jenvrad.2015.07.018. 

- Dziri, S., Nourreddine, A., Sellam, A., Pape, A., Baussan, E., 2012. Simulation approach to coincidence summing in spectrometry. Appl. Radiat. Isot. 70 (7), 1141–1144. https://doi.org/10.1016/j.apradiso.2011.09.014. 

- Gilmore, G., Hemingway, J., 1995. Practical Gamma-Ray Spectrometry. John Wiley & Sons, Chichester. https://doi.org/10.1002/rcm.1290091227. 

- Guerra J, G., Rubiano J, G., Winter, G.G., Guerra, A., Alonso, H., Arnedo, M.A., Tejera, A., Gi, l J.M., Rodríguez, R., Martel, P., Bolívar, J.P., 2015. A simple methodology for characterization of germanium coaxial detectors by using Monte Carlo simulation and evolutionary algorithms. J. Environ. Radioact. 149, 8–18. https://doi.org/10.1016/j.jenvrad.2015.06.017. 

- Guerra J, G., Rubiano J, G., Winter, G.G., Guerra, A., Alonso, H., Arnedo, M.A., Tejera, A., Mosqueda, F., Martel, P., Bolívar, J.P., 2018. Automatic modeling using PENELOPE of two HPGe detectors used for measurement of environmental samples by γ-spectrometry from a few sets of experimental efficiencies. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 880, 67–74. https://doi.org/10.1016/j.nima.2017.10.076. 

- IAEA, 1987. Preparation of gamma-ray spectrometry reference materials RGU-1, RGTh-1 and RGK-1. Report-IAEA/RL/148, Vienna. https://nucleus.iaea.org/sites/Reference Materials/Shared%20Documents/ReferenceMaterials/Radionuclides/IAEA-RGTh 

-1/rl_148.pdf. 

- IAEA, 2020. Reference materials. https://nucleus.iaea.org/sites/ReferenceMaterials/ Pages/Index-for-Radionuclides.aspx. 

- Maurotto, A., Rizzo, S., Tomarchio, E., 2009. MCNP5 modelling of HPGe detectors for efficiency evaluation in γ-ray spectrometry. Radiat. Eff. Defect Solid 164 (5–6), 302–306. https://doi.org/10.1080/10420150902809189. 

_Radiation Physics and Chemistry 221 (2024) 111763_ 

_A. Barba-Lobo et al._ 

- P´erez-Moreno, J.P., San Miguel, E.G., Bolívar, J.P., Aguado, J.L., 2002. A comprehensive calibration method of Ge detectors for low-level gamma-spectrometry measurements. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 491, 152–162. https://doi.org/10.1016/S0168-9002(02)01165-8. 

- Peyres, V., García-Torano, E., 2007. Efficiency calibration of an extended-range Ge ˜ detector by a detailed Monte Carlo simulation. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 580 (1), 296–298. https://doi.org/ 10.1016/j.nima.2007.05.160. 

- Quintana, B., Montes, C., 2014. Summing-coincidence corrections with Geant4 in routine measurements by g spectrometry of environmental samples. Appl. Radiat. Isot. 87 (0), 390–393. https://doi.org/10.1016/j.apradiso.2013.11.067. 

Su´arez-Navarro, J.A., Moreno-Reyes, A.M., Gasco, C., Alonso, M.M., Puertas, F., 2020. ´ Gamma spectrometry and LabSOCS-calculated efficiency in the radiological 

characterisation of quadrangular and cubic specimens of hardened portland cement paste. Radiat. Phys. Chem. 171, 108709 https://doi.org/10.1016/j. radphyschem.2020.108709. 

- Tedjani, A., Mavon, C., Belafrites, A., Degrelle, D., Boumala, D., Rius, D., Groetz, J.E., 2016. Well GeHP detector calibration for environmental measurements using reference materials. Nucl. Instrum. Methods Phys. Res. Sect. A Accel. Spectrom. Detect. Assoc. Equip. 838, 12–17. https://doi.org/10.1016/j.nima.2016.09.022. 

- Venegas-Argumedo, Y., Montero-Cabrera, M.E., 2015. True coincidence summing corrections for an extended energy range HPGe detector. AIP Conf. Proc. 1671, 030004 https://doi.org/10.1063/1.4927193. 

- Vidmar, T., Kanisch, G., Vidmar, G., 2011. Calculation of true coincidence summing corrections for extended sources with EFFTRAN. Appl. Radiat. Isot. 69 (6), 908–911. https://doi.org/10.1016/j.apradiso.2011.02.042.
