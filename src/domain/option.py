from uuid import uuid4,UUID
from pydantic import BaseModel, Field
from bson import ObjectId
from src.domain.py_object_id import PyObjectId

class Option(BaseModel): 
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    label: str= Field()
    
    class config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {PyObjectId: str}
