import streamlit as st
from utils import extract_text_from_pdf
from ats_scoring import calculate_ats_score

st.set_page_config(page_title="ATS Resume Analyzer", page_icon=":mag:")

st.title("ATS Resume Analyzer")
st.write("Upload a PDF resume to analyze how well it scores for an Applicant Tracking System (ATS). Results are processed locally for privacy.")

uploaded_file = st.file_uploader("Choose your resume (PDF only)", type=["pdf"])

if uploaded_file is not None:
    with st.spinner("Extracting text..."):
        try:
            text = extract_text_from_pdf(uploaded_file)
        except Exception as e:
            st.error(f"Failed to process PDF: {e}")
            st.stop()
        if not text or len(text.strip()) < 50:
            st.warning("Could not extract sufficient text from your PDF. Try a different file.")
        else:
            st.success("Text extracted from PDF!")
            st.subheader("Resume Preview")
            st.text_area("Extracted Text", text, height=150, disabled=True)

            with st.spinner("Analyzing resume..."):
                score, details = calculate_ats_score(text)
            st.header(f"ATS Score: {score}/100")
            st.progress(int(score))

            st.subheader("Detailed Breakdown")
            for k, v in details.items():
                st.write(f"- **{k}:** {v}")
