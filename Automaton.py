from CONSTANTS import *

class Automaton:
    
    def __init__(self, type:str, L:int, G:int) -> None:
        """
        Initialize an Automaton Instance
        :param type: A, B or U type
        :param L: no. of cells
        :param G: no. of generations to compute
        """

        self._type = type
        self._length = L
        self._gens = G
        self._boollist = [0]*8      # Empty list, 8 indices long
        self._celllist = [0]*(L+2)  # Celllist: no. of cells (L) + two extra indices for left- and rightmost borders (zero values)
                                    # [ X, X, X, X, ... , 0, 0] is used as:
                                    # [ 0, X, X, X, X, ... , 0] where X are the actual cells of interest.
        

    def AssignOccupiedCells(self, indexList:list) -> None:
        """
        Assign first row of occupied cells
        :param indexList: A list containing positions for '1' values on first cell row.
        """
        __row1 = self._celllist
        for i in indexList:
            if i <= self._length: # Check if integer is in length of automaton. Otherwise, ignore.
                __row1[i-1] = 1
        self._celllist = __row1

    def AssignTruthTable(self, boolList:list) -> None:
        """
        Assign Boolean values to rule set (for Universal Automaton only)
        :param boolList: A list containing bool values for b0, b1, ... , b7 (8 values expected)
        """
        if(len(boolList) == len(self._boollist)):
            self._boollist = boolList
            # print(f'boollist set to: {boolList}')
        else:
            raise Exception("Assigned boolean list does not meet requirements for length for truth table")

   
    
    def PerformGenStep(self, currentrow) -> list:
        row = currentrow
        newrow = [0]*(self._length+2)
        
        # Standard procedure (for all types) to compute next generation.
        # Convert current cell situation to binary:
        # Left |  Cell  | Right
        # False - False - False = 000 (binary) = 0 (decimal)
        # False - False - True = 001 (binary) = 1 (decimal)
        # etc.

        for i in range(len(row)-2):
            keybin = str(row[i-1]) + str(row[i]) + str(row[i+1]) # Concatenate string values from left cell, current cell and right cell
            keydec = int(keybin,2)  # Convert from binary value to decimal value for indexing in truth table
            newrow[i] = self._boollist[keydec] # Assign new cell value based on truth table
        self._celllist = newrow
        return newrow

    @staticmethod
    def PrintOutput(cellrow) -> None:
        line = ""
        for i in cellrow:
            if(i):
                # line += '*'
                line += '■'
            else:
                line += ' '
        print(line)


    def FullRun(self) -> None:
        match self._type:
            case 'A':
                # Perform steps for type A
                self.AssignTruthTable(TRUTH_A)
                
            case 'B':
                # Perform steps for type B
                self.AssignTruthTable(TRUTH_B)

            case 'U':
                # Perform steps for type U (Default case)
                pass
                
            case _:
                # Perform default case, where no type is assigned
                raise Exception("No new generation processed, Automoton type not correctly set")  

        # Print 1st generation
        self.PrintOutput(self._celllist)

        # Print subsequent generations until end of set no. of gens
        for i in range(self._gens):
            self.PrintOutput(self.PerformGenStep(self._celllist))
