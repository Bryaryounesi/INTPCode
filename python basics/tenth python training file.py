# فایل دهم آموزش پایتون - List Comprehensions و مفاهیم پیشرفته
# =======================================================

print("lesson name : list comprehensions & advanced concepts")

# ==============================
# List Comprehensions (خلاصه‌سازی لیست)
# ==============================

print("=== بخش List Comprehensions ===")

# روش سنتی ساخت لیست جدید
print("--- روش سنتی ---")
prices = [10, 38, 40, 58, 62]
halved = []
for price in prices:
    half_price = price / 2
    halved.append(half_price)
print("Original prices:", prices)
print("Halved prices (traditional):", halved)

print("-------------------------")

# روش List Comprehension
print("--- روش List Comprehension ---")
halved_comprehension = [price / 2 for price in prices]
print("Halved prices (comprehension):", halved_comprehension)

print("-------------------------")

# مثال‌های مختلف List Comprehension
print("--- مثال‌های مختلف ---")

# تبدیل متر به کیلومتر
meters = [100, 3800, 4000, 2500]
kilometers = [m / 1000 for m in meters]
print("Meters:", meters)
print("Kilometers:", kilometers)

print("-------------------------")

# تبدیل درجه سانتیگراد به فارنهایت
celsius = [0, 20, 30, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

print("-------------------------")

# محاسبه مربع اعداد
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("Numbers:", numbers)
print("Squares:", squares)

print("-------------------------")

# تبدیل بولین‌ها
answers = [True, False, False, True]
opposites = [not answer for answer in answers]
print("Answers:", answers)
print("Opposites:", opposites)

print("-------------------------")

# بررسی سن قانونی
ages = [15, 20, 17, 25, 16]
adults = [age >= 18 for age in ages]
print("Ages:", ages)
print("Adults:", adults)

print("-------------------------")

# ==============================
# استفاده از توابع در List Comprehensions
# ==============================

print("=== توابع در List Comprehensions ===")

# تابع ساده برای تقسیم
def halve(number):
    return number / 2

prices = [100, 200, 300, 400]
halved_prices = [halve(price) for price in prices]
print("Prices:", prices)
print("Halved prices with function:", halved_prices)

print("-------------------------")

# تابع برای اعمال مالیات
def apply_tax(price, tax_rate=0.09):
    return price * (1 + tax_rate)

product_prices = [50, 100, 150, 200]
prices_with_tax = [apply_tax(price) for price in product_prices]
print("Product prices:", product_prices)
print("Prices with tax:", prices_with_tax)

print("-------------------------")

# تابع برای فرمت‌بندی نام
def format_name(full_name):
    parts = full_name.split(" ")
    return f"{parts[1]}, {parts[0]}"

authors = ["Virginia Woolf", "John Steinbeck", "Jane Austen"]
formatted_names = [format_name(author) for author in authors]
print("Original names:", authors)
print("Formatted names:", formatted_names)

print("-------------------------")

# تابع برای بررسی شرایط خاص
def is_strong_password(password):
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*" for char in password)
    return has_upper and has_digit and has_special

passwords = ["password", "Password1!", "123456", "Secure@2024"]
password_strength = [is_strong_password(pwd) for pwd in passwords]
print("Passwords:", passwords)
print("Strength check:", password_strength)

print("-------------------------")

# ==============================
# فیلتر کردن با شرط if
# ==============================

print("=== فیلتر کردن با شرط if ===")

# فیلتر اعداد بزرگتر از ۲۰
scores = [12, 47, 30, 29, 19, 35, 42]
high_scores = [score for score in scores if score > 20]
print("All scores:", scores)
print("High scores (>20):", high_scores)

print("-------------------------")

# فیلتر قیمت‌های بالای ۱۵۰
product_prices = [150, 45, 200, 340, 80, 120]
expensive_products = [price for price in product_prices if price > 150]
print("All prices:", product_prices)
print("Expensive products (>150):", expensive_products)

print("-------------------------")

# فیلتر وبسایت‌های فرانسوی
websites = ["nytimes.com", "lemonde.fr", "economist.com", "figaro.fr"]
french_sites = [site for site in websites if ".fr" in site]
print("All websites:", websites)
print("French websites:", french_sites)

print("-------------------------")

# فیلتر اعداد زوج
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("All numbers:", numbers)
print("Even numbers:", even_numbers)

print("-------------------------")

# فیلتر ترکیبی با تغییر و شرط
temperatures = [15, 20, 25, 30, 35, 40]
hot_days_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures if temp > 25]
print("Temperatures (C):", temperatures)
print("Hot days in Fahrenheit (>25C):", hot_days_fahrenheit)

print("-------------------------")

# ==============================
# Negative Indexing
# ==============================

print("=== Negative Indexing ===")

# دسترسی به عناصر با ایندکس منفی
users = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print("Users list:", users)
print("Last user (index -1):", users[-1])
print("Second last user (index -2):", users[-2])
print("First user (index -5):", users[-5])

print("-------------------------")

# تغییر عناصر با ایندکس منفی
colors = ["red", "green", "blue", "yellow"]
print("Original colors:", colors)
colors[-1] = "purple"
colors[-3] = "orange"
print("Modified colors:", colors)

print("-------------------------")

# استفاده در لیست‌های تو در تو
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matrix:", matrix)
print("Last element of first row:", matrix[0][-1])
print("First element of last row:", matrix[-1][0])

print("-------------------------")

# ==============================
# حذف با دستور del
# ==============================

print("=== حذف با دستور del ===")

# حذف عناصر از لیست
items = ["apple", "banana", "cherry", "date", "elderberry"]
print("Original items:", items)

del items[-1]  # حذف آخرین عنصر
print("After del items[-1]:", items)

del items[1]   # حذف عنصر دوم
print("After del items[1]:", items)

print("-------------------------")

# حذف از دیکشنری
student = {
    "name": "Ali",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print("Original student:", student)
del student["gpa"]
print("After del student['gpa']:", student)

print("-------------------------")

# حذف شرطی
inventory = ["sword", "shield", "potion", "key", "map"]
print("Original inventory:", inventory)
if len(inventory) > 3:
    del inventory[-1]
    print("After conditional del:", inventory)

print("-------------------------")

# ==============================
# Slice Notation (برش لیست)
# ==============================

print("=== Slice Notation ===")

# برش ساده
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("All numbers:", numbers)
print("Slice [2:6]:", numbers[2:6])
print("Slice [:4]:", numbers[:4])
print("Slice [7:]:", numbers[7:])
print("Slice [::2]:", numbers[::2])  # یک در میان
print("Slice [1::2]:", numbers[1::2])  # از عنصر دوم، یک در میان

print("-------------------------")

# برش با ایندکس منفی
letters = ["A", "B", "C", "D", "E", "F", "G"]
print("Letters:", letters)
print("Slice [-3:]:", letters[-3:])  # سه عنصر آخر
print("Slice [:-2]:", letters[:-2])  # همه به جز دو عنصر آخر
print("Slice [-4:-1]:", letters[-4:-1])  # از منفی چهارم تا منفی دوم

print("-------------------------")

# برش معکوس
colors = ["red", "orange", "yellow", "green", "blue"]
print("Colors:", colors)
print("Reverse slice [::-1]:", colors[::-1])  # معکوس کامل
print("Reverse slice [3:0:-1]:", colors[3:0:-1])  # از سبز تا نارنجی
print("Reverse slice [::-2]:", colors[::-2])  # معکوس، یک در میان

print("-------------------------")

# کاربردهای عملی برش
text = "Hello World Python Programming"
words = text.split()
print("Text:", text)
print("First 2 words:", words[:2])
print("Last 2 words:", words[-2:])
print("Every second word:", words[::2])

print("-------------------------")

# ==============================
# مثال‌های ترکیبی پیشرفته
# ==============================

print("=== مثال‌های ترکیبی پیشرفته ===")

# پردازش داده‌های سنسور
sensor_readings = [23.5, 24.1, 22.8, 25.3, 21.9, 26.7, 20.5, 27.2]
print("All readings:", sensor_readings)

# میانگین ۳ خوانش آخر
last_three = sensor_readings[-3:]
average_last_three = sum(last_three) / len(last_three)
print("Last three readings:", last_three)
print("Average of last three:", f"{average_last_three:.2f}")

# فیلتر خوانش‌های نرمال (بین ۲۲ تا ۲۶)
normal_readings = [reading for reading in sensor_readings if 22 <= reading <= 26]
print("Normal readings (22-26):", normal_readings)

print("-------------------------")

# سیستم مدیریت کاربران
users = [
    {"name": "Alice", "age": 25, "active": True},
    {"name": "Bob", "age": 17, "active": True},
    {"name": "Charlie", "age": 30, "active": False},
    {"name": "Diana", "age": 22, "active": True},
    {"name": "Eve", "age": 16, "active": False}
]

# کاربران فعال بالای ۱۸ سال
active_adults = [user for user in users if user["active"] and user["age"] >= 18]
print("Active adult users:")
for user in active_adults:
    print(f"  - {user['name']} ({user['age']} years old)")

# نام کاربران غیرفعال
inactive_names = [user["name"] for user in users if not user["active"]]
print("Inactive users:", inactive_names)

print("-------------------------")

# پردازش متن
sentences = [
    "Python is a great programming language.",
    "List comprehensions are very useful.",
    "We love coding in Python!",
    "Data analysis with Python is fun."
]

# تعداد کلمات در هر جمله
word_counts = [len(sentence.split()) for sentence in sentences]
print("Sentences:", sentences)
print("Word counts:", word_counts)

# جملاتی که کلمه "Python" دارند
python_sentences = [sentence for sentence in sentences if "Python" in sentence]
print("Sentences with 'Python':", python_sentences)

print("-------------------------")

# ==============================
# تمرین‌های عملی
# ==============================

print("=== تمرین‌های عملی ===")

# تمرین ۱: تبدیل درجه‌ها
celsius_temps = [-10, 0, 10, 20, 30, 40]
fahrenheit_temps = [(c * 9/5) + 32 for c in celsius_temps]
print("Celsius to Fahrenheit:")
for c, f in zip(celsius_temps, fahrenheit_temps):
    print(f"  {c}°C = {f:.1f}°F")

print("-------------------------")

# تمرین ۲: فیلتر محصولات
products = [
    {"name": "Laptop", "price": 1000, "category": "electronics"},
    {"name": "Book", "price": 20, "category": "education"},
    {"name": "Phone", "price": 500, "category": "electronics"},
    {"name": "Pen", "price": 2, "category": "office"},
    {"name": "Tablet", "price": 300, "category": "electronics"}
]

# محصولات الکترونیکی ارزان (زیر ۴۰۰)
cheap_electronics = [
    product["name"] for product in products 
    if product["category"] == "electronics" and product["price"] < 400
]
print("Cheap electronics (<400):", cheap_electronics)

print("-------------------------")

# تمرین ۳: پردازش امتیازات
scores = [85, 92, 78, 96, 88, 76, 95, 89]
print("All scores:", scores)

# بالاترین و پایین‌ترین امتیاز
highest = max(scores)
lowest = min(scores)
print(f"Highest: {highest}, Lowest: {lowest}")

# امتیازات بالاتر از میانگین
average_score = sum(scores) / len(scores)
above_average = [score for score in scores if score > average_score]
print(f"Average: {average_score:.2f}")
print("Above average:", above_average)

print("-------------------------")

# تمرین ۴: مدیریت لیست‌ها
data = list(range(1, 21))  # اعداد ۱ تا ۲۰
print("Original data (1-20):", data)

# اعداد فرد معکوس
odd_numbers_reversed = [num for num in data if num % 2 == 1][::-1]
print("Odd numbers reversed:", odd_numbers_reversed)

# برش‌های مختلف
first_third = data[:7]
middle_third = data[7:14]
last_third = data[14:]
print("First third:", first_third)
print("Middle third:", middle_third)
print("Last third:", last_third)

print("-------------------------")

# تمرین ۵: ترکیب مفاهیم
text = "Hello World! This is Python Programming."
print("Original text:", text)

# کاراکترهای الفبا به حروف بزرگ (به جز فاصله و علائم)
clean_chars = [char.upper() for char in text if char.isalpha()]
print("Clean uppercase chars:", "".join(clean_chars))

# کلمات با طول بیشتر از ۴ حرف
words = text.split()
long_words = [word for word in words if len(word) > 4]
print("Words longer than 4 chars:", long_words)

print("End of list comprehensions training")