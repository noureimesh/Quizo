from pydantic import BaseModel,Field

class ViewQuizDto(BaseModel):
    id: str= Field()
    label: str = Field()