from services.llm_service import ask_llm


def generate_hint(question: str):
    prompt = f"""
    Give a small hint for this DSA problem.

    Do not reveal full solution.

    Problem:
    {question}
    """

    return ask_llm(prompt)