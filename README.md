# 🏦 Banking System Application

A Python implementation of a banking system following Clean Architecture principles.

## 🏗️ Project Structure
```
├── domain/                           # Core business logic
│   ├── entities/
│   │   ├── accounts.py               # Account entity
│   │   └── customers.py              # Customer entity
│   ├── value_objects/
│   │   └── transactions.py
│   └── exceptions.py
├── use_cases/                        # Application business rules
│   ├── account/
│   │   ├── create_account.py
│   │   ├── transaction.py
│   │   └── statement.py
└── infrastructure/                   # External implementations
    └── repositories/
        └── account_repository.py
        └── customer_repository.py
    
```

## ⚙️ Features
- **Core Entities**
  - `Accounts`: Manage balances with deposit/withdraw operations
  - `Customers`: Store client information
- **Business Use Cases**
  - Account creation
  - Transaction processing (deposit/withdraw)
  - Account statement generation
- **Persistence**
  - `AccountRepository`: Data storage interface
  - `CustomerRepository`: Data storage interface

## 🚀 Getting Started
```bash
git clone https://github.com/rymarksr/Banking-System-Application.git
cd Banking-System-Application
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

## 🧪 Usage Example (Run the application)
```bash
python -m "banking_system_app"
```
## ✅ Testing
Run test scenarios:

Welcome message 
Menu from 1-4
images/Welcome to RSR Bank.png

Create Account
images/CreateAccount.png

Deposit
images/Deposit.png

Withdraw
images/Withdraw.png

Generate Statement
images/GenerateStatement.png

Exit
images/Exit.png


## 📚 Clean Architecture Layers
1. **Domain**: Pure business rules (`Account`, `Customer`)
2. **Use Cases**: Application-specific business rules
3. **Infrastructure**: DB/External system implementations

## 🤝 Contributing
Contributions welcome! Ensure:
- 100% test coverage
- PEP8 compliance
- Clean architecture boundaries maintained


> **Note**: Replace repository URLs and contact info with your actual project details
