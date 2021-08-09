from tkinter import *

def login():
    pass

def register():
    pass

def main_screen():
    root = Tk()
    Button(text="Login", commang=login()).pack()
    Button(text="Register", command=register()).pack()
    root.mainloop()

main_screen()

# user login > check login from db > if success session created