# EDT-009 — Object Identifier Stability Across EPLAN Exports

**Status:** `PENDING RE-TEST` — Project owner will test after a new export is available.  
**Approval:** No claim of cross-export stability has been approved.  
**Source baseline:** `e459be0b6e588bb7795bf76211b84b8dfba97160`.

## Test objective

Determine whether the BOM value `P_PROPUSER_DBOBJECTID` remains the same for a particular EPLAN object after various project operations and exports. Separately evaluate `A1` from External Editing and placement/function IDs. Do not treat them as interchangeable or permanent IDs without evidence.

## Baseline example values (old export)

| Device DT | BOM `P_PROPUSER_DBOBJECTID` |
|---|---|
| `=ST101+JB01-6K3` | `30/68/17266/0` |
| `=CPT-103+A-5FR1` | `30/68/16985/0` |

These are **observed identifier strings**, not a documented decomposition of their numeric parts. No meaning should be assigned to the components `30`, `68`, etc. without evidence.

## Controlled re-test cases

| Case | Operation | Observation to collect |
|---|---|---|
| A | Export same untouched project twice | BOM ID and `A1` equality |
| B | Close and reopen project, re-export | ID stability under reopen |
| C | Change non-identity property (e.g., Function text), re-export | ID stability under property change |
| D | Copy function/object, re-export | Old object's ID vs copied object's new ID |
| E | Delete/recreate object with same DT, re-export | Whether DT reuse creates distinct object identity |
| F | Compare BOM with EDC/AML/EPJ in one snapshot | Which exact IDs represent device, function, placement and part reference |

For each case capture project version, export timestamp, file/hash, full page, DT full, object/placement IDs and expected/actual match.

## Design constraint until approved

Store the EPLAN object ID as an **opaque, source-scoped evidence field**. Data Engine may generate its own stable surrogate ID and maintain explicit cross-snapshot matching rules, but do not claim a source object ID is a universal, immutable primary key until retesting confirms its scope and lifetime.

## Exit criteria

Tester supplies evidence for each case; project owner approves or rejects the resulting rule; only then Knowledge Maintainer updates `Content/02_PROPERTY_MAP.md`, `Content/06_LEARNING_LOG.md` or Skill. Keep this test `PENDING RE-TEST` until new export is available.
