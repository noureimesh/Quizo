# dealing with application logic and communicate with repositories 
from src.datasource.repository import QuizRepository
from src.shared.quiz_dto import QuizDto
from src.shared.option_dto import OptionDto
from src.shared.question_dto import QuestionDto


class QuizService:
    def __init__(self, repository : QuizRepository) :
        self.repository = repository

    def get_quizzes(self):
        quizzes = self.repository.get_quizzes()
        quiz_list : list[QuizDto] = []
        for quiz in quizzes:
            quiz_dto = self.quiz_to_dto(quiz)
            quiz_list.append(quiz_dto)
        return quiz_list

        #return quiz_list

    def get_quiz(self, quiz_id):
        quiz = self.repository.get_quiz(quiz_id)
        quiz_dto = self.quiz_to_dto(quiz)
        return quiz_dto

    def quiz_to_dto(self,quiz):
         quiz_dto = QuizDto(id= str(quiz.get("_id")), label=quiz.get("label"))
         for question in quiz.get("questions"):
            question_dto = QuestionDto(id= str(question.get("_id")), label=question.get("label"))
            for option in question.get("options"):
                question_dto.options.append(OptionDto(id = str(option.get("_id")), label=option.get("label")))
            quiz_dto.questions.append(question_dto)
         return quiz_dto