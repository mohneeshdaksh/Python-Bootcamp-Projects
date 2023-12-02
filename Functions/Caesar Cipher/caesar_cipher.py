'''Caesar Cipher'''

from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

def caesar(start_text, shift_amount, cipher_direction):
    '''Main Function for Caesar Cipher. Three inputs are required '''
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for character in start_text:
        if character in alphabet:
            alphabet_index = alphabet.index(character)
            new_index = alphabet_index + shift_amount
            end_text += alphabet[new_index]
        else:
            end_text += character
    print(f"Your {direction}d text is '{end_text}'")


loop_execution = True
while loop_execution:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        loop_execution = False
        print("Goodbye!")
    elif restart == "yes":
        pass
    else:
        print("Invalid entry! Please try again.")
