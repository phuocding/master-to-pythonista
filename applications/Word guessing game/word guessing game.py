#!/usr/bin/env python
# coding: utf-8

# In[6]:


#word guessing game in python
#Create a dictionary of words to play
word_box={'1':'python','2':'elephant','3':'cheetah','4':'giraffe','5':'rabbit'}
print('Choose a word to play by entering any number from 1 to 5')

#Input a number in the dictionary to choose a word to guess
x=str(input())

#store the word in the name'puzzle'
puzzle=word_box.get(x)

#create a list to store the characters in the word
puzzle_list=[]
for i in range(len(puzzle)):
    puzzle_list.append(puzzle[i])
    
#transform the list to a set to avoid repeated characters
puzzle_set=set(puzzle_list)

#print the rules of the game
print('Rules of the game:')
print('1. You have 10 chances to guess this %d letter word' %len(puzzle))
print('2. Enter the characters one by one. \n3. No need to repeat the same characters')

#give 10 chances for the player to guess the word
no_of_guesses=10

#Iterate the loop to get the characters from the player and to check if its right or wrong
for i in range(0,10):
    print('chance', i+1)
    
    #get the character from the player
    character_guess=(str(input())).lower()
    
    #decrease the number of guesses by 1
    no_of_guesses=no_of_guesses-1
    
    #check if the character is in the set we created
    if character_guess in puzzle_set:
        
    #if yes, remove it from the set and print 'correct' to let the player know
        puzzle_set.remove(character_guess)
        print('Correct guess')
    
    #if no, print 'wrong guess'
    else:
        print('Wrong guess')
        
    #check if player guessed all the characters correctly, if yes, break the loop and print the correct answer
    if len(puzzle_set) == 0:
        print('You won! The answer is', puzzle)
        break
    
    #check if number of guesses is zero
    if no_of_guesses == 0:
        print('You lost! Better luck next time!')
            


# In[ ]:




