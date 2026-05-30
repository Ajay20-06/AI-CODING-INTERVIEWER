from fastapi import FastAPI
from pydantic import BaseModel

from services.interview_services import InterviewService

app = FastAPI()

service = InterviewService()


class AnswerRequest(BaseModel):
    question: str
    answer: str


@app.get("/")
def home():
    return {
        "message": "AI Coding Interview Agent Running"
    }


@app.get("/start")
def start_interview(topic: str = "Arrays"):
    question = service.start_interview(topic)

    return {
        "question": question
    }


@app.post("/evaluate")
def evaluate_answer(data: AnswerRequest):
    result = service.evaluate(data.question, data.answer)

    return {
        "evaluation": result
    }


@app.get("/hint")
def get_hint(question: str):
    hint = service.hint(question)

    return {
        "hint": hint
    }


@app.get("/followup")
def followup(topic: str = "Arrays"):
    question = service.followup(topic)

    return {
        "followup_question": question
    }