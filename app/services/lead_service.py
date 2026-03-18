from app.workflows.lead_pipeline import run_pipeline

def process_lead(name: str, company: str):
    return run_pipeline(name, company)