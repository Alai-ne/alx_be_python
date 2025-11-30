import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100) 

    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "deposit" and len(sys.argv) == 3:
            amount = float(sys.argv[2])
            account.deposit(amount)
            account.display_balance()
        elif command == "withdraw" and len(sys.argv) == 3:
            amount = float(sys.argv[2])
            if account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Insufficient funds or invalid amount.")
            account.display_balance()
        elif command == "balance":
            account.display_balance()
        else:
            print("Invalid command or arguments.")
    else:
        print("Please provide a command (deposit, withdraw, balance).")
