def play_slot_machine():
    import random
    import sys
    import time

    while True:
        try:
            balance = int(input("Enter your starting balance: "))
            if balance <=0:
                print("Balance cannot be less than $1!")
            else:
                break
        except ValueError:
            print("Pick an integer value!")

    print(f'''
\nWelcome to the Slot Machine Game!
You start with a balance of ${balance}.''')

    mid_payout = ["💎","⭐"]
    slot_choices = ["🍒","🍋","🍊","🍇","🔔","💎","⭐"] #<to test payouts, put the emojis not in payout here>
    def slot():
        return random.choice(slot_choices)

    while True:
        print(f"\nCurrent Balance: {balance}")
        try:
            bet = int(input("Enter your bet amount: "))
            if bet <=0:
                print("You cannot bet less than $1!")
                continue
            elif bet > balance:
                print(f"You cannot bet more than ${balance}!")
                continue
        except ValueError:
            print("Pick an integer value!")
            continue
        slot1 = slot()
        slot2 = slot()
        slot3 = slot()
        slot4 = slot()
        slot5 = slot()
        slot6 = slot()
        slot7 = slot()
        slot8 = slot()
        slot9 = slot()
        slot10 = slot()
        slot11 = slot()
        slot12 = slot()
        print(f"{slot4}  |     |       ")
        time.sleep(0.5)
        sys.stdout.write("\033[A")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the line
        print(f"{slot5}  | {slot6}  |        ")
        time.sleep(0.5)
        sys.stdout.write("\033[A")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the line    
        print(f"{slot7}  | {slot8}  | {slot9}")
        time.sleep(0.5)
        sys.stdout.write("\033[A")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the line
        print(f"{slot10}  | {slot11}  | {slot12}")
        time.sleep(0.5)
        sys.stdout.write("\033[A")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the line
        print(f"{slot1}  | {slot2}  | {slot3}")
        time.sleep(0.5)
        if slot1 == slot2 == slot3 == "💎":
            print(f"JACKPOT! You won ${bet*30}!\n")
            balance += bet*29
            bet = 0
        elif slot1 == slot2 == slot3:
            print(f"Match 3! You won ${bet*10}!")
            balance += bet*9
            bet = 0
        elif (slot1 == slot2 and slot1 in mid_payout) or (slot2 == slot3 and slot2 in mid_payout) or (slot1 == slot3 and slot3 in mid_payout):
            print(f"Bonus Match 2! You won ${bet*5}!")
            balance += bet*4
            bet = 0
        elif slot1 == slot2 or slot2 == slot3 or slot3 == slot1:
            print(f"Match 2! You won ${bet*2}!")
            balance += bet*1
            bet = 0
        else:
            print(f"You lost ${bet}!")
            balance -= bet
            bet = 0
            if balance == 0:
                print("You have run out of balance. Thanks for playing!")
                break
        while True:
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again == "y":
                break
            elif play_again == "n":
                print(f"\nYou walk out with ${balance}. Thanks for playing!")
                return
            else:
                print("Choose between (y/n)!")

        
