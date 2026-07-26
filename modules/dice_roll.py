def play_dice_roll():
    import random

    #function for the dice roll
    def roll_dice(number_of_dice):
        return[random.randint(1,6) for i in range(number_of_dice)] #using () instead of [] here would return a generator object
    #i is just a placeholder variable


    #set the count and number of dice to zero
    count = 0
    number_of_dice = 0

    while True:
        roll = input("Roll the dice? (y/n): ")
        if roll.lower() == "y":
            try:
                number_of_dice = int(input("Enter the number of dice you want to roll: "))
                if number_of_dice <1:
                    print("Enter a valid number.")
                else:
                    current_roll = roll_dice(number_of_dice)
                    count +=1
                    print(f"You rolled {current_roll} and the current count is {count}.")
            except ValueError:
                print("Enter a valid number.")
        elif roll.lower() == "n":
            print(f"The current count is {count}. Thanks for playing!")
            break
        else:
            print("Invalid input!")
            