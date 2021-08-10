import mysql.connector

mydb = mysql.connector.connect(
    host='remotemysql.com',
    user='hqZySr5tq9',
    password='DMf7H5UB4X',
    port='3306',
    database='hqZySr5tq9'
)
mycursor = mydb.cursor()

name_query = "select summonername from users"
mycursor.execute(name_query)
result = mycursor.fetchall()
lst = []
for x in result:
    for y in x:
        lst.append(y)

def redwin():
    for x in lst:
        red_query = "update users set red_wins = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 1) where summonername = %s"
        mycursor.execute(red_query, (x, x))
        mydb.commit()


def redloss():
    for x in lst:
        red_query = "update users set red_loss = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 0) where summonername = %s"
        mycursor.execute(red_query, (x, x))
        mydb.commit()

def bluewin():
    for x in lst:
        blue_query = "update users set blue_wins = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 1) where summonername = %s"
        mycursor.execute(blue_query, (x, x))
        mydb.commit()


def blueloss():
    for x in lst:
        blue_query = "update users set blue_loss = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 0) where summonername = %s"
        mycursor.execute(blue_query, (x, x))
        mydb.commit()


def sumloss():
    for x in lst:
        sum_query = "select red_loss+blue_loss from users where summonername = %s"
        mycursor.execute(sum_query, (x, ))
        sum_result = mycursor.fetchall()
        lossval = sum_result[0]

        for i in lossval:
            query2 = "update users set loss = %s where summonername = %s"
            mycursor.execute(query2, (i, x))
            mydb.commit()


def sunwin():
    for x in lst:
        sum_query = "select red_wins+blue_wins from users where summonername = %s"
        mycursor.execute(sum_query, (x, ))
        sum_result = mycursor.fetchall()
        winval = sum_result[0]

        for i in winval:
            query2 = "update users set wins = %s where summonername = %s"
            mycursor.execute(query2, (i, x))
            mydb.commit()


def totalgame():
    for x in lst:
        sum_query = "select wins + loss from users where summonername = %s"
        mycursor.execute(sum_query, (x, ))
        sum_result = mycursor.fetchall()
        totalval = sum_result[0]

        for i in totalval:
            query2 = "update users set totalgame = %s where summonername = %s"
            mycursor.execute(query2, (i, x))
            mydb.commit()

def winrate():
    for x in lst:
        sum_query = "select round((wins / totalgame *100), 2) from users where summonername = %s"
        mycursor.execute(sum_query, (x, ))
        sum_result = mycursor.fetchall()
        winrate = str(sum_result[0][0])
        query2 = "update users set win_rate = %s where summonername = %s"
        mycursor.execute(query2, (winrate, x))
        mydb.commit()

