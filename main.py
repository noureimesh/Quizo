from pymongo import MongoClient
from fastapi import FastAPI,  Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from datasource.repository import QuizRepository

client= MongoClient("mongodb+srv://test:1234@cluster0.guuo75j.mongodb.net/?retryWrites=true&w=majority",uuidRepresentation='standard')
app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/quizzes")
async def get_quizzes():
    quizzes = QuizRepository.get_quizzes()
    
@app.get("/quizzes/{quiz_id}")
async def get_quiz():
    pass