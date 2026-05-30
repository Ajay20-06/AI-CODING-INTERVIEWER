from agents.interviewer_agent import generate_question
from agents.evaluvator_agent import evaluate_answer
from agents.hint_agent import generate_hint
from agents.followup_agent import generate_followup


class InterviewService:

    def start_interview(self, topic="Arrays"):
        question = generate_question(topic)
        return question

    def evaluate(self, question, answer):
        return evaluate_answer(question, answer)

    def hint(self, question):
        return generate_hint(question)

    def followup(self, topic):
        return generate_followup(topic)