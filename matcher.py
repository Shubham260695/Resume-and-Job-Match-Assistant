import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load API Key
load_dotenv()
groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY is not set. Check your .env file.")

# Initialize LLM
llm = ChatGroq(groq_api_key="actual groq api key", model="llama-3.3-70b-versatile")

def job_match_assistant(resume_text: str, job_description: str) -> str:
    """Compare resume with job description"""
    prompt = f"""
    You are an AI career assistant. Compare this resume with the job description.
    1. Provide a match score (0-100%).
    2. Highlight strengths where the resume matches the JD.
    3. Suggest improvements to increase the match.

    Resume: {resume_text}

    Job Description: {job_description}
    """
    response = llm.invoke(prompt)
    return response.content
