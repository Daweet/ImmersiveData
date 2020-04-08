#The following code mimics the game rock-paper-scissors game
from random import randint
play_list = ['rock', 'paper', 'scissors']
#comp_choice = random.choices(comp_list, weights = None)
comp_choice = play_list[randint(0,2)]

your_choice = True
#your_choice = input('rock, paper, scissors: ')
while your_choice:#when it equals True
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
 #Asking if they want to replay the game           
    play_again=str(input("Do you want to play again?, type yes or no: "))
    if play_again == "no":
        #your_choice = False
        break
