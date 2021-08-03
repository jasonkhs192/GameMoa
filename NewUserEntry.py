import GameMoa.lolstat
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Test GUI")
root.geometry() # length x width + x coordinate + y coordinate
root.resizable(False, False) # resize screen size true or false on x and y

label1 = Label(root, text="Summoner Name: ")
label1.grid(row=0, column=0)
txt = Entry(root, width=23)
txt.grid(row=0, column=1)
label2 = Label(root, text="Rank: ")
label2.grid(row=1, column=0)

rank = ["Unranked", "Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grand Master", "Challenger"]
values = [str(x) for x in rank]

combobox1 = ttk.Combobox(root, height=5, values=values, state="readonly")
combobox1.grid(row=1, column=1)
combobox1.set("-Select Rank-")

label3 = Label(root, text="Main Role: ")
label3.grid(row=2, column=0)

position = ["Top", "Jungle", "Mid", "ADC", "Support", "Any"]
values2 = [str(x) for x in position]

combobox2 = ttk.Combobox(root, height=5, values=values2, state="readonly")
combobox2.grid(row=2, column=1)
combobox2.set("-Select Main Position-")


def cmd():
    name_val = txt.get().lower()
    rank_val = combobox1.get()
    pos_val = combobox2.get()
    if name_val != "" and GameMoa.lolstat.CheckUser(name_val).get_result() == False and rank_val in rank and pos_val in position:
        GameMoa.lolstat.WinLoss()
        GameMoa.lolstat.NewUser(name_val, rank_val, pos_val)
        GameMoa.lolstat.WinLoss()
    else:
        print("Error")


button1 = Button(root, text="Submit", bg="yellow", fg="red", command=cmd)
button1.grid(row=3, column=1)
root.mainloop()