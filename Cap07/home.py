# coding : utf-8
import mysql.connector
from pprint import pprint

dbconfig = {
    'host': '127.0.0.1',
    'user': 'vsearch',
    'password': '123456',
    'database': 'vsearchlogDB'
}
conn = mysql.connector.connect(**dbconfig)

# É necessário criar um cursor para interagir com o BD
cursor = conn.cursor()
# _SQL = """show tables"""
_SQL = """insert into log (phrase, letters, ip, browser_string, results)
    values(%s,%s,%s,%s,%s)"""
cursor.execute(_SQL, (req.form['phrase'],req.form['letters'],req.remote_addr,req.user_agent.browser,res))
conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)

for row in cursor.fetchall():
    pprint(row)

cursor.close()
conn.close()
