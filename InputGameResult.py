import GameMoa.lolstat
from tkinter import *
import tkinter.ttk as ttk

root = Tk()
root.title("Test GUI")

date = Label(text="Date", width=9, relief="ridge")
date.grid(row=0, column=0)
side = Label(text="Side", width=9, relief="ridge")
side.grid(row=0, column=1)
top = Label(text="Top", width=9, relief="ridge")
top.grid(row=0, column=2)
jungle = Label(text="Jungle", width=9, relief="ridge")
jungle.grid(row=0, column=3)
mid = Label(text="Mid", width=9, relief="ridge")
mid.grid(row=0, column=4)
adc = Label(text="ADC", width=9, relief="ridge")
adc.grid(row=0, column=5)
support = Label(text="Support", width=9, relief="ridge")
support.grid(row=0, column=6)
result = Label(text="Result", width=9, relief="ridge")
result.grid(row=0, column=7)

date_entry = Entry(root, width=10, justify="center")
date_entry.grid(row=1, column=0, rowspan=2, padx=1, pady=1, ipady=10)
date_entry.insert(0, "YYYY-MM-DD")

red_side = Label(root, width=10, text="Red Team", justify="center")
red_side.grid(row=1, column=1)
top_entry = Entry(root, width=10, justify="center")
top_entry.grid(row=1, column=2)
jungle_entry = Entry(root, width=10, justify="center")
jungle_entry.grid(row=1, column=3)
mid_entry = Entry(root, width=10, justify="center")
mid_entry.grid(row=1, column=4)
adc_entry = Entry(root, width=10, justify="center")
adc_entry.grid(row=1, column=5)
support_entry = Entry(root, width=10, justify="center")
support_entry.grid(row=1, column=6)
option = ["Win", "Lose"]
winlose = [str(x) for x in option]
result_entry = ttk.Combobox(root, width=7, height=5, values=winlose, state="readonly")
result_entry.grid(row=1, column=7)

blue_side = Label(root, width=10, text="Blue Team", justify="center")
blue_side.grid(row=2, column=1)
top_entry2 = Entry(root, width=10, justify="center")
top_entry2.grid(row=2, column=2)
jungle_entry2 = Entry(root, width=10, justify="center")
jungle_entry2.grid(row=2, column=3)
mid_entry2 = Entry(root, width=10, justify="center")
mid_entry2.grid(row=2, column=4)
adc_entry2 = Entry(root, width=10, justify="center")
adc_entry2.grid(row=2, column=5)
support_entry2 = Entry(root, width=10, justify="center")
support_entry2.grid(row=2, column=6)
result_entry2 = ttk.Combobox(root, width=7, height=5, values=winlose, state="readonly")
result_entry2.grid(row=2, column=7)


def cmd():
    red_top = top_entry.get().lower()
    red_jungle = jungle_entry.get().lower()
    red_mid = mid_entry.get().lower()
    red_adc = adc_entry.get().lower()
    red_support = support_entry.get().lower()

    blue_top = top_entry2.get().lower()
    blue_jungle = jungle_entry2.get().lower()
    blue_mid = mid_entry2.get().lower()
    blue_adc = adc_entry2.get().lower()
    blue_support = support_entry2.get().lower()

    players = [red_top, red_jungle, red_mid, red_adc, red_support, blue_top, blue_jungle, blue_mid, blue_adc, blue_support]
    game_date = date_entry.get()
    if result_entry.get() == "Win":
        red_result = 1
    else:
        red_result = 0
    if result_entry2.get() == "Win":
        blue_result = 1
    else:
        blue_result = 0

    if red_result == 1 and blue_result == 1:
        print("Error - Both team cannot win")
        exit()
    else:
        print("Error - Both team cannot lose")
        exit()

    check_count = 0

    for player in players:
        if player != "" and GameMoa.lolstat.CheckUser(player).get_result() == True:
            check_count += 1

    if check_count == 10:
        GameMoa.lolstat.Redteam(red_top, red_jungle, red_mid, red_adc, red_support)
        GameMoa.lolstat.Blueteam(blue_top, blue_jungle, blue_mid, blue_adc, blue_support)
        GameMoa.lolstat.GameResult(red_result, blue_result, game_date)
    else:
        print("Error - not valid user")

button1 = Button(root, text="Save", command=cmd)
button1.grid(row=3, column=3)
root.mainloop()