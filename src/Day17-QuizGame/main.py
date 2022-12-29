from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = [Question(q['question'], q['correct_answer']) for q in question_data]
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.serve_next_question()

quiz.print_summary()
