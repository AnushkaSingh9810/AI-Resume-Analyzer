import streamlit as st
from pypdf import PdfReader
from google import genai

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

.hero {
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(135deg, #1f2937, #111827);
    margin-bottom: 25px;
}

.hero h1 {
    margin-bottom: 5px;
    font-size: 38px;
}

.hero p {
    font-size: 17px;
    opacity: 0.8;
}

.card {
    padding: 22px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,0.12);
    background: rgba(255,255,255,0.04);
    margin-bottom: 18px;
}

.score {
    text-align: center;
    padding: 25px;
    border-radius: 18px;
    background: linear-gradient(135deg, #312e81, #1e1b4b);
}

.score-number {
    font-size: 48px;
    font-weight: bold;
}

.section-title {
    font-size: 22px;
    font-weight: 700;
    margin-top: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="hero">
    <h1>🤖 AI Resume Analyzer</h1>
    <p>Analyze your resume against a job description using Generative AI.</p>
</div>
""", unsafe_allow_html=True)

# =========================
# INPUT SECTION
# =========================

col1, col2 = st.columns(2)


with col2:
    st.markdown("### 📄 Upload Resume")

    resume_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

st.markdown("### 💼 Job Description")

job_description = st.text_area(
    "Paste the job description",
    height=180,
    placeholder="Paste the job description here...",
    label_visibility="collapsed"
)

st.write("")

# =========================
# ANALYZE BUTTON
# =========================

analyze = st.button(
    "🔍 Analyze Resume",
    use_container_width=True
)

if analyze:

    if resume_file is None:
        st.warning("📄 Please upload your resume PDF.")

    elif not job_description.strip():
        st.warning("💼 Please enter a job description.")

    else:

        # =========================
        # READ RESUME
        # =========================

        reader = PdfReader(resume_file)

        resume_text = ""

        for page in reader.pages:
            resume_text += page.extract_text() or ""

        # =========================
        # GEMINI
        # =========================
        api_key = st.secrets["GEMINI_API_KEY"]
        client = genai.Client(api_key=api_key)

        prompt = f"""
You are an expert HR Resume Analyzer.

Compare the candidate's resume with the given job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return the analysis exactly using these headings:

MATCH SCORE:
Give a percentage from 0 to 100.

MATCHING SKILLS:
List the matching skills.

MISSING SKILLS:
List important missing skills.

STRENGTHS:
Give 3 strong points.

IMPROVEMENT SUGGESTIONS:
Give 3 practical suggestions.

INTERVIEW QUESTIONS:
Give 5 interview questions based on the resume and job description.
"""
import time

with st.spinner("🤖 AI is analyzing your resume..."):

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

    except Exception:
        time.sleep(3)

        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )
        result = response.text

        # =========================
        # RESULT HEADER
        # =========================

        st.markdown("---")

        st.markdown(
            "<h2>📊 Resume Analysis</h2>",
            unsafe_allow_html=True
        )

        # =========================
        # EXTRACT SCORE
        # =========================

        import re

        score_match = re.search(
            r"MATCH SCORE:\s*(\d+)",
            result,
            re.IGNORECASE
        )

        score = score_match.group(1) if score_match else "N/A"

        # =========================
        # SCORE CARD
        # =========================

        st.markdown(f"""
        <div class="score">
            <div>🎯 Resume Match Score</div>
            <div class="score-number">{score}%</div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        # =========================
        # DISPLAY SECTIONS
        # =========================

        sections = [
            ("MATCHING SKILLS:", "✅ Matching Skills"),
            ("MISSING SKILLS:", "❌ Missing Skills"),
            ("STRENGTHS:", "💪 Strengths"),
            ("IMPROVEMENT SUGGESTIONS:", "💡 Improvement Suggestions"),
            ("INTERVIEW QUESTIONS:", "🎤 Interview Questions")
        ]

        for keyword, title in sections:

            if keyword in result:

                start = result.index(keyword) + len(keyword)

                remaining = result[start:]

                next_positions = []

                for other_keyword, _ in sections:

                    if other_keyword != keyword and other_keyword in remaining:
                        next_positions.append(
                            remaining.index(other_keyword)
                        )

                end = (
                    min(next_positions)
                    if next_positions
                    else len(remaining)
                )

                content = remaining[:end].strip()

                st.markdown(
                    f'<div class="card"><div class="section-title">{title}</div>',
                    unsafe_allow_html=True
                )

                st.markdown(content.replace("\n", "  \n"))

                st.markdown("</div>", unsafe_allow_html=True)

        st.success("🎉 Resume analysis completed successfully!")
