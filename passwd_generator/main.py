

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
