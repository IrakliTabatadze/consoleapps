import random

word_list = ['python', 'java', 'swift', 'hangman', 'kotlin', 'javascript']


def choose_word(word_list):
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in already_guessed:
                print(f"You already guessed '{guess}'. Try again.")
            else:
                return guess
        else:
            print("Invalid input. Please enter a single letter.")


def play_hangman():
    word = choose_word(word_list)
    guessed_letters = set()
    incorrect_guesses = set()
    max_attempts = 6

    print("Welcome to Hangman!")

    while len(incorrect_guesses) < max_attempts:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Incorrect guesses ({len(incorrect_guesses)}/{max_attempts}):", ' '.join(incorrect_guesses))

        guess = get_guess(guessed_letters | incorrect_guesses)

        if guess in word:
            guessed_letters.add(guess)
            if set(word) == guessed_letters:
                print(f"Congratulations! You guessed the word '{word}'!")
                break
        else:
            incorrect_guesses.add(guess)
            print(f"Incorrect guess: '{guess}'")

    if len(incorrect_guesses) == max_attempts:
        print(f"\nYou've been hanged! The word was '{word}'.")


if __name__ == "__main__":
    play_hangman()
