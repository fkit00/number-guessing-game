#Number Guessing Game Objectives:
#from art import logo 
import random
from art import logo 
print(logo)

# Allow the player to submit a guess for a number between 1 and 100. do we want a function that takes in the number of guesses? 
number = random.randint(1,100)
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
 if number_of==0:
  print(f"You've run out of guesses, the number was {number}")
      
def game_function():
  print("Welcome to the guessing game!")
  level=input("Do you want to play on the easy or hard level?: ")
  if level =='easy':
    guessing_game(10)
  else:
    guessing_game(5)







# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).



game_function()