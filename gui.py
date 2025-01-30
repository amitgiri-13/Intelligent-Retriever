import streamlit as st
import os
from pipeline.rag_pipeline import RAGPipeline

def save_uploaded_file(uploaded_file):
    folder = "data/corpus"
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

def process_query(prompt, file_path):
    rag_pipeline = RAGPipeline()
    return rag_pipeline.run(prompt, file_path, 5)

# UI Styling
st.set_page_config(page_title="Smart Retriever", page_icon="🤖", layout="centered")

st.markdown(
    """
    <style>
        .main {background-color: #f4f4f4;}
        div.stButton > button {background-color: #4CAF50; color: white; border-radius: 8px; font-size: 18px;}
        div.stTextInput > div > input {border-radius: 8px; font-size: 18px;}
        div.stFileUploader > div {border-radius: 8px; font-size: 18px;}
        h2 {font-size: 32px;}
        h5 {font-size: 20px;}
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.markdown("## <h2>Intelligent Retriever</h2>", unsafe_allow_html=True)
st.markdown("##### <h5>Upload a PDF and get AI-powered insights instantly!</h5>", unsafe_allow_html=True)

# File Uploader
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"], help="Supports only .pdf files")

# User Input Prompt
prompt = st.text_input("Enter your query:", placeholder="Ask a question about your document...")

# Submit Button
if st.button("🔍 Retrieve Information"):
    if uploaded_file and prompt:
        file_path = save_uploaded_file(uploaded_file)
        response = process_query(prompt, file_path)
        st.success(response)
    else:
        st.error("⚠️ Please provide both a prompt and a file.")