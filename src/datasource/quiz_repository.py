#dealing with database operations only , no application logic
from bson import ObjectId

from pymongo import MongoClient

from src.domain.quiz import Quiz

class QuizRepository: 
    def __init__(self, database_client: MongoClient):
        self.database_client = database_client

    def get_quizzes(self) -> list[dict]:
        return list(self.database_client.db.quiz.find())
    
    def get_quiz(self,quiz_id :str) -> dict :
        return self.database_client.db.quiz.find_one({"_id":ObjectId(quiz_id)})
