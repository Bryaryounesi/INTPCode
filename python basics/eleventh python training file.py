# فایل یازدهم آموزش پایتون - کلاس‌ها و برنامه‌نویسی شیءگرا
# ===================================================

print("lesson name : classes & object-oriented programming")

# ==============================
# مقدمه‌ای بر برنامه‌نویسی شیءگرا
# ==============================

print("=== مفاهیم پایه برنامه‌نویسی شیءگرا ===")

# تعریف یک کلاس ساده
class Person:
    """یک کلاس ساده برای نمایش یک شخص"""
    
    # متغیرهای کلاس (Class Attributes)
    species = "Human"
    planet = "Earth"
    
    def __init__(self, name, age):
        # متغیرهای نمونه (Instance Attributes)
        self.name = name
        self.age = age
    
    # متدهای نمونه (Instance Methods)
    def introduce(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."
    
    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday! Now I'm {self.age} years old."

print("-------------------------")

# ایجاد نمونه‌هایی از کلاس
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())

print("-------------------------")

# دسترسی به متغیرهای کلاس و نمونه
print(f"Person1 name: {person1.name}")
print(f"Person2 age: {person2.age}")
print(f"All humans are: {Person.species}")
print(f"Person1 species: {person1.species}")

print("-------------------------")

# ==============================
# کلاس‌های پایه و نمونه‌سازی
# ==============================

print("=== کلاس‌های پایه و نمونه‌سازی ===")

class Car:
    """کلاسی برای نمایش خودرو"""
    
    # متغیرهای کلاس
    wheels = 4
    vehicle_type = "Land Vehicle"
    
    def __init__(self, brand, model, color):
        # متغیرهای نمونه
        self.brand = brand
        self.model = model
        self.color = color
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        return f"{self.brand} {self.model} engine started!"
    
    def stop_engine(self):
        self.is_running = False
        return f"{self.brand} {self.model} engine stopped!"
    
    def get_info(self):
        status = "running" if self.is_running else "stopped"
        return f"{self.color} {self.brand} {self.model} - {status}"

# ایجاد نمونه‌ها
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

print(car1.get_info())
print(car2.get_info())

print(car1.start_engine())
print(car1.get_info())

print("-------------------------")

# ==============================
# متدها و ویژگی‌ها
# ==============================

print("=== متدها و ویژگی‌ها ===")

class BankAccount:
    """کلاسی برای نمایش حساب بانکی"""
    
    bank_name = "Python Bank"
    interest_rate = 0.05
    
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()
    
    def _generate_account_number(self):
        """متد خصوصی برای تولید شماره حساب"""
        import random
        return f"ACC{random.randint(10000, 99999)}"
    
    def deposit(self, amount):
        """واریز به حساب"""
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"
    
    def withdraw(self, amount):
        """برداشت از حساب"""
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """دریافت موجودی"""
        return f"Balance: ${self.balance}"
    
    def apply_interest(self):
        """اعمال سود"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}"

# استفاده از کلاس حساب بانکی
account1 = BankAccount("Ali", 1000)
account2 = BankAccount("Sara", 500)

print(account1.deposit(200))
print(account1.withdraw(300))
print(account1.apply_interest())
print(account1.get_balance())

print("-------------------------")

# ==============================
# متد سازنده و پارامترهای اختیاری
# ==============================

print("=== متد سازنده و پارامترهای اختیاری ===")

class Student:
    """کلاسی برای نمایش دانشجو"""
    
    def __init__(self, name, student_id, major="Computer Science", year=1):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.year = year
        self.courses = []
    
    def enroll_course(self, course_name):
        """ثبت نام در درس"""
        self.courses.append(course_name)
        return f"Enrolled in {course_name}"
    
    def drop_course(self, course_name):
        """حذف درس"""
        if course_name in self.courses:
            self.courses.remove(course_name)
            return f"Dropped {course_name}"
        return f"Not enrolled in {course_name}"
    
    def get_info(self):
        """دریافت اطلاعات دانشجو"""
        return f"Student: {self.name} (ID: {self.student_id})\nMajor: {self.major}, Year: {self.year}\nCourses: {', '.join(self.courses) if self.courses else 'None'}"

# ایجاد دانشجوها با پارامترهای مختلف
student1 = Student("Mohammad", "S001", "Mathematics", 2)
student2 = Student("Fatemeh", "S002")  # استفاده از مقادیر پیش‌فرض

student1.enroll_course("Calculus")
student1.enroll_course("Physics")
student2.enroll_course("Programming")

print(student1.get_info())
print(student2.get_info())

print("-------------------------")

# ==============================
# کار با لیست‌ها و ساختارهای داده در کلاس
# ==============================

print("=== کار با لیست‌ها در کلاس ===")

class ShoppingCart:
    """کلاسی برای نمایش سبد خرید"""
    
    def __init__(self, owner):
        self.owner = owner
        self.items = []
        self.total_price = 0
    
    def add_item(self, item_name, price):
        """افزودن آیتم به سبد خرید"""
        self.items.append({"name": item_name, "price": price})
        self.total_price += price
        return f"Added {item_name} for ${price}"
    
    def remove_item(self, item_name):
        """حذف آیتم از سبد خرید"""
        for item in self.items:
            if item["name"] == item_name:
                self.total_price -= item["price"]
                self.items.remove(item)
                return f"Removed {item_name}"
        return f"Item {item_name} not found in cart"
    
    def show_cart(self):
        """نمایش محتوای سبد خرید"""
        if not self.items:
            return "Cart is empty"
        
        cart_content = f"{self.owner}'s Shopping Cart:\n"
        for i, item in enumerate(self.items, 1):
            cart_content += f"{i}. {item['name']} - ${item['price']}\n"
        cart_content += f"Total: ${self.total_price}"
        return cart_content
    
    def clear_cart(self):
        """پاک کردن سبد خرید"""
        self.items.clear()
        self.total_price = 0
        return "Cart cleared"

# استفاده از سبد خرید
cart = ShoppingCart("Reza")
cart.add_item("Laptop", 1000)
cart.add_item("Mouse", 25)
cart.add_item("Keyboard", 75)

print(cart.show_cart())
print(cart.remove_item("Mouse"))
print(cart.show_cart())

print("-------------------------")

# ==============================
# متدهای پیشرفته و قابلیت‌های کلاس
# ==============================

print("=== متدهای پیشرفته ===")

class Book:
    """کلاسی برای نمایش کتاب"""
    
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.is_available = True
    
    def __str__(self):
        """متد ویژه برای نمایش رشته‌ای شیء"""
        status = "Available" if self.is_available else "Borrowed"
        return f"'{self.title}' by {self.author} - {self.pages} pages - ${self.price} - {status}"
    
    def __len__(self):
        """متد ویژه برای بازگرداندن طول کتاب"""
        return self.pages
    
    def borrow(self):
        """امانت گرفتن کتاب"""
        if self.is_available:
            self.is_available = False
            return f"'{self.title}' has been borrowed"
        return f"'{self.title}' is already borrowed"
    
    def return_book(self):
        """برگرداندن کتاب"""
        if not self.is_available:
            self.is_available = True
            return f"'{self.title}' has been returned"
        return f"'{self.title}' was not borrowed"
    
    def apply_discount(self, percent):
        """اعمال تخفیف"""
        discount = self.price * (percent / 100)
        self.price -= discount
        return f"Applied {percent}% discount. New price: ${self.price:.2f}"

# استفاده از کلاس کتاب
book1 = Book("Python Programming", "John Smith", 350, 45.99)
book2 = Book("Data Science", "Jane Doe", 500, 60.00)

print(book1)
print(book2)
print(f"Book1 length: {len(book1)} pages")

print(book1.borrow())
print(book1.borrow())  # تلاش برای امانت گرفتن دوباره
print(book1.return_book())

print(book1.apply_discount(10))
print(book1)

print("-------------------------")

# ==============================
# مثال کاربردی: سیستم مدیریت کتابخانه
# ==============================

print("=== سیستم مدیریت کتابخانه ===")

class Library:
    """کلاسی برای مدیریت کتابخانه"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []
    
    def add_book(self, book):
        """افزودن کتاب به کتابخانه"""
        self.books.append(book)
        return f"Added '{book.title}' to library"
    
    def remove_book(self, book_title):
        """حذف کتاب از کتابخانه"""
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return f"Removed '{book_title}' from library"
        return f"Book '{book_title}' not found"
    
    def register_member(self, member_name):
        """ثبت نام عضو جدید"""
        self.members.append(member_name)
        return f"Registered new member: {member_name}"
    
    def find_available_books(self):
        """یافتن کتاب‌های موجود"""
        available_books = [book for book in self.books if book.is_available]
        if not available_books:
            return "No available books"
        
        result = f"Available books in {self.name}:\n"
        for book in available_books:
            result += f"- {book}\n"
        return result
    
    def borrow_book(self, member_name, book_title):
        """امانت دادن کتاب"""
        # بررسی وجود عضو
        if member_name not in self.members:
            return f"Member {member_name} not registered"
        
        # یافتن کتاب
        for book in self.books:
            if book.title == book_title:
                if book.is_available:
                    return book.borrow()
                else:
                    return f"'{book_title}' is already borrowed"
        
        return f"Book '{book_title}' not found in library"

# ایجاد کتابخانه و تست آن
library = Library("Central Library")

# افزودن کتاب‌ها
library.add_book(book1)
library.add_book(book2)
library.add_book(Book("Algorithms", "Robert Sedgewick", 800, 75.00))

# ثبت نام اعضا
library.register_member("Ali")
library.register_member("Maryam")

print(library.find_available_books())
print(library.borrow_book("Ali", "Python Programming"))
print(library.borrow_book("Mohammad", "Data Science"))  # عضو ثبت‌نام نکرده
print(library.find_available_books())

print("-------------------------")

# ==============================
# تمرین‌های عملی
# ==============================

print("=== تمرین‌های عملی ===")

# تمرین ۱: کلاس ماشین حساب
class Calculator:
    """کلاس ماشین حساب ساده"""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        result = a / b
        self.history.append(f"{a} ÷ {b} = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            return "No calculations yet"
        return "\n".join(self.history)
    
    def clear_history(self):
        self.history.clear()
        return "History cleared"

# تست ماشین حساب
calc = Calculator()
print("Calculator Operations:")
print(f"5 + 3 = {calc.add(5, 3)}")
print(f"10 - 4 = {calc.subtract(10, 4)}")
print(f"6 × 7 = {calc.multiply(6, 7)}")
print(f"15 ÷ 3 = {calc.divide(15, 3)}")
print("\nCalculation History:")
print(calc.show_history())

print("-------------------------")

# تمرین ۲: کلاس پروفایل کاربر
class UserProfile:
    """کلاس پروفایل کاربر"""
    
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.posts = []
        self.friends = []
    
    def create_post(self, content):
        """ایجاد پست جدید"""
        post = {
            "content": content,
            "timestamp": self._get_timestamp(),
            "likes": 0
        }
        self.posts.append(post)
        return f"New post created by {self.username}"
    
    def like_post(self, post_index):
        """لایک کردن پست"""
        if 0 <= post_index < len(self.posts):
            self.posts[post_index]["likes"] += 1
            return f"Post {post_index + 1} liked!"
        return "Invalid post index"
    
    def add_friend(self, friend_username):
        """افزودن دوست"""
        if friend_username not in self.friends:
            self.friends.append(friend_username)
            return f"Added {friend_username} as friend"
        return f"{friend_username} is already a friend"
    
    def get_profile_info(self):
        """دریافت اطلاعات پروفایل"""
        info = f"Username: {self.username}\n"
        info += f"Email: {self.email}\n"
        info += f"Posts: {len(self.posts)}\n"
        info += f"Friends: {len(self.friends)}\n"
        info += f"Total likes: {sum(post['likes'] for post in self.posts)}"
        return info
    
    def _get_timestamp(self):
        """متد خصوصی برای تولید timestamp"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# تست پروفایل کاربر
user = UserProfile("john_doe", "john@example.com")
user.create_post("Hello world! This is my first post.")
user.create_post("Learning Python is fun!")
user.add_friend("alice")
user.add_friend("bob")

user.like_post(0)
user.like_post(0)
user.like_post(1)

print(user.get_profile_info())

print("-------------------------")

# تمرین ۳: کلاس شکل‌های هندسی
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
    
    def get_info(self):
        return f"{self.color} {self.name} - Area: {self.area():.2f}, Perimeter: {self.perimeter():.2f}"

class Rectangle(Shape):
    """کلاس مستطیل"""
    
    def __init__(self, width, height, color="Blue"):
        super().__init__("Rectangle", color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    """کلاس دایره"""
    
    def __init__(self, radius, color="Red"):
        super().__init__("Circle", color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius

# تست شکل‌های هندسی
rect = Rectangle(5, 3, "Green")
circle = Circle(4, "Yellow")

print(rect.get_info())
print(circle.get_info())

print("End of classes training")