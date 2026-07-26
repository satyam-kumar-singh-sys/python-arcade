def play_number_guesser():
    import random

    best_score = None

    while True:
        #Asking for min value loop
        while True:
            try:
                min_value = int(input("Enter the min value: "))
                break
            except:
                print("Enter a valid integer value!")

        #Asking for max value loop
        while True:
            try:
                max_value = int(input("Enter the max value: "))
                if max_value < min_value:
                    print(f"Max value cannot be lesser than {min_value}.")
                    continue
                else:
                    break
            except:
                print("Enter a valid integer value!")

        secret_number = random.randint(min_value,max_value)
        guess_count = 0
        won = False

        #Max number of guesses loop
        while True:
            try:
                max_guess_count = int(input("Enter the no. of guesses you want: "))
                break
            except:
                print("Enter a valid integer value!")

        #Guessing loop
        while guess_count<max_guess_count:
            try:
                guess = int(input(f"Guess the number (between {min_value} and {max_value}): "))
                if guess < min_value or guess > max_value:
                    print(f"Guess between {min_value} and {max_value} please!")
                elif guess < secret_number:
                    guess_count += 1
                    print("Too low! Try again.")
                elif guess > secret_number:
                    guess_count += 1
                    print("Too high! Try again.")
                elif guess == secret_number:
                    guess_count += 1
                    print(f"Congratulations! You guessed the number in {guess_count} attempts.")
                    won = True
                    break
            except:
                print("Enter a valid integer value!")
        else:
            print(f"You couldn't guess the number. The number was {secret_number}.")
            won = False

        #Updating best score only on wins
        if best_score == None and won == True:
            best_score = guess_count
        elif best_score != None and won == True:
            if best_score > guess_count:
                best_score = guess_count

        #The play-again loop
        while True:
            play_again = input("Want to play again? (y/n): ")
            if play_again.lower() == "y":
                break
            elif play_again.lower() == "n":
                if best_score != None:
                    print(f"Thanks for playing! Your best score was {best_score} guesses.")
                else: 
                    print("Thanks for playing!")
                return
            else:
                print("Enter a valid input.")
