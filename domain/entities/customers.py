# Customer entity class
class Customer:
    # Initialize Customer object
    def __init__(self, customer_id: str, name: str, 
                 email: str, phone_number: str):
        """
        Customer with validated contact information

        :param customer_id: Unique customer identifier
        :param name: Customer name
        :param email: Customer valid email address
        :param phone_number: Customer phone number
        """
        if not name.strip():
            raise ValueError("Customer name cannot be empty")
        
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email address")
        
        if not phone_number.strip().isdigit() or len(phone_number) < 10:
            raise ValueError("Phone number must contain only digits and be at least 10 characters")
        
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number

    # String representation of Customer object
    def __str__(self) -> str:
        return f"Customer {self.name} (ID: {self.customer_id})\n" \
                f"Email: {self.email}\n" \
                f"Phone: {self.phone_number}"