from PAM import PersonalAcc

def main():
    account = PersonalAcc(1001, "John Doe")

    print(account)

    account.deposit(500)
    account.withdraw(150)

    # Operator overloading
    account + 200
    account - 50

    print("\nCurrent Balance:")
    print(f"${account.get_balance():.2f}")

    account.print_transaction_history()

if __name__ == "__main__":
    main()
