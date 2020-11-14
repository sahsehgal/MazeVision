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

class Optimal_path:
    optimal_path = []
    min_cost = 100000000

    def dfs(self, maze, rows, cols, i, j, path, cost, visited):
        neighbours = [(-1,0), (1, 0), (0, -1), (0, 1)]
        for neighbour in neighbours:
            x = i + neighbour[0]
            y = j + neighbour[1]
            if x < 0 or y < 0 or x>= rows or y >= cols or ((x,y) in visited) or maze[x][y] == 'X':
                continue
            if(maze[x][y] == 'E'):
                if(cost < self.min_cost):
                    self.min_cost = cost
                    self.optimal_path = path.copy()
                # print (path, cost)
                return 
            if maze[x][y] not in ['P', 'H', 'K']:
                cost += int(maze[x][y])
            visited.add((x,y))
            path.append((x,y))
            self.dfs(maze, rows, cols, x, y, path, cost, visited)
            if maze[x][y] not in ['P', 'H', 'K']:
                cost -= int(maze[x][y])
            path.remove((x,y))
            visited.discard((x,y))
        return
        

def find_optimal_path(maze):
    rows = len(maze)
    cols = len(maze[0])
    x, y = -1, -1
    for i in range(0, rows):
        for j in range(0, cols):
            if (maze[i][j] == 'P'):
                x, y = i, j
    path = [(x,y)]
    cost = 0
    visited = set((x, y))
    obj = Optimal_path()
    obj.dfs(maze, rows, cols, x, y, path, cost, visited)
    print ("min cost w path", obj.optimal_path, obj.min_cost)
    return obj.optimal_path, obj.min_cost