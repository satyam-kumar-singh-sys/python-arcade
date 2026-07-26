def play_pig_dice():
    import random
    import time

    player1_score = 0
    player2_score = 0
    current_player = 1
    round_score = 0
    target_score = 0

    def roll_die():
        return random.randint(1,6)

    while True:
        try:
            target_score = int(input("Set the target score: "))
            if target_score <1:
                print("Target score can't be lesser than 1.")
            else:
                break
        except:
            print("Type an integer please!")

    while True:
        print(f"Player {current_player}'s turn")
        time.sleep(1)
        round_score = 0
        turn_over = False
        while not turn_over:
            roll = roll_die()
            if roll == 1:
                print("You rolled a 1")
                time.sleep(1)
                print("You scored 0 points this turn.")
                time.sleep(1)
                print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}\n")
                time.sleep(1)
                turn_over = True
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
            else:
                round_score += roll
                print(f"\nYou rolled a {roll}")
                time.sleep(1)
                while True:
                    roll_again = input("Roll again? (y/n): ").strip().lower()
                    if roll_again == "y":
                        break
                    if roll_again == "n":
                        print(f"You scored {round_score} points this turn.")
                        time.sleep(1)
                        if current_player == 1:
                            player1_score += round_score
                            print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}\n")
                            if player1_score >= target_score:
                                print("The game is over. Player 1 has won!")
                                return
                        elif current_player == 2:
                            player2_score += round_score
                            print(f"Current scores: Player 1: {player1_score}, Player 2: {player2_score}\n")
                            if player2_score >= target_score:
                                print("The game is over. Player 2 has won!")   
                                return                     
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1
                        turn_over = True
                        break
                    else:
                        print("Choose between (y/n).")

                    
