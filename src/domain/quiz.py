from pydantic import BaseConfig, BaseModel, Field
from src.domain.question import Question
from typing import List
from src.domain.py_object_id import PyObjectId

class Quiz(BaseModel): 
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    label: str= Field()
    questions : List[Question] = []

    def __eq__(self, other) : 
       return self.__dict__ == other.__dict__

    class Config(BaseConfig):
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
