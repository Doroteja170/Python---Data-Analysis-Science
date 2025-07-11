letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction=input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
text=input('Type your message: ').lower()
shift=int(input('Type the shift number: '))

# def decode(original_text,shift_amount):
#     decode_text = ''
#     for i in original_text:
#         position=letters.index(i)-shift_amount #if the first letter is a the shifted will be c if shift=2
#         decode_text+=letters[position]
#     print(f'Here is the decoded result: {decode_text}')
#
# decode(text,shift)

#TODO-4 What happens if you try to shift z forwards by 9?
def decode(original_text,shift_amount):
    decode_text = ''
    for i in original_text:
        position=letters.index(i)-shift_amount
        position %= len(letters)
        decode_text+=letters[position]
    print(f'Here is the encoded result: {decode_text}')

decode(text,shift)



def ceaser(original_text,shift_amount,direct):
    cyper_text = ''
    for i in original_text:
        if direct=='decode':
            shift_amount*=-1
        position = letters.index(i) + shift_amount
        position %= len(letters)
        cyper_text += letters[position]
    print(f'Here is the {direct}d result: {cyper_text}')

ceaser(text,shift,direction)

