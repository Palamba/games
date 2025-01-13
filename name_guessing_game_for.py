"""
Name guessing game with a FOR loop
"""

name = "paula"
guess_count = 0

for _ in range(10):
    guess = input("Guess the name: ")
    guess_count += 1

    if guess == name:
        print(f"Congratulations! You guessed the name '{name}' in {guess_count} tries.")
        break
else:
    print(f"You've used all your tries. The name was '{name}'.")