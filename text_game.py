import sqlite3

conn = sqlite3.connect('test1.db')
print "Online"
cursor = conn.cursor()

print "Registro \n "

def user_register():

    NOMBRE = raw_input('Nombre : ')
    APELLIDO = raw_input('Apellido :')
    EDAD = raw_input('Edad : ')
    CORREO = raw_input('correo: ')

    cursor.execute(
    "INSERT INTO REG_PLAYERS( ID, NOMBRE, APELLIDO, EDAD, CORREO)\
    VALUES(1, ?, ?, ?, ?)",(NOMBRE, APELLIDO, EDAD, CORREO))


def crate_character():

    NICK_NAME = raw_input('Nombre de tu personaje: ')
    RAZA = raw_input('RAZA DE TU PERSONAJE: ')
    SEXO = raw_input('Sexo de tu personaje: ')

    cursor.execute(
    "INSERT INTO PERSONAJE(NICK_NAME, RAZA, SEXO)\
    VALUES(?,?,?)",(NICK_NAME, RAZA, SEXO))
