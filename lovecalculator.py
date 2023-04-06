# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
totalname = (name1 + name2).lower()
true = totalname.count('t') + totalname.count('r') + totalname.count('u') + totalname.count('e')
true = str(true)
love = totalname.count('l') + totalname.count('o') + totalname.count('v') + totalname.count('e')
love = str(love)
score = true + love
score = int(score)
if score < 10 or score > 90:
  print(f'Your score is {score}, you go together like coke and mentos.')
if 40 < score < 50:
  print(f'Your score is {score}, you are alright together.')
if 10 < score < 40 or 50 < score < 90:
  print(f'Your score is {score}.')


