# OpenSCAD for Web-Based Parametric Model Generation in AI-Supported Industrial Design

*A concise research report supporting an introductory dissertation chapter.*

## 1. What OpenSCAD is

OpenSCAD is a free, open-source, script-file-based 3D CAD environment aimed at producing solid geometry rather than artistic surfaces [^1]. Its official positioning is as "the programmers' solid 3D CAD modeller": the designer writes a `.scad` source file in a small, dedicated language, and the program compiles that description into a solid model [^2]. The default execution path is graphical (an editor plus a preview window), but the tool is architected so that the language, the geometry kernel, and the rendering pipeline are cleanly separable and can also be driven headlessly [^1].

Geometrically, OpenSCAD is a **constructive solid geometry (CSG)** system. CSG treats modelling as the algebraic composition of primitives — cubes, spheres, cylinders, extrusions — through Boolean operations (union, difference, intersection) and affine transformations [^3]. Every `.scad` script is, in effect, a CSG expression tree; OpenSCAD can even export this tree as a `.csg` file, and its preview mode uses OpenCSG to display the unresolved tree before committing to a full evaluation [^1].

Parametrically, geometry is defined by named variables and modules rather than by direct manipulation of a viewport. Changing a variable and re-running the script re-derives the model, so parameters are first-class citizens of the design [^4]. This is the core difference from conventional graphical CAD systems (SolidWorks, Fusion 360, FreeCAD's GUI, Rhino): those systems record a *history* of interactive operations and let the user parametrise selected features, whereas OpenSCAD *is* the parametric description — there is no separate history to reconcile, and the model exists only as source code [^5]. Users of programming-based CAD explicitly value this trade — the ability to abstract, reuse and structure geometry as code — even though it costs them the incremental, reversible feel of direct manipulation [^5].

## 2. What OpenSCAD is used for

The tool's typical uses follow directly from the CSG-plus-script model:

- **Procedural and parametric generation of 3D models.** Variables and control constructs (`for`, `if`, modules, function calls) let designers describe families of shapes rather than one instance. Parametric design in this sense is a form of generative design in which the designer manipulates the parameters that produce the shape, not the shape itself, and can therefore explore product families and variants quickly [^4].
- **Reproducible modelling workflows.** Because the model is a plain-text script, it is diff-able, versionable in Git, and re-executable; this is one reason OpenSCAD is the most widely used scripting tool for parametric open-source scientific hardware, where documentation and replicability are prerequisites [^6].
- **Generation of models for digital fabrication and additive manufacturing.** OpenSCAD exports directly to STL, 3MF, OFF, AMF, DXF, SVG and PNG — the standard input formats for slicers, laser cutters and documentation pipelines [^1].
- **Automation of design variations through parameters.** From the command line, `openscad -o out.stl -D var=val ... file.scad` re-derives a customised model for each parameter set, and `-p`/`-P` load full customiser parameter files or sets, so batch generation of variants can be scripted without opening the GUI [^1][^7].
- **Case studies in personalised products.** Reported applications include prosthetic fingers whose ROM is derived from anthropometric measurements [^8], body-powered prosthetic hands parametrised on phalanx and palm dimensions [^9], transradial sockets, orthoses, breast prostheses, and assistive devices for users with rheumatic diseases [^10][^11].

## 3. Why OpenSCAD suits a web platform for parametric model generation

Four properties of OpenSCAD map cleanly onto the requirements of a browser-based configurator:

**Parameter-driven workflows.** OpenSCAD scripts already exist to be parametrised: the "Customizer" convention exposes top-of-file variables as UI-editable parameters, and this same convention is honoured by the desktop application, by the command-line interface, and by third-party front-ends [^7][^12].

**Separation of geometry definition from user interface.** Because the geometry lives entirely in the `.scad` source and the UI only mutates parameter values, the two layers can evolve independently — a property explicitly exploited by early web customisers, which wrap unchanged OpenSCAD scripts in PHP or JavaScript form-generators so that novice users can customise 3-D-printable products without touching the code [^10].

**Automated generation of customised variants.** Command-line execution with `-D`, `-p`, `-P` and the full range of export flags makes OpenSCAD scriptable from any backend; this is how server-side "one click" customisers deliver a personalised STL per request [^1][^7].

**Integration through CLI, APIs, and WebAssembly.** OpenSCAD has been compiled to WebAssembly (the "openscad-wasm" build), and this headless WASM kernel now underlies multiple browser front-ends — the community *OpenSCAD Playground* [^12], the recent *OpenSCAD Web* project, which combines the WASM kernel with a Monaco editor, a Three.js viewer and a customiser UI [^13], and commercial services such as *printpal.io*, which render entirely in the browser with no upload of user code [^14]. The broader feasibility of running CAD kernels in the browser via WebAssembly, and its trade-offs against desktop systems, has itself been studied and reported to be adequate for collaborative, educational and lightweight design use, while still limited for very complex assemblies [^15].

**Relevance for scalable, browser-based configurators.** These properties together make OpenSCAD a viable geometry engine for scalable configurators of the kind explored in the mass-personalisation and open-source-hardware literatures, where the goal is precisely to let non-technical end-users derive their own STLs from a designer-authored parametric template [^10][^11].

## 4. Why OpenSCAD suits an AI-assisted design workflow

Recent work explicitly pairs OpenSCAD (and adjacent script-based CAD languages) with large language models:

- **AI can generate, adjust and explain parametric code.** ELhadad et al. train a custom LLM to turn natural-language design prompts into parametric OpenSCAD scripts for material-handling-equipment parts, reporting that the outputs are accurate, modifiable, and usable by OpenSCAD users of varying expertise [^16]. Schöfer & Seibel describe "augmented design automation" — a semantic layer above script-driven CAD (CadQuery in their demonstration) that interprets abstract, context-based user requests and drives the underlying parametric kernel [^17].
- **Text-to-CAD workflows are being productised around OpenSCAD.** Practitioner accounts describe using ChatGPT-class models to emit `.scad` code from short natural-language prompts and then iterating on the source, noting that OpenSCAD's small, well-documented language is disproportionately well represented in LLM training data, that scripts are self-contained (no imports, no environment), and that the render loop is fast enough for tight iteration — properties that make OpenSCAD a better LLM target than larger scripting APIs such as FreeCAD's [^18]. Similar observations recur in independent write-ups: LLMs can supply a "solid starting point for parametric design" but still make errors on more complex additions, so human review of the emitted code remains necessary [^19].
- **Requirements-to-parameters translation.** In an industrial-design/prosthetic context, the same mechanism can be used to map user requirements or anthropometric measurements onto parameter values feeding the OpenSCAD script — an application already prototyped for prosthetic fingers whose parameters are derived directly from measured finger dimensions [^8].
- **Traceability, versioning and reproducibility.** Because the artefact is source code, AI suggestions can be diffed, code-reviewed, versioned in Git, and re-executed to yield the same geometry — a property emphasised as the main reason OpenSCAD dominates the parametric open-source hardware ecosystem [^6].
- **Human review of AI-generated suggestions.** The parametric structure lets a human reviewer alter individual variables or modules without regenerating the whole design, and the immediate preview loop makes verification cheap [^18][^19].

## 5. Limitations and risks

- **Reduced suitability for complex organic surfaces.** A qualitative study of 20 programming-based CAD users (predominantly OpenSCAD) identifies "creation of organic shapes" as a persistent difficulty of the paradigm, alongside 3-D spatial understanding, validation/debugging, and code–view navigation [^5].
- **Steep learning curve for users unfamiliar with code.** OpenSCAD requires the designer both to reason spatially and to express that reasoning as code, a combination widely reported as difficult for newcomers and for spatially oriented but non-programming users [^19][^9].
- **Limits in interactive modelling / direct manipulation.** Direct manipulation has been the dominant CAD paradigm for decades because it is fast, incremental and reversible; OpenSCAD trades those affordances for abstraction and reproducibility [^5].
- **Format and interoperability limits.** OpenSCAD cannot export to standard *parametric* interchange formats (e.g. STEP with feature history), so parameter information is lost on export to downstream engineering pipelines — an important limitation for scientific-hardware and industrial workflows that depend on parametric interchange [^6].
- **Validation risk for AI-generated code and parameters.** LLMs produce plausible OpenSCAD readily but still emit wrong dimensions, thin walls, or ill-composed features, and cannot themselves guarantee geometric or physical correctness; practitioners consistently warn that AI output requires human verification [^18][^19]. Public tools that expose this workflow embed disclaimers to the same effect ("AI can make mistakes. Verify output before relying on it.") [^14].
- **Automated generation is not clinical or ergonomic validation.** Even the more developed parametric prosthetic and orthotic case studies stop at demonstrating that geometry matches measured anthropometry or a target range of motion — they do not, and cannot, replace fit trials, ergonomic assessment or clinical validation [^8][^9][^11].

## 6. Relevance to Industrial Design research

- **Research Through Design.** Because the artefact is executable code, a parametric OpenSCAD platform can itself be the site of enquiry: variants can be generated, printed, tested, and versioned as part of the research process, and the parameter space of the design becomes explicitly investigable rather than tacitly embedded in a designer's CAD file [^6][^4].
- **Design for Additive Manufacturing (DfAM).** Additive manufacturing has been argued to shift design agency toward the end-user by enabling design-toolkits and 3-D-printed personalisation; parametric script-based CAD is one of the most direct ways to realise those toolkits [^20][^10].
- **Personalised product design.** Applied studies of parametric AM in assistive and prosthetic contexts converge on the same argument: parametric templates plus online configurators plus low-cost AM equal a viable path to affordable, individually fitted devices [^11][^8][^9].
- **Transparent and reproducible design processes.** Text-based, open-source geometry supports the kind of disclosure and replication expected in open-source hardware and increasingly in design research more broadly [^6].
- **Web-based configurators for customised products.** The existence of production-ready WASM builds and community/commercial browser configurators demonstrates that OpenSCAD can be embedded in the class of platform proposed in this dissertation without a bespoke geometry kernel [^12][^13][^14].

## Synthesis

OpenSCAD is best understood as a **CSG-based, source-code-first CAD environment** whose defining trade-off is legibility, reproducibility and automatability in exchange for the interactive comfort of direct-manipulation CAD [^5][^6]. That trade-off is favourable for the specific context of this dissertation — a web-based configurator for parametric prosthetic hands assisted by AI — for three converging reasons: (i) the tool already separates geometry from interface and already runs headlessly and in the browser via WebAssembly, so a web configurator does not require reinventing a CAD kernel [^12][^13][^1]; (ii) its text-based, small, well-documented language is a favourable target for current LLMs, whose failure modes (dimensioning errors, invented features) are the same kinds of failures that a human reviewer can catch by reading a short script and adjusting variables [^18][^19]; and (iii) parametric anthropometric personalisation of upper-limb prostheses has repeatedly been demonstrated in the literature using OpenSCAD or equivalent script-based approaches, so the geometric plausibility of the pipeline is established, even though clinical and ergonomic validation remain outside its scope [^8][^9][^11].

## Comparison: OpenSCAD vs. conventional graphical CAD

| Dimension | OpenSCAD | Conventional graphical CAD (e.g. SolidWorks, Fusion 360, FreeCAD GUI) |
|---|---|---|
| Interaction paradigm | Programming-based; edit code, re-render [^5] | Direct manipulation of geometry in a viewport [^5] |
| Underlying representation | CSG expression tree evaluated from a script [^3][^1] | Feature history over B-rep kernel |
| Parameters | First-class — every variable is a parameter [^4] | Supported but layered onto a GUI feature tree |
| Reproducibility / version control | High (plain-text source, Git-friendly) [^6] | Binary files, weaker diff/merge |
| Organic surfaces / spline modelling | Weak [^5] | Native support |
| Debugging & validation | Reported as a persistent user challenge [^5] | Interactive feedback loop |
| Headless / automated execution | Native CLI, `-D`/`-p`/`-P`, many export formats [^1][^7] | Uneven; often requires proprietary APIs |
| Web / WebAssembly deployment | Available via WASM builds and multiple browser front-ends [^12][^13] | Rare; typically cloud-hosted commercial |
| Parametric export (e.g. STEP with features) | Not supported — parametric info is lost on export [^6] | Supported |
| Fit to LLM-based code generation | High — small, well-documented language [^18] | Lower — larger, less consistent APIs [^18] |

## Summary table: advantages, limitations, and implications for this project

| Aspect | Advantages | Limitations | Implication for the dissertation |
|---|---|---|---|
| Language & representation | Small, script-based, CSG-based; readable, versionable [^6][^3] | Steep learning curve; not organic-surface-oriented [^5][^19] | Geometry authored by a designer, edited (rarely) by end users, and largely generated by AI |
| Parametric workflow | Every variable is a parameter; Customizer convention exposes them to any UI [^7][^12] | Direct manipulation is limited [^5] | Anthropometric inputs map cleanly to script variables |
| Automation | CLI, WASM and API paths; batch export of STL/3MF [^1][^7] | No parametric export (STEP) [^6] | Server- or browser-side generation of per-user STLs is feasible; interoperability with engineering CAD is one-way |
| Web deployment | Mature WASM builds; multiple demonstrated browser front-ends [^12][^13][^15] | Web builds still limited for very complex assemblies [^15] | Browser configurator is realistic for a hand-scale device |
| AI integration | OpenSCAD is a favourable LLM target; recent research shows prompt-to-`.scad` pipelines [^16][^17][^18] | AI errors require human review; no clinical validity [^18][^14] | AI can propose and adjust code; the parametric structure lets a designer or clinician verify and correct it |
| Personalisation context | Demonstrated for prosthetic fingers, hands, sockets, orthoses, assistive devices [^8][^9][^11][^10] | Fit / ergonomics / clinical validation are out of scope of the tool [^8][^9] | The platform supports personalisation *of geometry*; clinical validity is a separate research object |
| Industrial-design framing | Aligns with Research-Through-Design, DfAM, open-source hardware and personalised product design [^20][^4][^6] | — | Provides a defensible conceptual bridge from tool-choice to design-research contribution |

## Scope note

This report is based on a bounded search of academic and practitioner sources and is not exhaustive. In particular, the practitioner-blog evidence for AI-assisted OpenSCAD workflows is early, and only a handful of peer-reviewed papers directly evaluate LLM-driven parametric CAD in a form usable for script-based CAD [^16][^17]. Peer-reviewed evidence in that specific intersection is still thin and should be expected to grow.

## References

- Bustamante, M., Vega-Centeno, R., Sanchez, M., & Mio, R. (2018). *A Parametric 3D-Printed Body-Powered Hand Prosthesis Based on the Four-Bar Linkage Mechanism.* [^9]
- ELhadad, N., Aboulhassan, A., & Hassan, Y. M. I. (2026). *LLM-based 3D Model Generation of MHE for OpenSCAD.* [^16]
- Ghali, S. (2008). *Constructive Solid Geometry* (chapter). [^3]
- Gonzalez Avila, J. F., Pietrzak, T., Girouard, A., & Casiez, G. (2024). *Understanding the Challenges of OpenSCAD Users for 3D Printing.* CHI 2024. [^5]
- Kudus, A., & Syahibudil, I. (2017). *The value of personalised consumer product design facilitated through additive manufacturing technology.* [^20]
- Lim, D. (2018). *Customization of a 3D Printed Prosthetic Finger Using Parametric Modeling* (DETC 2018-85645). [^8]
- Machado, F., Malpica, N., & Borromeo, S. (2019). *Parametric CAD modeling for open source scientific hardware: Comparing OpenSCAD and FreeCAD Python scripts.* PLOS ONE. [^6]
- Nilsiam, Y., & Pearce, J. M. (2017). *Free and Open Source 3-D Model Customizer for Websites to Democratize Design with OpenSCAD.* Designs, 1(1), 5. [^10]
- OpenSCAD project. *OpenSCAD — The Programmers Solid 3D CAD Modeller* (official site). [^2]
- OpenSCAD project. *openscad(1) manual page.* [^1]
- OpenSCAD community. *OpenSCAD User Manual — Using OpenSCAD in a command-line environment.* Wikibooks. [^7]
- OpenSCAD Playground (WebAssembly port). [^12]
- *OpenSCAD Web* (Brooks et al., open-source browser front-end). [^13]
- *printpal.io* — browser-based OpenSCAD CAD editor. [^14]
- Romani, A., & Levi, M. (2020). *Parametric Design for Online User Customization of 3D Printed Assistive Technology for Rheumatic Diseases.* [^11]
- Schöfer, F., & Seibel, A. (2025). *Augmented design automation: leveraging parametric designs using large language models.* Cambridge / DESIGN. [^17]
- Trautmann, L. (2021). *Product customization and generative design.* [^4]
- *Browser-Based Parametric Modeling: Bridging Web Technologies with CAD Kernels* (2020). IJETCSIT. [^15]
- TexoCAD (2026). *Using ChatGPT to write OpenSCAD code.* Practitioner blog. [^18]
- BryanPH. *Powerful Design Process with OpenSCAD and LLMs.* Practitioner blog. [^19]


[^1]: openscad(1) — openscad.

[^2]: OpenSCAD - The Programmers Solid 3D CAD Modeller.

[^3]: Ghali, 2008. Constructive Solid Geometry.

[^4]: Trautmann, 2021. Product customization and generative design. Multidiszciplináris Tudományok.

[^5]: Avila et al., 2024. Understanding the Challenges of OpenSCAD Users for 3D Printing. International Conference on Human Factors in Computing Systems.

[^6]: Machado et al., 2019. Parametric CAD modeling for open source scientific hardware: Comparing OpenSCAD and FreeCAD Python scripts. PLoS ONE.

[^7]: OpenSCAD User Manual/Using OpenSCAD in a command line ...

[^8]: Lim, 2018. DETC 2018-85645 CUSTOMIZATION OF A 3 D PRINTED PROSTHETIC FINGER USING PARAMETRIC MODELING.

[^9]: Bustamante et al., 2018. [Regular Paper] A Parametric 3D-Printed Body-Powered Hand Prosthesis Based on the Four-Bar Linkage Mechanism. International Conferences on Biological Information and Biomedical Engineering.

[^10]: Nilsiam & Pearce, 2017. Free and Open Source 3-D Model Customizer for Websites to Democratize Design with OpenSCAD.

[^11]: Romani & Levi, 2020. Parametric Design for Online User Customization of 3D Printed Assistive Technology for Rheumatic Diseases. International Conference on Augmented and Virtual Reality.

[^12]: OpenSCAD Playground | openscad-playground.

[^13]: CameronBrooks11/openscad-web, 2026.

[^14]: printpal - Free Online CAD Editor — Parametric 3D Design with OpenSCAD in your Browser | printpal.io.

[^15]: Browser-Based Parametric Modeling: Bridging Web Technologies with CAD Kernels, 2020. International Journal of Emerging Trends in Computer Science and Information Technology.

[^16]: ELhadad et al., 2026. LLM-based 3D Model Generation of MHE for OpenSCAD. Procedia Computer Science.

[^17]: Schöfer & Seibel, 2025. Augmented design automation: leveraging parametric designs using large language models. Proceedings of the Design Society.

[^18]: TexoCAD, 2026. Using ChatGPT to write OpenSCAD code | TexoCAD Blog.

[^19]: Powerful Design Process with OpenSCAD and LLMs | BryanPH.

[^20]: Kudus & Syahibudil, 2017. The value of personalised consumer product design facilitated through additive manufacturing technology.