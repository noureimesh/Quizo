# append the path of the parent directory in order to import from src
import sys
sys.path.append("..")

from pymongo import MongoClient
from fastapi import APIRouter
from src.datasource.seed import generate_quizzes
from src.datasource.repository import QuizRepository
from src.domain.service import QuizService

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
async def get_quizzes():
    seed_quizzes = generate_quizzes()
    client= get_mongo_client()
    quiz_collection = client.db.quiz
    quiz_collection.insert_many(seed_quizzes)

@router.get("/quizzes")
async def get_quizzes():
    return get_service().get_quizzes()
    
@router.get("/quizzes/{quiz_id}")
async def get_quiz(quiz_id):
    return get_service().get_quiz(quiz_id)
