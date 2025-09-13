import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API Key
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(model="llama-3.3-70b-versatile",
               groq_api_key="actual groq api key")

def generate_cover_letter(resume_text: str, job_description: str) -> str:
    """Generate AI cover letter"""
    prompt = f"""
    You are an AI assistant. Write a professional cover letter in 3 short paragraphs
    tailored to the given job description using the candidate's resume.

    Resume: {resume_text}

    Job Description: {job_description}
    """
    response = llm.invoke(prompt)
    return response.content
