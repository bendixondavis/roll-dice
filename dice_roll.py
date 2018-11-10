import random

num_sides = 0
result = 0
flip_again = 'y'

#the int() around the input casts the string input to an int
num_sides = int(input("How many sides do you want die to have? "))

while flip_again == 'y':
    result = random.randint(1,num_sides)
    print("You rolled a : ",result)
    flip_again = input("Play Again(y/n)")
