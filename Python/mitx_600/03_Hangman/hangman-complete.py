# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    output = '' 
    for char in secretWord:
        if char in lettersGuessed:
            output += char
        else:
            output += '_'
    return output

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    output = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if char not in lettersGuessed:
            output += char
    return output  

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    mistakesMade = 0
    lettersGuessed = ''
    availableLetters = ''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secretWord)))


    while True:
        print('----------')
        print('You have {} guesses left'.format(8- mistakesMade))
        availableLetters = getAvailableLetters(lettersGuessed)
        print('Available letters:', availableLetters)
        guess = input('Please guess a letter: ')
        guessInLowerCase = guess.lower()

        if guessInLowerCase not in availableLetters:
            print('Oops! You\'ve already guessed that letter:',
                  getGuessedWord(secretWord, lettersGuessed))
        elif guessInLowerCase in secretWord:
            lettersGuessed += guessInLowerCase
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guessInLowerCase
            mistakesMade += 1
            print('Oops! That letter is not in my word:',
                  getGuessedWord(secretWord, lettersGuessed))

        if mistakesMade == 8:
            print('----------')
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        elif isWordGuessed(secretWord, lettersGuessed):
            print('----------')
            print('Congratulations, you won!')
            break

# Choose a word and play the game
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
