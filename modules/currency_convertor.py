def start_currency_convertor():
    currency = ["USD", "EUR", "CAD"]
    rates = {"USD": 1.0, "EUR": 0.92, "CAD": 1.35}
    history = []

    while True:
        while True:
            try:
                amount = float(input("Enter the amount: "))
                if amount <=0:
                    print("Enter a number above 0!")
                else:
                    break
            except:
                print("Enter a valid number!")

        while True:
            source_currency = input("Source Currency (USD/EUR/CAD): ").upper()
            if source_currency not in currency:
                print("Choose a currency from the following: USD, EUR, CAD ")
            else:
                break

        while True:
            target_currency = input("Target Currency (USD/EUR/CAD): ").upper()
            if target_currency not in currency:
                print("Choose a currency from the following: USD, EUR, CAD ")
            else:
                break

        converted_currency = amount*rates[target_currency]/rates[source_currency]

        print(f"{amount:.2f} {source_currency} is equal to {converted_currency:.2f} {target_currency}")

        history_entry = (f"{amount:.2f} {source_currency} -> {converted_currency:.2f} {target_currency}")
        history.append(history_entry)

        while True:
            play_again = input("Try again? (y/n): ")
            if play_again == "y":
                break
            elif play_again == "n":
                print("\n--- CONVERSION HISTORY ---")
                if not history:
                    print("No conversions recorded.")
                else:
                    for entry in history:
                        print(f"• {entry}")
                return
            else:
                print("Choose between y/n: ")