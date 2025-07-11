letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#direction=input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text=input('Type your message: ').lower()
shift=int(input('Type the shift number: '))

#TODO-1 Create a function called encrypt() that takes original_test and shift_amount as 2 inputs
#TODO-2 Inside the encrypt function, shift each letter of the original text forwards in the alphabet by the shift amount and print the text
# def encrypt(original_text,shift_amount):
#     cyper_text = ''
#     for i in original_text:
#         position=letters.index(i)+shift_amount #if the first letter is a the shifted will be c if shift=2
#         cyper_text+=letters[position]
#     print(f'Here is the encoded result: {cyper_text}')
#
# #TODO-3 Call the encrypt() function and pass the arguments
# encrypt(text,shift)

#TODO-4 What happens if you try to shift z forwards by 9?
def encrypt(original_text,shift_amount):
    cyper_text = ''
    for i in original_text:
        position=letters.index(i)+shift_amount
        position%=len(letters)
        cyper_text+=letters[position]
    print(f'Here is the encoded result: {cyper_text}')

encrypt(text,shift)