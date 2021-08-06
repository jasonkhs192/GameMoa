import mysql.connector
import tkinter.ttk as ttk
from tkinter import *

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='moadb'
)

my_cursor = my_db.cursor()

root = Tk()
root.geometry("725x450")

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)

my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)

my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

column_list = ["Match", "Date", "Side", "Top", "Jungle", "Mid", "ADC", "Support", "Result"]
i = 0
for column in column_list:
    c = Label(second_frame, width=13, text=column, relief="ridge", borderwidth=2, font="helvetica 10 bold")
    c.grid(row=0, column=i)
    i += 1

query = "select id from gameresult"
my_cursor.execute(query)
result = my_cursor.fetchall()
i = 1
for x in result:
    c = Label(second_frame, width=15, text=x[0], relief="ridge", height=2)
    c.grid(row=i, column=0, rowspan=2)
    i += 2
query = "select game_date from gameresult"
my_cursor.execute(query)
result = my_cursor.fetchall()
game_counts = (len(result))
i = 1
for x in result:
    c = Label(second_frame, width=15, text=x[0], relief="ridge", height=2)
    c.grid(row=i, column=1, rowspan=2)
    i += 2

for x in range(1, game_counts*2, 2):
    Label(second_frame, text="Red Team", width=15, relief="ridge").grid(row=x, column=2)
    Label(second_frame, text="Blue Team", width=15, relief="ridge").grid(row=x+1, column=2)

query = "select top from redteam"
my_cursor.execute(query)
result = my_cursor.fetchall()
i = 0
for x in result:
    c = Label(second_frame, width=15, text=x[0], relief="ridge")
    c.grid(row=i+1, column=3)
    i += 2

query = "select top from blueteam"
my_cursor.execute(query)
result = my_cursor.fetchall()
i = 1
for x in result:
    c = Label(second_frame, width=15, text=x[0], relief="ridge")
    c.grid(row=i+1, column=3)
    i += 2
root.mainloop()