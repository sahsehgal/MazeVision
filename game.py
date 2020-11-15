import turtle
import math

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

# Function to initialize the maze
def setup_maze(level, pen, player):
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

                        elif character =="G":
                                pen.shape("square")
                                pen.color("green")
                                pen.goto(screen_x, screen_y)
                                pen.stamp()
                                score_map[(screen_x, screen_y)] = 1


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

def start_game(board):
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
    
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("MazeVision")
    wn.setup(700,700)
    wn.tracer(0)
    wn.bgpic("./background.gif")

    pen = Pen()
    player = Player()
    setup_maze(board, pen, player)

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