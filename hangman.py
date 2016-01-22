'''
Plays a game of hangman when run.  Will process a text file of words
representing the dictionary of words to be used in the game.  A user can then
repeatedly play games of hangman, and will be shown the statistics of the amount
of wins/losses from all the games played.
'''



if __name__ == '__main__':
    import random
    from hangman_lib import *

    totalRoundsPlayed = 0
    totalWins = 0

    printWelcome()

    words = processDictionary('dictionary.txt') #generate words to be used


    #Prompt user to play, pick out a random word and use for the game
    #record if the round was a win or a loss and prompt user to replay
    ans = input("Would you like to start a round? ")
    while ans == 'y' or ans == 'Y':
        randomWord = random.choice(words)
        result = playRound(randomWord)
        if result:
            totalRoundsPlayed += 1
            totalWins += 1
        else:
            totalRoundsPlayed += 1

        ans = input("Good game, enter y or Y to play again: ")

    printResults(totalRoundsPlayed, totalWins) #show the final statistics
