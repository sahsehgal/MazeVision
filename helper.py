import numpy
import turtle
import random

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

def get_level_statistics(level, level_no):
    class MazeVision():
        q_table = {}
        rewards = {}
        walls = []
        end_points = []
        start = []
        score_map = {}
        no_of_actions = 4
        visited_actions = []
        def __init__(self):
            for x in range(len(level)):
                for y in range(len(level[x])):
                    if level[x][y] == "X":
                        self.walls.append((x,y))
                        self.score_map[(x,y)] = 0
                        self.q_table[(x, y)] = [-3] * self.no_of_actions
                        self.rewards[(x, y)] = -3
                        
                    elif level[x][y] == "1":
                        self.score_map[(x,y)] = 1
                        self.q_table[(x, y)] = [-1] * self.no_of_actions
                        self.rewards[(x, y)] = -1

                    elif level[x][y] == "2":
                        self.score_map[(x,y)] = 2
                        self.q_table[(x, y)] = [-2] * self.no_of_actions
                        self.rewards[(x, y)] = -2

                    elif level[x][y] == "P":
                        self.start_x = x
                        self.start_y = y
                        self.score_map[(x,y)] = 0
                        self.q_table[(x, y)] = [-1] * self.no_of_actions
                        self.rewards[(x, y)] = -1

                    elif level[x][y] == "E":
                        self.end_points.append((x,y))
                        self.score_map[(x,y)] = 0
                        self.q_table[(x, y)] = [0] * self.no_of_actions
                        self.rewards[(x, y)] = 0

                    elif level[x][y] == "H":
                        self.score_map[(x,y)] = 0
                        self.q_table[(x, y)] = [-1] * self.no_of_actions
                        self.rewards[(x, y)] = -1

                    elif level[x][y] == "K":
                        self.score_map[(x,y)] = 0
                        self.q_table[(x, y)] = [-1] * self.no_of_actions
                        self.rewards[(x, y)] = -1

            print("Training Model for Level: {}".format(level_no))
            for episode in range(100):
                self.visited_actions = []
                cur_x, cur_y = self.start_x, self.start_y
                while (cur_x, cur_y) not in self.end_points:
                    cur_x, cur_y = self.train_model(cur_x, cur_y)
            print("Training completed for Level: {}".format(level_no))

        def train_model(self, cur_x, cur_y):
            available_states = []
            actions = [(-1,0), (1,0), (0, -1), (0, 1)]
            gamma = 0.1
            self.visited_actions.append((cur_x, cur_y))
            # print("training", cur_x, cur_y)
            # LEFT = 0, RIGHT = 1, BOTTOM = 2, TOP = 3
            for i in range(len(actions)) :
                next_x, next_y = cur_x + actions[i][0], cur_y + actions[i][1]
                
                self.q_table[(cur_x, cur_y)][i] = self.rewards[(next_x, next_y)] + gamma * max(self.q_table[(next_x, next_y)])
                if (next_x, next_y) not in self.walls and (next_x, next_y) not in self.visited_actions:
                        available_states.append((next_x, next_y))
            
            if len(available_states) == 0:
                return self.end_points[0]
            return random.choice(available_states)

        def play_with_baseline_AI(self):
            next_action_queue = []
            next_action_queue.append((self.start_x, self.start_y))
            is_game_finished = False
            visited_actions = []
            score = 0
            no_of_nodes_traversed = 0
            while is_game_finished == False and len(next_action_queue) > 0:
                cur_x, cur_y = next_action_queue[-1]
                visited_actions.append((cur_x, cur_y))
                next_action_queue.pop()
                score += self.score_map[(cur_x, cur_y)]
                no_of_nodes_traversed += 1
                for (x,y) in [(-1,0), (1,0), (0, -1), (0, 1)]:
                    next_x, next_y = (cur_x + x, cur_y + y)
                    if (next_x, next_y) in self.end_points:
                        is_game_finished = True
                        break
                    if (next_x, next_y) not in self.walls and (next_x, next_y) not in visited_actions:
                        next_action_queue.append((next_x, next_y))

            return {'score': score, 'no_of_nodes_traversed': no_of_nodes_traversed}

        def play_with_treebase_AI(self):
            next_action_queue = []
            next_action_queue.append((self.start_x, self.start_y))
            is_game_finished = False
            visited_actions = []
            score = 0
            no_of_nodes_traversed = 0
            while is_game_finished == False and len(next_action_queue) > 0:
                cur_x, cur_y = next_action_queue[0]
                visited_actions.append((cur_x, cur_y))
                next_action_queue.pop(0)
                score += self.score_map[(cur_x, cur_y)]
                no_of_nodes_traversed += 1
                for (x,y) in [(-1,0), (1,0), (0, -1), (0, 1)]:
                    next_x, next_y = (cur_x + x, cur_y + y)
                    if (next_x, next_y) in self.end_points:
                        is_game_finished = True
                        break
                    if (next_x, next_y) not in self.walls and (next_x, next_y) not in visited_actions:
                        next_action_queue.append((next_x, next_y))

            return {'score': score, 'no_of_nodes_traversed': no_of_nodes_traversed}

        def play_with_nn_tree_AI(self):
            is_game_finished = False
            visited_actions = []
            score = 0
            no_of_nodes_traversed = 0
            cur_x, cur_y = self.start_x, self.start_y
            actions = [(-1,0), (1,0), (0, -1), (0, 1)]
            while is_game_finished == False:
                visited_actions.append((cur_x, cur_y))
                max_reward = max(self.q_table[(cur_x, cur_y)])
                available_states = []
                for i in range(4):
                    next_x, next_y = cur_x + actions[i][0], cur_y + actions[i][1]
                    if max_reward == self.q_table[(cur_x, cur_y)][i] and (next_x, next_y) not in visited_actions and (next_x, next_y) not in self.walls:
                        available_states.append((next_x, next_y))
                
                no_of_nodes_traversed += 1
                
                if len(available_states):
                    cur_x, cur_y = available_states[0]
                    score += self.score_map[(cur_x, cur_y)]
                else:
                    cur_x, cur_y = self.end_points[0]

                if (cur_x, cur_y) in self.end_points:
                    is_game_finished = True
                    
            return {'score': score, 'no_of_nodes_traversed': no_of_nodes_traversed}

    game = MazeVision()
    result = {}
    result['baseline_AI'] = game.play_with_baseline_AI()
    result['treebase_AI'] = game.play_with_treebase_AI()
    result['nn_tree_AI'] = game.play_with_nn_tree_AI()
    return result

