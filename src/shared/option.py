from pydantic import BaseModel,Field

class Option(BaseModel):
    id: str= Field()
    label: str = Field()
