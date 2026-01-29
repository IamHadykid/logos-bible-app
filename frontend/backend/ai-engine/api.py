from fastapi import FastAPI
from logos_engine import LogosEngine

app = FastAPI()
engine = LogosEngine()

@app.get("/")
def home():
    return {"status": "Logos AI Engine is running"}

@app.post("/ask")
def ask_logos(question: str):
    response = engine.generate_response(question)
    return {"answer": response}
