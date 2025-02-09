# Encapsulate all relevant details about a single banking transaction
from dataclasses import dataclass # Import dataclass decorator
from datetime import datetime     # Import datetime module  

# Define Transaction class
@dataclass
class Transaction:
    transaction_type: str
    amount: float
    timestamp: datetime
    balance_after: float