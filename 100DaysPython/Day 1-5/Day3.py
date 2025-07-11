print('Welcome to the Tressure Island.\nYour mission is to fin the treasure')
print('You are at a cross road. Where do you want to go?')
road=input('Type left or right: ')

if road=="left":
    print('You\'ve come to a lake. There is an island in the middle of the lake.')
    lake=input('Type "wait" to wait for a boat. Type "swim" to swim acros: ')
    if lake=='wait':
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        house=input('Red, yellow and blue. Which one do you choose?: ')
        if house=='yellow':
            print('You Win!')
        elif house=='red':
            print('Burned by fire. Game Over!')
        elif house=='blue':
            print('Eeaten by beasts. Game Over!')
        else:
            print('Game Over!')
    else:
        print('Attacked by trout. Game Over!')
else:
    print('Fall into a hole. Game Over!')
