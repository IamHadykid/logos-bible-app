import os
from openai import OpenAI

class LogosEngine:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, question: str):
        prompt = f"""
You are a Bible scholar and teacher.
Answer the question using scripture, wisdom, and clarity.

Question: {question}

Answer:
"""

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Bible scholar AI."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300
        )

        return response.choices[0].message.content.strip()
