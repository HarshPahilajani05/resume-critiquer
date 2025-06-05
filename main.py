import streamlit as st
import os
import io
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="AI Resume Critiquer",
                   page_icon="📄",
                   layout="centered")

st.title("AI Resume Critiquer")
st.markdown(
    "Upload your résumé in PDF format and get feedback on how to improve it."
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

uploaded_file = st.file_uploader(
    "Upload your résumé (PDF format only)",
    type=["pdf", "txt"]
)

job_role = st.text_input(
    "Enter your desired job role (e.g., Software Engineer, Data Scientist):"
)

analyze = st.button("Analyze Résumé")

# ---------- helper functions ----------
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

def extract_text_from_file(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(io.BytesIO(uploaded_file.read()))
    return uploaded_file.read().decode("utf-8")

# ---------- main action ----------
if analyze and uploaded_file:
    try:
        file_content = extract_text_from_file(uploaded_file)

        if not file_content.strip():
            st.error("File does not have any content... Please check the file.")
            st.stop()

        prompt = f"""Please analyze this resume and provide constructive feedback on how to improve it.
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role if job_role else 'general job applications'}

        Resume content:
        {file_content}

        Please provide your feedback in a clear and concise manner with specific recommendations.
        """

        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "You are an expert resume reviewer with years of experience in HR and recruitment."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )

        st.markdown("### Analysis Results")
        st.markdown(response.choices[0].message.content)

    except Exception as e:
        st.error(f"An error occurred while processing the file: {e}")
