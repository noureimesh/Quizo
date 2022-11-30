from pydantic import BaseModel, Field
from src.domain.option import Option
from typing import List
from src.domain.py_object_id import PyObjectId

class Question(BaseModel): 
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    label: str = Field()
    answer_index: int = Field(default=0)
    options : List[Option] = []

    class config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}