import streamlit as st
import os
from pipeline.rag_pipeline import RAGPipeline



# UI Styling
st.set_page_config(page_title="Intelligent-Retriever", page_icon="🤖", layout="centered")


# App Title
st.markdown("## <h2>Intelligent Retriever</h2>", unsafe_allow_html=True)
st.markdown("##### <h5>Upload a PDF and get AI-powered insights instantly!</h5>", unsafe_allow_html=True)

# File Uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"], help="Supports only .pdf files")

def save_uploaded_file(uploaded_file):
    folder = "data/corpus"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# User Input Prompt
prompt = st.text_input("Enter your query:", placeholder="Ask a question about your document...")


def process_query(prompt, file_path):
    rag_pipeline = RAGPipeline()
    return rag_pipeline.run(prompt, file_path, 5)

# Submit Button
if st.button("🔍 Retrieve Information"):
    if uploaded_file and prompt:
        file_path = save_uploaded_file(uploaded_file)
        response = process_query(prompt, file_path)
        st.success(response)
    else:
        st.error("⚠️ Please provide both a prompt and a file.")