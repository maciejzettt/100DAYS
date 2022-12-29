class Question:

    def __init__(self, question: str, answer: str):
        self. _text = question
        self._answer = answer

    def __str__(self) -> str:
        return f"Q: {self._text}; A: {self._answer}."

    def get_text(self):
        return self._text

    def get_answer(self) -> bool:
        if self._answer.lower() in ['true', 'yes']:
            return True
        elif self._answer.lower() in ['false', 'no']:
            return False
        else:
            raise ValueError(f"The question {self._text} has unrecognized answer: {self._answer}.")
