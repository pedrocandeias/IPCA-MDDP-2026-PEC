# Notes — Capítulo 7.2

## Objective

Support section `7.2` by grounding the distinction between designer/technician experience and end-user experience in literature on prosthetic customization platforms, smart prosthetic systems, and adjacent assistive-device interfaces.

## Framing for Elicit

- The manuscript already positions `7.1` around interaction strategy, guided configuration, and controlled exposure of the parametric space.
- Section `7.2` needs literature that helps distinguish user experience by role, not just general usability claims.
- The strongest target is evidence on differentiated permissions, supervised adjustment, intelligibility for non-experts, and collaboration between technical and non-technical actors.
- Adjacent domains such as orthotics, rehabilitation interfaces, and assistive-device customization may be useful if upper-limb prosthetic evidence is sparse.

## Writing Targets

- Clarify how the platform supports the designer or technician as an exploratory and supervisory actor.
- Clarify how the platform supports the end user as an informed but not fully autonomous participant.
- Support the notion of asymmetric collaboration without collapsing the difference between roles.
- Identify literature that links visibility of changes, preview, and intelligibility to trust and acceptance.

## Current Findings

- The available literature provides very limited direct empirical evidence on clinician or prosthetist experience with digital parametric customization platforms for upper-limb prostheses.
- The strongest direct upper-limb customization evidence currently identified is `Saldarriaga et al. (2024)`, which supports parametric socket customization and workflow optimization, but not a detailed analysis of professional experience.
- `Resnik et al. (2018)` is useful for upper-limb prosthetic user experience, training burden, calibration, and interpretability, but it concerns control systems rather than customization platforms.
- `Cordella et al. (2016)`, `Trent et al. (2019)`, and `Bates et al. (2020)` help with upper-limb context, user needs, and design constraints, but do not directly study digital customization workflow experience.
- Most usable evidence on professional workflow, iteration, supervision, and decision-making comes from adjacent contexts, especially lower-limb prosthetics and other assistive-device design systems.

## Direct Evidence vs Transferable Evidence

### Direct upper-limb evidence

- `Saldarriaga et al. (2024)`: parametric transradial socket design, step-by-step customization, design-time optimization.
- `Resnik et al. (2018)`: professional and patient experience with upper-limb prosthetic control systems, calibration burden, training, adaptation.
- `Cordella et al. (2016)`: user needs and interface limitations in upper-limb prostheses.

### Transferable adjacent evidence

- `Mbithi et al. (2025)`: clinician-supervised digital workflow, iterative CAD/CAM process, importance of clinician input for patient-specific adjustments.
- `Lee et al. (2024)`: physics-based digital design and comfort-oriented computational workflow.
- `Mixuan Li & Aflatoony (2023)`: parametric tool development with therapist-centered testing and iterative design logic.
- `Patiniott et al. (2025)`: collaborative decision-making and visualization of design consequences across stakeholders.
- `Oldfrey et al. (2024)`: training and process gaps in digital fabrication for upper-limb prosthetics.

## Main Gap for Section 7.2

- There is a marked imbalance between the conceptual promise of digital customization platforms and the amount of empirical evidence about how professionals and end users actually experience them.
- The literature does not yet describe in detail how clinicians compare variants, conduct iterative adjustment, manage permissions, or distribute decision-making responsibility inside parametric platforms.
- There is also little direct evidence comparing technical-professional experience and end-user experience within the same digital system.

## Elicit Report 5aeb15f6-71b8-4ac4-8fe1-912a29d46898

### Core Argument Emerging from the Report

- Digital prosthetic customization platforms are best understood as spaces of asymmetric collaboration rather than neutral interfaces.
- In socket-design contexts, configurative authority and decision responsibility remain concentrated in technical professionals.
- In control-customization contexts, end users gain more meaningful agency because preference and usability can only be judged by the user in action.
- Automation functions less as a substitute for expert judgment than as a mechanism of cognitive offload, workflow structuring, and baseline proposal generation.

### Strongest Evidence for Section 7.2

- The clearest comparison between professional and end-user experience is domain-dependent rather than universal.
- In socket geometry, the literature supports clinician-dominant workflows with user participation mainly as comfort feedback, tolerance judgment, or preference confirmation.
- In control systems, the literature supports stronger end-user participation because users can judge subjective feel, control preference, and task performance in ways clinicians cannot fully infer.
- In aesthetic customization, platforms such as `Peixoto et al. (2025)` show that end users can exercise genuine autonomy when customization is decoupled from clinical fit and biomechanical risk.

### Strongest Evidence for End-User Experience

- End-user trust and intelligibility improve when system logic becomes more visible.
- `Yang et al.` indicates that explicit visualization of decision-space boundaries improves performance and understanding.
- `Sungeelee et al.` suggests that training oriented toward class separability supports better user mental models of the system.
- `Hepp et al.` and `Peixoto et al. (2025)` support the idea that user agency increases when the editable domain is understandable and low-risk.
- A key caution comes from `Resnik et al. (2018)`: technical capability does not guarantee user trust or preference, and users may still prefer more familiar systems.

### Strongest Evidence for Professional Experience

- Professionals retain authority where biomechanical, safety, and fitting concerns dominate.
- Lower-limb transferable studies such as `Mbithi et al.`, `Colombo et al.`, `Morotti`, `Quintero et al.`, and `Reznick et al.` show that platforms can reduce time, structure supervision, and provide more interpretable parameter spaces.
- At the same time, `Eshraghi et al.` shows that digitization may reduce professional confidence when it removes tactile or tacit cues that traditional practice relies on.
- The most useful interpretation is that platforms amplify some forms of professional expertise while constraining others.

### Bridge to Section 7.3

- The report strongly supports reading the platform as a mediator of the design process, not just as a vehicle for displaying parameters or executing commands.
- Mediation occurs through differentiated permissions, visibility control, constrained parameter access, algorithmic starting points, guided comparison, and embedded supervision.
- A central argumentative move for `7.3` is that the platform actively shapes what can be seen, changed, compared, and decided, thereby redistributing agency instead of merely digitizing an unchanged workflow.

### Report-Specific Gaps

- The most serious gap remains upper-limb socket customization platforms.
- There is almost no direct evidence comparing professional experience and end-user experience within the same upper-limb socket-design system.
- It is still unclear whether lower-limb paradigms of supervision, FEA-based evaluation, evidence-generated starting points, and role differentiation transfer cleanly to upper-limb biomechanical and functional demands.
- There is little longitudinal evidence on training, adaptation, confidence, and workflow change for either professionals or end users.

## Writing Implications

- The section should not claim that the literature robustly documents professional experience with upper-limb parametric platforms; it does not.
- The text can state that the professional role is supported mainly by indirect or transferable evidence: supervision, interpretation, clinical responsibility, and specialized adjustment remain concentrated in technical actors.
- The end-user side is likely to be better supported by literature on trust, intelligibility, training burden, perceived control, and visibility of system feedback.
- A strong argumentative move for `7.2` is to frame the platform as a space of asymmetric collaboration: the user gains visibility and participation, but not unrestricted authorship over all parameters or decisions.
- Another strong move is to explicitly identify the lack of studies that compare the experience of designers/clinicians and end users within the same prosthetic customization interface.
- The report supports a sharper internal distinction between three customization domains:
  socket geometry as clinician-dominant,
  control customization as user-sensitive and `human-in-the-loop`,
  and aesthetic customization as the domain where end-user autonomy is easiest to justify.
- The transition to `7.3` can be built around the claim that the platform does not merely support decisions; it structures the field of possible decisions through permissions, constraint-setting, visualization, and algorithmic mediation.

## Recommended Workflow

1. Run targeted searches `1` to `4` first.
2. Use `Report 1` as the main synthesis workflow for the section.
3. Use `Report 2` only if the first report underdevelops the distinction between professional and end-user experience.
4. Keep `Report 3` in reserve if useful overlap with section `7.3` becomes clear.
5. Prioritize a follow-up search or report focused on end-user experience, trust, intelligibility, and participation, because the professional side is currently more lacunar than evidential.
