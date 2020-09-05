# tests to make sure logic 

# Testing Words.py:
from Words import ReadFile, GenerateWordList
from Scramble import WordScrambler
from Dictionary import SpellCheck
import PyDictionary
# GenerateWordList and ReadFile test
# Easy Test
# result = GenerateWordList(1)
# for word in result:
#     print(word)
# Medium Test
# result = GenerateWordList(2)
# for word in result:
#     print(word)
# Hard Test
result = GenerateWordList(3)
# for word in result:
#     print(word)
#     # word scrambler test
#     print(WordScrambler(word))

# # spell check test
# print(SpellCheck(result[1]))
print(WordScrambler(result[1]))
print(SpellCheck(WordScrambler(result[1])))
# SpellCheck(WordScrambler(result[1]))