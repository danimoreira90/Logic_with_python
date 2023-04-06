# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
from random import randint
rpindex = randint(0, len(names))
print(f'{names[rpindex]} is going to buy the meal today!')









