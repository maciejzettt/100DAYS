from tkinter import *
import os.path
import threading
import sys


DIR = os.path.dirname(__file__)
BGCOLOUR = '#B1DDC6'

class FlashCardWnd:

    def __init__(self, title: str, words_dict) -> None:
        self._title = title
        self._words = words_dict
        
    def compose(self) -> None:
        self._wnd = Tk()
        self._frame = Frame(self._wnd, padx=20, pady=20, bg=BGCOLOUR)
        self._canvas_image = PhotoImage(file=os.path.join(DIR, "images/card_front.png"))
        self._btn_right_image = PhotoImage(file=os.path.join(DIR, "images/right.png"))
        self._btn_wrong_image = PhotoImage(file=os.path.join(DIR, "images/wrong.png"))
        self._canvas = Canvas(self._frame, height=526, width=800, bd=0, bg=BGCOLOUR, highlightthickness=0)
        self._btn_right = Button(self._frame, image=self._btn_right_image, highlightthickness=0, relief="solid", command=self.change_language)
        self._btn_wrong = Button(self._frame, image=self._btn_wrong_image, highlightthickness=0, relief="solid")
        
        self._wnd.title(self._title)
        self._wnd.resizable(False, False)
        self._wnd.config(bg=BGCOLOUR)
        self._canvas.create_image(0, 0, image=self._canvas_image, anchor='nw')
        
        self._frame.pack()
        self._canvas.grid(column=0, row=0, columnspan=2)
        self._btn_right.grid(column=0, row=1, padx=30, pady=10)
        self._btn_wrong.grid(column=1, row=1, padx=30, pady=10)
        
        self._txt_lang = self._canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="language")
        self._txt_word = self._canvas.create_text(400, 260, font=("Arial", 60, "bold"), text="word")
        
        self._wnd.mainloop()

        
    def change_language(self) -> None:
        self._canvas.itemconfig(self._txt_lang, {'text': "English"})
        
    def set_language(self, language: str) -> None:
        self._canvas.itemconfig(self._txt_lang, {'text': language})
        
    def set_word(self, word: str) -> None:
        self._canvas.itemconfig(self._txt_word, text=word)
        
    