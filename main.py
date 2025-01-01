from Automaton import *
from CONSTANTS import *

# Main script:

# 0. Wait for user input:
print("Linear Cellular Automata")
input("Press Enter to begin...\n")

# 1. Ask input for Automaton type, length, generations:
input_string = input("State automaton type, cells, generations (eg: A 11 10)\n")
[type, length, gens] = input_string.split()
# Make Automaton object (type [A,B,C], Length (cells), Generations to plot))
x = Automaton(type, int(length), int(gens))

# 2. Process user input for starting occupied cells
input_string = input("State occupied input cells. (eg: init_start 3 5 11 init_end)\n")
words = input_string.split()
init_pos:list = []
for i in words:
    try:
        pos = int(i)
        init_pos.append(int(i))
    except:
        pass
# Assign first row of initial values using list
x.AssignOccupiedCells(init_pos)

# 3. Ask for truth table in case of universal automaton
if type == U:
    input_string = input("State Truth table for Universal type automaton. list of 8 indices. (eg: 0 1 0 0 0 1 1 0)\n")
    words = input_string.split()
    boollist:list = []
    for i in words:
        try:
            b = int(i)
            boollist.append(int(i))
        except:
            pass
    x.AssignTruthTable(boollist)

# Compute full run
print('\n') # Start with empty line to seperate from earlier given commands
x.FullRun()

# Rule 30:  0 1 1 1 1 0 0 0 
# Rule 126: 0 1 1 1 1 1 1 0
# Rule 150: 0 1 1 0 1 0 0 1