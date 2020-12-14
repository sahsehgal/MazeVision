#Project Implementation by:
# 1. Sahil Sehgal (343933724)
# 2. Sandeepan Sharma Roy(487893821)
# 3. Aditi Mallesh (741614809)
# 4. Anisha Siddapur Math (500681255)

from levels import get_maze
from helper import randomize_maze_board, get_level_statistics
from game import start_game
from q_learning import start_qlearning_game
import matplotlib.pyplot as plt

def get_level_input():
        print("Enter level number you want to play. ")
        print("1. Basic")
        print("2. Easy")
        print("3. Intermediate")
        print("4. Hard")
        print("5. Master")
        return int(input())

def get_control_strategy():
        print("Enter the control strategy number you want to go ahead.")
        print("1. Human")
        print("2. Baseline AI")
        print("3. Tree-based AI")
        print("4. Tree + NN based AI")
        return int(input())                        

class Main:
        def play_game(self):
                print("Welcome to maze vision 2020.")
                level = get_level_input()
                print("\nYou selected", level)
                if level not in [1,2,3,4,5]:
                        print("You entered wrong value.")
                        return
                strategy = get_control_strategy()
                print("\nYou selected", strategy)
                if strategy not in [1,2,3,4]:
                        print("You entered wrong value.")
                        return
                active_maze = randomize_maze_board(get_maze(level))
                
                # If Neural Network selected
                if strategy == 4:
                        start_qlearning_game(active_maze, strategy)
                else:
                        start_game(active_maze, strategy)

        def get_statistics(self):
                for level in range(1,6):
                        for instance in range(100):
                                active_maze = randomize_maze_board(get_maze(level))
                                print ("Level: {}, Instance: {}".format(level, instance+1))
                                print ("Statistics: {}\n".format(get_level_statistics(active_maze, level)))

if __name__ == "__main__":
        maze = Main()
        # maze.play_game()
        maze.get_statistics()
