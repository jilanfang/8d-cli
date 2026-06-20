# ISO 9001 8D Complete Walkthrough

> **Scenario:** Food packaging line — intermittent seal integrity failure on retort pouches.
> **Industry:** Food packaging manufacturer, ISO 9001:2015 certified (non-automotive).
> **Nonconformance:** Retort pouch heat seal peeling at 0.8 bar pressure test (spec: must hold ≥ 1.2 bar). Found during in-process quality sampling 2026-06-15. Approximately 12% of samples failed over 3-day period.
> **Product:** Retort pouch P/N RP-500, 200g capacity, three-layer laminate (PET/Al/CPP).
> **Lot affected:** Approximately 45,000 pouches across 6 production shifts (2026-06-12 to 2026-06-15), Seal Station #3.

---

## Profile Activation: ISO 9001:2015 Profile Loads

The agent detects the problem context and activates the ISO 9001 profile:

```
[8D Guru — ISO 9001:2015 Profile Active]
  Industry: Food packaging (general manufacturing)
  Certification: ISO 9001:2015
  Nonconformance type: Process output deviation (in-process detection)
  Key clauses activated: 10.2 (Corrective Action), 8.7 (NCR Control), 8.5.6 (Change Control)
  Risk-based thinking: ON
```

The agent checks its references before proceeding:
- `references/clauses.md` → 10.2.1 a)-f) logic chain must close. 8.7 disposition paths must be documented. 7.1.5 measurement equipment must be calibrated.
- `references/risk-based.md` → Risk assessment framework (severity/occurrence/detection/scope/urgency/measurement confidence) activated.

---

## D0: Prepare and Plan — ISO 9001 Lens

**Agent prompts:**
- "Is this an external customer complaint, internal audit finding, or in-process detection? (10.2.1 a) — each path has different urgency and documentation requirements.)"
- "What is the severity of this failure? Is there a food safety risk if the seal fails in the field? (Risk matrix — safety > functionality > customer impact)"
- "When was the problem first observed? Who detected it? What was their immediate action?"

**User provides:**
- In-process detection — QC sampling at the bag-making station
- First observed: 2026-06-15, 10:30, by QC Inspector Zhang
- Immediate action: QC stopped release of the affected production lot; sampling frequency increased from 1/30min to 1/10min on Seal Station #3
- Not a food safety risk (pouch failed pressure test but no contamination detected; all retort-stage pouches already segregated), but a major functionality risk if undetected pouches entered the customer's retort process

**Agent risk assessment (D0):**
- Severity: 7 (major function loss — seal integrity)
- Occurrence: 5 (intermittent, 12% of samples, 3-day window)
- Detection: 4 (in-process QC caught it — but 1/30min sampling means up to 30min of production could have passed before detection)
- Scope: 45,000 pouches, 6 shifts, 1 seal station
- Urgency: Medium — in-process detection, not at customer yet, but product is held and cannot ship

**Agent sets action:**
- "This meets the criteria for formal corrective action per ISO 9001:2015 10.2.1 b) — functional nonconformity, >10% failure rate, over multiple shifts. A full 8D is warranted."

---

## D1: Team Formation — ISO 9001 Lens

**Agent prompts for team composition:**
- Quality Engineer (8D leader)
- Manufacturing/Process Engineer (seal station process owner)
- Maintenance Technician (seal station equipment knowledge)
- Material/Incoming Quality (laminate supplier interface)
- QC Inspector representative (front-line tester)

**Agent prompts for competence (ISO 9001:2015 7.2):**
- "Who on the team has training records on heat seal process troubleshooting? Is there a skill gap — does anyone understand the seal strength vs. temperature/time/pressure interaction?"
- "The QC Inspector doing the burst test — is their pressure test calibration current? Do they have documented competence for this test?"

**User provides:**
- Process Engineer Li has thermal process training records (updated 2025)
- QC Inspector Zhang has documented training on burst test method (SOP-QC-012, retrained 2026-01)
- No team member has formal root cause analysis training → Agent notes: "Gap identified per 7.2 b). 8D leader experienced from previous investigations will guide the team. This gap note goes into D8 for training needs input."

---

## D2: Problem Definition — ISO 9001 Lens

**Agent prompts for problem definition:**

1. **Process-method positioning (4.4.1):** "Where in the process flow did this failure occur? Let's use SIPOC: Supplier (laminate roll) → Input (laminate enters seal station) → Process (heat seal — temperature/time/pressure) → Output (sealed pouch at burst test) → Customer (retort processor). The failure point is at 'Seal Station #3 output.' Check process interfaces — is there an upstream or downstream interaction?"

2. **Measurement reliability (7.1.5):** "The burst test — pressure gauge serial number? Calibration due date? If the gauge is out of calibration, all failure rates are suspect."

3. **Is/Is-Not across process boundaries (4.4.1):**
   - What: Seal peel failure — IS on Seal Station #3; IS-NOT on Seal Station #1, #2, #4
   - Where: Seal seam center zone — IS 20-40mm from edge; IS-NOT at seal ends
   - When: IS June 12-15 (all 6 shifts); IS-NOT before June 12
   - Who (material): IS with Laminate Batch L-2406-03 and L-2406-04; IS-NOT with Batch L-2406-02 (consumed before June 12)
   - How Many: IS ~5,400 pouches failed (12% of 45,000); IS-NOT the other ~39,600 pouches

4. **NTF check (if applicable):** Agent notes: "Not applicable — failure reproduces on demand with burst test. However, if any samples pass burst test but fail at customer retort (higher temp), the issue would be latent. Consider testing at retort temperature."

**Agent temporal pattern detection:**
- The failure appeared suddenly on June 12 and persisted through June 15
- This is a "sudden step change" pattern → points to a specific change or event on or just before June 12
- Agent flags: "Check 4M change history for June 10-12. Look for: equipment maintenance, material batch change, temperature sensor replacement, shift handover anomaly."

---

## D3: Containment — ISO 9001 Lens

**Agent prompts for 8.7 nonconforming output control:**

1. **Five-window containment:** "For each of the five risk windows — customer site (not applicable, in-process detection), in-transit (held), inventory (finished goods warehouse check), WIP (at seal station), upstream (laminate roll stock) — what is the containment status and product disposition?"

2. **Disposition path selection (8.7.1):** "The 5,400 pouch failures: what disposition? Options per 8.7.1 — rework (can the seal be re-sealed to meet spec?), scrap (destroy if cannot be reworked), concession (sell as-is with customer approval?), downgrade (use for non-retort application?)."

**User provides:**
- 5,400 pouches already segregated in quarantine area with red tags (date/quantity/source/disposition/owner)
- Decision: Scrap — pouches cannot be re-sealed without risk of delamination. Batch L-2406-03 and L-2406-04 laminate rolls still in inventory (partially used) are quarantined pending root cause.
- Finished goods are quarantined pending 100% burst test at increased sampling (1/100 pouches)

**Agent checks (ISO 9001 overlay):**
- "Scrap disposition — is there a physical destruction process to ensure pouches don't re-enter production? (8.7.3 — physical segregation + verified destruction)"
- "Are you 100% sure the sampling increase to 1/100 pouches is adequate? What is the AQL? With 12% defect rate and random distribution, 1/100 sampling catches most — but if defects cluster within specific time windows, it could miss them. Consider 1/30min continuous sampling instead of batch-based."

**Agent risk note:** "The laminate rolls L-2406-03 and L-2406-04 are quarantined but NOT dispositioned yet. Hold this decision pending D4 — if root cause is in the seal process, the laminate may be fine. If root cause is in laminate material, these rolls may need to be returned to supplier per 8.7."

---

## D4: Root Cause — ISO 9001 Lens

**Agent prompts for 10.2.1 c) root cause determination:**

1. **Change analysis (6.3):** "Was there a change on or just before June 12? The Is/Is-Not says Seal Station #3 only, Laminate Batch L-2406-03 onwards only. Check: equipment maintenance log, temperature controller calibration, laminate incoming inspection records."

2. **Three-track root cause (10.2.1 c)):**
   - Track 1 — Occurrence: Why did the seal fail?
   - Track 2 — Non-detection: Why didn't the 1/30min QC sampling catch it faster? (30min gap)
   - Track 3 — Systemic: What process control weakness allowed this?

**Investigation findings:**
- **Equipment log:** Seal Station #3 had a thermocouple replaced on June 11 evening shift (maintenance work order WO-2406-118). The replacement thermocouple was installed but the temperature controller offset was not recalibrated. Actual seal jaw temperature was 8-12°C lower than indicated temperature.
- **Laminate analysis:** L-2406-03 and L-2406-04 had slightly thicker CPP layer (52μm vs. spec 50μm ±3μm — within spec but at upper limit). The combination of lower actual temperature + thicker CPP = insufficient heat penetration = weak seal.
- **Why didn't QC catch it:** 1/30min sampling at the bag-making station leaves a 30-minute window. The failure pattern was intermittent (occurred when both conditions met: lower temp + thicker CPP). During some 30min windows, no failures occurred. During others, failure rate was much higher than 12%.

**5-Why chain (Occurrence):**
1. Why did seal fail? → Insufficient heat at seal interface
2. Why insufficient heat? → Actual temperature 8-12°C lower than indicated
3. Why temperature lower? → Thermocouple replaced without controller recalibration
4. Why was recalibration missed? → Maintenance procedure MP-007 doesn't explicitly require controller recalibration after thermocouple replacement
5. Why doesn't the procedure require it? → The procedure was written for preventive maintenance (whole system calibration) not for individual component replacement

**5-Why chain (Non-detection):**
1. Why didn't 1/30min sampling catch it sooner? → 30min sampling interval is too long for intermittent failures
2. Why was 30min the sampling frequency? → Set based on historical Cpk > 2.0 for seal strength; not reviewed after process changes
3. Why wasn't sampling reviewed? → Control plan review frequency is annual; last review was 8 months ago

**Dual root cause (10.2.1 c)):**
- **TRC (Occurrence):** Temperature controller offset error after thermocouple replacement + upper-spec CPP thickness combined to reduce heat seal penetration
- **Escape Point:** QC sampling interval (1/30min) was inadequate for the actual failure pattern; sampling frequency was based on historical performance, not reviewed after maintenance events
- **MRC (Systemic):** Maintenance procedure MP-007 didn't include post-component-replacement calibration step; control plan review trigger didn't include maintenance-event-driven review

**Agent scoring (D4):**
- TRC complete: ✅ Physics mechanism clear (heat transfer → insufficient seal interface temp)
- Escape Point separate: ✅ Independent 5-Why chain to control point level
- MRC to system level: ✅ Traced to procedure deficiency + control plan review gap
- Falsification challenge: "If the thermocouple offset was the only cause, why did Station #1 and #2 not have the problem? Answer: Only Station #3 had the thermocouple replaced. If it was the CPP thickness alone, why before June 12 was L-2406-02 fine? Answer: L-2406-02 had CPP at 49μm (lower end of spec). The interaction required both conditions."

**Risk thinking check (6.1):** "Does this root cause suggest a broader risk? Any maintenance action that replaces a sensor/component in any station should trigger recalibration verification. This is not just a Station #3 issue — it's a maintenance procedure gap that affects all stations."

---

## D5: Corrective Actions — ISO 9001 Lens

**Agent prompts:**

1. **PCA-to-root-cause mapping (10.2.1 c)→e)):**
   | PCA | Corresponds to | Type |
   |-----|---------------|------|
   | Update MP-007 to mandate controller recalibration after any temperature sensor replacement + verification run of 10 pouches with burst test | MRC (procedure gap) | Elimination (procedure level) |
   | Add temperature verification step to shift-start checklist for all seal stations | TRC (detection of offset) | Detection |
   | Change QC sampling from 1/30min time-based to 1/100 pouches quantity-based + trigger: increase to 1/25 pouches for 2 hours after any maintenance event | Escape Point | Detection |

2. **Change control (8.5.6):** "The MP-007 revision and QC sampling change — do these go through your change control process? Who approves? Has the change been verified with a trial run?"

3. **Risk from the corrective actions (6.1):** "Changing QC sampling from time-based to quantity-based — does this affect QC workload? Does it require additional QC staffing? If QC misses a sample because they're overloaded, that's a new risk."

4. **Corrective action adequacy (10.2.1 e)):** "The measures match the severity (function-level failure, but not safety). Elimination of the procedure gap is the right level. Detection-level measures are appropriate as supplements."

**User provides:**
- MP-007 revision drafted, under change control CR-2406-052 with approvals from Mfg Eng, QA, Production
- Trial run on Seal Station #3 after recalibration: 100 pouches, all passed burst test at ≥ 1.3 bar
- QC workload assessed: the new sampling plan increases QC workload by approximately 15% during post-maintenance periods; QC Manager approved additional coverage

---

## D6: Verification — ISO 9001 Lens

**Agent prompts:**

1. **Measurement equipment check (7.1.5):** "Burst test pressure gauge — calibration check before using verification data. Gauge ID? Calibration due date?"

2. **Verification data sufficiency (9.1.1):**
   - "What's the post-correction seal strength Cpk?"
   - "How many production conditions were covered in verification?"
   - "Red Rabbit test: did you intentionally install an uncalibrated thermocouple to verify the new checklist catches it?"

**User provides:**
- Pressure gauge PT-007: calibrated 2026-05-20, valid through 2026-11-20 ✅
- Post-correction data: Cpk = 1.52 (target ≥ 1.33), 3 production shifts, 2 laminate batches
- Red Rabbit test: Maintenance intentionally installed a known-offset thermocouple on Station #3 (controlled test). Shift-start checklist caught it — temperature reading 9°C below expected, flagged before production started. ✅
- Verification covered: shift change (3 shifts), batch change (2 different laminate batches), but equipment restart condition not covered

**Agent flags:** "Equipment restart condition after weekend shutdown not yet verified. Please add to verification plan. This is a boundary condition — temperature controllers may behave differently on cold start."

---

## D7: Prevention — ISO 9001 Lens

**Agent prompts:**

1. **Similar potential nonconformities (10.2.1 e)):** "Scan all seal stations (#1, #2, #4) and all maintenance procedures that involve sensor/component replacement. Does MP-007 apply to other equipment with similar risk?"

2. **Risk assessment update (6.1.2 a)):** "PFMEA — Seal Station heat seal process. Before this 8D, what was the RPN for 'thermocouple offset'? Was this failure mode even identified?"

3. **Internal audit linkage (9.2.2 e)):** "This problem exposed a maintenance procedure gap and control plan review gap. Should the next internal audit specifically check maintenance procedures for post-replacement calibration requirements?"

4. **Management review input (9.3.2 c)):** "This 8D found a systemic gap. Should it be reported at the next management review as a 'process control effectiveness' input?"

**User provides:**
- Scan complete: 4 other maintenance procedures (flow meter, pressure sensor, UV lamp, tension controller) do NOT have post-replacement calibration steps. All updated via separate change controls.
- PFMEA: The 'thermocouple offset' failure mode was previously rated as Occurrence=2 (remote); inspection revealed it's Occurrence=5 (intermittent). RPN updated from 40 to 75 (Severity=5, Occurrence=5, Detection=3). Control method upgraded from 'SPC monitoring' to 'SPC monitoring + shift-start verification checklist.'
- Internal audit: Lead auditor added 'post-maintenance calibration verification' to the Q3 2026 manufacturing process audit checklist.
- Management review: 8D summary prepared for Q3 2026 management review package (trend input: maintenance procedure gap frequency).

---

## D8: Closure — ISO 9001 Lens

**Agent prompts:**

1. **Effectiveness review (10.2.1 f)):** "Has the effectiveness of corrective actions been reviewed? What is the basis for confirming the root cause has been eliminated?"

2. **Documented information finalization (7.5):** "The 8D evidence package — does it include all investigation records, test data, meeting minutes, and approval records? Are all files properly identified, versioned, and stored?"

3. **Uncertainty declaration:** "What are we still not certain about? Honestly declare."

4. **Internal audit tracking (9.2):** "Register this 8D closure as a verification item for the next internal audit — the auditor should verify: a) MP-007 is being followed, b) shift-start checklists show temperature verification, c) QC sampling plan is in effect."

**User provides:**
- Effectiveness review: 30-day post-corrective action data shows zero seal failures, Cpk stable at 1.48-1.55 across all stations
- Documented information: 8D evidence package saved to QMS document management system (QMS-DMS/8D/2026/8D-0615), all referenced files linked, document register updated
- Uncertainty: "We cannot yet confirm the cold-start verification condition — scheduled for July 2026 shutdown restart. Pending, but not blocking closure."
- Closure signed: QA Manager, Manufacturing Manager, Process Engineer

**Agent closure confirmation:**
"ISO 9001:2015 10.2 logic chain closed: a) Response ✅ → b) Action warranted ✅ → c) Actions implemented ✅ → d) Effectiveness reviewed ✅ → e) Risks updated (PFMEA + maintenance procedures) ✅ → f) QMS changes made (MP procedures updated, internal audit checklist updated, management review input prepared) ✅."

---

## Post-8D: What Was Different Because of ISO 9001 Profile

| Element | Without ISO 9001 Profile | With ISO 9001 Profile |
|---------|------------------------|----------------------|
| D0 | Basic risk matrix | Risk matrix + process source classification (10.2.1 a)) + action justification (10.2.1 b)) |
| D1 | RACI only | RACI + competence evidence (7.2) + skill gap identification |
| D2 | Is/Is-Not | Is/Is-Not + process method positioning (4.4.1) + measurement reliability check (7.1.5) |
| D3 | Containment | Containment + five disposition paths (8.7.1) + disposition documentation (7.5.3) |
| D4 | TRC + MRC + EP | TRC + MRC + EP + change analysis (6.3) + process interaction analysis (4.4.1) |
| D5 | PCA matrix | PCA-to-root-cause mapping + change control (8.5.6) + risk from PCA (6.1) + adequacy check (10.2.1 e)) |
| D6 | Cpk + Red Rabbit | Cpk + Red Rabbit + measurement equipment check (7.1.5) + verification coverage analysis (9.1.1) |
| D7 | Yokoten + FMEA | Yokoten + FMEA + internal audit linkage (9.2) + management review input (9.3) + organizational knowledge (7.1.6) |
| D8 | Team sign-off | Effectiveness review (10.2.1 f)) + documented information (7.5) + uncertainty declaration + internal audit verification item |
