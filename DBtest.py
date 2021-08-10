import mysql.connector

mydb = mysql.connector.connect(
    host='remotemysql.com',
    user='hqZySr5tq9',
    password='DMf7H5UB4X',
    port='3306',
    database='hqZySr5tq9'
)
mycursor = mydb.cursor()


def redwin():
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # Set users red team wins
    for x in result:
        for y in x:
            red_query = "update users set red_wins = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 1) where summonername = %s"
            mycursor.execute(red_query, (y, y))
            mydb.commit()


def redloss():
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # Set users red team loss
    for x in result:
        for y in x:
            red_query = "update users set red_loss = (select count(gameresult.id) from gameresult join redteam on gameresult.id = redteam.id where %s in (redteam.top, redteam.mid, redteam.jungle, redteam.adc, redteam.support) and gameresult.redteam_result = 0) where summonername = %s"
            mycursor.execute(red_query, (y, y))
            mydb.commit()

def bluewin():
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # Set users blue team wins
    for x in result:
        for y in x:
            blue_query = "update users set blue_wins = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 1) where summonername = %s"
            mycursor.execute(blue_query, (y, y))
            mydb.commit()


def blueloss():
    query = "select summonername from users"
    mycursor.execute(query)
    result = mycursor.fetchall()
    # Set users blue team loss
    for x in result:
        for y in x:
            blue_query = "update users set blue_loss = (select count(gameresult.id) from gameresult join blueteam on gameresult.id = blueteam.id where %s in (blueteam.top, blueteam.mid, blueteam.jungle, blueteam.adc, blueteam.support) and gameresult.blueteam_result = 0) where summonername = %s"
            mycursor.execute(blue_query, (y, y))
            mydb.commit()


def sumloss():
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


def sunwin():
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


def totalgame():
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

def winrate():
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

