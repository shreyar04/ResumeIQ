import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai
import requests
from bs4 import BeautifulSoup

# ------------------ STREAMLIT CONFIG ------------------
st.set_page_config(page_title="ATS Resume Expert", layout="wide")

# ------------------ LOAD ENV ------------------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found! Please check your .env file.")
    st.stop()

genai.configure(api_key=api_key)

# ------------------ MODEL INIT ------------------
model = genai.GenerativeModel("gemini-2.5-flash")

# ------------------ FUNCTION TO EXTRACT JD FROM URL ------------------
def extract_jd_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, "html.parser")

        for script in soup(["script", "style"]):
            script.extract()

        text = soup.get_text(separator=" ")
        text = " ".join(text.split())

        return text

    except Exception:
        return None

# ------------------ ATS PROMPT ------------------
ATS_PROMPT = """
You are an expert ATS (Applicant Tracking System) specialist.
Analyze the provided resume against the job description.

Output format:

### ATS Match Percentage: [0-100%]

**Matching Skills:**  
- 

**Missing Skills:**  
- 

**Strengths:**  
- 

**Improvements:**  
- 

**Final Verdict:**  
(Hire / Review / Reject)
"""

# ------------------ UI ------------------
st.title("📄 Smart ATS Resume Analyzer")
st.subheader("Powered by Gemini 2.5 Flash")

col1, col2 = st.columns(2)

# ------------------ JD INPUT ------------------
with col1:
    jd_option = st.radio(
        "Choose Job Description Input Method:",
        ["Paste Text", "From URL"]
    )

    job_description = None

    if jd_option == "Paste Text":
        job_description = st.text_area("📌 Paste Job Description", height=300)

    else:
        jd_url = st.text_input("🔗 Paste Job Description Link")

        if jd_url:
            with st.spinner("Fetching job description..."):
                job_description = extract_jd_from_url(jd_url)

            if job_description:
                st.success("✅ Job description fetched successfully!")
            else:
                st.error("❌ Unable to fetch JD from this link")

# ------------------ RESUME UPLOAD ------------------
with col2:
    uploaded_file = st.file_uploader(
        "📤 Upload Resume (PDF)", type=["pdf"]
    )

    if uploaded_file:
        st.success("✅ PDF Uploaded Successfully!")

# ------------------ ANALYZE BUTTON ------------------
if st.button("🔍 Analyze Resume"):

    if not job_description:
        st.warning("⚠ Please provide a Job Description.")

    elif not uploaded_file:
        st.warning("⚠ Please upload a resume.")

    else:
        with st.spinner("🤖 Gemini is analyzing your resume..."):

            try:
                job_description = job_description[:15000]

                response = model.generate_content(
                    [
                        {"text": ATS_PROMPT},
                        {"text": job_description},
                        {
                            "mime_type": "application/pdf",
                            "data": uploaded_file.getvalue(),
                        },
                    ]
                )

                st.markdown("---")
                st.subheader("📊 Evaluation Results")
                st.markdown(response.text)

                # JD Preview
                with st.expander("📄 Job Description Preview"):
                    st.write(job_description[:1000])

            except Exception as e:
                st.error(f"❌ An error occurred: {e}")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Native multimodal analysis — no OCR required.")
