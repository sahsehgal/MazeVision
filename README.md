

# Maze Vision
MazeVision is a single player game to find the fastest/cheapest path from start to end in a maze grid with walls. The walls will be built such that there are multiple paths leading to the target, but there is only one true path that exists with minimum cost. At the beginning of each maze, 4 positions are selected randomly to be "portals".  The agent can move from any portal to any portal in a single action costing 0. This will reduce the overall cost of the particular path, thereby making it the optimal path to the end. 

## Requirements
1. Python 3+<br>
2. turtle: <a href="https://pypi.org/project/PythonTurtle/">https://pypi.org/project/PythonTurtle/</a>

## Installation using python3 and pip3
python3 -m pip3 install --user PythonTurtle

## How to Run:
1. Go to the MazeVision repository.
2. Run python3 maze.py

## RULES:
<ul>
<li>The maze is built using an array with a given size. The start point is where the player is positioned. There are multiple points where the player can exit the maze boundary - called the target. There exists only one end point - which has been reached by the minimum cost path. This decides whether the player won or lost.</li>
<li>The game contains 6 features - Start, End, Targets, Portals and Position Costs
From the Start node, the agent has to continue through the maze in the general direction of the End node that the player decides is the optimal path.</li>
<li>There are 4 portals in the maze and agent can move from one portal to another portal in a single action costing 0. The player can then move towards the closest path in the direction of the End point.</li>
<li>For all other positions, a random cost between 1 and 4 is assigned, when an agent moves through that position, it incurs that cost.</li>
<li>The cost of a path from start to end is the sum of all position costs along the path. And the player has won the game if his chosen path has the lowest cost incurred.
If the agent reaches any Target node which is not the End, he/she loses.
</li>
</ul>