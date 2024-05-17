class Checkbook:
    """
    A simple class representing a checkbook to manage deposits, withdrawals, and balance checking.
    """

    def __init__(self):
        """
        Initializes a new Checkbook object with a balance of 0.0.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits funds into the checkbook.

        Args:
            amount (float): The amount to deposit.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Deposit amount must be a positive number.")
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self, amount):
        """
        Withdraws funds from the checkbook.

        Args:
            amount (float): The amount to withdraw.
        """
        try:
            amount = float(amount)
            if amount <= 0:
                raise ValueError("Withdrawal amount must be a positive number.")
            if amount > self.balance:
                raise ValueError("Insufficient funds to complete the withdrawal.")
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))
        except ValueError as e:
            print("Error:", str(e))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook object.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = input("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = input("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

