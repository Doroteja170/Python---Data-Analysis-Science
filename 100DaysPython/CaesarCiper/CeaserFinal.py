letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text = input('Type your message: ').lower()
shift = int(input('Type the shift number: '))

#What happens if the user enter number/symbol/space?

def ceaser(original_text, shift_amount, direct):
    cyper_text = ''
    if direct == 'decode':
        shift_amount *= -1
    for i in original_text:
        if i not in letters:
            cyper_text+=i
        else:
            position = letters.index(i) + shift_amount
            position %= len(letters)
            cyper_text += letters[position]
    print(f'Here is the {direct}d result: {cyper_text}')


ceaser(text, shift, direction)


#Can you find a way to restart the ciper program?
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))
    ceaser(text, shift, direction)

    again=input("Type 'yes' of you want to go again. Otherwise 'no'")
    if again=='no':
        should_continue=False
        print('Goodbye')
