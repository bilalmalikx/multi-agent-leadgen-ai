from fastapi import APIRouter
from app.services.lead_service import process_lead

router = APIRouter()

@router.post("/lead")
def create_lead(name: str, company: str):
    result = process_lead(name, company)
    return result