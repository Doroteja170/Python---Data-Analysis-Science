import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to Password Generator!')
print('How many letters would you like in your password?')
letter=int(input())
print('How many symbols would you like in your password?')
symbol=int(input())
print('How many numbers would you like in your password?')
number=int(input())

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# word=''
# for let in range(0,letter):
#     word=word+letters[random.randint(0,len(letters)-1)]
# for sym in range(0,symbol):
#     word=word+symbols[random.randint(0,len(symbols)-1)]
# for num in range(0,number):
#     word=word+numbers[random.randint(0,len(numbers)-1)]


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
word=''
for let in range(0, letter):
    word = word + letters[random.randint(0, len(letters) - 1)]
    #random.choice(letters)
for sym in range(0, symbol):
    word = word + symbols[random.randint(0, len(symbols) - 1)]
for num in range(0, number):
    word = word + numbers[random.randint(0, len(numbers) - 1)]
password_list=list(word)
random.shuffle(password_list)

password=''
for char in password_list:
    password+=char

print(password)