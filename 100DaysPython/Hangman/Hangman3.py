word_list=['basketball','chair','magic']

import random
chosen_word=random.choice(word_list)
print(chosen_word)
print(len(chosen_word)*'_')

# TODO-1 Use the while loop to let the user guess again
game_over=False;
correct=[]
while not game_over :
    guess = input('Guess a letter: ').lower()
    # TODO-2 Change the for loop so that you keep the previous correct letter
    display = ''
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct.append(guess)
        elif letter in correct:
            display+=letter
        else:
            display += '_'
    print(display)

    if '_' not in display:
        game_over=True
        print('You win')


#basketball
#''
#i=0, guess=a
#word[0]==a nije
#new=display[0]=_
#word[1]=a jeste
#new_display=_a