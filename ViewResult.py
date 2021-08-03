import mysql.connector
import tkinter as tk
from tkinter import *
my_w = tk.Tk()
my_w.geometry("860x250")
my_connect = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='moadb'
)
my_conn = my_connect.cursor()
####### end of connection ####
my_conn.execute("SELECT * FROM users")
result = my_conn.fetchall()
column_list = ["Index", "ID", "Rank", "Main Role", "Total Game", "Win", "Loss", "Red Win", "Red Loss", "Blue Win", "Blue Loss"]
for x in result:
    length = len(x)
    break

for x in range(length):
    c = Label(my_w, width=9, text=column_list[x], relief="ridge", borderwidth=2, font="helvetica 10 bold")
    c.grid(row=0, column=x+1)

i = 1
for x in result:
    j = 1
    for y in x:
        e = Entry(my_w, width=12, justify="center")
        e.grid(row=i, column=j)
        e.insert(END, y)
        j += 1
    i += 1
my_w.mainloop()