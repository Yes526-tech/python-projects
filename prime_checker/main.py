number = int(input("check a number if its a prime:"))

is_prime = True
if number == 2:
    print("prime")
if number == 1:
    print("not prime")
for num in range(2, number):
    if number % num == 0:
        is_prime = False
if is_prime:
    print("prime")

else:
    print("not prime")



