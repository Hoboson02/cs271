import math
import os 
import random
import re
import sys
import SymbolTable
import code
import parser
code = code
symbolTable = SymbolTable

for i in range(0, 16): 
   rValue = "R" + str(i)
   symbolTable.table[rValue] = i

   variableCursor = 16    # the next memory location available after the R# values
   root = sys.argv[1]     

def integrate(line):
# integrates null, dest, and jump fields, while making them translatable

  line = line[:-1]
  if not "=" in line:
    line = "null=" + line
  if not ";" in line:
    line = line + ";null"
  return line
   
def addVariable(label):
# allocates space for the newly added variables

  global variableCursor
  table[label] = variableCursor
  variableCursor += 1
  return symbolTable.table[label]

def firstPass():
# searches file for jump labels and enters them into the symbol table
# also removes out comments & empty lines

  infile = open(root + ".asm")
  outfile = open(root + ".tmp", "w")

  lineNumber = 0
  for line in infile:
    sline = code.strip(line)
    if sline != "":
      if sline[0] == "(":
        label = sline[1:-1]
        table[label] = lineNumber
        sline = ""
      else:
        lineNumber += 1
        outfile.write(sline + "\n")

  infile.close()
  outfile.close()


def assemble():
# takes file stripped of labels and translates it into .hack

  infile = open(root + ".tmp")
  outfile = open(root + ".hack", "w")

  for line in infile:
    tline = code.translate(line)
    outfile.write(tline + "\n")

  infile.close()
  outfile.close()
  os.remove(root + ".tmp")


# actual program is just calls to these two functions
firstPass()
assemble()