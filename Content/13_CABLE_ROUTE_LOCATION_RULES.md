# Cable Route by Location — Approved Rule (EDT-005/F04)

**Decision status:** `APPROVED` (owner confirmed Option B, Location + Raw Device, 2026-11-17).  
**Implementation/test status:** `PARTIAL` (normalization rule approved; extraction robustness and core graph need testing).  
**Source baseline:** GitHub `main` `e459be0b6e588bb7795bf76211b84b8dfba97160`.

## 1. Scope and semantics

A physical cable route is reported at the **location** level, not by the first/last connected device.

- **Cable Route:** `Source Location → Target Location`. Default user-facing representation.
- **Raw Cable Source/Target:** Exact source/target device values extracted from EPLAN Cable properties. Keep as separate unmodified fields for audit and engineering traceability.
- **Core / Connection:** Each conductor/connection has independent `Source Device/Pin → Target Device/Pin`. Do not substitute these endpoints into the Cable Route summary.
- A location can contain many devices. Device identity, location identity, cable identity and placement identity are distinct entities.
- Cable source/target order follows the source export; do not assume electrical power direction, physical cable laying direction or route topology without evidence.

## 2. Required output schema

| Field | Meaning | Evidence/Rule |
|---|---|---|
| `cable_dt_full` | Cable identity | `Cable_v2.edc` `P20006` |
| `route.source_location` | Route source structure/location | Resolved from EPLAN structure identifiers or validated location index |
| `route.target_location` | Route target structure/location | Resolved as above |
| `raw.source_device` | Original cable-level source | `P20376` (preserve exact text) |
| `raw.target_device` | Original cable-level target | `P20377` (preserve exact text) |
| `raw.source_with_plug` | Original cable source with plug | `P20383`, if present |
| `raw.target_with_plug` | Original cable target with plug | `P20385`, if present |
| `source_metadata` | Repo commit, file path, snapshot, object/placement ID | Preserve where available |
| `route.resolution_status` | `DIRECT` / `DERIVED_VALIDATED` / `UNRESOLVED` | Do not present a derived value as an exported direct field |
| `cores[]` | Optional conductors/connection-level data | Separate relation; validation still outstanding |

### Implementation requirements

1. Prefer native EPLAN location/structure fields and a canonical project location dictionary. Resolve each raw endpoint to the appropriate full `=...+...` structure, verifying against that dictionary.
2. **Never split at the first or last `-`**: a location such as `+DDC-103` contains a hyphen; a multi-level function/device syntax can contain additional delimiters.
3. If only a raw device string is available, permit a **derived** location only when project structure rules are unambiguous and it can be validated; otherwise return `UNRESOLVED` with raw endpoints intact.
4. Group Cable Definition placements by `cable_dt_full` for route summary but retain placement/object IDs as one-to-many child records. Do not sum `P20042` across repeated placements of the same cable.
5. Do not infer route location from `Function text` (e.g., “From Control Box To …”) when structural source/target is available; descriptive text and structural locations are independent.
6. Preserve raw EPLAN strings; normalization is an additional representation, not destructive rewriting.

## 3. Expected route examples (from `Cable_v2.edc`)

`P20376`/`P20377` are **direct** file values. Source/Target Locations in this table are **derived examples reviewed and approved as the desired presentation**, not independent location properties exported in the current scheme.

| Cable DT (full) | Source Location | Target Location | Raw Cable Source | Raw Cable Target |
|---|---|---|---|---|
| `=ST101+-4W1` | `=ST101+JB01` | `=ST101+CT01` | `=ST101+JB01-INPUT` | `=ST101+CT01-4S1` |
| `=ST101+-4W2` | `=ET101+DDC-103` | `=ST101+JB01` | `=ET101+DDC-103-2K1` | `=ST101+JB01-4K1` |
| `=ST101+-5W1` | `=CPT-103+A` | `=ST101+FD` | `=CPT-103+A-5FR1` | `=ST101+FD-5M1` |
| `=ST101+-5W2` | `=ST101+JB01` | `=CPT-103+A` | `=ST101+JB01-INPUT` | `=CPT-103+A-5FR1` |
| `=ST101+-5W3` | `=ST101+JB01` | `=ET101+DDC-103` | `=ST101+JB01-OUTPUT` | `=ET101+DDC-103-2K1` |
| `=ST101+-9W1` | `=ST101+JB01` | `=ST101+FD` | `=ST101+JB01-24VDC` | `=ST101+FD-9S4` |

**Exact-spelling rule:** The current export uses `CT01`, not `CT101`. Do not silently substitute one for the other.

## 4. User-facing response contract

For “Cable 5W1 goes from where to where?” answer:

> Cable `=ST101+-5W1`: `=CPT-103+A` → `=ST101+FD`.

Optionally show cable type, part and used/spare stats with evidence labels. Provide raw cable endpoints in an engineering/detail view, not as the default route.

For “Which pins do the cores connect to?” show a **separate** core-connection view, e.g. `5FR1:U/T1 → 5M1:U` for a documented `5W1` connection. Do not claim complete per-core associations until the cross-file association test passes.

## 5. Exceptions and quality gates

- Missing or ambiguous location: return `UNRESOLVED`; no guessing.
- Opposite Cable-level Source/Target vs conductor-level direction: retain both and report discrepancy; don't reverse to make them look consistent.
- Multiple Cable Definition placements: one logical cable plus many placements; preserve evidence for all.
- Different export snapshots: don't merge as if they were a single version.
- Verify handling of `+DDC-103`, `=CPT-103+A`, empty or nonstandard structure identifiers, and cable endpoints without a device reference.

## 6. References

- [Cable_v2.edc](../Export_ProjectData_Sanitized/External_editing/Cable_v2.edc)
- [Cable external-editing properties](12_CABLE_EXTERNAL_EDITING_ELEMENTS.md)
- [Cable/core test record](../Tests/EDT-005_CABLE_ROUTE_AND_CORE_VALIDATION.md)
