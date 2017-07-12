import world
from player import player


def play():

    world.load_map()
    player = player()
    while player.alive() and not player.victory:
        room = world.tales_exist(player.location_x, player.location_y)
        print (room.intro_text())
    while  player.alive() and not player.victory:
        room = world.tales_exist(player.location_x, player.location_y)
        room.playerstat(player)
        if player.alive() and not player.victory:
            print('Elije una accion..\n')
            avalible_action = room.avalible_action()
            for action in avalible_action:
                print(action)
            action_input = raw_input('Action')
            for action in avalible_action:
                if action_input == action.hotkeys:
                    player.do_something(action, **action.kwargs)
                    break

if __name__=="__main__":
    play()
