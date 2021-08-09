import mysql.connector

mydb = mysql.connector.connect(
    host='remotemysql.com',
    user='5iBhNlaY6v',
    password='LyNQnlWhvW',
    port='3306',
    database='5iBhNlaY6v'
)

mycursor = mydb.cursor()