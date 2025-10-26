import pytest
from src.bank import BankAccount

def test_create_account():
    account = BankAccount("Raihan", 100)

    assert account.owner == "Raihan"
    assert account.balance == 100

    # test for deposit money
def test_deposit():
    account = BankAccount("Emon")
    account.deposit(50)
    account.deposit(40)
    assert account.balance == 90

    # test depositing a negative amount (should raise an error)
    with pytest.raises(ValueError):
        account.deposit(-10)

    # test for withdrawing money
def test_withdraw():
    account = BankAccount("Ema", 100)
    account.withdraw(40)
    assert account.balance == 60

    # test the balance
@pytest.mark.skip(reason = "Skping this test due to xyz reason")
def test_get_balance():
    account = BankAccount("Ruhama", 200)
    assert account.get_balance() == 200