import mysql.connector

dataBase=mysql.connector.connect(
    host='db',
    user='root',
    passwd='password'
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")
print("ALL DONE")