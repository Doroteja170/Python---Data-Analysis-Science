import random

from fontTools.misc.cython import returns

print('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors')
answer=int(input('Your answer: '))
computer=random.randint(0,2)

if answer==0:
    print('You choose Rock')
elif answer==1:
    print('You choose Paper')
elif answer==2 :
    print('You choose Scissors')
else:
    print('Wrong input')
    exit()

if computer==0:
    print('Computer choose Rock')
elif computer==1:
    print('Computer choose Paper')
else:
    print('Computer choose Scissors')
#Type 0 for Rock, 1 for Paper or 2 for Scissors'
if answer==computer:
    print('Draw!')
elif (answer==0 and computer==1) or (answer==1 and computer==2) or (answer==2 and computer==0):
    print('You Lose!')
else:
    print('You Win!')
