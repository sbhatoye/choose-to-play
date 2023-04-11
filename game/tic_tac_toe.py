"""   **************             This is the code for the Tic Tac Toe game.            ************    """
"""   *********************************************************************************************    """


BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}


game_round = 0

def render(BOARD):
    '''
    Returns a string describing the board in its
    current state. It should look something like this:

     1 | 2 | 3
     - + - + -
     4 | 5 | 6
     - + - + -
     7 | 8 | 9

    Returns
    -------
    board_state : str

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

    print(BOARD[1] + '|' + BOARD[2] + '|' + BOARD[3])
    print('-+-+-')
    print(BOARD[4] + '|' + BOARD[5] + '|' + BOARD[6])
    print('-+-+-')
    print(BOARD[7] + '|' + BOARD[8] + '|' + BOARD[9])


def get_action(current_player):
    '''
    Prompts the current player for a number between 1 and 9.
    Checks* the returning input to ensure that it is an integer
    between 1 and 9 AND that the chosen board space is empty.

    Parameters
    ----------
    player : str

    Returns
    -------
    action : int

    Raises
    ======
    ValueError, TypeError

    Implements (See also)
    ---------------------
    BOARD : dict


    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

    player_move = int(input(f"\nPlayer {current_player}, please enter a number between 1 and 9 to place your marker in the desired position: "))
        
    if player_move >= 1 and player_move <=9 and BOARD[player_move] == ' ':
        BOARD[player_move] = current_player

    else:
        print("\nSorry this place is already filled. Please make another selection.")
  

def check_win(current_player):
    '''
    Checks victory conditions. If found, calls victory_message().
    This can be done with one long chain of if/elif statements, but
    it can also be condensed into a single if/else statement, among
    other strategies (pattern matching if you have python 3.10 or above).

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    True or False : bool

    Implements (See also)
    ---------------------
    BOARD : dict
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

        # Check horizontal conditions
    if BOARD[1] == BOARD[2] == BOARD[3] and BOARD[1] != " " :
        render(BOARD)
        # put this in victory message
        print(f"\nCongrats player {BOARD[1]}! You won this round of tic tac toe!")
        return True

    elif BOARD[4] == BOARD[5] == BOARD[6] and BOARD[4] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[4]}! You won this round of tic tac toe!")
        return True
    
    elif BOARD[7] == BOARD[8] == BOARD[9] and BOARD[7] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[7]}! You won this round of tic tac toe!")
        return True

    # Check vertical conditions

    elif BOARD[1] == BOARD[4] == BOARD[7] and BOARD[1] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[1]}! You won this round of tic tac toe!")
        return True
    
    elif BOARD[2] == BOARD[5] == BOARD[8] and BOARD[2] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[2]}! You won this round of tic tac toe!")
        return True
    
    elif BOARD[3] == BOARD[6] == BOARD[9] and BOARD[3] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[3]}! You won this round of tic tac toe!")
        return True

    # Check diagonal conditions 

    elif BOARD[1] == BOARD[5] == BOARD[9] and BOARD[1] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[1]}! You won this round of tic tac toe!")
        return True
        
    elif BOARD[3] == BOARD[5] == BOARD[7] and BOARD[3] != " " :
        render(BOARD)
        print(f"\nCongrats player {BOARD[3]}! You won this round of tic tac toe!")
        return True


def play_tic_tac_toe_game():
    '''
    This is the main game loop that is called from the launcher (main.py)

    Implements (See also)
    ---------------------
    BOARD : dict
    render() : func
    get_action(player) : func
    check_win(player) : func
    play_tic_tac_toe()* : func

    *Note: this function refers to itself. Be careful about
    inescapable infinite loops.
    '''

    current_player = "X"
    game_over = False
    game_round = 0


    while game_over == False:

        # Print the current state of the board
        render(BOARD)

        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(current_player)
       
        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.
        BOARD[action] = current_player

        # Increment the game round by 1.
        game_round += 1

        # Check if the game is winnable (game_round >= 5),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).
        
        if game_round >= 5:       
            if check_win(current_player) == True:
                game_over = True
                break


        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.
        
        if game_round == 9:
                render(BOARD)
                print("\nIt looks a like a tie! Nobody wins this round of tic tac toe.")
                game_over = True
                break


        # switch players with a quick conditional loop.
        if current_player == 'X': current_player = 'O'
        else: current_player = 'X'

    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
            
        # and reinitiate the game loop (play_t3()).

    play_again = input("\nDo you want to play another round? Answer 'yes' or 'no': ")
    if play_again.lower() == 'yes':
        for action in BOARD:
            BOARD[action] = " "
        play_tic_tac_toe_game()
    else:
        print("\nHope you enjoyed the game. See you next time!")
