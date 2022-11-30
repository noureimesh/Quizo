# API contract
from src.shared.option_dto import OptionDto
from pydantic import BaseModel,Field

class QuestionDto(BaseModel):
    id: str= Field()
    label: str = Field()
    options : list[OptionDto]=[]
