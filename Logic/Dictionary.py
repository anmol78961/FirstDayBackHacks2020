# changes to make in core.py in PyDictionary
#     @staticmethod
#     def meaning(term, disable_errors=False):
#         if len(term.split()) > 1:
#             print("Error: A Term must be only a single word")
#         else:
#             try:
#                 html = _get_soup_object("http://wordnetweb.princeton.edu/perl/webwn?s={0}".format(
#                     term))
#                 types = html.findAll("h3")
#                 length = len(types)
#                 lists = html.findAll("ul")
#                 out = {}
#                 for a in types:
#                     reg = str(lists[types.index(a)])
#                     meanings = []
#                     for x in re.findall(r'\((.*?)\)', reg):
#                         if 'often followed by' in x:
#                             pass
#                         elif len(x) > 5 or ' ' in str(x):
#                             meanings.append(x)
#                     name = a.text
#                     out[name] = meanings
#                 return out
#             except Exception as e:
#                 if disable_errors == False:
#                     print("Error: The Following Error occured: %s" % e) ==> change this to ==> return False



# Used to make api calls to PyDictionary
# Checks the submitted word,
#               returns true or false,
#               displays word and definition
import PyDictionary
from PyDictionary import PyDictionary
import sys, os


# def go_(word):
#     if PyDictionary(word).getMeanings() == {word: False}:
#         print("word doesn't exist")
#     else:
#         print(PyDictionary(word).getMeanings())


# The api force calls the print function when it fails, need to disable
# Disable
def block_print():
    sys.stdout = open(os.devnull, 'w')


# Restore
def enable_print():
    sys.stdout = sys.__stdout__


# calls the PyDictionary api
# returns the result
def spell_check(word):
    block_print()
    check = PyDictionary.meaning(word)
    enable_print()
    if check == {word: False}:
        print("Word doesn't exist")
    else:
        print(check)


pass
