while True:
    print("\n(1) = Rock...")
    print("(2) = Paper...")
    print("(3) = scissors...")

    player_1 = input("\nplayer 1 Choose: ").lower()
    player_2 = input("\nplayer 2 Choose: ").lower()

    if(player_1 and player_2):

        if player_1 == "rock" and player_2 == "paper":
            print("\nPlayer 2 Wins...")

        elif player_1 == "rock" and player_2 == "scissors":
            print("\nPlayer 1 Wins...")

        elif player_1 == "paper" and player_2 == "rock":
            print("\nPlayer 1 Wins...")

        elif player_1 == "paper" and player_2 == "scissors":
            print("\nPlayer 2 Wins...")
            
        elif player_1 == "scissors" and player_2 == "rock":
            print("\nPlayer 2 Wins...")

        elif player_1 == "scissors" and player_2 == "paper":
            print("\nPlayer 1 Wins...")

        elif player_1 == player_2:
            print("\nplayer 1 = player 2")
    
        else:
            print("\nSomething is not true...")
    else:
        print("wrong input...")