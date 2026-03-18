from app.agents.research_agent import research_agent
from app.agents.qualifier_agent import qualifier_agent
from app.agents.outreach_agent import outreach_agent
from app.tools.email_finder import find_email

def run_pipeline(name: str, company: str):
    research = research_agent(company)
    score = qualifier_agent(research)
    email = find_email(name, company)

    outreach = outreach_agent(name, email)

    return {
        "name": name,
        "company": company,
        "email": email,
        "score": score,
        "outreach": outreach
    }