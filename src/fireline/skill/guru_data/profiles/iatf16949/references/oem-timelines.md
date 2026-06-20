# Major OEM 8D Response Timeline Requirements

> **Purpose:** When the agent identifies the customer OEM, this table provides the hard deadline data needed at D0. The agent uses this to set countdown clocks and to prompt the user when a deadline is approaching.

---

## OEM Timeline Table

| OEM | Initial Response | D1-D3 Containment | Final 8D (D4-D7) | Submission Portal / System | Special Requirements | CSR Version / Source |
|-----|------------------|-------------------|------------------|---------------------------|---------------------|----------------------|
| **Stellantis** (FCA/PSA) | 24 hours | 48 hours | 10 working days | **eCIMS** (Electronic Customer Issue Management System) | NTF process required per CSR section 9.0; must use Stellantis 8D template; IC (Immediate Containment) must be verifiable at customer site. PI (Process Improvement) must show PFMEA and CP updates. | CSR June 2020 |
| **General Motors** | 24 hours | 48 hours | 10 working days | **GM Supply Power** (SPS) / **PRR** module | Must classify as PR&R (Product Reporting & Resolution) or SPPS (Supplier Product Problem Solving). D3 must include "suspect part identification" (SPI) tag method. If CC/SC, requires SQIE notification. NTF requires specific investigation per GP-5. | GM CSR Rev. 12 (Dec 2020) |
| **BMW Group** | 24 hours | 48 hours | 10 working days | **GQTS** (Global Quality Tracking System) | 8D must be submitted in German or English. BMW-specific 8D format mandatory. For safety-critical issues: additional QZ (Qualitatszentrum) review. D6 verification must include production trial run data. If CC characteristic, 0-km and field analysis required. | BMW Group QMT CSR (2021) |
| **Ford Motor Company** | 24 hours | 48 hours | 10 working days | **GSAR** (Global Supplier Assessment Report) / **Pulse** | Must use Ford 8D format. D4 must include: Is/Is Not, Change Point Analysis (4M), and why-made/why-escaped root cause. If escape point is in supplier's process, corrective action must address detection as well as prevention. Q1 consequence if repeat issue. PTC (Pass-Through Characteristic) identification mandatory. | Ford CSR Rev. 4.2 (2021) |
| **Volkswagen AG** | 24 hours | 48 hours | 10 working days | **QPN / KPM / DoE Portal** (varies by VW brand: VW, Audi, Porsche, Seat, Skoda) | D3 must include D/TLD (Dokumentationspflichtiges Teil / Safety-critical part) check. If D/TLD part: special documentation retention (15 years). 8D in German or English. VDA field failure analysis requirements apply. Error-proofing verification must follow VDA 4. | VW Formel Q Konkret (2019) |
| **Mercedes-Benz** (Daimler) | 24 hours | 48 hours | 10 working days | **SMART** (Supplier Management and Reporting Tool) | 8D submission language: German or English. D6 requires capability study (Cpk/Ppk ≥ 1.67 for CC characteristics). Additional QAA (Quality Assurance Agreement) requirements may apply. Repeat issues within 12 months trigger escalation to Q-Help process. | MB Special Terms 2020 |
| **Toyota** | 24 hours | Immediate (1 working day) | 15 working days | **T-QMS** (Toyota Quality Management System) / Direct report to SQA engineer | Follows Toyota Business Practices (TBP) problem-solving, not strictly 8D — but 8D format accepted. Genchi Genbutsu (go-and-see) strongly preferred. D4 must include physical part analysis on-site at Toyota location if possible. A3 summary expected alongside full report. Poka-yoke verification (D6) must be demonstrated with physical challenge test. | Toyota SQAM Rev. H (2022) |

---

## Timeline Triggers in Context

### Clock Starts When
The initial-response clock starts when the customer formally logs the complaint in their portal. The agent should prompt the user: "When did the customer notification arrive? Portal timestamp?" The answer sets the countdown.

### What "Initial Response" Means
- Acknowledge receipt of the complaint.
- Confirm that you have the affected part / lot numbers.
- State that containment has begun or will begin by [time].
- Provide contact name and internal tracking number.

### Escalation Thresholds
- **Safety/regulatory issue**: Timelines may compress; some OEMs require 8-hour D1-D3.
- **Repeat issue (same part, same failure mode within 12 months)**: May trigger Q1 (Ford), Q-Help (MB), or New Business Hold (GM).
- **Field action / recall**: Not covered by standard 8D timelines; OEM-specific recall procedures apply.

---

## Quick-Lookup: OEM by Detection Pattern

The agent can use these signals to identify the OEM when the user has not stated it explicitly:

| Signal | Likely OEM |
|--------|-----------|
| "PR&R" or "PRR" in complaint | General Motors |
| "GSAR" in complaint | Ford |
| "GQTS" portal reference | BMW |
| "eCIMS" portal reference | Stellantis |
| "D/TLD" requested | VW Group |
| "T-QMS" or "SQAM" reference | Toyota |
| "QAA" referenced | Mercedes-Benz |

---

## Special Requirements Detail

### NTF (No Trouble Found) Handling
- **Stellantis**: NTF must be investigated per CSR section 9.0. Cannot close as NTF without customer concurrence.
- **GM**: GP-5 NTF investigation required. Includes: electrical test data, environmental conditions at time of incident, warranty data cross-check.
- **Ford**: NTF classification only after full investigation and customer QE approval. Parts must be returned to supplier for further analysis.
- **All OEMs**: NTF rate > threshold triggers separate corrective action process. NTF is a quality indicator, not a defense.

### Repeat Issue Rules
- **GM**: Same part + same failure mode in 12 months = PR&R escalation level increased.
- **Ford**: Repeat within 12 months = Q1 escalation. Repeat within 6 months = CS1 (Controlled Shipping Level 1).
- **BMW**: Repeat within 15 months = QMT escalation and potential chargeback for investigation costs.
- **VW**: Repeat within VDA escalation (typically 12 months) = KRI (Kritische Reklamation) classification.
- **Mercedes-Benz**: Repeat within 12 months = Q-Help process.
- **Toyota**: Repeat treated seriously; SQA engineer escalation; may require on-site resident engineer.
