from fastapi import FastAPI
from pydantic import BaseModel
from logos_engine import LogosEngine

app = FastAPI()
engine = LogosEngine()

class Question(BaseModel):
    question: str

@app.get("/")
def home():
    return {"status": "Logos AI Engine Running"}

@app.post("/ask")
def ask_logos(data: Question):
    response = engine.generate_response(data.question)
    return {"answer": response}
