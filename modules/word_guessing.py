def play_word_guesser():
    import random 

    easy_words = [
        "APPLE", "BEACH", "BREAD", "BRUSH", "CHAIR", "CLOCK", "CLOUD", "DREAM",
        "DRIVE", "EARTH", "FLAME", "FLASH", "FRUIT", "GLASS", "HEART", "HOUSE",
        "JUICE", "KNIFE", "LIGHT", "LEMON", "MUSIC", "NIGHT", "OCEAN", "PAPER",
        "PLANT", "PLATE", "RIVER", "SHARK", "SMILE", "SMART", "SNAKE", "SPACE",
        "STORM", "TRAIN", "WATER", "WORLD", "BIRD", "BOAT", "BOOK", "CAMP",
        "DOOR", "FIRE", "FISH", "FROG", "GAME", "GIFT", "GOLD", "HILL",
        "KING", "LAKE", "MOON", "PARK", "RING", "STAR", "TREE"
    ]
    medium_words = [
        "BALCONY", "BASEBALL", "BLANKET", "BUILDING", "CABINET", "CALENDAR",
        "CAPTAIN", "CASTLE", "CERAMIC", "CHIMNEY", "COMPUTER", "DIAMOND",
        "DOLPHIN", "ELEPHANT", "FEATHER", "FOOTBALL", "GARDEN", "GIRAFFE",
        "HAMMER", "HOSPITAL", "INSECT", "JACKET", "JOURNEY", "KITCHEN",
        "LANTERN", "LIBRARY", "MONSTER", "MOUNTAIN", "OBJECT", "PACKAGE",
        "PAINTING", "PANTHER", "PENGUIN", "PLANET", "PLASTIC", "PYRAMID",
        "QUESTION", "RAINBOW", "SANDWICH", "SCULPTURE", "SHELTER", "STADIUM",
        "SUNSHINE", "SURPRISE", "TELESCOPE", "THEATER", "THUNDER", "TRAFFIC",
        "UMBRELLA", "VACATION", "VAMPIRE", "VILLAGE", "WHISTLE", "WINDOW"
    ]
    hard_words = [
        "ASTRONAUT", "ASTRONOMY", "BACKPACK", "BUTTERFLY", "CHOCOLATE",
        "CORNFIELD", "CROCODILE", "DANDELION", "DICTIONARY", "DINOSAUR",
        "DIRECTION", "FIREWORKS", "FIREFLIES", "FLAMINGO", "FRIENDSHIP",
        "HELICOPTER", "HEDGEHOG", "INVENTOR", "KANGAROO", "LIGHTNING",
        "LOCOMOTIVE", "MICROSCOPE", "ORCHESTRA", "PHOTOGRAPH", "PORCUPINE",
        "SATELLITE", "SCARECROW", "SPAGHETTI", "SUBMARINE", "SUNFLOWER",
        "TRAMPOLINE", "TORNADO", "VOLCANO", "WATERFALL", "WOODPECKER",
        "ARCHAEOLOGY", "ARCHITECTURE", "AUTHENTICITY", "BIODIVERSITY",
        "CATASTROPHE", "CELEBRATION", "CHAMPIONSHIP", "COMPASSION",
        "KALEIDOSCOPE", "LABYRINTH", "METAMORPHOSIS", "NEIGHBORHOOD",
        "PERSEVERANCE", "REVOLUTION", "TRANSPARENCY"
    ]

    games_won = 0
    games_lost = 0

    #Looping for play-again
    while True:
        #ask player for difficulty
        while True:
            difficulty = input("Set your difficulty- easy(e), medium(m) or hard(h): ").strip().lower()
            if difficulty == "e":
                easy_word = random.choice(easy_words)
                display_word = ["_"]*len(easy_word)
                word = easy_word
                break
            elif difficulty == "m":
                medium_word = random.choice(medium_words)
                display_word = ["_"]*len(medium_word)
                word = medium_word
                break
            elif difficulty == "h":
                hard_word = random.choice(hard_words)
                display_word = ["_"]*len(hard_word)
                word = hard_word
                break
            else:
                print("Choose between (e/m/h)!")

        guess_count = 0
        max_guess_count = 6
        guessed_letters = []
        win = False

        #main guessing loop
        while guess_count<max_guess_count and not win:
            print("".join(display_word)) #basically printing out the display_word list without commas in between
            #could use " ".join(display_word) to print the dashes with spaces in between

            input_letter = input("Enter a letter: ").strip().upper()

            #input validation check
            if len(input_letter) != 1 or not input_letter.isalpha():
                print("Guess a single valid letter please!")
            elif input_letter in guessed_letters:
                print("You have already guessed this letter!")
            else:
                #Letter matching
                #equated both medium_word and easy_word to a single "word" and shortened the code
                if input_letter in word:
                        print("Good guess\n")
                        guessed_letters.append(input_letter)
                        for index,letter in enumerate(word): #indexing the word
                            if letter == input_letter:
                                display_word[index] = input_letter #replacing the dash with letter
                else:
                    print("Wrong guess\n")
                    guess_count += 1
                    guessed_letters.append(input_letter) 
                    print(f"Guesses left: {max_guess_count-guess_count}")           
            
            #Win condition check
            if "_" not in display_word:
                print(f"You have guessed the word: {word}! You win!")
                games_won += 1
                win = True
            else:
                continue
        else:
            #ending game if guesses over
            if win == False:
                print(f"You have exhausted your guesses! The word was {word}, You lose!")
                games_lost += 1

        #play again loop
        while True:
            play_again = input("Play again? (y/n): ").strip().lower()
            if play_again == "y":
                break
            elif play_again == "n":
                print(f'''
_______________________
Player Stats
_______________________
Games played: {games_won+games_lost}
Games won:    {games_won}
Games lost:   {games_lost}
_______________________

Thanks for playing!''')
                return
                