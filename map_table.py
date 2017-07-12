import sqlite3


conn = sqlite3.connect('test1.db')
print "DB is online"

conn.execute('''CREATE TABLE MAP(
            BLOCK_A VARCHAR(50) PRIMARY KEY NOT NULL,
            BLOCK_B VARCHAR(50),
            BLOCK_C VARCHAR(50),
            BLOCK_D VARCHAR(50),
            BLOCK_E VARCHAR(50),
            BLOCK_F VARCHAR(50)
            REFERENCES PERSONAJE(NICK_NAME)
            )''')



conn.commit()
conn.close()
