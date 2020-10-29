#Project Implementation by: 
# 1. Sahil Sehgal (343933724)
# 2. Sandeepan Sharma Roy(487893821)
# 3. Aditi Mallesh (741614809)
# 4. Anisha Siddapur Math (500681255)

import turtle
import math

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("MazeVision")
wn.setup(700,700)
wn.tracer(0)
wn.bgpic("./background.gif")

# Hash map storing cost values associated with cell (x,y) : 1
score_map = {}

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

        # Handle up key stroke
        def go_up(self):
                if self.is_game_finished == True:
                    return

                move_to_x = player.xcor()
                move_to_y = player.ycor() + 24

                if (move_to_x, move_to_y) in end_points:
                        self.is_game_finished = True
                        EndGame()
                        self.goto(move_to_x, move_to_y)
                        return

                if (move_to_x, move_to_y) not in walls:
                        self.score += score_map[(move_to_x, move_to_y)]
                        UpdateScore(self, self.score)
                        self.goto(move_to_x, move_to_y)
                        return

        # Handle down key stroke
        def go_down(self):
                if self.is_game_finished == True:
                        return

                move_to_x = player.xcor()
                move_to_y = player.ycor() - 24

                if (move_to_x, move_to_y) in end_points:
                        self.is_game_finished = True
                        EndGame()
                        self.goto(move_to_x, move_to_y)
                        return

                if (move_to_x, move_to_y) not in walls:
                        self.score += score_map[(move_to_x, move_to_y)]
                        UpdateScore(self, self.score)
                        self.goto(move_to_x, move_to_y)
                        return

        # Handle left key stroke
        def go_left(self):
                if self.is_game_finished == True:
                    return

                move_to_x = player.xcor() - 24
                move_to_y = player.ycor()

                if (move_to_x, move_to_y) in end_points:
                        self.is_game_finished = True
                        EndGame()
                        self.goto(move_to_x, move_to_y)
                        return

                if (move_to_x, move_to_y) not in walls:
                        self.score += score_map[(move_to_x, move_to_y)]
                        UpdateScore(self, self.score)
                        self.goto(move_to_x, move_to_y)
                        return

        # Handle right key stroke
        def go_right(self):
                if self.is_game_finished == True:
                    return

                move_to_x = player.xcor() + 24
                move_to_y = player.ycor()

                if (move_to_x, move_to_y) in end_points:
                        self.is_game_finished = True
                        EndGame()
                        self.goto(move_to_x, move_to_y)
                        return

                if (move_to_x, move_to_y) not in walls:
                        self.score += score_map[(move_to_x, move_to_y)]
                        UpdateScore(self, self.score)
                        self.goto(move_to_x, move_to_y)
                        return

        # Check the collision with portal.
        def is_collision(self, other):
                a = self.xcor()-other.xcor()
                b = self.ycor()-other.ycor()
                distance = math.sqrt((a**2)+(b**2))

                if distance < 5:
                        return True
                else:
                        return False

# Update score value and show on screen
def UpdateScore(obj, score):
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

level = [""]

### Maze Board 
# X: Wall
# P: Start Player
# H: Portal 1
# K: Portal 2
# E: Target
# 1: Cell with cost value 1
# 2: Cell with cost value 2

# Update the board to try different paths
###
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"P1XXXXXXXH2111121211XXXXX",
"X12XXXXXXX22XXXXXX11XXXXX",
"X12122211112XXXXXX22XXXXX",
"X1K11111XX12XXX2XXX1211XX",
"XX1XXXXXXX11XXX2222XX11XX",
"XX1XXX11XX11XXXXXX1222XXX",
"XX122122XX1222XXXX11XXXXX",
"XXXXXX12XX1111XXXXX1H111E",
"XX122211XXXXXXXXXXXXXXXXX",
"X21XXXXXXXXXXXXXXXXXXXXXX",
"X1111111111111122XXXXXXXX",
"XXXXXXXXXXXX222XXXX11112X",
"XXXXXXXXXXXXXX122XXXXX11X",
"XXX21XXXXXXXXXX111111222X",
"XXX111111111111111111111X",
"XXX121222211XXXXXXXXXXXXX",
"XXXXXXXXXX11XXXXXXXXXXXXX",
"XXXXXXXXXX2222111111111XX",
"XX111XXXXX11111122211111X",
"XX122XXXXXXXXXXXXX11XXXXX",
"XX12221XXXXXXXXXXX12XXXXX",
"XX111XXXX111XXXXX11111XXX",
"XXXX1XXXXXX111XXXK111111E",
"XXXXXXXXXXXXXEXXXXXXXXXXX"
]

portalsH = []
portalsK = []
level.append(level_1)

# Function to initialize the maze
def setup_maze(level):
        for y in range(len(level)):
                for x in range(len(level[y])):
                        character = level[y][x]
                        screen_x = -288 + (x *24)
                        screen_y = 288 - (y * 24)

                        if character =="X":
                                pen.shape("square")
                                pen.color("white")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                walls.append((screen_x, screen_y))
                        
                        elif character =="1":
                                pen.shape("classic")
                                pen.color("purple")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 1
                        
                        elif character =="2":
                                pen.shape("classic")
                                pen.color("turquoise")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 2
                        
                        elif character=="P":
                                score_map[(screen_x, screen_y)] = 0
                                player.goto(screen_x, screen_y)
                        
                        elif character =="E":
                                pen.shape("circle")
                                pen.color("green")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                end_points.append((screen_x, screen_y))
                        
                        elif character =="H": 
                                pen.shape("square")
                                pen.color("yellow") 
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 0                        
                                portalsH.append(Portal(screen_x,screen_y))
                        
                        elif character =="K":
                                pen.shape("square")
                                pen.color("yellow")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 0
                                portalsK.append(Portal(screen_x,screen_y))

# Function to end the game
def EndGame():
        turtle.onscreenclick(None)
        turtle.speed(0)
        turtle.penup()
        turtle.goto(0,300)
        turtle.color("green")
        turtle.write("Game finished",align="left", font=(11))
        turtle.goto(2000,2000)

pen= Pen()
player = Player()

walls = []
end_points = []

setup_maze(level[1])

turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

wn.tracer(0)

while True:
    for portal,next_portal in zip(portalsH,portalsH[1:]):
            if player.is_collision(portal):
                player.goto(next_portal.pos())

    for portal,next_portal in zip(portalsK,portalsK[1:]):
            if player.is_collision(portal):
                player.goto(next_portal.pos())
    wn.update()

                
