rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
from random import randint
options = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
choice = options[int(input('What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors.'))]
computerchoice = options[randint(0,2)]
print('You choose:')
print(choice)
print('Computer chose:')
print(computerchoice)
if choice == options[0] and computerchoice == options[0] or choice == options[1] and computerchoice == options[1] or choice == options[2] and computerchoice == options[2]:
  print('Draw.')
elif choice == options[1] and computerchoice == options[0]:
  print('You win.')
elif choice == options[2] and computerchoice == options[0]:
  print('You lose.')
elif choice == options[0] and computerchoice == options[1]:
  print('You lose.')
elif choice == options[2] and computerchoice == options[1]:
  print('You win.')
elif choice == options[0] and computerchoice == options[2]:
  print('You win.')
elif choice == options[1] and computerchoice == options[2]:
  print('You lose.')

