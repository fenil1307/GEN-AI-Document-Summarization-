# GEN-AI-Document-Summarization-

# PDF to Mindmap with Gemini API

This project allows you to upload a PDF document, generate a summary using the **Gemini API**, and then create an interactive mindmap based on the summary. Additionally, it can generate questions from the summarized content using the Gemini API.

## Features:
- **PDF Upload:** Upload a PDF document and extract text from it.
- **Summary Generation:** Use the Gemini API to generate a summary of the content.
- **Mindmap Generation:** Convert the summary into a mindmap.
- **Question Generation:** Generate questions based on the summarized content to enhance study or understanding.

## Tech Stack:
- **Gemini API**: For text summarization and question generation.
- **Python**: The main programming language used for the project.
- **Streamlit**: For creating a user-friendly interface to interact with the tool.
- **Graphviz/NetworkX**: For generating mindmaps using Python (no need for Node.js or Markmap).
- **PyPDF2**: To extract text from PDF files.

## Requirements:
Before running the project, ensure you have the following installed:
- **Python 3.x**
- **Gemini API Key** (available via Gemini API portal)
- **Required Python libraries**:
  ```bash
  pip install requests langchain streamlit graphviz networkx
