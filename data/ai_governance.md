# AI Governance Policy: Emerging Technology Guidelines

**Document Type:** Artificial Intelligence Governance Policy  
**Effective Date:** January 1, 2025  
**Applies To:** All Employees, Contractors, and Vendors Using AI Tools in the Course of Work  
**Owner:** Chief Technology Officer (CTO) / Chief Information Security Officer (CISO) / Legal & Compliance  
**Review Cycle:** Semi-Annual (given the pace of AI development)  
**Classification:** Internal Use  
**Policy Status:** Active — supersedes all prior informal AI usage guidance

---

## 1. Purpose and Context

Artificial intelligence tools — including large language models (LLMs) such as ChatGPT, Claude, Gemini, Copilot, and others — have rapidly become powerful accelerants for professional productivity. When used appropriately, AI tools can help employees draft documents, summarize information, generate code, analyze data, brainstorm ideas, and complete routine tasks significantly faster than before.

However, the same capabilities that make these tools powerful also introduce meaningful organizational risk if they are used without proper governance. Among the most significant risks: the inadvertent transmission of confidential company data to third-party AI providers, the generation of inaccurate outputs used in consequential decisions without adequate review, legal exposure related to intellectual property and data privacy, and over-reliance on AI-generated content in contexts requiring professional judgment.

This policy establishes clear, enforceable guidelines for the use of AI tools — both approved company tools and personally or informally adopted tools — in the course of work. It is designed to enable employees to benefit from AI's capabilities responsibly, with appropriate safeguards in place.

This is a living policy. Given the speed at which AI technology and the regulatory landscape are evolving, this document will be reviewed and updated at least semi-annually. Employees should treat the version in the HR portal as the current governing version.

---

## 2. Definitions

**Artificial Intelligence (AI) Tool:** Any software application, API, plugin, or platform that uses machine learning, natural language processing, or generative AI models to perform tasks traditionally requiring human cognition. For the purposes of this policy, this includes: conversational AI assistants, AI writing tools, AI coding assistants, image/video generation tools, AI-powered search, and AI-enhanced productivity features embedded within third-party platforms (e.g., Microsoft Copilot in Office 365, Notion AI, Slack AI).

**Large Language Model (LLM):** A class of AI system trained on large volumes of text data to understand and generate human language. Examples include GPT-4 (OpenAI/ChatGPT), Claude (Anthropic), Gemini (Google), and Llama (Meta). LLMs form the backbone of most conversational AI products currently in commercial use.

**Approved AI Tool:** An AI tool that has been reviewed and explicitly approved by the IT Security and Legal teams for use with specified data classification levels. A current list of Approved AI Tools is maintained on the IT portal and updated as new tools are evaluated.

**Unapproved AI Tool:** Any AI tool not on the approved list, including publicly available tools used without formal IT/Legal review (e.g., using a personal ChatGPT account to process work documents).

**Proprietary Company Data:** Any information owned by or entrusted to the company that is not publicly available. This includes, but is not limited to: trade secrets, client data, financial data, employee records, source code, unreleased product plans, and internal strategies.

**Human-in-the-Loop (HITL):** A design principle and operational requirement whereby a qualified human reviews, validates, and takes responsibility for any AI-generated output before it is used in a consequential context.

---

## 3. The Core Risk: Proprietary Data and Third-Party LLMs

### 3.1 How LLM APIs and Products Handle Your Data

When you type a prompt into a consumer AI product — including the free or paid versions of tools like ChatGPT, Claude.ai, or Gemini — your input is transmitted to the provider's servers, where it is processed by the model. Depending on the provider's terms of service and your account configuration, this data may be:

- Logged and stored by the provider
- Reviewed by the provider's human contractors for safety or quality purposes
- Used to improve or fine-tune the provider's models (depending on opt-out settings)
- Subject to legal requests or government subpoenas directed at the provider

**This means that any proprietary company data you include in a prompt to an unapproved AI tool has potentially left the company's control.** Even if you delete the conversation, there is no guarantee the provider has deleted or will delete your data.

### 3.2 What You Must Never Enter into Unapproved AI Tools

Regardless of the AI tool in question, the following categories of data must never be entered into any AI tool that has not been explicitly approved for that data classification:

- Client names, contact information, or details of client engagements
- Personally identifiable information (PII) of any employee, customer, or third party
- Non-public financial data (including revenue figures, forecasts, or M&A activity)
- Source code, algorithms, or proprietary technical specifications
- Legal communications, litigation strategy, or privileged attorney-client correspondence
- Passwords, API keys, credentials, or authentication data
- Unreleased product names, roadmaps, or feature descriptions
- Compensation data, performance reviews, or other personnel records
- Any document marked Confidential or Restricted under the Information Classification Policy

### 3.3 Practical Guidance: Sanitizing Prompts

In many cases, you can still use AI tools productively without exposing proprietary data by sanitizing your prompts — replacing specific identifiers with generic placeholders.

**Instead of:** "Summarize the contract between Acme Corp and our company for the $2.3M software implementation starting Q2 2025..."  
**Try:** "Summarize the following contract for a software implementation. [Paste a redacted version with client name and financial figures removed]"

**Instead of:** "Review this email from John Smith at Goldman Sachs regarding our merger discussions..."  
**Try:** "Review the following email for tone and clarity. [Replace identifying information with generic labels]"

When in doubt about whether your prompt is safe, ask yourself: "If this prompt were published publicly, would it harm the company, a client, or an employee?" If yes, sanitize or don't use AI for this task.

---

## 4. Approved AI Tools

### 4.1 How Tools Get Approved

AI tools are evaluated by the IT Security and Legal teams against the following criteria before receiving approval:

- **Data processing agreements:** Does the provider offer a Data Processing Addendum (DPA) that meets our GDPR/CCPA requirements?
- **Enterprise data isolation:** Does the provider offer an enterprise tier that ensures your inputs are not used to train their models?
- **Encryption and access controls:** Are data in transit and at rest appropriately encrypted?
- **Residency and jurisdiction:** Where are the provider's servers located, and does that create regulatory concerns?
- **Breach notification:** What are the provider's obligations and track record regarding security incident disclosure?

### 4.2 Requesting Approval for a New AI Tool

Employees who want to use an AI tool not currently on the approved list should submit an AI Tool Evaluation Request through the IT portal. Include the tool's name, vendor, use case, and the data classification level of information you intend to process. The IT Security and Legal teams will evaluate the request within 15 business days.

Do not begin using an unapproved tool while your evaluation request is pending.

---

## 5. The Human-in-the-Loop (HITL) Requirement

### 5.1 Why Human Oversight Is Non-Negotiable

LLMs are probabilistic systems. They generate outputs by predicting statistically likely sequences of words or code — not by reasoning from facts the way humans do. This means:

- LLMs can and do "hallucinate" — generating plausible-sounding but factually incorrect information, including fabricated citations, non-existent statistics, and false attributions
- LLMs reflect biases present in their training data
- LLMs cannot reliably know what they don't know — they will often generate confident-sounding incorrect answers
- LLMs do not have access to real-time information (unless explicitly given search capabilities) and may apply outdated context

Given these limitations, the company requires that a qualified human review and take responsibility for all AI-generated outputs before they are used in any consequential context. This is the Human-in-the-Loop (HITL) requirement.

### 5.2 What "Consequential Context" Means

A context is consequential if the output will:

- Be shared externally (with clients, partners, regulators, media, or the public)
- Inform a business decision with financial, legal, or operational impact
- Be incorporated into a legal document, contract, or compliance filing
- Be used in a communication that could create liability for the company
- Influence a hiring, promotion, or disciplinary decision affecting an employee
- Be embedded in code that will run in a production environment

Essentially: if it matters, a human must verify it before it is used.

### 5.3 HITL Standards by Use Case

**AI-Drafted Documents (proposals, reports, emails):**  
A human author must read the full output, verify all factual claims independently, correct any errors, and take ownership of the final document. Simply reviewing for grammar is insufficient — you are responsible for the accuracy and appropriateness of everything in the document.

**AI-Generated Code:**  
All AI-generated code must be reviewed by a qualified developer before being merged into any codebase. The reviewer must understand the code and be able to explain its logic — approval of code you cannot explain is prohibited. AI-generated code must pass all existing testing, security scanning, and code review processes.

**AI-Assisted Research and Analysis:**  
All factual claims, statistics, or citations sourced from an AI tool must be independently verified against primary sources before use. Do not cite AI outputs directly as sources. Treat AI-generated research as a starting point for further investigation, not a final deliverable.

**AI-Assisted Decision Support:**  
AI tools may be used to help surface options, summarize data, or model scenarios in support of business decisions. However, the decision itself — and accountability for its outcomes — rests with the human decision-maker, not the AI system.

---

## 6. Prohibited Uses of AI Tools

The following uses of AI tools are prohibited under all circumstances:

- Using AI to generate, distribute, or amplify content intended to deceive, manipulate, or harm any individual or group
- Using AI to create deepfakes, synthetic voices, or other fabricated media depicting real individuals without their consent
- Using AI to circumvent security controls, generate malicious code, or assist in any activity prohibited by the IT Security Policy
- Using AI to make or automate employment decisions (hiring, firing, promotion, compensation) without human review and documentation
- Using AI to process regulated health information (PHI under HIPAA) or payment card data (PCI-DSS scope) in any tool not specifically certified and approved for those data types
- Representing AI-generated work as entirely your own in contexts where disclosure is required (e.g., academic submissions, regulatory filings, or contexts where the organization's methodology is represented as human-only)

---

## 7. Intellectual Property Considerations

### 7.1 Ownership of AI-Generated Outputs

The legal status of AI-generated content remains unsettled in many jurisdictions. As a general principle: AI-generated content may not be eligible for copyright protection in the U.S. if it contains no original human creative expression. Employees should not assume that AI-generated work product is automatically owned by the company or is fully protectable as intellectual property.

Consult the Legal team before relying on AI-generated content as the basis for any patent application, trademark registration, or copyright claim.

### 7.2 Training Data and Reproduction Risk

Some LLMs have been trained on copyrighted material, and there is a risk that they may reproduce portions of that material in their outputs. Do not use AI-generated content in contexts where verbatim reproduction of third-party copyrighted material could expose the company to infringement claims. Run significant AI-generated text through the company's approved plagiarism/AI-output verification tool before external publication.

---

## 8. Transparency and Disclosure

### 8.1 Internal Transparency

Employees are encouraged to be transparent with their teams and managers about when and how they use AI tools in their work. Transparency enables teams to quality-check AI-assisted outputs appropriately and helps the organization understand where AI adoption is occurring.

### 8.2 External Disclosure

In some contexts, disclosure that AI was used in generating a work product is legally or ethically required. These contexts include, but are not limited to: certain government contracts, academic publications, regulated client reports, and marketing materials subject to FTC guidelines on disclosure. When in doubt, disclose. Consult Legal if you are uncertain whether disclosure is required in a specific context.

---

## 9. Training Requirements

All employees are required to complete the AI Governance Awareness module in the Learning Management System (LMS) within 30 days of hire and annually thereafter. Employees in roles with significant AI tool usage (e.g., engineering, data science, marketing, legal) may be required to complete additional role-specific AI training as designated by their department head.

---

## 10. Reporting Concerns

If you become aware of AI tool usage that appears to violate this policy, report it to:

**IT Security Team:** security@company.com | ext. 4911  
**Legal & Compliance:** legal@company.com  
**Ethics Hotline (anonymous):** 1-800-XXX-XXXX | ethics.company.com  

Reports made in good faith will be treated confidentially and without retaliation.

---

## 11. Policy Review and Contacts

**CTO Office:** cto@company.com  
**CISO / IT Security:** security@company.com  
**Legal & Compliance (IP, data privacy, contract questions):** legal@company.com  
**AI Tool Evaluation Requests:** IT Portal → "Submit AI Tool Request"

*Last Updated: January 2025 | Version 1.2 | Classification: Internal Use Only*  
*Next Scheduled Review: July 2025*
