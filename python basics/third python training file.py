# ============================================
# Basic Conditions - شرط‌های اولیه
# ============================================
# 🔥 ضروری → کنترل جریان برنامه، تصمیم‌گیری در اتوماسیون
age = 21
can_drive = False
if age >= 18:
    can_drive = True
    print(can_drive)

inbox_full = True
show_alert = inbox_full == True
if show_alert:
    print("Inbox full")
    print("Archive some to continue")

# بررسی موجودی برای خرید بلیط
balance = 70
ticket_price = 66
enough_balance = balance >= ticket_price
if enough_balance:
    print("you have enough money to buy ticket")
    print(f"pay {ticket_price}$ and take your ticket")

# بررسی سن و دسترسی
age = 12
if age >= 18:
    print("Allowed to enter")
if age < 18:
    print("not allowed to access")

# ⚠️ غیرضروری / تمرینی
if True:
    print("hello")
if True:
    print("3  2  1 Go")
if False:
    print("to display or not to display")
if True:
    print("show notifications")
if True:
    print("the answer is 45 ")
if True:
    print("enable flight mode")

# ============================================
# Code Blocks - بلوک‌های کد
# ============================================
# 🔥 ضروری → بلوک‌ها پایه ساختار شرط‌ها
greet = True
if greet:
    print("hello")

is_charge = True
if is_charge:
    print("charged")
    print("low battery")

# ⚠️ غیرضروری / تمرینی
if True:
    print("i'm a code block")
    print("look at me")
is_online = True
if is_online:
    print("jill is online")
inbox_full = False
if inbox_full:
    print("your inbox is full")

# ============================================
# Comparisons in Conditions - مقایسه در شرط
# ============================================
# 🔥 ضروری → تصمیم‌گیری در اتوماسیون
answer = "picaso"
if answer == "picaso":
    print("answer is correct")

score = 51
pass_grade = score > 50
if pass_grade:
    print("passed")

# ⚠️ غیرضروری / تمرینی
answer = "matisse"
if answer != "picaso":
    print("answer is not correct")
age = 75
if age >= 55:
    print("Discount applied")
is_day = True
if is_day == True:
    print("Lights off")

# ============================================
# Logical AND - عملگر AND
# ============================================
# 🔥 ضروری → چند شرط همزمان، کنترل پیچیده
age = 17
has_permit = True
if age > 16 and has_permit:
    print("Can drive")

age = 17
has_permit = True
is_insured = True
if age > 16 and has_permit and is_insured:
    print("Can drive")

# ⚠️ غیرضروری / تمرینی
year = 1998
if year > 1900 and year < 2005:
    print("valid entry")
subway_defect = True
is_sunny = True
distance = 2
if subway_defect and is_sunny and distance <= 2:
    print("Walk to work")

# ============================================
# Logical OR - عملگر OR
# ============================================
# 🔥 ضروری → تصمیم‌گیری چندشاخه، انتخاب بین گزینه‌ها
average_grade = "A"
final_score = 1400
if average_grade == "A" or final_score >= 1400:
    print("certification achieved")

# ⚠️ غیرضروری / تمرینی
average_grade = "B"
final_score = 1400
won_competition = True
if average_grade == "A" or final_score >= 1500 or won_competition:
    print("Certificate achieved!")
is_weekend = True
on_vacation = False
if is_weekend or on_vacation:
    print("go on roadtrip")
highest_score = 100
score = 70
level = 5
if score > highest_score or level == 5:
    print("You won!")
promote_article = False
views = 100
shares = 30
likes = 70
if views > 150 or shares >= 50 or likes >= 60:
    promote_article = True
like_author = False
like_genre = True
got_recommendation = True
if like_author or like_genre or got_recommendation:
    print("Buy book")
bilingual = True
trilingual = False
multilingual = False
if bilingual or trilingual or multilingual:
    print("You speak more than one language!")

# ============================================
# f-strings - نمایش داده‌ها
# ============================================
# 🔥 ضروری → گزارش، پیام، نمایش پویا
min_age = 18
max_age = 28
print(f"{88}% of social media members are between {min_age} and {max_age}")
first = "english"
second = "madarin chiness"
third = "hindi"
print(f"most spoken languages: {first}, {second}, {third}")

hours = 18
minutes = 45
destination = "paris"
print(f"your flight to {destination}, take off at {hours} : {minutes}")

age = 12
adult_age = age >= 18
print(f"buy an adult_age ticket :{adult_age}")
print(adult_age)
if adult_age:
    print("GOOD JOB")

# ⚠️ غیرضروری / تمرینی
print(f"Mexico was the leading avocado producer in {2018}")
name = "kim"
greeting = f"good morning, {name}"
old_password = "hello123"
new_password = "goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "goodbye321"
compare_new = new_password == repeat_new_password
print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced correctly? {compare_new}")

# ============================================
# Large code blocks - بلوک‌های بزرگتر
# ============================================
# 🔥 ضروری → ترکیب شرط‌ها و بلوک‌های کد در اتوماسیون
great = True
if great:
    print("hello")
    print("hello world")

# ⚠️ غیرضروری / تمرینی
if great:
    print("i'm a code block")
    print("i'm not sure")