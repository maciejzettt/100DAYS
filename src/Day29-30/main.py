from tkinter import *
from tkinter import messagebox
from pwdgen import * 
from os import path
import json

DIR = path.dirname(__file__)


def save_to_file():
    validation = True
    errormsg = ""
    website = inp_website.get().strip()
    username = inp_username.get().strip()
    password = inp_password.get().strip()
    if len(website) == 0:
        validation = False
        errormsg += "No website provided.\n"
    if len(username) == 0:
        validation = False
        errormsg += "No username or email provided.\n"
    if len(password) == 0:
        validation = False
        errormsg += "No password provided"
    if validation is False:
        messagebox.showerror(title="Error", message=errormsg)
        return
    
    entry = {website: {
                    "username": username,
                    "password": password,
                }}
    if messagebox.askokcancel(title=website, message=f"Are these details correct?\nUser: {username}\nPassword: {password}"):
        if not path.exists(path.join(DIR, "passwords.json")):
            with open(path.join(DIR, "passwords.json"), mode="w") as f:
                json.dump(entry, f, indent=4)
        else:
            with open(path.join(DIR, "passwords.json"), mode="r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    messagebox.showerror(title="Error", message=f"Your date file is corrupted.\nException: {e}")     
                    return           
                data.update(entry)
            with open(path.join(DIR, "passwords.json"), mode="w") as f:
                json.dump(data, f, indent=4)
        inp_website.delete(0, END)
        inp_password.delete(0, END)
        messagebox.showinfo(title="Saved", message="Your data has been saved.")
        

def btn_generate_click():
    password = generate_password()
    inp_password.delete(0, END)
    inp_password.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)
    

def btn_search_click():
    website = inp_website.get().strip()
    try:
        with open(path.join(DIR, "passwords.json"), mode="r") as f:
            data = json.load(f)
            result = data[website]
            password = result['password']
            username = result['username']
    except FileNotFoundError as e:
        messagebox.showerror(title="Error", message=f"Data file not found:\n{e}")
    except json.JSONDecodeError as e:
        messagebox.showerror(title="Error", message=f"Your data file is corrupted or contains no data.\nException: {e}")
    except KeyError as e:
        messagebox.showerror(title="Error", message=f"Valid entry not found: {e}")     
    else:
        messagebox.showinfo(title="Search result", message=f"Login data for {website}:\nUser: {username}\nPassword: {password}")
        


window = Tk()
window.title("Password Manager")
window.resizable(False, False)

frame = Frame(window, padx=40, pady=30)

canvas = Canvas(
    frame,
    height = 191,
    width = 200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
img = PhotoImage(file=path.join(DIR, "logo.png"))
canvas.create_image(0, 0, image=img, anchor='nw')

lbl_website =       Label(frame, text="Website:")
lbl_username =      Label(frame, text="Username/Email:")
lbl_password =      Label(frame, text="Password:")

inp_website =       Entry(frame, width=30)
inp_username =      Entry(frame, width=30)
inp_password =      Entry(frame, width=30)

btn_search =        Button(frame, text="Search", width=14, command=btn_search_click)
btn_generate_pwd =  Button(frame, text="Generate Password", command=btn_generate_click)
btn_add =           Button(frame, width=43, text="Add or update", command=save_to_file)

frame.pack()
canvas.grid(column=1, row=0)
lbl_website.grid(column=0, row=1, sticky='w', padx=3, pady=2)
lbl_username.grid(column=0, row=2, sticky='w', padx=3, pady=2)
lbl_password.grid(column=0, row=3, sticky='w', padx=3, pady=2)
inp_website.grid(column=1, row=1, sticky='w', padx=3, pady=2)
inp_username.grid(column=1, row=2, sticky='w', padx=3, pady=2)
inp_password.grid(column=1, row=3, sticky='w', padx=3, pady=2)
btn_add.grid(column=1, row=4, columnspan=2, sticky='w', padx=3, pady=2)
btn_search.grid(column=2, row=1, sticky='w', padx=3, pady=2)
btn_generate_pwd.grid(column=2, row=3, sticky='w', padx=3, pady=2)

inp_website.focus()
inp_username.insert(0, "maciej@poczta.pl")



window.mainloop()
