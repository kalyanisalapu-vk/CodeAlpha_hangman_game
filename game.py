import random

# Updated words list
words = ["pizza", "python", "monkey", "happy", "laptop", "ninja", "cake", "friend", "smile"]

word = random.choice(words)

guessed = []
chances = 6

print("🎮 Welcome to Hangman Game")

while chances > 0:
    display = ""
    
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    
    print("\nWord:", display.strip())
    print("Guessed letters:", guessed)

    if "_" not in display:
        print("🎉 You won!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter!")
        continue

    if guess in guessed:
        print("⚠️ You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        chances -= 1
        print("Chances left:", chances)

if chances == 0:
    print("😢 You lost! The word was:", word)