import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

# ------------------ STREAMLIT CONFIG (MUST BE FIRST) ------------------
st.set_page_config(page_title="ATS Resume Expert", layout="wide")

# ------------------ LOAD ENV & CONFIGURE ------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("❌ GOOGLE_API_KEY not found! Please check your .env file.")
    st.stop()

# ------------------ MODEL INIT ------------------
st.write("SDK version:", genai.__version__)
st.write("Model line check:", "gemini-2.5-flash")

model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ ATS PROMPT ------------------
ATS_PROMPT = """
You are an expert ATS (Applicant Tracking System) specialist.
Analyze the provided resume against the job description.

Output format:
### ATS Match Percentage: [0-100%]
**Matching Skills:** [List]
**Missing Skills:** [List]
**Strengths:** [List]
**Improvements:** [List]
**Final Verdict:** (Hire / Review / Reject)
"""

# ------------------ UI ------------------
st.title("📄 Smart ATS Resume Analyzer")
st.subheader("Powered by Gemini 2.5 Flash")

col1, col2 = st.columns(2)

with col1:
    job_description = st.text_area("📌 Paste Job Description Here", height=300)

with col2:
    uploaded_file = st.file_uploader("📤 Upload Resume (PDF)", type=["pdf"])
    if uploaded_file:
        st.success("PDF Uploaded Successfully!")

if st.button("🔍 Analyze Resume"):
    if not job_description:
        st.warning("Please paste a job description.")
    elif not uploaded_file:
        st.warning("Please upload a resume.")
    else:
        with st.spinner("Gemini is analyzing your resume..."):
            try:
                response = model.generate_content([
                    {"text": ATS_PROMPT},
                    {"text": job_description},
                    {
                        "mime_type": "application/pdf",
                        "data": uploaded_file.getvalue()
                    }
                ])

                st.markdown("---")
                st.subheader("📊 Evaluation Results")
                st.markdown(response.text)

            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.caption("Native multimodal analysis — no OCR required.")
