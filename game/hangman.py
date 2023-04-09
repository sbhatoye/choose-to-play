import random 

"""   **************             This is the code for the Hangman game.            *************    """
"""   ******************************************************************************************    """


def generate_random_word():

    """ This function generates a random word which the user attempts to guess """
   
    words = """avenue,awkward,abyss,bagpipes,bandwagon,banjo,blizzard,boggle,bookworm,boxcar,
    cobweb,cycle,dizzying,duplex,dwarves,espionage,faking,fishhook,fixable,flapjack,fuchsia,funny,
    galaxy,gossip,haiku,haphazard,hyphen,icebox,injury,ivory,jackpot,jaundice,jinx,jiujitsu,jockey,
    jogging,jukebox,keyhole,khaki,kilobyte,kiwifruit ,knapsack,larynx,luxury,microwave,mnemonic,mystify,
    nightclub,oxygen,pajama,peekaboo,quartz,queue,rhubarb,rhythm,snazzy,sphinx,subway,transcript,twelfth,
    unknown,vaporize,walkway,waltz,wristwatch,xylophone,yachtsman,zigzag,zodiac,zombie""".split(",")

    index_of_word = random.randint(0, len(words) -1)
    return words[index_of_word]


def welcome():

    """ This function prints out a greeting for the user and explains the rules of the game """

    # Print out greeting 
    user_name = input("\nWelcome to the Hangman game! Please enter your preferred game name: ")

    # Explain the rules of the game
    print(f"""\nHi {user_name}!
              \nYou are going to be playing against the computer.
              \nThe computer is going to randomly choose a secret word and you have to guess what the word is.
              \nLet's play!""")

def play_again():

    """ This function asks the user if they want to play the hangman game again """

    another_round = input("\nDo you want to play another round? Answer 'yes' or 'no': ")
    if another_round.lower() == 'yes':
        play_hangman_game()
    else:
        print("\nHope you enjoyed the game. See you next time!")


def find_index(mystery_word, guess):

    """ This function finds all the indices of the letter guessed by the player in the secret word"""

    return [i for i, letter in enumerate(mystery_word) if letter == guess]


def play_hangman_game():
    
    """ This function runs the game for the player to play """

    display_hangman = ['''
    +---+
        |
        |
        |
        ===''', '''
    +---+
    O   |
        |
        |
        ===''', '''
    +---+
    O   |
    |   |
        |
        ===''', '''
    +---+
    O   |
   /|   |
        |
        ===''', '''
    +---+
    O   |
   /|\  |
        |
        ===''', '''
    +---+
    O   |
   /|\  |
   /    |
        ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
        ===''']

    hangman_counter = 0

    # Call the welcome function to greet player
    welcome()

    # Call generate_random_word function for the computer to choose a secret word from the provided list
    secret_word = generate_random_word()

    # Let the user know what the length of the secret word is
    secret_word_length = len(secret_word)
    print(f"\nThe computer has chosen a random word and it is {secret_word_length} letters long.")

    # The empty list letters_guessed will store the letters guessed by the player 
    letters_guessed = []

    # The number_of_tries variable initiates the number of tries the player has to win
    number_of_tries = 7

    # This prints out a dash representing each letter in the secret word 
    letters = "_" * len(secret_word)
    position_of_letters = list(letters)
    print (position_of_letters)

    # Each iteration of the while loop represents a chance for the player to guess a letter or word
    while number_of_tries > 0:
        
        # This is a quick checkpoint to check if the last letter guessed by the player yielded the secret word
        if position_of_letters == list(secret_word):
            print(f"\nCongrats! You've correctly guessed the secret word '{secret_word}'. You win this round of Hangman!")
            play_again()
            break
       
        # Print letters guessed and number of tries remaining
        print(f"""\nLetters guessed: {letters_guessed}
                  \nYou have {number_of_tries} tries remaining.""")
        
        # Prompt player to guess a letter
        player_guess = input("\nGuess a letter or the guess the word: ")

        # If the player guesses a letter, use length method to distinguish it from a guessed word 
        if len(player_guess) == 1:
            # Ensures only alphabetic letters are entered 
            if player_guess not in 'abcdefghijklmnopqrstuvwxyz':
                print("\nSorry wrong entry. Please enter a valid alphabetic letter.\n")
                print(position_of_letters)

            # Checks to see if letter has already been guessed before
            elif player_guess in letters_guessed:
                    print("\nSorry you have already guessed this letter before. Make another guess.\n")
                    print(position_of_letters)

            # If the player's guessed letter is present in the secret word        
            elif player_guess in secret_word: 
                    # Determines how many times the guessed letter appears in the secret word and prints out its... 
                    # ...position in the secret word
                    indices = find_index(secret_word, player_guess)
                    position_of_letters = list(letters)
                    for index in indices:
                        position_of_letters[index] = player_guess
                        letters = "".join(position_of_letters)
                        
                    # If the guess for the letter is valid, append the letter to the to letters_guessed list 
                    print("\nGood job! You've guessed the letter correctly!\n")
                    print(position_of_letters)
                    letters_guessed.append(player_guess)

            else: 
                print("\nSorry your guessed letter is not part the word. Try again!\n")
                print(position_of_letters)
                letters_guessed.append(player_guess)
                number_of_tries -= 1
                print(display_hangman[hangman_counter])
                hangman_counter += 1
                
               

        # If player guesses a word, the length of the guessed word must be equal the length of the secret word 
        elif len(player_guess) == len(secret_word):
            if player_guess == secret_word:
                print(f"\nCongrats! You've correctly guessed the secret word '{secret_word}'. You win this round of Hangman!")
                play_again()
                break
            else: 
                print("\nNice try but that's not the secret word. Try again!")
                number_of_tries -= 1
                print(display_hangman[hangman_counter])
                print(position_of_letters)
                hangman_counter += 1
        
        # If player makes a guess that contains more than one letter and is not equivalent to length of secret word        
        else:
            print("\nCheck your entry again. Please enter a valid letter or word.")
 
    
    # The else part of the while-else loop will print when if player runs out of tries
    else:
        print(f"\nSorry you've run out of all tries in this round of Hangman.The secret word was '{secret_word}'. Better luck next time!")
        # Call the play_again() function to ask if player wants to play another round or exit the game 
        play_again()




