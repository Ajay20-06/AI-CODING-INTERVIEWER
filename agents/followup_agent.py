from services.llm_service import ask_llm


def generate_followup(topic: str):
    prompt = f"""
    Generate one harder follow-up DSA interview question on:
    {topic}
    """

    return ask_llm(prompt)