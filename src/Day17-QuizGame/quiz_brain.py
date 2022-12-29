from question_model import Question


class QuizBrain:

    def __init__(self, question_list: list[Question]):
        self._question_list = question_list
        self._question_number = 0
        self._score = 0

    def still_has_questions(self) -> bool:
        return self._question_number < len(self._question_list)

    def serve_next_question(self):
        print()
        question = self._ask_next_question()
        user_answer = self._get_users_answer()
        if self._check_answer(user_answer, question):
            self._score += 1
            print(f"Correct answer. Your score is {self._score} of {self._question_number}.")
        else:
            print(f"Wrong answer. Your score is {self._score} of {self._question_number}.")

    def _ask_next_question(self) -> Question:
        question = self._get_next_question()
        print(f"Question {self._question_number}: {question.get_text()}")
        return question

    def _get_users_answer(self) -> bool:
        while True:
            response = input(f"Your answer for Q{self._question_number} (true/false): ")
            if response.lower() in ['true', 't', 'yes', 'y']:
                return True
            elif response.lower() in ['false', 'f', 'no', 'n']:
                return False
            else:
                print("Incorrect input: Enter 'True'/'t' or 'False'/'f'.")

    def _check_answer(self, user_answer, question) -> bool:
        return user_answer == question.get_answer()

    def _get_next_question(self) -> Question:
        if not self.still_has_questions():
            raise IndexError(f"QuizBrain: Question number {self._question_number} out of range.")
        current_question = self._question_list[self._question_number]
        self._question_number += 1
        return current_question

    def print_summary(self):
        print(f"\n\tYour quiz is over.\n"
              f"\tHere is your summary:\n"
              f"\tYour score: {self._score}.\n"
              f"\tMaximum score: {self._question_number}.")
