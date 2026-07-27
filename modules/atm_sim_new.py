import getpass


class Bank:
    def __init__(self):
        self.accounts = {} #dictionary of accounts with username mapped to details

    def create_account(self, username, pin, balance = 0):
        if username in self.accounts:
            print("An account with this username already exists!")
            return None
        account = Account(username, pin, balance)
        self.accounts[username] = account
        print(f"Account created for {username}.")
        return account

    def login(self, username, pin):
        account = self.accounts.get(username)
        if account == None:
            print("Incorrect username or PIN!")
            return None
        if account.pin != pin:
            print("Incorrect username or PIN!")
            return None
        return account

    def find_account(self, username):
        return self.accounts.get(username)
        
class Account:
    def __init__(self, username, pin, balance= 0):
        self.username = username
        self.pin = pin
        self.balance = balance
        self.transactions_history = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0!")
            return False
        self.balance += amount
        self.transactions_history.append(f"• Deposit:    {amount:.2f}  \t Current Balance: {self.balance:.2f}")
        print(f"Successfully deposited ${amount:.2f} in account.\n")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0!")
            return False
        if amount > self.balance:
            print(f"Cannot withdraw more than ${self.balance:.2f}!")
            return False
        self.balance -= amount
        self.transactions_history.append(f"• Withdrawal: {amount:.2f}\t Current Balance: {self.balance:.2f}")
        print(f"Successfully withdrew ${amount:.2f} from account.\n")

    def check_balance(self):
        print(f"\nCurrent balance: ${self.balance:.2f}\n")

    def transactions(self):
        if not self.transactions_history:
            print("No transactions yet.")
            return
        for transaction in self.transactions_history:
            print(transaction)

    def transfer_money(self, account, receiver_account, amount):
        self.balance -= amount
        self.transactions_history.append(f"• Transfer:   {amount:.2f}\t Current Balance: {self.balance:.2f}")
        receiver_account.balance += amount
        receiver_account.transactions_history.append(f"• Received:   {amount:.2f}\t Current Balance: {receiver_account.balance:.2f}")
        print(f"${amount:.2f} has been transferred to {receiver_account.username}!")

def start_atm_sim_new():
    bank = Bank() #fresh bank every time the module is run
    def bank_menu():
        while True:
            print('''
==========================
Welcome to the ATM!
1. Log In
2. Create New Account
3. Exit
==========================''')
            main_menu_option = input("Please pick an option: ")
            if main_menu_option == "1":
                username = input("Please enter your username: ").lower()
                pin = getpass.getpass("Please enter your pin: ")
                account =bank.login(username, pin)
                if account:
                    current_account_menu(account)
            elif main_menu_option == "2":
                new_username = input("Please enter your username: ").strip().lower()
                if not new_username:
                    print("Username cannot be empty!")
                    continue
                new_pin = getpass.getpass("Please enter your PIN: ").strip()
                if not new_pin:
                    print("PIN cannot be empty!")
                    continue
                bank.create_account(new_username, new_pin, balance = 0 )
            elif main_menu_option == "3":
                print("Thank you for using the ATM!")
                break

    def current_account_menu(account):
        print(f'''
=========================================
Welcome, Mr. {account.username}!
_________________________________________
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money to Another Account
5. Check Transaction History
6. Exit
=========================================''')
        while True:
            user_input = input("Please pick an option (or press 0 for menu): ")
            if user_input == "1":
                account.check_balance()
            elif user_input == "2":
                try:
                    amount = float(input("\nEnter the amount you want to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Enter a valid amount!")
            elif user_input == "3":
                try:
                    amount = float(input("\nEnter the amount you want to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Enter a valid amount!")
            elif user_input == "4":
                pass
                receiver_username = input("Enter the username of the account you want to transfer to: ")
                receiver_account = bank.find_account(receiver_username)
                if receiver_account == None:
                    print("User not found!")
                elif receiver_account is account:
                    print("You can't transfer to your own account!")
                else:
                    try:
                        money = float(input("Enter the amount of money you want to transfer: "))
                        if money > account.balance:
                            print(f"You can only transfer ${account.balance:.2f}!")
                        elif money <=0:
                            print(f"The minimum amount you can transfer is $0.01!")
                        else:
                            account.transfer_money(account, receiver_account, money)
                    except ValueError: 
                        print("Enter a valid amount!")
                
            elif user_input == "5":
                account.transactions()
            elif user_input == "6":
                print("Thank you for using the ATM!")
                break
            elif user_input == "0":
                print(f'''
_____________________________________
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money to Another Account
5. Check Transaction History
6. Exit
_____________________________________''')
            else:
                print("Please pick from one of the given options!")
                continue

    bank_menu()

if __name__ == "__main__":
    bank = Bank() #need to create Bank instance to be able to call methods on the class Bank
    start_atm_sim_new()
