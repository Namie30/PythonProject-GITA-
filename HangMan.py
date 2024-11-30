import random


def hangman():
    words = ['tbilisi', 'batumi', 'svaneti', 'kutaisi', 'borjomi', 'adjara', 'rioni', 'mestia']

    word = random.choice(words)
    guessed_word = ['_'] * len(word)

    attempts = 6
    guessed_letters = []

    print("Welcome to the Region Guessing Game in Georgia!")
    print("Try to guess the name of a region, city, or landmark in Georgia.")

    while attempts > 0:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"You have {attempts} attempts left.")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for index, letter in enumerate(word):  # amit vigebt poziciis nomers da im asos
                if letter == guess:
                    guessed_word[index] = guess
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts -= 1
            print(f"Sorry, '{guess}' is not in the word.")

        if '_' not in guessed_word:
            print(f"\nCongratulations! You've guessed the word: {word.upper()}!")
            break
    else:
        print(f"\nYou've run out of attempts! The word was: {word.upper()}")


hangman()
