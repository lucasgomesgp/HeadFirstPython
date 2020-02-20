from DBcm import UseDatabase

dbconfig = {
    'host': 'localhost',
    'user': 'vsearch',
    'password': '123456',
    'database': 'vsearchlogDB'
}

with UseDatabase(dbconfig) as cursor:
    _SQL = """insert into log 
    (phrase, letters, ip, broser_string, results) 
    values (%s,%s,%s,%s,%s)"""

cursor.execute(_SQL, (req.form['phrase'],
                      req.form['letters'],
                      req.remote_addr,
                      req.user_agent.browser,
                      res))
