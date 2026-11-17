# EMDS Learning Proposals — Troubleshooting V2.1

- Date: 2026-11-17
- Owner approval: **PENDING_TECHNICAL_APPROVAL**
- Scope: Additive proposal; does **not** replace the approved LL-005.
- Evidence basis: two user-led VALVE1 workflows; actual resolution of workflow 1 vs simulated responses of workflow 2 are separate.

## LL-006 — Operation-First Adaptive Troubleshooting & Field Evidence Validation

### Finding
A troubleshooting agent that begins with electrical tests can misdirect operators and escalate a small fault. EPLAN explains configured wiring, not actual operating mode, PLC interlocks, alarm latch, sequence, maintenance history, or safe reset procedure. In the real VALVE1 case, the owner confirmed a loose PLC expansion-module power connection as the resolved cause; initial readings including `OL` were ambiguous. The 22-step simulation did not independently resolve a live fault.

### Mandatory controls
1. **Operation-first:** ask machine status (new commissioning / previously healthy / after maintenance), symptoms, alarm/HMI and sequence state.
2. **Reset-history-first:** ask whether Reset was already attempted, which reset, according to what procedure, and what happened. Never recommend Reset without the applicable User Manual, safety conditions, and alarm-recording requirements.
3. **Multi-domain source matching:** Operation/User Manual, Alarm/Fault List, Interlock Matrix, Sequence of Operation, Mechanical/Pneumatic manual, EPLAN and manufacturer manual each answer different questions; none is a blanket substitute for another.
4. **Evidence gate:** if required documents or verifiable operational conditions are missing, say **NOT_AVAILABLE / UNKNOWN**, request exact relevant document, and **STOP**. No guess and no alternative diagnostic trail.
5. **Adaptive one-step dialogue:** when authorized to proceed, ask one safe discriminatory observation/check at a time; update confidence with each result.
6. **Field measurement validation:** `OL`, inverted voltage and unstable voltage require measuring mode, meter reference, load state and safety verification before interpretation.
7. **Stop/escalate:** lack of safe access, missing document, contradiction, or stalled progress ends the diagnostic path until evidence is provided.
8. **Closure:** `RESOLVED` only if the actual user confirms safe recovery; keep unexplained observations unresolved.

### Scope restriction
The principle “ask about Reset first” means **ask Reset history early**, not “perform Reset first.” On any hazard or unknown restart behavior, Reset remains blocked.

## LL-007 — Electrical Topology & Power Flow Verification

### Finding
In the simulated VALVE1 workflow, `Connection.edc` showed `=CPT-103+A-5FR1:R1C → =ST101+JB01-24VDC:1:1` (Object ID `18/15254`), but the agent wrongly treated the source side as a 24V supply upstream. `Device.edc` identifies 5FR1 as Schneider ATV310, part `SE.ATV310H037N4E`. `R1C` is part of a VFD relay contact, not a power supply output by virtue of the wire name.

### Mandatory controls
1. Separate connection record, energized continuity and actual power flow.
2. Resolve Part No and device category before interpreting terminals.
3. Verify pin functional meaning using model-specific trusted documentation; NO/NC/COM, interlock/safety state and load conditions must be considered.
4. Do not assume the `P31019` (Source) -> `P31020` (Target) export direction is the direction of electric current.
5. Do not infer that terminals with similar designation share a continuous or healthy bus without topology/terminal data.
6. If any required semantic is unknown, request documentation and **STOP**; don't pursue adjacent electrical nodes merely because a conductor is listed.

### Demonstrated boundary
Confirmed: wiring record from VFD R1C to JB01:1:1. Not confirmed: that VFD supplies 24V to valve output, or that the same terminal electrically connects to JB01:1:2. Actual incident root cause remains separately confirmed by the user.

## Approval and integration plan

- **Proposal:** keep this as a separate review file. Do not change approval state in `Content/06_LEARNING_LOG.md` before the Technical Approver accepts the rules.
- After approval: append links/summary and explicit approval metadata to `Content/06_LEARNING_LOG.md`; amend relevant testing skill/catalog as required.
- Use `Tests/EDT-010_TROUBLESHOOTING_V2_1_EVIDENCE_GATE.md` to record a retest, raw Agent output, `PASS/PARTIAL/FAIL`, and approver decision.
