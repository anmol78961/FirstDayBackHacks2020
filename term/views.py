from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
from .forms import levelone
from PyDictionary import PyDictionary
import sys, os, random


extra_list = []
word_list = ["yelling", "eying", "lying", "glen", "lien"]
word_found = []
definition = []


def check_list(to_find, found):
    count = 0
    to_find_len = len(to_find)

    for x in found:
        if x in to_find:
            to_find.remove(x)
            count += 1

    if count == to_find_len:
        return True
    else:
        return False


def split(word, user_word):
    new_word = word.lower()
    new_user_word = user_word.lower()
    char_len = 0
    user_len = len(new_user_word)
    word_split = list(new_word)
    user_split = list(new_user_word)
    for x in user_split:
        if x in word_split:
            word_split.remove(x)
            char_len += 1

    if char_len == user_len:
        return True
    else:
        return False


def check_word_found(word):
    if word in word_found:
        # print("You have already found this word \n")
        return True
    else:
        return False


def check_extra_word_found(word):
    if word in extra_list:
        return True
    else:
        return False


def spell_check(word):
    char_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', '\\', ' ', "'", '(',
                 ')', '*', '+', ',', '-', '.', '/', ':', ';', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
    new_word = list(word)
    for x in new_word:
        if x in char_list:
            return False
    #block_print()
    check = PyDictionary(word).getMeanings()
    #enable_print()
    if check == {word: None}:
        return False
    else:
        return check


def WordScrambler(word):
    listWord = list(word)
    random.shuffle(listWord)
    result = ''.join(listWord)
    return result


def index(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.info(
            request, "You must be Signed-up or Login to play the game")
    return render(request, "term/index.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/user-registration.html', context)


def levels(request):
    return render(request, "term/level.html")


def level1(request):
    question="igyleln"
    if request.method == 'POST':
        form = levelone(request.POST)

        if form.is_valid():
            while check_list(word_list, word_found) is False:
                user_input = str(form.cleaned_data['Word']).lower()
                limit = len(user_input)

                if limit <= 2:
                    messages.info(request,"Please enter a word with 3 characters or above.")
                    return redirect('level1')

                if user_input == "_scramble":
                    re_scramble = WordScrambler(question)
                    question = re_scramble
                    messages.info(request,"Your question has been re_scrambled")
                    return render(request, "term/level1.html",{'form':form, 'que':question})

                if split(question, user_input) is False:
                    messages.info(request,"Please enter a word with the characters in the scrambled word")
                    return redirect('level1')

                check = spell_check(user_input)
                if check is not False:
                    if user_input in word_list:
                        word_found.append(user_input)
                        definition.append(check)
                        messages.info(request, "Congrats, Word Found!")
                        return redirect('level1')
                    else:
                        if check_word_found(user_input) is True:
                            messages.info(request,"You have already found this word")
                            return redirect('level1')
                        elif check_extra_word_found(user_input) is True:
                            messages.info(request, "You have already found this word")
                            return redirect('level1')

                        extra_list.append(user_input)
                        definition.append(check)
                        messages.info(request, "Congrats, Extra Word Found!")
                        return redirect('level1')
                else:
                    messages.info(request, "Word doesn't exist, try again \n")
                    return redirect('level1')
            else:
                messages.info(request, "You have finished the level")
                return redirect('level1')
    else:
        form = levelone()
    context={'form':form, 'que':question}
    return render(request, "term/level1.html", context)
