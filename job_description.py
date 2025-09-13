def clean_jd(jd_text: str) -> str:
    """Simple cleaning of job description"""
    return jd_text.replace("\n", " ").strip()
