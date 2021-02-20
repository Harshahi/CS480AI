### Harshavardhan Shahi (hs4728), Madison Miller (mjm1361)
### File: EightPuzzle.py
### Solves Problem 2 Eight Puzzle.

#imports
from pq import *
from search import *
from informedSearch import *


ILLEGAL_STATE = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
class EightPuzzle(InformedProblemState):
  """
  Solves 8 puzzles using InformedSearch()
  """
  def __init__(self, positions):
    self.positions = positions

  def __str__(self):
    """
    Required method for use with the Search class.
    Returns a string representation of the state.
    """
    puzzle = ""
    for i in range(len(self.positions)):
      puzzle += str(self.positions[i])
      puzzle += " "
      #new line after every third
      if (i+1)%3 == 0:
        puzzle  += "\n"
    return puzzle

  def illegal(self):
    if self.positions == ILLEGAL_STATE: 
      return 1
    return 0

  def swap(self, list, pos1, pos2):
    """
    Swaps two elements
    """
    list[pos1], list[pos2] = list[pos2], list[pos1]

  def left(self):
    """
    Moves empty tile to the left
    """
    current = self.positions[:]
    empty_index = self.positions.index(0)

    if (empty_index == 0 or empty_index == 3 or empty_index == 6):
      return EightPuzzle(ILLEGAL_STATE)
    else:
      self.swap(current, empty_index, empty_index - 1)
      return EightPuzzle(current)

  def right(self):
    """
    Moves empty tile to the right
    """
    current = self.positions[:]
    empty_index = self.positions.index(0)
    
    if (empty_index == 2 or empty_index == 5 or empty_index == 8):
      return EightPuzzle(ILLEGAL_STATE)
    else:
      self.swap(current, empty_index, empty_index + 1)
      return EightPuzzle(current)

  def up(self):
    """
    Moves empty tile upwards
    """
    current = self.positions[:]
    empty_index = self.positions.index(0)

    if (empty_index == 0 or empty_index == 1 or empty_index == 2):
      return EightPuzzle(ILLEGAL_STATE)
    else:
      self.swap(current, empty_index, empty_index - 3)
      return EightPuzzle(current)


  def down(self):
    """
    Moves empty tile down
    """
    current = self.positions[:]
    empty_index = self.positions.index(0)

    if (empty_index == 6 or empty_index == 7 or empty_index == 8):
      return EightPuzzle(ILLEGAL_STATE)
    else:
      self.swap(current, empty_index, empty_index + 3)
      return EightPuzzle(current)


  def applyOperators(self):
    return[self.left(), self.right(), self.up(), self.down()]
  def operatorNames(self):
    return["left", "right","up", "down"]
  def equals(self, state):
    return (self.positions == state.positions)

  def getrowcol(self, item, goal):
    for index, value in enumerate(goal.positions):
      if (item == value):
        row,col = int(index / 3), index % 3
    return row,col


  def manhattan(self,goal,cost):
    initial_config = self.positions[:]
    goal_config = goal.positions[:]
    for i,item in enumerate(initial_config):
      prev_row,prev_col = int(i/ 3) , i % 3
      goal_row,goal_col = self.getrowcol(item, goal)
      cost += abs(prev_row-goal_row) + abs(prev_col - goal_col)
    return cost

  def misplacedTiles(self,goal,cost):
    for i in range(len(self.positions)):
      if self.positions[i] != goal.positions[i]:
        cost += 1
    return cost

  def heuristic(self, goal):
    cost = 0
    #BFS cost = 0 
    #return cost
    #Misplaced Tiles
    #return self.misplacedTiles(goal,cost)
    #Manhattan Distance
    #return self.manhattan(goal,cost)
      

InformedSearch(EightPuzzle([1, 3, 0, 8, 2, 4, 7, 6, 5]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #A
InformedSearch(EightPuzzle([1, 3, 4, 8, 6, 2, 0, 7, 5]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #B
InformedSearch(EightPuzzle([0, 1, 3, 4, 2, 5, 8, 7, 6]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #C
InformedSearch(EightPuzzle([7, 1, 2, 8, 0, 3, 6, 5, 4]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #D
InformedSearch(EightPuzzle([8, 1, 2, 7, 0, 4, 6, 5, 3]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #E
InformedSearch(EightPuzzle([2, 6, 3, 4, 0, 5, 1, 8, 7]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #F
InformedSearch(EightPuzzle([7, 3, 4, 6, 1, 5, 8, 0, 2]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #G
InformedSearch(EightPuzzle([7, 4, 5, 6, 0, 3, 8, 1, 2]), EightPuzzle([1, 2, 3, 8, 0, 4, 7, 6, 5]))  #H

"""
             Node Expansions
Problem     BFS       A*(tiles) A*(dist) 
A           6         3         3
B           66        8         7
C           179       18        9
D           550       48        26
E           699       44        29
F           1572      110       22
G           6922      375       51
H           53433     3290      176

Why is there a dip in the number of nodes expanded for
E tiles and F Manhattan dist? Is it due to us using a PQ
for those methods?         