"""
Basic version of a name guessing game 
* what can be easily changed: user input, number of players, case sensitivity, ...
"""

print("I am thinking of a name. Let's see if you can guess it!")
name = "paula"
guess_count = 0

while guess_count < 10:
    guess = str(input("Your guess: "))
    guess_count += 1

    if guess == name:
        print(f"Congratulations! You guessed the name '{name}' in {guess_count} tries.")
        break
    else:
        print("Incorrect guess. Try again!")

if guess_count == 10:
    print(f"You've used all your tries. The name was '{name}'.")