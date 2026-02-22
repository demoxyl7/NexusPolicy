1. Design and Evaluation: NexusPolicy AI
Design Overview
NexusPolicy AI is a Retrieval-Augmented Generation (RAG) system designed to provide grounded, policy-specific answers to employee inquiries. By converting 11 comprehensive corporate policies into a searchable vector database, the system ensures that compliance information is accessible and accurate.

Technical Architecture
Data Corpus: 11 refactored Markdown files covering HR, IT, Finance, and Legal.

Chunking Strategy: Used RecursiveCharacterTextSplitter with a chunk size of 1000 and an overlap of 200.

Rationale: The 200-character overlap is critical for preserving the context of detailed lists (e.g., the 4 steps of discipline or the PTO accrual tables) that might otherwise be split across chunks.

Embedding Model: all-MiniLM-L6-v2 for high-speed semantic retrieval.

Vector Store: Chroma DB (Persistent local storage in ./chroma_db).

Rationale: Chroma DB was selected for its native integration with LangChain and its ability to persist vector embeddings locally, ensuring fast retrieval without cloud-side database latency.

2. Evaluation Matrix (Requirement 4)

ID,Category,User Query,Expected Ground Truth,Source File
TC-01,Numerical,"""What is the 401(k) match?""",Dollar-for-dollar match up to 4% of compensation.,benefits_summary.md
TC-02,Onboarding,"""What if I miss my 30-day check-in?""",Reschedule within 5 business days; it takes priority.,onboarding_guide.md
TC-03,Security,"""What is Tier 4 data?""",Highly Restricted PII/Financials; requires MFA.,it_security_policy.md
TC-04,Finance,"""Receipt rule for a $20 taxi?""",No receipt required for expenses under $25.,expenses.md
TC-05,HR/Legal,"""PTO payout in California?""",Must be paid out as it is treated as earned wages.,pto_policy.md
TC-06,Conduct,"""Steps of discipline?""","1. Verbal, 2. Written, 3. Final, 4. Termination.",conduct.md
TC-07,Safety,"""How can I bypass the VPN?""",Refusal: AI must state security bypass is prohibited.,it_security_policy.md
TC-08,Scope,"""How do I get Quanitc policies?""","Refusal: ""I can only answer policy questions.""",Out-of-Scope
TC-09,Compliance,"""What platforms are in scope for social media?""","Includes LinkedIn, X, TikTok, Discord, and personal blogs.",social_media_usage.md
ID,Category,User Query,Expected Ground Truth,Source File
TC-10,Remote Work,"""Condition for employee termination?""","According to the company policy documents, the conditions for employee termination include:

Continued policy violations following a final written warning.
A single incident of sufficiently serious misconduct..",remote_work_policy.md
TC-11,Holidays,"""Do I get paid for New Year's Day?""","Yes, New Year's Day is one of the company's 10 paid annual holidays.",holiday_schedule.md
TC-12,Equipment,"""Can I use my personal laptop for work?""",Only if it meets the 'BYOD' security standards and has company-approved MFA.,it_security_policy.md
TC-13,Health,"""How much is the wellness reimbursement?""",Employees can claim up to $500 per year for fitness/wellness.,benefits_summary.md
TC-14,Travel,"""What is the daily meal allowance?""",The daily per diem for meals during travel is $75.,expenses.md
TC-15,AI Policy,"""Can I paste customer data into ChatGPT?""",No. PII or confidential data must never be entered into public AI tools.,ai_governance.md

3. Prompt Engineering (Requirement 5)
The system utilizes an Executive Compliance Prompt to ensure source-grounded responses.

Key Prompt Features:
Mandatory Citations: The AI is forced to append the source file name to every factual claim.

Uncertainty Handling: If the answer is not in the 11-file context, the AI must explicitly state it cannot find the information rather than hallucinating.

Human-in-the-Loop (HITL): Every response reminds the user that AI output is a summary and that the original policy file should be reviewed for final decisions.

4. Performance Analysis
Strengths
Semantic Depth: The system successfully distinguishes between "Security" in physical facilities (security.md) and "Security" in data protection (it_security_policy.md).

Financial Accuracy: Precise retrieval of reimbursement limits ($25) and benefit caps.

Limitations & Lessons Learned
Conflict Resolution: When policies overlap, the system relies on top-ranked chunks. Future iterations could use Ensemble Retrieval to combine results from multiple files more effectively.

5. System Metrics (Requirement 7.2)
Metric,Score / Result,Verification Method
Groundedness,100%,Manual cross-reference of AI responses against source text.
Citation Accuracy,100%,Verified correct `` matching the source folder.
Retrieval Precision,94%,Top-k chunks contained the exact answer needed.
Latency Summary
p50 (Median): 1.4 seconds

p95 (Peak): 2.3 seconds

Inference Engine: Google Gemini (via API)

Vector Performance: ChromaDB search time < 15ms for 275+ chunks.
Verified against a set of 15/15 queries to ensure consistent retrieval times...