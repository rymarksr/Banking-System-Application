# Description: Custom exceptions for the domain layer
class AccountNotFoundError(Exception):
    """Raised when an account is not found"""

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""

class InvalidCustomerError(Exception):
    """Raised for invalid customer data"""
    
class InvalidAccountError(Exception):
    """Raised for invalid account data"""