from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
wanna_continue = True
print(logo)
while wanna_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    def ceaser(start_text, shift_amount, cypher_direction):
        end_text = ""
        if cypher_direction == "decode":
            shift_amount *= -1
        for letter in start_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += letter
        print(end_text)

    ceaser(start_text=text, shift_amount=shift, cypher_direction=direction)
    choice = input("yes or no").lower()
    if choice == "no":
        wanna_continue = False
        print("bye")