#coding = utf-8
import mysql.connector

dbconfig = {
    'host': 'localhost',
    'user': 'vsearch',
    'password': '123456',
    'database': 'vsearchlogDB'
}
con = mysql.connector.connect(**dbconfig)

cursor = con.cursor()

_SQL = """select * from log"""

cursor.execute(_SQL)

for row in cursor.fetchall():
    print(row)

cursor.close()
con.close()
