# Description: CustomerRepository class responsible for handling customer data operations.
from threading import Lock                      # Import Lock class from threading module
from typing import Dict, Optional, List         # Import necessary modules
from domain.entities.customers import Customer  # Import Customer entity

# Define CustomerRepository class
class CustomerRepository:
    # Initialize CustomerRepository class
    def __init__(self):
        self._customers: Dict[str, Customer] = {}
        self._lock = Lock()

    # Define save_customer method
    def save_customer(self, customer: Customer) -> None:
        """Save a customer with thread-safe operation"""
        with self._lock:
            self._customers[customer.customer_id] = customer

    # Define find_customer_by_id method
    def find_accounts_by_customer_id(self, customer_id: str) -> Optional[Customer]:
        """Find customer by ID with thread-safe operation"""
        with self._lock:
            return self._customers.get(customer_id)
    
    