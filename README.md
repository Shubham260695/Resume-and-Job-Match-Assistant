 # Resume & Job Match Assistant
 
 ## Project Overview
 
Resume & Job Match Assistant that helps candidates and recruiters check how well a resume matches a given Job Description (JD).
Uses NLP + LLMs (Groq API) to:

- Analyze resumes and job descriptions.
- Calculate a match score.
- Generate a cover letter suggestion.
- Demonstrates how AI can be applied in HR Tech / Recruitment Automation.

## Purpose of the Project
 
- Help job seekers quickly understand how well their resume fits a specific job.
- Assist recruiters in shortlisting resumes faster.
- Automate cover letter drafting to save time.

## Features

- Upload or paste your Resume.
- Paste a Job Description (JD).
- Get a match score between Resume & JD.
- Automatically generate a cover letter based on the JD.
- Simple Streamlit Web App interface.

## Dataset / Input

Unlike traditional datasets, this project works directly with text inputs:
- Resume (text or uploaded file).
- Job Description (JD text from Naukri/LinkedIn/etc.).

## Technologies Used

- PyCharm
- Streamlit (for web interface)
- LangChain (prompting framework)
- Groq API (LLM backend)
- dotenv (for API key management)

## Project Steps

- Text Extraction
- Read Resume text (uploaded file or copy-paste).
- Clean the Job Description text.


## Preprocessing

- Basic cleaning (removing special characters, extra spaces).
- Job Match Assistant
- Use Groq LLM (Mixtral-8x7B / Gemma2-9B) to analyze similarity.
- Calculate a match score (0–100%).
- Cover Letter Generation
- Generate a tailored cover letter based on JD.
- Streamlit App
- Simple UI with text areas & file uploader.
- Real-time match score & cover letter displayed.

## Results

- Successfully matches Resume with JD text.
- Provides a clear percentage score to understand fit.
- Generates personalized cover letters that can be edited by the user.
