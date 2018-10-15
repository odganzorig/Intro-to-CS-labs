## guessing_game.py
## Author: <OD GANZORIG>
## Date: <10/07/2017>
##
## Description:
##    A program for playing a number guessing game in a terminal window.
##
##-----------------------------------------------------------------------------
## Import modules and functions
from random import randrange  # generates a random integer from a given range
from sys import exit          # terminates the running program when called

##-----------------------------------------------------------------------------
## set_debugging
##   function: Ask user if game should be run in debugging mode, and set global
##             variable `DEBUGGING`.
##   parameters: none
##   return value: none
##
## DO NOT CHANGE THIS FUNCTION
##-----------------------------------------------------------------------------
def set_debugging():
    global DEBUGGING
    ans = input("Run game in debugging mode (yes/no)?  ")
    DEBUGGING = ans in ["y", "yes", "Y", "Yes"]

##-----------------------------------------------------------------------------
## introduce_game
##   function: Introduce game to user and explain how to play.
##   parameters: none
##   return value: none
##-----------------------------------------------------------------------------
def introduce_game():
    print("Welcome to my number guessing game!Here's how it works.\nI'll ask you for three values: a lower number, a higher number,\nand the number of guesses you want to be allowed to have. All\nvalues should be integers, and the number of guesses should be\nat least 1.\n")

##-----------------------------------------------------------------------------
## check_valid_low_high
##   function: Verifies that the `low_num` and `high_num` game parameters given
##      by the user are valid; terminates program if parameters are invalid.
##   parameters: low_num, high_num
##   return value: none
##-----------------------------------------------------------------------------
def check_valid_low_high(low_num, high_num):
    if low_num>=high_num:
        print("I'm sorry. The low and high numbers that you gave me just won't work.")
        exit()
        

##-----------------------------------------------------------------------------
## check_valid_max_guesses
##   function: Verifies that the `max_guesses` game parameter given by the user
##      is valid; terminates program if parameter is invalid.
##   parameters: max_guesses
##   return value: none
##-----------------------------------------------------------------------------
def check_valid_max_guesses(max_guesses):
    if max_guesses<=0:
        print("I'm sorry. There's no way to win the game with zero or fewer guesses.")
        exit()


##-----------------------------------------------------------------------------
## get_game_params
##   function: Uses standard I/O to get game parameters from user.
##   parameters: none
##   return value: tuple containing lowest number in guess range, highest
##      highest number in guess range, and maximum number of guesses
##-----------------------------------------------------------------------------
def get_game_params():
    low_num = int(input("low number: "))
    high_num = int(input("high number: "))
    check_valid_low_high(low_num, high_num)
    max_guesses = int(input("maximum number of guesses: "))
    check_valid_max_guesses(max_guesses)
    return (low_num, high_num, max_guesses)

   
##-----------------------------------------------------------------------------
## get_num_to_guess
##   function: If DEBBUGGING is False, generates a random integer in the range
##      `low_num` to `high_num`; otherwise, gets the number to guess from the
##      user using standard I/O.
##   parameters: low_num, high_num
##   return value: an integer between low_num and high_num (inclusive)
##
## DO NOT CHANGE THIS FUNCTION
##-----------------------------------------------------------------------------
def get_num_to_guess(low_num, high_num):
    if not DEBUGGING:
        return randrange(low_num, high_num + 1)
    else:
        print("\nrunning in debugging mode...")
        return int(input("What is your number to guess? "))

##-----------------------------------------------------------------------------
## print_too_low_hint
##   function: Outputs a message telling the user that their guess was too low.
##   parameters: none
##   return value: none
##-----------------------------------------------------------------------------
def print_too_low_hint():
        print("Sorry! That guess is too low!")

##-----------------------------------------------------------------------------
## print_too_high_hint
##   function: Outputs a message telling the user that their guess was too high.
##   parameters: none
##   return value: none
##-----------------------------------------------------------------------------
def print_too_high_hint():
        print("Sorry! That guess is too high!")

##-----------------------------------------------------------------------------
## play_game
##   function: Runs the actual guessing game with user until they either guess
##      the number or run out of guesses.
##   parameters: low_num, high_num, num_to_guess, max_guesses)
##   return value: number of guesses taken by the user
##-----------------------------------------------------------------------------
def play_game(low_num, high_num, num_to_guess, max_guesses):
    for i in range(max_guesses):
        ur_guess = int(input("What's your guess? "))
        if ur_guess<num_to_guess:
            print_too_low_hint()
        if ur_guess>num_to_guess:
            print_too_high_hint()
        if ur_guess==num_to_guess:
            return i+1
    return -1

##-----------------------------------------------------------------------------
## main function
##-----------------------------------------------------------------------------
def main():
    set_debugging()
    introduce_game()
    x = get_game_params()
    y = get_num_to_guess(x[0], x[1])
    print("------------------------------------------")
    print("I've picked a number between", x[0], "and", x[1],", and it's your task\nto guess the number that I've picked!\nI'll give you some hints to help you out.\n")
    z = play_game(x[0], x[1], y, x[2]) 
    if z==-1:
        print("Too bad! The number I'd picked was ",y,".", sep="")
    else:
        print("Congratulations! You guessed it in only", z, "guesses.")

main()
