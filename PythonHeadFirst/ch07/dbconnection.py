import mysql.connector

dbconfig = {'host': '127.0.0.1',
            'user': 'vsearch',
            'password': 'vsearchpasswd',
            'database': 'vsearchlogDB', }

conn = mysql.connector.connect(**dbconfig)
cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)
res = cursor.fetchall()

_SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
for row in res:
    print(row)

_SQL = """insert into log (phrase, letters, ip, browser_string, results) 
values ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL)

_SQL = """insert into log (phrase, letters, ip, browser_string, results) values (%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))
conn.commit()

_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
