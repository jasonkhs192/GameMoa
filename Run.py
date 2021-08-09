import tkinter as tk
import tkinter.ttk as ttk
import GameMoa.DB_GameResult
import GameMoa.DB_User

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
        tk.Button(self, text="Input Game Result",
                  command=lambda: master.switch_frame(PageTwo)).pack(fill="x", pady=2)
        tk.Button(self, text="View Player Stats",
                  command=lambda: master.switch_frame(PageThree)).pack(fill="x", pady=2)
        tk.Button(self, text="View Game Results",
                  command=lambda: master.switch_frame(PageFour)).pack(fill="x", pady=2)


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

            if name_val == "" or rank_val == "" or pos_val == "":
                print("There is/are empty field.")
            else:
                GameMoa.DB_User.NewUser(name_val, rank_val, pos_val)


        button1 = tk.Button(self, text="Submit", bg="yellow", fg="red", command=cmd)
        button1.grid(row=3, column=1)

        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=3, column=1, sticky="E")


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        date = tk.Label(self, text="Date", width=12, relief="ridge")
        date.grid(row=0, column=0)
        side = tk.Label(self, text="Side", width=12, relief="ridge")
        side.grid(row=0, column=1)
        top = tk.Label(self, text="Top", width=16, relief="ridge")
        top.grid(row=0, column=2)
        jungle = tk.Label(self, text="Jungle", width=16, relief="ridge")
        jungle.grid(row=0, column=3)
        mid = tk.Label(self, text="Mid", width=16, relief="ridge")
        mid.grid(row=0, column=4)
        adc = tk.Label(self, text="ADC", width=16, relief="ridge")
        adc.grid(row=0, column=5)
        support = tk.Label(self, text="Support", width=16, relief="ridge")
        support.grid(row=0, column=6)
        result = tk.Label(self, text="Result", width=8, relief="ridge")
        result.grid(row=0, column=7)

        date_entry = tk.Entry(self, width=14, justify="center")
        date_entry.grid(row=1, column=0, rowspan=2, padx=1, pady=1, ipady=10)
        date_entry.insert(0, "YYYY-MM-DD")

        red_side = tk.Label(self, width=12, text="Red Team", justify="center")
        red_side.grid(row=1, column=1)
        top_entry = tk.Entry(self, width=18, justify="center")
        top_entry.grid(row=1, column=2)
        jungle_entry = tk.Entry(self, width=18, justify="center")
        jungle_entry.grid(row=1, column=3)
        mid_entry = tk.Entry(self, width=18, justify="center")
        mid_entry.grid(row=1, column=4)
        adc_entry = tk.Entry(self, width=18, justify="center")
        adc_entry.grid(row=1, column=5)
        support_entry = tk.Entry(self, width=18, justify="center")
        support_entry.grid(row=1, column=6)
        option = ["Win", "Lose"]
        winlose = [str(x) for x in option]
        result_entry = tk.ttk.Combobox(self, width=6, height=5, values=winlose, state="readonly")
        result_entry.grid(row=1, column=7)

        blue_side = tk.Label(self, width=12, text="Blue Team", justify="center")
        blue_side.grid(row=2, column=1)
        top_entry2 = tk.Entry(self, width=18, justify="center")
        top_entry2.grid(row=2, column=2)
        jungle_entry2 = tk.Entry(self, width=18, justify="center")
        jungle_entry2.grid(row=2, column=3)
        mid_entry2 = tk.Entry(self, width=18, justify="center")
        mid_entry2.grid(row=2, column=4)
        adc_entry2 = tk.Entry(self, width=18, justify="center")
        adc_entry2.grid(row=2, column=5)
        support_entry2 = tk.Entry(self, width=18, justify="center")
        support_entry2.grid(row=2, column=6)
        result_entry2 = tk.ttk.Combobox(self, width=6, height=5, values=winlose, state="readonly")
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

            players = [red_top, red_jungle, red_mid, red_adc, red_support, blue_top, blue_jungle, blue_mid, blue_adc,
                       blue_support]
            game_date = date_entry.get()

            if result_entry.get() == "Win":
                red_result = 1
            elif result_entry.get() == "Lose":
                red_result = 0
            else:
                red_result = None

            if result_entry2.get() == "Win":
                blue_result = 1
            elif result_entry2.get() == "Lose":
                blue_result = 0
            else:
                blue_result = None


            if red_result == 1 and blue_result == 1:
                print("Error - Both team cannot win")
            elif red_result == 0 and blue_result == 0:
                print("Error - Both team cannot lose")
            elif red_result == None and blue_result != None:
                print("Red team result invalid")
            elif red_result != None and blue_result == None:
                print("Blue team result invalid")
            else:
                print("Red and Blue team result invalid")

            check_count = 0

            for player in players:
                if player != "" and GameMoa.DB_User.CheckUser(player).get_result() == True:
                    check_count += 1

            if check_count == 10:
                GameMoa.DB_GameResult.GameResult(red_result, blue_result, game_date)
                GameMoa.DB_GameResult.Redteam(red_top, red_jungle, red_mid, red_adc, red_support)
                GameMoa.DB_GameResult.Blueteam(blue_top, blue_jungle, blue_mid, blue_adc, blue_support)

            else:
                print("Error - not valid user")

        button1 = tk.Button(self, text="Save", command=cmd)
        button1.grid(row=3, column=3)
        tk.Button(self, text="Back",
                  command=lambda: master.switch_frame(StartPage)).grid(row=3, column=4)


class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=1)

        my_canvas = tk.Canvas(main_frame, width=1325, height=600)
        my_canvas.pack(side="left", fill="both", expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
        my_scrollbar.pack(side="right", fill="y")

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda f: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = tk.Frame(my_canvas)

        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        column_list = ["Index", "ID", "Rank", "Main Role", "Win Rate %", "Total Game", "Win", "Loss", "Red Win",
                       "Red Loss",
                       "Blue Win", "Blue Loss"]
        i = 0
        for column in column_list:
            c = tk.Label(second_frame, width=13, text=column, relief="ridge", borderwidth=2, font="helvetica 10 bold")
            c.grid(row=0, column=i + 1)
            i += 1

        result = GameMoa.DB_User.UsersAll().get_result()
        i = 1
        for x in result:
            j = 1
            for y in x:
                e = tk.Label(second_frame, text=y, width=15, justify="center", relief="ridge")
                e.grid(row=i, column=j)
                j += 1
            i += 1

        tk.Button(self, text="Back", width=10, command=lambda: master.switch_frame(StartPage)).pack()


class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        main_frame = tk.Frame(self)
        main_frame.pack(fill="both", expand=1)

        my_canvas = tk.Canvas(main_frame, width=990, height=1000)
        my_canvas.pack(side="left", fill="both", expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
        my_scrollbar.pack(side="right", fill="y")

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        second_frame = tk.Frame(my_canvas)

        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        column_list = ["Match", "Date", "Side", "Top", "Jungle", "Mid", "ADC", "Support", "Result"]
        i = 0
        for column in column_list:
            c = tk.Label(second_frame, width=13, text=column, relief="ridge", borderwidth=2, font="helvetica 10 bold")
            c.grid(row=0, column=i)
            i += 1

        result = GameMoa.DB_GameResult.GameID().get_result()
        i = 1
        for x in result:
            c = tk.Label(second_frame, width=15, text=x[0], relief="ridge", height=2)
            c.grid(row=i, column=0, rowspan=2)
            i += 2

        result = GameMoa.DB_GameResult.GameDate().get_result()
        game_counts = (len(result))
        i = 1
        for x in result:
            c = tk.Label(second_frame, width=15, text=x[0], relief="ridge", height=2)
            c.grid(row=i, column=1, rowspan=2)
            i += 2

        for x in range(1, game_counts * 2, 2):
            tk.Label(second_frame, text="Red Team", width=15, relief="ridge").grid(row=x, column=2)
            tk.Label(second_frame, text="Blue Team", width=15, relief="ridge").grid(row=x + 1, column=2)

        result = GameMoa.DB_GameResult.Red().get_result()
        i = 1
        for x in result:
            j = 3
            for y in x:
                e = tk.Label(second_frame, text=y, width=15, justify="center", relief="ridge")
                e.grid(row=i, column=j)
                j += 1
            i += 2

        result = GameMoa.DB_GameResult.Blue().get_result()
        i = 2
        for x in result:
            j = 3
            for y in x:
                e = tk.Label(second_frame, text=y, width=15, justify="center", relief="ridge")
                e.grid(row=i, column=j)
                j += 1
            i += 2

        result = GameMoa.DB_GameResult.Red_Result().get_result()
        i = 0
        r = 0
        for x in result:
            if x[0] == 1:
                r = "Win"
            elif x[0] == 0:
                r = "Lose"
            c = tk.Label(second_frame, width=15, text=r, relief="ridge")
            c.grid(row=i + 1, column=8)
            i += 2

        result = GameMoa.DB_GameResult.Blue_Result().get_result()
        i = 1
        r = 0
        for x in result:
            if x[0] == 1:
                r = "Win"
            elif x[0] == 0:
                r = "Lose"
            c = tk.Label(second_frame, width=15, text=r, relief="ridge")
            c.grid(row=i + 1, column=8)
            i += 2

        tk.Button(self, text="Back", width=10, command=lambda: master.switch_frame(StartPage)).pack()




app = SampleApp()
app.mainloop()
