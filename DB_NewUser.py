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

        query = "INSERT INTO users (summonername, ranktier, mainposition, win_rate, totalgame, wins, loss, red_wins, red_loss, blue_wins, blue_loss) values (%s, %s, %s, %s, 0, 0, 0, 0, 0, 0, 0)"
        val = (name, rank, position, "NA")
        mycursor.execute(query, val)
        mydb.commit()