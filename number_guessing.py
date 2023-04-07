# import random module
import random
def play_number_guessing_game():
    # counter variable 
    num_chances = 3
    print("\nWelcome, let's play the number guessing game!")
    
    # Computer selects a random number within a range
    # returns a random in the inclusive range 
    random_num = random.randint(0,10)
    print (random_num) 

    
    while num_chances > 0:
        print(random_num)
        player_guess = int(input("""\nThe computer has chosen a random number between 0 and 10.
                                \nWhat could the number be? Make a guess! """))
        if(player_guess == random_num): 
            print("\nGood job, you guessed it!")
            play_again = input("Would you like to play again? Enter Y/N: ")
            if(play_again.capitalize() == 'Y' or play_again.casefold() )
            break
        else: print("\nAww shucks, that's the wrong guess. Try again!")
        num_chances -= 1
    else: print("\nSorry, you've run out of chances to guess! Better luck next time!")
    
    
play_number_guessing_game()


#\nNumber of remaining chances to guess correctly: {chances} 
#\nWhat could the number be? Make a guess! """.format(chances=num_chances))



