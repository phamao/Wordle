from five_letter_words import get_words
import random
import string
from colorama import Fore

# Runs a game of Wordle
def run_wordle(word_list):

    # Resets text to default color
    print(Fore.RESET)

    # Chooses a random word from the word_list
    word = word_list[random.randint(0, 487)]
    word = word.lower()

    print(word) #debug

    # Contains unused letters
    unused_letters = list(string.ascii_lowercase)

    # Contains wrong letters
    wrong_letters = []

    # Contains out of order letters
    wrong_order = []

    # Contains letters in order
    in_order = ['', '', '', '', '']

    # Win state
    win = False

    # Prompts 6 guesses
    for i in range(6):
        while True:

            # Asks for a 5 letter word
            guess = input(Fore.RESET + '\nEnter a 5-letter word:\n> ').lower()

            # Checks is the guess is 5 letters and contains only alphabetic letters
            if len(guess) != 5 or not guess.isalpha():
                print(Fore.RESET + 'That is not a 5-letter word. Try again.')
            
            # If it is, exit the while and continue with the for
            else:
                break
        
        # Checks the guess against the word
        for letter in guess:
            
            # If the the letter is in the word and at the same index, print it green and add it to in_order
            if letter in word and guess.index(letter) == word.index(letter):
                in_order[guess.index(letter)] = letter
                print(Fore.GREEN + letter, end='')

                # If the ordered letter is found in wrong_order, remove it
                if letter in wrong_order:
                    wrong_order.remove(letter)

            # If the letter is in the word but NOT at the same index, print it yellow and add it to wrong_order
            elif letter in word and guess.index(letter) != word.index(letter):
                wrong_order.append(letter)
                print(Fore.YELLOW + letter, end='')

            # If the letter is not in the word, print it white and add it to wrong_letters
            elif letter not in word:
                wrong_letters.append(letter)
                print(Fore.RESET + letter, end='')

            # Removes the letter from unused_letters
            try:
                unused_letters.remove(letter)
            except:
                continue

        # print(in_order) #debug

        # If in_order has no more blank slots, the player has won
        if '' not in in_order:
            print(Fore.RESET + '\nYOU WON!\n')
            win = True
            break

        
        print(Fore.RESET + '\nUnused Letters: {unused}'.format(unused=unused_letters))
        print(Fore.RESET + 'Out of Order Letters: {unordered}'.format(unordered=list(set(wrong_order))))
        print(Fore.RESET + 'Correct Letters: {correct}\n'.format(correct=in_order))

    # If the player ran out of guesses and failed to guess, they lost
    if not win:
        print(Fore.RESET + '\nYou lost :(\n')

    # Resets text to default color
    print(Fore.RESET)


run_wordle(get_words())