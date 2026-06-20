# Automotive 8D Complete Walkthrough

> **Scenario:** Brake caliper bracket — intermittent hole diameter undersized by 0.3mm on a CC characteristic.
> **Customer:** BMW Group
> **Tier:** Tier-1 supplier, machined casting bracket
> **Nonconformance:** Mounting hole diameter measured 9.70mm (spec: 10.00mm +/- 0.15mm), found at BMW assembly line during vehicle build. CC characteristic marked ▽ on BMW drawing no. B4711-34-200.
> **Lot affected:** 240 pieces across 3 production shifts (2026-05-14 to 2026-05-16, Bracket P/N BC-200-01).

---

## Profile Activation: IATF 16949 Profile Loads

The agent detects the problem context and activates the IATF profile:

```
[8D Guru — IATF 16949 Profile Active]
  OEM detected: BMW Group
  Characteristic type: CC (▽ on BMW drawing B4711-34-200)
  PPAP status: Pending lookup (prompt user)
  CSR active: BMW Group QMT CSR (2021)
  Timeline loaded: 24hr initial / 48hr containment / 10 working days final
```

The agent checks its references before proceeding:
- `references/oem-timelines.md` → BMW timeline confirmed: 24h initial, 48h D1-D3, 10wd final, GQTS portal, D/TLD check required.
- `references/characteristic-types.md` → CC (▽) = safety-critical, Cpk >= 1.67, error-proofing required, customer notification for any change.
- `references/clauses.md` → 8.3.3.3 (Special Characteristics), 8.3.4.4 (PPAP), 10.2.3 (Problem Solving), 10.2.4 (Error-Proofing), 10.3.1 (PFMEA review) all activated.

---

## D0: Prepare and Plan

**Agent prompts:**
- "What is the BMW complaint number and GQTS ticket ID?"
- "When was the complaint received? (Portal timestamp sets the 24-hour clock)"
- "Is this a repeat issue for this part number?"

**User provides:**
- GQTS Ticket: GQTS-2026-06145
- Received: 2026-06-18 09:15 CET
- Not a repeat issue. Clean complaint history on BC-200-01.
- BMW contact: Herr Muller, SQE Munich

**Agent sets the countdown:**
- Initial response due: 2026-06-19 09:15 CET (24h)
- D1-D3 containment due: 2026-06-20 09:15 CET (48h, likely satisfied by initial response if containment starts immediately)
- Final 8D due: 2026-07-02 09:15 CET (10 working days, note: check BMW calendar for German public holidays)

**Agent check:**
- The ⏇ is a CC characteristic → D/TLD check per BMW CSR.
- Agent prompts: "Is bracket BC-200-01 classified as D/TLD part? Check BMW drawing block."
- User confirms: Yes, D/TLD marked on drawing. Documentation retention: 15 years.

---

## D1: Team Formation

**Agent prompts for team composition:**
- Quality Engineer (8D leader)
- Manufacturing Engineer (process owner for CNC machining cell)
- Tooling Engineer (cutting tool management)
- Supplier Quality Engineer (sub-tier supplier contact for cutting inserts)
- Metrology Technician (measurement data)
- Customer Quality Engineer (BMW interface)

**Agent note:** For a CC characteristic defect on a D/TLD part, BMW expects the team to include a person with decision authority on tooling changes and PPAP resubmission. Include your Quality Manager.

---

## D2: Problem Description

**Is/Is Not Analysis (agent-structured):**

| Question | IS | IS NOT |
|----------|----|--------|
| What? | Mounting hole diameter 9.70mm (spec 10.00+/-0.15, LSL=9.85mm). 0.15mm below LSL. | No other hole undersized. Threaded holes on same bracket OK. |
| Where? | CNC Cell 4, Op 30 (finish boring), Bracket P/N BC-200-01. Detected at BMW Dingolfing assembly line, Station 47. | Not detected in-house at final inspection. |
| When? | Parts from 2026-05-14 to 2026-05-16. First detection at BMW on 2026-06-17. | Parts before 05-14 and after 05-16 within spec (confirmed by SPC data). |
| How many? | 240 pieces total across 3 shifts. 12 pieces confirmed undersized at BMW (5% of sample checked so far). Estimated 15-25% of lot affected based on SPC trend. | Remaining 180+ pieces not at BMW — some in transit, some at BMW warehouse. |
| Who? | Detected by BMW assembly line automatic gauging station. | Not detected by supplier final inspection (CMM sampling: 1 per 25 pieces, gauge R&R OK). |

**Problem statement (8D format):**
Bracket BC-200-01, mounting hole diameter (CC ▽) measured 9.70mm against specification 10.00+/-0.15mm (LSL=9.85mm). Detected at BMW Dingolfing assembly, Station 47, by automatic gauging on 2026-06-17. 240 pieces potentially affected across 3 production shifts (2026-05-14 to 2026-05-16). Nonconformance escaped supplier final inspection.

---

## D3: Containment Actions (Interim)

**Agent activates IATF 8.7.1 (Control of Nonconforming Outputs) and 10.2.5 (Warranty Management):**

**Immediate containment:**
1. All 240 pieces in the suspect lot flagged. BMW inventory: 48 pieces at Dingolfing — quarantined. In-transit: 72 pieces — recall to supplier or BMW quarantine (coordinated with BMW SQE). Supplier stock: 120 pieces — 100% inspection started within 2 hours of complaint receipt.
2. Sort method: Go/No-Go plug gauge at 9.85mm (LSL) + CMM verification on all borderline parts. All parts with diameter < 9.85mm: scrap. Parts 9.85-9.90mm: rework possible, pending BMW authorization.
3. Shipping hold on BC-200-01 effective immediately.
4. BMW notified within 24 hours: containment actions logged in GQTS.

**Agent prompt — Warranty exposure:**
"BMW CC characteristic with D/TLD classification. Calculate warranty exposure: how many brackets shipped to BMW in the 30 days before the suspect lot? Check shipment records for BC-200-01."
- User: 1,840 brackets shipped in the last 30 days. 240 in suspect window. Prior batches all passed SPC with Cpk > 1.33.

**Agent recommendation:** Even though prior batches appear OK, offer BMW a field inspection of the last 30 days' delivered inventory. BMW SQE may decline but the offer shows good faith and satisfies 10.2.5 diligence.

---

## D4: Root Cause Analysis

### 4M Change History

**Agent walks the 4M (Man, Machine, Material, Method) systematically:**

**Man:**
- 3 operators across 3 shifts. All certified on Cell 4. No new operators, no training gaps.
- Operator on shift 2 (05-15) noted increased tool wear alarm but reset and continued. No escalation.

**Machine:**
- CNC Cell 4, Op 30 (finish boring). Machine Cpk on this feature historically 1.38 (within spec but marginal).
- No machine maintenance events in the suspect window.
- No tool breakage events logged.
- **Key finding:** Cutting tool change interval was 800 pieces. Tool wear compensation enabled but not linked to SPC feedback.

**Material:**
- Bracket casting P/N BC-200-CAST from supplier CastTech GmbH, unchanged.
- **Key finding:** Cutting tool inserts changed supplier on 2026-05-10. Previous supplier: Sandvik (insert P/N 1234-X). New supplier: Tungaloy (insert P/N 5678-Y). The change was made under a cost-reduction initiative and was not flagged as a process change requiring PPAP notification because the insert was deemed "form-fit-function equivalent" by purchasing.

**Method:**
- CNC program unchanged. Cutting parameters same (speed, feed, depth of cut).
- Control Plan entry for mounting hole diameter: CMM check 1 per 25 pieces, Cpk calculation weekly.
- **Key finding:** Control Plan had no entry for tool wear monitoring linked to the CC hole diameter. Tool change was by piece count, not by trend.

### S1-S5: The Root Cause Chain

**Agent pushes from "tool wear" to true MRC (Manufacturing Root Cause):**

**S1: First Why —** Why was the hole diameter undersized?
- The finish boring tool insert wore faster than expected, reducing the effective cutting diameter. Tool wear compensation reached its limit and could no longer adjust.

**S2: Second Why —** Why did the tool insert wear faster than expected?
- The replacement insert from Tungaloy had different substrate and coating properties than the Sandvik insert. Under the same cutting parameters, the Tungaloy insert exhibited 40% higher wear rate on the cast iron bracket material.

**S3: Third Why —** Why was the insert change not evaluated for its effect on the CC characteristic?
- The purchasing department treated the insert as equivalent (same insert geometry on paper: ISO designation, nose radius, clearance angle). No cutting trial was performed. No tool life study was conducted. No PPAP impact assessment was triggered.

**S4: Fourth Why —** Why did the Control Plan not detect the tool wear trend before it produced out-of-spec parts?
- The Control Plan monitored hole diameter by CMM sampling (1 per 25), but Cpk was calculated only weekly. The deterioration occurred over 3 shifts — faster than the weekly review cycle. By the time the weekly Cpk check would have flagged it, 240 pieces had already been produced.

**S5: Fifth Why —** Why was tool change frequency not linked to the CC hole diameter in the Control Plan?
- **MRC identified:** The Control Plan treated the CC characteristic's monitoring (CMM check) separately from the process parameter that governed it (tool wear). There was no feedback loop: SPC data on hole diameter was not used to trigger tool change or tool wear inspection. The Control Plan was written for a stable process but did not account for input variation (supplier change of tool insert).

**Root Cause Summary:**
- **Root Cause 1 (Occurrence):** Cutting tool insert supplier changed without process validation. Tungaloy insert had different wear characteristics → accelerated tool wear → hole diameter drifted below LSL.
- **Root Cause 2 (Escape):** Control Plan lacked real-time SPC-to-tool-change feedback. Weekly Cpk calculation too slow to catch 3-shift deterioration trend. Final inspection sampling (1:25) missed the intermittent nature of the defect (tool wear at end of insert life on each shift).

**Agent activation — IATF clauses for D4 findings:**
- **8.4.2.1** (Supplier Control): The tool insert supplier change was not evaluated per supplier control requirements. Cost reduction did not follow the supplier change validation process.
- **8.5.1** (Control Plan): CC characteristic monitoring was too slow and not linked to process parameter (tool wear).
- **10.2.3** (Problem Solving): Both occurrence and escape root causes identified.

---

## D5: Permanent Corrective Actions

**Agent activates IATF 8.3.4.4 (PPAP), 8.5.6.1 (Control of Changes), and 10.2.4 (Error-Proofing):**

### PCA-1: Revert Tool Insert to Validated Source
- Immediate action: Replace all Tungaloy inserts with Sandvik inserts (original validated insert). 100% inspection of first 50 pieces after change — all within spec.
- **PPAP trigger:** Tooling change (insert supplier) = PPAP notification to BMW per 8.3.4.4. Since insert affects a CC characteristic, BMW notification is mandatory. Agent prompts: "Prepare PPAP notification package for BMW: updated PSW, dimensional report (100% of first 50 pieces, CC characteristic highlighted), updated Control Plan, tool life study data."
- **Change control:** Logged in internal change management system per 8.5.6.1. Production trial run completed (50 pieces, all OK).

### PCA-2: SPC-Triggered Tool Change Protocol
- New Control Plan entry for mounting hole diameter (CC):
  - **Monitoring method:** In-process SPC with real-time X-bar/R chart. Sample frequency: 5 pieces every 50 (increased from 1 per 25).
  - **Tool wear monitoring:** Tool wear compensation value trended on SPC chart alongside hole diameter.
  - **Reaction plan:** If X-bar approaches LSL within 1 sigma (9.92mm), automatic tool change triggered. Operators trained on new reaction plan.
  - **Cpk review frequency:** Shiftly (every 8 hours), not weekly. Cpk < 1.33 triggers immediate investigation.

### PCA-3: Supplier Change Validation Process
- Revised supplier change procedure: any change to cutting tool, insert, coating, or coolant requires a documented cutting trial on the specific part and material. Purchasing cannot authorize "equivalent" tool substitutions without Quality sign-off.
- Supplier quality engineer added to the change approval workflow for any tooling affecting CC or SC characteristics.

### PCA-4: Error-Proofing (IATF 10.2.4)
- The CNC program updated: if tool wear compensation exceeds 80% of available range, machine stops and requires operator intervention (poka-yoke — process cannot continue without active decision).
- In-process gauge: post-bore air gauge added to Cell 4 to measure every part (100% inspection). If hole diameter < 9.88mm (3-sigma warning limit), machine stops automatically.

---

## D6: Verification of Corrective Actions

**Agent activates IATF 8.5.6.1 (production trial), 10.2.4 (error-proofing test):**

### Red Rabbit / Challenge Parts
- 10 challenge parts prepared with hole diameters at 9.80mm, 9.82mm, 9.85mm (known bad), 9.88mm (warning), 9.92mm (marginal), and 10.00mm, 10.05mm (good).
- All challenge parts run through the updated process:
  - In-process air gauge correctly rejected all parts < 9.88mm (warning limit).
  - Go/No-Go gauge correctly separated good from bad.
  - Machine stop triggered when tool wear compensation exceeded 80%.
  - 3 borderline parts (9.85mm-9.87mm) flagged for review — process correctly identified them.

### Cpk Restoration
- 50-piece capability study run with Sandvik inserts and updated Control Plan.
- **Result: Cpk = 1.45** (up from 0.92 during defect period, up from historical 1.38). SPC charts stable, no special-cause variation.

### Production Trial Run
- 200 consecutive pieces produced under updated process.
- 100% dimensional inspection.
- Zero nonconforming parts. Cpk sustained at 1.41-1.48 across the run.
- **BMW requirement satisfied:** Production trial run data uploaded to GQTS.

### Verification Checklist
| Action | Method | Result | Status |
|--------|--------|--------|--------|
| Revert to Sandvik insert | 100% inspection, first 50 pcs | All within spec. Cpk 1.45. | OK |
| SPC-triggered tool change | SPC charting over 200-piece trial | Tool change triggered correctly at 1-sigma warning limit. No drift to LSL. | OK |
| Error-proofing (air gauge) | Red Rabbit challenge test | All 10 challenge parts correctly identified. Machine stop verified. | OK |
| Error-proofing (wear compensation) | Forced tool wear to 85% | Machine stopped. Operator intervention required. No bypass possible. | OK |
| Supplier change process | Documented process audit | New approval workflow in place. Quality sign-off required. | OK |

---

## D7: Preventive Actions (Systemic)

**Agent activates IATF 10.3.1 (PFMEA review), 8.5.1 (Control Plan update):**

### PFMEA Update (IATF 10.3.1)
Original PFMEA line for mounting hole diameter undersize:
- **Severity:** 9 (safety-critical — CC characteristic on braking system bracket)
- **Occurrence:** 3 (pre-change rating)
- **Detection:** 5 (CMM sampling 1:25, weekly Cpk)
- **RPN:** 135 → accepted below threshold of 150

Updated PFMEA:
- **Severity:** 9 (unchanged — CC characteristic severity is fixed)
- **Occurrence:** 2 (reduced — supplier change control now prevents unvalidated insert changes, tool wear monitoring provides warning)
- **Detection:** 3 (improved — 100% air gauge inspection, real-time SPC, machine stop at 80% wear)
- **RPN:** 54 → well below threshold

Additional failure mode added: "Tool insert supplier change without process validation" — previously not in PFMEA.
- Severity: 8, Occurrence: 2, Detection: 3 → RPN: 48

### Control Plan Updates
| Characteristic | Method | Frequency | Reaction Plan |
|---------------|--------|-----------|---------------|
| Mounting hole diameter (CC) | In-process air gauge (100%) | Every piece | Machine stop if < 9.88mm. Quarantine suspect parts. Notify shift leader. |
| Mounting hole diameter SPC | X-bar/R chart | 5 pcs / 50 | Tool change if X-bar within 1-sigma of LSL (9.92mm). Notify Quality Engineer. |
| Tool wear compensation | SPC trend | Continuous | Machine stop at 80% compensation range. Operator inspection required. |
| Cutting insert source | Receiving inspection — verify P/N, supplier | Each receipt | Non-approved supplier → reject. Notify Supplier Quality Engineer. |
| Tool change log | Operator entry | Each change | Cross-check with SPC trend. Investigate if change frequency deviates >20%. |

### Standardized Work Instructions
- Cell 4 work instructions updated: new reaction plan for tool wear alarm, new air gauge check procedure, new tool change logging requirement.
- Operator training completed for all 3 shifts. Training record filed.

### LPA Checklist Update (IATF 9.2.2.3)
- LPA item added: "Is the air gauge functioning? Verify with master part at start of shift."
- LPA item added: "Is the tool change log complete and signed?"

---

## D8: Closure and Customer Sign-Off

**Agent activates IATF 10.2.6 (Customer Complaints), 4.3.2 (CSRs):**

### BMW GQTS Submission
Full 8D package uploaded to BMW GQTS portal:
- D0-D8 documentation in BMW-required format
- PPAP notification for tooling change (insert reversion — level 3 notification)
- Capability study data (Cpk 1.45)
- Red Rabbit challenge test results
- Updated Control Plan
- Updated PFMEA (before/after)
- Production trial run data (200 pieces)
- Operator training records

### Customer Sign-Off
- BMW SQE (Herr Muller) reviews the 8D in GQTS.
- BMW requests additional data: Cpk trend over the next 4 production weeks to confirm sustained improvement.
- Agent prompt: "Set reminder: submit 4-week Cpk trend to BMW GQTS by 2026-07-30. Target: Cpk ≥ 1.33 sustained."
- BMW accepts the 8D with the follow-up condition. GQTS status: Closed with Monitoring.

### Lessons Learned (D8 Internal)
- **Supplier change control:** Cost-reduction initiatives involving any material or tooling that touches a CC characteristic must pass through the full PPAP change evaluation. "Form-fit-function equivalent" is not a purchasing decision — it is a quality decision.
- **SPC feedback loop:** Cpk calculated weekly is too slow for processes that can deteriorate within days. Shiftly Cpk review for CC characteristics.
- **Control Plan linkage:** Every CC product characteristic must have its governing process parameter (KCC) in the Control Plan with a linked reaction plan. The Control Plan must tell the operator: "If KCC does X, check the product CC and do Y."

### Documentation Retention
- D/TLD part → all 8D records retained for 15 years per BMW CSR.
- Records archived in quality system with D/TLD flag.

---

## Timeline Summary

| Milestone | Due Date | Actual | Status |
|-----------|---------|--------|--------|
| Initial response (24h) | 2026-06-19 09:15 | 2026-06-18 16:20 | Complete |
| D1-D3 containment (48h) | 2026-06-20 09:15 | 2026-06-19 14:00 | Complete |
| Final 8D (10 w.d.) | 2026-07-02 09:15 | 2026-06-28 10:00 | Complete |
| GQTS submission | 2026-07-02 09:15 | 2026-06-28 10:00 | Complete |
| BMW sign-off | — | 2026-06-30 14:30 | Closed with monitoring |
| 4-week Cpk follow-up | 2026-07-30 | — | Pending |

---

## Clause Coverage Summary

| IATF Clause | How It Was Applied |
|-------------|--------------------|
| 4.3.2 (CSRs) | BMW GQTS portal used, BMW 8D format, D/TLD documentation requirements met |
| 8.3.3.3 (Special Characteristics) | CC ▽ characteristic identified, escalated investigation and control |
| 8.3.4.4 (PPAP) | PPAP notification submitted for tooling change (insert reversion) |
| 8.3.5.2 (Error-Proofing Design) | Air gauge + tool wear compensation stop designed into process |
| 8.4.2.1 (Supplier Control) | Insert supplier change evaluation process revised |
| 8.5.1 (Control Plan) | Updated with linked KCC, real-time SPC, reaction plan |
| 8.5.6.1 (Control of Changes) | Tooling change validated via production trial, documented |
| 8.7.1 (Nonconforming Outputs) | Suspect product identified, quarantined, dispositioned |
| 9.2.2.3 (LPA) | LPA checklist updated with air gauge and tool change log check |
| 10.2.3 (Problem Solving) | 8D process followed with both occurrence and escape root causes |
| 10.2.4 (Error-Proofing) | Error-proofing effectiveness tested with Red Rabbit challenge parts |
| 10.2.5 (Warranty Management) | Warranty exposure analyzed, field inspection offered |
| 10.2.6 (Customer Complaints) | GQTS submission, BMW format, customer sign-off obtained |
| 10.3.1 (PFMEA Review) | PFMEA updated, RPN 135 → 54, new failure mode added |

---

## Agent Behavior Notes

This walkthrough demonstrates how the 8D Guru agent uses the IATF profile:

1. **Auto-activation:** When the user describes an automotive quality issue (OEM name, IATF reference, PPAP, PFMEA, CC/SC symbol, 8D context), the agent loads this profile and its three reference files.

2. **Clause-guided prompts:** At each D-step, the agent pulls the relevant clauses from `clauses.md` and prompts the user for clause-specific evidence. The agent does not just say "do D4" — it says "D4 requires both occurrence and escape root cause per 10.2.3, and check supplier control per 8.4.2.1. Let's walk through 4M and then use 5-Why."

3. **OEM-specific enforcement:** When the OEM is identified (BMW in this case), the agent enforces BMW-specific rules from `oem-timelines.md`: GQTS portal, 10 working day deadline, D/TLD check, German or English language.

4. **Characteristic-driven escalation:** When the agent sees "CC ▽", it escalates everything — faster containment, tighter Cpk requirements (1.67), error-proofing expectation, PPAP notification. The `characteristic-types.md` reference drives this behavior.

5. **S1-S5 discipline in D4:** The agent does not accept "tool wear" as root cause. It pushes through the full 5-Why chain until it lands on the systemic failure: the Control Plan gap that allowed the supplier change to escape validation. The MRC is what the organization will fix to prevent recurrence across all parts, not just this one.
