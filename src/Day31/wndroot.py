from tkinter import *
import os.path
import random
import pandas


DIR = os.path.dirname(__file__)
BGCOLOUR = '#B1DDC6'

class FlashCardWnd:

    def __init__(self, title: str, default_words_file) -> None:
        
        self._words = self.prepare_words_list(default_words_file)
        self.current_word = {}
        self._wnd = Tk()
        self._frame = Frame(self._wnd, padx=20, pady=20, bg=BGCOLOUR)
        self._canvas_image_front = PhotoImage(file=os.path.join(DIR, "images/card_front.png"))
        self._canvas_image_back = PhotoImage(file=os.path.join(DIR, "images/card_back.png"))
        self._btn_right_image = PhotoImage(file=os.path.join(DIR, "images/right.png"))
        self._btn_wrong_image = PhotoImage(file=os.path.join(DIR, "images/wrong.png"))
        self._canvas = Canvas(self._frame, height=526, width=800, bd=0, bg=BGCOLOUR, highlightthickness=0)
        self._btn_right = Button(self._frame, image=self._btn_right_image, highlightthickness=0, relief="solid", command=self.btn_right_click)
        self._btn_wrong = Button(self._frame, image=self._btn_wrong_image, highlightthickness=0, relief="solid", command=self.btn_wrong_click)
        
        self._wnd.title(title)
        self._wnd.resizable(False, False)
        self._wnd.config(bg=BGCOLOUR)
        self._card_background = self._canvas.create_image(0, 0, image=self._canvas_image_front, anchor='nw')
        
        self._frame.pack()
        self._canvas.grid(column=0, row=0, columnspan=2)
        self._btn_right.grid(column=0, row=1, padx=30, pady=10)
        self._btn_wrong.grid(column=1, row=1, padx=30, pady=10)
        
        self._txt_lang = self._canvas.create_text(400, 150, font=("Arial", 40, "italic"), text="")
        self._txt_word = self._canvas.create_text(400, 260, font=("Arial", 60, "bold"), text="")
        
        self._word_timer = self._wnd.after(40000, self.flip_card)
        self.next_word()
        
        self._wnd.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self._wnd.mainloop()

    def prepare_words_list(self, default_file) -> list:
        if os.path.exists(os.path.join(DIR, "data/words_to_learn.csv")):
            print("Reading from previously saved data.")
            file = os.path.join(DIR, "data/words_to_learn.csv")
        else:
            print("Reading from new data.")
            file = default_file
        raw_words = pandas.read_csv(file)
        words = raw_words.to_dict(orient="records")
        return words
        
    def next_word(self) -> None:
        self._wnd.after_cancel(self._word_timer)
        self._canvas.itemconfig(self._card_background, image=self._canvas_image_front)
        self.current_word = random.choice(self._words)
        self._canvas.itemconfig(self._txt_lang, text="French")
        self._canvas.itemconfig(self._txt_word, text=self.current_word.get("French"))
        self._word_timer = self._wnd.after(4000, self.flip_card)
        
    def flip_card(self) -> None:
        self._canvas.itemconfig(self._card_background, image=self._canvas_image_back)
        self._canvas.itemconfig(self._txt_lang, text="English")
        self._canvas.itemconfig(self._txt_word, text=self.current_word.get("English"))
        
    def btn_right_click(self) -> None:
        self._words.remove(self.current_word)
        self.next_word()
    
    def btn_wrong_click(self) -> None:
        self.next_word()
    
    def on_closing(self) -> None:
        print("Received close signal")
        df = pandas.DataFrame.from_dict(self._words)
        print(f"Dataframe created\n{df}")
        df.to_csv(os.path.join(DIR, "data/words_to_learn.csv"), index=False)
        print("File saved. Exiting...")
        self._wnd.destroy()