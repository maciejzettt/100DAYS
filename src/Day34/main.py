from data import question_data
from ui import Quizzler

question_bank = [{"question": q["question"], "answer": q["correct_answer"]} for q in question_data]

quiz = Quizzler(question_bank)
