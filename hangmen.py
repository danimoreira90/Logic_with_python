#Step 1 

word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
import random
stages = ['''
  +---+
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

chosen_word = random.choice(word_list)
print(chosen_word)
lives = 6
display = []
word_length = len(chosen_word)
for _ in range(word_length):
  display += '_'
#print(display)
end_of_game = False

while not end_of_game:
  guess = str(input('Guess a letter: ')).lower()
  for position in range(0, word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    lives -= 1
    if lives == 0:
      end_of_game = True
      print('You lose.')
  
  print(f"{' '.join(display)}")

  if '_' not in display:
    end_of_game = True
    print('You win!')

  print(stages[lives])
  