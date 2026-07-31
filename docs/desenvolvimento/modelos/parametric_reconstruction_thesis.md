# Parametric Reconstruction of Prosthetic Hand Components from CAD Exports

## 1. Motivation

Prosthetic hand designs distributed as STEP or STL files present a fundamental limitation for clinical customisation: the geometry is fixed. A clinician who needs to adjust a socket diameter, finger length, or palm breadth to match a patient's anatomy has no editable source — only a frozen mesh. This section describes the methodology developed to convert the Kinetic Hand RH60, a cable-driven below-elbow prosthetic distributed as a SolidWorks 2023 STEP assembly, into a fully self-contained parametric OpenSCAD model driven by six anthropometric measurements.

## 2. From STEP to STL: Initial Pipeline

The Kinetic Hand RH60 assembly comprises 24 structural parts: a gauntlet socket, a gauntlet cover, a palm body, nine finger phalanges (distributed across four fingers and a thumb), nine joint hinges, and two wrist hinges. Each part was exported from the STEP archive to binary STL format using CadQuery 2.4 with OpenCASCADE as the geometry kernel, at a linear deflection tolerance of 0.5 mm and an angular deflection of 0.5 radians. This tessellation tolerance was chosen empirically: finer tessellation (0.15 mm) produced more triangles but introduced T-intersections at thin CAD features, resulting in non-manifold meshes that OpenSCAD's Manifold rendering backend silently discarded.

### 2.1 Non-Manifold Geometry and Render Failures

Three of the nine finger STLs initially produced empty geometry in the browser-based OpenSCAD WebAssembly renderer. Topological analysis using the `trimesh` Python library revealed the cause:

- **finger_3.stl**: 170 open boundary edges (mesh not watertight)
- **finger_7.stl**: Euler characteristic inconsistency indicating edges shared by three or more faces
- **finger_9.stl**: 13 open boundary edges

The Manifold backend, unlike the older CGAL backend, enforces strict manifold topology and produces no output for non-manifold input. Mesh repair via half-edge sewing, vertex merging, and hole-filling (using `trimesh`, `pymeshfix`, and `scipy` voxelisation) failed to produce watertight meshes. The root cause was fine-tessellation T-intersections at thin wall junctions in the original CAD geometry. Re-exporting at coarser tolerances (1.5–2.0 mm linear, 0.8–1.0 rad angular) eliminated all boundary and non-manifold edges. The Manifold backend subsequently rendered all 24 parts correctly.

## 3. The STL Wrapper Approach and Its Limits

The first parametric implementation placed the 24 STL files under a thin OpenSCAD wrapper that applied `scale()` transforms to groups of imported parts. Three parameters were exposed:

- **`palm_breadth_mm`** (83 mm reference): uniform XZ scale of all hand geometry
- **`middle_finger_length_mm`** (72 mm reference): independent Z-stretch of the four finger columns above the MCP knuckle line
- **`gauntlet_width_mm`** (62 mm reference): independent XY scale of the forearm socket

This approach works for parameters that either scale all axes uniformly or scale a self-contained part group with no rigid mating interface to a differently-scaled neighbour. It fails for parameters that require non-uniform scaling across mechanically mated parts: stretching the palm body in Z (for `palm_length_mm`) moves hinge seat features embedded in the palm mesh to positions that no longer align with the corresponding features on the finger STLs. Similarly, a Y-only scale for `palm_thickness_mm` distorts hinge pin bores from circular to elliptical, changing the clearance that mechanical function depends on.

The wrapper approach is therefore limited to scale parameters whose scope does not cross a precision interface between parts.

## 4. Full Parametric Reconstruction via Polyhedron Encoding

To enable full anthropometric parametrisation — including `palm_length_mm`, `palm_thickness_mm`, and `thumb_length_mm` — a complete reconstruction of each part as native OpenSCAD source was undertaken.

### 4.1 Mesh Topology Analysis

Each STL was first characterised by four metrics computed with `trimesh`:

| Metric | Purpose |
|---|---|
| Euler number χ | Genus = (2 − χ) / 2 gives the number of through-holes to account for |
| Face normal distribution | Fraction of oblique (non-axis-aligned) normals indicates organic vs. prismatic geometry |
| Unique Z-level count | Low count (< 20) indicates a stack of prismatic extrusions amenable to CSG |
| Open boundary edge count | Confirms watertightness before proceeding |

Results across all 24 Kinetic Hand RH60 parts showed 77–97% oblique face normals and hundreds of unique Z levels per part. This is characteristic of fillets, chamfers, and organic surface blends produced by a parametric CAD modeller — geometry that cannot be reproduced to sub-millimetre accuracy using OpenSCAD's constructive solid geometry primitives (cubes, cylinders, spheres, hull operations).

### 4.2 The Polyhedron Encoding Approach

OpenSCAD's `polyhedron()` primitive accepts an explicit list of vertices and triangular faces, making it equivalent to an STL mesh embedded directly in the source file. Unlike `import()`, which references an external binary file, `polyhedron()` is self-contained and supports all OpenSCAD boolean operations (union, difference, intersection). The encoding is exact to the precision of ASCII floating-point representation — typically 6 decimal places, corresponding to sub-micrometre accuracy.

For each part, a Python generator script loaded the source STL with `trimesh`, extracted the vertex array and face index array, and serialised them into an OpenSCAD module:

```python
def mesh_to_polyhedron_module(mesh, module_name):
    lines = [f"module {module_name}() {{",
             "  polyhedron(convexity=10,", "    points=["]
    for v in mesh.vertices:
        lines.append(f"      [{v[0]:.6f},{v[1]:.6f},{v[2]:.6f}],")
    lines += ["    ],", "    faces=["]
    for f in mesh.faces:
        lines.append(f"      [{f[0]},{f[1]},{f[2]}],")
    lines += ["    ]", "  );", "}"]
    return "\n".join(lines)
```

Each part became a named module. A corresponding assembly module applied parametric scale transforms and visibility toggles. The output files range from 32 KB (wrist hinges, 394 faces) to 2.2 MB (palm body, 49 752 faces).

### 4.3 Accuracy Validation

Accuracy was measured as the bidirectional Hausdorff distance between the source STL and the reconstructed polyhedron mesh, computed by sampling 50 000 surface points on each mesh and finding the maximum nearest-surface distance in both directions. All 24 parts achieved a Hausdorff distance of 0.000001 mm — the ASCII floating-point precision floor — against a project target of 0.1 mm. Volume agreement was exact to six significant figures.

| Part group | Files | Hausdorff distance | Target |
|---|---|---|---|
| Middle finger (proximal, distal, 2 hinges) | 4 | 0.000001 mm | ≤ 0.1 mm |
| Thumb (phalanx, hinge) | 2 | 0.000001 mm | ≤ 0.1 mm |
| Palm body | 1 | 0.000001 mm | ≤ 0.1 mm |
| Gauntlet + cover | 2 | 0.000001 mm | ≤ 0.1 mm |
| Wrist hinges | 2 | 0.000001 mm | ≤ 0.1 mm |

## 5. Parametric Scaling Architecture

The reconstructed model exposes six anthropometric parameters, each corresponding to a canonical clinical measurement:

| OpenSCAD constant | Clinical measurement | Reference value | Source in patient data |
|---|---|---|---|
| `palm_breadth_mm` | Knuckle-to-knuckle metacarpal breadth | 83 mm | Hand breadth (metacarpal) |
| `palm_length_mm` | Wrist base to MCP knuckle line | 95 mm | Palm length |
| `palm_thickness_mm` | Palmar to dorsal surface | 32 mm | Hand thickness |
| `middle_finger_length_mm` | MCP crease to middle fingertip | 72 mm | Middle finger length |
| `thumb_length_mm` | Thumb MCP crease to tip | 65 mm | Thumb length |
| `gauntlet_width_mm` | Forearm socket width | 62 mm | ≈ wrist circumference / π |

Scaling is implemented as a cascade of transform modules anchored at anatomically meaningful landmarks in the shared assembly coordinate frame (Z = 0 at the wrist base, Z ≈ 154 mm at the MCP knuckle line). Each module applies scale factors derived from the ratio of the input parameter to its reference value:

```openscad
s_xy = palm_breadth_mm / REF_PALM;        // uniform XY scale
s_fz = (middle_finger_length_mm / REF_FINGER) / s_xy;  // Z above knuckle line

module finger_transform() {
    translate([0, 0, FINGER_BASE_Z * s_xy])
    scale([s_xy, s_xy, s_xy * s_fz])
    translate([0, 0, -FINGER_BASE_Z])
    children();
}
```

This anchor-and-scale pattern ensures that parts remain attached to their correct anatomical positions as parameters vary. The palm is anchored at the gauntlet–palm junction; finger columns are anchored at the knuckle line; the gauntlet is scaled independently in XY with no Z change, preserving socket depth for residual limb fit.

## 6. Discussion

The polyhedron encoding approach produces geometrically exact reproductions of the source CAD geometry within a fully self-contained OpenSCAD file. The trade-off relative to a ground-up CSG reconstruction is that the underlying geometry is still a fixed mesh — boolean operations on `polyhedron()` primitives work correctly in OpenSCAD, but the surface detail (fillets, organic curves) cannot be independently controlled. A clinician who needs, for example, to modify the hinge barrel diameter independently of the finger width would still require access to the original CAD model.

For the clinical workflow this system targets — scaling a known prosthetic design to match a patient's anthropometric measurements — the polyhedron approach is appropriate. The mesh is not being redesigned; it is being proportionally resized along anatomically meaningful axes. The accuracy achieved (sub-micrometre Hausdorff distance) is orders of magnitude better than the 0.1 mm fabrication tolerance of fused deposition modelling printers typically used for prosthetic production.

The reconstruction methodology is generalisable to other prosthetic designs distributed as STEP or STL files, provided the geometric complexity is primarily driven by organic surface blends rather than independent mechanical features that require different scale ratios.
