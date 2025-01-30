import streamlit as st
from pdf_utils import extract_text_from_pdf
from summarizer import summarize_text_gemini, generate_questions
from mindmap_generator import create_mindmap_from_summary

st.title("Generative AI for Document Summarization")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file:
    # Step 1: Extract text
    st.info("Extracting text from PDF...")
    text = extract_text_from_pdf(uploaded_file)

    # Step 2: Summarize text
    st.info("Generating summary...")
    summary = summarize_text_gemini(text)
    st.write("### Summary", summary)

    # Step 3: Generate questions
    st.info("Generating questions...")
    questions = generate_questions(text)
    st.write("Questions", questions)

    # Step 4: Create mindmap
    st.info("Creating mindmap...")
    create_mindmap_from_summary(summary, "mindmap.html")
    st.markdown("[Download Mindmap](./mindmap.html)", unsafe_allow_html=True)
