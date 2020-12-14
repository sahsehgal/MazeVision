import turtle
import math
import random

# Hash map storing cost values associated with cell (x,y) : 1
score_map = {}

# Update score value and show on screen
def UpdateScore(obj,score):
    obj.clear()
    obj.goto(-250,300)
    obj.color("red")
    obj.write("Current score: {}".format(score),align="left", font=(11))
    obj.color("chocolate")

# Portal Class initializing the portal cells
class Portal(turtle.Turtle):
        def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                v=self.getscreen()
                self.color("red")
                self.penup()
                self.speed(0)
                self.goto(x,y)

portalsH = []
portalsK = []

q_table = {}
no_of_actions = 4
LEFT, RIGHT, BOTTOM, TOP = (0,1,2,3)
rewards = {}
max_episodes = 1000
epsilon = 0.25
alpha = 0.01
gamma = 0.9

offset_pixel = 24

# Function to initialize the maze
def setup_maze(level, pen, player):
        for y in range(len(level)):
                for x in range(len(level[y])):
                        character = level[y][x]
                        screen_x = -288 + (x * offset_pixel)
                        screen_y = 288 - (y * offset_pixel)

                        if character =="X":
                                pen.shape("square")
                                pen.color("white")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                walls.append((screen_x, screen_y))
                                q_table[(screen_x, screen_y)] = [-3] * no_of_actions
                                rewards[(screen_x, screen_y)] = -3
                        
                        elif character =="1":
                                pen.shape("classic")
                                pen.color("purple")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 1
                                q_table[(screen_x, screen_y)] = [-1] * no_of_actions
                                rewards[(screen_x, screen_y)] = -1
                        
                        elif character =="2":
                                pen.shape("classic")
                                pen.color("turquoise")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 2
                                q_table[(screen_x, screen_y)] = [-2] * no_of_actions
                                rewards[(screen_x, screen_y)] = -2
                        
                        elif character=="P":
                                score_map[(screen_x, screen_y)] = 0
                                player.goto(screen_x, screen_y)
                                q_table[(screen_x, screen_y)] = [-1] * no_of_actions
                                rewards[(screen_x, screen_y)] = -1
                        
                        elif character =="E":
                                pen.shape("circle")
                                pen.color("green")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 0
                                end_points.append((screen_x, screen_y))
                                q_table[(screen_x, screen_y)] = [0] * no_of_actions
                                rewards[(screen_x, screen_y)] = 0
                        
                        elif character =="H": 
                                pen.shape("square")
                                pen.color("yellow") 
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 0                        
                                portalsH.append(Portal(screen_x,screen_y))
                                q_table[(screen_x, screen_y)] = [-1] * no_of_actions
                                rewards[(screen_x, screen_y)] = -1
                        
                        elif character =="K":
                                pen.shape("square")
                                pen.color("yellow")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 0
                                portalsK.append(Portal(screen_x,screen_y))
                                q_table[(screen_x, screen_y)] = [-1] * no_of_actions
                                rewards[(screen_x, screen_y)] = -1

                        elif character =="G":
                                pen.shape("square")
                                pen.color("green")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 1
                                q_table[(screen_x, screen_y)] = [-1] * no_of_actions
                                rewards[(screen_x, screen_y)] = -1


# Function to end the game
def EndGame():
        turtle.onscreenclick(None)
        turtle.speed(0)
        turtle.penup()
        turtle.goto(0,300)
        turtle.color("green")
        turtle.write("Game finished",align="left", font=(11))
        turtle.goto(2000,2000)

walls = []
end_points = []
optimal_paths = []
next_action_queue = []
visited_actions = []

def start_qlearning_game(board, strategy):
    # Pen class storing information about the cursor drawing on the screen
    class  Pen(turtle.Turtle):
        def  __init__(self):
            turtle.Turtle.__init__(self)
            v=self.getscreen()
            self.color("white")
            self.penup()
            self.speed(3)

    # Player class storing information about score and 
    # has methods handling user key strokes
    class Player(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            v=self.getscreen()
            self.shape("turtle")
            self.color("chocolate")
            self.penup()
            self.speed(0)
            self.score = 0
            self.is_game_finished = False

        # Handle enter key stroke
        def go_return(self):
            if self.is_game_finished == True:
                return
            x = player.xcor()
            y = player.ycor()
            visited_actions.append((x,y))
            max_reward = max(q_table[(x,y)])

            # Left Cell 
            next_x, next_y = (x - offset_pixel, y)
            if max_reward == q_table[(x,y)][LEFT] and (next_x, next_y) not in visited_actions and (next_x, next_y) not in walls:
                next_action_queue.append((next_x, next_y)) 
            
            # Right Cell 
            next_x, next_y = (x + offset_pixel, y)
            if max_reward == q_table[(x,y)][RIGHT] and (next_x, next_y) not in visited_actions and (next_x, next_y) not in walls:
                next_action_queue.append((next_x, next_y)) 
            
            # Bottom Cell 
            next_x, next_y = (x, y - offset_pixel)
            if max_reward == q_table[(x,y)][BOTTOM] and (next_x, next_y) not in visited_actions and (next_x, next_y) not in walls:
                next_action_queue.append((next_x, next_y)) 
            
            # Top Cell 
            next_x, next_y = (x, y + offset_pixel)
            if max_reward == q_table[(x,y)][TOP] and (next_x, next_y) not in visited_actions and (next_x, next_y) not in walls:
                next_action_queue.append((next_x, next_y)) 

            if len(next_action_queue) > 0:
                next_x, next_y = next_action_queue[-1]
                next_action_queue.pop()
                self.score += score_map[(next_x, next_y)]
                UpdateScore(self, self.score)
                self.goto(next_x, next_y)
                if (next_x, next_y) in end_points:
                        self.is_game_finished = True
                        EndGame()

        # Check the collision with portal.
        def is_collision(self, other):
            a = self.xcor()-other.xcor()
            b = self.ycor()-other.ycor()
            distance = math.sqrt((a**2)+(b**2))

            if distance < 5:
                    return True
            else:
                    return False

        def train_model(self, current_state):
                available_states = []
                # Left action reward
                x, y = (current_state[0] - offset_pixel, current_state[1])
                q_table[current_state][LEFT] = rewards[(x,y)] + gamma * max(q_table[(x,y)])
                if (x,y) not in walls:
                        available_states.append((x,y))

                # Right action reward
                x, y = (current_state[0] + offset_pixel, current_state[1])
                q_table[current_state][RIGHT] = rewards[(x,y)] + gamma * max(q_table[(x,y)])
                if (x,y) not in walls:
                        available_states.append((x,y))

                # Bottom action reward
                x, y = (current_state[0], current_state[1] - offset_pixel)
                q_table[current_state][BOTTOM] = rewards[(x,y)] + gamma * max(q_table[(x,y)])
                if (x,y) not in walls:
                        available_states.append((x,y))

                # Top action reward
                x, y = (current_state[0], current_state[1] + offset_pixel)
                q_table[current_state][TOP] = rewards[(x,y)] + gamma * max(q_table[(x,y)])
                if (x,y) not in walls:
                        available_states.append((x,y))

                return random.choice(available_states)

    
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("MazeVision")
    wn.setup(700,700)
    wn.tracer(0)
    wn.bgpic("./background.gif")

    pen = Pen()
    player = Player()
    player.speed(0)
    setup_maze(board, pen, player)

    turtle.listen()
    turtle.onkey(player.go_return,"Return")
    visited_actions.append((player.xcor(), player.ycor()))

    wn.tracer(0)

    # Training Model and updating q_table
    cur_state = (player.xcor(), player.ycor())
    for i in range(max_episodes):
        cur_state = (player.xcor(), player.ycor())
        num_of_nodes = 0
        while cur_state not in end_points:
                cur_state = player.train_model(cur_state)
                num_of_nodes += 1
        print ("Episode: {}".format(i+1))
        print ("No. of nodes traversed: {}".format(num_of_nodes))

    while True:
        for portal,next_portal in zip(portalsH,portalsH[1:]):
                if player.is_collision(portal):
                    player.goto(next_portal.pos())

        for portal,next_portal in zip(portalsK,portalsK[1:]):
                if player.is_collision(portal):
                    player.goto(next_portal.pos())
        wn.update()