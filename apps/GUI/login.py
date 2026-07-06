from tkinter import *
from tkinter import ttk

def render_login_page():
    root = Tk()
    root.title("Password Manager")
    root.geometry("1000x600")

    canvas = Canvas(root, width=400, height=300)   
    canvas.pack()

    frame = Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    frame.pack()

    title = Label(frame, text="LoginPage", font=("Arial", 20), bg="white")
    title.pack()


    root.mainloop()
