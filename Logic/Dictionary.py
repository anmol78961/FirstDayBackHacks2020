# Used to make api calls to PyDictionary
# Checks the submitted word, 
#               returns true or false, 
#               displays word and definition
import PyDictionary
from PyDictionary import PyDictionary
import sys, os

# The api force calls the print function when it fails, need to disable
# Disable
def blockPrint():
    sys.stdout = open(os.devnull, 'w')

# Restore
def enablePrint():
    sys.stdout = sys.__stdout__

# calls the PyDictionary api
# returns the result
def SpellCheck(word):
    blockPrint()
    check = PyDictionary.meaning(word)
    enablePrint()
    if check:
        return check
    else:
        return "Incorrect"