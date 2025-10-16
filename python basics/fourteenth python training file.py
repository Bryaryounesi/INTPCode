# Python Tutorial File 14 - Errors and Exceptions
# ==============================================

print("lesson name : errors and exceptions handling")

# ==============================
# Syntax Errors
# ==============================

print("=== Syntax Errors ===")

print("--- Common Syntax Error Examples ---")

# 1. IndentationError
print("1. IndentationError:")
try:
    exec('''def test():
print("Hello")''')
except IndentationError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 2. SyntaxError - Unclosed parenthesis
print("2. SyntaxError - Unclosed parenthesis:")
try:
    exec('print("Hello"')
except SyntaxError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 3. SyntaxError - Incorrect operator usage
print("3. SyntaxError - Incorrect operator usage:")
try:
    exec('''if x = 5:
    print(x)''')
except SyntaxError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 4. SyntaxError - Invalid keyword
print("4. SyntaxError - Invalid keyword:")
try:
    exec('class = "Python"')
except SyntaxError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 5. SyntaxError - Incomplete string
print("5. SyntaxError - Incomplete string:")
try:
    exec('f"Hello {name"')
except SyntaxError as e:
    print(f"   Error: {e}")

print("-------------------------")

# ==============================
# Exceptions
# ==============================

print("=== Exceptions ===")

print("--- Common Exception Examples ---")

# 1. TypeError - Operation on inappropriate type
print("1. TypeError:")
try:
    result = 5 + "Hello"
except TypeError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 2. ValueError - Invalid value
print("2. ValueError:")
try:
    number = int("Hello")
except ValueError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 3. IndexError - Index out of range
print("3. IndexError:")
try:
    my_list = [1, 2, 3]
    item = my_list[5]
except IndexError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 4. KeyError - Key not found in dictionary
print("4. KeyError:")
try:
    my_dict = {"name": "Ali", "age": 25}
    value = my_dict["email"]
except KeyError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 5. ZeroDivisionError - Division by zero
print("5. ZeroDivisionError:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 6. NameError - Undefined variable
print("6. NameError:")
try:
    print("undefined_variable")
except NameError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 7. AttributeError - Attribute doesn't exist
print("7. AttributeError:")
try:
    number = 5
    number.append(10)
except AttributeError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 8. FileNotFoundError - File doesn't exist
print("8. FileNotFoundError:")
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"   Error: {e}")

print("-------------------------")

# ==============================
# Raising Exceptions
# ==============================

print("=== Raising Exceptions ===")

# Raising exception with condition
def validate_age(age):
    """Age validation"""
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 150:
        raise ValueError("Age cannot be more than 150")
    return age

print("--- Age Validation Test ---")
try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    validate_age(25)
    print("Age is valid")
except ValueError as e:
    print(f"Error: {e}")

print("-------------------------")

# Raising exception in calculations
def calculate_average(numbers):
    """Calculate average of numbers"""
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    
    if any(not isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All values must be numeric")
    
    return sum(numbers) / len(numbers)

print("--- Average Calculation Test ---")
try:
    result = calculate_average([])
except ValueError as e:
    print(f"Error: {e}")

try:
    result = calculate_average([10, 20, "30"])
except TypeError as e:
    print(f"Error: {e}")

try:
    result = calculate_average([10, 20, 30])
    print(f"Average: {result}")
except Exception as e:
    print(f"Error: {e}")

print("-------------------------")

# ==============================
# Exception Handling
# ==============================

print("=== Exception Handling ===")

print("--- Basic try-except handling ---")

# Handling division by zero error
def safe_divide(a, b):
    """Safe division with error handling"""
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except TypeError:
        return "Error: Both values must be numeric"
    else:
        return f"Result: {result}"
    finally:
        print("  Division operation completed")

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "2"))

print("-------------------------")

# Handling list access errors
def get_list_item(lst, index):
    """Get item from list with error handling"""
    try:
        return lst[index]
    except IndexError:
        return f"Error: Index {index} is out of list range"
    except TypeError:
        return "Error: Index must be numeric"

my_list = ["a", "b", "c"]
print(get_list_item(my_list, 1))
print(get_list_item(my_list, 5))
print(get_list_item(my_list, "1"))

print("-------------------------")

print("--- Using else and finally ---")

def process_user_data(user_data):
    """Process user data with complete error handling"""
    try:
        name = user_data["name"]
        age = user_data["age"]
        print(f"  Processing data for {name}...")
        
    except KeyError as e:
        print(f"  Error: Field {e} does not exist")
        return None
    
    except Exception as e:
        print(f"  Unexpected error: {e}")
        return None
    
    else:
        # If no error occurs
        print("  Data processed successfully")
        return {"name": name, "age": age}
    
    finally:
        # Always executes
        print("  Processing operation completed")

print("--- User Data Processing Test ---")
user1 = {"name": "Ali", "age": 25}
result1 = process_user_data(user1)

user2 = {"name": "Sara"}  # age is missing
result2 = process_user_data(user2)

print("-------------------------")

# ==============================
# Advanced Exception Handling
# ==============================

print("=== Advanced Exception Handling ===")

class CustomError(Exception):
    """Custom exception"""
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code
    
    def __str__(self):
        return f"{self.args[0]} (Error Code: {self.error_code})"

def validate_password(password):
    """Password validation"""
    if len(password) < 8:
        raise CustomError("Password must be at least 8 characters", 1001)
    
    if not any(char.isdigit() for char in password):
        raise CustomError("Password must contain at least one digit", 1002)
    
    if not any(char.isupper() for char in password):
        raise CustomError("Password must contain at least one uppercase letter", 1003)
    
    return "Password is valid"

print("--- Password Validation Test ---")
passwords = ["short", "nouppercase1", "NOLOWERCASE1", "ValidPass123"]

for pwd in passwords:
    try:
        result = validate_password(pwd)
        print(f"  '{pwd}': {result}")
    except CustomError as e:
        print(f"  '{pwd}': {e}")

print("-------------------------")

# ==============================
# Practical Example: Bank Management System
# ==============================

print("=== Bank Management System ===")

class BankAccount:
    """Bank account class with error handling"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        """Deposit to account"""
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return f"Amount ${amount} deposited successfully"
        
        except ValueError as e:
            return f"Deposit error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    
    def withdraw(self, amount):
        """Withdraw from account"""
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -${amount}")
            return f"Amount ${amount} withdrawn successfully"
        
        except ValueError as e:
            return f"Withdrawal error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    
    def transfer(self, amount, target_account):
        """Transfer to another account"""
        try:
            if not isinstance(target_account, BankAccount):
                raise TypeError("Target account must be a BankAccount")
            
            # Withdraw from current account
            withdraw_result = self.withdraw(amount)
            if "error" in withdraw_result.lower():
                raise ValueError(withdraw_result)
            
            # Deposit to target account
            target_account.deposit(amount)
            self.transaction_history.append(f"Transfer to {target_account.account_holder}: -${amount}")
            
            return f"Amount ${amount} transferred to {target_account.account_holder}"
        
        except (TypeError, ValueError) as e:
            return f"Transfer error: {e}"
        except Exception as e:
            return f"Unexpected error: {e}"
    
    def get_balance(self):
        """Get account balance"""
        return f"Account balance for {self.account_holder}: ${self.balance}"
    
    def get_transaction_history(self):
        """Get transaction history"""
        if not self.transaction_history:
            return "No transactions performed"
        
        history = f"Transaction history for {self.account_holder}:\n"
        for i, transaction in enumerate(self.transaction_history, 1):
            history += f"  {i}. {transaction}\n"
        return history

# Test bank system
print("--- Bank Management System Test ---")
account1 = BankAccount("Ali Rezaei", 1000)
account2 = BankAccount("Sara Ahmadi", 500)

print(account1.deposit(200))
print(account1.withdraw(100))
print(account1.withdraw(2000))  # Insufficient balance
print(account1.transfer(300, account2))
print(account1.transfer(-100, account2))  # Negative amount

print(account1.get_balance())
print(account2.get_balance())

print("-------------------------")

# ==============================
# Practical Exercises
# ==============================

print("=== Practical Exercises ===")

# Exercise 1: Safe Calculator
print("--- Safe Calculator ---")

def safe_calculator():
    """Calculator with error handling"""
    print("Safe Calculator")
    print("Operations: +, -, *, /")
    
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator: ")
        num2 = float(input("Enter second number: "))
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator")
        
        print(f"Result: {result}")
    
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Calculator operation completed")

# Simulate user input (use input() in real environment)
print("Calculator simulation:")
try:
    # Simulate correct calculation
    num1, operator, num2 = 10, "/", 2
    if operator == "/" and num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    print(f"  10 / 2 = {10 / 2}")
except ZeroDivisionError as e:
    print(f"  Error: {e}")

try:
    # Simulate error
    num1, operator, num2 = 10, "/", 0
    if operator == "/" and num2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    print(f"  10 / 0 = {10 / 0}")
except ZeroDivisionError as e:
    print(f"  Error: {e}")

print("-------------------------")

# Exercise 2: Form Validation System
print("--- Form Validation System ---")

def validate_form_data(data):
    """Form data validation"""
    errors = []
    
    # Name validation
    try:
        if not data.get("name"):
            raise ValueError("Name is required")
        if len(data["name"]) < 2:
            raise ValueError("Name must be at least 2 characters")
    except ValueError as e:
        errors.append(f"Name: {e}")
    
    # Email validation
    try:
        email = data.get("email", "")
        if not email:
            raise ValueError("Email is required")
        if "@" not in email:
            raise ValueError("Invalid email format")
    except ValueError as e:
        errors.append(f"Email: {e}")
    
    # Age validation
    try:
        age = data.get("age")
        if age is None:
            raise ValueError("Age is required")
        
        age = int(age)
        if age < 18:
            raise ValueError("Age must be at least 18")
        if age > 100:
            raise ValueError("Age cannot be more than 100")
    
    except ValueError as e:
        errors.append(f"Age: {e}")
    except TypeError:
        errors.append("Age: Must be numeric")
    
    return errors

# Test form validation
test_cases = [
    {"name": "Ali", "email": "ali@example.com", "age": "25"},
    {"name": "A", "email": "invalid-email", "age": "15"},
    {"name": "", "email": "", "age": "invalid"},
    {"name": "Sara", "email": "sara@example.com", "age": "120"}
]

for i, data in enumerate(test_cases, 1):
    print(f"  Test {i}:")
    errors = validate_form_data(data)
    if errors:
        for error in errors:
            print(f"    - {error}")
    else:
        print("    ✓ Data is valid")

print("-------------------------")

# Exercise 3: File Management with Error Handling
print("--- File Management with Error Handling ---")

def safe_file_operations():
    """Safe file operations"""
    try:
        # Try to read file
        with open("example.txt", "r") as file:
            content = file.read()
            print("File content read successfully")
    
    except FileNotFoundError:
        print("File does not exist, creating new file...")
        
        try:
            # Create new file
            with open("example.txt", "w") as file:
                file.write("This is a sample file\n")
                file.write("Error handling in Python\n")
            print("New file created successfully")
        
        except PermissionError:
            print("Error: No permission to create file")
        except Exception as e:
            print(f"Unexpected error in file creation: {e}")
    
    except PermissionError:
        print("Error: No permission to read file")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
    
    finally:
        print("File operation completed")

# Test file management
safe_file_operations()

print("-------------------------")

print("=== Final Notes ===")
print("1. Syntax errors are identified before program execution")
print("2. Exceptions occur during program execution")
print("3. Use try-except to handle errors")
print("4. Use else for code that should run when no error occurs")
print("5. Use finally for code that should always run")
print("6. You can create custom exceptions")

print("End of errors and exceptions training")