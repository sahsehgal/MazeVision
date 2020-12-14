

def get_maze(index):
    level_1 = [
    "XXXXXXX",
    "X     X",
    "X     X",
    "XXXXXXX",
    ]

    level_2 = [
    "XXXXXX",
    "X    X",
    "X  X X",
    "X    X",
    "X   XX",
    "XXXXXX"
    ]

    level_3 = [
    "XXXXXXXX",
    "X  X X X",
    "X      X",
    "X  X   X",
    "X  X X X",
    "XXXXXXXX"
    ]

    level_4 = [
    "XXXXXX",
    "X  X X",
    "X  X X",
    "X    X",
    "X  X X",
    "XXXXXX",
    ]

    level_5 = [
    "XXXXXXXXXX",
    "X    X   X",
    "X        X",
    "X  XX  X X",
    "X        X",
    "X    X   X",
    "XXXXXXXXXX"
    ]

    if index == 1:
        return level_1
    elif index == 2:
        return level_2
    elif index == 3:
        return level_3
    elif index == 4:
        return level_4
    elif index == 5:
        return level_5
    
