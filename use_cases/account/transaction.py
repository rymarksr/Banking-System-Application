# Descriptio: This file contains the TransactionUseCase class, which is responsible for executing financial transactions on accounts.
from domain.exceptions import AccountNotFoundError, InsufficientFundsError # Import exceptions

# Define TransactionUseCase class
class TransactionUseCase:
    # Initialize TransactionUseCase class
    def __init__(self, account_repository):
        self.account_repository = account_repository
    
    # Define make_transaction method
    def make_transaction(self, account_id: str, amount: float, 
                        transaction_type: str) -> None:
        """
        Execute a financial transaction on an account
        
        Args:
            account_id: Target account identifier
            amount: Transaction amount (must be positive)
            transaction_type: 'deposit' or 'withdraw'
            
        Raises:
            ValueError: Invalid input parameters
            AccountNotFoundError: Account doesn't exist
            InsufficientFundsError: Withdrawal exceeds balance
        """
        if amount <= 0:
            raise ValueError("Transaction amount must be positive")
            
        if transaction_type not in ['deposit', 'withdraw']:
            raise ValueError("Invalid transaction type")
            
        account = self.account_repository.find_account_by_id(account_id)
        if not account:
            raise AccountNotFoundError(f"Account {account_id} not found")
            
        try:
            if transaction_type == 'deposit':
                account.deposit(amount)
            else:
                account.withdraw(amount)
        except ValueError as e:
            raise InsufficientFundsError(str(e)) from e

        self.account_repository.save_account(account)