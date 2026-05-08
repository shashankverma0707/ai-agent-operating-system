from fastapi import FastAPI
from pydantic import BaseModel

from app.orchestration.crew_manager import run_company

app = FastAPI()


class RequestBody(BaseModel):
    goal: str


@app.get("/")
def home():
    return {
        "message": "AI Company Running"
    }


@app.post("/run")
def run_ai_company(body: RequestBody):
    result = run_company(body.goal)

    return {
        "result": result
    }