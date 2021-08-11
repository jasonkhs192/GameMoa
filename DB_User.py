import mysql.connector

mydb = mysql.connector.connect(
    host='remotemysql.com',
    user='hqZySr5tq9',
    password='DMf7H5UB4X',
    port='3306',
    database='hqZySr5tq9'
)

mycursor = mydb.cursor()


class NewUser:
    def __init__(self, name, rank, position):
        self.name = name
        self.rank = rank
        self.position = position

        query = "INSERT INTO users (summonername, ranktier, mainposition, red_wins, red_loss, blue_wins, blue_loss) values (%s, %s, %s, 0, 0, 0, 0)"
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

class UsersAll:
    def __init__(self):
        query = "select * from users"
        mycursor.execute(query)
        self.result = mycursor.fetchall()

    def get_result(self):
        return self.result