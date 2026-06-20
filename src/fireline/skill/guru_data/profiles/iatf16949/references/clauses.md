# IATF 16949:2016 Quick Clause Reference for 8D

> **Purpose:** Map every IATF clause that touches the 8D process. When the agent detects an automotive context, this table drives clause-aware prompts at each D-step.

---

## Clause-to-8D Matrix

| Clause | Title | What It Means for 8D | D-Step |
|--------|-------|----------------------|--------|
| **4.3.2** | Customer-Specific Requirements (CSRs) | Before opening the 8D, check which CSR document applies. Timeline, template, and special-characteristic symbols all flow from the OEM's CSR. If the CSR mandates a specific portal or format, the 8D must comply from D0. | D0, D8 |
| **8.3.3.3** | Special Characteristics | The drawing or spec marks CC/SC symbols. The 8D must identify whether the nonconformance affects a special characteristic. If it does, the investigation depth, containment speed, and sign-off authority all escalate — CC defects typically require customer notification and PPAP resubmission. | D1, D2, D4 |
| **8.3.4.4** | Product Approval Process (PPAP) | If the root cause or corrective action changes product or process design, PPAP re-submission is triggered. The 8D must reference the original PPAP submission (PSW date, level) and assess whether the change requires a new submission. | D5, D6, D7 |
| **8.3.5.2** | Manufacturing Process Design Output (Error-Proofing) | Error-proofing must be designed into the process, not bolted on after. When D5 selects error-proofing as the corrective action, the 8D must verify that the solution meets the design-output requirements from this clause — poka-yoke by design, not by inspection. | D5 |
| **8.4.2.1** | Supplier Type and Extent of Control | If root cause traces to a purchased component or subprocess, this clause governs how the supplier must be controlled. The 8D must assess whether the supplier's current control level was adequate and whether escalation is needed. | D4, D5 |
| **8.4.2.4** | Supplier Monitoring | When supplier performance caused the problem, the 8D must reference existing monitoring indicators and determine why they failed to catch the issue. PPM, on-time delivery, and SCAR history are the entry points. | D4 |
| **8.4.2.4.1** | Second-Party Audits | If the supplier's root cause points to systemic weakness, a second-party audit may be the chosen permanent action. The 8D documents the audit scope and findings, then tracks closure. | D5, D6 |
| **8.5.1** | Control of Production (Control Plan, Standardized Work) | The Control Plan is the beating heart of D7. Every permanent corrective action must map back to an updated Control Plan entry with the characteristic, method, frequency, and reaction plan. Standardized work instructions must be revised if the corrective action changes operator tasks. | D7 |
| **8.5.6.1** | Control of Changes — Supplemental | Any process change made as a corrective action must go through the organization's change-control system. This clause requires that change validation includes production trial runs (Red Rabbit, boundary samples). | D5, D6 |
| **8.7.1** | Control of Nonconforming Outputs | D1-D3 containment actions must satisfy the requirements of this clause: identification, segregation, disposition. The 8D must document how suspect product was quarantined and what disposition was applied (rework, scrap, use-as-is with customer authorization). | D1, D2, D3 |
| **9.2.2.3** | Manufacturing Process Audit (Layered Process Audit / LPA) | The 8D should cross-check D4 findings against recent LPA results. If the LPA missed the failing condition, the LPA checklist itself may need revision — that is part of D7 preventive action. | D4, D7 |
| **10.2.3** | Problem Solving (8D) | The clause that mandates structured problem solving. It requires: documenting the problem, containing it, identifying root cause, implementing corrective action, verifying effectiveness, and feeding lessons back into FMEA and Control Plan. Every D-step must satisfy the evidence standard this clause implies. | D0-D8 |
| **10.2.4** | Error-Proofing | When D5 selects error-proofing, this clause requires: the method must be verified during implementation, a control plan entry must exist, and the effectiveness test must include challenge parts. D6 verification must explicitly test the error-proofing device. | D5, D6 |
| **10.2.5** | Warranty Management | If the nonconformance could affect warranty (safety, durability), the 8D must include a warranty exposure analysis. How many units in the field? Over what production window? What is the failure consequence? This feeds D1 containment breadth and D8 customer negotiation. | D1, D4, D8 |
| **10.2.6** | Customer Complaints and Field Failure Test Analysis | The customer's complaint is the input to D0. This clause requires: timely response, use of the customer's designated format, and field-failure part analysis where applicable. The 8D must return parts to the customer if requested and document the analysis. | D0, D4 |
| **10.3.1** | Continual Improvement — PFMEA Review | D7 is not complete until the PFMEA is reviewed and updated. This clause requires that the organization use the 8D finding to re-evaluate RPNs, add previously unidentified failure modes, and confirm that detection and prevention controls are effective. | D7 |

---

## Clause Activation Logic (for Agent)

When the agent loads this IATF profile, it should activate clauses by trigger:

| Trigger | Activated Clauses |
|---------|-------------------|
| Customer complaint received | 10.2.6, 4.3.2 |
| Safety or regulatory characteristic involved | 8.3.3.3, 10.2.5 |
| Root cause traced to supplier | 8.4.2.1, 8.4.2.4, 8.4.2.4.1 |
| Process change proposed (PCA) | 8.3.4.4, 8.5.6.1 |
| Error-proofing selected as PCA | 10.2.4, 8.3.5.2 |
| Control Plan updated (D7) | 8.5.1, 10.3.1 |
| Verification / Red Rabbit | 8.5.6.1, 10.2.4 |
| Customer sign-off (D8) | 10.2.6, 8.3.4.4 |

---

## Clause Text Summary (for Quick Reference)

**4.3.2 Customer-Specific Requirements** — The organization shall include all CSRs in the scope of its QMS. If the customer says "use portal X, respond within Y hours," the QMS must reflect that.

**8.3.3.3 Special Characteristics** — The organization shall use a multidisciplinary approach to identify special characteristics. The symbol system (▽, ◇, etc.) comes from the customer; if the customer does not define symbols, the organization defines them.

**8.3.4.4 Product Approval Process** — PPAP shall be performed for all products. The organization shall maintain a PPAP status log. Any change that affects fit, form, function, performance, or durability triggers re-submission.

**8.3.5.2 Manufacturing Process Design Output** — The output shall include error-proofing methods for all operations where risk assessment indicates it is necessary.

**8.5.6.1 Control of Changes** — The organization shall control production process changes. The organization shall verify that any process change resulted in the desired effect. Production trial run results shall be documented.

**10.2.3 Problem Solving** — The organization shall have a documented process for problem solving. The process shall include defined approaches for identifying root cause. The corrective action shall eliminate the root cause.

**10.2.4 Error-Proofing** — The organization shall have a documented process for determining the use of error-proofing. The effectiveness of error-proofing shall be tested.

**10.3.1 Continual Improvement** — The organization shall review and update the PFMEA as part of continual improvement.
