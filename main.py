#Number Guessing Game Objectives:
#from art import logo 

import random

#print(logo)

number =30



# the number guess will be random.randint(1-100)

# Allow the player to submit a guess for a number between 1 and 100. do we want a function that takes in the number of guesses? 

def guessing_game(number_of):
 while number_of != 0:
    number_of=number_of-1
    guess = int(input('Make a guess: '))
    if guess > number and number_of != 0:
      print('Too high, try again')
      print(f'You have {number_of} remaining guesses')
    if guess < number and number_of != 0 :
      print('Too Low, try again')
      print(f'You have {number_of} remaining guesses')
    if guess == number:
      print(f"Congratulations you've guessed the number! It was {number}")
      return
print(f"You've run out of guesses you lose, the number was {number} ")
      
guessing_game(5)


# If they run out of turns, provide feedback to the player.

# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

