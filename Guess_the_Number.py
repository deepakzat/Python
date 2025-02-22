print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number b/w 1 to 100")

import random
number = random.randint(1,100)



difficulty=input("Choose a difficulty. Type 'easy' or 'hard':").lower()

if difficulty=='easy':
    attempts=10
else:
    attempts=5

while attempts>0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess=int(input("Make a guess: "))
    if guess==number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess>number:
        print("Too high.")
    else:
        print("Too low.")
    attempts-=1
    if attempts==0:
        print(f"You've run out of guesses, you lose.the correct number is {number}")

    else:
        print("Guess again.")

