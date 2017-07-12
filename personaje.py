import sqlite3

conn = sqlite3.connect('test1.db')

print "DB is online"

conn.execute('''CREATE TABLE PERSONAJE(
            NICK_NAME VARCHAR(30) PRIMARY KEY,
            RAZA VARCHAR(30),
            SEXO VARCHAR(30)
            REFERENCES REG_PLAYERS(ID)
            )''')
conn.commit()

conn.close()
