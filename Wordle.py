########################################
# Name: Sam Dyke
# Collaborators (if any): Some help from Prof. Deutschbein, major help from Quad Center people, mainly Olivia, my section leader.
# GenAI Transcript (if any):
# Estimated time spent (hr): 5 hrs ish
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random
import string

def wordle():
    # The main function to play the Wordle game.
    def enter_action(): # What should happen when RETURN/ENTER is pressed.
        Guess="" #initially sets Guess as blank word
        r=gw.get_current_row() #sets variable r to represent the number value of the current row.
        for i in range(0,5): #runs code contained below 5 times. 
        	letter=gw.get_square_letter(gw.get_current_row(),i) #scans each column in the current row to check the letters of the guess word.
        	Guess+=letter #adds each letter to the Guess to fill out the blank word.
        guess=Guess.lower() #changes the Guess word that is currently upper-case into lower-case so that...
        #...it matches the lower-case words in ENGLISH WORDS.
        if guess in ENGLISH_WORDS: #checks if guess is a word in ENGLISH_WORDS.
        	unmatched = hw #variable to represent the as-yet-unmatched letters.
        	for l in range(len(guess)):	#each letter position in the word. l stands for letter.
        		if guess[l] == unmatched[l]:	#the letter in that position matches the hidden word:
        			gw.set_square_color(r, l, CORRECT_COLOR)	#Color that square green
        			unmatched = unmatched.replace(guess[l], "_",1) #removes letter from unmatched letters
        			gw.set_key_color(guess[l], CORRECT_COLOR) #sets correct letter keys as green.
        	for l in range(len(guess)): #each letter position in the word. l stands for letter.
        		if gw.get_square_color(r,l) == UNKNOWN_COLOR: #the square in that position is not already colored
        			if guess[l] in unmatched:#the letter in that position is in the unmatched collection:
        				gw.set_square_color(r, l, PRESENT_COLOR)	#Color that square yellow.
        				unmatched = unmatched.replace(guess[l],"_",1) #removes letter from unmatched letters
        				if gw.get_key_color(guess[l]) != CORRECT_COLOR: #If key is already colored green...
        					gw.set_key_color(guess[l], PRESENT_COLOR) #...colors letter key Yellow.
        			else: #if letter is not in the hidden word:
        				gw.set_square_color(r, l, MISSING_COLOR)	#Color that square gray
        				if gw.get_key_color(guess[l]) == UNKNOWN_COLOR: #if that letter key is white...
        					gw.set_key_color(guess[l], MISSING_COLOR) #...color it gray.
        	gw.set_current_row(gw.get_current_row()+1) #at the end of checking a guess, move to the next row for the next guess.
        else: #if not in ENGLISH_WORDS
        	gw.show_message("not English Word") #show message informing the player that their guess was not an English Word.
        if r==5: #When last guess is incorrect:
        	gw.set_current_row(N_ROWS) #ends game.
        	gw.show_message(hw) #informs the player of the correct word.
        if guess == hw: #if the guessed the answer:
        	gw.set_current_row(N_ROWS) #ends game.
        	gw.show_message("Wordle Complete!") #informs the player that they got the right answer.
		

        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
   
hw = "" #variable for hidden word.

while len(hw)!=5: #when the length of hw is specifically equal to a length of 5 characters.
	hw=random.choice(ENGLISH_WORDS) #sets hw to a random word in ENGLISH_WORDS.
print(hw) #this only prints in terminal and will not show up anywhere on the Wordle popup.




# Startup boilerplate
if __name__ == "__main__":
    wordle()
