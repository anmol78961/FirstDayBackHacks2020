# Grabs and loads the words from dictionary3000.txt to use as the basis for
#   the initial scramble.
import random

def ReadFile(dfile):
    file1 = open(dfile)
    words1 = file1.readlines()
    wordsOutput = []
    for word in words1:
        output = word.strip()
        wordsOutput.append(output)
    return wordsOutput

# difficulty is an int 1 - 3 for easy med hard
def GenerateWordList(difficulty):
    wordList = ReadFile("dictionary3000.txt")
    # easy = (1, 4)
    # medium = (5, 7)
    # hard = (8, -1)
    generatedOutput = []
    if difficulty == 1:
        for word in wordList:
            if len(word) in range(1, 4):
                generatedOutput.append(word)
    elif difficulty == 2:
        for word in wordList:
            if len(word) in range(5, 7):
                generatedOutput.append(word)
    elif difficulty == 3:
        for word in wordList:
            if len(word) in range(8, 20): 
                generatedOutput.append(word)
    # shuffles the list of words so they are not in alphabetical order
    random.shuffle(generatedOutput)
    return generatedOutput