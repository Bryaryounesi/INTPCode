# فایل ششم آموزش پایتون - عملیات لیست
print("lesson: list operations")
print("----------------------------")
# min و max
# ==============================

# پیدا کردن بزرگترین و کوچکترین مقدار
numbers = [12, 6, 5, 2, 7]
print("List:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))

print("----------------------------")

# ذخیره min و max در متغیر
max_list = max(numbers)
min_list = min(numbers)
print("Max + Min:", max_list + min_list)

print("----------------------------")

# استفاده عملی از max
weekly_profits = [20, 59, 43, 76, 24, 60]
max_profit = max(weekly_profits)
print(f"max profit: {max_profit} usd")

print("----------------------------")

# حلقه for روی لیست
for profit in weekly_profits:
    print(f"Profit: {profit}")

print("----------------------------")

# ==============================
# مرتب‌سازی لیست (sort)
# ==============================

# مرتب‌سازی اعداد
scores = [10, 9.25, 8, 4.5, 17, 11.75]
print("Before sort:", scores)
scores.sort()
print("After sort:", scores)

print("----------------------------")

# مرتب‌سازی اعداد منفی و مثبت
temperature = [10, 4, -1, 7, -5, 16, 0]
print("Before sort:", temperature)
temperature.sort()
print("After sort:", temperature)

print("----------------------------")

# مرتب‌سازی رشته‌ها
names = ["cloe", "bill", "ana"]
print("Before sort:", names)
names.sort()
print("After sort:", names)

print("----------------------------")

# مرتب‌سازی حروف
grades = ["A", "C", "F", "B", "G"]
print("Before sort:", grades)
grades.sort()
print("After sort:", grades)

print("----------------------------")

# مرتب‌سازی اعداد اعشاری
oxygen_level = [19.99, 21.2, 20.85]
print("Before sort:", oxygen_level)
oxygen_level.sort()
print("After sort:", oxygen_level)

print("----------------------------")

# ==============================
# جمع‌زدن لیست (sum)
# ==============================

# جمع ساده لیست
signups = [12, 30, 40, 10, 4, 8]
print("List:", signups)
print("Sum:", sum(signups))

# ذخیره sum در متغیر
sumation = sum(signups)
print("Sum stored in variable:", sumation)

print("----------------------------")

# min روی لیست با اعداد تکراری
coordinates = [0, 0, 0]
print("Coordinates:", coordinates)
print("Min coordinate:", min(coordinates))

print("----------------------------")

# ==============================
# الحاق لیست‌ها (+)
# ==============================

# الحاق لیست‌های عددی
database_1 = [1, 2, 3]
database_2 = [4, 5]
print("Database 1:", database_1)
print("Database 2:", database_2)
print("Combined:", database_1 + database_2)

print("----------------------------")

# الحاق لیست‌های مختلف
seats = [1, 2, 3]
taken = [True, True, False]
print("Seats:", seats)
print("Taken status:", taken)
print("Combined:", seats + taken)

print("----------------------------")

# ذخیره لیست الحاق شده
combine = database_1 + database_2
print("Stored combination:", combine)

print("----------------------------")

# الحاق لیست‌های مشتریان و سفارشات
consumers = ["jess", "mike", "lyne"]
order_numbers = [3, 2, 1]
print("Consumers:", consumers)
print("Order numbers:", order_numbers)
print("Combined:", consumers + order_numbers)

print("----------------------------")

# الحاق لیست‌های تیم‌ها
team_1 = ["ana", 78, "kim", 25, "rose", 40]
team_2 = ["jerry", 24, "henry", 28]
print("Team 1:", team_1)
print("Team 2:", team_2)
print("Combined teams:", team_1 + team_2)

print("----------------------------")

# الحاق لیست‌های روزانه
day_1 = [3.5, 2, 4]
day_2 = [1, 2]
overview = day_1 + day_2
print("Day 1:", day_1)
print("Day 2:", day_2)
print("Overview:", overview)

print("----------------------------")

# ==============================
# شمارش المنت‌ها (count)
# ==============================

# شمارش رشته‌ها
answers = ["yes", "no", "sometimes", "yes", "no"]
print("Answers:", answers)
print("Count of 'yes':", answers.count("yes"))

print("----------------------------")

# شمارم مقادیر boolean
free_seats = [True, False, True, True, False]
print("Free seats:", free_seats)
print("Count of True:", free_seats.count(True))

print("----------------------------")

# ذخیره count در متغیر
seats_count = free_seats.count(True)
print("Seats count stored:", seats_count)

print("----------------------------")

# شمارش در لیست ماموریت‌ها
missions = ["mars", "moon", "mars", "ISS"]
print("Missions:", missions)
print("Count of 'mars':", missions.count("mars"))

print("----------------------------")

# شمارش طعم‌ها
flavors = ["vanilla", "chocolate", "strawberry", "vanilla", "vanilla"]
print("Flavors:", flavors)
print("Count of 'vanilla':", flavors.count("vanilla"))

print("----------------------------")

# شمارش کدها
code = [0, 3, 2, 0, 1, 0]
print("Code:", code)
print("Count of 0:", code.count(0))

print("----------------------------")

# ==============================
# بررسی وجود المنت (in)
# ==============================

# بررسی وجود در لیست مواد
ingredients = ["milk", "suger", "eggs", "flour", "butter"]
print("Ingredients:", ingredients)
print("'suger' in ingredients:", "suger" in ingredients)

print("----------------------------")

# ذخیره نتیجه in در متغیر
has_suger = "suger" in ingredients
print("Has suger stored:", has_suger)

print("----------------------------")

# بررسی در لیست اعداد برنده
winning_numbers = [2, 36, 40, 13]
print("Winning numbers:", winning_numbers)
print("13 in winning_numbers:", 13 in winning_numbers)
print("20 in winning_numbers:", 20 in winning_numbers)

has_21 = 21 in winning_numbers
print("Has 21 stored:", has_21)

print("----------------------------")

# بررسی در برنامه زمانبندی
schedule = ["ballet", "swimming", "running", "ballet"]
print("Schedule:", schedule)
print("'ballet' in schedule:", "ballet" in schedule)
print("'running' in schedule:", "running" in schedule)
print("'going' in schedule:", "going" in schedule)

print("----------------------------")

# ==============================
# مثال‌های ترکیبی و کاربردی
# ==============================

# الحاق لیست دانش‌آموزان
students_1 = ["Anna", 16, "Kim", 16]
students_2 = ["Joe", 17, "Lee", 15]
print("Students 1:", students_1)
print("Students 2:", students_2)
print("All students:", students_1 + students_2)

print("----------------------------")

# سیستم سفارشات
customers = ["Jess", "Mike", "Lynn"]
order_numbers = [3, 1, 2]
orders = customers + order_numbers
print("Customers:", customers)
print("Order numbers:", order_numbers)
print("Orders list:", orders)

print("----------------------------")

# محاسبه میانگین
savings = [220, 50, 1000, 70]
total = sum(savings)
number = len(savings)
average = total / number
print("Savings:", savings)
print("Total savings:", total)
print("Number of entries:", number)
print("Average savings:", average)

print("----------------------------")

# استفاده از in در شرط
savings_check = [220, 50, 1000, 70]
if 50 in savings_check:
    print("Good luck! Found 50 in savings")

print("----------------------------")

# ترکیب عملیات مختلف
data = [15, 3, 8, 20, 3, 8]
print("Data:", data)
print("Max:", max(data))
print("Min:", min(data))
print("Sum:", sum(data))
print("Count of 3:", data.count(3))
print("Sorted:", sorted(data))  # بدون تغییر لیست اصلی

print("----------------------------")

# سیستم موجودی کالا
inventory = [10, 5, 8, 3, 15]
print("Inventory:", inventory)
print("Max stock:", max(inventory))
print("Min stock:", min(inventory))
print("Total items:", sum(inventory))
if min(inventory) < 5:
    print("Warning: Low stock alert!")

print("----------------------------")

# سیستم نمرات
grades_list = [85, 92, 78, 90, 65]
print("Grades:", grades_list)
print("Highest grade:", max(grades_list))
print("Lowest grade:", min(grades_list))
print("Average grade:", sum(grades_list) / len(grades_list))
grades_list.sort()
print("Sorted grades:", grades_list)

print("End of list operations training")