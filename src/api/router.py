# append the path of the parent directory in order to import from src
import sys
sys.path.append("..")

from pymongo import MongoClient
from fastapi import APIRouter, HTTPException
from src.datasource.seed import generate_quizzes
from src.datasource.quiz_repository import QuizRepository
from src.domain.quiz_service import QuizService
from src.domain.py_object_id import PyObjectId
from src.shared.quiz_dto import QuizDto
from src.shared.solve_quiz_dto import SolveQuizDto

from src.shared.view_quiz_dto import ViewQuizDto
router = APIRouter()

def get_mongo_client():
    return MongoClient("mongodb+srv://test:1234@cluster0.guuo75j.mongodb.net/?retryWrites=true&w=majority",uuidRepresentation='standard')

def get_service():
    client= get_mongo_client()
    quiz_repository = QuizRepository(client)
    quiz_service = QuizService(quiz_repository)
    return quiz_service

#TODO: For development only / remove when release
@router.get("/seed")
async def seed() -> None:
    seed_quizzes = generate_quizzes()
    client= get_mongo_client()
    quiz_collection = client.db.quiz
    quiz_collection.insert_many(seed_quizzes)

@router.get("/quizzes")
async def get_quizzes()-> list[ViewQuizDto]:
    return get_service().get_quizzes()
    
@router.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id : str) -> QuizDto:
    quiz = get_service().get_quiz(quiz_id)
    if(quiz == None):
         raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz 

@router.post("/quiz/{quiz_id}/solution")
async def solve_quiz(quiz_id : str, question_answer_dict: dict[PyObjectId, PyObjectId])-> SolveQuizDto:
    return get_service().solve_quiz(quiz_id,question_answer_dict)
