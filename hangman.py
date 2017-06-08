import os
import random
from word_list import word_list

GUESSES = 7

good_guesses = []
bad_guesses = []

secret_word = random.choice(word_list).upper()

playing = True


def write_instructions():
    print "GUESSES LEFT: {}".format(GUESSES - len(bad_guesses))
    print "Guess a letter, or solve the puzzle. Enter 'QUIT' to stop the game."


def render_spaces(word):
    spaces = ""
    for letter in word:
        if letter in good_guesses:
            spaces += letter.upper() + " "
        else:
            spaces += "_" + " "
    print spaces


while playing:
    os.system('cls' if os.name == 'nt' else 'clear')
    # print secret_word
    write_instructions()
    render_spaces(secret_word)
    guess = raw_input("> ").upper()

    if guess == "QUIT":
        quit()
    elif len(guess) == 1:
        if guess in secret_word:
            good_guesses.append(guess)
        else:
            bad_guesses.append(guess)
    else:
        if guess == secret_word:
            os.system('cls' if os.name == 'nt' else 'clear')
            print "You win! The secret word was {}".format(secret_word)
            break

    if len(bad_guesses) == GUESSES:
        os.system('cls' if os.name == 'nt' else 'clear')
        render_spaces(secret_word)
        print "No more guesses. The secret word was {}.".format(secret_word)
        break
    else:
        if set(secret_word) == set(good_guesses):
            os.system('cls' if os.name == 'nt' else 'clear')
            print "You win! The secret word was {}".format(secret_word)
            break
