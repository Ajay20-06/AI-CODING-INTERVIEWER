from services.llm_service import ask_llm


def generate_question(topic: str):
    prompt = f"""
    You are a DSA coding interviewer.

    Generate one medium-level coding interview question on:
    {topic}

    Give:
    1. Problem statement
    2. Example input/output
    3. Constraints
    """

    return ask_llm(prompt)