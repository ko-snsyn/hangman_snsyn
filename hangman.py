#!/usr/bin/env python
# coding: utf-8

# In[5]:


####################################################################################
######################### Hangman - Sensyne Health #################################
####################################################################################


print("HANGMAN Word Game .............. ")
print("Ready to Start? ")

#Scoring
playername = input('What is your Name?  ')


##################################################
########### Display Current Score Board###########
##################################################
import pandas as pd

# print ScoreBoard.
from tabulate import tabulate
df_Score = pd.read_csv('scoreboard.csv') #load the DF
scoreboard_summary = df_Score.groupby(['Name']).sum(); #Aggregate Data
scoreboard_display = scoreboard_summary.sort_values(by='Score', ascending=False).reset_index().head(10) #Sort Data
print(tabulate(scoreboard_display, headers='keys', tablefmt='psql')); #display Current ScoreBoard


########### End Display Current Score Board###########


##################################################
################### Game / Event #################
##################################################

import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("please guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print(playername + " Congrats, that's the word! You win!")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("------------------------------------------------")
        print("     Sensyne Health Hangman Score")
        print("------------------------------------------------")
        print("PlayerName - " + playername + "  |  Score   +" + str(10))  
        
        name = playername
        win = 10    
        
        
        data = [[name, win]] # initialize list of lists
        df = pd.DataFrame(data, columns = ['Name', 'Score']) # Create the pandas DataFrame of the Current Score
        df.to_csv(r'currentscoreboard.csv', mode='w+', index = False, header=False) #overwrite currentscore file#
        df.to_csv(r'scoreboard.csv', mode='a', index = False, header=False) #insert current score to scoreboard file


    else:
        print("Sorry, you ran out of tries. The word was " + word + ". Try Again?")
        print("                                        ")
        print("                                        ")
        print("                                        ")
        print("------------------------------------------------")
        print("     Sensyne Health Hangman Score")
        print("------------------------------------------------")
        print("PlayerName - " + playername + "  |  Score    " + str(0))
        
################### ENd Game / Event #################


####################################################################
################### Display Hangman after each try #################
####################################################################

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


####################################################################
################### Main Method to Start the Game ##################
####################################################################

def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()


# In[ ]:




