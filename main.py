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
import pandas as pd
import numpy as np

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

def plot_graph(data, key, title, file_name):
        # data = [data['baseline_AI'], data['treebase_AI'], data['nn_tree_AI']]
        labels = ["{}".format(i+1) for i in range(len(data['baseline_AI']))]
        X = data['baseline_AI']
        Y = data['treebase_AI']
        Z = data['nn_tree_AI']

        df = pd.DataFrame(np.c_[X,Y,Z], index=labels)
        df.plot.bar()
        y_pos = range(len(labels))
        plt.xticks(y_pos, labels, rotation=0)
        plt.title(title, fontsize=14)
        plt.xlabel('Game Instances', fontsize=14)
        plt.ylabel(key, fontsize=14)
        plt.savefig(file_name)
        # plt.show()
        

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
                print("Enter number of instances per level.")
                no_of_instances = int(input())
                for level in range(1,6):
                        scores, neurons = {}, {}
                        scores['baseline_AI'] = []
                        scores['treebase_AI'] = []
                        scores['nn_tree_AI'] = []
                        
                        neurons['baseline_AI'] = []
                        neurons['treebase_AI'] = []
                        neurons['nn_tree_AI'] = []
                        for instance in range(no_of_instances):
                                active_maze = randomize_maze_board(get_maze(level))
                                print ("Level: {}, Instance: {}".format(level, instance+1))
                                statistics = get_level_statistics(active_maze, level)
                                print ("Statistics: {}\n".format(statistics))
                                
                                scores['baseline_AI'].append(statistics['baseline_AI']['score'])
                                scores['treebase_AI'].append(statistics['treebase_AI']['score'])
                                scores['nn_tree_AI'].append(statistics['nn_tree_AI']['score'])

                                neurons['baseline_AI'].append(statistics['baseline_AI']['no_of_nodes_traversed'])
                                neurons['treebase_AI'].append(statistics['treebase_AI']['no_of_nodes_traversed'])
                                neurons['nn_tree_AI'].append(statistics['nn_tree_AI']['no_of_nodes_traversed'])
                        
                        plot_graph(scores, 'Scores', 'Scores of Level {}'.format(level), 'Level_{}_scores.png'.format(level))
                        plot_graph(neurons, 'Neurons', 'No. of nodes/neurons traversed in Level {}'.format(level), 'Level_{}_neurons.png'.format(level))


if __name__ == "__main__":
        maze = Main()
        # maze.play_game()
        maze.get_statistics()
