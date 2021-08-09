import mysql.connector

mydb = mysql.connector.connect(
    host='remotemysql.com',
    user='hqZySr5tq9',
    password='DMf7H5UB4X',
    port='3306',
    database='hqZySr5tq9'
)

mycursor = mydb.cursor()

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


class GameID:
    def __init__(self):
        query = "select id from gameresult"
        mycursor.execute(query)
        self.result = mycursor.fetchall()
    def get_result(self):
        return self.result


class GameDate:
    def __init__(self):
        query = "select game_date from gameresult"
        mycursor.execute(query)
        self.result = mycursor.fetchall()
    def get_result(self):
        return self.result


class Red:
    def __init__(self):
        query = "select top, jungle, mid, adc, support from redteam"
        mycursor.execute(query)
        self.result = mycursor.fetchall()
    def get_result(self):
        return self.result


class Blue:
    def __init__(self):
        query = "select top, jungle, mid, adc, support from blueteam"
        mycursor.execute(query)
        self.result = mycursor.fetchall()
    def get_result(self):
        return self.result


class Red_Result:
    def __init__(self):
        query = "select redteam_result from gameresult"
        mycursor.execute(query)
        self.result = mycursor.fetchall()
    def get_result(self):
        return self.result


class Blue_Result:
    def __init__(self):
        query = "select blueteam_result from gameresult"
        mycursor.execute(query)
        self.result = mycursor.fetchall()
    def get_result(self):
        return self.result