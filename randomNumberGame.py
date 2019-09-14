import random

print("Hello. What's your name?")
playerName = input()

print("Well, " + playerName + ", I'm thinking of a number between 1 and 20.")
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print("Take a guess.")
    while True:
        try:
            playerGuess = int(input())
        except ValueError:
            print('Please enter a number.')
            continue
        else:
            break
    if playerGuess > secretNumber:
        print('That number is too high.')
    elif playerGuess < secretNumber:
        print('That number is too low.')
    else:
        break

if playerGuess == secretNumber:
    print('You are correct! ' + str(secretNumber) + ' is what I was thinking.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')
            
