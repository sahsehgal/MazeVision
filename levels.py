

def get_maze(index):
    level_1 = [
    "X       ",
    "X      X",
    "X X    X",
    "        "
    ]

    level_2 = [
    "XXXXX XXX   XX  X  X",
    "  XX                ",
    "X        XXXX     XX",
    "X                   ",
    "X  XXXXX  XXX     XX",
    "XX              XXXX",
    "   XXX  X   XX      ",
    "XX             X   X"
    ]

    level_3 = [
    "XXXXXX  X   XXXXX       ",
    "X         XXX   XXXXXX  ",
    "X  XXXX                 ",
    "X    XXX           XXXXX",
    "XX        XXX    XXXX  X",
    "XXXXXX        XX      XX",
    "XXX        XXXX         ",
    "                       X",
    "XXX    XX             XX",
    "XXXXX XXXX XXXXX   XXXXX"
    ]

    level_4 = [
    "XXXXXXXX XXX XXXXX     XXX  XXXX",
    "  X      XXXX          X      XX",
    "X XXX               XX          ",
    "                             XXX",
    "X                  XX   XXX   XX",
    "XX   XX      XXX               X",
    "X      XX                    XXX",
    "XX      X                     XX",
    "XXXXXX        XX          XX    ",
    "XX   XXXX                   XXXX",
    "         X                 XXXXX",
    "X                       XX  XXXX",
    "XXXXXXXXX                      X",
    "XXXXX                    XXXXX X",
    "XXX   XX     XXX            XX X",
    ]

    level_5 = [
    "XXXXXX   XXX XX  XXX     XXX      XXXX",
    "XXX                             X  XXX",
    "X                                 XXXX",
    "X                        XX         XX",
    "     XXX   XX                         ",
    "XX                   XX             XX",
    "XX      XXX                          X",
    "X         XXXX                X       ",
    "XXXX   XX           XX                ",
    "X             XXXX                 XXX",
    "XXXXXXX             XXX            XXX",
    "X                             XXXXXXXX",
    "XXXX       XXX   X                    ",
    "XXXXXXXX          XXXXX              X",
    "XX           XXX          XX          ",
    "XXX                                  X",
    "XX                          XXXXXXXXXX",
    "XXXXXXXXXX XXX X X    XXXXX   XX    XX",
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
    
