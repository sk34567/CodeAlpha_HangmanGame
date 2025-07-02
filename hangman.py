import random

def get_random_word():
    words = ['apple', 'banana', 'grape', 'orange', 'mango']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    print("🎮 Welcome to Hangman Game!")
    word_to_guess = get_random_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("✅ Good guess!")
        else:
            attempts -= 1
            print(f"❌ Wrong guess. Attempts left: {attempts}")

        if all(letter in guessed_letters for letter in word_to_guess):
            print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
            break
    else:
        print("\n💀 Game Over! The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
