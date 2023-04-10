BOARD = {1: ' ',  2: ' ',  3: ' ',

        4: ' ',  5: ' ',  6: ' ',

        7: ' ',  8: ' ',  9: ' '}

current_player = 'X'
game_round = 0
game_over = False


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

    *Note: Implementing a while loop in this function is recommended,
    but make sure you aren't coding any infinite loops.
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

    player_move = int(input("\nPlease enter a number between 1 and 9 to place your marker in the desired position: "))
        
    if player_move >= 1 and player_move <=9 and BOARD[player_move] == ' ':
        BOARD[player_move] = current_player
    else:
        print("Sorry this place is already filled. Please make another selection.")
  


def victory_message(current_player):
    '''
    Prints the updated board and returns a victory message for the
    winning player.

    Parameters
    ----------
    player : 'X' / 'O'

    Returns
    -------
    victory_message : str

    Implements (See also)
    ---------------------
    print_t3() : func
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

def check_win(player):
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
    victory_message(player) : func
    '''
    # ----------------
    # INSERT CODE HERE
    # ----------------

    



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


    while not game_over:

       # game_over = True # Delete this line when you're ready to run the loop.

        # Print the current state of the board
        render(BOARD)

        # Get the current player's action and assign it to a variable called 'action'.
        action = get_action(current_player)
       
        # Assign the current player ('X' or 'O') as a value to BOARD. Use the 'action' variable as the key.

        # Increment the game round by 1.

        # Check if the game is winnable (game_round >= 4),
            # then check for win conditions (check_win(player)),
                # and if there's a win, end the game (game_over = True),
                # and break the loop (break).

        # Check if there are any open spots left (game_round == 9),
            # and if there aren't, print a tie message,
            # end the game,
            # and break the loop.

        # switch players with a quick conditional loop.

      #  if player == 'X': player = 'O'
      #  else: player = 'X'

    # prompt for a restart and assign the input to a 'restart' variable.
    # if yes,
        # clear each key in the board with a for loop
            
        # and reinitiate the game loop (play_t3()).

play_tic_tac_toe_game()