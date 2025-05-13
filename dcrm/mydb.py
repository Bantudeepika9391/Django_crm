# install mysql on u r computer
# pip insatll mysql
# pip install mysql-connector 
# pip-insatll-mysql-connector-python


import mysql.connector

dataBase=mysql.connector.connect(
    host= 'localhost',
    user='root',
    passwd='Deepika12'
)
# preper a curser object
cursorObject =dataBase.cursor()
# creat a database
cursorObject.execute("CREATE DATABASE elderco")
print("ALL DONE!")