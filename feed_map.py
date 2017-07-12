import walls
import sqlite3

conn = sqlite3.connect('test1.db')
print 'online'
cursor = conn.cursor()
#Aqui van los detalles de el mundo#

cursor.execute("INSERT INTO MAP (BLOCK_A, BLOCK_B, BLOCK_C, BLOCK_D, BLOCK_E, BLOCK_F)\
            VALUES('Scene_1', 'hall1', 'FindKey', 'FindLetter', 'Room1', 'ExitRoom'  )")


conn.commit()
print "WE are up!"
conn.close()
