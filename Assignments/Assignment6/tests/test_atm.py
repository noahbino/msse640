# tests/test_app.py
import pytest
from src.atm import ATM

# -- Create Account --

def testCreateAccountFailWithNegative():
    atm = ATM()
    with pytest.raises(KeyError, match="Deposit must not be negative") : atm.createAccount(-1)

def testCreateAccountSuccess():
    atm = ATM()
    atm.createAccount()

# -- Deposit --
def testInvalidAccountNumber():
    atm = ATM()
    with pytest.raises(KeyError, match="Invalid account number") : atm.deposit(5, 28)

def testDepositFailure():
    atm = ATM()
    with pytest.raises(KeyError, match="Account 67098 not found") : atm.deposit(67098, 10)

def testNonPositiveDeposit():
    atm = ATM()
    with pytest.raises(KeyError, match="Deposit must be positive") : atm.deposit(12345, 0)

def testSuccessfulDeposit():
    atm = ATM()
    depositAmount = 10
    accountID = 12345
    amountBefore = atm.getBalance(accountID)
    amountAfter = atm.deposit(12345, depositAmount)
    assert amountBefore + depositAmount == amountAfter

# -- Withdraw --

def testWithdrawAccountNotFound():
    atm = ATM()
    with pytest.raises(KeyError, match="Account 77777 not found") :  atm.withdraw(77777, 99)

def testWithdrawNegative():
    atm = ATM()
    with pytest.raises(KeyError, match="Withdrawal must be positive") :  atm.withdraw(12345, -10)

def testWithdrawInsufficientFunds():
    atm = ATM()
    with pytest.raises(KeyError, match="Insufficient funds") :  atm.withdraw(12345, 100000)

def testWithdrawSuccess():
    atm = ATM()
    withdrawAmount = 10
    accountID = 12345
    amountBefore = atm.getBalance(accountID)
    amountAfter = atm.withdraw(accountID, withdrawAmount)
    assert amountBefore - withdrawAmount == amountAfter

# -- Get Balance --

def testGetBalanceInvalidAccount():
    atm = ATM()
    with pytest.raises(KeyError, match="Invalid account number") :  atm.getBalance(3)


def testGetBalanceAccountFailure():
    atm = ATM()
    with pytest.raises(KeyError, match="Account 55555 not found") :  atm.getBalance(55555)

def testGetBalanceSuccess():
    atm = ATM()
    balance = atm.getBalance(12345)
    assert balance == 400

# -- Entire Flow -- 

def testFlowSuccess():
    atm = ATM()
    initialDeposit = 25
    newAccount = atm.createAccount(initialDeposit)
    assert atm.getBalance(newAccount) == initialDeposit

    withdrawAmount = 10
    amountAfterWithdraw = atm.withdraw(newAccount, withdrawAmount)
    assert atm.getBalance(newAccount) == initialDeposit - withdrawAmount

    depositAmount = 55
    amountAfterDeposit = atm.deposit(newAccount, depositAmount)
    assert atm.getBalance(newAccount) == amountAfterDeposit

    assert atm.getBalance(newAccount) == (initialDeposit - withdrawAmount + depositAmount)



    