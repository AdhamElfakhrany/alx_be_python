import sys
from bank_account import BankAccount

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: main-0.py <owner> <action> <amount>")
        sys.exit(1)

    owner = sys.argv[1]
    action = sys.argv[2]
    amount = float(sys.argv[3])

    account = BankAccount(owner)

    if action == "deposit":
        account.deposit(amount)
    elif action == "withdraw":
        account.withdraw(amount)
    elif action == "display":
        account.display_balance()
    else:
        print("Unknown action")
