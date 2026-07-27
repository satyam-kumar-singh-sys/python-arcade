def start_atm_old():
    import getpass

    user_pin = 1234
    balance = 0
    transactions = []

    while True:
        try:
            print("Welcome to the ATM!")
            pin_input = int(getpass.getpass('''
Enter your PIN please (or press 0 to quit): '''))
            if pin_input == user_pin:
                print('''
Welcome to the ATM, Mr Satyam!
1. Check Balance
2. Deposit 
3. Withdraw
4. Check Past Transactions
5. Exit''')

                choices = [1,2,3,4,5]
                while True:
                    try:
                        choice = int(input("\nPlease choose an option: "))
                        if choice not in choices:
                            print("Please choose between (1/2/3/4/5).")
                        else:
                            if choice == 1:
                                print(f"Your current balance is ${balance}")
                            elif choice == 2:
                                try:
                                    deposit = float(input("Enter the amount to deposit: "))
                                    if deposit <=0:
                                        print("Deposit should be greater than 0!")
                                    else:
                                        print(f"Successfully deposited ${deposit:.2f}.")
                                        balance += deposit
                                        transactions.append(f"• deposit = ${deposit:.2f}  \t Current Balance: ${balance:.2f}")
                                except:
                                    print("Deposit should be a number!")
                            elif choice == 3:
                                try:
                                    withdraw = float(input("Enter the amount to withdraw: "))
                                    if withdraw <=0:
                                        print("Withdrawal should be greater than 0!")
                                    elif withdraw > balance:
                                        print(f"Can't withdraw more than {balance}!")
                                    else:
                                        print(f"Successfully withdrew ${withdraw:.2f}.")
                                        balance -= withdraw
                                        transactions.append(f"• withdrawal = ${withdraw:.2f}\t Current Balance: ${balance:.2f}")
                                except:
                                    print("Withdrawal should be a number!")   
                            elif choice == 4:
                                if not transactions:
                                    print("No transactions yet.")
                                else:
                                    for transaction in transactions:
                                        print(transaction)
                            elif choice == 5:
                                print("Thank you for using the ATM!")
                                break
                            #here if I had used exit(), or imported sys and then used sys.exit(), those would get caught by the bare except
                            #and would end up in an infinite loop or back on the "Please choose an option" menu. to avoid that, I have used 
                            #"break" here, which would return back to the "enter your pin" menu. I could've also used "except ValueError" 
                            #instead of the bare excepts and then used exit() here, which would quit the program at this step itself.
                    except:
                        print("Please choose between (1/2/3/4/5).")
            elif pin_input == 0:
                print("Thank you for using the ATM!")
                break
            else:
                print("Wrong PIN! Please try again.")
        except:
            print("Please enter a valid PIN!")

