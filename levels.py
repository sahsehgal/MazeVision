

def get_maze(index):
    level_1 = [
    "X   ",
    "    ",
    "X   "
    ]

    level_2 = [
    "X   ",
    "   X",
    "    ",
    "    "
    ]

    level_3 = [
    "  X ",
    "    ",
    "X   ",
    "   X"
    ]

    level_4 = [
    "XXXX",
    "   X",
    "X  X",
    "   X",
    "X  X"
    ]

    level_5 = [
    "XXXXX",
    "X   X",
    "X    ",
    "X  XX",
    "XX XX"
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
    
