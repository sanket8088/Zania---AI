from pydantic import BaseModel, Field

class QuestionResponse(BaseModel):
        answer:str = Field(..., description="Response of the question asked")
        confidence_score:float = Field(..., description="Confidence score of the answer")