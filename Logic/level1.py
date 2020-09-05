import Dictionary
import Scramble


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


def start():
    question = "igyleln"
    print(f"Unscramble the word \"{question}\"")

    extra_list = []
    word_list = ["yelling", "eying", "lying", "glen", "lien"]
    word_found = []
    definition = []

    print("Enter the word you can form from unscrambling the given word: "
          "and enter \"_scramble_\" to re-scramble the question")

    while check_list(word_list, word_found) is False:
        user_input = str(input())
        limit = len(user_input)

        if limit <= 2:
            print("Enter a word with 3 letters or above \n")
            continue

        if user_input.lower() == "_scramble":
            re_scramble = Scramble.word_scrambler(question)
            print(re_scramble, "\n")
            continue

        if split(question, user_input) is False:
            print("Please enter a word with the characters in the scrambled word \n")
            continue
        check = Dictionary.spell_check(user_input)

        if check is not False:

            if user_input in word_list:

                if user_input in word_found:
                    print("You have already found this word \n")
                    continue

                word_found.append(user_input)
                definition.append(check)
                print("word found \n")

            else:
                if user_input in extra_list:
                    print("extra word already found \n")
                    continue

                extra_list.append(user_input)
                definition.append(check)
                print("extra word \n")

        else:
            print("Word doesn't exist, try again \n")

    else:
        print("The words found are: ")
        for x in word_found:
            print(x)
        print()

        print("The extra word found are: ")
        if len(extra_list) is None:
            print("No extra elements were found \n")
        else:
            for z in extra_list:
                print(z)
            print()

        print("The definition of the words found are: ")
        for y in definition:
            print(y)
        print()


pass
