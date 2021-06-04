import random
#from hangman_words import word_list
stages = ['''
  +---+s
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

family_word = ["yunus", "emre", "döndü", "pakize", "salih", "melih", "semih","emine", "said", "fatma", "kadir"]
choiced = random.choice(family_word)
length = len(choiced)
spaces = []
for _ in range(length):
    spaces += "_"
print(spaces)

lives = 6
end_of_game = False
while not end_of_game:
    guess = input("guess a letter:").lower()
    if guess in spaces:
        print(f"you've already guessed {guess}")
    for location in range(length):
        letter = choiced[location]
        if letter == guess:
            spaces[location] = letter

    print(spaces)


    if guess not in choiced:
        lives -= 1
        print(stages[lives])

        if lives == 0:
            end_of_game = True
            print("you lose")

    if "_" not in spaces:
        end_of_game = True
        print("you win")

