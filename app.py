import streamlit as st
from utils.model_loader import load_embedding_model
from utils.pdf_parser import extract_text_from_pdf
from modules.sourcing import resume_matching
from modules.hiring import generate_interview_summary
from modules.growth import skill_gap_analysis
from modules.performance import analyze_feedback
from modules.attrition import train_attrition_model, predict_attrition
import nltk

nltk.download('vader_lexicon')

st.title("AI HR Lifecycle System")

model = load_embedding_model()
attrition_model = train_attrition_model()

st.header("1. Resume Screening")

job_description = st.text_area("Enter Job Description")
uploaded_resume = st.file_uploader("Upload Resume PDF", type=["pdf"])

if uploaded_resume:
    resume_text = extract_text_from_pdf(uploaded_resume)
    
    if st.button("Match Resume"):
        score = resume_matching(model, job_description, resume_text)
        st.success(f"Semantic Match Score: {score}%")


st.header("2. AI Interview Evaluation")

interview_text = st.text_area("Paste Interview Transcript")

if st.button("Generate Evaluation"):
    result = generate_interview_summary(interview_text)
    st.write(result)

st.header("3. Skill Gap Analysis")

req = st.text_input("Required Skills")
emp = st.text_input("Employee Skills")

if st.button("Analyze"):
    matched, missing = skill_gap_analysis(req, emp)
    st.write("Matched Skills:", matched)
    st.write("Missing Skills:", missing)


st.header("4. Performance Feedback")

feedback = st.text_area("Enter Feedback")

if st.button("Analyze Feedback"):
    sentiment = analyze_feedback(feedback)
    st.write(sentiment)


st.header("5. Attrition Prediction")

years = st.number_input("Years at Company", 0, 30)
performance = st.number_input("Performance Score (1-10)", 1, 10)
promotion = st.selectbox("Promotion in Last 2 Years?", [0,1])

if st.button("Predict"):
    result = predict_attrition(attrition_model, years, performance, promotion)
    if result == 1:
        st.error("High Risk of Leaving")
    else:
        st.success("Likely to Stay")