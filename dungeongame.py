print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print('_' * 40)
print('You arrive at the lsland and there are two options. On the left side there is a cave, on the right, a lake. Enter the cave or dive in the lake?')
option1 = str(input('Cave or lake? (right or left) [R/L]: ')).upper()
print('_' * 40)
if option1 == 'L':
  print('You just entered the dark cave.')
  print('When entering the dark cave, you see three doors, one with a face of a lion, another with a face of the tiger and the last with the face of a bear. Which do you enter?')
  option2 = str(input("Enter 'L' for Lion, 'T' for Tiger, and 'B' for Bear.")).upper()
  print('_' * 40)
  if option2 == 'L':
    print("You see the red eyes of the starving lion staring from the back of the room, it's ready too make its move. But there's still hope, in the corner of the room you see two weapons, and axe and a sword, which do you pick?")
    option3 = str(input("'A' for axe or 'S' for sword? [A/S]:")).upper()
    print('_' * 40)
    if option3 == 'S':
      print("You desperately run for the sword. Grab it and when the beast jumps over you with its mouth wide open you luckily crave the blade into its throat. Good move. You may proceed into the cave.")
      print("As you go further the path splits in two, you take left or right?")
      option6 = str(input("Left 'L' or Right 'R' ?")).upper()
      if option6 == 'R':
        print("Good job! You found the chest! Don't go spend your fortune in candies and drugs!")
      else:
        print("Suddenly you stepped in an interruptor which opened a traphole full of spikes beneath you. Game over.")
    else:
      print('You grab the axe. Unfortunately, you swing it towards the beast but there is no use, you end up being ripped apart by its claws and teeth. Game over.')
      print('_' * 40)
  elif option2 == 'T':
    print("As expected. You see the giant tiger but there is no where to run or hide, the beast comes and slashes and bites you with everything its got. No match for you. You're dead. Game over.")
    print('_' * 40)
  elif option2 == 'B':
    print("As you enter the bear room, you can't see quite well because there's not much torches in this area, but is barely visible a giant sillouette of a huge grizzly bear in front of you. Luckily, the beast in entertained with a gigantic pot of honey which seems not to end up fast and for that it did not sense your presence in the room. As time passes by, you spot a table with a shotgun at the other corner of the room, but there's still something telling you that you could try and sneak around the bear wuthout being spotted. what do you do?")
    option5 = int(input('1 for sneak around or 2 for shotgun?'))
    print('_' * 40)
    if option5 == 1:
      print('You quietly passed around the beast without being seen. Good job. Proceed to the depths of the cave.')
      print("As you go further the path splits in two, you take left or right?")
      option7 = str(input("Left 'L' or Right 'R' ?")).upper()
      if option7 == 'R':
        print("Good job! You found the chest! Don't go spend your fortune in candies and drugs!")
      else:
        print("Suddenly you stepped in an interruptor which opened a traphole full of spikes beneath you. Game over.")
      print('_' * 40)
    else:
      print("You walk for the shotgun and try to fire it. It was unloaded, but the beast hears the click of the trigger. You shouldn't have done that. Game over.")
else:
  print('When you jumped into the lake you were drawn into a deadly whirlpool that crushed your bones and ripped your skin and organs. Game over.')



