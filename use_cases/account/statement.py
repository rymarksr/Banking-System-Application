# Use Case: Generate account statement
from domain.exceptions import AccountNotFoundError  # Import AccountNotFoundError exception

# Define StatementUseCase class
class StatementUseCase:
    # Initialize StatementUseCase class
    def __init__(self, account_repository):
        self.account_repository = account_repository
    
    # Define generate_account_statement method
    def generate_account_statement(self, account_id: str) -> str:
        """
        Generate a formatted account statement with transaction history
        
        Args:
            account_id: Target account identifier
            
        Returns:
            Formatted statement string with header and transaction list
            
        Raises:
            AccountNotFoundError: If account doesn't exist
        """
        account = self.account_repository.get(account_id)
        if not account:
            raise AccountNotFoundError(f"Account {account_id} not found")

        statement = [
            f"Statement for Account: {account.account_number}",
            f"Balance: {account.balance:.2f}",
            "\nTransactions:",
            "Date/Time\t\tType\t\tAmount\t\tBalance"
        ]
        for txn in account.transactions:
            statement.append(
                f"{txn.timestamp.strftime('%Y-%m-%d %H:%M')}\t"
                f"{txn.transaction_type:<10}\t"                 # Left-align in 10-character width
                f"{txn.amount:>8.2f}\t"                         # Right-align amount in 8-char width
                f"{txn.balance_after:>8.2f}"                    # Right-align amount in 8-char width
            )
        return "\n".join(statement)