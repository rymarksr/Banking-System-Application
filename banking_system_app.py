# Description: This file contains the main entry point for the banking system application.
from infrastructure.repositories.account_repository import AccountRepository                    # Import AccountRepository class
from infrastructure.repositories.customer_repository import CustomerRepository                  # Import CustomerRepository class
from use_cases.account.create_account import CreateAccountUseCase                               # Import CreateAccountUseCase class    
from use_cases.account.transaction import TransactionUseCase                                    # Import TransactionUseCase class
from use_cases.account.statement import StatementUseCase                                        # Import StatementUseCase class
from domain.exceptions import AccountNotFoundError, InsufficientFundsError, InvalidAccountError # Import exceptions


def main():
    # Initialize repositories
    account_repo = AccountRepository()                  # Initialize account repository
    customer_repo = CustomerRepository()                # Initialize customer repository
    transaction_uc = TransactionUseCase(account_repo)   # Initialize transaction use case
    statement_uc = StatementUseCase(account_repo)       # Initialize statement use case

    # Create use case instance
    account_creator = CreateAccountUseCase(account_repo, customer_repo)

    while True:
        # Display menu
        print("\n\t\t\tℍ𝕖𝕝𝕝𝕠 𝕒𝕟𝕕 𝕎𝕖𝕝𝕔𝕠𝕞𝕖 𝕥𝕠 ℝ𝕊ℝ 𝔹𝕒𝕟𝕜​​​​​ \n\n (𝟭) Create Account | (𝟮) Make Transaction | (𝟯) Generate Statement | (𝟰) Exit")
        
        try:
            # Get user input
            command = int(input("\nPress 1, 2, 3 or 4: "))

            if command == 1:
                        # Get customer details
                        customer_id = input("Enter customer ID: ")
                        name = input("Enter full name: ")
                        email = input("Enter email: ")
                        phone_number = input("Enter phone number: ")
                        
                        try:
                            # Create account
                            new_account = account_creator.create_account(
                                customer_id=customer_id,
                                name=name,
                                email=email,
                                phone_number=phone_number
                            )
                            
                            # Display results
                            print("\n=== Account Created Successfully ===")
                            print(f"Customer ID: {customer_id}")
                            print(f"Account Holder: {name}")
                            print(f"Account Number: {new_account.account_number}")
                            print(f"Current Balance: ${new_account.balance:.2f}")
                            print(f"Account ID: {new_account.account_id}")
                            print("=" * 90)
                            
                        # Handle exceptions for Account creation
                        except InvalidAccountError as e:
                            print(f"\nError creating account: {str(e)}")

            elif command == 2:
                    # Get user input
                    account_id = input("Enter account ID: ").strip()
                    transaction_type = input("Transaction type (deposit/withdraw): ").strip().lower()
                    amount = float(input("Amount: ").strip())

                    try:
                        # Execute transaction
                            transaction_uc.make_transaction(account_id, amount, transaction_type)
                            
                            # Get updated account details
                            updated_account = account_repo.find_account_by_id(account_id)
                            
                            print("\n=== Transaction Successful ===")
                            print(f"Account ID: {updated_account.account_id}")
                            print(f"New Balance: ${updated_account.balance:.2f}")
                            print("=" * 90)

                    # Handle exceptions for Make Transaction
                    except ValueError as e:
                        print(f"\nInvalid input: {str(e)}")
                    except AccountNotFoundError as e:
                        print(f"\nAccount error: {str(e)}")
                    except InsufficientFundsError as e:
                        print(f"\nFunds error: {str(e)}")

            elif command == 3:
                    try:
                        # Get user input for account statement (using account ID)
                        account_id = input("Enter account ID (from account creation): ").strip()
                        statement = statement_uc.generate_account_statement(account_id)
                        
                        print("\n=== Account Statement ===")
                        print(statement)
                        print("=" * 90)
                    
                    # Handle exceptions for Generate Statement
                    except AccountNotFoundError as e:
                        print(f"\nError: {str(e)}")
                    except ValueError as e:
                        print(f"\nInvalid input: {str(e)}")
                        
            elif command == 4:
                    # Exit the program
                    print("\n\t\t\t𝕋𝕙𝕒𝕟𝕜 𝕪𝕠𝕦 𝕗𝕠𝕣 𝕦𝕤𝕚𝕟𝕘 ℝ𝕊ℝ 𝔹𝕒𝕟𝕜❕\n")
                    break
               
        except ValueError:
            # Invalid command
            print("\n\t\tInvalid Input❗ Please enter a valid number (1-4).")
            print("=" * 90)

# Entry point for the Banking System Application
if __name__ == "__main__":
    main()