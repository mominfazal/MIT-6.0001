# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    in_file = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
WORDLIST = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
    lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
    assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
    False otherwise
    '''

    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_secret_word = secret_word
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_secret_word = guessed_secret_word.replace(letter, "_ ")

    return guessed_secret_word

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    lowercase_letters = string.ascii_lowercase
    for letter in letters_guessed:
        lowercase_letters = lowercase_letters.replace(letter, "")

    return lowercase_letters


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed_word_so_far = ""
    print(secret_word)
    print(" Welcome to the game Hangman!",
          "I am thinking of a word that is",
          len(secret_word),
          "letters long.")
    lives_left = 6
    letters_guessed = []
    while lives_left:
        if is_word_guessed(secret_word, letters_guessed):
            print("you won")
            break

        print("You have", lives_left, "lives left")
        letter = input("Guess a letter: ")
        if letter.isalpha():
            letters_guessed.append(letter)
            if letter in secret_word:
                guessed_word_so_far = get_guessed_word(
                    secret_word, letters_guessed)
                print("Guessed word so far is", guessed_word_so_far)
                print("Available letters are",
                      get_available_letters(letters_guessed))
            else:
                print("one live lost")
                lives_left = lives_left - 1
    if lives_left == 0:
        print("You lost the game")
    else:
        print("You guessed the word")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace("_ ", "_")
    if len(other_word) != len(my_word):
        return False

    for i, letter in enumerate(my_word):
        if letter == "_":
            continue
        if letter is not other_word[i]:
            return False
    return True

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''

    suggestions = []
    for word in WORDLIST:
        if match_with_gaps(my_word, word):
            suggestions.append(word)

    print(suggestions)
    if suggestions:
        for word in suggestions:
            print(word)
    else:
        print('No suggestions found')

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessed_word_so_far = ""
    print(secret_word)
    print(" Welcome to the game Hangman!",
          "I am thinking of a word that is",
          len(secret_word),
          "letters long.")
    lives_left = 6
    letters_guessed = []
    while lives_left:
        if is_word_guessed(secret_word, letters_guessed):
            print("you won")
            break

        print("You have", lives_left, "lives left")
        letter = input("Guess a letter: ")
        if len(letter) == 1:
            if letter.isalpha():
                letters_guessed.append(letter.lower())
                if letter in secret_word:
                    guessed_word_so_far = get_guessed_word(
                        secret_word, letters_guessed)
                    print("Guessed word so far is", guessed_word_so_far)
                    print("Available letters are", get_available_letters(letters_guessed))
                else:
                    print("one live lost")
                    lives_left -= 1
            elif letter == "*":
                if guessed_word_so_far:
                    show_possible_matches(guessed_word_so_far)
                    lives_left -= 1
                else:
                    print("First letter cannot be *")
                continue
            else:
                print("Please type only letter")
        else:
            print("Please type single letter at a time")
    if lives_left == 0:
        print("You lost the game")
    else:
        print("You guessed the word")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(WORDLIST)
    # hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(WORDLIST)
    hangman_with_hints(secret_word)
