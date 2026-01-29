from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

class BibleQuestion(BaseModel):
    question: str

@app.post("/ask")
async def ask_bible_ai(data: BibleQuestion):
    prompt = f"""
You are a Bible scholar and teacher.
Answer the question using scripture, wisdom, and clear explanation.

Question: {data.question}

Answer:
"""

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Bible scholar."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )

    return {"answer": response.choices[0].message.content}
