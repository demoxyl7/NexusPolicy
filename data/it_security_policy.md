# IT Security Policy: Data Protection

**Document Type:** Information Security Policy  
**Effective Date:** January 1, 2025  
**Applies To:** All Employees, Contractors, Vendors with System Access  
**Owner:** Chief Information Security Officer (CISO) / IT Security Team  
**Review Cycle:** Annual (or following any material security incident)  
**Classification:** Internal Use Only

---

## 1. Purpose and Scope

This IT Security Policy establishes the standards, requirements, and responsibilities governing the protection of the organization's information assets. It applies to all individuals who access company systems, networks, data, or devices — regardless of employment status, location, or the nature of the device used to connect.

Information security is not an IT problem alone. It is an organizational discipline that requires every employee's active participation. A single compromised account, one clicked phishing link, or one instance of improperly stored customer data can result in regulatory penalties, reputational damage, and real harm to the individuals whose data we hold. This policy exists to make secure behavior the default — not the exception.

Violations of this policy may result in disciplinary action up to and including termination, and may also result in civil or criminal liability depending on the nature of the breach.

---

## 2. Information Classification

Not all data carries the same level of risk. Understanding how information is classified is the first step in protecting it appropriately. The organization uses the following four-tier classification model:

**Tier 1 — Public:** Information intentionally made available to the public. No special handling required (e.g., marketing materials, published press releases).

**Tier 2 — Internal:** Information intended for use within the organization. Should not be shared externally without authorization (e.g., internal memos, org charts, operational procedures).

**Tier 3 — Confidential:** Sensitive business or personal information with restricted access. Must be encrypted in transit and at rest. Sharing requires explicit authorization (e.g., employee records, financial projections, client contracts, PII).

**Tier 4 — Restricted:** Highly sensitive data where unauthorized disclosure could cause severe legal, financial, or reputational harm. Subject to the strictest access controls (e.g., trade secrets, regulated health data, payment card data, authentication credentials).

Employees who are unsure of a document's classification level should contact their manager or the IT Security team before sharing or storing the information.

---

## 3. Password Policy and Rotation

### 3.1 Password Requirements

All passwords for company systems must meet the following minimum requirements:

- **Minimum length:** 14 characters
- **Complexity:** Must include at least one uppercase letter, one lowercase letter, one number, and one special character (e.g., !, @, #, $, %)
- **No reuse:** Employees may not reuse any of their last 12 passwords
- **No shared passwords:** Each account must have a unique password. Sharing credentials with colleagues — even temporarily — is prohibited
- **No dictionary words or personal identifiers:** Passwords may not contain your name, username, birthdate, or common words found in any dictionary

### 3.2 Mandatory 90-Day Password Rotation

All employee passwords for corporate systems — including email, VPN, SSO portals, and internal applications — must be rotated every 90 days. The system will prompt you to update your password before the expiration date.

**Important notes on password rotation:**

- You will receive automated reminders 14 days, 7 days, and 1 day before your password expires
- If you allow your password to expire, you will be locked out of the system and must contact the IT helpdesk to regain access
- Password rotation applies to all accounts, including service accounts managed by IT
- Do not increment passwords (e.g., Password2024, Password2025) — this is treated as reuse and will be flagged

### 3.3 Password Manager Requirement

Given the complexity and uniqueness requirements for passwords across multiple systems, the use of the company-approved password manager is strongly encouraged and, for roles with access to Tier 3 or Tier 4 data, mandatory. Approved password managers will be provisioned by IT. Personal or third-party password managers not approved by IT Security are not permitted for storing company credentials.

### 3.4 Multi-Factor Authentication (MFA)

MFA is mandatory for all corporate accounts. A second authentication factor — such as an authenticator app (preferred), SMS code, or hardware token — must be enrolled during IT onboarding and maintained throughout employment.

Employees who lose access to their MFA device must contact the IT helpdesk immediately. Under no circumstances should MFA codes be shared with anyone, including IT staff. IT personnel will never ask for your MFA code.

---

## 4. Phishing Simulation Protocols

### 4.1 Why We Run Simulated Phishing Campaigns

Phishing remains one of the most effective attack vectors used by malicious actors. According to industry data, more than 90% of successful cyberattacks begin with a phishing email. Our phishing simulation program is designed not to punish employees but to build real-world awareness and reduce the organization's risk exposure over time.

### 4.2 How Simulations Work

The IT Security team, in coordination with an approved third-party vendor, conducts unannounced phishing simulations on a rotating basis throughout the year. These simulations use realistic email templates — including spoofed sender addresses, urgent calls to action, and convincing branding — to mimic the tactics used in actual attacks.

Simulations are:

- **Unannounced:** Employees will not be given advance notice of when simulations occur. The element of surprise is essential to realistic testing.
- **Non-punitive for first-time clicks:** If you click a simulated phishing link, you will be redirected to an immediate educational landing page rather than penalized. The experience is designed to be instructive, not embarrassing.
- **Tracked for aggregate learning:** Results are reported at the department and team level, not the individual level, unless an employee demonstrates a pattern of repeated engagement with simulated phishing after completing remedial training.

### 4.3 What to Do When You Receive a Suspicious Email

If you receive an email that seems suspicious — whether during a known simulation period or any other time — follow the Report, Don't Click protocol:

1. Do not click any links or attachments
2. Do not reply to the email
3. Use the "Report Phishing" button in your email client (configured by IT) to flag the message
4. If you are unsure whether the "Report Phishing" button is available, forward the email as an attachment to phishing@company.com
5. If you accidentally clicked a link or entered credentials, report it to the IT Security team immediately at security@company.com or ext. 4911. Immediate reporting dramatically limits the impact of a real incident.

### 4.4 Remedial Training

Employees who click simulated phishing links are automatically enrolled in a short, self-paced online training module (approximately 20 minutes). This training must be completed within 5 business days. Employees who engage with multiple simulated phishing attempts in a 12-month period after completing remedial training may be subject to additional security awareness requirements, including mandatory in-person training, at the discretion of the CISO.

---

## 5. GDPR Compliance Requirements

The General Data Protection Regulation (GDPR) applies to the personal data of individuals located in the European Union and European Economic Area, regardless of where our organization is based. Employees who handle, process, or access personal data of EU/EEA residents must comply with the following requirements.

### 5.1 Key GDPR Principles

All personal data processing must adhere to these core principles:

**Lawfulness, Fairness, and Transparency:** Personal data may only be processed when there is a lawful basis — such as consent, contractual necessity, legal obligation, or legitimate interest. Individuals must be informed about how their data is used.

**Purpose Limitation:** Data collected for one specific purpose may not be repurposed without additional authorization or a new lawful basis.

**Data Minimization:** Collect only the data that is strictly necessary for the stated purpose. Avoid over-collection.

**Accuracy:** Personal data must be kept accurate and up to date. Employees should flag inaccuracies in customer or employee data promptly.

**Storage Limitation:** Personal data should not be retained longer than necessary. Follow the Data Retention Schedule maintained by the Legal and Compliance team.

**Integrity and Confidentiality:** Personal data must be protected against unauthorized access, loss, or destruction through appropriate technical and organizational security measures.

### 5.2 Employee Obligations Under GDPR

- Do not access personal data that you do not have a legitimate business reason to view
- Do not export, copy, or transfer personal data outside of approved systems without authorization
- Report any suspected personal data breach to the Privacy team within 24 hours of becoming aware of it — GDPR requires organizations to notify regulators within 72 hours
- Complete the annual GDPR awareness training module assigned via the Learning Management System (LMS)

---

## 6. CCPA Compliance Requirements

The California Consumer Privacy Act (CCPA), as amended by the California Privacy Rights Act (CPRA), grants California residents rights regarding their personal information. Employees in customer-facing roles or those who handle California resident data must understand and uphold these rights.

### 6.1 Consumer Rights Under CCPA

California residents have the right to:

- **Know** what personal information the company collects about them and how it is used
- **Delete** personal information collected about them (with certain exceptions)
- **Correct** inaccurate personal information
- **Opt-out** of the sale or sharing of their personal information
- **Limit** the use of sensitive personal information
- **Non-discrimination** — they may not be penalized for exercising their privacy rights

### 6.2 Handling CCPA Data Subject Requests

When a customer or employee submits a data subject request (also called a Data Subject Access Request, or DSAR), the request must be routed to the Privacy team immediately via privacy@company.com. The company has 45 days to respond. Do not attempt to fulfill data subject requests independently — all requests must be processed through the official workflow.

### 6.3 What Constitutes "Personal Information" Under CCPA

Under CCPA, personal information is broadly defined and includes: names, email addresses, IP addresses, purchase history, browsing behavior on company platforms, geolocation data, audio or video recordings, employment information, and inferences drawn from any of the above.

---

## 7. Acceptable Use of Company Systems

Company systems — including laptops, mobile devices, email, cloud storage, collaboration platforms, and network access — are provided for business purposes. Limited personal use is permitted provided it does not interfere with work performance, consume excessive resources, or expose the company to legal or security risk.

**Prohibited activities include, but are not limited to:**

- Accessing, transmitting, or storing content that is illegal, offensive, or violates company policies
- Using company systems to conduct personal business, freelance work, or side employment
- Installing unauthorized software or browser extensions
- Connecting to public Wi-Fi networks without using the company VPN
- Disabling or circumventing security controls, including antivirus software or endpoint detection tools
- Accessing systems or data beyond the scope of your job responsibilities (unauthorized access)
- Using AI tools or cloud applications not approved by IT to process Tier 3 or Tier 4 data

---

## 8. Incident Reporting

Security incidents must be reported promptly. An incident includes (but is not limited to): a lost or stolen device, a suspected phishing email that was clicked, unauthorized access to your account, discovery of data in an unexpected location, or any situation where confidential information may have been exposed.

**Report incidents to:** security@company.com | ext. 4911 (24/7)

Early reporting limits damage. Employees who promptly report incidents — even if they were involved in causing them — will be treated with greater leniency than those who delay or conceal incidents.

---

## 9. Policy Review and Contacts

**CISO Office:** ciso@company.com  
**IT Security Team:** security@company.com | ext. 4911  
**Privacy / GDPR / CCPA Inquiries:** privacy@company.com  
**IT Helpdesk (password resets, MFA issues):** itsupport@company.com | ext. 4357  

*Last Updated: January 2025 | Version 3.1 | Classification: Internal Use Only*
