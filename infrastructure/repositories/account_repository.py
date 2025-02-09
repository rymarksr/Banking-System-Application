# Description: AccountRepository class to handle account data storage and retrieval
from threading import Lock                          # Import Lock class
from typing import Dict, List, Optional             # Import Dict, List, Optional
from collections import defaultdict                 # Import defaultdict
from domain.entities.accounts import Account        # Import Account class    
from domain.exceptions import AccountNotFoundError  # Import AccountNotFoundError exception

# Define AccountRepository class
class AccountRepository:
    # Initialize AccountRepository class
    def __init__(self):
        self._accounts: Dict[str, Account] = {}
        self._customer_accounts = defaultdict(list)
        self._lock = Lock()

    # Define get method
    def get(self, account_id: str) -> Account:
        """
        Retrieve account by ID
        Raises AccountNotFoundError if not found
        """
        account = self._accounts.get(account_id)
        if not account:
            raise AccountNotFoundError(f"Account {account_id} not found")
        return account
    
    # Define save_account method
    def save_account(self, account: Account) -> None:
        with self._lock:
            self._accounts[account.account_id] = account
            if account.account_id not in self._customer_accounts[account.customer_id]:
                self._customer_accounts[account.customer_id].append(account.account_id)

    # Define find_account_by_id method
    def find_account_by_id(self, account_id: str) -> Optional[Account]:
        with self._lock:
            return self._accounts.get(account_id)

    # Define find_accounts_by_customer_id method
    def find_accounts_by_customer_id(self, customer_id: str) -> List[Account]:
        with self._lock:
            return [self._accounts[aid] for aid in 
                   self._customer_accounts.get(customer_id, []) 
                   if aid in self._accounts]