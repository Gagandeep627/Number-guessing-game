


import random
import math

lower = int(input("Enter Lower bound:- "))

upper = int(input("Enter Upper bound:- "))


x = random.randint(lower, upper)


y = round(math.log(upper - lower + 1, 2))

print("\n\tYou've only ", y, " chances to guess the integer!\n")


count = 1

while count < math.log(upper - lower + 1, 2):
    


    guess = int(input("Guess a number:- "))

    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
    
    count += 1



if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")
