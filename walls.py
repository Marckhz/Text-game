import ITEMS, controls, world

class MAP:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplemtedError()

    def playerstat(self, player):
        raise NotImplemtedError()

class Scene_1(MAP):
    def intro_text(self):
        return """
        Estas en una habitacion oscura
        """

    def  playerstat(self, player):
        pass

class LootRoom(MAP):
    def __init__(self,x,y, item):
        self.item = item
        super().__init__(x,y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def playerstat(self, player):
        self.add_loot(player)


class  Room1(MAP):
    def intro_text(self):

        return """
        Vaya esta habitacion luce similar, a excepcion de  la mesa de trabajo

                  supongo que ha de ser alguna clase de estudio
                  """
class  hall1(MAP):
    #lleva a room 2
    def intro_text(self):

        return """
        Es una pasillo largo...la iluminacion no va bien...
        """

class FindKey(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Item.Key())

    def intro_text(self):

        return """ hey...esta llave, de seguro podre salir de este lugar..."""

class FindLetter(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, Item.Letter())

    def __init__(self):

        return """ una carta...que carajos..."""

class ExitRoom(MAP):
    def __init__(self):

        return """He escapado...espero que sea el fin..."""

    def playerstat(self, player):
        player.victory = True


def move_around(self):

    moves = []
    if world.tales_exist(self.x +1, self.y):
        moves.append(Controls.mEast())
    if world.tales_exist(self.x -1,self.y):
        moves.append(Controls.mWest())
    if world.tales_exist(self.x, self.y -1):
        moves.append(Controls.mNorth())
    if world.tales_exist(self.x, self.y +1):
        moves.append(Controls.mSouth())
    return moves

def avalible_action(self):

    moves = self.move_around()
    moves.append(Controls.inventory())

    return moves
