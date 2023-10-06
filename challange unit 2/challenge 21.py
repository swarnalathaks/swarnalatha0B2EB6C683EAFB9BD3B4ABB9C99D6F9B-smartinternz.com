class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive amount.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance}")

# Testing the BankAccount class
if __name__ == "__main__":
    account = BankAccount("123456789", "John Doe", 1000)
    
    account.display_balance()  # Display initial balance
    
    account.deposit(500)  # Deposit $500
    account.withdraw(200)  # Withdraw $200
    account.withdraw(1500)  # Attempt to withdraw $1500 (insufficient funds)

    account.display_balance()  # Display final balance
