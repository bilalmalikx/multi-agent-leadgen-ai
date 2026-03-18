def qualifier_agent(data: dict):
    # simple scoring logic
    score = 80 if "tech" in data["company_info"].lower() else 50
    return score