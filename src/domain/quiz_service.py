# dealing with application logic and communicate with repositories 
from src.datasource.quiz_repository import QuizRepository
from src.domain.py_object_id import PyObjectId
from src.domain.quiz import Quiz
from src.shared.quiz_dto import QuizDto
from src.shared.option_dto import OptionDto
from src.shared.question_dto import QuestionDto
from src.shared.solve_quiz_dto import SolveQuizDto
from src.shared.view_quiz_dto import ViewQuizDto


class QuizService:
    def __init__(self, repository : QuizRepository) :
        self.repository = repository
  

    def get_quizzes(self) -> list[ViewQuizDto]:
        quizzes = self.repository.get_quizzes()
        quiz_list : list[ViewQuizDto] = []
        for quiz in quizzes:
            quiz_list.append(ViewQuizDto(id = str(quiz.get("_id")), label= quiz.get("label")))
        return quiz_list

    def get_quiz(self, quiz_id: str) -> QuizDto:
        quiz = self.repository.get_quiz(quiz_id)
        if(quiz == None):
            return None
        quiz_dto = self.quiz_to_dto(quiz)
        return quiz_dto

    def solve_quiz(self, quiz_id: str, question_answer_dict: dict[str, str])-> SolveQuizDto:
        quiz = self.repository.get_quiz(quiz_id)
        print(quiz_id)
        correct_answers = 0
        for question in quiz.get("questions"):
            if str(question.get("answer_id")) == question_answer_dict.get(str(question.get("_id"))):
                correct_answers +=1
        solve_quiz_dto = SolveQuizDto (quiz_id = quiz_id, total_questions_count= len(quiz.get("questions")), correct_answers_count = correct_answers)
        return solve_quiz_dto

    def quiz_to_dto(self,quiz: Quiz) -> QuizDto:
         quiz_dto = QuizDto(id= str(quiz.get("_id")), label=quiz.get("label"))
         for question in quiz.get("questions"):
            question_dto = QuestionDto(id= str(question.get("_id")), label=question.get("label"))
            for option in question.get("options"):
                question_dto.options.append(OptionDto(id = str(option.get("_id")), label=option.get("label")))
            quiz_dto.questions.append(question_dto)
         return quiz_dto