def play_rps():
    import random
    import time
    import getpass #to hide one player's choices from the other

    total_player_wins = 0
    total_player_losses = 0
    total_player_ties = 0

    total_player1_wins = 0
    total_player1_ties = 0
    total_player1_losses = 0

    total_player2_wins = 0
    total_player2_ties = 0
    total_player2_losses = 0

    while True:
        pvp_or_pvc = input("Type p for pvp, c for pvc: ")
        if pvp_or_pvc == "p":
            while True:
                player1_wins = 0
                player2_wins = 0
                rps = ["r", "p", "s"]

                while player1_wins<2 and player2_wins <2:
                    #player 1 chooses
                    while True:
                        choice1 = getpass.getpass("Player 1 - Rock, paper or scissors? (r/p/s): ")
                        if choice1 in ["r","p","s"]:
                            break
                        else:
                            print("Choose again!")

                    #player 2 chooses
                    while True:    
                        choice2 = getpass.getpass("Player 2 - Rock, paper or scissors? (r/p/s): ")
                        if choice2 in ["r","p","s"]:
                            break
                        else:
                            print("Choose again!")

                    #using dictionary for printing choices
                    choices = {"r":"🪨","p":"📃" ,"s":"✂️" }
                    time.sleep(1)
                    print(f"Player 1 chose {choices[choice1]}")
                    time.sleep(1)
                    print(f"Player 2 chose {choices[choice2]}")

                    #printing who won the round
                    time.sleep(1)
                    winning_pairs = {"r":"s","s":"p","p":"r"}
                    if choice1 == choice2:
                        print("It's a tie!")
                        total_player1_ties += 1
                        total_player2_ties += 1
                    elif winning_pairs[choice1] == choice2:
                        print("Player 1 won!")
                        player1_wins += 1
                        total_player1_wins += 1
                        total_player2_losses += 1
                    else:
                        print("Player 2 won!")
                        player2_wins +=1
                        total_player1_losses += 1
                        total_player2_wins +=1

                #best 2 out of 3 rounds 
                if player1_wins == 2:
                    print("Player 1 won the game!")
                else:
                    print("Player 2 won the game!")

                #continue game or print total scores
                while True:
                    play_again = input("Continue? (y/n): ").lower()
                    if play_again == "y":
                        break
                    elif play_again == "n":
                        print(f'''
____________________________________
Player 1
____________________________________
Total wins:   {total_player1_wins}
Total losses: {total_player1_losses}
Total ties:   {total_player1_ties}
____________________________________
Player 2
____________________________________
Total wins:   {total_player2_wins}
Total losses: {total_player2_losses}
Total ties:   {total_player2_ties}
____________________________________''')
                        return
                    else:
                        print("Enter a valid input! (y/n)")

        elif pvp_or_pvc == "c":
            while True:
                player_wins = 0
                python_wins = 0
                rps = ["r", "p", "s"]

                #python and player choose
                while player_wins<2 and python_wins <2:
                    while True:
                        python_choice = random.choice(rps)
                        choice = input("Rock, paper or scissors? (r/p/s): ")
                        if choice in ["r","p","s"]:
                            break
                        else:
                            print("Choose again!")

                    #using dictionary for printing choices
                    choices = {"r":"🪨","p":"📃" ,"s":"✂️" }
                    time.sleep(1)
                    print(f"You chose {choices[choice]}")
                    time.sleep(1)
                    print(f"Computer chose {choices[python_choice]}")

                    time.sleep(1)
                    winning_pairs = {"r":"s","s":"p","p":"r"}
                    if choice == python_choice:
                        print("It's a tie!")
                        total_player_ties += 1
                    elif winning_pairs[choice] == python_choice:
                        print("You won!")
                        player_wins += 1
                        total_player_wins += 1
                    else:
                        print("You lost!")
                        python_wins +=1
                        total_player_losses += 1
                if player_wins == 2:
                    print("You won the game!")
                else:
                    print("Computer won the game!")

                while True:
                    play_again = input("Continue? (y/n): ").lower()
                    if play_again == "y":
                        break
                    elif play_again == "n":
                        print(f'''
___________________________________
Total wins:   {total_player_wins}
Total losses: {total_player_losses}
Total ties:   {total_player_ties}
___________________________________''')
                        return
                    else:
                        print("Enter a valid input! (y/n)")

        else:
            print("Type p or c!")
