from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")


def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == 'easy':
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS



def number_guessing_game():
  #Choosing a number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  #Make a function to set difficulty.
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    #Let the user guess a number.
    guess = int(input("Make a guess: "))
    
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      print(f"The answer was {answer}")
      return
    elif guess != answer:
      print("Guess again.")
      
  
number_guessing_game()  
  #Function to check the user's guess against the actual number.
  
  #Track the number of turns and reduce by 1 if they get it wrong.
  
  #Repeat the guessing functionality if they get it wrong.