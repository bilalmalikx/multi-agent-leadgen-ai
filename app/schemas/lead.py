from pydantic import BaseModel

class LeadCreate(BaseModel):
    name: str
    company: str

class LeadResponse(BaseModel):
    id: int
    name: str
    email: str
    company: str
    score: int

    class Config:
        from_attributes = True