import numpy as np

class Automaton:
    
    def __init__(self, type:str, L:int, G:int) -> None:
        self._type = type
        self._length = L
        self._gens = G
        self._list = np.zeros(L+2)  # Add two extra indices for left- and rightmost borders (zero values)
                                    # [ X, X, X, X, ... , 0, 0] is used as:
                                    # [ 0, X, X, X, X, ... , 0] where X are the actual cells of interest.
        

    def AssignOccupiedCells(self, indexList:list) -> None:
        __row1 = self._list
        for i in indexList:
            if i <= self._length:
                __row1[i-1] = 1
        self._list = __row1

   
    
    def PerformGenStep(self, currentrow) -> list:
        row = currentrow
        newrow = np.zeros(self._length+2)
        match self._type:
            case 'A':
                # Perform steps for type A
                for i in range(len(row)-2):
                    if(row[i]): 
                        # If cell is currently 1, then:
                        if(row[i-1] != row[i+1]): # XOR gate (exactly one neighbor is 1 -> result is 1)
                            newrow[i] = 1
                    else:
                        # If cell is currently 0, then:
                        if(not (row[i-1] or row[i+1]) == 0): # NOR gate (both neighbors are 0 -> result is 1)
                            newrow[i] = 1
                self._list = newrow
                return newrow
            # case 'B':
            #     # Perform steps for type B

            # case 'U':
            #     # Perform steps for type U

            case _:
                # Perform default case
                return newrow
                print("No new generation processed, Automoton type not set")

    def FullRun(self) -> None:
            for i in range(self._gens):
                print(self.PerformGenStep(self._list))
