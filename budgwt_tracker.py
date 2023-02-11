class BudgetTracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: ${amount}")

    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: ${amount}")
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def show_transactions(self):
        for transaction in self.transactions:
            print(transaction)


def main():
    budget_tracker = BudgetTracker()
    while True:
        user_input = input(
            "Enter 'd' to deposit, 'w' to withdraw, 'b' to check balance, 't' to view transactions, or 'q' to quit: ")
        if user_input == 'd':
            deposit_amount = int(input("Enter amount to deposit: $"))
            budget_tracker.deposit(deposit_amount)
        elif user_input == 'w':
            withdraw_amount = int(input("Enter amount to withdraw: $"))
            budget_tracker.withdraw(withdraw_amount)
        elif user_input == 'b':
            print(f"Balance: ${budget_tracker.get_balance()}")
        elif user_input == 't':
            budget_tracker.show_transactions()
        elif user_input == 'q':
            break
        else:
            print("Invalid input. Try again.")


if __name__ == '__main__':
    main()


#md rohanur rahman ontu