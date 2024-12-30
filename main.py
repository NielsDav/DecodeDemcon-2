from Automaton import *
from CONSTANTS import *

# Main script:
# Make Automaton object (type [A,B,C], Length (cells), Generations to plot))
x = Automaton(A, 5, 4)

# Assign first row of initial values using list
x.AssignOccupiedCells([1,2])

# Compute next generation of cells
print(x._list)
# print(x.PerformGenStep())
x.FullRun()
