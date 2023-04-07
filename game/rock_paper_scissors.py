# The while True loop never continues until it's told to stop 

def play_rock_paper_scissors_game():
  player1_score = 0
  player2_score = 0
  num_draws = 0
  round = 0

  print("\nWelcome, let's play rock paper scissors!")
  while True:
    player1_input = input("\nPlayer 1, to play rock paper scissors enter one of r, p or s: ")
    player2_input = input("\nPlayer 2, to play rock paper scissors enter one of r, p or s: ")

    player1 = player1_input.lower()
    player2 = player2_input.lower()


    if(player1 == 'r'):
      print("\nPlayer 1 is rock")
    if(player1 == 's'):
      print("\nPlayer 1 is scissor")
    if(player1 == 'p'):
      print("\nPlayer 1 is paper")

    print("--------------------------")

    if(player2 == 'r'):
      print("Player 2 is rock")
    if(player2 == 's'):
      print("Player 2 is scissor")
    if(player2 == 'p'):
      print("Player 2 is paper")

    print("--------------------------")

    if(player1 == 's' and player2 == 'p'):
      print("Player 1 won and Player 2 lost.")
      player1_score += 1
    elif(player1 == 'p' and player2 == 's'):
      print("Player 2 won and Player 1 lost.")
      player2_score += 1
    elif(player1 == 'r' and player2 == 's'):
      print("Player 1 won and Player 2 lost.")
      player1_score += 1
    elif(player1 == 's' and player2 == 'r'):
      print("Player 2 won and Player 1 lost.")
      player2_score += 1
    elif(player1 == 'p' and player2 == 'r'):
      print("Player 1 won and Player 2 lost.")
      player1_score += 1
    elif(player1 == 'r' and player2 == 'p'):
      print("Player 2 won and Player 1 lost.")
      player2_score += 1
    else:
      print("It is a draw.");
      num_draws += 1
    print("\nPlayer 1 score:", player1_score)
    print("\nPlayer 2 score:", player2_score)
    print("\nThe number of draws are:", num_draws)

  # After each turn ask user if they'd like to continue to play or not 
    exit_loop = input("\nDo you want to continue playing the game? Answer yes or no: ")
    if exit_loop.lower() == "no":
       
       try:
        lines = ['Player 1 total score: ', str(player1_score), 'Player 2 total score: ', str(player2_score)]
        with open("rps_game_results.txt", 'w') as rps_file:
          for line in lines: 
            rps_file.write(line)
            rps_file.write('\n')

       except FileNotFoundError:
        print("File not Found")     
    
       break

  print("\nHope you enjoyed the game. See you next time!")



