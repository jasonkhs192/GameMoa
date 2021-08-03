import tkinter as tk
import tkinter.ttk as ttk
import GameMoa.lolstat
import mysql.connector

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("GameMoa")
        tk.Label(self, text="Welcome GameMoa!", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Input New Player",
                  command=lambda: master.switch_frame(PageOne)).pack(fill="x", pady=2)
        tk.Button(self, text="View Results",
                  command=lambda: master.switch_frame(PageTwo)).pack(fill="x", pady=2)


class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        label1 = tk.Label(self, text="Summoner Name: ")
        label1.grid(row=0, column=0)
        txt = tk.Entry(self, width=23)
        txt.grid(row=0, column=1)
        label2 = tk.Label(self, text="Rank: ")
        label2.grid(row=1, column=0)
        rank = ["Unranked", "Iron", "Bronze", "Silver", "Gold", "Platinum", "Diamond", "Master", "Grand Master",
                "Challenger"]
        values = [str(x) for x in rank]

        combobox1 = tk.ttk.Combobox(self, height=5, values=values, state="readonly")
        combobox1.grid(row=1, column=1)
        combobox1.set("-Select Rank-")

        label3 = tk.Label(self, text="Main Role: ")
        label3.grid(row=2, column=0)

        position = ["Top", "Jungle", "Mid", "ADC", "Support", "Any"]
        values2 = [str(x) for x in position]

        combobox2 = tk.ttk.Combobox(self, height=5, values=values2, state="readonly")
        combobox2.grid(row=2, column=1)
        combobox2.set("-Select Main Position-")

        def cmd():
            name_val = txt.get().lower()
            rank_val = combobox1.get()
            pos_val = combobox2.get()
            if name_val != "" and GameMoa.lolstat.CheckUser(
                    name_val).get_result() == False and rank_val in rank and pos_val in position:

                GameMoa.lolstat.NewUser(name_val, rank_val, pos_val)

            else:
                print("Error")

            GameMoa.lolstat.WinLoss()

        button1 = tk.Button(self, text="Submit", bg="yellow", fg="red", command=cmd)
        button1.grid(row=3, column=1)

        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=3, column=1, sticky="E")


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
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
        column_list = ["Index", "ID", "Rank", "Main Role", "Total Game", "Win", "Loss", "Red Win", "Red Loss",
                       "Blue Win", "Blue Loss"]
        for x in result:
            length = len(x)
            break

        for x in range(length):
            c = tk.Label(self, width=9, text=column_list[x], relief="ridge", borderwidth=2, font="helvetica 10 bold")
            c.grid(row=0, column=x + 1)

        i = 1
        for x in result:
            j = 1
            for y in x:
                e = tk.Entry(self, width=12, justify="center")
                e.grid(row=i, column=j)
                e.insert(tk.END, y)
                j += 1
            i += 1

        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=i+1, column=j-1)

app = SampleApp()
app.mainloop()