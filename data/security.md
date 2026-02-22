# Security Policy: Physical and Digital Security Standards

**Document Type:** Information and Physical Security Policy
**Effective Date:** January 1, 2025
**Applies To:** All Employees, Contractors, and Authorized Visitors
**Owner:** Chief Information Security Officer (CISO) / Facilities Security
**Review Cycle:** Annual (or following any material security incident)
**Classification:** Internal Use Only

---

## 1. Purpose and Security Philosophy

Security is a shared responsibility. No firewall, badge reader, or encryption algorithm can fully compensate for human lapses in judgment — and no technical control is as effective as a workforce that understands why security matters and takes personal ownership of it. This policy establishes the organization's minimum security requirements across both the digital and physical domains.

Every employee, contractor, and authorized visitor to company facilities or systems is accountable for complying with the standards in this document. Compliance is not optional, and non-compliance is treated as a serious conduct issue regardless of whether it results in a measurable incident. Security events that occur due to negligence or deliberate policy violations will be investigated and may result in disciplinary action, up to and including termination.

This policy should be read in conjunction with the IT Security Policy (which addresses data classification, phishing simulations, GDPR/CCPA requirements, and acceptable use) and the AI Governance Policy.

---

## 2. Password Complexity and 90-Day Rotation

### 2.1 Password Complexity Requirements

All passwords used to access company systems — including email, applications, the VPN, and any internally hosted tools — must meet the following complexity requirements:

- **Minimum length:** 14 characters
- **Character requirements:** At least one uppercase letter (A–Z), one lowercase letter (a–z), one numeric digit (0–9), and one special character (e.g., !, @, #, $, %, ^, &, *)
- **No reuse:** The system will block any of your last 12 passwords from being reused
- **No dictionary words or personal identifiers:** Passwords may not consist of common English dictionary words, variations of your name, username, or employee ID, or personal information that others could reasonably guess (birth year, pet's name, street address)
- **No incremental variations:** Adding a number or punctuation mark to the end of an old password (e.g., Password2024 → Password2025!) does not meet the complexity requirement and will be flagged

Strong passwords are typically passphrases — four or more unrelated words combined with numbers and symbols, which are both long and memorable. Example structure: Blue!Market92Fence (this is illustrative only — do not use this exact example).

### 2.2 Mandatory 90-Day Rotation

All employee passwords for corporate accounts must be changed every **90 days**. The system will prompt you to update your password during the 14-day window before expiration. If you allow a password to expire, you will be locked out of the affected system and must contact the IT helpdesk to have your access restored.

Password rotation applies to: your primary network account (SSO), corporate email, VPN credentials, and any application-specific accounts not federated with SSO. Service accounts managed by IT are also subject to 90-day rotation on a staggered schedule managed by the IT Security team.

### 2.3 Password Manager Requirement

Given the volume and complexity of passwords employees are required to maintain, the use of the company-approved password manager is mandatory for all employees with access to Tier 3 (Confidential) or Tier 4 (Restricted) systems. The password manager is provisioned and configured by IT. Storing company system passwords in personal, unapproved password managers or in plain-text files (including spreadsheets, sticky notes, or notes apps) is a security violation.

---

## 3. Clear Desk Policy

### 3.1 Policy Statement

The Clear Desk Policy requires all employees to ensure that their physical workspace — whether in a company office or at home — does not expose confidential or sensitive information when they step away from their desk, at the end of the workday, or during any period of sustained absence.

This policy exists because physical access to confidential documents, screen contents, or written notes can be just as damaging as a digital breach — particularly in open-plan offices, shared workspaces, conference rooms, and home offices where family members or visitors may be present.

### 3.2 What "Clear Desk" Requires

**At the end of every workday and during any absence of 30 minutes or more:**

- Lock your computer screen (Windows: Win + L; Mac: Control + Command + Q). Your screen should never be left unattended and unlocked.
- Remove all physical documents containing confidential or sensitive information from your desk surface and store them in a locked drawer or filing cabinet
- Shred any physical documents no longer needed that contain PII, financial data, or information classified as Confidential or Restricted (use designated cross-cut shredding bins provided by the company)
- Ensure printed documents are retrieved from the printer promptly — do not send sensitive print jobs and leave them unattended in the printer tray
- Whiteboard contents containing sensitive information (client names, strategic plans, financial projections) must be erased before you leave the room

**For remote employees:** Apply the same standards to your home workspace. Lock your screen when stepping away, even briefly. Secure physical documents. Be especially mindful if you work in a shared or semi-public area of your home.

### 3.3 Compliance Spot Checks

Facilities and IT Security may conduct unannounced clear desk compliance checks in company offices. Employees whose desks are found non-compliant (e.g., unattended unlocked screens, sensitive documents left visible) will be reminded of the policy. Repeated non-compliance will be escalated to the employee's manager and HR.

---

## 4. Multi-Factor Authentication (MFA)

### 4.1 MFA Is Mandatory for All Corporate Accounts

Multi-Factor Authentication (MFA) is required for all employees and contractors accessing any company system, network, or cloud application. MFA requires you to verify your identity through two or more factors: something you know (your password) and something you have (an authenticator app, hardware token, or SMS code).

MFA must be enrolled during IT onboarding and must remain active throughout your employment. There are no role-based exceptions to the MFA requirement.

### 4.2 Approved MFA Methods (in order of preference)

**Authenticator app (preferred):** Time-based one-time password (TOTP) generated by an approved authenticator application installed on your smartphone. The company-approved authenticator app is provided by IT. Authenticator apps are preferred because they function without cellular connectivity and are resistant to SIM-swapping attacks.

**Hardware security key:** A physical FIDO2-compatible key (e.g., YubiKey) that plugs into your device's USB port. Available upon request for employees in high-security roles. Hardware keys are the most phishing-resistant MFA method.

**SMS/Text message codes:** Acceptable as a backup method only. SMS-based codes are vulnerable to SIM-swapping and interception and should not be the sole MFA method for accounts with access to Tier 3 or Tier 4 data.

**MFA codes must never be shared.** IT staff will never ask you for your MFA code. If anyone — by phone, email, or chat — requests your authentication code, do not provide it and report the request to the IT Security team immediately.

### 4.3 Lost or Compromised MFA Devices

If you lose access to your MFA device or your authenticator app, contact the IT helpdesk immediately. Account recovery requires identity verification through HR records. MFA device loss does not justify bypassing the MFA requirement — your account will remain locked until proper recovery procedures are completed.

---

## 5. Reporting Lost or Stolen Hardware

### 5.1 Immediate Reporting Requirement

Any company-issued device — laptop, smartphone, tablet, security token, or access badge — that is lost or stolen must be reported to the IT Security team within **2 hours** of the employee becoming aware of the loss. Delayed reporting significantly increases the window of potential unauthorized access to company systems and data.

To report a lost or stolen device: call the IT Security emergency line at ext. 4911 (available 24/7), or email security@company.com from a secondary device. Do not wait until the next business day if the loss occurs outside of working hours.

### 5.2 What Happens After Reporting

Upon receiving a lost/stolen device report, IT Security will immediately: remotely lock and, where possible, remotely wipe the device; revoke the device's access tokens and certificates; force a password reset on all accounts that were authenticated on that device; review access logs for unauthorized activity in the preceding 48 hours; and issue a replacement device after identity verification.

### 5.3 Employee Responsibility and Liability

Employees are expected to take reasonable precautions to prevent device loss or theft: never leave company devices unattended in public spaces, always use a security cable lock in shared work environments, and store devices securely when not in use. Devices lost through negligence (e.g., left visibly on a car seat, forgotten in a public space) may result in the employee being held partially responsible for recovery or replacement costs, as outlined in the Equipment Policy.

---

## 6. Handling Personally Identifiable Information (PII)

### 6.1 What Is PII

Personally Identifiable Information (PII) is any data that can be used, alone or in combination, to identify a specific individual. PII includes: full name, home address, email address, phone number, date of birth, Social Security number, government-issued ID numbers, biometric data, financial account numbers, health information, employment records, IP addresses, device identifiers, and geolocation data.

PII is classified as Confidential (Tier 3) or Restricted (Tier 4) under the company's Information Classification Policy and must be handled accordingly.

### 6.2 Minimum Necessary Principle

Access to PII should be limited to employees who have a documented, legitimate business need. Do not access, copy, or use PII beyond what is required for your specific job function. When completing a task, use the minimum amount of PII necessary — if an analysis can be completed with anonymized or pseudonymized data, use that instead.

### 6.3 PII Handling Procedures

**Storage:** PII must be stored in approved, encrypted company systems only. Storing PII in personal cloud storage (Google Drive personal, iCloud, Dropbox personal), unencrypted email attachments, or local device files outside designated secure folders is prohibited.

**Transmission:** PII transmitted electronically must be encrypted. Use secure file-sharing platforms approved by IT. Never transmit PII via unencrypted email or SMS. When PII must be sent via email, use the company's encrypted email feature or a secure file transfer tool.

**Disposal:** Physical documents containing PII must be shredded using cross-cut shredders or designated secure shredding bins. Digital files must be permanently deleted using IT-approved methods — simply moving a file to the Trash is not sufficient for Tier 3 or Tier 4 data.

**Breach Response:** If you suspect that PII has been accessed, transmitted, or disclosed without authorization, report it to the IT Security team and Legal immediately. Under GDPR, the company has 72 hours to notify the relevant supervisory authority. Prompt internal reporting is essential.

---

## 7. Removable Media (USB) Restrictions

### 7.1 USB and Removable Media Policy

The use of removable media — including USB flash drives, external hard drives, SD cards, and optical discs — on company devices is **prohibited by default**. Removable media represents one of the most common vectors for both data exfiltration (intentional or accidental) and malware introduction.

Company-issued laptops are configured with endpoint security controls that restrict unauthorized USB device connections. Attempting to circumvent these controls is a serious security violation.

### 7.2 Authorized Exceptions

Removable media use may be authorized for specific, documented business purposes upon request to IT Security. Authorization requires: a written request describing the business need, the type and amount of data to be transferred, the device to be used (must be company-issued or IT-vetted), and manager approval.

Authorized removable media must be: encrypted using the company's approved encryption tool, used only for the approved purpose, returned to IT or securely erased immediately after use, and never shared with or lent to other employees unless individually authorized.

**Personal USB devices** — even those used previously for work purposes — are never permitted to be connected to company-issued hardware.

---

## 8. Physical Office Access and Badge Security

### 8.1 Badge Requirements

All employees, contractors, and authorized visitors must display a valid, visible access badge at all times while in company facilities. Badges must be worn on the upper body (not in pockets, bags, or attached to lanyards that obscure the photo). Failing to display your badge is a security violation subject to escalation.

### 8.2 Tailgating and Piggybacking

**Tailgating** (following an authorized person through a secured entry point without independently badging in) is prohibited, even if you know the individual you are following. Every person entering a secured area must badge independently. If you see someone attempting to tailgate, politely ask them to use their own badge. If they are unable to, escort them to the reception desk and notify Facilities Security.

Do not hold doors open for individuals you do not personally know to be authorized, regardless of their stated role or apparent urgency.

### 8.3 Lost Badges

A lost or stolen access badge must be reported to Facilities Security immediately. The badge will be deactivated. Continued use of a deactivated badge will trigger a security alert. Replacement badges are issued by Facilities Security following identity verification.

### 8.4 Visitor Access

All visitors must: sign in at reception, present government-issued identification, receive a temporary visitor badge, and be escorted at all times by the employee hosting them. Visitors may not be left unattended in secure areas, server rooms, or any space beyond the reception or designated visitor waiting area.

---

## 9. Security Incident Reporting

Report all security concerns — lost devices, suspected breaches, policy violations, or suspicious physical or digital activity — immediately to:

**IT Security (24/7):** security@company.com | ext. 4911
**Facilities Security:** facilities@company.com | ext. 4100
**Anonymous Ethics Hotline:** 1-800-XXX-XXXX

*Last Updated: January 2025 | Version 2.9 | Classification: Internal Use Only*
