import random 

class ATM:
    def __init__(self):
        self.accounts = {
            12345: 400,
            54321: 0,
            121212: 5
        }

    def createAccount(self, initialDeposit = 0.0):
        newAccount = random.randint(10000, 99999)
        if newAccount in self.accounts:
            raise KeyError(f"Account exists")
        if initialDeposit < 0:
            raise KeyError(f"Deposit must not be negative")
        self.accounts[newAccount] = initialDeposit
        return newAccount

    def deposit(self, accountID: int, amount: float):
        if accountID < 10000 or accountID > 99999:
            raise KeyError(f"Invalid account number")
        if accountID not in self.accounts:
            raise KeyError(f"Account {accountID} not found")
        if amount <= 0:
            raise KeyError(f"Deposit must be positive")
        self.accounts[accountID] += amount
        return self.accounts[accountID]
    
    def withdraw(self, accountID: int, amount: float):
        if accountID not in self.accounts:
            raise KeyError(f"Account {accountID} not found")
        if amount <= 0:
            raise KeyError(f"Withdrawal must be positive")
        if amount > self.accounts[accountID]:
            raise KeyError(f"Insufficient funds")
        self.accounts[accountID] -= amount
        return self.accounts[accountID]
    
    def getBalance(self, accountID: int) -> float:
        if accountID < 10000 or accountID > 99999:
            raise KeyError(f"Invalid account number")
        if accountID not in self.accounts:
            raise KeyError(f"Account {accountID} not found")
        return self.accounts[accountID]
    
    
