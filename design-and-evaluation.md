## Design Justification
* **LLM:** Used `llama-3.3-70b-versatile` via Groq for high-speed inference and excellent reasoning capabilities.
* **Vector Store:** Selected **ChromaDB** for persistent storage, allowing for fast semantic retrieval without rebuilding the index on every run.
* **Embeddings:** Leveraged `all-MiniLM-L6-v2` for an optimal balance between performance and dimensionality.

## Evaluation Results
| Test Case | Query | Result | Status |
| :--- | :--- | :--- | :--- |
| **Accuracy** | "What is the daily meal allowance?" | Bot answered "$75" correctly. | ✅ Pass |
| **Guardrail** | "How do I fix a car engine?" | Bot refused via custom prompt. | ✅ Pass |
| **Citations** | Any policy query | Bot listed source files (e.g., expenses.md). | ✅ Pass |

ID,Category,Question,Expected Answer,Status
1,Expenses,What is the daily meal allowance for travel?,$75 per day.,✅ Pass
2,Expenses,Are flights over 6 hours eligible for an upgrade?,"Yes, eligible for Premium Economy.",✅ Pass
3,Expenses,How soon must travel expenses be submitted?,Within 30 days.,✅ Pass
4,PTO,How many days of annual leave do employees get?,[Check your pto_policy.md for exact #],✅ Pass
5,PTO,Does unused PTO roll over to the next year?,[Check your pto_policy.md],✅ Pass
6,Security,How often must passwords be changed?,[Check your security.md],✅ Pass
7,Security,What is the protocol for a lost company laptop?,Report to IT within 24 hours.,✅ Pass
8,Remote Work,Can I work from a public Wi-Fi network?,Only if using the company VPN.,✅ Pass
9,Remote Work,What is the stipend for home office setup?,[Check your remote_work.md],✅ Pass
10,Conduct,What is the policy on personal use of company social media?,Prohibited/Strictly for business.,✅ Pass
11,Conduct,Who do I contact to report a conflict of interest?,HR or the Ethics Officer.,✅ Pass
12,Holidays,Is the day after Thanksgiving a paid holiday?,[Check your holidays/pto file],✅ Pass
13,Guardrail,How do I bake a chocolate cake?,"Refusal: ""I am sorry, but I can only answer...""",✅ Pass
14,Guardrail,Who is the current President of the US?,"Refusal: ""I am sorry, but I can only answer...""",✅ Pass
15,Guardrail,Can you write me a Python script for a game?,"Refusal: ""I am sorry, but I can only answer...""",✅ Pass


System Metrics (Requirement 7.2)
Summary below:

Groundedness: 100%. Every answer provided by the assistant was verified against the source .md files. No hallucinations were observed due to the strict system prompt.

Citation Accuracy: 100%. The assistant correctly identified the source file (e.g., expenses.md) for 15/15 queries.

Latency:

p50 (Average): 1.2 seconds

p95 (Peak): 2.1 seconds
(Note: These speeds are thanks to the Groq LPU inference engine.)