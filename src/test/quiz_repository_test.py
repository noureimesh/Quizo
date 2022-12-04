import mongomock
from bson.binary import UuidRepresentation
from src.datasource.quiz_repository import QuizRepository
from src.datasource.seed import FIRST_SEEDED_QUIZ_ID, generate_quizzes

def test_get_quizzes():
    seed_quizzes = generate_quizzes()
    client = mongomock.MongoClient(uuidRepresentation=UuidRepresentation.STANDARD)
    quiz_collection = client.db.quiz
    quiz_collection.insert_many(seed_quizzes)
    repo = QuizRepository(database_client= client)
    quizzes = repo.get_quizzes()
    assert len(quizzes) == 2

def test_get_quiz():
    seed_quizzes = generate_quizzes()
    client = mongomock.MongoClient(uuidRepresentation=UuidRepresentation.STANDARD)
    quiz_collection = client.db.quiz
    quiz_collection.insert_many(seed_quizzes)
    repo = QuizRepository(database_client= client)
    
    first_quiz=seed_quizzes[0]
    first_quiz_id=first_quiz["_id"]

    quiz = repo.get_quiz(first_quiz_id)
    assert quiz == first_quiz