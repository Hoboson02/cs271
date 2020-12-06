import SymbolTable
import Assembler

symbolTable = SymbolTable
assembler = Assembler
def aTranslate(line):
# translates a symbolic a-instruction into an int (if necessary)
# then translates that into a binary machine instruction

  if line[1].isalpha():
    label = line[1:-1]
    aValue = symbolTable.table.get(label, -1)
    if aValue == -1:
      aValue = assembler.addVariable(label)
  else:
    aValue = int(line[1:])
  bValue = bin(aValue)[2:].zfill(16)
  return bValue
 

def cTranslate(line):
# splits a c-instruction into its components & translates them

  line = assembler.integrate(line)
  tempValue = line.split("=")
  destCode = symbolTable.dest.get(tempValue[0], "destFAIL")
  tempValue = tempValue[1].split(";")
  compCode = symbolTable.comp.get(tempValue[0], "compFAIL")
  jumpCode = symbolTable.jump.get(tempValue[1], "jumpFAIL")
  return compCode, destCode, jumpCode


def translate(line):
# distinguishes a- and c-instructions and then runs them through the proper function, so they can be translated

  if line[0] == "@":
    return aTranslate(line)
  else:
    codes = cTranslate(line)
    return "111" + codes[0] + codes[1] + codes[2]