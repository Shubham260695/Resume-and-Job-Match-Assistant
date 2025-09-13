 *Resume & Job Match Assistant*
 
 *Project Overview*
 
Resume & Job Match Assistant that helps candidates and recruiters check how well a resume matches a given Job Description (JD).
Uses NLP + LLMs (Groq API) to:

1.Analyze resumes and job descriptions.
2.Calculate a match score.
3.Generate a cover letter suggestion.
4.Demonstrates how AI can be applied in HR Tech / Recruitment Automation.

*Purpose of the Project*
 
1.Help job seekers quickly understand how well their resume fits a specific job.
2.Assist recruiters in shortlisting resumes faster.
3.Automate cover letter drafting to save time.

*Features*

1.Upload or paste your Resume.
2.Paste a Job Description (JD).
3.Get a match score between Resume & JD.
4.Automatically generate a cover letter based on the JD.
5.Simple Streamlit Web App interface.

*Dataset / Input*

Unlike traditional datasets, this project works directly with text inputs:
1.Resume (text or uploaded file).
2.Job Description (JD text from Naukri/LinkedIn/etc.).

*Technologies Used*

1.PyCharm
2.Streamlit (for web interface)
3.LangChain (prompting framework)
4.Groq API (LLM backend)
5.dotenv (for API key management)

*Project Steps*

1.Text Extraction
2.Read Resume text (uploaded file or copy-paste).
3.Clean the Job Description text.

*Preprocessing*

1.Basic cleaning (removing special characters, extra spaces).
2.Job Match Assistant
3.Use Groq LLM (Mixtral-8x7B / Gemma2-9B) to analyze similarity.
4.Calculate a match score (0–100%).
5.Cover Letter Generation
6.Generate a tailored cover letter based on JD.
7.Streamlit App
8.Simple UI with text areas & file uploader.
9.Real-time match score & cover letter displayed.

*Results*

1.Successfully matches Resume with JD text.
2.Provides a clear percentage score to understand fit.
3.Generates personalized cover letters that can be edited by the user.
