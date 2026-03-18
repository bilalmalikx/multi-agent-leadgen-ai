from app.tools.google_search import search_company

def research_agent(company: str):
    data = search_company(company)
    return {"company_info": data}