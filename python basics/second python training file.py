# مقایسه اعداد (Comparing Numbers)
# ==============================

print("hello world")  # از یادداشت شما

# عملگر کمتر از <
print(1 < 235)
print(235 < 1)

# عملگر بزرگتر از >
print(191 > 1)
print(100 > 1)  # از تمرین فایل
print(11 >= 11)  # از تمرین فایل

# عملگر کمتر از یا مساوی <=
print(4 <= 23)

mini = 5
maxi = 10
result = mini <= maxi
print(result)

# عملگر بزرگتر از یا مساوی >=
print(3099 >= 3098)
print(3099 >= 3099)

# مثال‌های کاربردی
battery_level = 10
low = battery_level <= 20
print("low battery : ")
print(low)

points = 12
level_two = points >= 10
print("level two :")
print(level_two)

# ==============================
# عملگر برابری در رشته‌ها
# ==============================

print("online" == "online")
print("online" != "offline")
print("apple" == "apple")
print("apple" == "orange")

fruit_1 = "apple"
fruit_2 = "orange"
print(fruit_1 == fruit_2)

my_answer = "act"
solution = "ace"
print(my_answer == solution)

# از تمرین فایل
copy = "results.xls"
submission = "sales.xls"
print(copy != submission)

# ==============================
# عملگر نابرابری در رشته‌ها
# ==============================

print("subscribed" != "rejected")
same = "subscribed" != "subscribed"
print(same)

previous_leader = "ana"
new_leader = "jim"
print(previous_leader != new_leader)

# ==============================
# انواع داده (Types)
# ==============================

# بررسی انواع داده از یادداشت شما
name = "hasan"
print(type(name))

number = 35
print(type(number))

sum = 18.26
print(type(sum))

alive = True
print(type(alive))

# انواع داده از فایل اصلی
suger_content = "high"
score = 42
pi = 3.14159
recieved_newsletter = True

# ==============================
# تبدیل انواع (Type Conversion)
# ==============================

# بررسی نوع داده
is_ready = True
fuel_deposite = 59.89
best_grade = "A"
number_of_pets = 2
print(type(is_ready))
print(type(best_grade))
print(type(number_of_pets))
print(type(fuel_deposite))

# تبدیل رشته به عدد
age = "18"  # از یادداشت شما
print(type(age))
age_convered = int(age)
print(age_convered)
print(type(age_convered))
print(age_convered <= 18)

# تبدیل float به int
price = 12.3  # از یادداشت شما
price_converted = int(price)
print(price_converted)
print(int(price))

price_main = 9.99  # از فایل اصلی
print(int(price_main))

# تبدیل int به float
week = 12  # از یادداشت شما
print(float(week))

weeks_main = 12  # از فایل اصلی
print(float(weeks_main))

# تبدیل boolean به int
member = True
not_member = False
value = int(member)
second_value = int(not_member)
print(value)
print(second_value)
print(int(member))
print(int(not_member))

# تبدیل به boolean
member_name = "sam"
middle_name = ""
sibling = 0
foot_size = 8.5
print(bool(member_name))
print(bool(sibling))
print(bool(foot_size))
print(bool(middle_name))

detail = "i love you"
response = bool(detail)
print(response)

# مثال‌های boolean از فایل اصلی
pets = 3
kids = 0
has_pets = bool(pets)
has_kids = bool(kids)
print(has_pets)
print(has_kids)

# ==============================
# f-strings و نمایش داده‌ها
# ==============================

# f-strings پایه
print(f"{12} new masage")
print(f"{13} comments")
print(f"{23} new message")
print(f"{4+3} new message and {50} comments")

# f-strings با متغیرها
apple = 40
orange = 36
print(f"{apple*orange} new message and {24} comments")

new = 51
status = f"{new} new massage"
print(status)

print(f"I would walk  {500}  miles")

price = 40
print(f"glasses price: {price} dollar")

# f-strings پیچیده‌تر
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

# ==============================
# مقایسه‌های کاربردی
# ==============================

age = 15
legal_age = age >= 18
print(age >= legal_age)
if legal_age:
    print("welcom")

charge = 30
low_charge = charge <= 20
print(low_charge)
if low_charge:
    print("battery is low")

# از فایل اصلی
age_check = 18
print(age_check < 18)

# ==============================
# الحاق رشته‌ها (روش قدیمی)
# ==============================

print("comment_number:" + "12")

# ==============================
# عملیات ریاضی ساده
# ==============================

print(12+5)