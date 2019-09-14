import random

def playerGuess():
    while True:
        try:
            guess = int(input())
        except ValueError:
            print('Please enter a number.')
            continue
        else:
            return guess

print("Hello. What's your name?")
playerName = input()

print("Well, " + playerName + ", I'm thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = playerGuess()
    if guess > secretNumber:
        print('That number is too high.')
    elif guess < secretNumber:
        print('That number is too low.')
    else:
        print('You are correct!')

print('The number I was thinking of was ' + str(secretNumber) + '.')
            
