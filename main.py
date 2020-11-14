#Project Implementation by: 
# 1. Sahil Sehgal (343933724)
# 2. Sandeepan Sharma Roy(487893821)
# 3. Aditi Mallesh (741614809)
# 4. Anisha Siddapur Math (500681255)

from levels import get_maze
from helper import randomize_maze_board
from game import start_game

class Main:
        active_maze = []
        def print_maze(self, m):
                for i in range(len(m)):
                        print(m[i])
        def main(self):
                print("Welcome to maze vision 2020.")
                print("Enter level number you want to play. ")
                print("1. Basic")
                print("2. Easy")
                print("3. Intermediate")
                print("4. Hard")
                print("5. Master")
                level = int(input())
                print("\nYou selected", level)
                if level not in [1,2,3,4]:
                        print("You selected wrong value.")
                        return
                self.active_maze = randomize_maze_board(get_maze(level))
                self.print_maze(self.active_maze)
                start_game(self.active_maze)

if __name__ == "__main__":
        maze = Main()
        maze.main()                
