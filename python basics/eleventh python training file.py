# فایل یازدهم آموزش پایتون - کلاس‌ها و برنامه‌نویسی شیءگرا 🔥
# ===================================================

print("lesson name : classes & object-oriented programming")
🔥 ضروری برای اتوماسیون هوشمند و APIها
♻️ میان‌رده / مفید اما غیرمستقیم
⚠️ کم‌اهمیت / فقط آموزشی

# ==============================
# مقدمه‌ای بر برنامه‌نویسی شیءگرا 🔥
# ==============================

print("=== مفاهیم پایه برنامه‌نویسی شیءگرا ===")

# تعریف یک کلاس ساده 🔥
class Person:
    """یک کلاس ساده برای نمایش یک شخص"""
    
    # متغیرهای کلاس (Class Attributes) ♻️
    species = "Human"
    planet = "Earth"
    
    def __init__(self, name, age):  # 🔥 سازنده
        self.name = name
        self.age = age
    
    # متدهای نمونه (Instance Methods) 🔥
    def introduce(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday! Now I'm {self.age} years old."

print("-------------------------")

# ایجاد نمونه‌هایی از کلاس 🔥
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())

print("-------------------------")

# دسترسی به متغیرهای کلاس و نمونه ♻️
print(f"Person1 name: {person1.name}")
print(f"Person2 age: {person2.age}")
print(f"All humans are: {Person.species}")
print(f"Person1 species: {person1.species}")

print("-------------------------")

# ==============================
# کلاس‌های پایه و نمونه‌سازی 🔥
# ==============================

print("=== کلاس‌های پایه و نمونه‌سازی ===")

class Car:  # 🔥 مدل‌سازی سرویس/ربات
    """کلاسی برای نمایش خودرو"""
    
    wheels = 4  # ♻️
    vehicle_type = "Land Vehicle"  # ♻️
    
    def __init__(self, brand, model, color):  # 🔥
        self.brand = brand
        self.model = model
        self.color = color
        self.is_running = False
    
    def start_engine(self):  # 🔥 کنترل وضعیت
        self.is_running = True
        return f"{self.brand} {self.model} engine started!"
    
    def stop_engine(self):  # 🔥
        self.is_running = False
        return f"{self.brand} {self.model} engine stopped!"
    
    def get_info(self):  # ♻️
        status = "running" if self.is_running else "stopped"
        return f"{self.color} {self.brand} {self.model} - {status}"

# ایجاد نمونه‌ها 🔥
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

print(car1.get_info())
print(car2.get_info())

print(car1.start_engine())
print(car1.get_info())

print("-------------------------")

# ==============================
# متدها و ویژگی‌ها 🔥
# ==============================

print("=== متدها و ویژگی‌ها ===")

class BankAccount:  # 🔥 مثال واقعی (پرداخت/توکن/داده حساس)
    """کلاسی برای نمایش حساب بانکی"""
    
    bank_name = "Python Bank"  # ♻️
    interest_rate = 0.05  # ♻️
    
    def __init__(self, account_holder, initial_balance=0):  # 🔥 ورودی‌های مهم
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()  # 🔥 متد خصوصی
    
    def _generate_account_number(self):  # 🔥 Encapsulation
        import random
        return f"ACC{random.randint(10000, 99999)}"
    
    def deposit(self, amount):  # 🔥 عملیات
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):  # 🔥 مدیریت خطا
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):  # ♻️
        return f"Balance: ${self.balance}"
    
    def apply_interest(self):  # ♻️
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}"

# استفاده از کلاس حساب بانکی 🔥
account1 = BankAccount("Ali", 1000)
account2 = BankAccount("Sara", 500)