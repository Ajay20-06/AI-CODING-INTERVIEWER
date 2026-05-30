from services.llm_service import ask_llm


def evaluate_answer(question: str, answer: str):
    prompt = f"""
    You are an expert coding interviewer.

    Question:
    {question}

    Candidate Answer:
    {answer}

    Evaluate:
    1. Correctness
    2. Time Complexity
    3. Space Complexity
    4. Edge Cases

    Give score out of 10.
    """

    return ask_llm(prompt)