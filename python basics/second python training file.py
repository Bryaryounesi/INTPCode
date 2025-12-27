# ============================================
# Comparing Numbers - مقایسه اعداد
# ============================================
# 🔥 ضروری → تصمیم‌گیری، شرط‌ها و کنترل جریان در اتوماسیون
battery_level = 10
low = battery_level <= 20
print("low battery :")
print(low)

points = 12
level_two = points >= 10
print("level two :")
print(level_two)

# ⚠️ غیرضروری / تمرینی
print("hello world")
print(1 < 235)
print(235 < 1)
print(191 > 1)
print(100 > 1)
print(11 >= 11)
print(4 <= 23)
mini = 5
maxi = 10
result = mini <= maxi
print(result)
print(3099 >= 3098)
print(3099 >= 3099)

# ============================================
# String Equality - برابری و نابرابری رشته‌ها
# ============================================
# 🔥 ضروری → بررسی داده‌ها و شرایط متنی
fruit_1 = "apple"
fruit_2 = "orange"
print(fruit_1 == fruit_2)
previous_leader = "ana"
new_leader = "jim"
print(previous_leader != new_leader)

# ⚠️ غیرضروری / تمرینی
print("online" == "online")
print("online" != "offline")
print("apple" == "apple")
print("apple" == "orange")
my_answer = "act"
solution = "ace"
print(my_answer == solution)
copy = "results.xls"
submission = "sales.xls"
print(copy != submission)
print("subscribed" != "rejected")
same = "subscribed" != "subscribed"
print(same)

# ============================================
# Data Types - انواع داده
# ============================================
# 🔥 ضروری → فهم نوع داده‌ها برای پردازش صحیح در اتوماسیون
name = "hasan"
print(type(name))
number = 35
print(type(number))
sum = 18.26
print(type(sum))
alive = True
print(type(alive))

# ⚠️ غیرضروری / تمرینی
suger_content = "high"
score = 42
pi = 3.14159
recieved_newsletter = True

# ============================================
# Type Conversion - تبدیل انواع داده
# ============================================
# 🔥 ضروری → تبدیل داده‌ها برای عملیات و مقایسه‌ها
age = "18"
age_converted = int(age)
print(age_converted)
print(type(age_converted))
print(age_converted <= 18)

price = 12.3
price_converted = int(price)
print(price_converted)
print(int(price))
week = 12
print(float(week))
member = True
not_member = False
print(int(member))
print(int(not_member))
member_name = "sam"
sibling = 0
foot_size = 8.5
print(bool(member_name))
print(bool(sibling))
print(bool(foot_size))

# ⚠️ غیرضروری / تمرینی
best_grade = "A"
number_of_pets = 2
fuel_deposite = 59.89
detail = "i love you"
response = bool(detail)
pets = 3
kids = 0
has_pets = bool(pets)
has_kids = bool(kids)

# ============================================
# f-strings - فرمت مدرن رشته‌ها
# ============================================
# 🔥 ضروری → گزارش، نمایش اطلاعات پویا، پیام‌ها
apple = 40
orange = 36
print(f"{apple*orange} new message and {24} comments")
new = 51
status = f"{new} new massage"
print(status)
print(f"I would walk  {500}  miles")
price = 40
print(f"glasses price: {price} dollar")

# ⚠️ غیرضروری / تمرینی
print(f"{12} new masage")
print(f"{13} comments")
print(f"{23} new message")
print(f"{4+3} new message and {50} comments")
vehicle = "airplane"
vehicle = "train"
vehicle = "bus"
event = "movie"
ticket_price = 50
currency = "dollar"
currency = "euro"
print(f"{vehicle} ticket price: {ticket_price} {currency}")
print(f"{event} ticket price: {ticket_price} {currency}")
ticket_price = 30
print(f"{event} ticket price: {ticket_price} {currency}")
author = "agatha christi"
description = f"a book by {author}"
print(description)

# ============================================
# Practical Comparisons - مقایسه‌های کاربردی
# ============================================
# 🔥 ضروری → تصمیم‌گیری در اتوماسیون
age = 15
legal_age = age >= 18
print(age >= legal_age)
if legal_age:
    print("welcome")

charge = 30
low_charge = charge <= 20
print(low_charge)
if low_charge:
    print("battery is low")

age_check = 18
print(age_check < 18)

# ============================================
# String concatenation - الحاق رشته‌ها (قدیمی)
# ============================================
# ⚠️ تمرینی / آموزشی
print("comment_number:" + "12")

# ============================================
# Simple Math Operations - عملیات ریاضی ساده
# ============================================
# 🔥 ضروری → پایه‌ای برای پردازش داده‌ها
print(12+5)