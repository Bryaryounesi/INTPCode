# فایل دهم آموزش پایتون - List Comprehensions و مفاهیم پیشرفته
# =======================================================
print("Lesson: List Comprehensions & Advanced Concepts")
line = "----------------------------"

# ==============================
# 🔥 ضروری: List Comprehensions پایه
# ==============================
print("=== بخش List Comprehensions ===")

# روش سنتی ساخت لیست
prices = [10, 38, 40, 58, 62]  # ضروری
halved = []
for price in prices:
    halved.append(price / 2)
print("Halved prices (traditional):", halved)

# روش List Comprehension
halved_comprehension = [price / 2 for price in prices]  # ضروری
print("Halved prices (comprehension):", halved_comprehension)

# تبدیل متر به کیلومتر
meters = [100, 3800, 4000, 2500]  # ضروری
kilometers = [m / 1000 for m in meters]
print("Kilometers:", kilometers)

# تبدیل درجه سانتیگراد به فارنهایت
celsius = [0, 20, 30, 100]  # ضروری
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Fahrenheit:", fahrenheit)

# محاسبه مربع اعداد
numbers = [1, 2, 3, 4, 5]  # ضروری
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# تبدیل بولین‌ها
answers = [True, False, False, True]  # ضروری
opposites = [not answer for answer in answers]
print("Opposites:", opposites)

# بررسی سن قانونی
ages = [15, 20, 17, 25, 16]  # ضروری
adults = [age >= 18 for age in ages]
print("Adults:", adults)

print(line)

# ==============================
# 🔥 ضروری: توابع در List Comprehensions
# ==============================
print("=== توابع در List Comprehensions ===")

def halve(number):  # ضروری
    return number / 2

prices = [100, 200, 300, 400]
halved_prices = [halve(p) for p in prices]
print("Halved prices with function:", halved_prices)

def apply_tax(price, tax_rate=0.09):  # ضروری
    return price * (1 + tax_rate)

product_prices = [50, 100, 150, 200]
prices_with_tax = [apply_tax(p) for p in product_prices]
print("Prices with tax:", prices_with_tax)

def format_name(full_name):  # ضروری
    parts = full_name.split(" ")
    return f"{parts[1]}, {parts[0]}"

authors = ["Virginia Woolf", "John Steinbeck", "Jane Austen"]
formatted_names = [format_name(a) for a in authors]
print("Formatted names:", formatted_names)

def is_strong_password(password):  # ضروری
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    return has_upper and has_digit and has_special

passwords = ["password", "Password1!", "123456", "Secure@2024"]
password_strength = [is_strong_password(p) for p in passwords]
print("Strength check:", password_strength)

print(line)

# ==============================
# 🔥 ضروری: فیلتر کردن با شرط if
# ==============================
print("=== فیلتر کردن با شرط if ===")

scores = [12, 47, 30, 29, 19, 35, 42]  # ضروری
high_scores = [s for s in scores if s > 20]
print("High scores (>20):", high_scores)

product_prices = [150, 45, 200, 340, 80, 120]  # ضروری
expensive_products = [p for p in product_prices if p > 150]
print("Expensive products (>150):", expensive_products)

websites = ["nytimes.com", "lemonde.fr", "economist.com", "figaro.fr"]  # ضروری
french_sites = [w for w in websites if ".fr" in w]
print("French websites:", french_sites)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # ضروری
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even numbers:", even_numbers)

temperatures = [15, 20, 25, 30, 35, 40]  # ضروری
hot_days_fahrenheit = [(t * 9/5) + 32 for t in temperatures if t > 25]
print("Hot days in Fahrenheit (>25C):", hot_days_fahrenheit)

print(line)

# ==============================
# 🔁 تکراری: Negative Indexing
# ==============================
print("=== Negative Indexing ===")

users = ["Alice", "Bob", "Charlie", "Diana", "Eve"]  # تکراری
print("Last user:", users[-1])
print("Second last user:", users[-2])

colors = ["red", "green", "blue", "yellow"]  # تکراری
colors[-1] = "purple"
colors[-3] = "orange"
print("Modified colors:", colors)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # تکراری
print("Last element of first row:", matrix[0][-1])

print(line)

# ==============================
# 🔁 تکراری: حذف با del
# ==============================
print("=== حذف با دستور del ===")

items = ["apple", "banana", "cherry", "date", "elderberry"]  # تکراری
del items[-1]
del items[1]
print("After del:", items)

student = {"name": "Ali", "age": 20, "major": "CS", "gpa": 3.8}  # تکراری
del student["gpa"]
print("After del student['gpa']:", student)

inventory = ["sword", "shield", "potion", "key", "map"]  # تکراری
if len(inventory) > 3:
    del inventory[-1]
print("After conditional del:", inventory)

print(line)

# ==============================
# 🔁 تکراری: Slice Notation
# ==============================
print("=== Slice Notation ===")

numbers = list(range(10))  # تکراری
print("Slice [2:6]:", numbers[2:6])
print("Slice [::2]:", numbers[::2])

letters = ["A", "B", "C", "D", "E", "F", "G"]  # تکراری
print("Slice [-3:]:", letters[-3:])
print("Slice [:-2]:", letters[:-2])

colors = ["red", "orange", "yellow", "green", "blue"]  # تکراری
print("Reverse slice [::-1]:", colors[::-1])

text = "Hello World Python Programming"  # تکراری
words = text.split()
print("First 2 words:", words[:2])
print("Every second word:", words[::2])

print(line)

# ==============================
# ✅ تمرینی: مثال‌های ترکیبی پیشرفته
# ==============================
print("=== مثال‌های تمرینی ===")

sensor_readings = [23.5, 24.1, 22.8, 25.3, 21.9, 26.7, 20.5, 27.2]  # تمرینی
last_three = sensor_readings[-3:]
average_last_three = sum(last_three) / len(last_three)
normal_readings = [r for r in sensor_readings if 22 <= r <= 26]
print("Normal readings (22-26):", normal_readings)

users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 22, "active": True},
    {"name": "Eve", "age": 16, "active": False}
]  # تمرینی
active_adults = [u for u in users if u["active"] and u["age"] >= 18]
inactive_names = [u["name"] for u in users if not u["active"]]
print("Active adults:", [u["name"] for u in active_adults])
print("Inactive users:", inactive_names)

sentences = [
    "Python is a great programming language.",
    "List comprehensions are very useful.",
    "We love coding in Python!",
    "Data analysis with Python is fun."
]  # تمرینی
word_counts = [len(s.split()) for s in sentences]
python_sentences = [s for s in sentences if "Python" in s]
print("Word counts:", word_counts)
print("Sentences with 'Python':", python_sentences)

print(line)

# ==============================
# ✅ تمرینی: تمرین‌های عملی
# ==============================
print("=== تمرین‌های عملی ===")

# تمرین ۱: تبدیل درجه‌ها
celsius_temps = [-10, 0, 10, 20, 30, 40]  # تمرینی
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print("Celsius to Fahrenheit:", fahrenheit_temps)

# تمرین ۲: فیلتر محصولات
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Book", "price": 20, "category": "education"},
    {"name": "Phone", "price": 500, "category": "electronics"},
    {"name": "Pen", "price": 2, "category": "office"},
    {"name": "Tablet", "price": 300, "category": "electronics"}
]  # تمرینی
cheap_electronics = [
    p["name"] for p in products if p["category"] == "electronics" and p["price"] < 400
]
print("Cheap electronics (<400):", cheap_electronics)

# تمرین ۳: پردازش امتیازات
scores = [85, 92, 78, 96, 88, 76, 95, 89]  # تمرینی
highest = max(scores)
lowest = min(scores)
average_score = sum(scores)/len(scores)
above_average = [s for s in scores if s > average_score]
print("Above average:", above_average)

# تمرین ۴: مدیریت لیست‌ها
data = list(range(1, 21))  # تمرینی
odd_numbers_reversed = [n for n in data if n % 2 == 1][::-1]
print("Odd numbers reversed:", odd_numbers_reversed)

first_third = data[:7]
middle_third = data[7:14]
last_third = data[14:]
print("First third:", first_third)
print("Middle third:", middle_third)
print("Last third:", last_third)

# تمرین ۵: ترکیب مفاهیم
text = "Hello World! This is Python Programming."  # تمرینی
clean_chars = [c.upper() for c in text if c.isalpha()]
long_words = [w for w in text.split() if len(w) > 4]
print("Clean uppercase chars:", "".join(clean_chars))
print("Words longer than 4 chars:", long_words)

print("End of list comprehensions training")