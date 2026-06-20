# Mona AI Hackathon 2026

10 AI agent prototypes built in one day for real companies across the Saarland region.
Each tool runs entirely in the browser — no installation, no server, no technical knowledge required.

**Built with:** Claude AI (Anthropic) · Python FastAPI · HTML/JS
**GitHub:** [haniasid07/mona-hackathon-2026](https://github.com/haniasid07/mona-hackathon-2026)

---

## The 10 Problems

### 1. Invoice Processing Automation
**Client:** Globus Group (St. Wendel)

Automatically reads supplier invoices (PDF, PNG, DOCX) and routes them to the right department. Extracts vendor, amount, VAT, due date, and generates a compliance audit trail. Processes 10 real sample invoices across IT, Finance, Facilities, Marketing and more.

→ `problem1_invoice_processor.html`

---

### 2. Shift Replacement Agent
**Client:** Universitätsklinikum des Saarlandes / UKS (Homburg)

Last-minute sick call at 18:30 — night shift starts at 19:00. The agent reads a 100-person hospital roster, checks qualifications, rest time, weekly hour limits, and availability, then ranks eligible staff and writes a personalised WhatsApp outreach message in one click.

→ `problem2_shift_replacement.html`

---

### 3. Work Permit Validator
**Client:** Leistenschneider Personaldienstleistungen GmbH (Saarbrücken)

Upload any German residence or work permit PDF. The agent validates it against today's date, checks whether employment is actually permitted, extracts all key fields, and returns a confidence score. Tested against 4 sample permits (2 valid, 2 invalid).

→ `problem3_work_permit.html`

---

### 4. Certificate & CV Fraud Detector
**Client:** Persowerk Deutschland GmbH (Saarbrücken)

Upload a certificate or CV image. The agent analyses it for AI-generation artifacts, font inconsistencies, implausible issuers, missing seals, and date anomalies — returning an authenticity score, AI-generation probability, flagged red flags, and an HR recommendation.

→ `problem4_certificate_fraud.html`

---

### 5. Interview Question Generator
**Client:** Kohlpharma GmbH (Merzig)

Paste any job description or pick from 3 real sample roles (Hiring Manager, GTM Engineer, Forward Deployed Engineer). The agent generates 8 tailored technical questions, 5 behavioural questions, 6 red flags to watch for, and a suggested opening line — all explained in plain English for non-technical hirers.

→ `problem5_interview_generator.html`

---

### 6. Marketing Content / Filmmaker Agent
**Client:** Dr. Theiss Naturwaren GmbH (Homburg)

Pick a hero product, content angle (ASMR ritual, post-workout recovery, before/after, etc.), platform (TikTok / Instagram), and duration (15s / 30s / 60s). The agent generates a full scene-by-scene storyboard, safe zone preview, HWG compliance check, and ready-to-paste caption with hashtags.

→ `problem6_filmmaker_agent.html`

---

### 7. Customer Analytics Agent
**Client:** Dr. Theiss Naturwaren GmbH (Homburg)

Four-tab analytics tool: segment analysis (RFM profiles, behavioural patterns, optimal send windows), targeting signal generator (best channels, creative hooks, timing), campaign lift measurement (A/B test interpreter), and a free-text query interface for any customer/targeting question.

→ `problem7_customer_analytics.html`

---

### 8. Dynamic Pricing Agent
**Client:** Dr. Theiss Naturwaren GmbH (Homburg)

Signal-driven pricing engine for 12 Allgäuer Latschenkiefer products. Adjusts price within a ±12% guardrail band based on weather, seasonal/religious events, football fixtures, supply chain status, and competitor movements. Includes full audit log and German pharmacy RPM compliance.

→ `problem8_dynamic_pricing.html`

---

### 9. Competitive Gap Analysis Agent
**Client:** Dr. Theiss Naturwaren GmbH (Homburg)

Maps Allgäuer Latschenkiefer's product range against 10 competitors across a need × format grid. Surfaces white-space opportunities where competitors are present but the brand is absent, scored by priority, brand fit, and market size. Includes positioning weaknesses and quick wins.

→ `problem9_competitive_gap.html`

---

### 10. Prompt-Injection-Resistant Email Agent
**Client:** Rheinmetall AG (cross-account)

Secure applicant processing agent that sandboxes all untrusted email content inside labelled XML tags — injected instructions inside CVs or email bodies cannot escape to affect system behaviour. Checks for all 3 required documents (CV, work/residence permit, criminal record statement) and flags security threats. Built in response to a real prompt injection incident.

→ `problem10_secure_email_agent.html`

---

## How to run any tool

1. Download the `.html` file
2. Open it in any browser (Chrome, Firefox, Edge)
3. That's it — no server, no installation needed

Each tool calls the Claude API directly from the browser.

---

## Tech stack

| Layer | Technology |
|---|---|
| AI backbone | Claude Sonnet 4.6 (Anthropic) |
| Backend | Python · FastAPI · uvicorn |
| Frontend | Vanilla HTML · CSS · JavaScript |
| Document parsing | pypdf · pdftotext · openpyxl |
| Deployment | GitHub (static HTML files) |

---

*Built at Mona AI Hackathon 2026 — Saarbrücken, 20 June 2026*
