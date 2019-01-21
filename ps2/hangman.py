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
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
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
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for letter in secret_word:
      if(letter not in letters_guessed):
        return False
    return True

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out = ''
    for letter in secret_word:
      if(letter not in letters_guessed):
        out += '_ '
      else:
        out += letter
    return out

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word,letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out = ''
    for letter in string.ascii_lowercase:
      if(letter not in letters_guessed):
        out += letter
    return out

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_available_letters(letters_guessed))    

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
    # secret_word while you're doing your own testing)
    print('-----------------------------------------')
    print('Welcome to the game Hangman!')
    print('I am thinking of the word that is ' + str(len(secret_word)) + ' letters long.')
    
    unique_letters = len(string.ascii_lowercase) - len(get_available_letters(list(secret_word))) 

    print('You have 3 warnings left.')
    print('-----------------')

    
    guesses_left = 6
    warnings_lelft = 3

    letters_guessed = []
    while(guesses_left > 0):

      print('You have ' + str(guesses_left) + ' guesses left.')
      print('Available letters: ', get_available_letters(letters_guessed))
      letter_guessed = input('Please guess a letter: ')
      if(letter_guessed in secret_word and letter_guessed not in letters_guessed):
        letters_guessed +=  [letter_guessed]
        print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
      elif(letter_guessed in secret_word and letter_guessed in letters_guessed):
        if(warnings_lelft >= 1):
          warnings_lelft -= 1
          print("Oops! You've already guessed that letter. You have " + str(warnings_lelft) + ' warnings left:')
          print(get_guessed_word(secret_word, letters_guessed))
        else:
          guesses_left -= 1
          print("Oops! You've already guessed that letter. You have no warnings_left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
        letters_guessed += [letter_guessed]  
      elif(letter_guessed not in secret_word):
        if(letter_guessed not in letters_guessed):
          if(letter_guessed.islower() and letter_guessed.isalpha()):
            if(letter_guessed == 'a' or letter_guessed == 'e' or letter_guessed == 'i' or letter_guessed == 'o' or letter_guessed == 'u'):
              guesses_left -= 2
            else:
              guesses_left -= 1
            print('Oops! That letter is not in my word.')
            print('Please guess a letter: ', get_guessed_word(secret_word, letters_guessed))
          else:
            if(warnings_lelft >= 1):
              warnings_lelft -= 1
              print('Oops! That is not a valid letter. You have ' + str(warnings_lelft) + ' warning left: ', get_guessed_word(secret_word, letters_guessed))
            else:
              guesses_left -= 1
              print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))   
        else:
          if(warnings_lelft >= 1):
            warnings_lelft -= 1
            print("Oops! You've already guessed that letter. You have " + str(warnings_lelft) + ' warning left: ')
            print(get_guessed_word(secret_word, letters_guessed))
          else:
            guesses_left -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))        
        letters_guessed += [letter_guessed]
  
      print('-------------------------')

      if(is_word_guessed(secret_word, letters_guessed)):
        print('Congratulations, you won!')
        print('Your total score for this game is: ', guesses_left * unique_letters)
        return None

    print('Sorry, you ran out of guesses. The word was ' + secret_word)

# secret_word = 'else'
# hangman(secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
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
    tmp = my_word.split()
    this_word = ''
    for t in tmp:
      this_word += t 
    #print(this_word)
    if(len(this_word) != len(other_word)):
      return False
    else:
      for i in range(len(other_word)):
        if(this_word[i] == '_' and other_word[i] in this_word):
          return False
        elif(this_word[i] != '_' and this_word[i] != other_word[i]):
          return False
    return True

#print(match_with_gaps("a_ _ le","apple"))

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out = ''
    for word in wordlist:
      if(match_with_gaps(my_word, word)):
        out += word 
        out += ' '
    if(len(out) != 0):
      print(out)
    else:
      print('No matches found')

#show_possible_matches("a_ pl_ ")


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('-----------------------------------------')
    print('Welcome to the game Hangman!')
    print('I am thinking of the word that is ' + str(len(secret_word)) + ' letters long.')
    
    unique_letters = len(string.ascii_lowercase) - len(get_available_letters(list(secret_word))) 

    print('You have 3 warnings left.')
    print('-----------------')

    
    guesses_left = 6
    warnings_lelft = 3

    letters_guessed = []
    while(guesses_left > 0):
      print('You have ' + str(guesses_left) + ' guesses left.')
      print('Available letters: ', get_available_letters(letters_guessed))
      letter_guessed = input('Please guess a letter: ')
      if(letter_guessed == '*'):
        print('Possible word matches are: ')
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      else:
        if(letter_guessed in secret_word and letter_guessed not in letters_guessed):
          letters_guessed +=  [letter_guessed]
          print('Good guess: ', get_guessed_word(secret_word, letters_guessed))
        elif(letter_guessed in secret_word and letter_guessed in letters_guessed):
          if(warnings_lelft >= 1):
            warnings_lelft -= 1
            print("Oops! You've already guessed that letter. You have " + str(warnings_lelft) + ' warnings left:')
            print(get_guessed_word(secret_word, letters_guessed))
          else:
            guesses_left -= 1
            print("Oops! You've already guessed that letter. You have no warnings_left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
          letters_guessed += [letter_guessed]  
        elif(letter_guessed not in secret_word):
          if(letter_guessed not in letters_guessed):
            if(letter_guessed.islower() and letter_guessed.isalpha()):
              if(letter_guessed == 'a' or letter_guessed == 'e' or letter_guessed == 'i' or letter_guessed == 'o' or letter_guessed == 'u'):
                guesses_left -= 2
              else:
                guesses_left -= 1
              print('Oops! That letter is not in my word.')
              print('Please guess a letter: ', get_guessed_word(secret_word, letters_guessed))
            else:
              if(warnings_lelft >= 1):
                warnings_lelft -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings_lelft) + ' warning left: ', get_guessed_word(secret_word, letters_guessed))
              else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))   
          else:
            if(warnings_lelft >= 1):
              warnings_lelft -= 1
              print("Oops! You've already guessed that letter. You have " + str(warnings_lelft) + ' warning left: ')
              print(get_guessed_word(secret_word, letters_guessed))
            else:
              guesses_left -= 1
              print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:", get_guessed_word(secret_word, letters_guessed))        
          letters_guessed += [letter_guessed]
    
        print('-------------------------')

        if(is_word_guessed(secret_word, letters_guessed)):
          print('Congratulations, you won!')
          print('Your total score for this game is: ', guesses_left * unique_letters)
          return None

    print('Sorry, you ran out of guesses. The word was ' + secret_word)

hangman_with_hints('apple')

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
