from Automaton import *
from CONSTANTS import *

# Main script:
# Make Automaton object (type [A,B,C], Length (cells), Generations to plot))
x = Automaton(B, 150, 60)

# Assign first row of initial values using list
x.AssignOccupiedCells([14,90])

x.AssignTruthTable([1,0,1,0,1,0,1,1]) # Only for Universal Automaton
x.AssignTruthTable(TRUTH_A)

# Compute full run
x.FullRun()
