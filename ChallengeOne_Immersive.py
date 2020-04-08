#!/usr/bin/env python
# coding: utf-8

# Create a program where the user can play a game of rock, paper, scissors against a computer. Set a play choice (rock, paper, or scissors) for the computer player and during the program, request for the user to input their play choice.
# 
# The rules in Rock, Paper, Scissors are:
# 
# * Rock beats scissors 
# * Scissors beats paper 
# * Paper beats rock 
# 
# 
# If the user wins, then display "You win!" If they lose against the computer, then display "You lose." If the computer and the user have the same play choice, display "It's a draw."
# 
# BONUS: Randomize the play choice for the computer (hint: Python has a library called random). Also ask the user if they would like to play again. If they do, start the game again but if not, thank the user for playing the game.


from random import randint
play_list = ['rock', 'paper', 'scissors']
#comp_choice = random.choices(comp_list, weights = None)
comp_choice = play_list[randint(0,2)]

your_choice = True
#your_choice = input('rock, paper, scissors: ')
while your_choice:#your_choice
    your_choice = input('rock, paper, scissors: ')
    if your_choice == comp_choice:
        print("Its a draw!")
    elif your_choice == 'rock': 
        if comp_choice == 'scissors':
            print("You won!")
        else:
            print("You lose!")
            
    elif your_choice == 'scissors':
        if comp_choice == 'paper':
            print("You won!")
        else:
            print("You lose!")
    elif your_choice == 'paper': 
        if comp_choice == 'rock':
            print("You won!")
        else:
            print("You lose!")
    #your_choice = False
    #comp_choice = play_list[randint(0,2)] 
    play_again=str(input("Do you want to play again?, type yes or no: "))
    if play_again == "no":
      your_choice = False
    


# This assignmnet is submitted by Dawit Hailu!
