# Description: CreateAccountUseCase class
from uuid import uuid4                          # Import uuid4
from domain.entities.accounts import Account    # Import Account class
from domain.entities.customers import Customer  # Import Customer class

# Define CreateAccountUseCase class
class CreateAccountUseCase:
    # Initialize CreateAccountUseCase class
    def __init__(self, account_repository, customer_repository):
        self.account_repository = account_repository
        self.customer_repository = customer_repository
        self.account_number_seq = 10000000

    # Define create_account method
    def create_account(self, customer_id: str, name: str, email: str, phone_number: str) -> Account:
        # Check if customer exists or create new
        customer = self.customer_repository.find_accounts_by_customer_id(customer_id)
        if not customer:
            customer = Customer(
                customer_id=customer_id,
                name=name,
                email=email,
                phone_number=phone_number
            )
            self.customer_repository.save_customer(customer)

        # Create account
        account = Account(
            account_id=str(uuid4()),
            customer_id=customer_id,
            account_number=self._generate_account_number(),
            balance=0.0
        )

        # Save account
        self.account_repository.save_account(account)
        return account

    # Define _generate_account_number method
    def _generate_account_number(self) -> str:
        num = self.account_number_seq
        self.account_number_seq += 1
        return f"{num:08d}"