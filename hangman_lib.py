def processDictionary(file):
    '''
    Reads in data from a text file, generates a list of words from the file.

    param file[string]: a string representing the file to open
    returns: a list containing the words
    '''
    wordList = []
    inFile = open(file)
    for line in inFile:
        wordList.append(line.strip('\n'))
    return wordList


def revealLetter(prompt, letter, actualWord):
    '''
    Checks to see if a given guessed letter is actually in the hidden word.
    If the letter is in hidden word, reveal the letter in the hidden word's
    prompt.

    param prompt[string]: the hidden word prompt to modify
    param letter[string]: the letter that was guessed

    returns: a string representing the updated prompt for the hidden word
    '''
    charList = list(prompt)
    for i in range(len(actualWord)): #check to see if the letter contianed in hidden word
        if actualWord[i] == letter:
            charList[i] = letter #have the hidden prompt display the letter
        
    return "".join(charList)

def wordToDashes(word):
    '''
    Converts a word to a sequence of dashes, represents a hidden form of the word.

    param word[string]: the word to use to convert to dashes

    returns: a string that is the representation of the word as a sequence of dashes
    '''
    return '_' * len(word)

def isRevealed(hiddenWord):
    '''
    Checks if all letters of hidden word have been correctly guessed.

    param hiddenWord[string]: the hidden word to check

    returns: True or False if the hidden word is fully revealed
    '''
    return '_' not in hiddenWord #word is guessed if the prompt has no more dashes


def playRound(randomWord):
    '''
    plays the game round, returns True if word is guessed, False if not

    param randomWord[string]: the randomly chosen word to use for game round

    returns: True or False if the user correctly reveals the word
    '''
    hiddenWord = wordToDashes(randomWord)

    turnsRemaining = 8
    wrongGuesses = 0
    lettersGuessed = [] #keep track of previously guessed letters

    
    while turnsRemaining > 0: #user can make only 8 wrong guesses
        print("Word to guess is: {}\n".format(hiddenWord))
        ans = input("Please guess a letter: ")
        if (len(ans) != 1) or (ans.lower() not in "abcdefghijklmnopqrstuvwxyz"): #check that a single letter is answered
            print("The input must only be a single letter.")
            continue

        if ans in lettersGuessed: #reprompt if user enters a previously guessed letter
            print("You have already guessed the letter '{}'".format(ans))
            continue
        
        if ans.lower() in randomWord.lower(): #user correctly guessed letter
            lettersGuessed.append(ans)
            print("'{}' is indeed contained in the hidden word!".format(ans))
            hiddenWord = revealLetter(hiddenWord, ans, randomWord) #reveal the letter that was guessed in the prompt
            if isRevealed(hiddenWord): #game ends if word is fully revealed by guessed letters
                print("You have revealed {} as the hidden word!\n".format(randomWord))
                return True
            
        else: #user has guessed wrong, decrement the amount of turns remaining
            lettersGuessed.append(ans)
            wrongGuesses += 1
            turnsRemaining -= 1
            print("Unfortunately '{}' was not contained in the hidden word.".format(ans))
            print("You have currently guessed wrong {} time(s).".format(wrongGuesses))
            print("You have {} more turn(s) remaining.\n".format(turnsRemaining))

    #end the game if the user guesses wrong 8 times
    print("Unfortunately you were not able to guess the word in 8 attempts.")
    print("The hidden word was {}.\n".format(randomWord))
    return False

def printWelcome():
    '''
    Prints the welcome menu for the game of hangman.

    no parameters
    
    no return type.
    '''
    print('\t\t\t' + '*' * 19)
    print("\t\t\tWelcome to Hangman!\n")
    print("A word will randomly be selected from the dictionary.")
    print("You will then have 8 attempts to successfully guess the word.")
    print("Every time you correctly guess a letter, it will be revealed.\n")
    print("Enter y or Y to play a round of hangman, press any other key to quit.")
    print("\t\t\tGOOD LUCK\n")

def printResults(roundsPlayed, wins):
    '''
    Prints the statistics of all the games played, amount of wins and total rounds played.

    param roundsPlayed[int]: the total amount of played rounds
    param wins[int]: the total amount of wins

    no return type
    '''
    print("Your total statistics are as follows:")
    print("Total rounds played\t{}".format(roundsPlayed))
    print("Total times you won\t{}".format(wins))
    print("Thanks for playing the game!")
    print('\t' + '*' * 19)
        


 

    
    
    
