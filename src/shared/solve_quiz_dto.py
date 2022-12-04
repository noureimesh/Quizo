
from pydantic import BaseModel,Field

class SolveQuizDto(BaseModel):
    quiz_id: str= Field()
    total_questions_count: int = Field()
    correct_answers_count: int = Field()
    
