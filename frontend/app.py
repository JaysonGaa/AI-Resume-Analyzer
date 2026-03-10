# frontend/app.py  (run with: streamlit run app.py)
import streamlit as st
import requests

API_URL = "http://localhost:8000/analyze"

st.set_page_config(page_title="Resume Analyzer", page_icon="🧠")
st.title("🧠 AI Resume Job Match Analyzer")
st.caption("Upload your resume and paste a job description to see how well you match.")

# --- Inputs ---
uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])
job_description = st.text_input("Paste the job link here")

if st.button("Analyze Match") and uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        response = requests.post(
            API_URL,
            files={"resume": uploaded_file.getvalue()},
            data={"job_description": job_description}
        )
        result = response.json()

    # --- Results Display ---
    st.subheader(f"Match Score: {result['match_score']}%")
    # TODO: Add a progress bar or gauge chart here
    st.progress(result["match_score"] / 100)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### ❌ Missing Skills")
        for skill in result["missing_skills"]:
            st.markdown(f"- {skill}")

    with col2:
        st.markdown("### ✅ Suggestions")
        for tip in result["suggestions"]:
            st.markdown(f"- {tip}")

    st.info(result["summary"])