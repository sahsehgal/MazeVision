#Project Implementation by:
# 1. Sahil Sehgal (343933724)
# 2. Sandeepan Sharma Roy(487893821)
# 3. Aditi Mallesh (741614809)
# 4. Anisha Siddapur Math (500681255)

from levels import get_maze
from helper import randomize_maze_board, find_optimal_path
from game import start_game
from q_learning import start_qlearning_game
import matplotlib.pyplot as plt

class Main:
        active_maze = []
        def print_maze(self, m):
                for i in range(len(m)):
                        print(m[i])
        def main(self):
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
                self.active_maze = randomize_maze_board(get_maze(level))
                
                # If Neural Network selected
                if strategy == 4:
                        start_qlearning_game(self.active_maze, strategy)
                else:
                        start_game(self.active_maze, strategy)
                
                # self.active_maze = show_optimal_path(self.active_maze)
                # graph_plot()

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

def show_optimal_path(maze):
    path,cost = find_optimal_path(maze)
    for i in range(0, len(path)):
         x, y = path[i]
         if maze[x][y] not in ['P']:
             list1 = list(maze[x])
             list1[y] = 'G'
             maze[x] = ''.join(list1)
    return maze


def graph_plot(self):
        for i in [self.levels]:
                scores = []
                Iterations = []
                for turn in range(0, 100):
                        active_maze = randomize_maze_board(get_maze(i))
                        path, cost = find_optimal_path(active_maze)
                        scores.append(cost)

                freq = {}
                for item in scores:
                        if (item in freq):
                                freq[item] += 1
                        else:
                                freq[item] = 1

                cost = list(freq.keys())
                frequency = list(freq.values())

                fig = plt.figure(figsize=(10, 5))
                plt.bar(cost, frequency, color='red', width=0.1)
                plt.title('Level ' + str(i), fontsize=14)
                plt.xlabel('Cost', fontsize=14)
                plt.ylabel('Frequency', fontsize=14)
                plt.grid(True)
                plt.savefig('Level ' + str(i) + ' Statistics.png')

        
                        

if __name__ == "__main__":
        maze = Main()
        maze.main()