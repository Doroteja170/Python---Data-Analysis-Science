print('Welcome to the Pizza Deliveries!')
size=input('What size do you want? S, M or L:')
pepperoni=input('Do you want pepperoni? Y or N:')
extra_cheese=input('Do you want extra cheese? Y or N:')

#S=15$, M=20$, L=25$, extra_p_S=2$ extra_p_M_L=3$ extra_c=1$

bill=0

if size=='S':
    bill+=15
    if(pepperoni=='Y'):
        bill+=2
elif size=='M':
    bill+=20
    if (pepperoni == 'Y'):
        bill += 3
elif size=='L':
    bill += 25
    if (pepperoni == 'Y'):
        bill += 3
else:
    print('Wrong input')
if extra_cheese=='Y':
    bill+=1

print('Your bill is: $',bill)


