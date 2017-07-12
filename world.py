import walls

world = {}
starting_position = (0,0)

def load_map():

    with open('my_Tales.txt', 'r') as f:
        rows = f.readlines()
    x_rows = len(rows[0].split('\t'))
    for i in range(len(rows)):
        colm = rows[i].split('\t')
        for k in range(x_rows):
            tales_name = colm[k].replace('\n', ' ')
            if tales_name == "Scene_1":
                global starting_position
                starting_position = (i, k)
            #world[(i, j)] = None if tales_name == '' else getattr(__import__("walls"), tales_name(i,j)


#def tales_exist(a, b):
#    return world.get((i, j))
