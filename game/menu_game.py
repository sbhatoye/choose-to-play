"""" ************** This is the main file. Please make a selection for which game you want to play. ***************** """

from rock_paper_scissors import play_rock_paper_scissors_game
from hangman import *
from tic_tac_toe import *

menu_options = {
    1: "Rock paper scissors",
    2: "Hangman",
    3: "Tic Tac Toe"
}


while True:
    print("""
Your game menu:
1: Rock paper scissors
2: Hangman
3: Tic-Tac-Toe
""")
    user_game_choice = input("""\n Please select game which game you would like to play.
                            \n Enter 1 for Rock Paper Scissors, 2 for Hangman and 3 efor Tic-Tac-Toe. 
                            \n If you would like to leave the menu, please type 'exit'.   """)

    if user_game_choice == '1':
        play_rock_paper_scissors_game()
        user_game_choice = None

    elif user_game_choice == '2':
        play_hangman_game()
        user_game_choice = None

    elif user_game_choice == '3':
        play_tic_tac_toe_game()
        user_game_choice = None

    elif user_game_choice == 'exit':
        break
