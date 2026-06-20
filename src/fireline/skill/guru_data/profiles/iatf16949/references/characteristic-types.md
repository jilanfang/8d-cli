# Special Characteristics Classification Reference

> **Purpose:** When the agent encounters drawing symbols, CSR designations, or customer classification terms for a characteristic, this table provides the definition, IATF basis, and control requirements. The agent uses this at D1 (to classify severity), D2 (to determine containment scope), and D5 (to select appropriate corrective action strength).

---

## Core Classification Table

| Classification | Symbol(s) | Definition | IATF Clause | Control Requirements | SPC / Cpk Requirements | Examples |
|---------------|-----------|------------|-------------|---------------------|----------------------|----------|
| **CC — Critical Characteristic** | ▽ (hollow triangle), ▲ (filled triangle), **CC**, **S/C** (Safety/Critical) | A product characteristic whose deviation from specification is likely to result in a hazardous condition, failure to comply with safety regulations, or a significant reduction in product safety performance. | 8.3.3.3 | 100% inspection or error-proofing required. Control Plan entry mandatory with reaction plan. Change requires customer notification and PPAP resubmission. | Cpk ≥ 1.67 (long-term), Ppk ≥ 1.67 (initial). 100% SPC charting where automated; manual charting at minimum frequency defined in Control Plan. | Brake line burst pressure, airbag deployment threshold, fuel system leak rate, steering column collapse force |
| **SC — Significant Characteristic** | ◇ (diamond), **SC**, **SIG**, **F/F** (Fit/Function) | A product characteristic whose deviation from specification affects fit, form, function, performance, durability, or customer satisfaction, but does not create a safety or regulatory risk. | 8.3.3.3 | Statistical process control with defined monitoring frequency. Control Plan entry required. Change may require customer notification depending on CSR. | Cpk ≥ 1.33 (long-term), Ppk ≥ 1.33 often expected. Some OEMs accept Cpk ≥ 1.00 with attribute inspection for certain characteristics. | Bearing journal diameter, connector pin retention force, NVH characteristic, coating thickness on appearance surface |
| **HIC — High Impact Characteristic** | **HIC**, **HI**, varies by OEM | OEM-specific classification: a characteristic that, if nonconforming, has a high impact on the customer's manufacturing process or end-user satisfaction, but does not meet the full safety/regulatory threshold of CC. Used primarily by GM and former GM-influenced supply chains. | 8.3.3.3 (under customer-specific approach) | Similar to SC but with higher visibility. Must appear on cross-functional sign-off. GM requires SQIE notification for HIC defects. | Cpk ≥ 1.33 minimum. GM GP-12 (Early Production Containment) usually applies during launch for HIC characteristics. | Engine mount bolt torque on assembly line (if it fails, line stops but no safety issue), door seal compression force |
| **PTC — Pass-Through Characteristic** | **PTC**, **PT**, sometimes marked with supplier's own symbol | A characteristic that is classified as CC or SC by a sub-tier supplier and passes through the organization unchanged to the customer. The organization inherits the control obligation and must verify it in receiving inspection or in-process. | 8.4.2.1, 8.3.3.3 | The organization must not degrade the control level applied by the sub-tier supplier. Receiving inspection must verify PTC at defined frequency. Control Plan must identify PTCs and their source. | Cpk requirements flow from the original classification (CC or SC). If the sub-tier supplier classified it as CC (Cpk ≥ 1.67), the receiving organization must maintain that standard. | Heat-treated fastener from supplier where hardness is a sub-tier CC; braking surface finish from casting supplier |
| **KPC — Key Product Characteristic** | **KPC** | Alternative terminology used by some OEMs (notably in Asia-Pacific supply chains) for CC or SC characteristics. Toyota, Honda, and Nissan-influenced supply chains often use KPC instead of CC/SC. | 8.3.3.3 (equivalent coverage) | Same as CC or SC depending on severity. Toyota: KPC is roughly equivalent to SC in terms of control; safety-critical items get separate "S" designation. | Cpk ≥ 1.33 typical for KPC. Toyota requires Cpk ≥ 1.33 for KPC, Cpk ≥ 1.67 for safety items. | As CC/SC above, depending on customer |
| **KCC — Key Control Characteristic** | **KCC** | A process parameter (not a product characteristic) whose variation significantly affects a CC or SC product characteristic. KCC is the process-side counterpart: if you want to control the product CC, you must control its KCC process parameters. | 8.5.1 (Control Plan), 10.3.1 (PFMEA) | Must be monitored in the Control Plan with defined target, tolerance, and reaction plan. SPC charting of process parameters (not just product outputs). | Process capability measured as Cpk of the process parameter against its control limits, not the product spec limit. | Furnace temperature for a hardness CC, injection pressure for a dimensional SC, weld current for a penetration CC |

---

## OEM-Specific Symbol Variations

| OEM / Group | CC Symbol | SC Symbol | Additional Symbols | Notes |
|-------------|-----------|-----------|-------------------|-------|
| **General Motors** | ▽ (hollow triangle with diamond border) | ◇ (diamond) | **HIC** — High Impact; **S/C** — Safety/Critical; **P** — Process (KCC equivalent) | GM uses a diamond-around-triangle for CC. Key Characteristics Designation System (KCDS) defines the full hierarchy. |
| **Stellantis** (FCA legacy) | ⬠ (pentagon / shield), **CC** | ◇ (diamond), **SC** | **SR** — Safety/Regulatory (above CC); **STD** — Standard (no symbol) | FCA used a shield/pentagon for CC. Post-merger Stellantis uses the merged CSR but some legacy drawings still show the shield. |
| **Stellantis** (PSA legacy) | **S** (safety), **F** (function) | — | **R** — Regulatory; **M** — Major (function); **m** — Minor | PSA used letter codes, not symbols. Legacy PSA drawings still circulate. |
| **Ford** | ▽ (hollow triangle) | ◇ (diamond) | **▽ (S)** — Safety Critical (triangle+S); **PTC** — Pass-Through; **YC** — Yellow Crayon (visual inspection key characteristic) | Ford's system is closest to AIAG standard. "Yellow Crayon" is a legacy term from paper-drawing days. |
| **BMW Group** | **D/TLD** marking, **CC** | **SC** | **D** — Documentation-required part (Dokumentationspflichtiges Teil); **TLD** — Safety/regulatory (Teile mit Lebensdauer-Dokumentation) | BMW uses D and TLD classifications alongside CC/SC. TLD parts require 15-year documentation retention. |
| **VW Group** | **D/TLD** (safety), **CC** | **SC** | **D** part documentation; **TLD** = Teil mit Lebensdauerdokumentation; **A** / **B** / **C** — former VDA classification (still seen on legacy drawings) | VW and BMW share D/TLD concept. VDA classification (A/B/C) is largely replaced but appears on older prints. |
| **Mercedes-Benz** | **CC** (with specific MB symbology) | **SC** | **Q-Relevant** — quality-relevant characteristic (broader than SC); **ZV** — Zuverlassigkeitsrelevant (reliability-relevant) | MB integrates with Daimler QAA (Quality Assurance Agreement) for characteristic management. |
| **Toyota** | **S** (safety) | **KPC** (Key Product Characteristic) | **P** — Process (KCC equivalent); **QC** — Quality Characteristic; **SQC** — Safety Quality Characteristic | Toyota does not use AIAG symbols. KPC and S markings appear on Toyota engineering drawings. Toyota typically expects poka-yoke for S characteristics. |
| **Honda** | **S** (safety) | **F** (function) | **Q** — Quality; **P** — Process | Simple letter-based system. Honda expects full traceability for S characteristics. |
| **Nissan** | **S** (safety) | **F** (function) | **S2** — Level 2 safety (torque-critical); **F2** — Level 2 function | Nissan's two-tier system adds a severity level number. |

---

## Default AIAG Symbol Hierarchy (North American Default)

When the customer CSR is silent on symbols, the AIAG (Automotive Industry Action Group) default applies:

```
  ▽   CC — Critical Characteristic (safety/regulatory)
  /\
 /  \

  ◇   SC — Significant Characteristic (fit/function/performance)
 /  \
 \  /
  \/

  P   Process Characteristic (KCC equivalent)

  PTC Pass-Through Characteristic
```

**AIAG Reference**: AIAG CQI-9, AIAG Advanced Product Quality Planning (APQP) Manual, AIAG Production Part Approval Process (PPAP) Manual, 4th Edition.

---

## How the Agent Uses This Reference

### D0-D1: Classification Detection
When a nonconformance is reported, the agent checks:
1. Is the characteristic marked on the drawing? What symbol?
2. What is the customer's symbol system? (Use OEM table above)
3. What control obligations does this classification trigger?

### D2: Containment Scope
- CC defect → immediate customer notification, suspect lot quarantine, possibly field containment.
- SC defect → internal containment, customer notified per regular timeline.
- KCC drift → process adjustment, product may not need containment if Cpk still above limit.

### D4-D5: Root Cause and Corrective Action Strength
- CC root cause → error-proofing strongly indicated. Detection-based controls alone insufficient.
- SC root cause → SPC improvement may be adequate. Error-proofing preferred but not required.
- KCC root cause → process control improvement (better monitoring, tighter limits, automated feedback).

### D7: FMEA and Control Plan Updates
- CC/SC characteristics require PFMEA updates with RPN review.
- KCC additions to Control Plan with defined reaction plan.
- PTC updates flow through to receiving inspection documentation.
