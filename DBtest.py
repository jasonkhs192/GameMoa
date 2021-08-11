import mysql.connector

# CREATE TABLE order_details (price DOUBLE, quantity INT, amount DOUBLE AS (price * quantity));
#
# INSERT INTO order_details (price, quantity) VALUES(100,1),(300,4),(60,8);

# alter table users add column win_rate varchar(100) as (round((red_wins+blue_wins)/nullif((red_wins+red_loss+blue_wins+blue_loss)*(1/100), 0), 2)) after MainPosition

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

