# EDT-005 — Cable Route and Core Validation

**Approval:** `EDT-005/F04 APPROVED` (Option B: route at Location level, original device endpoints retained).  
**Test execution:** `PARTIAL`.  
**Review status of other observations:** `PENDING APPROVAL`.  
**Baseline:** `e459be0b6e588bb7795bf76211b84b8dfba97160`.

## Approved acceptance criteria — F04

1. Default cable route is `source_location → target_location`, e.g. `=CPT-103+A → =ST101+FD` for `=ST101+-5W1`.
2. Preserve original `P20376`/`P20377` plus optional `P20383`/`P20385` without modification.
3. Keep core/pin source and target as a separate relation.
4. Handle identifiers containing hyphens (`+DDC-103`); no naive string split.
5. Preserve one logical cable and all its Cable Definition placements; no duplicated core counts.
6. When location resolution is unverified, clearly label derived/unknown status.

## Current direct evidence from Cable_v2.edc

- Six distinct full Cable DT: `=ST101+-4W1`, `=ST101+-4W2`, `=ST101+-5W1`, `=ST101+-5W2`, `=ST101+-5W3`, `=ST101+-9W1`.
- Thirteen Cable Definition records/placements in the export, rather than thirteen distinct cables.
- Property IDs: `20006` Cable Full DT, `20376` Cable Source, `20377` Cable Target, `20383`/`20385` endpoints with plug, `20042` number of connections, `20040` cable type, `20067` designation in graphic, `20041` cable length.
- Cable length fields observed blank in this snapshot.
- Source/Target values and proposed derived locations: see [approved rule](../Content/13_CABLE_ROUTE_LOCATION_RULES.md).

## Core inventory from existing EPDZ extraction document — requires independent re-test

The figures below are **reported in the current** `Content/11_WIRING_EPDZ_EXTRACTION.md`. In the recent tester session, that text was checked and cable totals compared with `Cable_v2.edc`, **but `Wiring.epdz`/`manifest.db` was not independently re-extracted**. Do not upgrade status to full PASS on that basis alone.

| Cable | Total | Reported used | Reported spare | Reported spare IDs |
|---|---:|---:|---:|---|
| `4W1` | 6 | 5 | 1 | GN |
| `4W2` | 10 | 8 | 2 | 9, 10 |
| `5W1` | 3 | 3 | 0 | — |
| `5W2` | 10 | 6 | 4 | 3, 8, 9, 10 |
| `5W3` | 30 | 30 | 0 | — |
| `9W1` | 2 | 1 | 1 | BK |
| **Total** | **61** | **53** | **8** | |

`Content/11_WIRING_EPDZ_EXTRACTION.md` identifies a conductor's EPLAN page/placement value (`19007`) as a signal for being drawn on the schematic. **Placement present is not automatically proof of physical termination or installation.** A missing placement needs exception tests (e.g. unplaced yet assigned conductor), prior to universal used/spare classification.

## Pending discrepancy tests

- `4W1`: `P20040 = 6x0.5 mm²` whereas `M20067` text refers to `CY-6x1.25mm2`.
- `5W1`: `P20040 = CVV-3X2.5 mm2 – 0.6/1kV` whereas `M20067` text refers to `CVV-3X1.5 mm2`.
- Compare with EPLAN project/part master data. Do not auto-correct or elevate one field above the other without review.

## Next test procedure

1. Confirm sanitized snapshot and record commit/file hashes and dates.
2. Parse the six distinct Cable DT records from `Cable_v2.edc` and list all 13 Cable Definition object IDs.
3. Extract `Wiring.epdz` → `manifest.db` and enumerate every `Cable definition` and `Conductor / wire` (including unplaced conductors).
4. Join conductors to cable by explicit relationship/DT with evidence; validate uniqueness and count each core once. Verify `P19007` and use/placement status semantics.
5. Join each used conductor to Source Device/Pin and Target Device/Pin using explicit connection association where available; report missing links instead of inventing.
6. Resolve the two route locations against the project location structures; test `+DDC-103` parsing.
7. Validate six route examples in EPLAN. Distinguish physical route, cable endpoint, conductor endpoint and schematic placement.
8. Record PASS/PARTIAL/FAIL/UNVERIFIED per acceptance criterion and obtain user approval before modifying reusable rules.

## References

- [Cable_v2.edc](../Export_ProjectData_Sanitized/External_editing/Cable_v2.edc)
- [Existing EPDZ research](../Content/11_WIRING_EPDZ_EXTRACTION.md)
- [Cable external-editing mapping](../Content/12_CABLE_EXTERNAL_EDITING_ELEMENTS.md)
