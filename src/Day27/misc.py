from tkinter import *



def btn_click():
    def popup_btn_click():
        label.config(text=popup_wnd_input.get())
        popup_window.destroy()
    global label_var
    popup_window = Tk()
    popup_window.title("Success")
    popup_window.geometry("200x100")
    popup_wnd_label = Label(popup_window, text="Enter new value", font=("Consolas", 12, "bold"))
    popup_wnd_label.pack()
    popup_wnd_input = Entry(popup_window)
    popup_wnd_input.pack()
    label_var = popup_wnd_input.get()
    popup_wnd_button = Button(popup_window, text="Close", command=popup_btn_click)
    popup_wnd_button.pack()


main_window = Tk()


main_window.geometry("600x400")
main_window.title("Tkinter application demo")
main_window.resizable(width=False, height=False)
main_window.config(padx=10, pady=10)

label = Label(text="Initial", font=("Consolas", 20, "bold"))
label.grid(column=0, row=0, columnspan=2)
label.config(padx=10, pady=10)

btn = Button(text="Edit Label", command=btn_click)
btn.grid(column=2, row=1)
btn.config(padx=5, pady=10)

btn_exit = Button(text="Exit", command=main_window.destroy)
btn_exit.grid(column=3, row=0)
btn_exit.config(padx=5, pady=10)

main_window.mainloop()
