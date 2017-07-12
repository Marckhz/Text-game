import ITEMS


class player():
    def __init__(self):
        self.inventory = [Item.bow, Item.coin]
        self.hp = 100
        self.location_x, self.location_y, = world.start
        self.victory = False

    def alive(self):
        return self.hp > 0

    def inventory():
        for item in self.inventory:
            print(Item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.title_exist(self.location_x, self.location_y).intro_text())

    def go_north(self):
        self.move(dx = 0, dy = -1)

    def go_south(self):
        self.move(dx= 0, dy = -1)

    def go_east(self):
        self.move(dx=1, dy = 0)

    def go_west(self):
        self.move(dx= -1, dy = 0)

    def do_something(self, control,  **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
