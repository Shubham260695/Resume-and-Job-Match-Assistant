import streamlit as st
from Resume_Parsing import extract_resume
from job_description import clean_jd
from matcher import job_match_assistant
from ai_cover_letter import generate_cover_letter

st.title("📄 Resume & Job Description Matcher")

# Upload Resume
resume_file = st.file_uploader("Upload your Resume", type=["pdf", "docx"])

# Paste JD text
jd_text = st.text_area("Paste the Job Description here")

if st.button("Match Resume with JD"):
    if resume_file and jd_text:
        # Save resume temporarily
        with open(resume_file.name, "wb") as f:
            f.write(resume_file.read())

        # Extract resume text
        resume_text = extract_resume(resume_file.name)

        # Clean JD
        cleaned_jd = clean_jd(jd_text)

        # Match score + Cover Letter
        score = job_match_assistant(resume_text, cleaned_jd)
        cover_letter = generate_cover_letter(resume_text, cleaned_jd)

        # Show results
        st.success(f"✅ Match Score: {score}")
        st.subheader("📩 Cover Letter Preview")
        st.write(cover_letter[:1000])  # showing first 1000 chars
    else:
        st.error("⚠️ Please upload a resume and paste a job description.")

