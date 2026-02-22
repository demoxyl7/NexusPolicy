import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import streamlit as st
import os
# We import directly from engine because PYTHONPATH is set to 'src'
from engine import get_nexus_response 

st.set_page_config(page_title="NexusPolicy AI", page_icon="⚖️")

st.title("⚖️ NexusPolicy Assistant")
st.markdown("Query company policies with grounded citations and guardrails.")

# Sidebar for Status
with st.sidebar:
    st.success("Knowledge Base: Active")
    st.info("Model: Llama 3 (8B)")

query = st.text_input("What would you like to know about our policies?")

if query:
    with st.spinner("Analyzing policies..."):
        try:
            # Call our engine
            answer, docs = get_nexus_response(query)
            
            st.write("### 🤖 Answer")
            st.write(answer)
            
            # Show Citations (Requirement 6)
            st.write("---")
            st.write("### 📄 Source Documents")
            for doc in docs:
                # Get the filename from the metadata path
                source_name = os.path.basename(doc.metadata.get('source', 'Unknown'))
                st.info(f"Context found in: **{source_name}**")
                
        except Exception as e:
            st.error(f"Engine Error: {e}")
            st.info("Tip: Ensure your GROQ_API_KEY is set in the .env file.")