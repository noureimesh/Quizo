# API contract
from src.shared.option import Option
from pydantic import BaseModel,Field

class Question(BaseModel):
    id: str= Field()
    label: str = Field()
    options : list[Option]=[]
