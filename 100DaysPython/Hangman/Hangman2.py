word_list=['basketball','chair','magic']

import random
chosen_word=random.choice(word_list)
print(chosen_word)

# TODO-1 Create a placeholder with the same number of blanks as the chosen word
print(len(chosen_word)*'_')
guess=input('Guess a letter: ').lower()

# TODO-2 Create a display that puts the guess letter in the right position
display=''
for letter in chosen_word: # c h a i r
    if letter==guess:
        display+=letter
    else:
        display+='_'
print(display)