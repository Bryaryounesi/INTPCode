# Variables - متغیرها
# ============================================
# 🔥 ضروری برای اتوماسیون
# این متغیرها پایه هر اسکریپت هستند: ذخیره داده‌ها و وضعیت‌ها
car = "porsche"        # استفاده در مثال‌های ذخیره و نمایش
city = "miami"          # استفاده برای مسیر فایل/API

greeting = "hello world"  # پیام اولیه
name = "Daenerys"         # نمونه نام کاربر

# ⚠️ غیرضروری / آموزشی / تکراری
greating = "hello world"   # ⚠️ اشتباه تایپی
first_name = "Elizabeth"   # ⚠️ تکراری
last_name = "tailor"       # ⚠️
name = "Elizabeth tailor"  # ⚠️
city = "las vegas"         # ⚠️
person_name = "Elizabeth tailor"  # ⚠️
city_name = "Washington DC"       # ⚠️
sport = "B-ball"                  # ⚠️
frequency = "daily"               # ⚠️
job = "sherif"                    # ⚠️

# ============================================
# Print - چاپ خروجی
# ============================================
# 🔥 ضروری برای اتوماسیون
# نمایش نتایج و وضعیت برنامه
print(greeting)
print(name)
print(city)

# ⚠️ غیرضروری / آموزشی
print("3 , 2 , 1")
print("go")
print("hello world")
print("bye")
print(person_name)
print(city_name)
print(sport)
print(frequency)

# ============================================
# String concatenation - الحاق رشته‌ها
# ============================================
# 🔥 ضروری → پیام‌ها، گزارش، درخواست API
job = "artist"
likes = "20"
print("job:" + job)
print("likes:" + likes)

# ⚠️ غیرضروری / تکراری
print("sport:" + sport)
print("name:" + person_name)
print("city:" + city_name)
print("singer:" + person_name)
label = "name:" + "joe"
print(label)

# ============================================
# Update variables - به‌روزرسانی مقادیر
# ============================================
# 🔥 ضروری → تغییر وضعیت‌ها در اتوماسیون
status = "watching HBO"
status = "relaxing in bed"
print(status)

# ⚠️ غیرضروری / تمرینی
default_option = "upload"
new_status = "download"
new_status = default_option
print(new_status)

temperature = "0 degree"
temperature = "100 degree"
print(temperature)

# ============================================
# Numeric operations - محاسبات عددی
# ============================================
# 🔥 ضروری → محاسبات، شمارش، آمار، پردازش داده‌ها
ticket = 200
ticket2 = ticket * 10
print(ticket2)

active_users = 5
print(active_users + 1)
active_users = 5 + 1
print(active_users)

percent = 0.5 * 100
print(percent)

# ⚠️ غیرضروری / تمرینی
private = 32
public = 10 - 5
total = public + private
print(total)
print(total - private - 10)
print("student:")
print(private * 10)
private_old = 56
public_old = 30
total_old = private_old + public_old
print(total_old)
print(private_old - public_old)

# ============================================
# Boolean & NOT - بولین و نقیض
# ============================================
# 🔥 ضروری → شرط‌ها و کنترل وضعیت‌ها
restart = True
print(not restart)

is_open = True
is_closed = not is_open
print(is_closed)

available = True
print(not available)
unavailable = not available
print(unavailable)

morning = True
evening = not morning
print(evening)

# ⚠️ غیرضروری / تمرینی
shutdown = False
prevent_logout = False
print(shutdown)
print(not True)
print(not False)
print(restart)
print(not restart)
powered_on = True
print(powered_on)
print(not False)
open = True
print(not open)

# ============================================
# Comparisons - مقایسه‌ها
# ============================================
# 🔥 ضروری → تصمیم‌گیری در اتوماسیون
entered_pin = 5448
expected_pin = 5440
print(entered_pin == expected_pin)

one = 1
two = 2
print(one == two)

votes = 120
winning_target = 130
im_winner = votes == winning_target
print(im_winner)

level = 10
highest_level = 50
print(level == highest_level)

print(1 != 10)
result = 1 != 10
print(result)
print(one != two)

# ⚠️ غیرضروری / آموزشی
print(10 == 9)
print(10 == 10)
print(10 == 9)

# ============================================
# f-strings - فرمت مدرن رشته‌ها
# ============================================
# 🔥 ضروری → گزارش، پیام، نمایش اطلاعات پویا
new_message = 4
print(f"{new_message} new messages")

degree = 70
print(f"temperature: {degree} F")

new = 5
read = 2
print(f"{new - read} unread messages")

# ⚠️ غیرضروری / تمرینی
print(f"{2} new message")
print(f"{3} friends")
print(f"{3} new messages and {5} friend requests")
x = 2
y = 5
t = f"{x/2} + {y/2}"
print(t)
movie = "vertigo"
display = f"airing tonight: {movie}"
print(display)

# ============================================
# Expressions - ترکیب‌ها و مثال‌ها
# ============================================
# ♻️ میان‌رده → فهم ساختار رشته‌ها و داده‌ها
user = "snopdoge"
print("username:" + user)

temperature = "45"
print("temperature:" + temperature + "degree")

# ⚠️ غیرضروری / تمرینی
print("folower :" + "55")
print("John" + "athan")
print("Ms." + "Irene")