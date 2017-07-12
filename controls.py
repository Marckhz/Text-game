import player

class  Controls():
    def __init__(self, method, name, hotkeys, **kwargs):
        self.method = method
        self.name = name
        self.hotkeys = hotkeys
        self.kwargs  = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkeys, self.name)


class mNorth(Controls):
    def __init__(self):
        super().__init__(method = player.go_north, name = 'move north', hotkeys = 'n')

class mSouth(Controls):
    def __init__(self):
        super().__init__(method = player.go_south, name = 'move south ', hotkeys = 's')

class mWest(Controls):
    def __init__(self):
        super().__init__(method = player.go_west, name = 'move west ', hotkeys = 'w')

class mEast(Controls):
    def __init__(self):
        super().__init__(method = player.go_east, name = 'move east', hotkeys = 'e')

class readItem(Controls):
    def __init__(self):
        super().__init__(method = player.inventory, name = 'read item', hotkeys = 'r')

class inventory(Controls):
    def __init__(self):
        super().__init__(method = player.inventory, name = 'view Inventory', hotkeys = 'i')
