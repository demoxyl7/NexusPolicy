# AI Tooling Disclosure

## Tools Used
* **Gemini (Google):** Primary AI collaborator for architecture design, debugging, and documentation.
* **Cursor/VS Code:** Integrated Development Environment.

## How AI Was Leveraged
1. **Environment Troubleshooting:** Used AI to resolve critical version conflicts between Python 3.14 (experimental) and the stable requirements for ChromaDB and Pydantic, eventually guiding the migration to Python 3.11.
2. **Refactoring:** Assisted in the transition from FAISS to ChromaDB to ensure persistent vector storage as per project requirements.
3. **Prompt Engineering:** Iteratively refined the system prompt to maintain strict guardrails, ensuring the model refuses non-policy questions (Groundedness).
4. **Documentation:** Assisted in generating the evaluation metrics and system architecture justifications.

## What Worked Well
* **Rapid Debugging:** AI was extremely effective at interpreting tracebacks and providing the correct `pip` commands for a stable environment.
* **Boilerplate Generation:** Streamlit UI components were generated and customized quickly.

## Challenges
* **Context Windows:** Initially, the "strict" prompt caused the AI to refuse valid questions. I had to use the AI to help balance the "helpful assistant" persona with the "strict policy" guardrail.