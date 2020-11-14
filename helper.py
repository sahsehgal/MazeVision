import numpy

def get_random_x_y(rows, cols):
    x = numpy.random.randint(low=0, high=rows, size=None, dtype='l')
    y = numpy.random.randint(low=0, high=cols, size=None, dtype='l')
    return x, y

def get_start_coordinates(maze, rows, cols):
    x, y = get_random_x_y(rows, cols)
    while(maze[x][y] == 'X'):
        x, y = get_random_x_y(rows, cols)
    return x, y

def get_end_coordinates(maze, rows, cols):
    x, y = get_random_x_y(rows, cols)
    while(maze[x][y] in ['X', 'P']):
        x, y = get_random_x_y(rows, cols)
    return x, y

def generate_portals(maze, rows, cols):
    # For portal 1
    for i in range(0,2):
        x, y = get_random_x_y(rows, cols)
        while(maze[x][y] in ['X', 'P', 'E', 'H']):
            x, y = get_random_x_y(rows, cols)
        list1 = list(maze[x])
        list1[y] = 'H'
        maze[x] = ''.join(list1)

    # For portal 2
    for i in range(0,2):
        x, y = get_random_x_y(rows, cols)
        while(maze[x][y] in ['X', 'P', 'E', 'H', 'K']):
            x, y = get_random_x_y(rows, cols)
        list1 = list(maze[x])
        list1[y] = 'K'
        maze[x] = ''.join(list1)

    return maze

def generate_random_cell_values(maze, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == ' ':
                list1 = list(maze[i])
                list1[j] = str(numpy.random.randint(low=1, high=3, size=None, dtype='l'))
                maze[i] = ''.join(list1)
    return maze


def randomize_maze_board(maze):
    rows = len(maze)
    cols = len(maze[0])
    x, y = get_start_coordinates(maze, rows, cols)
    list1 = list(maze[x])
    list1[y] = 'P'
    maze[x] = ''.join(list1)

    x, y = get_end_coordinates(maze, rows, cols)
    list1 = list(maze[x])
    list1[y] = 'E'
    maze[x] = ''.join(list1)
    maze = generate_portals(maze, rows, cols)
    maze = generate_random_cell_values(maze, rows, cols)
    return maze
    