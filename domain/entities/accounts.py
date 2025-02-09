# Description: Account entity class
from dataclasses import dataclass                   # Import dataclass decorator
from datetime import datetime                       # Import datetime module
from typing import List                             # Import List type hint
from ..value_objects.transaction import Transaction # Import Transaction class

# Define Account class
class Account:
    # Initialize Account class
    def __init__(self, account_id: str, customer_id: str,
                 account_number: str, balance: float = 0.0):
        self.account_id = account_id
        self.customer_id = customer_id
        self.account_number = account_number
        self.balance = balance
        self.transactions: List[Transaction] = []
    
    # Deposit method
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero")
        self.balance += amount
        self._record_transaction('deposit', amount)

    # Withdraw method
    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self._record_transaction('withdraw', amount)
    
    # Record transaction method
    def _record_transaction(self, transaction_type: str, amount: float) -> None:
        self.transactions.append(
            Transaction(
                transaction_type=transaction_type,
                amount=amount,
                timestamp=datetime.now(),
                balance_after=self.balance
            )
        )

    # Get balance method
    def get_balance(self) -> float:
        return self.balance