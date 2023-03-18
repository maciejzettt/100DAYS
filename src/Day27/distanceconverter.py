import tkinter as tk


def errormsg(message: str):
    def dismiss():
        popup.grab_release()
        popup.destroy()

    popup = tk.Toplevel()
    popup.grab_set()
    popup.title("Error")
    msg = tk.Label(master=popup, text=message, padx=20, pady=10)
    msg.pack()
    btn = tk.Button(master=popup, text="OK", background="#CC9999", command=dismiss)
    btn.pack()


def calculate():
    try:
        miles = float(text.get())
        km = round(1.609344 * miles, 3)
        result.set(km)
    except ValueError:
        errormsg("Wrong input!\nOnly decimal numbers are allowed.")


root_wnd = tk.Tk()
root_wnd.geometry("250x150")
root_wnd.title("Distance converter")
root_wnd.resizable(False, False)

text = tk.StringVar(value="0")
result = tk.DoubleVar(value=0.0)

frm = tk.Frame(root_wnd)
frm.config(pady=30)
frm.pack(side='top')
text_input = tk.Entry(frm)
text_input.config(textvariable=text)
text_input.grid(column=0, row=0, columnspan=4)

lbl_unit = tk.Label(master=frm, text="Miles", padx=10)
lbl_unit.grid(row=0, column=4)

lbl_isequal = tk.Label(master=frm, text="Is equal to", padx=10, pady=10)
lbl_isequal.grid(column=0, row=1, columnspan=2)

lbl_result = tk.Label(master=frm, textvariable=result, font=('Arial', 10, 'bold'), justify='right', state='disabled')
lbl_result.grid(column=2, row=1, columnspan=2)

lbl_result_unit = tk.Label(master=frm, text="km")
lbl_result_unit.grid(column=4, row=1)

btn_calculate = tk.Button(master=frm, text="Calculate", command=calculate, background="#99CC99")
btn_calculate.grid(column=2, row=2, columnspan=2)

btn_exit = tk.Button(master=frm, text="Exit", command=root_wnd.destroy, background="#CC9999")
btn_exit.grid(column=4, row=2)

root_wnd.mainloop()
