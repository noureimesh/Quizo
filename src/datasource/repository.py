#dealing with database operations only , no application logic
import sys

from mongomock import MongoClient

class QuizRepository: 
    def __init__(self, database_client: MongoClient):
        self.database_client = database_client

    def get_quizzes(self):
        return list(self.database_client.db.quiz.find())
    
    def get_quiz(self,quiz_id):
        return self.database_client.db.quiz.find_one({"_id":quiz_id})

      