# API contract
from src.shared.option import Option
from src.shared.question import Question
from pydantic import BaseModel,Field

class Quiz(BaseModel):
    id: str= Field()
    label: str = Field()
    questions : list[Question]=[]
