import random

def play_hangman():
  # list of words to choose from
  words = ["apple", "banana", "orange", "strawberry", "grape"]

  # choose a random word
  word = random.choice(words)

  # create a list of underscores to represent the letters in the word
  word_letters = ["_" for _ in word]

  # set the number of incorrect guesses to zero
  incorrect_guesses = 0

  # set the maximum number of incorrect guesses
  max_incorrect_guesses = 6

  # set the game to not yet be won
  game_won = False

  # ASCII art for the hangman figure
  hangman_art = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
  ]

  # run the game loop
  while not game_won:
    # print the hangman figure
    print(hangman_art[incorrect_guesses])

    # print the current state of the word
    print("Current word: ", " ".join(word_letters))

    # get the player's guess
    guess = str.lower(input("Guess a letter: "))

    # if the guess is correct, update the word to show the correct letters
    if guess in word:
      for i in range(len(word)):
        if word[i] == guess:
          word_letters[i] = guess
      
      # check if the player has won
      if "_" not in word_letters:
        print("You won! The word was:", word)
        game_won = True
    else:
      # if the guess is incorrect, increment the number of incorrect guesses
      incorrect_guesses += 1

      # print a message telling the player how many incorrect guesses they have left
      if incorrect_guesses < max_incorrect_guesses:
        print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "incorrect guesses left.")
      else:
        print("You lost! The word was:", word)
    if game_won = True

# start the game
play_hangman()
