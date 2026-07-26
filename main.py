import modules.atm_sim as atm_sim
import modules.currency_convertor as currency_convertor
import modules.qrcode_gen as qrcode_gen
import modules.text_editor as text_editor
import modules.to_do_app as to_do_app
import modules.dice_roll as dice_roll
import modules.word_guessing as word_guessing
import modules.number_guessing as number_guessing
import modules.pig_dice as pig_dice
import modules.slot_machine as slot_machine
import time

def menu_help():
    print('''
==========================
Welcome to Python Arcade!
==========================
1. ATM Simulator
2. Currency Convertor
3. QR Code Generator
4. Text Editor
5. To Do App
6. Dice Roll
7. Word Guessing
8. Number Guessing
9. Pig Dice
10.Slot Machine
11.Exit
==========================
''')

def menu():
    while True:
        menu_help()
        time.sleep(0.5)
        user_input = input("\nPick an option: ")

            #try-except to catch an accidental system-exit can prevent the file exiting to cmd main menu, but the program would still
            #give a traceback because the system exit closes the standard input output system (sys.stdin), which is required in menu().
            #Could've reopened sys.stdin using the cmd below but this looks cleaner for main.py (but I had to manually remove exit() 
            #from multiple files, so if the file count was too high, reopening sys.stdin is more viable.)
       #if user_input == "1":            
            # try:
            #     atm_sim.start_atm()
            # except SystemExit:
            #     print("Returning to main menu...")
            #Re-open sys.stdin so input() works again!
            #     sys.stdin = open(0)

        if user_input == "1":
            atm_sim.start_atm()

        elif user_input == "2":
            currency_convertor.start_currency_convertor()

        elif user_input == "3":
            qrcode_gen.use_qrcode_gen()

        elif user_input == "4":
            text_editor.use_text_editor()

        elif user_input == "5":
            to_do_app.use_to_do_app()

        elif user_input == "6":
            dice_roll.play_dice_roll()

        elif user_input == "7":
            word_guessing.play_word_guesser()

        elif user_input == "8":
            number_guessing.play_number_guesser()

        elif user_input == "9":
            pig_dice.play_pig_dice()

        elif user_input == "10":
            slot_machine.play_slot_machine()

        elif user_input == "11":
            print("Thanks for using Python Arcade!")
            exit()
        else:
            print("Pick between the options given!")

if __name__ == "__main__":
    menu()