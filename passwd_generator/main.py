import string
import random
digit = string.digits
lower = string.ascii_lowercase
upper = string.ascii_uppercase
all_letters = lower + upper
sembol = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) #2
nr_symbols = int(input(f"How many symbols would you like?\n")) #2
nr_numbers = int(input(f"How many numbers would you like?\n")) #2

passwd_list = []
passwd = str(passwd_list)

while nr_letters > 0:

    passwd += random.choice(all_letters)
    nr_letters -= 1
while nr_numbers > 0:
    passwd += random.choice(digit)
    nr_numbers -= 1
while nr_symbols > 0:
    passwd += random.choice(sembol)
    nr_symbols -= 1
random.shuffle(passwd_list)
