import os
from dotenv import load_dotenv
import streamlit as st

from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Optional: LangSmith (only if you're using it)
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")
LANGSMITH_TRACING = os.getenv("LANGSMITH_TRACING")
LANGSMITH_PROJECT = os.getenv("LANGSMITH_PROJECT")
LANGSMITH_ENDPOINT = os.getenv("LANGSMITH_ENDPOINT")

# Debug (optional)
print("LANGSMITH_API_KEY:", LANGSMITH_API_KEY)
print("LANGSMITH_TRACING:", LANGSMITH_TRACING)
print("LANGSMITH_PROJECT:", LANGSMITH_PROJECT)
print("LANGSMITH_ENDPOINT:", LANGSMITH_ENDPOINT)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant that answers the prompt"),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain with Google Gemini ")
input_text = st.text_input("How may I help you?")

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",     # or "gemini-1.5-pro"
    temperature=0.3,
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({"question": input_text}))
