# -*- coding: utf-8 -*-

class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
         return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

class Key(Item):
    def __init__(self, old):
        self.old = old
        super().__init__(name = 'key',
                         description= 'es una llave vieja, creo que solo sera usada una vez',
                         value = 'no tiene valor alguno')
class Weapon(Item):
    def __init__(self, bow):
        self.bow = bow
        super().__init__(name = 'Sphyx',
                        description = 'es un arco de madera muy basico',
                        value= 'Tiene un valor sentimental, no creo poder venderlo')
class Coin(Item):
    def __init__(self, coin):
        self.coin = coin
        super().__init__(name = 'Moneda',
                        description = 'Unas cuantas monedas, que me dejo mi padre, no creo que tegan valor alguno',
                        value = '????')

class Letter(Item):
    def __init__(self, letter):
        self.letter = letter
        super().__init__(letter = "carta misteriosa",
                         description = """El acertijo has de descifrar si quieres avanzar,
                         El terror es una sensación de miedo muy intensa,
                         El miedo se define como una perturbación angustiosa del ánimo por un riesgo real o imaginario,
                         cuando éste supera los controles cerebrales y el sujeto no puede pensar de forma racional, aparece el terror,
                         No lejos de Madrid, hay un granero muy grande de madera. El granero está completamente vacío,  excepto por un hombre muerto que cuelga del medio de la viga central,
                         La cuerda alrededor de su cuello mide tres metros de largo y los pies del hombre cuelgan a una distancia de un metro del suelo. El muro más cercano está a 6 metros de distancia del hombre,
                         Hay un charco de agua cerca.  No es posible escalar por las paredes o subir a las vigas,
                         El hombre se colgó él solo.  ¿Como lo hizo?
                         """)
