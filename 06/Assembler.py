import math
import os 
import random
import re
import sys
import SymbolTable

symbolTable = SymbolTable

for i in range(0, 16): 
   rValue = "R" + str(i)
   symbolTable.table[rValue] = i

   variableCursor = 16    # the next memory location available after the R# values
   root = sys.argv[1]     

