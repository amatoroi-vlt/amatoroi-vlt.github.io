---
title: "remage: a Geant4-based simulation framework for low-background experiments"
authors: ["Toby Dixon", "Eric Esch", "Reyco Henning", "Manuel Huber", "Moritz Neuberger", "Luigi Pertoldi", "Zichen Wang"]
year: "2026"
source_pdf: "papers/raw/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf"
converted_at: "2026-11-02T10:01:05.330166"
abstract: "Monte Carlo simulations are an essential tool for data modeling and experimental design in low-background physics. These simulations typically demand a considerable effort, with each collaboration developing and maintaining its own complex Geant4 application. In this paper we present the design and validation of remage, which is an open-source framework designed to standardize these simulations and significantly reduce this effort. Its design separates the geometry, built with dedicated Python tools, from the compiled application. It provides a physics list and event generators tuned to radiogenic and cosmogenic backgrounds, output tailored to the most common detector types, and robust validation backed by modern software development practices. The software is distributed ready to use and scales efficiently with the computing resources that demanding simulations require. remage has been primarily developed for the LEGEND experiment, but is applicable to a wide variety of experiments."
---

Prepared for submission to JINST 

# **remage: a Geant4-based simulation framework for low-background experiments T. Dixon ,**<sup>_𝑎_</sup> **E. Esch ,**<sup>_𝑏_</sup> **R. Henning ,**<sup>_𝑑,𝑒_</sup> **M. Huber ,**<sup>_𝑐_</sup> **M. Neuberger ,**<sup>_𝑐_</sup> **L. Pertoldi** _𝑐,_ 1 **and Z. Wang** _𝑑_ 

_𝑎Department of Physics and Astronomy, University College London, London WC1E 6BT, United Kingdom 𝑏Department of Physics, University Tübingen, Tübingen 72076, Germany_ 

- _𝑐Department of Physics, TUM School of Natural Sciences, Technical University of Munich, 85748 Garching b. München, Germany_ 

- _𝑑Department of Physics and Astronomy, University of North Carolina, Chapel Hill, North Carolina 27599, USA_ 

- _𝑒Triangle Universities Nuclear Laboratory, Durham, NC 27708, USA_ 

_E-mail:_ luigi.pertoldi@tum.de 

Abstract: Monte Carlo simulations are an essential tool for data modeling and experimental design in low-background physics. These simulations typically demand a considerable effort, with each collaboration developing and maintaining its own complex Geant4 application. In this paper we present the design and validation of remage, which is an open-source framework designed to standardize these simulations and significantly reduce this effort. Its design separates the geometry, built with dedicated Python tools, from the compiled application. It provides a physics list and event generators tuned to radiogenic and cosmogenic backgrounds, output tailored to the most common detector types, and robust validation backed by modern software development practices. The software is distributed ready to use and scales efficiently with the computing resources that demanding simulations require. remage has been primarily developed for the LEGEND experiment, but is applicable to a wide variety of experiments. 

Keywords: Simulation methods and programs; Software architectures (event data models, frameworks and databases) 

ArXiv ePrint: 1234.56789 

1Corresponding author. 

## **Contents
|**1**|**Intr**|**oduction**|**2**|
|---|---|---|---|
|**2**|**Des**|**ign principles of the remage framework**|**3**|
|**3**|**Exp**|**erimental geometry**|**5**|
||3.1|Custom GDML extensions|5|
||3.2|Practical geometry construction in Python|6|
||3.3|Geometry checking and benchmarking|7|
|**4**|**Pri**|**mary event generation**|**7**|
||4.1|Vertex generators|8|
||4.2|Event generators|10|
|**5**|**Phy**|**sics list**|**11**|
|**6**|**Sim**|**ulation execution and parallelization**|**16**|
|**7**|**Out**|**put and data reduction**|**16**|
||7.1|Output schemes|18|
||7.2|Step clustering|20|
||7.3|Event filtering|22|
||7.4|Conditional tracking|22|
||7.5|Particle filtering|23|
||7.6|Processing the simulation output|24|
|**8**|**End**|**-to-end validation with a germanium detector and a radioactive source**|**24**|
|**9**|**Soft**|**ware development, documentation and distribution**|**25**|
|**10 **|**App**|**lications**|**26**|
|**11 **|**Sum**|**mary and outlook**|**27**|
|**A **|**A c**|**omplete simulation example**|**32**|

– 1 – 

## **1 Introduction
Monte Carlo simulations are a crucial tool in high-energy physics, both for predicting experimental outcomes and for planning new experiments. Geant4 is a state-of-the-art particle tracking toolkit for nuclear, leptonic and optical simulations [1–3], which are ubiquitous in experimental particle physics and other fields such as medical physics. For example, they are used in low-background physics experiments to simulate radioactive and cosmogenic (i.e., induced by cosmic radiation) background sources, for experimental design and data analysis (see for example [4–10]). 

Geant4 is a general toolkit supporting a vast range of uses. For a particular use case it is typically necessary to develop a dedicated Geant4 application. A significant amount of effort goes into the development of these programs. This includes the implementation of specific (often complex) experimental geometries, selection of appropriate physics processes, and implementation of routines to generate primary particles and store output information. Since Geant4 is based on C++, a low-level programming language with a large barrier to entry, this typically implies writing and maintaining large amounts of C++ code, which further increases the effort required. Finally, considerable validation is required to confirm that the application is appropriate for a certain use case, in particular the physics processes selected from such a general toolkit. The development of these Geant4 applications has historically been performed separately by each experiment or research group [5, 11–13], with sharing limited by the presence of sensitive information in these applications. 

remage is a Geant4-based framework designed to reduce the effort required to run Monte Carlo simulations for low-background physics experiments. Unlike most Geant4 applications of this kind, its design separates the definition of the experimental geometry from particle generation and tracking. remage is inspired by the MaGe [11] project, which enabled sharing of simulation routines between the Majorana Demonstrator and Gerda experiments. We generalize this approach to allow use by a wide range of low-background physics experiments, simplify the definition of experimental geometries, and employ modern software development practices. This approach also standardizes the selection of physics processes appropriate for low-background experiments, based on a dedicated sequence of validation routines that are fully integrated into the software design and run automatically. This specialization for low-background physics also covers the computational performance necessary to investigate rare background sources and flexible output structures. Other projects either target different applications, such as beamline simulations [14], or do not provide enough functionality for low-background physics experiments [15–17]. 

This paper describes the design and implementation of the remage framework. In section 2, we introduce the design principles of the framework. Sections 3 to 7 describe its main components: defining experimental geometries, generating initial particles, selecting appropriate physics processes, running the simulation, and storing and reducing the outputs. Sections 8 to 10 then cover the end-to-end validation of remage, the software development and the applications of the framework. Throughout, we describe remage v1.2.0 [18] used with Geant4 version 11.3.2, the most recent Geant4 version our validation suite had been run against at the time of writing. 

– 2 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0004-00.png)

<!-- Start of picture text -->
Python HDF5 C++ HDF5 Python HDF5<br>event<br>revertex vertices remage output reboost output analysis<br>Python<br>Python GDML software<br>legend- data<br>geometry<br>code pygeom- geometry useroptionalcode<br>tools<br><!-- End of picture text -->

**Figure 1** . The main remage simulation flow, with the typical processing steps and the interfaces between them. The core of the workflow is drawn with solid arrows: the remage application reads the experimental geometry as a GDML file and writes the simulation results in HDF5 format. Everything drawn with dashed lines is optional and lives outside the core application in the surrounding ecosystem of packages that produce inputs (revertex) or post-process the output (reboost). Since the interfaces are well-defined file formats, these components can be replaced by any other tool utilizing the same data exchange format. 

## **2 Design principles of the remage framework
remage is built on a design and structure that differs from most typical Geant4 applications. In this section we describe it, leaving the details of the individual components to the following sections. 

The guiding principle of this design is to limit the compiled application to the tasks that strictly depend on Geant4. We move everything else, for example geometry definition, into separate packages, which can be written in programming languages other than C++, such as Python. This modular approach minimizes the amount of C++ code that has to be written and maintained. remage is therefore both this core C++ application and, by extension, the whole framework it forms together with these packages. This modular approach means that remage does not contain any geometry code, which usually carries sensitive experiment-specific information, and can therefore be released as open-source software. The separation also allows the packages to be maintained independently of the main application. The general design of the resulting software, with its modular components and data exchange formats, is shown in figure 1. 

Building remage on wrappers that expose Geant4 from a higher-level language, such as the Python bindings [19] or Geant4.jl [20, 21] for Julia, would have been a legitimate alternative, but both target simple applications and are not yet mature enough for an advanced application like remage. 

Separating the C++ application from the surrounding packages depends on a clear interface between the individual components. We therefore define that interface in terms of the data exchanged across it, rather than in terms of code. The experimental geometry enters the application as a Geometry Description Markup Language (GDML) [22] file, and the simulation results leave it in one of several supported output formats. Among these, remage recommends its own Hierarchical Data Format version 5 (HDF5) [23] layout, following the LEGEND HDF5 specification [24], as the primary output format, since only this format exposes the framework’s most advanced output features, described in section 7. Optionally, input particle kinematics and positions (“event vertices”) can also be read by remage as HDF5 files (sections 4 and 4.1), which enables event generators to be written in languages other than C++. We stay as close to the plain formats as we can: remage reads 

– 3 – 

standard GDML, and the few additional constructs it relies on are documented precisely (section 3), as are the data structures it writes (section 7). These formats are language-agnostic, so every step before and after the tracking simulation can be implemented in whichever language suits it best, in our case usually Python or Julia. 

Within this boundary, the executable has to be flexible enough that users do not need to modify or rebuild it. Most of remage’s features are therefore exposed through a command line interface (section 6) and through a rich set of Geant4 messenger commands, which can be collected in macro files; listing 2 in section A shows such a macro file for a typical simulation setup. remage’s own commands are explicitly designed to keep these files simple, which reduces both the work of writing them and the risk of mistakes. Evaluating a different geometry version, physics scenario or set of output options becomes a matter of configuration rather than recompilation, which keeps the turnaround short and avoids duplicating large amounts of code when building upon an existing simulation setup. In particular, to support a broad range of low-background physics applications, the output format is strongly customizable, as described in section 7. 

Since most users interact with remage via Geant4 macro commands, we place a particular focus on documentation as a critical component of the software design; one important part of this is the automatic generation of documentation for all remage macro commands [25]. Needs that go beyond the available commands are still accommodated, since the application logic is also available as a library that users can extend with their own C++ code, as described in section 9. 

Users who do not have to modify the application should not have to compile it either, and we treat this as a deliberate design goal rather than an afterthought. We provide container images for the remage core and conda-forge [26] packages, so that even the compiled C++ application is available ready to use, and a full simulation can be installed and run without ever needing to set up a C++ build environment (section 9). The data exchange layer is in turn only as useful as the tools available to work with it. We therefore also maintain the packages that surround it: legend-pygeom-tools [27], built on pyg4ometry [28, 29], for writing geometries as Python code, revertex [30] for generating input vertices (section 4.1), legend-lh5io [31] for reading and writing the primary HDF5 output, and reboost [32] for post-processing the output (section 7.6). 

Validation of the simulation outputs and methods is essential for enabling robust and reliable results, and again we treat this as a critical component of the software design, backed by a dedicated set of software tests and validation routines. This encompasses tests of the individual algorithms, checks on physics processes (section 5) and full end-to-end validation by comparing to experimental data (section 8). We use GitHub continuous integration to run these tests and simulations automatically for every change to the remage software, and the results are then stored on a website as part of the remage documentation [33]. This means that the validation is naturally updated for every change in remage or Geant4, which is what makes it possible to adopt each new Geant4 version while keeping the physics output stable. It has already allowed us to uncover regressions in the upstream Geant4 project, which we reported to its developers [34, 35]. 

Low-background physics searches often require simulations with high statistics in order to study rare background sources. remage’s performance is therefore an important consideration for use on both personal computers and high-performance computing systems. In addition to the builtin Geant4 multi-threading, remage implements a custom multi-process parallelization mode to achieve consistent performance scaling on large machines; both parallelization modes are described 

– 4 – 

in section 6. Runtime and output volume can be reduced further through step limits (section 5), the clustering of Geant4 steps (section 7.2), and the choice of output fields (section 7.1). 

## **3 Experimental geometry
In Geant4 the detector construction is defined as a hierarchy of nested volumes, together with the materials they are made of and their physical properties. For a non-trivial experimental setup, this geometry definition is typically the largest part, by volume of code, of a Geant4 application, and also the part that changes most frequently as a detector design evolves. In a typical Geant4 setup, every such change requires a rebuild of the application. 

Alternatively, the geometry can be described in a dedicated text-based input format, such as Geant4’s own ASCII geometry description, used for example by GAMOS [15]. This removes the need to recompile, but it asks the user to learn a dedicated syntax, and such files are typically written by hand. 

As mentioned previously, remage avoids this by not implementing the geometry as C++ code at all: the volume tree is instead loaded at run time from a user-supplied GDML file, a widely used, application-independent XML-based file format that closely follows the geometry object model implemented by Geant4 [22, 36], and for which several other reading and writing software toolkits in different programming languages exist [28, 29, 37, 38]. The format can describe the experimental geometry and materials. In addition, it can specify the optical properties of the setup, meaning optical photons can be simulated (see section 5) without additional inputs. GDML files are typically written by a user’s geometry-writing application, and not by hand. GDML files, however, do not typically carry any information on which volumes are sensitive detectors, on how volumes should be drawn, or on whether and how Geant4 regions are defined. In the following we describe the custom extension that carries this information alongside the geometry (section 3.1), how both are most conveniently produced together in Python (section 3.2), and how the result can be checked and profiled before it is used (section 3.3). 

### **3.1 Custom GDML extensions
Closely related to the geometry definition is the assignment of detectors to volumes, i.e., to make them respond in a specific way to particles interacting inside them, and to store this information into output files. Throughout this paper we use “detector” for what Geant4 itself calls a sensitive volume, since this is the term remage itself uses. This assignment is mostly relevant for reading out the hits recorded in these volumes, and a complete description of how it shapes the simulation output is given in section 7; here we focus on how detectors are defined alongside the geometry. 

Detectors can be registered at run time through a macro command, which assigns a detector type and a user-defined unique identifier to a volume, used internally by remage and to label the detector in the output. For complex setups, which usually reuse the same large set of detectors across most of their simulation workflows, it is more convenient to store this assignment in the geometry file and to create it together with the geometry itself. Plain GDML cannot carry it, however, since detector logic is not part of the Geant4 geometry model that GDML describes. 

remage closes this gap with a custom extension that does not modify the GDML schema itself, but reuses Geant4’s own standard mechanism for including arbitrary auxiliary values in a 

– 5 – 

GDML file [36]. Files produced with this extension therefore remain valid, plain GDML, readable by any GDML-capable viewer or application, while carrying additional structures that remage understands. Detector assignment uses the RMG_detector and RMG_detector_meta auxiliary structures, which associate a physical volume with a detector type, a numeric unique identifier, and further optional metadata, e.g., 

**<userinfo > <auxiliary** auxtype= "RMG_detector " auxvalue= "germanium" **> <auxiliary** auxtype= "det_pv" auxvalue= "101" **/> </auxiliary > <auxiliary** auxtype= " RMG_detector_meta " auxvalue= "" **> <auxiliary** auxtype= "det_pv" auxvalue= ’{" manufacturer ": "D. Radford "}’ **/> </auxiliary > </userinfo >
defines the physical volume det_pv as a germanium-type detector with unique identifier 101, just as registering it at run time would. The RMG_detector_meta entry attaches optional, userdefined metadata, which can carry detector information that has no equivalent in Geant4’s own geometry model and can be read from the GDML file by other tools. 

This detector setup is not read from the GDML file automatically, but only on request through a dedicated macro command. Registration at run time with macro commands remains useful for volumes not authored that way, for interoperability with GDML files that lack this metadata, or for registering and overriding detectors at run time without touching the geometry file. 

A second structure, rmg_color, stores the RGBA color and transparency of a logical volume, read only by our visualization tools (section 3.2). A third structure, Region, encodes a grouping of logical volumes into a Geant4 region [39], together with associated production cuts and step, track, time or energy limits, in the format expected by Geant4’s own region-import mechanism; this structure can be written directly, and remage activates it automatically at run time when the geometry is loaded. 

### **3.2 Practical geometry construction in Python
In practice, both the geometry and its auxiliary metadata are most conveniently produced together in Python. To produce these GDML files, we rely on pyg4ometry [28, 29], a general-purpose, Geant4-independent Python geometry package. Its Python classes for constructive solids and logical and physical volumes closely mirror Geant4’s own C++ interface, so that users familiar with it can easily adapt their work; and it supports reading, writing and editing GDML files directly. Most features of the geometry model are supported: solids, volume structure, materials and optical material properties. pyg4ometry can also import CAD geometries, with tessellation, and ROOT geometries, converting both to GDML and making it straightforward to reuse existing engineering or detector models. It further includes a standalone, VTK-based [40] interactive visualization that runs without any Geant4 installation, useful for users who only want to inspect a geometry rather than simulate it. 

We extend pyg4ometry with our own package, legend-pygeom-tools [27], for the remagespecific parts of this workflow. Besides the detector-registration functionality described below, it provides a single function that commits all pending auxiliary metadata, detectors, colors and 

– 6 – 

regions, and writes the final GDML file. Before writing, a set of geometry sanity checks is run, covering registry consistency and common material definition mistakes, such as not registering all components with the pyg4ometry registry before writing the file. For visualization, it provides the standalone command-line viewer legend-pygeom-vis, which extends pyg4ometry’s VTK-based display with a configurable YAML “scene file” format, supporting camera presets, clipping planes, per-volume color overrides, overlay of points or events read from the HDF5 output, and offscreen export to PNG images. 

On the Python side, it is possible to attach to a physical volume object the information remage requires for detector registration. Listing 1 in section A shows the detector registration in a more complete workflow, together with attaching a visualization color, defining a Geant4 region, and iterating over the registered detectors before writing the final GDML file. 

See section 10 for an outlook on the existing Python packages that implement, on top of this ecosystem, the geometry of specific experimental setups. 

### **3.3 Geometry checking and benchmarking
remage provides three distinct mechanisms to validate and profile a geometry, addressing different needs and offering different levels of detail. By default, every GDML file loaded by remage is checked for volume overlaps using Geant4’s own sampled-point overlap test. This always-on check is a convenient first line of defense against basic geometry construction errors. 

A deeper, opt-in correctness check is available through the GeometryCheck output scheme (see section 7.1). Unlike the overlap check, this mechanism is based on geantinos: massless, chargeless, non-interacting Geant4 tracking particles used purely to probe navigation. remage fires geantino primaries through the geometry and verifies, at every step, that the pre- and post-step volume transitions reported by the navigator are consistent with the declared volume hierarchy. This catches subtler navigation bugs than a plain overlap test can, such as cases where volumes of the geometry are only overlapping through coincident surfaces, and not their bulk. 

remage also ships a standalone command-line tool, remage-geombench, for profiling the navigation performance of a geometry rather than its correctness, which is useful during geometry design to identify components that slow down navigation. Like the GeometryCheck scheme, it relies on geantinos, but shoots them from a regular three-dimensional grid of starting points laid out on three orthogonal sampling planes, and records the navigation wall-clock time at each grid point. The resulting per-point timing map highlights geometry regions where navigation is disproportionately slow, guiding further optimization before running full physics simulations. An example output for a sample geometry with multiple different volumes is shown in figure 2. 

## **4 Primary event generation
With the geometry defined by the user, the next key aspect of a Geant4 simulation is to define the primary particles and their initial state. Every simulated event starts from a primary vertex: the position and time at which one or more particles are created, together with each particle’s type and momentum. Producing all of these quantities is the task of what is generally referred to as an event generator. 

– 7 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0009-00.png)

<!-- Start of picture text -->
time per event [µs] time per event [µs]<br>10 15 20 10 1 10 2<br>80<br>40<br>60<br>20 40<br>20<br>0<br>0<br>−20 −20<br>−40<br>−40<br>−60<br>−40 −20 0 20 40 −75 −50 −25 0 25 50 75<br>x [mm] x [mm]<br>y [mm] z [mm]<br><!-- End of picture text -->

**Figure 2** . Output of remage-geombench (left panels) for a sample geometry (rendered in the rightmost panel), a LEGEND-1000 detector unit [41]. Each point of a map gives the wall-clock time Geant4 spends navigating a single geantino launched from that point through the geometry, for two orthogonal sampling planes. The first isolates the base plate below the germanium detector, a tessellated solid whose many facets make tracking slow; the second shows it alongside parts built from Geant4 native solids, where it still dominates the simulation time. 

In low-background experiments, the spatial distribution of primary vertices deserves particular attention of its own, since reproducing a radiogenic background correctly requires knowing not only what decays, but where, within the experimental setup, it occurs. remage reflects this by conceptually splitting the definition of an event’s initial state into two separate steps: spatial sampling, referred to as “vertex generation”, and the generation of the primary particle kinematics, referred to as “event generation”; these are configured independently of each other and are described separately in the following two subsections, with the caveat that some event generators produce the vertex position themselves. Geant4 ships with general-purpose primary generators, but these alone rarely cover the needs of a realistic experiment, in either of the two steps. remage therefore extends them, integrating a number of generators tailored to the needs of low-background experiments, some of which are based on sophisticated algorithms. 

### **4.1 Vertex generators
Low-background experiments typically need to account for several sources of potential radioactive backgrounds originating from their experimental setup, which are routinely quantified with Monte Carlo-based background models [4–6, 8]. Depending on the source of the radioactive contaminant, it will manifest itself either in the bulk of a material or only in a thin layer at its surface, for instance as a result of handling or machining during detector fabrication. remage provides dedicated vertex confinement modes that place primary vertices to reproduce where such contamination occurs, described in the following. By design, every simulated event has exactly one vertex, shared by all particles produced in that event. Note that some of the generators described in section 4.2 can also provide vertex positions on their own; in that case, no separate vertex confinement needs to be configured. 

– 8 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0010-00.png)

<!-- Start of picture text -->
intersection subtraction<br>union virtual cylinder virtual cylinder surface surface + depth profile<br>40<br>(a) (b) (c) (d) (e)<br>20<br>0<br>−20<br>−40<br>0 20 40 0 20 40 0 20 40 0 20 40 0 20 40<br>r  [mm] r  [mm] r  [mm] r  [mm] r  [mm]<br> [mm] z<br><!-- End of picture text -->

**Figure 3** . Some vertex confinement options provided by remage, illustrated with two germanium detectors in a medium. The figures show the radial component of the sampled vertices and thus exhibit a 1/ _𝑟_ dependence in the density. From left to right: (a) shows bulk sampling in both detectors (union). (b) samples from the intersection of the surrounding volume and a virtual, user-defined cylinder. In (c), this cylinder is rather subtracted from the surrounding volume. (d) and (e) show the surface samples, both without and with an additional depth distribution applied to the sampled vertices. 

The volumes to sample from can be either physical volumes already present in the Geant4 geometry or virtual, independently defined solids. Physical volumes are selected by name or, more generally, by regular expression; virtual solids, such as boxes, spheres or cylinders, are defined by the user through remage macro commands. Since a contamination normally affects all components of the same type, and these are usually named after a common scheme in the geometry, a single pattern such as det_holder_.* selects them all at once, keeping the macro file short and sparing the user the error-prone enumeration of hundreds of volume names. For some simple constructive solids (box, sphere, orb and tube) remage samples analytically; for any other Geant4 solid, it falls back to a generic rejection-sampling algorithm, using the solid’s bounding extent together with an inside/outside containment check. Sampling from the bulk of these volumes is the default; sampling on their surface can be selected instead and is described below. 

When several volumes are configured in this way, the method used to combine them can also be chosen from three modes. The default mode samples from the union of all of them, and is the natural choice when several detector components share the same contamination scenario, as shown in figure 3a. The other two combination modes handle cases where the contamination is only present in a subregion of a volume: sampling can be restricted to the intersection of the physical volumes with a user-defined virtual solid (figure 3b), or, conversely, one or more virtual solids can be excluded from the sampling region (figure 3c). 

By default, the vertex density is uniformly sampled across the sampling region regardless of how many volumes contribute to it. Two alternative weighting schemes are available for cases where the contaminant is not expected to scale with the geometric volume: the vertex density can instead be weighted by the volume mass, or by the mass contribution of one isotope. The latter is the natural choice when the simulated process is bound to the abundance of an isotope, for instance decays generated (section 4.2) in a set of volumes with different, known enrichment fractions. These mass-weighting schemes apply only to bulk sampling; surface sampling is always weighted 

– 9 – 

by surface area instead, and cannot be combined with them. 

For some simple constructive solids (box, sphere, orb and tube) remage also can sample vertices on the surface analytically. Surface sampling of arbitrary solids instead relies on an algorithm based on counting the intersection points of lines with the surface, as described in [42]. Unlike the description in that publication, remage directly implements this surface sampling algorithm without using a first simulation pass. Surface sampling is shown in figure 3d. 

Surface-sampled vertices can optionally be displaced inward into the material, to model subsurface contamination such as implanted or diffused activity, as introduced by machining of parts or surface treatments. A depth profile can be configured, choosing between an exponential, a uniform or a truncated Gaussian shape, with associated parameters; the sampled depth is then subtracted from the sampled surface point along the inward normal, as shown in figure 3e. The sampled depth of the displaced vertex is clamped to the distance to the opposite surface of the volume to avoid placing vertices outside of the volume. 

All the sampling algorithms described above are tested automatically by the remage validation suite, which verifies the distribution of the generated vertices both statistically and through visual checks. 

For scenarios not covered by these built-in options, remage can instead read event vertices from an external file; the specification of the input format and further implementation details are given in the remage documentation [25]. The Python package revertex [30] generates compatible files, covering both vertex positions and, as described in section 4.2, primary particle kinematics. One case the built-in sampling does not cover, but revertex does, is sampling of vertices on a specific surface of a volume only, e.g., on the differently processed surfaces of an high-purity germanium (HPGe) detector that are differently affected by some background components. 

### **4.2 Event generators
The simplest way to generate primary events in remage is to reuse Geant4’s own built-in generators, the general particle source or the more basic particle gun. Beyond these, remage directly includes the C++-based cosmogenic muon generator EcoMug for surface muon fluxes [43], and links against BxDecay0 [44], which provides both double- _𝛽_ decay and single-isotope background decay generators; both can be configured directly with macro commands. remage also supports reading input files generated by MUSUN, which samples cosmogenic muons from the distributions specific to underground laboratories [45]. These specialized generators are crucial for simulating cosmogenic backgrounds in both above-ground and underground experiments, as well as for the physics requirements of experiments searching for double- _𝛽_ decay. 

No set of generators can cover every case, so remage also accepts primary particle kinematics from an external file, produced by whichever tool or script suits the problem. This makes it possible, for example, to study exotic physics processes that no existing generator implements, without modifying the core remage application. The format is the same HDF5-based one already introduced for input vertices in section 4.1, with a table providing columns for the particle type as a PDG code [46], its kinetic energy, momentum direction and emission time. As for vertex files, the full format specification and further implementation details are given in the remage documentation [25]. 

– 10 – 

Vertex confinement and kinematics generation are two independent configuration choices in remage, and can be combined freely: BxDecay0 kinematics, for instance, can be distributed over an array of detector volumes to simulate double- _𝛽_ decay, or paired with vertices read from an external vertex-only file; conversely, a kinematics-only file can be combined with volume-based vertex confinement. A single, combined table carrying both position and kinematics columns together is also supported. Besides the vertex-generation routines described in section 4.1, revertex [30] also provides dedicated primary-kinematics generators, writing their output directly in the format remage reads back in. 

## **5 Physics list
Once the primary particles have been generated, the physical processes they can undergo, and the models used to simulate them, must be specified. In Geant4, the set of enabled physics processes and their parameters are bundled in a “physics list” [47]. remage provides a custom physics list tuned to the needs of low-background experiments, namely the simulation of radiogenic backgrounds in the energy range from keV to a few MeV, as well as cosmogenic backgrounds. It covers the electromagnetic interactions of _𝛾_ -rays and charged particles, radioactive decays and their chains, the hadronic processes induced by cosmic-ray muons and neutrons, and the production and propagation of scintillation and Cherenkov light. Its parameters are furthermore chosen to reach the precision required to model the response of solid-state and optical detectors. The list is close to the default physics list in upstream Geant4, and is mostly built from the physics building blocks (“physics constructors”) that Geant4 itself provides, with some notable changes. In terms of physics content it also closely resembles the list used by MaGe [11], which addressed the same class of experiments, although remage implements it independently and targets more recent Geant4 versions. 

The remage validation suite covers every part of this physics list, comparing important features of the simulated processes to experimental data, to theoretical calculations, or in some cases to other simulation frameworks. In the following we describe the physics list and, alongside it, show a selection of these checks. 

**Electromagnetic physics.** By default, electromagnetic interactions are simulated with the “Livermore” constructor (G4EmLivermorePhysics) [48, 49], which is one of the Geant4 electromagnetic options that are specifically also targeted at low-energy applications. Its models are built on evaluated atomic data libraries, describe _𝛾_ and electron interactions down to 100 eV, and account for atomic effects such as fluorescence and Doppler broadening. This low-energy treatment concerns _𝛾_ rays and electrons: positrons, muons and ions are described as in Geant4’s standard electromagnetic models. A macro command lets the user select one of the other electromagnetic constructors shipped with Geant4 instead of the Livermore constructor, among a fixed set of alternatives. Like most upstream physics lists, remage enables the simulation of electro-nuclear, muon-nuclear and gamma-nuclear interactions (G4EmExtraPhysics). 

**Decay physics.** Both the decays of unstable particles (G4DecayPhysics) and the radioactive decays of nuclei (G4RadioactiveDecayPhysics) are simulated by default. Geant4 does not simulate the decay of a nuclide whose lifetime, or whose sampled decay time, exceeds a configurable 

– 11 – 

threshold, effectively treating it as stable, and Geant4’s recent default value of one year is far too short for the long-lived members of the natural decay series. remage therefore raises the threshold to Geant4’s previous default value exceeding the age of the universe (10<sup>18</sup> s ≈ 3 _._ 17 × 10<sup>10</sup> yr), so that entire chains can be followed, and leaves it adjustable through a macro command. remage additionally enables the angular correlations between the _𝛾_ rays emitted in a de-excitation cascade, which Geant4 leaves switched off by default. Decays that Geant4’s own data cannot describe, double- _𝛽_ decay in particular, are instead handled by the dedicated generators discussed in section 4, such as BxDecay0. 

remage also implements a custom, optional process for inner bremsstrahlung that Geant4 does not model. Inner bremsstrahlung is the radiation emitted by the sudden acceleration of the electron as it is created in a _𝛽_ decay, rather than by its later scattering in matter [50]. Conversely, inner bremsstrahlung radiation can also be emitted during an electron capture decay, which is not implemented in remage. Currently this implementation is experimental and not enabled by default. 

**Production cuts and step limits.** Geant4 will generally track all created particles until they lose all their energy. Some processes may create many secondary particles with low energies, and tracking these would lead to excessive simulation time and output file size. Setting production cuts remediates this, as low-energy particles are not produced for tracking if they have less than a specified range left to travel, as determined by their kinetic energy [51]. The energy is instead locally deposited. This stops a large number of low-energy particles (e.g., low-energy bremsstrahlung photons) from increasing simulation time without significantly changing the simulation result. 

By default, the remage physics list uses a production cut of 0.1 mm for all particles, which is lower than the cuts in all upstream physics lists and corresponds to a production threshold of about 175 keV for electrons and 6 keV for gammas in germanium. This is necessary for high-precision modeling of signal generation in germanium detectors, as these are sensitive to the position of the ionizing interactions on this scale. This can be altered via remage macro commands or, for individual groups of volumes, through the region definitions carried by the geometry file itself (section 3.1). 

remage further allows a maximum step length to be imposed on the tracking of charged particles separately for each volume through a macro command. No step limit is set by default, in which case Geant4 derives the step length from the distance to the next volume boundary, the mean free path to the next interaction, and the multiple-scattering algorithm [52]. Forcing shorter steps samples the energy deposition along a track more finely, at a cost in computing time and output volume that grows steeply. This matters wherever the spatial distribution of the deposits is important, such as in the thin region at the surface of an HPGe detector where the charge collection efficiency is sensitive to the precise location. 

Production cuts and step limits can affect simulated observables, so the validation suite quantifies their effect, both to determine the defaults above and to guide users who choose their own. Because Geant4 always ends steps when reaching a geometrical boundary and also overrides the production cut for secondaries very close to boundaries, the energy deposit attributed to each volume is largely independent of the step length or production cut. Near the surface of a p-type HPGe detector, however, the charge collection efficiency follows a continuous profile that is applied to the energy depositions during post-processing (sections 7.6 and 8), and applying it correctly requires 

– 12 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0014-00.png)

<!-- Start of picture text -->
Bulk: energy in 1000 ± 1 keV Bulk events: simulation performance<br>450<br>96.0<br>CPU time<br>400<br>Wall-clock time<br>95.8<br>350 Output size<br>95.6<br>300<br>87.0<br>250<br>86.8 200<br>86.6 150<br>Total energy Active energy<br>100<br>86.4<br>50 100 150 200 No step 50 100 150 200 No step<br>limit limit<br>Maximum step length in germanium [µm] Maximum step length in germanium [µm]<br>Fraction of events [%]<br>Relative to no step limit [%]<br><!-- End of picture text -->

**Figure 4** . Effect of step limits on simulated observables, for 1 MeV electrons generated throughout the full volume of a p-type germanium detector of typical geometry. The left panel shows the fraction of events whose collected energy, obtained by weighting each energy deposition by a charge collection efficiency that rises linearly with depth over a thickness typical of the detector surface region, falls within 1000 ± 1 keV, as a function of the maximum step length imposed in germanium, with the dashed line and band marking the no-step-limit result. The fraction decreases as the step length is shortened, and the attribution of energy depositions to the differently sensitive parts of the germanium volume gets more precise. The right panel shows the associated computing cost: CPU time, wall-clock time and output file size, each relative to the no-step-limit case, all grow steeply as the step length is shortened. 

knowing where in this region each deposition occurred. Geant4 only reports the total energy deposited along a step, delimited by its start and end points, without resolving where along it the energy was released; remage by default assigns the deposit to the midpoint between the two. The step is in any case not the true trajectory of an electron, for example, since multiple scattering is modeled only approximately [52]. Because this region is not a boundary of the simulated geometry, Geant4 does not shorten steps there as it does when a track approaches one, and a shorter step length has to be imposed by the user. Figure 4 quantifies this for 1 MeV electrons generated throughout the full volume of a p-type germanium detector modeled with a cylindrical geometry, weighting each energy deposition by a charge collection efficiency that rises linearly with depth over a thickness typical of this region. Shortening the maximum step length from 200 to 10 _𝜇_ m lowers the fraction of events with the full collected energy by about 1%, while the CPU time and the output size grow substantially. These numbers are only an example, and the trade-off between accuracy and performance needs to be judged for each simulation goal. The impact of the step length depends on the simulated physics and on the detector geometry, and in particular on the charge collection efficiency profile assumed near the detector surface. 

**Hadronic physics.** Radiogenic background studies for low-background experiments usually require only electromagnetic physics. Hadronic physics becomes necessary for two further classes of background: the atmospheric muons that cross the detector, and neutrons, whether produced by those muons or released in the surrounding materials. Muons can induce a signal through their 

– 13 – 

own ionization, through the particle showers they generate, or through the time-delayed decays of the many radioactive isotopes those showers produce; the last two require hadronic interactions to be modeled, as does the transport of neutrons and their capture on the surrounding nuclei. 

In remage, hadronic physics is activated through a macro command, with which the user also selects among several constructors modeled after the hadronic parts of Geant4’s reference physics lists (QGSP_BIC_HP, QGSP_BERT_HP, FTFP_BERT_HP and Shielding). 

All of them are initialized together with Geant4’s Neutron-HP model, which treats neutrons below 20 MeV with evaluated cross-section data, both for inelastic and elastic scattering (G4Hadr onElasticPhysicsHP), and Geant4’s thermal neutron scattering can be enabled on top with an additional command (G4ThermalNeutrons). remage further simulates the capture of negatively charged particles coming to rest, muons among them (G4StoppingPhysics), and the inelastic nuclear interactions of light and heavy ions (G4IonPhysics). 

When isotopes are produced by neutron capture, a good model of the corresponding _𝛾_ cascade is needed. Geant4 provides two built-in statistical models for generating these _𝛾_ rays: G4Neu tronHPCapture, based on the G4NDL library, and G4PhotonEvaporation, based on levelscheme data from ENSDF. Neither is accurate enough to model the detector response with the precision a tagging strategy requires (see the discussion in [53]), so an alternative generator is required. remage therefore allows the default de-excitation to be overridden with _𝛾_ cascades read from external input files, specified by isotope and by range of incoming neutron kinetic energy. The file format is based on the output of MAURINA [54, 55], a Hauser-Feshbach generator that, unlike the two models above, also accounts for the initial spin distribution of the compound nucleus and for the level density and parity distribution during de-excitation. Keeping the cascades in separate files nevertheless makes the mechanism independent of the generator that produced them. Other generators, such as NuDEX [56], now part of Geant4, and G4RiversideCASCADE [53], are candidates for native support in future remage releases. 

Because the background from the decays of muon-induced isotopes must be well understood, both the simulated isotope production rate and any accompanying signal that would allow the production to be tagged need to be validated. Validation tests on muon physics consist of two parts. The first concerns the mean energy loss per unit of slant depth of muons in different materials and at different kinetic energies. The second considers the mean particle yield in hadronic showers, specifically, of neutrons and spallation isotopes, for different materials, at different muon kinetic energies, and different physics lists. Where available, the simulation estimates are compared to experimental values, but for all combinations tested, parameterizations based on experimental and simulation data are employed. In addition, FLUKA simulations [57–59] with the same setup were performed and are used as an additional reference. Due to the considerable uncertainties in both experimental and simulation estimates, deviations from these should be considered significant only when they are large. A selection of plots provided in the validation suite is shown in figure 5. The suite also covers the transport and capture of neutrons themselves, against evaluated nuclear data. 

**Optical physics.** Many low-background experiments also read out the light that energy depositions produce through scintillation or Cherenkov emission. To simulate the response of these channels as well, the physics list can be extended with a macro command that enables the tracking of optical photons and their interactions. This part follows the upstream Geant4 physics closely, adding the 

– 14 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0016-00.png)

<!-- Start of picture text -->
(G4.9.4, QGS-BiC, ENDF/B-VI) FLUKA 33<br>(G4.10.5, Shielding, G4NDL 4.5) remage 32<br>general parametrization 10 0 31<br>remage (G4.11.4, Shielding, G4NDL 4.7.1) 3 0<br>10 −2 FLUKA (4.5.1) 2 9<br>2 8<br>10 −1 36 38 40 42 44<br>N<br>10 −2<br>10 −3<br>10 − 3<br>10 1 10 2<br>⟨A⟩ of material<br>Z<br>Pb<br>G-S rock Xe<br>Scint OH2 Ar<br>isotope yield per muon<br>2neutron yield [n / )] / (g/cmμ<br>77Ge 69Ge 76Ga 75Ga 74Ga 72Ga 68Ga 71Zn 66Cu<br><!-- End of picture text -->

**Figure 5** . Selected hadronic physi <mark>cs</mark> cross-checks from the remage validation suite. The left plot shows the simulated muon-induced ne <mark>utron y</mark> ield for various materials used in low-background experiments with muons started at 280 GeV. <mark>It com</mark> pares remage with FLUKA, previous Geant4-based studies [10, 60] for precise comparison, a <mark>nd a</mark> general parameterization [61] as a rough estimate. The right plot compares simulated muon-indu <mark>ced</mark> isotope production in germanium enriched to about 92% in<sup>76</sup> Ge using remage and FLUKA, wit <mark>h mu</mark> ons starting at 100 GeV and identical geometry. The heat map in the inset shows the predicted F <mark>LUK</mark> A production rate and highlights the location of the selected isotopes in the nuclear chart. Differences in both plots compared to reference simulations can be due to systematic differences in models and potentially also to differences in the methodology used to estimate the observables. Therefore, only large deviations should be flagged. 

two emission processes above (G4Cerenkov and G4Scintillation) together with the optical boundary, bulk absorption and Rayleigh scattering processes (G4OpBoundaryProcess, G4OpAbs orption and G4OpRayleigh), as well as the wavelength-shifting (WLS) process in the modified form described below. The scintillation process is configured to distinguish the emission spectrum and yield of different particle types. Enabling these processes is not sufficient on its own, however. The optical properties of the individual detector materials must also be supplied by the user as part of the experimental geometry, as described in section 3. 

Once a WLS efficiency is assigned to a material, Geant4’s wavelength-shifting process (G4OpWLS) draws the number of shifted photons from a Poisson distribution. Even though this efficiency is below unity for the usual shifters, such as tetraphenyl butadiene, a single incident photon can still yield more than one shifted photon, and the total energy of the emitted photons is never compared against that of the incident one, so energy conservation is not guaranteed either. Neither behavior is appropriate for these materials. By default, remage therefore replaces this process with a custom one that emits at most one photon, performing a Bernoulli trial with the configured efficiency in place of the Poisson sampling. Geant4’s original process can be restored with a macro command. remage additionally opts in to sampling the emission time from an exponential profile rather than from Geant4’s default delta function. 

Optical physics is sensitive to physics or infrastructure changes, and the validation suite verifies the optical simulation microphysics. As an example, the validation suite checks whether the expected number of photons is generated in a scintillation or Cherenkov event, is absorbed after various lengths of absorbing materials, or is detected at a photo-sensor at the correct rate. 

– 15 – 

## **6 Simulation execution and parallelization
All user interaction with remage happens through a single command-line entry point, the remage executable. A typical invocation only needs to specify a detector geometry, a macro file describing the simulation to run, and an output file; for example: 

$ remage -g geometry.gdml -o output.lh5 [OPTIONS] macro.mac 

This basic invocation runs the simulation in a single process. Simulations for low-background physics, however, often have to generate very large numbers of events, since background sources frequently have a low probability of producing a detectable signal. Techniques that bias the simulation toward these rare paths are often challenging to apply, so scaling the simulation up to large computing clusters is usually the most direct way to keep it tractable. 

remage therefore offers two mutually exclusive ways of parallelizing a simulation run, selected with dedicated command-line flags: a threading mode and a multi-processing mode. The threading mode delegates directly to Geant4’s own native multi-threaded run manager. A single remage process spawns several worker threads that share the same memory space, so that objects common to the whole run, notably the geometry, are built only once regardless of how many threads are used. The multi-processing mode is instead implemented by remage itself, independently of Geant4. The executable launches several independent processes, each running its own complete, separate remage instance with its own private memory. 

In both modes, each worker thread or process writes its own output file, identified by a threador process-specific suffix; these partial files can optionally be merged back into a single file once the run completes. 

The two modes differ most importantly in the following respects. Because every process in multi-processing mode carries its own full, independent memory footprint, this mode is markedly more resource-hungry than the threading mode, where sharing the geometry and physics tables keeps the additional memory cost of each worker thread low. The two modes also scale differently with the number of parallel workers. Both scale linearly at first, though the threading mode usually with a lower slope, and both eventually saturate. In multi-processing mode this saturation sets in around the number of available physical CPU cores; in threading mode it is reached earlier. This behavior is shown quantitatively in figure 6, for two different sets of primary event setups in the same geometry. The source of this congestion in multi-threaded mode is not fully understood, and it also is dependent on the choice of simulation setup. 

Because the threading mode relies directly on Geant4’s own multi-threading implementation, this behavior reflects the Geant4 version used at the time of writing and may change as that implementation evolves. As a rule of thumb, the threading mode is the better choice when memory is the limiting resource, while the multi-processing mode gives better overall throughput otherwise. Both modes are also fully compatible with externally supplied primary events (sections 4 and 4.1). 

## **7 Output and data reduction
Users of simulation tools like remage need the outcome of the simulated particle interactions written to disk in a form suitable for further analysis: information about recorded interactions of interest in a detector must be captured in a structured form. remage stores this information in 

– 16 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0018-00.png)

<!-- Start of picture text -->
multithreaded multiprocessed ideal<br>e −  simulation γ simulation<br>2 8<br>2 6<br>2 4<br>2 2<br>2 0 128 physical cores<br>2 0 2 2 2 4 2 6 2 8 2 0 2 2 2 4 2 6 2 8<br>number of threads / processes m<br>event rate speedup factor<br><!-- End of picture text -->

**Figure 6** . The speedup factor for simulated event rates as a function of the number of parallel processes or threads. The setup used a geometry consisting of a germanium box in liquid argon, both registered as sensitive volumes. The left panel used primary electrons, and the right panel used gammas, both started with the general particle source (GPS) at 1 MeV without confinement. Each process or thread used the same number of primaries (testing weak scaling). Simulations ran on nodes with two AMD EPYC 7763 CPUs (128 physical cores) and saved output to flash storage with 204.8 GB/s bandwidth. In both cases, performance scaled linearly at first, then slowed or saturated. Multi-processing slowed down at around the number of physical cores due to entering the hyper-threaded regime. Multi-threading saturated earlier, and the saturation point depends on the setup and primary particle. 

table-like structures, arranged hierarchically within the output file much like a directory tree. What is written, and how it is organized, is governed by a set of configurable output schemes (section 7.1). 

remage’s primary output format is HDF5 [23], following the LEGEND HDF5 specification [24]; only this format exposes remage’s most advanced output features, described below. remage also supports all the other output formats provided by Geant4’s own G4AnalysisManager (plain HDF5, ROOT, CSV, and others), and the same set of formats is used for reading in primary particle information, as already discussed in sections 4 and 4.1. remage’s HDF5 output can be read straightforwardly with either the Python or Julia packages from the LEGEND software ecosystem [31, 62]. However, HDF5 is standardized and commonly used in many other scientific applications, so the files can additionally be used with any of the many other libraries capable of opening HDF5 files. These output files are also compressed with the Zstandard algorithm [63] to reduce disk space usage. 

What is written and in which format is only part of the picture. Depending on the physics processes and settings enabled, a simulation can record more detail than is actually needed, and can spend time tracking particles that never affect the result. remage offers measures against both, targeting the detailed microscopic simulation inside active detectors (section 7.2) and the simulation of particles that do not contribute to the final observables (sections 7.3 and 7.4). 

– 17 – 

### **7.1 Output schemes
The content and structure of remage’s output are determined by what we call “output schemes”: interchangeable components that implement event selection, the persistency of simulated quantities to disk, and, for some of them, control over which particles are tracked (Geant4’s “stacking action”). Schemes fall into two categories: those tied to a detector type and those global to the run. The former relate directly to the “detector” concept already introduced in section 3.1. Every detector has a type, one of Germanium, Scintillator, Optical or Calorimeter, and a unique identifier chosen by the user, either through a macro command or in the GDML file itself, as described in section 3.1. Registering any sensitive volume of a given type automatically activates the corresponding output scheme, which records only interactions occurring inside the registered volumes. The macro command selects volumes by regular expression and assigns identifiers that are either incremented automatically across the matched volumes or shared by all of them, so that a whole array of detectors can be registered in a single line. Volumes sharing an identifier are written to the same output table, and are thus essentially handled as one large detector volume. 

The observables stored per hit or event depend on the scheme, but typically include the interaction time, particle type, position and deposited energy. The number of quantities written out in a simulation not only affects the storage space required, but also strongly affects the overall runtime of the simulation. Encoding and storing output data to disk can take a substantial amount of simulation time; in some cases, the simulation performance can even be limited by the I/O throughput of the used storage device. While in the past (such as in the output classes implemented in MaGe) often most tracking information was written out for later post-processing, remage takes a different approach: it minimizes this amount by selecting only the minimum necessary set of quantities stored in the tabular output data. All output schemes tied to detector types try to restrict their output in this way, but often give users additional flexibility to selectively turn on other data columns if required for their analysis. This reduction complements the other strategies to minimize the amount of output data in remage that are described in subsequent sections. 

remage currently offers the following detector-specific output schemes: 

- Germanium: records step-wise, rather than summed, hit information, including the distance of each step from the detector surface; recommended for HPGe and other solid-state detectors, useful for offline pulse-shape and active-volume modeling. 

- Scintillator: follows the same step-wise philosophy as Germanium; recommended for scintillating or other bulk media, such as liquid argon, useful for offline optical-response modeling. 

- Optical: records the timestamp and wavelength of optical photons detected at the detector surface, terminating their tracks there; recommended for optical detectors like silicon photomultipliers (SiPMs) and photomultiplier tubes (PMTs). 

- Calorimeter: a minimal scheme that stores, for each Geant4 event, only the total deposited energy and the time of the first energy deposit, without any per-step detail; recommended for simple veto or absorber detectors. 

– 18 – 

The second category comprises three further schemes: Vertex, which records the primaryvertex information of every simulated event and is activated automatically whenever any other output scheme is active; Track, an optional scheme that stores the initial state of every simulated track; and GeometryCheck, already described in section 3, opt-in like Track but targeting geometry validation rather than detector output. 

The step-level detail recorded by the Germanium and Scintillator schemes lets downstream post-processing software, such as reboost [32] from the remage ecosystem, apply detector response models offline, without repeating the computationally expensive tracking simulation, a two-stage approach commonly adopted by experiments in the field [7, 64–66]. Such detail is required because the response of these detectors depends on where the energy was deposited and not only on how much: an HPGe detector is sensitive to the spatial topology of the depositions through the resulting pulse shape, while in a scintillating volume the probability that the emitted light reaches an optical detector varies with the position of the deposition. Where this level of detail is not needed, a volume can instead be registered as a Calorimeter. 

In an actual experiment, an event is defined as the set of signals falling within a time window set by the detector’s time resolution, and remage aims to reproduce this definition for simulated events. The Geant4 event index alone does not achieve this. A Geant4 event describing a full radioactive decay chain (section 5), for instance, can include energy depositions from a delayed daughter decay occurring long after those from the parent, well beyond the time window of any real detector, yet still attributed to the same Geant4 event. 

remage therefore introduces the concept of a “hit”: the set of steps recorded within a single detector that fall within a given time-coincidence window. A new hit begins whenever the underlying Geant4 event index changes, or whenever, within the same event, the recorded time jumps by more than the window size since the previous step. The window defaults to 10 _𝜇_ s, a value driven by the typical time resolution with which HPGe detectors separate two signals into distinct hits, and can be adjusted by the user where a different value is needed. As a result, one row of a remage output table does not necessarily correspond one-to-one with one simulated Geant4 event; in the decay-chain example above, remage splits the single Geant4 event into several separate hits. 

For the step-wise schemes, Germanium and Scintillator, the number of steps in a hit varies, so the columns holding step-level quantities are stored as variable-length arrays rather than as fixedwidth columns. This is the natural representation for data of this kind, and it simplifies the analysis, since all the steps belonging to a hit are already grouped together. Such variable-length columns are part of the LEGEND HDF5 specification [24] and are not available in the other supported formats. 

Two further features concern how the hits are distributed across tables. By default, each detector is written to its own output table, but the user can instead request a single, merged table per detector type, with the original detector volume labeled by the numeric detector ID. Since the default layout scatters the hits of a single event over several tables, remage also computes and stores in the output file a lookup table, the time-coincidence map (TCM), that lets downstream analysis reconstruct which rows in the different detector tables belong to the same time-coincident event, without having to scan every table. Figure 7 showcases the interplay of all described tables using the example of a germanium detector in argon. 

– 19 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0021-00.png)

<!-- Start of picture text -->
primaries and tracks one simulated event detector hits<br>/vtx one row per vertex /stp/det001 one row per hit<br>liquid argon, uid 1<br>evtid time xloc n_part … evtid t0 edep xloc …<br>⋮<br>⋮<br>value<br>HPGe,  /tcm one row per coincidence<br>per-step array uid 11<br>rows of this event table_key row_in_table<br>linked columns<br>reference primary vertex 11 1 2 3<br>γ track<br>/tracks one row per track e⁻ track ⋮<br>energy deposit<br>evtid trackid parent_trackid …<br>/stp/det011 one row per hit<br>evtid t0 trackid edep …<br>⋮<br>⋮<br>⋮<br><!-- End of picture text -->

**Figure 7** . Simplified sketch of remage’s output table structure in an HDF5 file. In this simple example, a _𝛾_ -ray is started in a liquid argon volume and deposits energy both in this scintillator volume and in a germanium detector. The /vtx and /particle tables contain information on the primary _𝛾_ -ray, e.g., its position, energy and momentum. Similar information is (optionally) also stored for all secondary tracks in the /tracks table. Actual detector energy depositions are stored in tables below /stp/ labeled by the unique detector ID number (uid). These are also reshaped in such a way that depositions close together in time are not stored in separate rows but in variable-length fields as a “hit”. Even in this simple two-detector setup, the information from this one Geant4 event is already scattered across two detector tables. To ease iterating over these for subsequent analysis, the time-coincidence map in /tcm stores references to the rows in the individual detector tables that fall into the same time window. 

### **7.2 Step clustering
The step-wise detail recorded by the Germanium and Scintillator schemes can substantially increase the output volume and the associated performance degradation due to high system I/O load. Often, however, Geant4 takes steps much shorter than what is meaningful in an HPGe or a scintillation detector, well below the experimental resolution. In germanium, for example, the charge clouds produced by interactions are typically 1–2 mm across, so the simulation is not sensitive to tracking at the micrometer level. remage therefore clusters steps that lie close together, reducing the output file size while retaining the information needed to compute the observables of interest. 

Clustering is restricted to steps within the same G4Track, so that each cluster remains interpretable as an effective step in the detector, combining the time, position and energy of its constituent steps, simply with a larger step length. The output format is unchanged: clustering reduces the number of rows written, not their meaning. One exception is made for very low-energy tracks: some Geant4 processes, such as atomic de-excitation, produce many secondary tracks with very low energy and range that are not expected to affect the observables of interest. Each such low-energy track is merged into the neighboring track with the highest energy among those whose 

– 20 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0022-00.png)

<!-- Start of picture text -->
(a) no clustering (b) with clustering<br>36 steps 8 steps<br>e −<br>γ (E0 > 100 keV)<br>γ (E0 < 100 keV)<br>area ∝ Edep<br>50 μm 50 μm<br><!-- End of picture text -->

**Figure 8** . Microscopic view of simulated steps in a germanium volume, after Compton scattering of a _𝛾_ -ray (bottom left). Without clustering (left panel), many small steps of the secondary electrons, as well as secondary, low-energy bremsstrahlung _𝛾_ s are visible. The post-step points of all particles’ steps are indicated with points whose area is proportional to the energy deposition in the step leading to this point. With clustering (remage’s default settings, right panel), these low-energy energy depositions are merged into fewer steps, each with a higher energy. The clustering preserves the location of the energy depositions. The number of secondary tracks or their particle type are not necessarily preserved. For example, the bremsstrahlung track is merged into one of the electron tracks. 

first pre-step point lies within the same distance threshold of its own first pre-step point. After this pre-processing step, remage walks through the steps of each track, joining a step to the current cluster whenever its distance from the cluster’s first step and its time difference from that step both stay below user-defined thresholds; this clustering time threshold is unrelated to the time-coincidence window used to define hits (section 7.1). Germanium detectors require finer treatment near their surface, where the charge collection efficiency varies steeply with depth, and spatial detail that is irrelevant in the bulk directly affects the modeled response there. A separate clustering distance threshold therefore applies to the surface region, and clusters are broken whenever a track crosses the boundary between the two regions. Figure 8 illustrates the effect of this clustering. 

Clustering is enabled by default and fully customizable through macro commands. The default thresholds are chosen to stay well below the resolution any real detector achieves, so that no physically useful information is discarded, while still removing a large fraction of Geant4 steps. For Germanium, steps are clustered when they lie within 50 _𝜇_ m and 10 _𝜇_ s of each other, and the merging of low-energy tracks described above applies below 10 keV. Within the 2 mm region closest to the detector surface, where an HPGe detector’s response is most position-sensitive, no clustering is applied. These defaults represent a deliberately minimal first pass at data reduction, leaving the choice of a more aggressive reduction, where needed, to the user. 

By reducing the number of step-wise rows written to the output tables, clustering lowers both the output file size and the associated I/O cost. Figure 9 shows the performance gains achieved by remage when step clustering is enabled. It is a simple simulation of 1 MeV electrons in the bulk of a germanium detector that is registered as a sensitive volume. Even small clustering thresholds (such as remage’s default) yield a significant reduction of the simulation’s CPU time and output size. Not shown is the further performance gain in the post-processing steps. With less data to process, 

– 21 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0023-00.png)

<!-- Start of picture text -->
Bulk events: simulation performance<br>100<br>No clustering CPU time<br>90 Wall-clock time<br>Output size<br>80<br>70<br>60<br>50<br>40<br>30 remage default (50  µ m)<br>0 200 400 600 800 1000<br>Cluster distance (bulk) [µm]<br>Relative to no clustering [%]<br><!-- End of picture text -->

**Figure 9** . Performance impact of step clustering, for a setup with 1 MeV electrons generated uniformly in the bulk of a germanium detector. Compared to the case without step clustering, both the CPU time spent and the output size are lowered significantly. 

both the hit-like reshaping (see section 7.1) and the users’ analysis code require fewer computing resources. This performance gain increases for larger clustering radii, so the radius needs to be chosen by looking at its impact on the simulated physics (not shown here). 

### **7.3 Event filtering
Event filtering decides, for each event, whether it is worth writing to disk; it acts purely at the output stage and leaves the simulation itself unaffected. It is useful whenever a large fraction of the simulated events could be irrelevant to the subsequent analysis. remage offers two criteria for this decision. The first is the energy deposited, available for Germanium and Scintillator detectors: the user sets upper and lower thresholds and selects which detectors participate, and the event is written only if the summed energy deposition across them falls within the bounds. This can be used to reproduce in the simulation the trigger energy threshold of the real experiment. The second is the production of a given isotope: a dedicated filtering scheme keeps only those events in which a specific isotope has been produced. This is useful, for instance, in simulations of rare neutron activation, where only a small fraction of the simulated events produce the isotope of interest. 

### **7.4 Conditional tracking
Simulating optical photons in Geant4 is computationally expensive, and a typical scintillating medium produces a large number of them in a single event. Reading out such a medium as a veto is a common experimental technique, and simulating it faithfully means tracking the scintillation light all the way to the optical detectors that collect it. In such a setup the decision on whether an event is worth keeping at all rests on a different detector. In LEGEND, for example, one of the triggering schemes is provided by the HPGe detectors, while the surrounding liquid argon is read out as a veto. If no energy is deposited in the germanium, the event is discarded regardless of what happens in the argon, so the effort spent tracking its optical photons is wasted. Conditional tracking exists 

– 22 – 

to avoid exactly this. The energy criterion that decides the fate of the deferred tracks is available only for Germanium detectors. 

Deferred tracks are not tracked immediately but stored for later. Optical photons are the natural candidates, as deferring them leaves the physics untouched; they cannot alter the energy deposition on which the later decision for tracking them is based. Electrons can be deferred as well, and optionally positrons under the same conditions; for them the user gives an energy threshold and a minimum distance from the Germanium detector surfaces, chosen so that the discard decision described above is not itself affected by the deferral. The distance matters because an electron need not reach a detector for its byproducts to do so, bremsstrahlung photons being one example, and these can deposit energy well away from where the electron itself stops. Depending on whether the conditions for further tracking are satisfied, the stored tracks are either tracked or dropped along with the rest of the event. The energy entering that decision is summed over all Germanium detectors, or over a user-chosen subset of them. The deferral acts at the moment a track is created; a companion mechanism, suspension, acts during tracking instead, halting an electron whose energy drops below a configured threshold and deferring it in the same way. 

Conditional tracking is not free of consequences for the physics. Deferring electrons is more delicate than deferring optical photons alone, since electrons can carry a significant fraction of the energy in an electromagnetic cascade. Part of an energy deposit may be carried by the deferred tracks themselves and therefore go uncounted when the discard decision is taken, so that the condition fails and the waiting tracks are dropped, and deferring high-energy shower components can likewise suppress isotope production. It should therefore be validated against the physics observables of interest before being relied upon. 

Beyond Geant4’s own staging mechanism, remage adds a custom deferral mechanism, because optical simulations can leave a vast number of waiting tracks that occupy considerable memory; it spills waiting tracks from memory to a scratch file, with negligible impact on processing speed, as validated with the remage validation suite. 

As an example, two deferral configurations were tested using the geometry from the speedup tests in figure 6, with 2.6 MeV gammas sampled 50 cm from the HPGe and a 100 keV minimum energy threshold in the HPGe. Deferring only the optical photons gave a 5× speedup, while deferring both optical photons and electrons more than 10 cm from the HPGe yielded a 170× speedup. The greater speedup is due to avoiding the overhead of placing optical photons on the waiting stack by deferring their parent electrons as well. 

### **7.5 Particle filtering
The particle filter follows a similar but more drastic approach: rather than deciding after the fact whether an event is worth writing to disk, it removes selected particles from the simulation, immediately after they are created and before they are tracked, with no regard for energy conservation. This differs from Geant4’s production cuts (section 5), which stop a particle only once its remaining range falls below a threshold and deposit its energy locally to conserve the event’s energy budget. 

This can reduce simulation effort by discarding particles with a short range produced far from any detector and therefore unable to contribute to the observables of interest, such as _𝛼_ particles from radioactive decay in a _𝛾_ -ray experiment, or serve to verify that a given particle species does not contribute to the output, by removing it and comparing the result. The user specifies which 

– 23 – 

particle species the filter targets, and can further restrict its action to chosen production processes, chosen production volumes, or both, in each case configuring the filter to keep only the matching particles or to remove only them. Because it breaks energy conservation, results obtained with the particle filter call for the same caution as any deliberately incomplete physical picture. 

### **7.6 Processing the simulation output
The remage output can be analyzed as it is, but an optional post-processing step allows the response of the detectors to be applied to it afterwards. reboost [32] implements this step as a collection of processors that act on the remage output, so that the same simulation can be reprocessed under different response models without repeating the tracking. Among them are the activeness model that weights each energy deposit by its distance from the detector surface, and a range of models for observables related to the shape of the detector signal, from simple heuristics based on the spatial spread of the energy deposits or on their drift time, to an analytic model of the current pulse and to libraries of simulated pulse shapes. Optical maps can also be applied, replacing the tracking of individual scintillation photons with a precomputed, position-dependent detection probability for each optical channel; reboost provides the routines to produce such maps from a dedicated optical simulation as well. Others reproduce the response of the readout, from the smearing of the energy with the detector resolution to the trigger and pile-up behavior of the data acquisition system. Another typical workflow for HPGe detectors is worth a mention: the simulated energy depositions are passed to a dedicated signal simulation tool, such as SolidStateDetectors.jl [67], and the language-agnostic HDF5 output makes this step seamless. 

## **8 End-to-end validation with a germanium detector and a radioactive source
The validation tests described so far are component-level: each isolates a single algorithm, physics process or generator and checks it against a theoretical expectation, a reference database or an independent calculation. To also test the full simulation chain against an actual measurement, we reuse one of the existing characterization runs [68] that the GERDA detectors underwent before deployment [69], performed at the HPGe detector characterization facility in the HADES underground laboratory [70]. In this 17-hour run, a BEGe detector was exposed to a<sup>228</sup> Th point source of about 6.3 kBq, placed on the detector symmetry axis 41 mm above the detector face. Quality cuts against pile-up and unphysical events retain about 84% of the recorded events. 

The corresponding simulation reproduces this setup, with the geometry built with legend-pygeom-hades [71], and the<sup>228</sup> Th decay chain generated with the Geant4 general particle source confined to the source volume, using remage’s default physics list and production cuts, without any tuning specific to this test. The resulting energy depositions are post-processed with reboost, applying a simple activeness model near the detector’s n<sup>+</sup> contact and a Gaussian energy resolution smearing to obtain a realistic-looking spectrum; the residual environmental radioactivity of the setup, measured in a separate run without the source, is rescaled to the live time of the characterization run and added to the simulated spectrum before the comparison. The simulated spectrum itself is scaled by the source activity, the live and dead time of the run, and the efficiency of the quality cuts. Figure 10 shows the resulting comparison, using a variable binning that is coarser around the _𝛾_ -lines so that the result is not sensitive to their detailed peak shape. 

– 24 – 

![](images/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments/2026_remage_a_Geant4_based_simulation_framework_for_low_background_experiments.pdf-0026-00.png)

<!-- Start of picture text -->
data<br>10 5 remage<br>10 4<br>10 3<br>10 2<br>10 1<br>5<br>0<br>−5<br>500 1000 1500 2000 2500 3000<br>energy [keV]<br>counts / keV<br>pulls<br><!-- End of picture text -->

**Figure 10** . Comparison of a germanium energy spectrum simulated with remage (red) to data (blue) taken by the GERDA collaboration at the HPGe detector characterization setup in HADES [70], following exposure to a<sup>228</sup> Th calibration source. The lower panel shows the residuals between data and simulation in units of standard deviations. 

Over most of the spectrum, above roughly 300 keV, the residuals between data and simulation stay within about 3 standard deviations, with a handful of points at lower energy showing larger deviations. Several sources of uncertainty are expected to contribute at this level, none of which concerns the particle transport itself: the simplified description of the detector geometry and of the surrounding materials, the knowledge of the source geometry and position, the uncertainty on the source activity and the approximate model of the detector active volume, whose effect is most pronounced at low energy. Given that the simulation uses remage’s default physics settings, with nothing tuned to reproduce this particular measurement, the level of reproduction achieved is good. 

## **9 Software development, documentation and distribution
remage is developed openly on GitHub [72] and released, like the surrounding ecosystem of Python packages, under the GPL-3.0 license. Development follows modern software engineering practices, centered on continuous integration and deployment (CI/CD). Every proposed change is automatically built and tested, and the resulting artifacts, from container images to documentation, are published automatically rather than assembled by hand at release time. Code formatting and static analysis, for both C++ and Python, are enforced automatically on every change. 

Continuous deployment extends to the user-facing documentation [25], which is rebuilt and published on every change to the repository. The macro command reference introduced in section 2 is generated automatically from the source code that defines the commands, so it cannot fall out of date. 

Making remage easy to install is treated as seriously as making it easy to use (section 2). Container images are published on Docker Hub [73]. remage is also packaged for conda-forge [26], for Linux and macOS for all common CPU architectures, and is therefore installable with conda [74] or Pixi [75]. The surrounding ecosystem of Python packages, including reboost, revertex, legend-lh5io and the legend-pygeom family of geometry packages, is available separately on 

– 25 – 

PyPI and conda-forge. Together, these channels cover the full simulation stack, from the compiled remage application to the surrounding Python tooling. Every release of remage and of the ecosystem packages is additionally archived on Zenodo, which assigns it a citable digital object identifier (DOI). 

For each remage release we recommend a specific Geant4 version, which is also the one our distributed binaries and container images are built against. We provide compatibility with new Geant4 releases as quickly as we can and test against them immediately, but the version we recommend is the one that has passed the validation suite. Since the validation simulations are far more demanding than the ordinary tests, this suite runs on a separate machine that we maintain ourselves, with considerably more computing power than the machines the CI service provides. 

The remage executable that users invoke is itself a thin Python wrapper around the compiled C++ application. It pre-processes the input, orchestrates the underlying C++ processes, which is what makes the multi-process parallelization mode of section 6 possible, and post-processes the output into the primary HDF5 format. The two sides communicate over Unix pipes, which also carry requests from C++ for Python to handle, such as validating the GDML input. Keeping this outer layer in Python lets us extend what remage can do without writing new C++ code. The few users whose needs go beyond the macro command interface can instead work from the other end: remage is also installed as a library, so they can link against it and plug in their own C++ components, reusing everything else. 

## **10 Applications
LEGEND is moving its entire simulation effort to remage, away from the previous MaGe toolkit. LEGEND-200 [76], which is already taking data, is simulated with remage from a geometry built in Python with the legend-pygeom packages [77]. This is a complete experimental geometry, and one in which the argon scintillation light also has to be produced and propagated, so it exercises parts of remage that a simpler setup does not. Nor is it a single, static description: it is designed to reproduce the multiple real configurations in which the experiment has run. LEGEND-1000 [78], the planned successor, uses the same software stack in the opposite mode [41]: since the experiment is not yet built, its geometry is instead driven by design parameters that are varied to compare options, supporting design studies rather than reproducing an installed configuration. Two components of this ecosystem are not specific to LEGEND and can be used in any experiment of this kind. legend-pygeom-hpges [79] simplifies the construction of HPGe detectors in the geometry, building the types in common use from a standardized set of geometrical measurements. legend-pygeom-optics [80] is a catalog of the optical properties of the materials these experiments use, together with the methods to attach them to a geometry or to override them, which removes most of the bookkeeping that these many tabulated quantities otherwise require; its documentation is generated automatically and plots every property together with the reference it comes from, so the catalog can also be browsed online [81]. 

A number of smaller test stands and _𝛾_ -ray spectroscopy setups, with considerably simpler geometries, also rely on remage. These include the LEGEND HPGe detector characterization facility at HADES [70], whose geometry package, legend-pygeom-hades [82], is also the basis for the end-to-end validation of section 8, and SCARF [83], a liquid argon cryostat at TUM hosting 

– 26 – 

HPGe detectors for LEGEND-related R&D, supported by the pygeom-scarf package [84]. remage has also been used for the GeMPI radiopurity screening facility at LNGS and for BUGS [85], the screening facility at the Boulby underground laboratory. 

## **11 Summary and outlook
This paper presented remage, a framework designed to address the recurring challenges of running Monte Carlo simulations for low-background physics experiments. Its architecture separates the experimental geometry, built and checked with dedicated Python tools, from the core Geant4 application. remage provides a physics list and event generators tuned to typical radiogenic and cosmogenic backgrounds, output schemes optimized for the most common detector types and analysis needs, and a validation suite that also quantifies the impact of key simulation settings on the observables of interest. It scales efficiently with the available computing resources, which keeps demanding simulations tractable, and further cuts computing cost directly through mechanisms such as step clustering, filtering and conditional tracking, which avoid spending effort on events or tracks that cannot affect the result. 

remage has become the simulation framework of the LEGEND experiment, and will therefore be developed and maintained for many years to come. Sustaining it is made easier by modern software development practices, such as continuous integration and deployment, automatically generated documentation, and fully open development, which also let its validation suite track new Geant4 releases while keeping the physics output stable. The feature set described here reflects remage’s state at the time of writing: development continues, the validation suite grows with it as new physics processes and detector types are covered, and the online documentation remains the authoritative, up-to-date reference. 

For these reasons, we argue that remage is a valuable resource, especially for small and medium-sized low-background experiments, since it already provides a high-quality, validated implementation of the features most of them need, without requiring each collaboration to develop and maintain its own. Through LEGEND and the several smaller, connected experimental efforts that already rely on it, remage is also a resource for the wider low-background physics community. 

## **Acknowledgments
remage is developed within, and primarily for, the LEGEND collaboration, and much of what is described in this paper reflects that context. We thank the collaboration for its continued support of the software. We would like to thank the GERDA collaboration for the HPGe characterization data used in the validation, and the pygama authors for the processing of those data [68]. We also thank the authors of legend-pygeom-hades [82] and reboost [32] for the geometry implementation of that setup and for the post-processing tools used there. 

This research is funded in part by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) – Excellence Cluster ORIGINS EXC 2094-390783311; SFB1258-283604770. We acknowledge the support of the German Federal Ministry of Research, Technology and Space (BMFTR) through grant numbers 05A2023 and 05A2026. This work has been supported by the Science and Technology Facilities Council (STFC), part of U.K. Research and Innovation (grant 

– 27 – 

number ST/W00058X/1). This research is supported by the U.S. Department of Energy, Office of Science, Office of Nuclear Physics under DE-FG02-97ER41041 and DE-FG02-97ER41033. This research used resources provided by the National Energy Research Scientific Computing Center (NERSC), a U.S. Department of Energy Office of Science User Facility at LBNL. 

Generative artificial intelligence (AI) tools were used at a later stage of the development of remage, once the software had already reached an advanced and largely mature state; the great majority of the codebase was written by the human authors. Such tools were also used to assist in editing this manuscript. 

## **Data and code availability
remage and all the ecosystem packages discussed in this work are openly developed on GitHub, in the legend-exp organization (https://github.com/legend-exp). Everything is released under the GPL-3.0 license. Every release of each package is archived on Zenodo and can be cited through its DOI [27, 86]; this paper describes remage v1.2.0 [18] and legend-pygeom-tools v0.7.1 [87]. Ready-to-use conda-forge packages and Docker Hub container images are described in section 9, and the user documentation is available online [25]. 

## **References
- [1] GEANT4 collaboration, _GEANT4 - A Simulation Toolkit_ , _Nucl. Instrum. Meth. A_ **506** (2003) 250. 

- [2] J. Allison et al., _Geant4 developments and applications_ , _IEEE Trans. Nucl. Sci._ **53** (2006) 270. 

- [3] J. Allison et al., _Recent developments in Geant4_ , _Nucl. Instrum. Meth. A_ **835** (2016) 186. 

- [4] GERDA collaboration, _Modeling of GERDA Phase II data_ , _JHEP_ **03** (2020) 139. 

- [5] CUORE collaboration, _Data-driven background model for the CUORE experiment_ , _Phys. Rev. D_ **110** (2024) 052003. 

- [6] LZ collaboration, _Background determination for the LUX-ZEPLIN dark matter experiment_ , _Phys. Rev. D_ **108** (2023) 012010. 

- [7] GERDA collaboration, _Liquid argon light collection and veto modeling in GERDA Phase II_ , _Eur. Phys. J. C_ **83** (2023) 319. 

- [8] Majorana collaboration, _Assay-based background projection for the Majorana Demonstrator using Monte Carlo uncertainty propagation_ , _Phys. Rev. C_ **110** (2024) 055804. 

- [9] C. Wiesinger, L. Pandola et al., _Virtual depth by active background suppression: Revisiting the cosmic muon induced background of GERDA Phase II_ , _Eur. Phys. J. C_ **78** (2018) 597. 

- [10] V. Pěč, V.A. Kudryavtsev et al., _Muon-induced background in a next-generation dark matter experiment based on liquid xenon_ , _Eur. Phys. J. C_ **84** (2024) 481. 

- [11] M. Boswell et al., _MaGe — a Geant4-based Monte Carlo Application Framework for Low-background Germanium Experiments_ , _IEEE Trans. Nucl. Sci._ **58** (2011) 1212. 

- [12] Z. She et al., _SAGE: a Monte Carlo simulation framework for experiments with germanium detectors_ , _JINST_ **16** (2021) T09005. 

- [13] G. Angloher et al., _ImpCresst – A versatile simulation tool focusing on solid-state detectors at keV energies_ , 2603.01770. 

– 28 – 

- [14] L.J. Nevay et al., _BDSIM: An accelerator tracking code with particle–matter interactions_ , _Comput. Phys. Commun._ **252** (2020) 107200. 

- [15] P. Arce et al., _Gamos: A framework to do Geant4 simulations in different physics fields with an user-friendly interface_ , _Nucl. Instrum. Meth. A_ **735** (2014) 304. 

- [16] J. Liu, _GEARS – A Fully Run-Time Configurable Geant4 Application_ , 2512.09246. 

- [17] J. Detwiler, “g4simple: a simple Geant4 simulation suite.” https://github.com/legend-exp/g4simple. 

- [18] L. Pertoldi, M. Huber et al., _remage v1.2.0_ , Oct., 2026. 10.5281/zenodo.23391506. 

- [19] Geant4 Collaboration, “Geant4 Book for Application Developers: Language Bindings.” https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/ LanguageBindings/languageBindings.html. 

- [20] JuliaHEP, “Geant4.jl: Julia bindings to the Geant4 simulation toolkit.” https://github.com/JuliaHEP/Geant4.jl. 

- [21] G.A. Stewart et al., _Julia in HEP_ , _EPJ Web Conf._ **337** (2025) 01266. 

- [22] R. Chytracek, J. McCormick et al., _Geometry description markup language for physics simulation and analysis applications_ , _IEEE Trans. Nucl. Sci._ **53** (2006) 2892. 

- [23] The HDF Group, _Hierarchical Data Format, version 5_ , 2025. 10.5281/zenodo.17808614. 

- [24] LEGEND collaboration, _LEGEND Data Format Specifications: HDF5 file format_ , 2020. https://legend-exp.github.io/legend-data-format-specs/dev/hdf5/. 

- [25] “remage documentation.” https://remage.readthedocs.io. 

- [26] conda-forge community, _The conda-forge Project: Community-based Software Distribution Built on the conda Package Format and Ecosystem_ , 2015. 10.5281/zenodo.4774216. 

- [27] L. Pertoldi, M. Huber et al., _legend-pygeom-tools_ , Aug., 2026. 10.5281/zenodo.15094869. 

- [28] S. Boogert, A. Abramov et al., _Pyg4ometry: A Python library for the creation of Monte Carlo radiation transport physical geometries_ , _Comput. Phys. Commun._ **272** (2022) 108228. 

- [29] S. Boogert, A. Abramov et al., _pyg4ometry_ , Feb., 2025. 10.5281/zenodo.14926560. 

- [30] L. Pertoldi, T. Dixon et al., _revertex_ , Nov., 2025. 10.5281/zenodo.20798501. 

- [31] J. Detwiler, L. Pertoldi et al., _legend-lh5io_ , Feb., 2026. 10.5281/zenodo.18700604. 

- [32] L. Pertoldi, T. Dixon et al., _reboost_ , Mar., 2025. 10.5281/zenodo.15094776. 

- [33] “remage validation suite.” https://legend-exp.github.io/remage/validation/latest. 

- [34] E. Esch and M. Huber, “Neutron capture cross-section issues using Shielding in G4.11.4.” Geant4 Bugzilla, bug report 2759, 2026. https://bugzilla-geant4.kek.jp/show_bug.cgi?id=2759. 

- [35] M. Huber, “v11.4 also produces scintillation photons for energy deposited by photons.” Geant4 Bugzilla, bug report 2750, 2026. https://bugzilla-geant4.kek.jp/show_bug.cgi?id=2750. 

- [36] “GDML User’s Guide, Version 3.0.” https://gdml.web.cern.ch/GDML/doc/GDMLmanual.pdf. 

- [37] R. Brun and F. Rademakers, _ROOT — An object oriented data analysis framework_ , _Nucl. Instrum. Meth. A_ **389** (1997) 81. 

- [38] K. Sloan, M. Hindi et al., _KeithSloan/GDML: the FreeCAD GDML workbench_ , 2020. 10.5281/zenodo.3787318. 

– 29 – 

- [39] Geant4 Collaboration, “Geant4 Book for Application Developers: Cuts per Region.” https://geant4-userdoc.web.cern.ch/UsersGuides/ForApplicationDeveloper/html/ TrackingAndPhysics/cutsPerRegion.html. 

- [40] W. Schroeder, K. Martin et al., _The Visualization Toolkit_ , Kitware, 4 ed. (2006). 

- [41] L. Pertoldi, M. Huber et al., _legend-pygeom-l1000_ , Aug., 2026. 10.5281/zenodo.22030739. 

- [42] J.A. Detwiler, R. Henning et al., _A Generic Surface Sampler for Monte Carlo Simulations_ , _IEEE Trans. Nucl. Sci._ **55** (2008) 2329. 

- [43] D. Pagano, G. Bonomi et al., _EcoMug: An Efficient COsmic MUon Generator for cosmic-ray muon applications_ , _Nucl. Instrum. Meth. A_ **1014** (2021) 165732. 

- [44] V. Tretyak and F. Mauger, “BxDecay0: C++ port of the legacy Decay0 FORTRAN library.” https://github.com/BxCppDev/bxdecay0. 

- [45] V.A. Kudryavtsev, _Muon simulation codes MUSIC and MUSUN for underground physics_ , _Comput. Phys. Commun._ **180** (2009) 339. 

- [46] Particle Data Group collaboration, _Review of particle physics_ , _Phys. Rev. D_ **110** (2024) 030001. 

- [47] Geant4 Collaboration, “Geant4 Guide for Physics Lists.” https: //geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/index.html. 

- [48] Geant4 Collaboration, “Geant4 Guide for Physics Lists: EM constructors, Liv.” https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsListGuide/html/ electromagnetic/Liv.html. 

- [49] Geant4 Collaboration, “Geant4 Physics Reference Manual: Low Energy Livermore Model.” https://geant4-userdoc.web.cern.ch/UsersGuides/PhysicsReferenceManual/html/ electromagnetic/introduction/livermore.html. 

- [50] L. Hayen, N. Severijns et al., _High precision analytical description of the allowed 𝛽 spectrum shape_ , _Rev. Mod. Phys._ **90** (2018) 015008. 

- [51] Geant4 Collaboration, “Geant4 Book for Application Developers: Production Threshold versus Tracking Cut.” https://geant4-userdoc.web.cern.ch/UsersGuides/ ForApplicationDeveloper/html/TrackingAndPhysics/thresholdVScut.html. 

- [52] V.N. Ivanchenko, O. Kadri et al., _Geant4 models for simulation of multiple scattering_ , _J. Phys. Conf. Ser._ **219** (2010) 032045. 

- [53] L. Weimer, E. Ellingwood et al., _G4RiversideCASCADE: A data-driven implementation of_ ( _𝑛, 𝛾_ ) _cascades in Geant4_ , _Nucl. Instrum. Meth. A_ (2026) 171940. 

- [54] P. Grabmayr, _Cross sections and gamma cascades in_<sup>77</sup> _Ge needed for background reduction in_ 0 _𝜈𝛽𝛽 experiments on_<sup>76</sup> _Ge_ , _Eur. Phys. J. A_ **60** (2024) 115. 

- [55] P. Grabmayr, _Gamma cascades in gadolinium isotopes_ , _Eur. Phys. J. C_ **83** (2023) 444. 

- [56] E. Mendoza, V. Alcayne et al., _Neutron capture measurements with high efficiency detectors and the Pulse Height Weighting Technique_ , _Nucl. Instrum. Meth. A_ **1047** (2023) 167894. 

- [57] C. Ahdida et al., _New Capabilities of the FLUKA Multi-Purpose Code_ , _Front. in Phys._ **9** (2022) 788253. 

- [58] G. Battistoni et al., _Overview of the FLUKA code_ , _Annals Nucl. Energy_ **82** (2015) 10. 

- [59] “FLUKA website.” https://fluka.cern. 

– 30 – 

- [60] K.V. Manukovsky, O.G. Ryazhskaya et al., _Neutron production by cosmic-ray muons in various materials_ , _Phys. Atom. Nucl._ **79** (2016) 631. 

- [61] N.Y. Agafonova and A.S. Malgin, _Universal formula for the muon-induced neutron yield_ , _Phys. Rev. D_ **87** (2013) 113013. 

- [62] O. Schulz et al., _LegendHDF5IO.jl_ , Nov., 2018. https://github.com/legend-exp/LegendHDF5IO.jl. 

- [63] Y. Collet and M.S. Kucherawy, “Zstandard Compression and the ’application/zstd’ Media Type.” RFC 8878, Feb., 2021. 10.17487/RFC8878. 

- [64] M. Agostini, C.A. Ur et al., _Signal modeling of high-purity Ge detectors with a small read-out electrode and application to neutrinoless double beta decay search in Ge-76_ , _JINST_ **6** (2011) P03005. 

- [65] M. Carrettoni and M. Vignati, _Signal and noise simulation of CUORE bolometric detectors_ , _JINST_ **6** (2011) P08007. 

- [66] LZ collaboration, _Simulations of Events for the LUX-ZEPLIN (LZ) Dark Matter Experiment_ , _Astropart. Phys._ **125** (2021) 102480. 

- [67] I. Abt, F. Fischer et al., _Simulation of semiconductor detectors in 3D with SolidStateDetectors.jl_ , _JINST_ **16** (2021) P08007 [2104.00109]. 

- [68] M. Agostini et al., _Germanium energy spectra from a_<sup>228</sup> _Th source measurement at HADES_ , 2026. 10.5281/zenodo.22799602. 

- [69] GERDA collaboration, _Characterization of 30_<sup>76</sup> _Ge enriched Broad Energy Ge detectors for GERDA Phase II_ , _Eur. Phys. J. C_ **79** (2019) 978. 

- [70] E. Andreotti et al., _HEROICA: an Underground Facility for the Fast Screening of Germanium Detectors_ , _JINST_ **8** (2013) P06012. 

- [71] L. Pertoldi, T. Dixon et al., _legend-pygeom-hades v0.2.1_ , Aug., 2026. 10.5281/zenodo.22029997. 

- [72] “remage source code repository.” https://github.com/legend-exp/remage. 

- [73] “Docker Hub.” https://hub.docker.com. 

- [74] Anaconda, Inc., “conda: package, dependency and environment management for any language.” https://docs.conda.io. 

- [75] prefix.dev, “pixi: package management made easy.” https://pixi.sh. 

- [76] LEGEND collaboration, _First Results on the Search for Lepton Number Violating Neutrinoless Double-𝛽 Decay with the LEGEND-200 Experiment_ , _Phys. Rev. Lett._ **136** (2026) 022701. 

- [77] M. Huber, L. Pertoldi et al., _legend-pygeom-l200_ , June, 2024. 10.5281/zenodo.16778749. 

- [78] LEGEND collaboration, _The Large Enriched Germanium Experiment for Neutrinoless 𝛽𝛽 Decay: LEGEND-1000 Preconceptual Design Report_ , 2107.11462. 

- [79] L. Pertoldi, N.N.P.N. Lay et al., _legend-pygeom-hpges_ , May, 2024. 10.5281/zenodo.11115664. 

- [80] L. Pertoldi, M. Huber et al., _legend-pygeom-optics_ , May, 2024. 10.5281/zenodo.11115646. 

- [81] “legend-pygeom-optics documentation: optical properties reference.” https://legend-pygeom-optics.readthedocs.io/en/stable/api/pygeomoptics.html. 

- [82] L. Pertoldi, T. Dixon et al., _legend-pygeom-hades_ , Aug., 2026. 10.5281/zenodo.22029996. 

- [83] M. Schwarz, C. Vogl et al.,<sup>42</sup> _Ar production and injection to a liquid argon environment for background mitigation studies_ , _Nucl. Instrum. Meth. A_ **1087** (2026) 171434. 

– 31 – 

- [84] T. Dixon, L. Pertoldi et al., _pygeom-scarf_ , Aug., 2026. 10.5281/zenodo.22030137. 

- [85] P.R. Scovell et al., _Low Background Gamma Spectroscopy at the Boulby Underground Laboratory_ , _Astropart. Phys._ **97** (2018) 160. 

- [86] L. Pertoldi, M. Huber et al., _remage_ , May, 2024. 10.5281/zenodo.11115662. 

- [87] L. Pertoldi, M. Huber et al., _legend-pygeom-tools v0.7.1_ , Aug., 2026. 10.5281/zenodo.21907048. 

## **A A complete simulation example
The two listings below make up a minimal but complete remage setup. Listing 1 builds the experimental geometry in Python and writes it to a GDML file, following the workflow of section 3. Listing 2 is the macro file that runs the simulation on that geometry, registering the detectors, confining the event vertices and selecting the event kinematics. 

Listing 1. Registering a detector with legend-pygeom-tools, attaching visualization and region metadata, and inspecting the registered detectors before writing the final GDML file. 

- 1 **import** pint 2 **from** pygeomtools **import** Region, RemageDetectorInfo, write_pygeom 

- 3 **from** pygeomtools.detectors **import** walk_detectors 

- 4 

- 5 u = pint.get_application_registry() 

- 7 _# reg, det_pv and det_lv are, respectively, a pyg4ometry.geant4.Registry_ 

- 8 _# and the physical and logical volume of the detector to register,_ 

- 9 _# produced by the pyg4ometry geometry-building code (omitted here)_ 

- 11 _# mark the detector physical volume as a germanium detector for remage_ 12 det_pv.set_pygeom_active_detector( 13 RemageDetectorInfo("germanium", 101, {"manufacturer": "Mirion"}) 14 ) 

- 15 _# ...and change its appearance_ 

- 16 det_lv.pygeom_color_rgba = (0.6, 0.6, 0.6, 1) _# for visualization_ 17 

- 18 _# define a custom region that contains the detector volume and set a_ 

- 19 _# custom production cut for it_ 

- 20 region = Region("det_region") 21 region.add_volume(det_lv) 22 region.set_cuts(0.2 * u.mm) _# production cuts_ 23 region.add_to_gdml(reg) 

- 25 _# inspect the detectors previously defined in the Python code_ 

- 26 **for** pv, det **in** walk_detectors(reg): 

- 27 **print** (pv.name, det.detector_type, det.uid) 

- 29 _# commit everything to a GDML file internally. This runs sanity checks to_ 

- 30 _# catch common geometry mistakes_ 31 write_pygeom(reg, "geometry.gdml") 

– 32 – 

Listing 2. Example remage macro that illustrates a typical simulation setup with registered detectors, vertex confinement and the selection of event kinematics. The geometry file is assumed to be set as a command-line option and is thus not spelled out in this listing. 

- 1 _# register a single physical volume as a Germanium-type detector with identifier 101_ 

- 2 /RMG/Geometry/RegisterDetector Germanium hpge_01 101 

- 3 _# register all matched volumes individually, with id starting from 200_ 

- 4 /RMG/Geometry/RegisterDetector Optical sipm_.* 200 

- 5 _# register all matching volumes into one single detector (with id 300)_ 

- 6 /RMG/Geometry/RegisterDetector Calorimeter calo_segment_.* 300 .* true 

- 7 

- 8 _# discard event if energy in detectors is < 100 keV_ 

- 9 /RMG/Output/Germanium/EdepCutLow 100 keV 

- 10 /RMG/Output/Germanium/AddDetectorForEdepThreshold 101 _# select detector(s) by id_ 

- 11 

- 12 /run/initialize 

- 13 

- 14 _# confine event vertices in a cylindrical sub-region of the "liquid_argon" volume_ 

- 15 /RMG/Generator/Confine Volume 

- 16 /RMG/Generator/Confinement/Physical/AddVolume liquid_argon 

- 17 /RMG/Generator/Confinement/SamplingMode IntersectPhysicalWithGeometrical 

- 18 /RMG/Generator/Confinement/Geometrical/AddSolid Cylinder 

- 19 /RMG/Generator/Confinement/Geometrical/CenterPositionZ 0 m 

- 20 /RMG/Generator/Confinement/Geometrical/Cylinder/InnerRadius 0 m 

- 21 /RMG/Generator/Confinement/Geometrical/Cylinder/OuterRadius 3 cm 

- 22 /RMG/Generator/Confinement/Geometrical/Cylinder/Height 5 cm 

- 23 

- 24 _# alternative 1: generate event kinematics with a built-in Geant4 generator_ 

- 25 /RMG/Generator/Select GPS 

- 26 /gps/particle e- 

- 27 /gps/energy 2.039 MeV 

- 28 /gps/ang/type iso 

- 29 

- 30 _# alternative 2: remage generator_ 

- 31 /RMG/Generator/Select BxDecay0 

- 32 /RMG/Generator/BxDecay0/DoubleBetaDecay Ge76 2vbb 

- 33 

- 34 _# run the simulation_ 

- 35 /run/beamOn 1000 

– 33 –
