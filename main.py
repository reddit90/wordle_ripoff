from helpers import *

def main():
    words = load("wordle_words.txt")
    win_word = random_word(words) 
    valid = [letter for letter in string.ascii_uppercase]

    welcome(win_word)
    
    i = 1
    while i < TURNS + 1:
        print_alpha(valid)
        ask = guess(i)
        if check(ask, words):
            compare(win_word, ask, valid)
        i += 1

        if ask == win_word:
            print(colored("WINNER", "red"))
            break

    print(colored("The word was ", "blue") + colored(win_word.upper(), "green"))
    
    if play_again():
        main()


if  __name__ == "__main__":
    main()