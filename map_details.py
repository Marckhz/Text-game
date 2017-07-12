import sqlite3

conn = sqlite3.connect('test1.db')
print 'online'

cursor = conn.cursor()

#Aqui van los detalles de el mundo#


conn.execute("INSERT INTO MAP (BLOCK_A, BLOCK_B, BLOCK_C, BLOCK_D, BLOCK_E, BLOCK_F)\
            VALUES('Scene_1', 'hall1', 'FindKey', 'Room1',  'FindLetter', 'ExitRoom')")
#conn.execute("DELETE from MAP where BLOCK_A='Scene_1';")

conn.commit()

print "WE are up!"

conn.close()
