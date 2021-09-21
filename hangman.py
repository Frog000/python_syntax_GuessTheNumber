import random
from hangman_words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # print(string.ascii_uppercase) -> ABCDEFGHIJKLMNOPQRSTUVWXYZ
    used_letters = set() # what the user has guessed
    print(word, used_letters)

    lives = 6

    while len(word_letters) > 0 and lives > 0: 
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list), '\n')

        # getting user input
        user_letter = input('Guess a letter:').upper() # Evaluation of python with uppercase is different from lowercase
        if user_letter in alphabet - used_letters: # print(set(string.ascii_uppercase) - set()) -> All alphabets
            used_letters.add(user_letter)  
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            
            else: 
                lives = lives - 1 # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters: 
            print('You have already used that character. Please try again.')

        else:
            print('Invalid character. Please try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('\nYou died, sorry. The word was', word)
    else:
        print(f'Good! You have guessed the word, {word}')

hangman()