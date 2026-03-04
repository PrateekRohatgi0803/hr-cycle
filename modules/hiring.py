import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_interview_summary(interview_text):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a professional HR evaluator."},
            {"role": "user", "content": f"""
            Analyze this interview.
            Give:
            1. Technical Score (out of 10)
            2. Communication Score
            3. Strengths
            4. Weaknesses
            5. Final Recommendation

            Interview:
            {interview_text}
            """}
        ]
    )

    return response.choices[0].message.content