from src.datasource.seed import FIRST_SEEDED_QUIZ_ID, generate_quizzes,FIRST_SEEDED_QUIZ_FIRST_QUESTION_ID,FIRST_SEEDED_QUIZ_FIRST_QUESTION_OPTION_ID
from src.domain.py_object_id import PyObjectId
from src.domain.quiz_service import QuizService
from src.shared.quiz import Quiz
from src.shared.view_quiz import ViewQuiz


class MockRepository:
    def __init__(self) -> None:
        self.quzzies = generate_quizzes()

    def get_quizzes(self)-> list[dict]:
       return self.quzzies
    
    def get_quiz(self,quiz_id : str)-> dict:
        for quiz in self.quzzies:
            if(quiz_id == str(quiz.get("_id"))):
                return quiz
        return None

def test_get_quizzes():
    mock_repository = MockRepository()
    service = QuizService(repository = mock_repository)
    quizzes = service.get_quizzes()
    assert isinstance(quizzes,list)  
    source_quizzes = generate_quizzes()
    for quiz in quizzes:
       for source_quiz in source_quizzes:
        if source_quiz.get("id") == quiz.id :
            assert source_quiz.get("label") == quiz.label

def test_get_quiz():
    mock_repository = MockRepository()
    service = QuizService(repository = mock_repository)
    quiz = service.get_quiz(FIRST_SEEDED_QUIZ_ID)
    source_quizzes = generate_quizzes()
    for source_quiz in source_quizzes:
        if str(source_quiz.get("_id")) == quiz.id:
            source_quiz_data = source_quiz
            break
    assert source_quiz_data != None
    assert quiz.label == source_quiz_data.get("label")
    assert len(quiz.questions) == len(source_quiz.get("questions"))

def test_non_existing_quiz():
    mock_repository = MockRepository()
    service = QuizService(repository = mock_repository)
    quiz = service.get_quiz("666f6f2d6261722d71757577")
    assert quiz == None

def test_solve_quiz():
    mock_repository = MockRepository()
    service = QuizService(repository = mock_repository)
    solve_quiz = service.solve_quiz(quiz_id= FIRST_SEEDED_QUIZ_ID,question_answer_dict={FIRST_SEEDED_QUIZ_FIRST_QUESTION_ID : FIRST_SEEDED_QUIZ_FIRST_QUESTION_OPTION_ID})
    assert solve_quiz.quiz_id == FIRST_SEEDED_QUIZ_ID
    assert solve_quiz.total_questions_count == 3
    assert solve_quiz.correct_answers_count == 1
