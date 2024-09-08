import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0
if mode == "easy":
    attempts = 10
elif mode == "hard":
    attempts = 5
number = random.randint(1,100)

print(number)
while attempts > 0:
    print(f"You have {attempts} remaining to guess the number")
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The number was {number}")
        break
    elif guess > number:
        print("Too high\nGuess again")
    elif guess < number:
        print("Too low\nGuess agin")
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses, you lose.")


