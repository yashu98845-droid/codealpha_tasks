import random     # used to generate the random values or numbers
words = ["apple", "banana", "cherry", "date", "elderberry"]      # list of words to choose from
word = random.choice(words)      #method used to select a random word from the list
attempts = 6                     #total attempts allowed for the player to guess the word
print("Welcome to Hangman Game!")     #first message displayed to the player when the game starts
word_display = ["_"] * len(word)      #list used to display the guessed letters and underscores for unguessed letters
print(word_display)             #display the initial state of the word

print("guess the word one letter at a time")    #instructions for the player
while attempts > 0:                           #loop continues until the player runs out of attempts or guesses the word
    guess = input("Enter a letter: ").lower()        #take input from the player and convert it to lowercase
    print(f"You guessed: {guess}")                  #display the guessed letter
    print(f"Current word: {' '.join(word_display)}") #display the current state of the word
    print(f"Remaining attempts: {attempts}")        #display the remaining attempts
    if guess in word:                                #check if the guessed letter is in the word
        for i in range(len(word)):                   #loop through each letter in the word
            if word[i] == guess:                     #if the guessed letter matches the letter in the word, update the display list
                word_display[i] = guess              
    else:                                  #if the guessed letter is not in the word, decrement the attempts and display a message
        attempts -= 1                 
        print(f"Wrong guess! You have {attempts} attempts left.") #remaining attempts are displayed to the player
    if "_" not in word_display: #if there are no underscores left in the display list, it means the player has guessed the word correctly
        print(f"Congratulations! You guessed the word: {word}")    #display a congratulatory message
if attempts == 0:                                   #if the player runs out of attempts, display a game over message along with the correct word
    print(f"Game over! The word was: {word}")      #display the correct word




    # THIS IS THE HANGMAN GAME CODE. IT IS A SIMPLE WORD GUESS.
    # THANK YOU FOR USING THIS CODE. I HOPE YOU ENJOYED IT.