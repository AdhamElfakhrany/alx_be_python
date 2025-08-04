import sys
from bank_account import BankAccount

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: main-0.py <owner> <action> [<amount>]")
        sys.exit(1)

    owner = sys.argv[1]
    action = sys.argv[2]

    account = BankAccount(owner)

    if action == "deposit":
        if len(sys.argv) != 4:
            print("Amount required for deposit.")
        else:
            account.deposit(float(sys.argv[3]))
    elif action == "withdraw":
        if len(sys.argv) != 4:
            print("Amount required for withdraw.")
        else:
            account.withdraw(float(sys.argv[3]))
    elif action == "display":
        account.display_balance()
    else:
        print("Unknown action")
