import pytest
from wallet import Wallet, InsufficientAmount

@pytest.fixture
def wallet():
    '''Returns a Wallet instance with a zero balance'''
    return Wallet(0)

@pytest.fixture
def wallet_with_funds():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)

def test_default_initial_amount(wallet):
    assert wallet.balance == 0
    
def test_setting_initial_amount(wallet_with_funds):
    assert wallet_with_funds.balance == 20
    
def test_wallet_add_cash(wallet_with_funds):
    wallet_with_funds.add_cash(80)
    assert wallet_with_funds.balance == 100
    
def test_wallet_spend_cash(wallet_with_funds):
    wallet_with_funds.spend_cash(10)
    assert wallet_with_funds.balance == 10
    
def test_wallet_spend_cash_raises_exception_on_insufficient_amount(wallet_with_funds):   
    with pytest.raises(InsufficientAmount):
        wallet_with_funds.spend_cash(100)
        