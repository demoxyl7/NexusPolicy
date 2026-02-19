# NexusPolicy AI Assistant
An AI-powered RAG (Retrieval-Augmented Generation) system to query company policies.

## Setup Instructions
1. Ensure Python 3.11 is installed.
2. Create venv: `py -3.11 -m venv venv_stable`
3. Activate: `.\venv_stable\Scripts\activate`
4. Install: `pip install -r requirements.txt`
5. Add your `GROQ_API_KEY` to the `.env` file.

## Usage
1. Run `python src/ingest.py` to index policies.
2. Run `streamlit run src/app.py` to launch the UI.