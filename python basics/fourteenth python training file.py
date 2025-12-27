# فایل چهاردهم آموزش پایتون - مدیریت خطاها و استثناها
# ====================================================

print("lesson name : errors and exceptions handling")

# 🔥 ضروری برای درک خطاها و جلوگیری از کرش برنامه
# ==============================
# خطاهای نحوی (Syntax Errors)
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

# 2. SyntaxError - Unclosed parenthesis
print("2. SyntaxError - Unclosed parenthesis:")
try:
    exec('print("Hello"')
except SyntaxError as e:
    print(f"   Error: {e}")

# 3. SyntaxError - Incorrect operator usage
print("3. SyntaxError - Incorrect operator usage:")
try:
    exec('''if x = 5:
    print(x)''')
except SyntaxError as e:
    print(f"   Error: {e}")

# 4. SyntaxError - Invalid keyword
print("4. SyntaxError - Invalid keyword:")
try:
    exec('class = "Python"')
except SyntaxError as e:
    print(f"   Error: {e}")

# 5. SyntaxError - Incomplete string
print("5. SyntaxError - Incomplete string:")
try:
    exec('f"Hello {name"')
except SyntaxError as e:
    print(f"   Error: {e}")

print("-------------------------")

# 🔥 ضروری برای مدیریت استثناها در اجرای برنامه
# ==============================
# Exceptions
# ==============================

print("=== Exceptions ===")
print("--- Common Exception Examples ---")

# 1. TypeError
print("1. TypeError:")
try:
    result = 5 + "Hello"
except TypeError as e:
    print(f"   Error: {e}")

# 2. ValueError
print("2. ValueError:")
try:
    number = int("Hello")
except ValueError as e:
    print(f"   Error: {e}")

# 3. IndexError
print("3. IndexError:")
try:
    my_list = [1, 2, 3]
    item = my_list[5]
except IndexError as e:
    print(f"   Error: {e}")

# 4. KeyError
print("4. KeyError:")
try:
    my_dict = {"name": "Ali", "age": 25}
    value = my_dict["email"]
except KeyError as e:
    print(f"   Error: {e}")

# 5. ZeroDivisionError
print("5. ZeroDivisionError:")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"   Error: {e}")

# 6. NameError
print("6. NameError:")
try:
    print(undefined_variable)
except NameError as e:
    print(f"   Error: {e}")

# 7. AttributeError
print("7. AttributeError:")
try:
    number = 5
    number.append(10)
except AttributeError as e:
    print(f"   Error: {e}")

# 8. FileNotFoundError
print("8. FileNotFoundError:")
try:
    with open("nonexistent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"   Error: {e}")

print("-------------------------")

# ✅ تمرینی: بالا بردن درک عملی
# ==============================
# Raising Exceptions
# ==============================

print("=== Raising Exceptions ===")

def validate_age(age):
    """Age validation"""
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 150:
        raise ValueError("Age cannot be more than 150")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")

try:
    validate_age(25)
    print("Age is valid")
except ValueError as e:
    print(f"Error: {e}")

def calculate_average(numbers):
    """Calculate average of numbers"""
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    
    if any(not isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All values must be numeric")
    
    return sum(numbers) / len(numbers)

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

# 🔥 ضروری برای اتوماسیون و برنامه‌های واقعی
# ==============================
# Exception Handling
# ==============================

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

# ✅ تمرینی: else و finally
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
        print("  Data processed successfully")
        return {"name": name, "age": age}
    finally:
        print("  Processing operation completed")

user1 = {"name": "Ali", "age": 25}
result1 = process_user_data(user1)
user2 = {"name": "Sara"}
result2 = process_user_data(user2)

print("-------------------------")

# 🔥 ضروری برای پروژه‌های واقعی
# ==============================
# Advanced Exception Handling
# ==============================

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

passwords = ["short", "nouppercase1", "NOLOWERCASE1", "ValidPass123"]
for pwd in passwords:
    try:
        result = validate_password(pwd)
        print(f"  '{pwd}': {result}")
    except CustomError as e:
        print(f"  '{pwd}': {e}")

print("-------------------------")

# ✅ تمرینی: سیستم بانکی با مدیریت خطا
# ==============================
class BankAccount:
    """Bank account class with error handling"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
    
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            self.transaction_history.append(f"Deposit: +${amount}")
            return f"Amount ${amount} deposited successfully"
        except ValueError as e:
            return f"Deposit error: {e}"
    
    def withdraw(self, amount):
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
    
    def transfer(self, amount, target_account):
        try:
            if not isinstance(target_account, BankAccount):
                raise TypeError("Target account must be a BankAccount")
            withdraw_result = self.withdraw(amount)
            if "error" in withdraw_result.lower():
                raise ValueError(withdraw_result)
            target_account.deposit(amount)
            self.transaction_history.append(f"Transfer to {target_account.account_holder}: -${amount}")
            return f"Amount ${amount} transferred to {target_account.account_holder}"
        except (TypeError, ValueError) as e:
            return f"Transfer error: {e}"

account1 = BankAccount("Ali Rezaei", 1000)
account2 = BankAccount("Sara Ahmadi", 500)
print(account1.deposit(200))
print(account1.withdraw(100))
print(account1.withdraw(2000))
print(account1.transfer(300, account2))
print(account1.transfer(-100, account2))

print("End of errors and exceptions training")