from pydantic import BaseModel

# Class which describes incoming request payload
class ResumeModel(BaseModel):
    name: str
    min_exp: int
    experience: int
    status: int
    score: int