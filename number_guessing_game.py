"""
Basic version of a number guessing game
*what can be easily changed:    
-the range of numbers.
- the amount of guesses.
- print message for when a user is not putting a number in.
"""

import random

secret_number = random.randint(1, 30)
guesses_taken = 0

print('I am thinking of a number between 1 and 30.')

while guesses_taken < 6:
    guess = int(input('Take a guess: '))
    guesses_taken += 1

    if guess < secret_number:
        print('Your guess is too low.')
    elif guess > secret_number:
        print('Your guess is too high.')
    else:
        break

  # Correct guess
if guess == secret_number:
    print(f'Good job! You guessed my number in {guesses_taken} guesses.')
else:
    print(f'Nope. The number I was thinking of was {secret_number}')
