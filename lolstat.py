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
    def __init__(self, id, top, jungle, mid, adc, support):
        self.id = id
        self.top = top
        self.jungle = jungle
        self.mid = mid
        self.adc = adc
        self.support = support

        query = "INSERT INTO redteam (id, top, jungle, mid, adc, support) values (%s, %s, %s, %s, %s, %s)"
        val = (id, top, jungle, mid, adc, support)
        mycursor.execute(query, val)
        mydb.commit()

class Blueteam:
    def __init__(self, id, top, jungle, mid, adc, support):
        self.id = id
        self.top = top
        self.jungle = jungle
        self.mid = mid
        self.adc = adc
        self.support = support

        query = "INSERT INTO blueteam (id, top, jungle, mid, adc, support) values (%s, %s, %s, %s, %s, %s)"
        val = (id, top, jungle, mid, adc, support)
        mycursor.execute(query, val)
        mydb.commit()

class GameResult:
    def __init__(self, redteam, blueteam):
        self.redteam = redteam
        self.blueteam = blueteam


        query = "INSERT INTO gameresult (redteam_result, blueteam_result) values (%s, %s)"
        val = (redteam, blueteam)
        mycursor.execute(query, val)
        mydb.commit()

class NewUser:
    def __init__(self, name, rank, position):
        self.name = name
        self.rank = rank
        self.position = position

        query = "INSERT INTO users (summonername, ranktier, mainposition) values (%s, %s, %s)"
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


class RedteamResult:
    def __init__(self):
        query = "select gameresult.id, redteam.top, redteam.jungle, redteam.mid, redteam.adc, redteam.support, gameresult.redteam_result from gameresult join redteam on gameresult.id = redteam.id order by gameresult.id desc limit 1"
        mycursor.execute(query)
        result = mycursor.fetchall()
        for x in result:
            print(x)

class GamesPlayedOnRedTeam:
    def __init__(self, name):
        self.name = name
        query = "select count(gameresult.id) as totalgame from gameresult join redteam on gameresult.id = redteam.id where %s in (top, mid, jungle, adc, support)"
        mycursor.execute(query, (name, ))
        result = mycursor.fetchall()
        for x in result:
            print(x[0])

class GamesPlayedOnBlueTeam:
    def __init__(self, name):
        self.name = name
        query = "select count(gameresult.id) as totalgame from gameresult join blueteam on gameresult.id = blueteam.id where %s in (top, mid, jungle, adc, support)"
        mycursor.execute(query, (name, ))
        result = mycursor.fetchall()
        for x in result:
            print(x[0])

class TotalGames:
    def __init__(self, name):
        self.name = name
        query = "select count(gameresult.id) as totalgame from gameresult join blueteam on gameresult.id = blueteam.id join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support, blueteam.top, blueteam.jungle, blueteam.mid, blueteam.adc, blueteam.support)"
        mycursor.execute(query, (name, ))
        result = mycursor.fetchall()
        for x in result:
            print(x[0])

# class UpdateTotal:
#     query = "select summonername from users"
#     mycursor.execute(query)
#     result = mycursor.fetchall()
#     for x in result:
#         for y in x:
#             query2 = "update users set totalgame = (select count(gameresult.id) as totalgame from gameresult join blueteam on gameresult.id = blueteam.id join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support, blueteam.top, blueteam.jungle, blueteam.mid, blueteam.adc, blueteam.support)) where summonername = %s"
#             mycursor.execute(query2, (y, y))
#             mydb.commit()
#
# class UpdateWins:
#     query = "select summonername from users"
#     mycursor.execute(query)
#     result = mycursor.fetchall()
#     for x in result:
#         for y in x:
#             query2 = "update users set wins = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support, blueteam.top, blueteam.jungle, blueteam.mid, blueteam.adc, blueteam.support) and gameresult.redteam_result = 1 or gameresult.blueteam_result = 1) where summonername = %s"
#             mycursor.execute(query2, (y, y))
#             mydb.commit()
#
# class UpdateLoss:
#     query = "select summonername from users"
#     mycursor.execute(query)
#     result = mycursor.fetchall()
#     for x in result:
#         for y in x:
#             query2 = "update users set loss = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support, blueteam.top, blueteam.jungle, blueteam.mid, blueteam.adc, blueteam.support) and where (gameresult.redteam_result = 0) or (gameresult.blueteam_result = 0)) where summonername = %s"
#             mycursor.execute(query2, (y, y))

class WinLoss:
    query = "select lower(summonername) from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    winval = []
    lossval = []
    for x in result:
        for y in x:
            red_query = "update users set red_wins = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 1) where summonername = %s"
            mycursor.execute(red_query, (y, y))
            mydb.commit()

    for x in result:
        for y in x:
            blue_query = "update users set blue_wins = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 1) where summonername = %s"
            mycursor.execute(blue_query, (y, y))
            mydb.commit()

    for x in result:
        for y in x:
            red_query = "update users set red_loss = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 0) where summonername = %s"
            mycursor.execute(red_query, (y, y))
            mydb.commit()

    for x in result:
        for y in x:
            blue_query = "update users set blue_loss = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 0) where summonername = %s"
            mycursor.execute(blue_query, (y, y))
            mydb.commit()

    for x in result:
        for y in x:
            sum_query = "select red_loss+blue_loss from users where summonername = %s"
            mycursor.execute(sum_query, (y, ))
            sum_result = mycursor.fetchall()
            lossval = sum_result[0][0]

    for x in result:
        for y in x:
            sum_query = "select red_wins+blue_wins from users where summonername = %s"
            mycursor.execute(sum_query, (y, ))
            sum_result = mycursor.fetchall()
            winval = sum_result[0][0]
            # for a in sum_result:
            #     print(a[0])

    for x in result:
        for y in x:
            win_query = "update users set wins = %s where summonername = %s"
            mycursor.execute(win_query, (winval, y))
            mydb.commit()

    for x in result:
        for y in x:
            loss_query = "update users set loss = %s where summonername = %s"
            mycursor.execute(loss_query, (lossval, y))
            mydb.commit()

# GamesPlayedOnRedTeam("Suppresser")
# User(1, "Bluecrime", "lincon9", "Flearce", "Enblanc", "churchhistory")
# Blueteam(1, "Dragonjin", "Suppresser", "gpoh508", "Dami Bbo", "Oys4410"
# GameResult(False, True)
# Testing("Suppresser", "Platinum", "Jungle")
# r_result = input("Red: ")
# b_result = input("Blue: ")
# gid = input("Game ID: ")
# top = input("Top: ")
# jungle = input("Jungle: ")
# mid = input("Mid: ")
# adc = input("ADC: ")
# support = input("Support: ")

# GameResult(r_result, b_result)
# Redteam(gid, top, jungle, mid, adc, support)
# Blueteam(gid, top, jungle, mid, adc, support)

