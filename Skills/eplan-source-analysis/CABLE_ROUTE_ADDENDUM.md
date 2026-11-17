# Reusable Query Procedure — Cable Route by Location

**Approved decision:** EDT-005/F04 — Option B, Location + Raw Device.

Use this procedure when answering questions such as “Cable 5W1 đi từ đâu đến đâu?”, “Liệt kê tuyến cáp Source/Target”, or preparing a route inventory.

1. Establish project/snapshot and verify approved sanitized data access. Keep original values and cite file/property/commit.
2. Read `Cable_v2.edc` (or equivalent cable export). Group by `P20006` (Cable DT full); retain all Cable Definition object IDs and placement records separately.
3. Get cable-level original `P20376` and `P20377` (optionally `P20383` and `P20385`). These are **raw Device endpoint values**, not by themselves the user's requested route labels.
4. Resolve `source_location` and `target_location` through EPLAN structure identifiers or a validated location dictionary. Do not split on `-` because locations such as `+DDC-103` contain hyphens. Label derived endpoints as derived unless backed by explicit location properties.
5. **Default answer:** `Cable DT | Source Location | Target Location`; optionally type/part/number of cores.
6. **Detailed engineering view:** Include original Cable Source/Target Device endpoints alongside Location; do not discard or silently rewrite them.
7. **Core view:** Keep conductor `Source Device/Pin` / `Target Device/Pin` separate from cable route; require direct associations, no guessed joins.
8. Preserve source order. Do not infer power-flow direction or physical path from cable endpoint order.
9. If any location is missing or ambiguous, output `UNRESOLVED`, provide original endpoints and explain what is missing.
10. For this sample, check six examples in `../../Content/13_CABLE_ROUTE_LOCATION_RULES.md`; verify literal `CT01` (do not rewrite to `CT101`).

**Separate open work:** Core Used/Spare report and per-core connection mapping remain `EDT-005 PARTIAL`; cross-export Object ID lifetime remains `EDT-009 PENDING RE-TEST`.

[Approved rule](../../Content/13_CABLE_ROUTE_LOCATION_RULES.md) | [Test case EDT-005](../../Tests/EDT-005_CABLE_ROUTE_AND_CORE_VALIDATION.md) | [Test case EDT-009](../../Tests/EDT-009_OBJECT_ID_STABILITY.md)
