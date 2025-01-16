from random import randint

while True:
    print("\n(1) = Rock...")
    print("(2) = Paper...")
    print("(3) = Scissors...")

    player = int(input("\nplayer Choose: "))
    computer = randint(1,3)
    print(f"computer choose: {computer}")

    if(player and computer):

        if player == 1 and computer == 2:
            print("\ncomputer Wins...")

        elif player == 1 and computer == 3:
            print("\nPlayer Wins...")

        elif player == 2 and computer == 1:
            print("\nPlayer Wins...")

        elif player == 2 and computer == 3:
            print("\ncomputer Wins...")
            
        elif player == 3 and computer == 1:
            print("\ncomputer Wins...")

        elif player == 3 and computer == 2:
            print("\nPlayer Wins...")

        elif player == computer:
            print("\nplayer = computer")
    
        else:
            print("\nSomething is not true...")
    else:
        print("wrong input...")