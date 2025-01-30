import requests
import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent"

def summarize_text_gemini(text):
    """Summarizes text using Gemini API"""
    if not gemini_api_key:
        return "Error: API Key is missing. Please set GEMINI_API_KEY in .env"

    url = f"{GEMINI_API_URL}?key={gemini_api_key}"  
    headers = {"Content-Type": "application/json"}
    payload = {"contents": [{"parts": [{"text": text}]}]}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        if "candidates" in data:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        else:
            return "Error: Unexpected API response format."

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def generate_questions(text):
    """Generates questions using Gemini API via LangChain"""
    if not gemini_api_key:
        return "Error: API Key is missing. Please set GEMINI_API_KEY in .env"

    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=gemini_api_key, temperature=0.7)  # ✅ Pass API key
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Generate 5 questions based on the following content:\n{text}"
    )
    return llm.invoke(prompt.format(text=text))  