# فایل نهم آموزش پایتون - تاپل‌ها، دیکشنری‌ها و مجموعه‌ها
# =====================================================
print("Lesson: Tuples, Dictionaries & Sets")
line = "----------------------------"

# ==============================
# 🔥 ضروری: تاپل‌ها (Tuples)
# ==============================
print("=== بخش تاپل‌ها ===")

# ایجاد تاپل‌های ساده
movie_data = ("Inception", 2010, "Christopher Nolan")  # ضروری
print("Movie data tuple:", movie_data)

# تاپل تک عنصری
single_item = ("Python",)  # ضروری
print("Single item tuple:", single_item)
print("Type:", type(single_item))

# دسترسی به عناصر تاپل با ایندکس
user_profile = ("john_doe", 30, "Engineer")  # ضروری
print("Username:", user_profile[0])
print("Age:", user_profile[1])
print("Profession:", user_profile[2])

# تاپل‌ها در لیست‌ها
students_scores = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]  # ضروری
print("Bob's score:", students_scores[1][1])

# حلقه زدن در تاپل‌ها
coordinates = (10, 20, 30)  # ضروری
for coord in coordinates:
    print(f"Coordinate: {coord}")

print(line)

# ==============================
# 🔥 ضروری: بازگرداندن تاپل از توابع
# ==============================
def calculate_stats(numbers):  # ضروری
    """تابعی که چند مقدار را در قالب تاپل برمی‌گرداند"""
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

scores = [85, 92, 78, 96, 88]
stats = calculate_stats(scores)  # ضروری
print("Statistics tuple:", stats)

# تفکیک مقادیر بازگشتی
total_score, avg_score, max_score, min_score = calculate_stats(scores)  # ضروری
print(f"Unpacked - Total: {total_score}, Avg: {avg_score:.2f}")

print(line)

# ==============================
# 🔥 ضروری: دیکشنری‌ها (Dictionaries)
# ==============================
print("=== بخش دیکشنری‌ها ===")

# ایجاد دیکشنری ساده
student = {"name": "Ali", "age": 22, "major": "CS", "gpa": 3.8}  # ضروری
print("Student dictionary:", student)

# دسترسی به مقادیر دیکشنری
print("Student name:", student["name"])  # ضروری
print("Student major:", student.get("major"))  # ضروری

# به‌روزرسانی مقادیر و اضافه کردن کلید جدید
car = {"brand": "Toyota", "model": "Camry", "year": 2020}  # ضروری
car["year"] = 2022
car["color"] = "blue"
print("Updated car:", car)

# حلقه زدن در دیکشنری
for key, value in car.items():  # ضروری
    print(f"{key}: {value}")

# بررسی وجود کلید
print("Is 'brand' in car?", "brand" in car)  # ضروری
print("Is 'price' in car?", "price" in car)  # ضروری

# حذف از دیکشنری
inventory = {"apples": 50, "oranges": 30, "bananas": 25, "grapes": 40}  # ضروری
removed_item = inventory.pop("oranges")
print("After pop:", inventory)
last_item = inventory.popitem()
print("After popitem:", inventory)

print(line)

# ==============================
# 🔥 ضروری: مجموعه‌ها (Sets)
# ==============================
print("=== بخش مجموعه‌ها ===")

# ایجاد مجموعه‌ها
programming_languages = {"Python", "Java", "JavaScript", "C++", "Python"}  # ضروری
print("Programming languages set:", programming_languages)

# مجموعه از لیست
numbers_list = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
numbers_set = set(numbers_list)  # ضروری
print("Numbers set:", numbers_set)

# اضافه کردن و حذف عناصر
fruits = {"apple", "banana"}  # ضروری
fruits.add("orange")
fruits.remove("banana")
fruits.discard("grape")  # خطا نمی‌دهد اگر وجود نداشته باشد
print("Fruits set:", fruits)

# عملیات مجموعه‌ها
set_a = {1, 2, 3, 4, 5}  # ضروری
set_b = {4, 5, 6, 7, 8}
print("Union:", set_a.union(set_b))
print("Intersection:", set_a.intersection(set_b))
print("Difference (A-B):", set_a.difference(set_b))
print("Symmetric Difference:", set_a.symmetric_difference(set_b))

# بررسی زیرمجموعه و مازاد
set_c = {1, 2, 3}
set_d = {1, 2, 3, 4, 5}
print(f"Is {set_c} subset of {set_d}? {set_c.issubset(set_d)}")
print(f"Is {set_d} superset of {set_c}? {set_d.issuperset(set_c)}")

print(line)

# ==============================
# ✅ تمرینی: مثال‌های کاربردی ترکیبی
# ==============================
# سیستم مدیریت دانشجویان
students = [("A001", "Alice Johnson", 3.9),
            ("A002", "Bob Smith", 3.7),
            ("A003", "Charlie Brown", 3.5)]
students_dict = {sid: {"name": name, "gpa": gpa} for sid, name, gpa in students}
for sid, info in students_dict.items():
    print(f"ID: {sid}, Name: {info['name']}, GPA: {info['gpa']}")

# سیستم موجودی فروشگاه
inventory_system = {
    "products": {
        "laptop": {"price": 1000, "stock": 15},
        "mouse": {"price": 25, "stock": 50},
    },
    "categories": {"electronics", "computers"}
}
for product, details in inventory_system["products"].items():
    print(f"{product} -> Price: {details['price']}, Stock: {details['stock']}")
print("Categories:", inventory_system["categories"])

# پردازش داده‌های کاربر
user_data = {
    "username": "john_doe",
    "friends": {"alice", "bob", "charlie"},
    "activity_log": [("login", "2024-01-15"), ("post", "2024-01-15")]
}
print("Friends:", user_data["friends"])
print("Recent Activity:", user_data["activity_log"][:2])

# تحلیل داده با مجموعه‌ها
survey_a = {"python", "java", "javascript", "c++"}
survey_b = {"python", "javascript", "go", "rust"}
print("Common languages:", survey_a.intersection(survey_b))
print("All languages:", survey_a.union(survey_b))
print("Unique to survey A:", survey_a.difference(survey_b))

print(line)

# ==============================
# ✅ تمرینی: تمرین‌های عملی
# ==============================
# تمرین 1: مدیریت مخاطبین
contacts = {
    "ali": {"phone": "09123456789", "email": "ali@example.com"},
    "sara": {"phone": "09129876543", "email": "sara@example.com"}
}
contacts["reza"] = {"phone": "09121112233", "email": "reza@example.com"}
if "sara" in contacts:
    removed_contact = contacts.pop("sara")
print("Final contacts:", contacts)

# تمرین 2: سیستم رأی‌گیری
votes = ["candidate_a", "candidate_b", "candidate_a", "candidate_c"]
unique_voters = set(votes)
print("Total unique votes:", len(unique_voters))

# تمرین 3: تبدیل داده‌ها
employee_tuples = [("e001", "John", 50000), ("e002", "Jane", 60000)]
employee_dict = {emp[0]: {"name": emp[1], "salary": emp[2]} for emp in employee_tuples}
print("Employee dictionary:", employee_dict)

# تمرین 4: عملیات پیشرفته مجموعه‌ها
group1 = {"math", "physics", "chemistry"}
group2 = {"biology", "physics", "computer science"}
group3 = {"math", "computer science", "statistics"}
common_courses = group1.intersection(group2, group3)
all_unique_courses = group1.union(group2, group3)
print("Common courses:", common_courses)
print("All unique courses:", all_unique_courses)

print("End of tuples, dictionaries & sets training")