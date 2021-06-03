import string
import random
digit = string.digits
lower = string.ascii_lowercase
upper = string.ascii_uppercase
all_letters = lower + upper
sembol = string.punctuation

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
passwd_list = []
for char in range(1, nr_numbers +1):
    passwd_list += random.choice(digit)
for char in range(1, nr_symbols +1):
    passwd_list += random.choice(sembol)
for char in range(1, nr_letters +1):
    passwd_list += random.choice(all_letters)
print(passwd_list)

passwd = ""
for item in passwd_list:
    passwd += item
print(passwd)