# شرط‌های اولیه (Basic Conditions)
# ==============================

# شرط‌های ساده با True/False
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

# ==============================
# بلوک‌های کد (Code Blocks)
# ==============================

# بلوک کد با تورفتگی
if True:
    print("i'm a code block")
    print("look at me")

# استفاده از متغیر در شرط
greet = True
if greet:
    print("hello")

is_charge = True
if is_charge:
    print("charged")
    print("low battery")

is_online = True
if is_online:
    print("jill is online")

inbox_full = False
if inbox_full:
    print("your inbox is full")

# ==============================
# استفاده از عملگرهای مقایسه در شرط
# ==============================

# مقایسه رشته‌ها
answer = "picaso"
if answer == "picaso":
    print("answer is correct")

answer = "matisse"
if answer != "picaso":
    print("answer is not correct")

# مقایسه اعداد
age = 75
if age >= 55:
    print("Discount applied")

# مقایسه boolean
is_day = True
if is_day == True:
    print("Lights off")

# ذخیره نتیجه مقایسه در متغیر
score = 51
pass_grade = score > 50
if pass_grade:
    print("passed")

# ==============================
# مثال‌های کاربردی از فایل اصلی
# ==============================

song = "Don't stop me now"
replay_times = 345
if replay_times >= 300:
    print("Your top song this week: ")
    print(song)

diet = "vegetarian"
veggie_restaurant = "Root"
restaurant = "DelPosto"

if diet == "vegetarian":
    print("Try out: ")
    print(veggie_restaurant)

today = "Wednesday"
if today != "satureday":
    print("set alarm at 7:00")

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

# ==============================
# مثال‌های کاربردی از یادداشت‌های شما
# ==============================

# مقایسه شهرها
big_city = "tokyo"
small_city = "zurich"
print(big_city != small_city)

# بررسی وضعیت باتری
charge = 30
low_charge = charge <= 20
print(low_charge)
if low_charge:
    print("battery is low")

# بررسی صندوق پیام
inbox_message = 502
inbox_capacity = 500
full = inbox_message >= inbox_capacity
print(full)
if full:
    print("you're inbox is full")

# بررسی موجودی برای خرید بلیط
balance = 70
ticket_price = 66
enough_balance = balance >= ticket_price
if enough_balance:
    print("you have enough money to buy ticket")
    print(f"pay {ticket_price}$ and take youre ticket")

# بررسی پاسخ
answer = "Mattisse"
if answer == "picaso":
    print(answer + " is correct")
    print(f"{answer} is correct ")
    print("Your answer is true")
if answer != "pivaso":
    print("Your answer is wrong")
    print(f"{answer} is wrong")
    print(answer + " is wrong")

# بررسی سن
age = 12
if age >= 18:
    print("Allowed to enter")
if age < 18:
    print("not allowed to access")

# بررسی نمره
score = 50
pass_grade = score >= 51
if pass_grade:
    print("passed!")
if score >= 51:
    print("passed!")
if score < 51:
    print("rejected!")

# بررسی روز
print("what day is today?")
today = "saturday"
if today != "friday":
    print("set the alarm at 8:00 am")

# بررسی جنسیت و رانندگی
gender = "male"
can_drive = False
if gender != "female":
    can_drive = True
    print(can_drive)
    print("You can drive")

# بررسی آب و هوا
weather = "rainy"
color_code = "yellow"
if weather == "rainy":
    color_code = "blue"
    print(color_code)
print(color_code)

character = "Wizard"
if character != "Wizard":
    print("You can't use spells")

account = "premium"
if account == "premium":
    print("Exclude from data set")


# ==============================
# عملگر and
# ==============================

# and پایه
age = 17
has_permit = True
if age > 16 and has_permit:
    print("Can drive")

# چندین شرط با and
age = 17
has_permit = True
is_insured = True
if age > 16 and has_permit and is_insured:
    print("Can drive")

year = 1998
if year > 1900 and year < 2005:
    print("valid entry")

subway_defect = True
is_sunny = True
distance = 2
if subway_defect and is_sunny and distance <= 2:
    print("Walk to work")

# ==============================
# عملگر or
# ==============================

# or پایه
average_grade = "A"
final_score = 1400
if average_grade == "A" or final_score >= 1400:
    print("certification achieved")

# چندین شرط با or
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

# تغییر مقدار با or
promote_article = False
views = 100
shares = 30
likes = 70
if views > 150 or shares >= 50 or likes >= 60:
    promote_article = True

# مثال‌های تمرینی از فایل اصلی
like_author = False
like_genre = True
got_recommendation = True
if like_author or like_genre or got_recommendation:
    print("Buy book")

hungry = True
food_ready = False
if hungry and food_ready:
    print("Let's eat!")

bilingual = True
trilingual = False
multilingual = False
if bilingual or trilingual or multilingual:
    print("You speak more than one language!")

# ==============================
# f-string و نمایش داده‌ها
# ==============================

# f-string با اعداد و رشته
min_age = 18
max_age = 28
print(f"{88}% of social media members are between {min_age} and {max_age}")

print(f"Mexico was the leading avocado producer in {2018} ")

first = "english"
second = "madarin chiness"
third = "hindi"
print(f"most spoken languages: {first}, {second}, {third}")

hours = 18
minutes = 45
destination = "paris"
print(f"you'r flight to {destination}, take off at {hours} : {minutes}")

name = "kim"
greeting = f"good morning, {name}"

# f-string با مقایسه‌ها
old_password = "hello123"
new_password = "goodbye321"
compare_old_new = old_password != new_password
repeat_new_password = "goodbye321"
compare_new = new_password == repeat_new_password

print(f"Is new password different from old password? {compare_old_new}")
print(f"Has new password been introduced correctly? {compare_new}")

# f-string با boolean
age = 12
adult_age = age >= 18
print(f"buy an adult_age ticket :{adult_age}")
print(adult_age)
if adult_age:
    print("GOOD JOB")

# ==============================
# بلوک‌های کد بزرگتر
# ==============================

great = True
awfule = False
if great:
    print("hello")
    print("hello world")
    print("i'm a code block")
    print("i'm not sure")