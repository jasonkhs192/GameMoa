import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    port='3306',
    database='moadb'
)

mycursor = mydb.cursor()
# user = mycursor.fetchall()
#
# for x in user:
#     print("Summoner Name: {}\nRank: {}\n".format(x[1], x[2]))


class Redteam:
    def __init__(self, top, jungle, mid, adc, support):
        self.top = top
        self.jungle = jungle
        self.mid = mid
        self.adc = adc
        self.support = support

        query = "INSERT INTO redteam (top, jungle, mid, adc, support) values (%s, %s, %s, %s, %s)"
        val = (top, jungle, mid, adc, support)
        mycursor.execute(query, val)
        mydb.commit()


class Blueteam:
    def __init__(self, top, jungle, mid, adc, support):
        self.top = top
        self.jungle = jungle
        self.mid = mid
        self.adc = adc
        self.support = support

        query = "INSERT INTO blueteam (top, jungle, mid, adc, support) values (%s, %s, %s, %s, %s)"
        val = (top, jungle, mid, adc, support)
        mycursor.execute(query, val)
        mydb.commit()


class GameResult:
    def __init__(self, redteam, blueteam, game_date):
        self.redteam = redteam
        self.blueteam = blueteam
        self.game_date = game_date

        query = "INSERT INTO gameresult (redteam_result, blueteam_result, game_date) values (%s, %s, %s)"
        val = (redteam, blueteam, game_date)
        mycursor.execute(query, val)
        mydb.commit()


class NewUser:
    def __init__(self, name, rank, position):
        self.name = name
        self.rank = rank
        self.position = position

        query = "INSERT INTO users (summonername, ranktier, mainposition, win_rate, totalgame, wins, loss, red_wins, red_loss, blue_wins, blue_loss) values (%s, %s, %s, -, 0, 0, 0, 0, 0, 0, 0)"
        val = (name, rank, position)
        mycursor.execute(query, val)
        mydb.commit()


class CheckUser:
    def __init__(self, name):
        self.name = name

        query = "Select lower(summonername) from users"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for x in result:
            if x[0] == name:
                self.result2 = True
                break
            else:
                self.result2 = False

    def get_result(self):
        return self.result2


class RedWin:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    winval = []
    lossval = []
    totalval = []
    winrate = []
    # Set users red team wins
    for x in result:
        for y in x:
            red_query = "update users set red_wins = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 1) where summonername = %s"
            mycursor.execute(red_query, (y, y))
            mydb.commit()


class RedLose:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()

    # Set users red team loss
    for x in result:
        for y in x:
            red_query = "update users set red_loss = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 0) where summonername = %s"
            mycursor.execute(red_query, (y, y))
            mydb.commit()


class BlueWin:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()

    # Set users blue team wins
    for x in result:
        for y in x:
            blue_query = "update users set blue_wins = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 1) where summonername = %s"
            mycursor.execute(blue_query, (y, y))
            mydb.commit()


class BlueLose:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()

    # Set users blue team loss
    for x in result:
        for y in x:
            blue_query = "update users set blue_loss = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 0) where summonername = %s"
            mycursor.execute(blue_query, (y, y))
            mydb.commit()


class SumLose:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # add users red team loss and blue team loss
    for x in result:
        for y in x:
            sum_query = "select red_loss+blue_loss from users where summonername = %s"
            mycursor.execute(sum_query, (y, ))
            sum_result = mycursor.fetchall()
            lossval = sum_result[0]

        for i in lossval:
            query2 = "update users set loss = %s where summonername = %s"
            mycursor.execute(query2, (i, y))
            mydb.commit()


class SumWin:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # add users red team wins and blue team wins
    for x in result:
        for y in x:
            sum_query = "select red_wins+blue_wins from users where summonername = %s"
            mycursor.execute(sum_query, (y, ))
            sum_result = mycursor.fetchall()
            winval = sum_result[0]

        for i in winval:
            query2 = "update users set wins = %s where summonername = %s"
            mycursor.execute(query2, (i, y))
            mydb.commit()


class TotalGame:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # add users wins and loss
    for x in result:
        for y in x:
            sum_query = "select wins + loss from users where summonername = %s"
            mycursor.execute(sum_query, (y, ))
            sum_result = mycursor.fetchall()
            totalval = sum_result[0]

        for i in totalval:
            query2 = "update users set totalgame = %s where summonername = %s"
            mycursor.execute(query2, (i, y))
            mydb.commit()

class WinRate:
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # add users wins and loss
    for x in result:
        for y in x:
            sum_query = "select round((wins / totalgame *100), 2) from users where summonername = %s"
            mycursor.execute(sum_query, (y, ))
            sum_result = mycursor.fetchall()
            winrate = str(sum_result[0][0])
            query2 = "update users set win_rate = %s where summonername = %s"
            mycursor.execute(query2, (winrate, y))
            mydb.commit()
