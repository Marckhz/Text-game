import sqlite3

conn = sqlite3.connect('test1.db')

print "DB is online"

conn.execute('''CREATE TABLE REG_PLAYERS(
            ID INT PRIMARY KEY NOT NULL,
            NOMBRE VARCHAR(30),
            APELLIDO VARCHAR (30),
            EDAD INT NOT NULL,
            CORREO VARCHAR(30)
            )''')

print "table is up"

conn.close()
