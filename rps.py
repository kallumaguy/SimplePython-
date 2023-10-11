#This is a simple example program of rock, paper and scissors.

import random
comp_choice = random.choice(['scissors','rock','paper'])

user_choice = input('Choose - rock,paper,scissors\n')

if comp_choice == user_choice:
    print("TIE")
elif user_choice == 'rock' and comp_choice == 'scissors':
    print("WIN, the computer had " + comp_choice)
elif user_choice == 'paper' and comp_choice == 'rock':
    print("WIN, the computer had " + comp_choice)
elif user_choice == 'scissors' and comp_choice == 'paper':
    print("WIN, the computer had " + comp_choice)
else:
    print("You lose,the computer had " + comp_choice)
