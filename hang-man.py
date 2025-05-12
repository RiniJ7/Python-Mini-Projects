import random

hangman_art = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\\  |
  / \\  |
       |
 =========''']

word_list = ["aadvark", "baboon", "camel"]
lives = 6
chosen_word = random.choice(word_list)
# For debugging, remove in final version
# print(chosen_word)

# Initialize display with dashes
display = []
for letter in chosen_word:
    display.append("-")
print("".join(display))

game_over = False
guessed_letters = []  # Track all guessed letters

while not game_over:
    # Show current hangman state
    print(hangman_art[6 - lives])
    
    guess = input("Guess a letter: ").lower()
    
    # Check if letter was already guessed
    if guess in guessed_letters:
        print(f"You already guessed '{guess}'. Try another letter.")
        continue
    
    guessed_letters.append(guess)
    
    # Update display with correct guesses
    found_letter = False
    for position in range(len(chosen_word)):
        if chosen_word[position] == guess:
            display[position] = guess
            found_letter = True
    
    # Print current state of word
    print("".join(display))
    
    # Check if guess was wrong
    if not found_letter:
        lives -= 1
        print(f"'{guess}' is not in the word. You lose a life.")
        
        if lives == 0:
            game_over = True
            print(hangman_art[6])
            print(f"You lose! The word was '{chosen_word}'.")
    
    # Check if player has won
    if "-" not in display:
        game_over = True
        print("You win!")