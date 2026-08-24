import random
words = ["apple", "banana", "cherry", "date", "elderberry"]
word = random.choice(words)
attempts = 6
print("Welcome to Hangman Game!")
word_display = ["_"] * len(word)
print(word_display)

print("guess the word one letter at a time")
while attempts > 0:
    guess = input("Enter a letter: ").lower()
    print(f"You guessed: {guess}")
    print(f"Current word: {' '.join(word_display)}")
    print(f"Remaining attempts: {attempts}")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
    else:
        attempts -= 1   
        print(f"Wrong guess! You have {attempts} attempts left.")
    if "_" not in word_display:
        print(f"Congratulations! You guessed the word: {word}")
if attempts == 0:
    print(f"Game over! The word was: {word}")