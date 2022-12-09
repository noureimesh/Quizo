from pydantic import BaseModel,Field

class ViewQuiz(BaseModel):
    id: str= Field()
    label: str = Field()
