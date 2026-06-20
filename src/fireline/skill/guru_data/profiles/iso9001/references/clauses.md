# ISO 9001:2015 Quick Clause Reference for 8D

> **Purpose:** Map every ISO 9001:2015 clause that touches the 8D process. When the agent detects an ISO 9001 context, this table drives clause-aware prompts at each D-step.

---

## Clause-to-8D Matrix

| Clause | Title | What It Means for 8D | D-Step |
|--------|-------|----------------------|--------|
| **4.4.1** | Quality Management System and Its Processes | The organization shall determine the processes needed for the QMS, their sequence and interaction. For 8D: root cause analysis must consider process interactions, not just isolated department actions. Use SIPOC or Turtle Diagram to locate where in the process chain the failure occurred. | D2, D4 |
| **5.1** | Leadership and Commitment | Top management shall demonstrate leadership by taking accountability for the effectiveness of the QMS. For 8D: D1 must identify who at management level owns the resources needed. If the corrective action requires capital or cross-functional coordination, leadership must be engaged — not just named, but actively involved in gate decisions. | D1, D5 |
| **6.1** | Actions to Address Risks and Opportunities | When planning the QMS, the organization shall determine risks and opportunities. For 8D: every corrective action is a change — it must be evaluated for new risks it introduces. Measures should be proportional to the potential impact of the nonconformity. | D0, D5, D7 |
| **7.1.5** | Monitoring and Measuring Resources | The organization shall ensure that the resources provided are suitable for the type of monitoring and measurement. For 8D: every measurement used in the investigation (dimensions, test data, SPC charts) must come from calibrated, verified equipment. If the gage is out of calibration, the data is invalid — D2 and D6 depend on this. | D2, D6 |
| **7.2** | Competence | The organization shall determine the necessary competence of persons doing work under its control, ensure they are competent, and retain documented information as evidence of competence. For 8D: D1 team members must have documented competence. If the root cause involves operator error, competence records of that operator must be checked. | D1, D4 |
| **7.5** | Documented Information | The QMS shall include documented information required by the standard plus that determined by the organization as necessary. For 8D: the 8D evidence package — not just the final report but all investigation records, test data, meeting minutes, and approval records — is documented information that must be controlled, identified, stored, protected, and retrievable. | D0-D8 |
| **8.5.6** | Control of Changes | The organization shall review and control changes for production and service provision to ensure continuing conformity. For 8D: any PCA that involves a process change is subject to this clause. The change must be reviewed before implementation, verified after, and documented with approved records. | D5, D6 |
| **8.7** | Control of Nonconforming Outputs | The organization shall ensure outputs that do not conform to requirements are identified and controlled to prevent unintended use or delivery. For 8D: D3 containment must satisfy 8.7 identification, segregation, and disposition requirements. Five disposition paths: rework, repair, concession, scrap, downgrade — each with distinct control requirements. | D3 |
| **9.1** | Monitoring, Measurement, Analysis and Evaluation | The organization shall evaluate the performance and the effectiveness of the QMS. For 8D: D6 verification data is a subset of this requirement. The organization shall analyze the data to evaluate effectiveness of corrective actions. | D6 |
| **9.2** | Internal Audit | The organization shall conduct internal audits at planned intervals. For 8D: the 8D's preventive actions (D7) should feed into internal audit checklists. Internal audits should verify that corrective actions remain effective over time. | D7, D8 |
| **9.3** | Management Review | Top management shall review the QMS at planned intervals. For 8D: significant or recurring 8D findings — especially those exposing systemic weaknesses — must feed into management review as input (9.3.2c: nonconformities and corrective actions). Management review outputs should include decisions on resources and actions to address systemic risks. | D7, D8 |
| **10.2** | Nonconformity and Corrective Action | The core clause for 8D. Requires: a) react to the nonconformity → control/correct it b) evaluate the need for action c) implement actions d) review effectiveness e) update risks and opportunities f) make changes to the QMS if needed. The 8D process is the implementation of 10.2. Each sub-item (a through f) maps to specific D-steps. | D0-D8 |
| **10.3** | Continual Improvement | The organization shall continually improve the suitability, adequacy, and effectiveness of the QMS. For 8D: D7 is not complete until lessons learned are embedded into the improvement system. This is broader than fixing one product's FMEA — it's about whether the QMS itself got better because of this 8D. | D7 |

---

## Clause Activation Logic (for Agent)

When the agent loads this ISO 9001 profile, activate clauses by trigger:

| Trigger | Activated Clauses |
|---------|-------------------|
| Nonconformity discovered | 10.2, 8.7 |
| Customer complaint received | 10.2.1, 8.7 |
| Internal audit finding | 10.2, 9.2 |
| Process change proposed (PCA) | 8.5.6, 6.1 |
| Measurement involved in investigation | 7.1.5 |
| Team formation (D1) | 7.2, 5.1 |
| Containment action taken (D3) | 8.7 |
| Root cause identified (D4) | 4.4.1, 6.1 |
| Corrective action selected (D5) | 8.5.6, 6.1, 7.5 |
| Verification data collected (D6) | 7.1.5, 9.1 |
| Preventive system updates (D7) | 10.3, 9.2, 9.3, 6.1 |
| Closure (D8) | 10.2.1 f), 7.5, 9.2, 9.3 |

---

## Clause Text Summary (for Quick Reference)

**4.4.1 Quality Management System and its Processes** — The organization shall determine the processes needed, their sequence and interaction, criteria and methods for effective operation, resources needed, responsibilities, and risks and opportunities.

**5.1 Leadership and Commitment** — Top management shall demonstrate leadership by taking accountability for the effectiveness of the QMS, ensuring the quality policy and objectives are established, promoting process approach and risk-based thinking, and ensuring resources are available.

**6.1 Actions to Address Risks and Opportunities** — The organization shall consider internal/external issues and interested party requirements when determining risks and opportunities. Actions shall be proportional to the potential impact on the conformity of products and services.

**7.1.5 Monitoring and Measuring Resources** — Where measurement is used to verify conformity, measuring equipment shall be calibrated or verified at specified intervals or before use, against measurement standards traceable to international or national standards. Calibration records shall be retained.

**7.2 Competence** — The organization shall determine the necessary competence of persons doing work that affects QMS performance and effectiveness, ensure these persons are competent (education/training/experience), take actions to acquire necessary competence, and retain documented information as evidence.

**7.5 Documented Information** — The QMS shall include standard-required documented information plus that determined by the organization as necessary for QMS effectiveness. When creating/updating, ensure appropriate identification, format, review, and approval. Control includes distribution, access, retrieval, use, storage, preservation, change control, retention, and disposition.

**8.5.6 Control of Changes** — The organization shall review and control changes for production or service provision to the extent necessary to ensure continuing conformity with requirements. Documented information describing the results of the review, persons authorizing the change, and any necessary actions shall be retained.

**8.7 Control of Nonconforming Outputs** — Nonconforming outputs shall be identified and controlled to prevent unintended use or delivery. The organization shall take action based on the nature of the nonconformity and its effect on conformity. This applies to product, service, and process outputs.

**9.1 Monitoring, Measurement, Analysis and Evaluation** — The organization shall determine what needs to be monitored and measured, the methods, when monitoring shall be performed, and when results shall be analyzed and evaluated. Results shall be retained as documented information.

**9.2 Internal Audit** — Internal audits shall be conducted at planned intervals. An audit program shall be established. Auditors shall not audit their own work. The responsible management shall ensure corrections and corrective actions are taken without undue delay.

**9.3 Management Review** — Top management shall review the QMS at planned intervals. Inputs include status of previous management review actions, changes in external/internal issues, process performance and product conformity, nonconformities and corrective actions, audit results, and resource adequacy.

**10.2 Nonconformity and Corrective Action** — When nonconformity occurs, the organization shall: a) react, control, correct, and deal with consequences b) evaluate the need for action to eliminate causes c) implement needed actions d) review effectiveness of corrective action e) update risks and opportunities f) make changes to the QMS if needed. Documented information shall be retained as evidence of: the nature of nonconformities, subsequent actions, and results of corrective action.

**10.3 Continual Improvement** — The organization shall continually improve the suitability, adequacy, and effectiveness of the QMS. The organization shall consider the results of analysis and evaluation, and the outputs from management review, to determine if there are needs or opportunities that shall be addressed.
