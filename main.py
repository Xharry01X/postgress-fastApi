from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool

class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]  # Corrected the usage of List

@app.post("/questions/")
def create_question(question: QuestionBase):
    return question
