from openai import OpenAI
from serializers import QuestionResponse
import instructor
from utils import chunk_text
class GPTClient:
    
    def __init__(self, api_key: str):
        self.api_key = api_key

    def __get_answer_with_confidence(self, context: str, question: str) -> dict:
        """Generate an answer with a confidence score based on context and question."""

        
        prompt = (
            f"Context:\n{context}\n\n"
            f"Question:\n{question}\n\n"
            "Provide an answer to the question and include from the context provided and  a confidence score from 0 to 100, where 100 is the highest confidence."
            "The confidence score should be a percentage and should be included at the end of your response."
            "If the question is not related to context provide a confidence score of 0."
        )

        messages = [{"role": "system",  "content": prompt}]
        client = instructor.patch(OpenAI(api_key= self.api_key))

        response = client.chat.completions.create(
                model="gpt-4o-mini",
                response_model=QuestionResponse,
                messages=messages
            )
        
        return {
            "answer": response.answer.strip(),
            "confidence": response.confidence_score
        }

    def answer_questions(self, text: str, questions: list) -> dict:
        """Answer questions based on the provided text."""
        answers = {}
        text_chunks = chunk_text(text)

        for question in questions:
            full_answer = None
            for chunk in text_chunks:
                response = self.__get_answer_with_confidence(chunk, question)
                if response["confidence"] == 100.00:
                    full_answer = response["answer"]
                    break
            if full_answer:
                answers[question] =full_answer.strip()
            else:
                answers[question] = "Data Not Available"

        return answers

