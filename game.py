import random

words = ["apple", "banana", "grape", "mango","strawberry"]
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
    
    # Check win
    if "_" not in display:
        print("🎉 You won!")
        break
    
    guess = input("Enter a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single letter!")
        continue
    
    # ✅ If already guessed → show warning
    if guess in guessed:
        print("⚠️ You already guessed that letter!")
    
    # Check correct or wrong
    if guess in word:
        print("✅ Correct!")
    else:
        print("❌ Wrong!")
        chances -= 1
        print("Chances left:", chances)
    
    # Add to guessed list (after checking)
    if guess not in guessed:
        guessed.append(guess)

# If lost
if chances == 0:
    print("😢 You lost! The word was:", word)