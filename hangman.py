#pictures, just for aesthetics
hanged = [list(" _ _ _ _ _ _"),
          list("|     |     "),
          list("|    ( )    "),
          list("|   __|__   "),
          list("|     |     "),
          list("|    / \    "),
          list("|           ")]


free = [ list(" _ _ _ _ _ _"),
         list("|     |     "),  
         list("|           "), 
         list("|     \( )/ "),          
         list("|      \|/  "),        
         list("|    \  |   "),      
         list("|     \/ \  "),
         list("          \ ")]


dead = [list(" _ _ _ _ _ _"),
        list("|     |     "),     
        list("|     |     "),    
        list("|    (++)   "),   
        list("|    /|\    "),    
        list("|     |     "),   
        list("|    / \    ")]
    

#function to print pics
def print_pics(figure):
    for i in range(len(figure)):
        for j in figure[i]:
            print(j, end="")
        print("")    

# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

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

# end of helper code
# -----------------------------------

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
    word = list(secretWord)

    for alphabet in word:
        if alphabet not in lettersGuessed:
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = list(secretWord)
    
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            word[i] = "_ "
    
    return "".join(word)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    return "".join([i for i in alphabets if i not in lettersGuessed])    

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
    print("\nWelcome to the game, Hangman!")
    print("\nI am thinking of a word that is", len(secretWord), "letters long...")
    lettersGuessed = []
    mistakesMade = 0
    
    while True:
        print("==#==#==#==#==#==#==#==#==#==#==#==#==#==#==")
        print_pics(hanged)      
        print("You have", 8-mistakesMade, "guesses left.")
        print("Available letters:", getAvailableLetters(lettersGuessed))
        x = input("Please guess a letter: ")
        
        if x in lettersGuessed:
            print("Oops! You have already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            continue
        else:
            lettersGuessed.append(x)
            if isWordGuessed(secretWord, lettersGuessed):
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
                print("==#==#==#==#==#==#==#==#==#==#==#==#==#==#==")
                print_pics(free)      
                return "\nCongratulations, you won!\nThe Hangman is free!"
            elif x in secretWord:
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                mistakesMade += 1
        if mistakesMade == 8:
            print("==#==#==#==#==#==#==#==#==#==#==#==#==#==#==")
            print_pics(dead)      
            print("Sorry, you ran out of guesses. The word was", secretWord)
            print("Alas! The Hangman died :\(")
            print("Better luck next time!")
            
            return ""

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))
input()

