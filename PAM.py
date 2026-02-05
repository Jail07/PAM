from datetime import datetime
class Amount:
    def __init__(self, amount: float, transaction_type: str ):
        self.amount = amount
        self.timestamp = datetime.now()
        self.transaction_type = transaction_type
    
    def __str__(self) -> str:
        return f"[{self.timestamp}] {self.transaction_type}: {self.amount}"


class PersonalAcc:
    def __init__(self, account_number: int, account_holder: str ):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount: float):
        if amount <= 0 and amount >= self.balance:
            raise ValueError
        transaction = Amount(amount, "DEPOSIT")
        self.transactions.append(transaction)
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError
        transaction = Amount(amount, "WITHDRAW")
        self.transactions.append(transaction)
        self.balance -= amount

    def print_transaction_history(self):
        print("Transaction history:")
        for transaction in self.transactions:
            print(transaction)
    
    def get_balance(self):
        return self.balance
    
    def set_account_number(self, account_number: int):
        self.account_number = account_number
    
    def get_account_holder(self):
        return self.account_holder
    
    def set_account_holder(self, account_holder: str):
        self.account_holder = account_holder

    def __str__(self):
        return f"{self.account_number}:{self.account_holder}: {self.balance}"
    
    def __add__(self, amount: int):
        self.deposit(amount)
        return self
    
    
    def __sub__(self, amount: int):
        self.withdraw(amount)
        return self
    


    

    



    


    

    
        