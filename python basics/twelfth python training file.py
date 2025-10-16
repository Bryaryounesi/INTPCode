# فایل دوازدهم آموزش پایتون - برنامه‌نویسی شیءگرا پیشرفته
# ====================================================

print("lesson name : advanced object-oriented programming")

# ==============================
# مقایسه برنامه‌نویسی تابعی و شیءگرا
# ==============================

print("=== مقایسه برنامه‌نویسی تابعی و شیءگرا ===")

# برنامه‌نویسی تابعی (Functional Programming)
print("--- برنامه‌نویسی تابعی ---")

def calculate_area(width, height):
    """تابع برای محاسبه مساحت مستطیل"""
    return width * height

def calculate_perimeter(width, height):
    """تابع برای محاسبه محیط مستطیل"""
    return 2 * (width + height)

# داده‌ها و توابع جدا از هم هستند
width = 5
height = 3
area = calculate_area(width, height)
perimeter = calculate_perimeter(width, height)

print(f"Rectangle: {width}x{height}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print("-------------------------")

# برنامه‌نویسی شیءگرا (Object-Oriented Programming)
print("--- برنامه‌نویسی شیءگرا ---")

class Rectangle:
    """کلاس مستطیل در برنامه‌نویسی شیءگرا"""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        """محاسبه مساحت"""
        return self.width * self.height
    
    def perimeter(self):
        """محاسبه محیط"""
        return 2 * (self.width + self.height)
    
    def get_info(self):
        """دریافت اطلاعات مستطیل"""
        return f"Rectangle: {self.width}x{self.height} - Area: {self.area()} - Perimeter: {self.perimeter()}"

# ایجاد شیء و استفاده از آن
rect = Rectangle(5, 3)
print(rect.get_info())

print("-------------------------")

# ==============================
# کپسوله‌سازی (Encapsulation)
# ==============================

print("=== کپسوله‌سازی ===")

class BankAccount:
    """کلاس حساب بانکی با کپسوله‌سازی"""
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self._balance = initial_balance  # متغیر محافظت‌شده
        self._transaction_history = []
    
    def deposit(self, amount):
        """واریز به حساب"""
        if amount > 0:
            self._balance += amount
            self._transaction_history.append(f"Deposit: +${amount}")
            return f"Successfully deposited ${amount}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """برداشت از حساب"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_history.append(f"Withdrawal: -${amount}")
            return f"Successfully withdrew ${amount}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """دریافت موجودی (دسترسی کنترل‌شده)"""
        return f"Current balance: ${self._balance}"
    
    def get_transaction_history(self):
        """دریافت تاریخچه تراکنش‌ها"""
        return self._transaction_history
    
    def account_summary(self):
        """خلاصه حساب"""
        summary = f"Account Holder: {self.account_holder}\n"
        summary += f"Balance: ${self._balance}\n"
        summary += f"Transactions: {len(self._transaction_history)}"
        return summary

# استفاده از کلاس بانک
account = BankAccount("Ali Rezaei", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))  # موجودی کافی نیست
print(account.get_balance())
print("Transaction History:", account.get_transaction_history())

print("-------------------------")

# ==============================
# وراثت (Inheritance)
# ==============================

print("=== وراثت ===")

# کلاس والد
class Vehicle:
    """کلاس پایه برای وسایل نقلیه"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self._is_running = False
    
    def start_engine(self):
        """روشن کردن موتور"""
        self._is_running = True
        return f"{self.brand} {self.model} engine started"
    
    def stop_engine(self):
        """خاموش کردن موتور"""
        self._is_running = False
        return f"{self.brand} {self.model} engine stopped"
    
    def get_info(self):
        """دریافت اطلاعات وسیله نقلیه"""
        status = "running" if self._is_running else "stopped"
        return f"{self.year} {self.brand} {self.model} - {status}"

# کلاس فرزند ۱
class Car(Vehicle):
    """کلاس ماشین که از Vehicle ارث می‌برد"""
    
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
    
    def open_trunk(self):
        """باز کردن صندوق"""
        return f"Trunk of {self.brand} {self.model} is open"
    
    def get_info(self):
        """اورراید کردن متد والد"""
        base_info = super().get_info()
        return f"{base_info} - Doors: {self.num_doors}"

# کلاس فرزند ۲
class Motorcycle(Vehicle):
    """کلاس موتورسیکلت که از Vehicle ارث می‌برد"""
    
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
    
    def do_wheelie(self):
        """انجام ویلی"""
        return f"{self.brand} {self.model} is doing a wheelie!"
    
    def get_info(self):
        """اورراید کردن متد والد"""
        base_info = super().get_info()
        sidecar = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"{base_info} - {sidecar}"

# استفاده از کلاس‌ها
car = Car("Toyota", "Camry", 2022, 4)
motorcycle = Motorcycle("Honda", "CBR", 2023, False)

print(car.get_info())
print(car.start_engine())
print(car.open_trunk())

print(motorcycle.get_info())
print(motorcycle.start_engine())
print(motorcycle.do_wheelie())

print("-------------------------")

# ==============================
# انتزاع (Abstraction)
# ==============================

print("=== انتزاع ===")

class CoffeeMachine:
    """ماشین قهوه‌ساز با انتزاع"""
    
    def __init__(self, water_level=1000, coffee_beans=500):
        self.water_level = water_level  # میلی‌لیتر
        self.coffee_beans = coffee_beans  # گرم
        self._is_on = False
    
    def _grind_beans(self):
        """متد خصوصی برای آسیاب کردن دانه‌های قهوه"""
        if self.coffee_beans >= 20:
            self.coffee_beans -= 20
            print("Grinding coffee beans...")
            return True
        print("Not enough coffee beans!")
        return False
    
    def _heat_water(self):
        """متد خصوصی برای گرم کردن آب"""
        if self.water_level >= 200:
            self.water_level -= 200
            print("Heating water...")
            return True
        print("Not enough water!")
        return False
    
    def _brew_coffee(self):
        """متد خصوصی برای دم کردن قهوه"""
        print("Brewing coffee...")
        return "Fresh coffee"
    
    def make_coffee(self):
        """متد اصلی برای درست کردن قهوه (انتزاع)"""
        print("Starting coffee making process...")
        
        if not self._grind_beans():
            return "Coffee making failed: No beans"
        
        if not self._heat_water():
            return "Coffee making failed: No water"
        
        coffee = self._brew_coffee()
        return f"Coffee ready! Enjoy your {coffee}"
    
    def get_status(self):
        """دریافت وضعیت ماشین"""
        return f"Water: {self.water_level}ml, Beans: {self.coffee_beans}g"

# استفاده از ماشین قهوه‌ساز
coffee_machine = CoffeeMachine()
print(coffee_machine.get_status())
print(coffee_machine.make_coffee())
print(coffee_machine.get_status())

print("-------------------------")

# مثال پیچیده‌تر از انتزاع
class Computer:
    """کلاس کامپیوتر با انتزاع پیشرفته"""
    
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage
        self._is_powered_on = False
        self._os_loaded = False
    
    def _power_on(self):
        """متد خصوصی برای روشن کردن سخت‌افزار"""
        print("Powering on hardware...")
        self._is_powered_on = True
        return True
    
    def _load_bios(self):
        """متد خصوصی برای لود کردن BIOS"""
        if self._is_powered_on:
            print("Loading BIOS...")
            return True
        return False
    
    def _load_os(self):
        """متد خصوصی برای لود کردن سیستم عامل"""
        if self._load_bios():
            print("Loading operating system...")
            self._os_loaded = True
            return True
        return False
    
    def _initialize_peripherals(self):
        """متد خصوصی برای راه‌اندازی تجهیزات جانبی"""
        if self._os_loaded:
            print("Initializing peripherals...")
            return True
        return False
    
    def start_computer(self):
        """متد اصلی برای راه‌اندازی کامپیوتر (انتزاع)"""
        print(f"Starting {self.brand} computer...")
        
        if not self._power_on():
            return "Failed to power on"
        
        if not self._load_os():
            return "Failed to load OS"
        
        if not self._initialize_peripherals():
            return "Failed to initialize peripherals"
        
        return "Computer ready to use!"
    
    def get_specs(self):
        """دریافت مشخصات کامپیوتر"""
        return f"{self.brand} - RAM: {self.ram}GB, Storage: {self.storage}GB"

# استفاده از کامپیوتر
my_pc = Computer("Dell", 16, 512)
print(my_pc.get_specs())
print(my_pc.start_computer())

print("-------------------------")

# ==============================
# چندریختی (Polymorphism)
# ==============================

print("=== چندریختی ===")

class Animal:
    """کلاس پایه حیوانات"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """تولید صدا - متد پایه"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def move(self):
        """حرکت کردن - متد پایه"""
        return f"{self.name} is moving"

class Dog(Animal):
    """کلاس سگ"""
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        """تولید صدا - پیاده‌سازی خاص سگ"""
        return f"{self.name} says: Woof!"
    
    def fetch(self):
        """آوردن توپ - متد مخصوص سگ"""
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    """کلاس گربه"""
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def speak(self):
        """تولید صدا - پیاده‌سازی خاص گربه"""
        return f"{self.name} says: Meow!"
    
    def climb(self):
        """بالا رفتن از درخت - متد مخصوص گربه"""
        return f"{self.name} is climbing the tree"

class Bird(Animal):
    """کلاس پرنده"""
    
    def __init__(self, name, can_fly=True):
        super().__init__(name)
        self.can_fly = can_fly
    
    def speak(self):
        """تولید صدا - پیاده‌سازی خاص پرنده"""
        return f"{self.name} says: Tweet!"
    
    def move(self):
        """حرکت کردن - اورراید کردن متد والد"""
        if self.can_fly:
            return f"{self.name} is flying"
        else:
            return f"{self.name} is walking"

# نمایش چندریختی در عمل
animals = [
    Dog("Buddy", "Golden Retriever"),
    Cat("Whiskers", "Gray"),
    Bird("Tweety", True),
    Bird("Penguin", False)
]

print("=== Animal Sounds ===")
for animal in animals:
    print(animal.speak())

print("\n=== Animal Movements ===")
for animal in animals:
    print(animal.move())

print("\n=== Special Abilities ===")
# استفاده از متدهای خاص هر کلاس
dog = animals[0]
cat = animals[1]

print(dog.fetch())
print(cat.climb())

print("-------------------------")

# ==============================
# مثال کاربردی: سیستم مدیریت دانشگاه
# ==============================

print("=== سیستم مدیریت دانشگاه ===")

class UniversityMember:
    """کلاس پایه برای اعضای دانشگاه"""
    
    def __init__(self, name, member_id, department):
        self.name = name
        self.member_id = member_id
        self.department = department
    
    def get_info(self):
        """دریافت اطلاعات عضو"""
        return f"ID: {self.member_id}, Name: {self.name}, Department: {self.department}"
    
    def work(self):
        """کار کردن - متد پایه"""
        raise NotImplementedError("Subclasses must implement this method")

class Student(UniversityMember):
    """کلاس دانشجو"""
    
    def __init__(self, name, student_id, department, year, gpa=0.0):
        super().__init__(name, student_id, department)
        self.year = year
        self.gpa = gpa
        self.courses = []
    
    def enroll_course(self, course_name):
        """ثبت نام در درس"""
        self.courses.append(course_name)
        return f"Enrolled in {course_name}"
    
    def study(self):
        """مطالعه کردن"""
        return f"{self.name} is studying"
    
    def work(self):
        """کار کردن - پیاده‌سازی برای دانشجو"""
        return f"{self.name} is working on assignments"
    
    def get_info(self):
        """اورراید کردن متد والد"""
        base_info = super().get_info()
        return f"{base_info}, Year: {self.year}, GPA: {self.gpa}"

class Professor(UniversityMember):
    """کلاس استاد"""
    
    def __init__(self, name, professor_id, department, specialty, salary):
        super().__init__(name, professor_id, department)
        self.specialty = specialty
        self.salary = salary
        self.courses_teaching = []
    
    def teach_course(self, course_name):
        """تدریس درس"""
        self.courses_teaching.append(course_name)
        return f"Teaching {course_name}"
    
    def conduct_research(self):
        """انجام تحقیق"""
        return f"{self.name} is conducting research in {self.specialty}"
    
    def work(self):
        """کار کردن - پیاده‌سازی برای استاد"""
        return f"{self.name} is teaching and researching"
    
    def get_info(self):
        """اورراید کردن متد والد"""
        base_info = super().get_info()
        return f"{base_info}, Specialty: {self.specialty}, Salary: ${self.salary}"

class Staff(UniversityMember):
    """کلاس کارمند"""
    
    def __init__(self, name, staff_id, department, position):
        super().__init__(name, staff_id, department)
        self.position = position
    
    def perform_duties(self):
        """انجام وظایف"""
        return f"{self.name} is performing {self.position} duties"
    
    def work(self):
        """کار کردن - پیاده‌سازی برای کارمند"""
        return f"{self.name} is working as a {self.position}"
    
    def get_info(self):
        """اورراید کردن متد والد"""
        base_info = super().get_info()
        return f"{base_info}, Position: {self.position}"

# استفاده از سیستم مدیریت دانشگاه
university_members = [
    Student("Ali Mohammadi", "S001", "Computer Science", 3, 3.8),
    Professor("Dr. Smith", "P001", "Mathematics", "Algebra", 75000),
    Staff("Maryam Johnson", "ST001", "Administration", "Secretary"),
    Student("Sara Williams", "S002", "Physics", 2, 3.5)
]

print("=== University Members ===")
for member in university_members:
    print(member.get_info())

print("\n=== Work Activities ===")
for member in university_members:
    print(member.work())

print("\n=== Special Activities ===")
# فعالیت‌های خاص هر کلاس
student = university_members[0]
professor = university_members[1]
staff = university_members[2]

print(student.enroll_course("Advanced Programming"))
print(professor.teach_course("Calculus"))
print(professor.conduct_research())
print(staff.perform_duties())

print("-------------------------")

# ==============================
# تمرین‌های عملی
# ==============================

print("=== تمرین‌های عملی ===")

# تمرین ۱: سیستم شکل‌های هندسی
print("--- سیستم شکل‌های هندسی ---")

class Shape:
    """کلاس پایه برای شکل‌های هندسی"""
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def area(self):
        """محاسبه مساحت"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def perimeter(self):
        """محاسبه محیط"""
        raise NotImplementedError("Subclasses must implement this method")
    
    def describe(self):
        """توصیف شکل"""
        return f"This is a {self.color} {self.name}"

class Circle(Shape):
    """کلاس دایره"""
    
    def __init__(self, radius, color="Red"):
        super().__init__("Circle", color)
        self.radius = radius
    
    def area(self):
        """محاسبه مساحت دایره"""
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        """محاسبه محیط دایره"""
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    """کلاس مستطیل"""
    
    def __init__(self, width, height, color="Blue"):
        super().__init__("Rectangle", color)
        self.width = width
        self.height = height
    
    def area(self):
        """محاسبه مساحت مستطیل"""
        return self.width * self.height
    
    def perimeter(self):
        """محاسبه محیط مستطیل"""
        return 2 * (self.width + self.height)

class Triangle(Shape):
    """کلاس مثلث"""
    
    def __init__(self, base, height, color="Green"):
        super().__init__("Triangle", color)
        self.base = base
        self.height = height
    
    def area(self):
        """محاسبه مساحت مثلث"""
        return 0.5 * self.base * self.height
    
    def perimeter(self):
        """محاسبه محیط مثلث (فرض مثلث متساوی‌الساقین)"""
        # برای سادگی، فرض می‌کنیم مثلث متساوی‌الساقین است
        side = (self.base**2 + self.height**2)**0.5
        return self.base + 2 * side

# تست سیستم شکل‌ها
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Triangle(3, 4)
]

for shape in shapes:
    print(f"{shape.describe()}")
    print(f"Area: {shape.area():.2f}, Perimeter: {shape.perimeter():.2f}")
    print()

print("End of advanced OOP training")