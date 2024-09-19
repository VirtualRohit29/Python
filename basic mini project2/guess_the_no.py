# we are going to write a program that genertates a random number and asks the user to guess it
#  if the playes guess is hihger than the actual no. the program displays "lower nuber please".similarily ,if the user's guess is too low , the program prints "higher number please ".when the user gusses the correct number  the programm display the number of guesses the player used arrive at the number 

# HINT :- Use the Random module.......

# your code starts here 

import random

n=random.randint(1,100)
a=-1

guesses=1
while(a!=n):
    a=int(input("guess the number: "))
    if(a>n):
        print("plese enter the lower number")
        guesses+=1
    elif(a<n):
        print("plese enter the higher number")
        guesses+=1

print(f"congratulations! you have guess the number :{n} in {guesses} attempts ")        
