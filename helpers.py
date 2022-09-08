import sys, string, random
from time import process_time
from termcolor import colored
from collections import defaultdict

ALPHA = 26
TURNS = 5


def random_word(words):
    return random.choice(words[random.randint(0, ALPHA)])


def hash(letter, whole=True):
    if whole:
        letter = letter[0]
    return string.ascii_lowercase.index(letter)
    

def load(file):
    array = [[] for i in range(ALPHA)]

    with open(file, "r") as f:
        for words in f.readlines():
            index = hash(words)
            array[index].append(words.strip())
    return array


def print_alpha(valid):
    print()
    for i in valid:
        print(i, end=" ")
    print()  
    print()


def guess(num):
    ask = input("Guess #" + str(num) + ": ").lower().strip()
    if len(ask) == 5 or ask.isalpha():
        return ask
    return guess(num)


# This returns duplicate letters with their index postitions if there is any but have yet to implement it yet
def duplicate_letters(win_word):
    dups = defaultdict(list)

    for index, letter in enumerate(win_word):
        if win_word.count(letter) > 1:
            dups[letter].append(index)

    return dups


def check(guess, word_list):
    if guess in word_list[hash(guess)]:
        return True     
    return False 


def update(color, letter, valid):
    valid[hash(letter, False)] = colored(letter.upper(), color)
    print(colored(letter, color), end="")


def compare(win_word, guess_word, valid_letters):
    duplicates = duplicate_letters(win_word)

    for i in range(len(guess_word)):
        if guess_word[i] == win_word[i]:
            update("green", guess_word[i], valid_letters)
        elif guess_word[i] in win_word:
            update("yellow", guess_word[i], valid_letters)
        else:
            update("grey", guess_word[i], valid_letters)
            
    print()

def play_again():
    prompt = input(colored("Play Again? y/n", "blue"))
    if prompt.lower() in ("yes", "y"):
        return True
    elif prompt.lower() in ("no", "n"):
        print(colored("Thanks for playing!", "blue"))
        sys.exit()
    
    print(colored("Not acceptable input enter yes/y or no/n.", "red"))
    return play_again()


def welcome(win_word):
    # Welcome message
    print()
    print(colored("Welcome to Wordle", "blue"))

    # Warning message for duplicates, havent implemented support for the rest
    if len(duplicate_letters(win_word)) >= 1:
        print(colored("DUPLICATE LETTERS IN THIS WORD", "red"))

