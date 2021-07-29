fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange', 'ffff']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
uppercased_fruits = [fruit.upper() for fruit in fruits]
print(f"1 - {uppercased_fruits}")
# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(f"2 - {capitalized_fruits}")
# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels.
# Hint: You'll need a way to check if something is a vowel.




fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len(set(fruit.lower()).intersection("aeiou")) >= 2]
print(fruits_with_more_than_two_vowels)



print(set('mango').intersection("aemiou"))




# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
# Exercise 5 - make a list that contains each fruit with more than 5 characters
five_characters = [fruit for fruit in fruits if len(fruit) > 5]
print(f"5 - {five_characters}")
# Exercise 6 - make a list that contains each fruit with exactly 5 characters
five_characters = [fruit for fruit in fruits if len(fruit) == 5]
print(f"6 - {five_characters}")
# Exercise 7 - Make a list that contains fruits that have less than 5 characters
five_characters = [fruit for fruit in fruits if len(fruit) < 5]
print(f"7 - {five_characters}")
# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
five_characters1 = [len(fruit) for fruit in fruits]
print(f"8 - {five_characters1}")
# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
fruits_with_letter_a = [fruit for fruit in fruits if "a" in fruit]
print(f"9 - {fruits_with_letter_a}")
# Exercise 10 - Make a variable named even_numbers that holds only the even numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print(f"10 - {even_numbers}")
# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if not number % 2 == 0]
print(f"11 - {odd_numbers}")
# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numbers = [number for number in numbers if number > 0]
print(f"12 - {positive_numbers}")
# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numbers = [number for number in numbers if number < 0]
print(f"13 - {negative_numbers}")
# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number < 0 and not number % 2 == 0]
print(f"16 - {odd_negative_numbers}")
# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
numbers_plus_5 = [number + 5 for number in numbers]
print(f"17 - {numbers_plus_5}")
# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
fruit = 'Apple'

x = ['Even' if 4 + number % 2 == 0 else 'Odd' for number in range(10)]

y = 'Yes' if fruit == 'Apple' else 'No'


if fruit == "Apple":
    y = "yes"
else:
    y = "no"

if y == 'Yes':
    z = 0
else:
    z = 1






print(x)

# ['Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']