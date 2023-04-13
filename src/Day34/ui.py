from tkinter import *
from typing import Literal
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class Quizzler:
    
    def __init__(self, questions: list) -> None:
        self._quiz_brain = QuizBrain(questions)
        self._wnd = Tk()
        self._wnd.title("Quizzler App")
        self._wnd.resizable(height=False, width=False)
        self._wnd.config(bg=THEME_COLOR)
        self._score = 0
        self._inactive = False
        
        self._frame = Frame(self._wnd, bg=THEME_COLOR)
        self._frame.pack()
        
        self._lbl_score_text = StringVar(name="_lbl_score_text", value="Score: 0")
        self._lbl_score = Label(self._frame, textvariable= self._lbl_score_text, bg=THEME_COLOR, fg='white', font=("Arial", 14, "bold"))
        
        self._canvas = Canvas(self._frame, width=300, height=250, bg='white')
        
        self._btn_yes_img = PhotoImage(file="./images/true.png")
        self._btn_no_img = PhotoImage(file="./images/false.png")
        self._btn_yes = Button(self._frame, image=self._btn_yes_img, highlightthickness=0, relief="flat", command=self._answer_yes)
        self._btn_no = Button(self._frame, image=self._btn_no_img, highlightthickness=0, relief="flat", command=self._answer_no)
        
        self._question_text = self._canvas.create_text(150, 125, text="A question will appear here when it's finally done",
                                                       fill=THEME_COLOR, font=("Arial", 16, "italic"), width=280, justify="center")
        
        self._lbl_score.grid(column=1, row=0, padx=20, pady=20)
        self._canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self._btn_yes.grid(column=0, row=2, padx=20, pady=20)
        self._btn_no.grid(column=1, row=2, padx=20, pady=20)
        
        self._next_question()

        self._wnd.mainloop()

    def _next_question(self) -> None:
        q = self._quiz_brain.next_question()
        if q == None:
            self._finish()
            return
        self._canvas.itemconfig(self._question_text, text=q)
        self._inactive = False
        
    def _answer_yes(self) -> None:
        if self._inactive:
            return
        else:
            self._answer("True")
    
    def _answer_no(self) -> None:
        if self._inactive:
            return
        else:
            self._answer("False")
    
    def _answer(self, answer: Literal["True", "False"] | bool) -> None:
        _answer = str(answer)
        is_correct = self._quiz_brain.check_answer(_answer)
        if is_correct:
            self._score += 1
            self._update_score_lbl()
            self._canvas.itemconfig(self._question_text, text="Correct answer!")
            self._inactive = True
            self._wnd.after(ms=2000, func=self._next_question)
        else:
            self._canvas.itemconfig(self._question_text, text="Your answer was wrong.")
            self._inactive = True
            self._wnd.after(ms=2000, func=self._next_question)
            
            
    def _update_score_lbl(self) -> None:
        self._lbl_score_text.set(f"Score: {self._score}")
        
    def _finish(self) -> None:
        self._inactive = True
        self._canvas.itemconfig(self._question_text, text=f"There are no more questions.\n Your final score is {self._score}.")
