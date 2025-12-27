# فایل نهم آموزش پایتون - تاپل‌ها، دیکشنری‌ها و مجموعه‌ها
# =====================================================

print("lesson name : tuples, dictionaries & sets operations")

# ==============================
# تاپل‌ها (Tuples)
# ==============================

print("=== بخش تاپل‌ها ===")

# ایجاد تاپل‌های ساده
movie_data = ("Inception", 2010, "Christopher Nolan")
print("Movie data tuple:", movie_data)

# تاپل تک عنصری
single_item = ("python",)
print("Single item tuple:", single_item)
print("Type:", type(single_item))

print("-------------------------")

# دسترسی به عناصر تاپل با ایندکس
user_profile = ("john_doe", 30, "Engineer")
print("User profile:", user_profile)
print("Username:", user_profile[0])
print("Age:", user_profile[1])
print("Profession:", user_profile[2])

print("-------------------------")

# تاپل‌ها در لیست‌ها
students_scores = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
print("Students scores:", students_scores)
print("First student:", students_scores[0])
print("Bob's score:", students_scores[1][1])

print("-------------------------")

# تغییرناپذیری تاپل‌ها
colors = ("red", "green", "blue")
print("Original colors:", colors)
# خط زیر خطا می‌دهد:
# colors[0] = "yellow"

print("-------------------------")

# حلقه زدن در تاپل‌ها
coordinates = (10, 20, 30)
print("Coordinates:")
for coord in coordinates:
    print(f"Coordinate: {coord}")

print("-------------------------")

# ==============================
# بازگرداندن تاپل از توابع
# ==============================

def calculate_stats(numbers):
    """تابعی که چند مقدار را در قالب تاپل برمی‌گرداند"""
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

# استفاده از تابع
scores = [85, 92, 78, 96, 88]
stats = calculate_stats(scores)
print("Statistics tuple:", stats)
print(f"Total: {stats[0]}, Average: {stats[1]:.2f}")
print(f"Max: {stats[2]}, Min: {stats[3]}")

print("-------------------------")

# تفکیک مقادیر بازگشتی
total_score, avg_score, max_score, min_score = calculate_stats(scores)
print(f"Unpacked - Total: {total_score}, Avg: {avg_score:.2f}")

print("-------------------------")

# ==============================
# دیکشنری‌ها (Dictionaries)
# ==============================

print("=== بخش دیکشنری‌ها ===")

# ایجاد دیکشنری ساده
student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}
print("Student dictionary:", student)

# دیکشنری خالی
empty_dict = {}
print("Empty dictionary:", empty_dict)

print("-------------------------")

# دسترسی به مقادیر دیکشنری
print("Student name:", student["name"])
print("Student age:", student["age"])

# دسترسی امن با get()
print("Student major:", student.get("major"))
print("Unknown key:", student.get("phone", "Not available"))

print("-------------------------")

# انواع مختلف کلید و مقدار
mixed_dict = {
    "string_key": "string value",
    123: "numeric key",
    True: "boolean key",
    (1, 2): "tuple key"
}
print("Mixed dictionary:", mixed_dict)

print("-------------------------")

# به‌روزرسانی مقادیر
car = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2020
}
print("Original car:", car)
car["year"] = 2022
car["color"] = "blue"  # اضافه کردن کلید جدید
print("Updated car:", car)

print("-------------------------")

# حلقه زدن در دیکشنری
print("Car details:")
for key in car:
    print(f"{key}: {car[key]}")

print("-------------------------")

# روش‌های مختلف حلقه‌زنی
print("Keys only:")
for key in car.keys():
    print(key)

print("Values only:")
for value in car.values():
    print(value)

print("Items (key-value pairs):")
for key, value in car.items():
    print(f"{key}: {value}")

print("-------------------------")

# بررسی وجود کلید
print("Is 'brand' in car?", "brand" in car)
print("Is 'price' in car?", "price" in car)

print("-------------------------")

# حذف از دیکشنری
inventory = {
    "apples": 50,
    "oranges": 30,
    "bananas": 25,
    "grapes": 40
}
print("Original inventory:", inventory)

# حذف با pop
removed_item = inventory.pop("oranges")
print(f"Removed oranges: {removed_item}")
print("After pop:", inventory)

# حذف با popitem
last_item = inventory.popitem()
print(f"Removed last item: {last_item}")
print("After popitem:", inventory)

print("-------------------------")

# ==============================
# مجموعه‌ها (Sets)
# ==============================

print("=== بخش مجموعه‌ها ===")

# ایجاد مجموعه‌ها
programming_languages = {"Python", "Java", "JavaScript", "C++", "Python"}
print("Programming languages set:", programming_languages)  # تکراری‌ها حذف می‌شوند

# مجموعه از لیست
numbers_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
numbers_set = set(numbers_list)
print("Numbers list:", numbers_list)
print("Numbers set:", numbers_set)

print("-------------------------")

# اضافه کردن به مجموعه
fruits = {"apple", "banana"}
print("Original fruits:", fruits)
fruits.add("orange")
fruits.add("apple")  # اضافه نمی‌شود چون تکراری است
print("After adding:", fruits)

print("-------------------------")

# حذف از مجموعه
fruits.remove("banana")
print("After remove:", fruits)

# حذف امن با discard
fruits.discard("grape")  # خطا نمی‌دهد اگر وجود نداشته باشد
print("After discard:", fruits)

print("-------------------------")

# عملیات مجموعه‌ها
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A-B):", set_a.difference(set_b))
print("Difference (B-A):", set_b.difference(set_a))
print("Symmetric Difference:", set_a.symmetric_difference(set_b))

print("-------------------------")

# بررسی زیرمجموعه
set_c = {1, 2, 3}
set_d = {1, 2, 3, 4, 5}
print(f"Is {set_c} subset of {set_d}? {set_c.issubset(set_d)}")
print(f"Is {set_d} superset of {set_c}? {set_d.issuperset(set_c)}")

print("-------------------------")

# ==============================
# مثال‌های کاربردی ترکیبی
# ==============================

print("=== مثال‌های کاربردی ===")

# سیستم مدیریت دانشجویان
students = [
    ("A001", "Alice Johnson", 3.9),
    ("A002", "Bob Smith", 3.7),
    ("A003", "Charlie Brown", 3.5)
]

# تبدیل به دیکشنری برای دسترسی بهتر
students_dict = {}
for student_id, name, gpa in students:
    students_dict[student_id] = {"name": name, "gpa": gpa}

print("Students database:")
for student_id, info in students_dict.items():
    print(f"ID: {student_id}, Name: {info['name']}, GPA: {info['gpa']}")

print("-------------------------")

# سیستم موجودی فروشگاه
inventory_system = {
    "products": {
        "laptop": {"price": 1000, "stock": 15},
        "mouse": {"price": 25, "stock": 50},
        "keyboard": {"price": 75, "stock": 30}
    },
    "categories": {"electronics", "computers", "accessories"}
}

print("Inventory System:")
for product, details in inventory_system["products"].items():
    print(f"Product: {product}")
    print(f"  Price: ${details['price']}")
    print(f"  Stock: {details['stock']}")

print("Categories:", inventory_system["categories"])

print("-------------------------")

# پردازش داده‌های کاربر
user_data = {
    "username": "john_doe",
    "email": "john@example.com",
    "preferences": {"theme": "dark", "language": "en", "notifications": True},
    "friends": {"alice", "bob", "charlie"},
    "activity_log": [("login", "2024-01-15"), ("post", "2024-01-15")]
}

print("User Profile:")
print(f"Username: {user_data['username']}")
print(f"Email: {user_data['email']}")
print(f"Preferences: {user_data['preferences']}")
print(f"Friends: {user_data['friends']}")
print(f"Recent Activity: {user_data['activity_log'][:2]}")

print("-------------------------")

# تحلیل داده با مجموعه‌ها
survey_a = {"python", "java", "javascript", "c++"}
survey_b = {"python", "javascript", "go", "rust"}

common_languages = survey_a.intersection(survey_b)
all_languages = survey_a.union(survey_b)
unique_to_a = survey_a.difference(survey_b)

print("Survey Analysis:")
print(f"Common languages: {common_languages}")
print(f"All languages: {all_languages}")
print(f"Unique to survey A: {unique_to_a}")

print("-------------------------")

# ==============================
# تمرین‌های عملی
# ==============================

print("=== تمرین‌های عملی ===")

# تمرین 1: مدیریت مخاطبین
contacts = {
    "ali": {"phone": "09123456789", "email": "ali@example.com"},
    "sara": {"phone": "09129876543", "email": "sara@example.com"}
}

# اضافه کردن مخاطب جدید
contacts["reza"] = {"phone": "09121112233", "email": "reza@example.com"}
print("Contacts after adding Reza:", contacts)

# حذف مخاطب
if "sara" in contacts:
    removed_contact = contacts.pop("sara")
    print(f"Removed contact: Sara - {removed_contact}")

print("Final contacts:", contacts)

print("-------------------------")

# تمرین 2: سیستم رأی‌گیری
votes = ["candidate_a", "candidate_b", "candidate_a", "candidate_c", "candidate_b", "candidate_a"]
unique_voters = set(votes)
print("Votes:", votes)
print("Unique voters:", unique_voters)
print("Total unique votes:", len(unique_voters))

print("-------------------------")

# تمرین 3: تبدیل داده‌ها
# تبدیل لیست تاپل‌ها به دیکشنری
employee_tuples = [("e001", "John", 50000), ("e002", "Jane", 60000)]
employee_dict = {emp[0]: {"name": emp[1], "salary": emp[2]} for emp in employee_tuples}
print("Employee tuples:", employee_tuples)
print("Employee dictionary:", employee_dict)

print("-------------------------")

# تمرین 4: عملیات پیشرفته مجموعه‌ها
group1 = {"math", "physics", "chemistry"}
group2 = {"biology", "physics", "computer science"}
group3 = {"math", "computer science", "statistics"}

# دروس مشترک بین همه گروه‌ها
common_courses = group1.intersection(group2, group3)
print("Common courses in all groups:", common_courses)

# تمام دروس منحصر به فرد
all_unique_courses = group1.union(group2, group3)
print("All unique courses:", all_unique_courses)

print("End of tuples, dictionaries & sets training")