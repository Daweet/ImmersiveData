"""This is a Rock, Paper, Scissors game."""

prompt = "\nWelcome to the Rock, Paper, Scissors game. Enter your play choice: "

user_play = input(prompt)
opponent_play = 'rock'
#import random
#opponent_choice = ['rock','paper','scissors']
#choice_index = random.randint(0,2)
#opponent_play = opponet_choices[choice_index]
# the keys in the root dictionary will be the user play
# the keys in the nested dictionaries are for the opponent's play
# will be used to extract win/lose outcome
win_lose_combo = {'rock':{'scissors':'win!',
                          'paper': 'lose.'
                         },
                  'paper':{'rock': 'win!',
                           'scissors': 'lose.'
                          },
                  'scissors':{'paper': 'win!',
                              'rock': 'lose.'
                             }
                 }

if user_play == opponent_play:
    print("It's a draw.")
else:
    outcome = win_lose_combo[user_play][opponent_play]
    print(f"Your opponent chose {opponent_play}. You {outcome}")