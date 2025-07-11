word_list=['basketball','chair','magic']

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word
import random
chosen_word=random.choice(word_list)
print(chosen_word)

# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
guess=input('Guess a letter: ').lower()

# TODO-3 Check if the letter that user guessed is one of the letter in chosen_word. Print Right if it is, else Wrong
for letter in chosen_word: # c h a i r
    if letter==guess:
        print('Right')
    else:
        print('Wrong')
