# API contract
from src.shared.option_dto import OptionDto
from src.shared.question_dto import QuestionDto
from pydantic import BaseModel,Field

class QuizDto(BaseModel):
    id: str= Field()
    label: str = Field()
    questions : list[QuestionDto]=[]
