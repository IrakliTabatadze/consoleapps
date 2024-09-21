import random

min_num = 1
max_num = 100
max_attempts = 10
target_number = random.randint(min_num, max_num)
attempts = 0

print(f"Welcome to the Guess the Number Game! I'm thinking of a number between {min_num} and {max_num}.")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        attempts += 1

        if guess < min_num or guess > max_num:
            print(f"Please guess a number between {min_num} and {max_num}.")
        elif guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
else:
    print(f"Game over! The correct number was {target_number}.")
