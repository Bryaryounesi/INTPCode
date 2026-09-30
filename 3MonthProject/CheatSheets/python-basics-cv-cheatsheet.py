"""

چیت‌شیت جامع پایتون پایه برای مسیر یادگیری کامپیوتر ویژن (جونیور)
=====================================================================
نسخه: 1.0
هدف: مرجع سریع برای مرور و یادآوری پایتون پایه، با تمرکز روی
کاربردهای واقعی در مسیر یادگیری بینایی کامپیوتر.
راهنما:
  - بخش‌های مهم برای CV با [CV] برچسب‌گذاری شده‌اند.
  - مطالب جدیدی که در فایل‌های اصلی نبودند با [جدید] مشخص شده‌اند.
  - کدها برای خوانایی نوشته شده‌اند و لزوماً همه قابل اجرا نیستند.
===============================================================
"""
import os

os.environ["PYTHONIOENCODING"] = "utf-8"

# =============================================================
# بخش ۰ — پیش‌نیازها، تنظیمات، ساختار اسکریپت
# ===============================================================

# [جدید] نسخه پیشنهادی پایتون: 3.10 یا بالاتر
# دلیل: f-string پایدارتر، پشتیبانی بهتر کتابخانه‌های CV،
#        سرعت بهتر، خطاهای واضح‌تر.
#
# [جدید] کتابخانه‌های پایه (چیت‌شیت جدا برای هرکدام داری):
#   pip install numpy opencv-python matplotlib pandas
#
# [جدید] محیط پیشنهادی برای کار روزمره CV: Jupyter Notebook یا VS Code
#        با افزونه Python و Pylance.

# [جدید] ساختار اسکریپت قابل اجرا با if __name__ == "__main__"
# این الگو تضمین می‌کند کد فقط وقتی مستقیم اجرا می‌شود اجرا شود،
# نه وقتی به عنوان ماژول import می‌شود (مثلاً از یک اسکریپت دیگر).

def main():
    print("hello CV")

if __name__ == "__main__":
    main()


# =====================================================================
# بخش ۱ — متغیرها، انواع داده، تبدیل انواع
# =====================================================================

# --- انواع پایه ---
count = 10              # int
price = 9.99            # float
name = "cat"            # str
is_valid = True         # bool
nothing = None          # NoneType (مقدار خالی)

# دیدن نوع یک مقدار
print(type(count))      # <class 'int'>
print(type(name))       # <class 'str'>
print(type(price))      # <class 'float'>
print(type(is_valid))   # <class 'bool'>

# --- [جدید] قواعد نام‌گذاری ---
# متغیر و تابع: snake_case مثل image_path, load_image, model_name
# ثابت‌ها: UPPER_CASE مثل MAX_SIZE = 512, IMAGE_DIR = "data/train"
# کلاس‌ها: PascalCase مثل ImageDataset, DataLoader
# غلط‌های رایج: greating → درست: greeting
#               tempreture → درست: temperature

# --- انتساب چندگانه ---
a, b, c = 1, 2, 3
x = y = z = 0

# --- آپدیت متغیر ---
status = "watching"
status = "relaxing"     # مقدار قبلی پاک می‌شود
print(status)

# --- انتساب مقدار یک متغیر به متغیر دیگر ---
default_option = "upload"
new_status = default_option    # کپی مقدار، نه ارجاع
print(new_status)


# --- عملیات ریاضی ---
ticket = 200
ticket2 = ticket * 10
print(ticket2)                 # 2000

private = 32
public = 10 - 5
total = public + private
print(total)                   # 37

# عملیات ریاضی روی متغیر عددی
active_users = 5
print(active_users + 1)        # 6
active_users = 5 + 1           # متغیر مقدار جدید می‌گیرد
print(active_users)            # 6

percent = 0.5 * 100
print(percent)                 # 50.0

# عملیات ریاضی روی رشته (تکرار)
ticket = "1000"
print(ticket)                  # "1000"
ticket_3 = "baba"
ticket_4 = ticket_3 * 10       # تکرار رشته
print(ticket_4)                # "babababababababababa"

# ⚠️ تله رایج: رشته عددی با ضرب تکرار می‌شود، نه ضرب عددی
# "1000" * 3 می‌شود "100010001000" نه 3000.
# برای تبدیل به عدد باید int("1000") بزنی.

# --- نمایش دما با واحد ---
temperature = "15"
print("temperature: " + temperature + " degrees")
# بهتر است با f-string:
print(f"temperature: {temperature} degrees")

# [CV] در CV معمولاً با اعداد اعشاری سر و کار داری
# (نرمال‌سازی پیکسل‌ها به بازه 0 تا 1). پس int() که برش می‌ده
# را با float() اشتباه نگیر.


# =====================================================================
# بخش ۲ — Boolean و عملگرهای مقایسه‌ای
# =====================================================================

# --- Boolean ---
restart = True
shutdown = False
prevent_logout = False

print(shutdown)                # False
print(not restart)             # False
print(prevent_logout)          # False
print(not True)                # False
print(not False)               # True
print(restart)                 # True
print(not restart)             # False

# نفی مقدار یک متغیر
available = True
unavailable = not available
print(unavailable)             # False

# نفی در هنگام چاپ
power = True
print(not power)               # False

# [CV] Bool برای ماسک‌گذاری استفاده می‌شود. mask=1/0 یا True/False.

# --- عملگرهای مقایسه‌ای ---
# برابر
print(10 == 9)                 # False
print(10 == 10)                # True

# نامساوی
print(1 != 10)                 # True
print(1 != 1)                  # False

# کمتر و بیشتر
print(1 < 235)                 # True
print(235 < 1)                 # False
print(191 > 1)                 # True

# کمتر یا مساوی / بیشتر یا مساوی
print(4 <= 23)                 # True
print(11 >= 11)                # True
print(3099 >= 3098)            # True

# مثال کاربردی: شارژ باتری
battery_level = 10
low = battery_level <= 20
print("low battery:", low)     # True

# مثال کاربردی: سطح کاربری
points = 12
level_two = points >= 10
print("level two:", level_two) # True

# مقایسه رشته‌ها
print("online" == "online")    # True
print("online" != "offline")   # True
print("apple" == "orange")     # False

copy = "results.xls"
submission = "sales.xls"
print(copy != submission)      # True


# =====================================================================
# بخش ۳ — تبدیل انواع (Type Conversion)
# =====================================================================

# [CV] تبدیل نوع یکی از پرتکرارترین کارهاست. مخصوصاً وقتی
# از input() می‌خونی یا فایل متنی پارس می‌کنی.

# --- انواع داده ---
name = "hasan"
print(type(name))              # <class 'str'>

number = 35
print(type(number))            # <class 'int'>

sum_value = 18.26
print(type(sum_value))         # <class 'float'>

alive = True
print(type(alive))             # <class 'bool'>

# --- تبدیل عدد صحیح ---
integerr = 25
print(str(integerr))           # "25"
print(bool(integerr))          # True
print(float(integerr))         # 25.0

# --- تبدیل Boolean ---
booli = True
print(int(booli))              # 1
print(float(booli))            # 1.0
print(str(booli))              # "True"

# True → 1 ، False → 0

# --- تبدیل رشته ---
stringo = "nana"
stringo2 = "65239"
# print(int(stringo))          # ValueError چون nana عدد نیست
print(int(stringo2))           # 65239
print(float(stringo2))         # 65239.0
print(bool(stringo))           # True (هر رشته غیرخالی True است)
print(bool(""))                # False (رشته خالی False است)

# --- تبدیل رشته به عدد ---
age = "18"
print(type(age))               # <class 'str'>
age_converted = int(age)
print(age_converted)           # 18
print(type(age_converted))     # <class 'int'>
print(age_converted <= 18)     # True

# --- تبدیل float به int (برش، نه گرد کردن) ---
price = 12.3
print(int(price))              # 12
price_main = 9.99
print(int(price_main))         # 9

# --- تبدیل int به float ---
week = 12
print(float(week))             # 12.0

# --- تبدیل boolean به int ---
member = True
not_member = False
print(int(member))             # 1
print(int(not_member))         # 0

# --- تبدیل به boolean ---
# هر مقدار غیرخالی / غیرصفر → True
a = 12.5
member = False
city = "albakerki"
number = 45
emp = ""

print("float to bool:", bool(a))         # True
print("str to bool:", bool(city))        # True
print("int to bool:", bool(number))      # True
print("empty to bool:", bool(emp))       # False

# --- مثال ---
pets = 3
kids = 0
has_pets = bool(pets)         # True
has_kids = bool(kids)         # False
print(has_pets)
print(has_kids)

# قانون‌های کلیدی:
# - int("18") کار می‌کند، int("nana") خطا می‌دهد.
# - int(9.99) می‌شود 9 (برش به سمت صفر، نه گرد کردن).
# - bool("") می‌شود False، bool("any text") می‌شود True.
# - bool(0) می‌شود False، bool(12) می‌شود True.


# =====================================================================
# بخش ۴ — f-string و قالب‌بندی رشته
# =====================================================================

# f-string بهترین راه برای ترکیب رشته و مقدار است.

# --- با مقدار مستقیم ---
print(f"{2} new message")      # "2 new message"
print(f"{3} friends")          # "3 friends"

# --- با متغیر ---
new_message = 4
print(f"{new_message} new messages")   # "4 new messages"

# --- با عملیات ریاضی ---
new = 5
read = 2
print(f"{new - read} unread messages") # "3 unread messages"

# --- با چند متغیر ---
print(f"{3} new messages and {5} friend requests")

# --- با فرمول پیچیده ---
x = 2
y = 5
t = f"{x/2} + {y/2}"
print(t)                       # "1.0 + 2.5"

# --- مثال دما ---
degree = 70
print(f"temperature: {degree} F")

# --- مثال فیلم ---
movie = "vertigo"
display = f"airing tonight: {movie}"  # type: ignore
print(display)

# --- [جدید] گرد کردن در f-string ---
accuracy = 0.95678
print(f"accuracy: {accuracy:.2f}")     # "accuracy: 0.96"
# فرمت :.2f یعنی دو رقم اعشار

# --- [جدید] درصد ---
print(f"accuracy: {accuracy:.1%}")     # "accuracy: 95.7%"

# --- [جدید] فاصله‌دهی ---
print(f"|{name:>10}|")     # راست‌چین در 10 کاراکتر
print(f"|{name:<10}|")     # چپ‌چین
print(f"|{name:^10}|")     # وسط‌چین
# ----------------------------------------------------------------
# ============================================================
# f-string — راهنمای کامل فرمت‌بندی
# ============================================================
#
# f-string یعنی رشته‌ای که با f یا F شروع می‌شود و داخل {} می‌توان
# متغیر، عبارت، یا فرمت‌بندی گذاشت. از پایتون 3.6 به بعد هست.

# --- سینتکس پایه ---
name = "yolo"
version = 8
accuracy = 0.95678

print(f"{name}")                    # yolo
print(f"{name}_{version}")          # yolo_8
print(f"model: {name} v{version}")  # model: yolo v8

# --- فرمت‌بندی عدد اعشاری ---
value = 3.14159
print(f"{value:.2f}")               # 3.14    دو رقم اعشار
print(f"{value:.3f}")               # 3.142   سه رقم اعشار
print(f"{value:.0f}")               # 3       بدون اعشار
print(f"{value:+.2f}")              # +3.14   با علامت

# [CV] نمایش accuracy، confidence، loss
print(f"accuracy: {accuracy:.4f}")  # accuracy: 0.9568

# --- فرمت‌بندی درصد ---
value = 0.95678
print(f"{value:.1%}")               # 95.7%   یک رقم اعشار درصد
print(f"{value:.2%}")               # 95.68%  دو رقم اعشار درصد

# [CV] نمایش دقت مدل
precision = 0.9567
print(f"precision: {precision:.1%}")   # precision: 95.7%

# --- فرمت‌بندی عدد صحیح ---
count = 42
print(f"{count:d}")                 # 42
print(f"{count:5d}")                # "   42"  حداقل 5 کاراکتر
print(f"{count:05d}")               # "00042"  پر با صفر
print(f"{count:+d}")                # "+42"    با علامت

# [CV] ساخت نام فایل شماره‌دار
for idx in range(3):
    print(f"image_{idx:04d}.jpg")
# image_0000.jpg
# image_0001.jpg
# image_0002.jpg

# --- جداکننده هزارگان ---
big = 1234567
print(f"{big:,}")                   # 1,234,567
print(f"{big:_}")                   # 1_234_567

# --- تراز (Alignment) ---
text = "model"
print(f"|{text:>10}|")              # |     model|   راست‌چین
print(f"|{text:<10}|")              # |model     |   چپ‌چین
print(f"|{text:^10}|")              # |  model   |   وسط‌چین

# [CV] جدول‌بندی خروجی لاگ
print(f"{'model':<15} {'accuracy':>10}")
print(f"{'yolo':<15} {0.9567:>10.4f}")
print(f"{'resnet':<15} {0.8734:>10.4f}")
# model              accuracy
# yolo                 0.9567
# resnet               0.8734

# --- پر کردن با کاراکتر دلخواه ---
value = 42
print(f"{value:*>10}")              # *******42
print(f"{value:0<10}")              # 4200000000
print(f"{value:->10}")              # --------42

# --- فرمت علمی و نمایش‌های خاص ---
value = 1234.5678
print(f"{value:e}")                 # 1.234568e+03   علمی
print(f"{value:.2e}")               # 1.23e+03       علمی با دو اعشار
print(f"{value:g}")                 # 1234.57        عمومی

# --- فرمت‌های مبنایی (کم‌کاربرد در CV) ---
value = 255
print(f"{value:b}")                 # 11111111   باینری
print(f"{value:o}")                 # 377        اکتال
print(f"{value:x}")                 # ff         هگز (کوچک)
print(f"{value:X}")                 # FF         هگز (بزرگ)

# --- ترکیب چند فرمت (خیلی رایج) ---
value = 0.95678
print(f"{value:>10.2f}")            # راست‌چین در 10 کاراکتر با دو اعشار
print(f"{value:<10.2%}")            # چپ‌چین با فرمت درصد
print(f"{value:08.2f}")             # پر با صفر، دو اعشار

# [CV] جدول متریک‌های مدل
results = [
    ("yolo", 0.9567, 0.0234),
    ("resnet", 0.8734, 0.1456)
]
for name, acc, loss in results:
    print(f"{name:<15} acc: {acc:>6.2%} loss: {loss:>8.4f}")
# yolo            acc: 95.67% loss:   0.0234
# resnet          acc: 87.34% loss:   0.1456

# --- فراخوانی متد و attribute داخل f-string ---
name = "yolo"
image_shape = (1080, 1920, 3)
data = {"label": "cat", "conf": 0.92}

print(f"{name.upper()}")                    # YOLO
print(f"{image_shape[0]} x {image_shape[1]}")   # 1080 x 1920
print(f"{data['label']}")                   # cat

# [CV] لاگ‌گیری از ابعاد تصویر
path = "cat.jpg"
img_shape = (1080, 1920, 3)
print(f"loaded {path}: {img_shape}")        # loaded cat.jpg: (1080, 1920, 3)

# --- شرط یک‌خطی داخل f-string ---
valid = True
conf = 0.92
print(f"{'yes' if valid else 'no'}")            # yes
print(f"{'OK' if conf > 0.8 else 'low'}")       # OK

# [CV] وضعیت پردازش در لاگ
for idx, ok in enumerate([True, False, True]):
    print(f"image_{idx:04d}: {'OK' if ok else 'FAIL'}")
# image_0000: ✓
# image_0001: ✗
# image_0002: ✓

# --- نکات مهم ---
# 1. داخل {} می‌شود هر عبارت معتبر پایتون نوشت.
# 2. برای نمایش خود { یا }، از {{ و }} استفاده کن:
print(f"{{literal braces}}")        # {literal braces}
# 3. تفاوت f"{value}" و f"{value!r}":
#    !r → repr    (برای دیباگ، با کوتیشن)
#    !s → str     (پیش‌فرض)
name = "yolo"
print(f"{name}")                    # yolo
print(f"{name!r}")                  # 'yolo'
# 4. f-string از پایتون 3.6 به بعد وجود دارد. در کد قدیمی .format()
#    می‌بینی:
"{}: {}".format("acc", 0.95)        # روش قدیمی
f"acc: {0.95}"                      # روش جدید
# 5. در پایتون 3.12+ می‌شود داخل {} کامنت و خط جدید هم نوشت
#    (nesting f-string)، ولی برای خوانایی ساده نگهش دار.
# 6. از f-string برای مسیر فایل استفاده کن، نه الحاق با +:
#    ❌ "data/" + folder + "/" + name + ".jpg"
#    ✅ f"data/{folder}/{name}.jpg"
# =====================================================================
# بخش ۵ — رشته‌ها: عملیات ضروری
# =====================================================================

# [CV] کار با مسیر فایل، پارس لاگ، خواندن CSV همه با متدهای رشته‌ای.

# --- split: تقسیم رشته به لیست ---
new_users = "Ann Jon Alex"
users_list = new_users.split()
print(users_list)              # ['Ann', 'Jon', 'Alex']

# جداکننده مشخص
signups = "44-22-44-11"
print(signups.split("-"))      # ['44', '22', '44', '11']

# جداکننده نقطه
new_users = "reza.hadi.ali.ana"
print(new_users.split("."))    # ['reza', 'hadi', 'ali', 'ana']

# تقسیم با space صریح
words = "gear fault lights build-up"
print(words.split(" "))

# تقسیم با آندراسکور
user = "Lauren_25 F Architect"
print(user.split("_"))

# [CV] پارس مسیر فایل
path = "indiano.com/glossary/python"
print(path.split("/"))         # ['indiano.com', 'glossary', 'python']

# [CV] پارس داده‌های CSV
csv_data = "name,age,city,john,25,new york,jane,30,los angeles"
print(csv_data.split(","))

# --- join: تبدیل لیست رشته‌ای به رشته ---
users_list = ['Ann', 'Jon', 'Alex']
print("--".join(users_list))   # "Ann--Jon--Alex"
print("".join(users_list))     # "AnnJonAlex"

# [CV] ساخت مسیر
parts = ["data", "train", "cat.jpg"]
print("/".join(parts))         # "data/train/cat.jpg"

# --- replace: جایگزینی (نیاز به self-assignment) ---
special = "today's special is pizza"
new_special = special.replace("pizza", "pasta")
print(new_special)             # "today's special is pasta"

# ⚠️ بدون ذخیره‌سازی تغییر نمی‌کند:
special = "today's special is pizza"
special.replace("pizza", "spaghetti")
print(special)                 # هنوز "pizza" دارد

# با self-assignment
sport = "todays sport is football"
sport = sport.replace("football", "ping pong")
print(sport)                   # "todays sport is ping pong"

# جایگزینی تمام تکرارها
june = "June sales target. Let's rock June!"
july = june.replace("June", "July")
print(july)

# --- [CV] تبدیل رشته عددی به لیستی از اعداد ---
int_str = "84561518916483155"
int_list = [int(digit) for digit in int_str]
print(int_list)

# --- [CV] تبدیل رشته به لیستی از حروف ---
string1 = "kjdssjksdkllkfjsfksfjklhn"
letter_list = [let for let in string1]
print(letter_list)

# --- [CV] پردازش لاگ ---
log_entry = "ERROR 2024-01-15 14:30:25 Database connection failed"
log_parts = log_entry.split()
print(log_parts[0])            # "ERROR"

# --- [CV] پردازش داده CSV به شکل رکورد ---
csv_data = "name,age,city,john,25,new york,jane,30,los angeles"
csv_list = csv_data.split(",")
records = []
for i in range(0, len(csv_list), 3):
    record = csv_list[i:i+3]
    records.append(record)
print(records)

# --- متدهای رشته‌ای مفید دیگر ---
s = "Hello World"
print(s.upper())          # "HELLO WORLD"
print(s.lower())          # "hello world"
print(s.strip())          # حذف فاصله ابتدا و انتها
print(s.startswith("Hello"))   # True
print(s.endswith("World"))     # True
print("World" in s)            # True


# =====================================================================
# بخش ۶ — شرط‌ها (if / elif / else)
# =====================================================================

# --- شرط ساده ---
if True:
    print("hello")

if False:
    print("این چاپ نمی‌شود")

# --- استفاده از متغیر در شرط ---
greet = True    #type:ignore
if greet:
    print("hello")

is_online = True
if is_online:
    print("jill is online")

inbox_full = False
if inbox_full:
    print("your inbox is full")

# --- شرط با عملگر مقایسه ---
answer = "picaso"
if answer == "picaso":
    print("answer is correct")

answer = "matisse"
if answer != "picaso":
    print("answer is not correct")

age = 75
if age >= 55:
    print("Discount applied")

# --- ذخیره نتیجه مقایسه در متغیر ---
score = 51
pass_grade = score > 50
if pass_grade:
    print("passed")

# [CV] همین الگو برای confidence استفاده می‌شود:
confidence = 0.85
is_confident = confidence > 0.7
if is_confident:
    print("prediction accepted")

# --- else ---
age = 12
if age >= 18:
    print("Allowed to enter")
else:
    print("not allowed")

# --- elif: شرط‌های زنجیره‌ای ---
score = 75
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("D")

# [CV] مثال: سطح اطمینان مدل
confidence = 0.65
if confidence >= 0.9:
    label = "high"
elif confidence >= 0.7:
    label = "medium"
elif confidence >= 0.5:
    label = "low"
else:
    label = "reject"

# ⚠️ نکته طلایی ترتیب شرط‌ها:
# شرط‌های خاص‌تر (با AND/OR بیشتر) باید بالاتر بیان،
# چون پایتون به محض یافتن اولین شرط True، بقیه را نادیده می‌گیرد.

# مثال ترتیب صحیح:
age = 25
is_student = True
is_vip = False

if age >= 65 or is_student:
    discount = 25
elif is_vip and age >= 18:
    discount = 15
else:
    discount = 0

# --- نکته: if x بنویس، نه if x == True ---
# هر مقدار falsy (0، ""، []، None، False) در if معادل False است.
is_day = True
if is_day:                     # بهتر از if is_day == True
    print("lights off")

# --- [جدید] شرط یک‌خطی (ternary) ---
status = "adult" if age >= 18 else "minor"
# معادل:
# if age >= 18:
#     status = "adult"
# else:
#     status = "minor"

# --- and / or / not ---
# and: هر دو شرط باید True باشند
age = 17
has_permit = True
if age > 16 and has_permit:
    print("Can drive")

# or: حداقل یکی True باشد
average_grade = "A"
final_score = 1400
if average_grade == "A" or final_score >= 1400:
    print("certification achieved")

# ترکیب and و or
weather = "sunny"
day_type = "weekend"
has_car = True
if weather == "sunny" and (day_type == "weekend" or has_car):
    print("Perfect day for a trip!")

# not
if not inbox_full:
    print("inbox not full")


# =====================================================================
# بخش ۷ — حلقه while
# =====================================================================

# --- while پایه ---
test = True
while test:
    print("once")
    test = False               # بدون این خط، حلقه بی‌نهایت می‌شود

# --- while با شمارنده صعودی ---
counter = 1
while counter < 10:
    print(counter)
    counter += 2               # معادل counter = counter + 2

# --- while با شمارنده نزولی ---
counter = 3
while counter > 0:
    print(counter)
    counter -= 1

# --- while با شرط مرکب ---
sales = 0
inventory = 10
while sales <= 10 and inventory >= 0:
    print(f"Sales: {sales}")
    print(f"Inventory: {inventory}")
    sales += 1
    inventory -= 1

# --- while با break ---
counter = 10
while counter > 0:
    print(counter)
    counter -= 1
    if counter == 5:
        break

# --- else در while (اجرا می‌شود فقط اگر break نزده باشی) ---
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print("loop ended normally")

i = 0
while i < 3:
    print(i)
    if i == 1:
        break
    i += 1
else:
    print("این چاپ نمی‌شود، چون break خورد")

# ⚠️ هشدار: while True بدون break خطرناک است.
# اگر می‌نویسی، حتماً شرط خروج داشته باش.


# =====================================================================
# بخش ۸ — حلقه for
# =====================================================================

# --- for با range ---
for i in range(5):
    print(i)                   # 0,1,2,3,4

for i in range(2, 5):
    print(i)                   # 2,3,4

for i in range(2, 10, 2):
    print(i)                   # 2,4,6,8

# --- for روی لیست ---
numbers_list = [1, 2, 3, 4, 6, 8, 10]
for n in numbers_list:
    print(n)

artists = ["chagall", "lissitzky"]
for artist in artists:
    print(artist)

# --- [CV] for روی لیست مسیر تصاویر ---
image_paths = ["cat.jpg", "dog.jpg", "bird.jpg"]
for path in image_paths:
    print(f"loading {path}")

# --- for با متغیر خارجی (به‌روزرسانی) ---
x = 3
for i in range(5):
    print(x)
    x += 2                     # هر دور 2 اضافه می‌شود

# --- for با رشته ---
x = "23"
for i in range(5):
    x += "~~"
    print(x)

# --- [CV] for با enumerate: هم ایندکس هم مقدار ---
days = ["saturday", "sunday", "monday"]
for index, day in enumerate(days):
    print(f"{index}: {day}")

# [CV] بسیار رایج: پیمایش دیتاست با ایندکس
images = ["img1.jpg", "img2.jpg", "img3.jpg"]
for idx, img in enumerate(images):
    print(f"image {idx}: {img}")

# --- [CV] for با zip: پیمایش همزمان دو لیست ---
names = ["ali", "sara", "reza"]
scores = [18, 20, 15]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# [CV] زیپ برای جفت کردن تصویر و لیبل
images = ["img1.jpg", "img2.jpg", "img3.jpg"]
labels = ["cat", "dog", "bird"]
for img, label in zip(images, labels):
    print(f"{img}-> {label}")

# --- for با دیکشنری ---
student = {"name": "Maryam", "age": 22, "grade": "A"}

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(f"{key}: {value}")

# --- حلقه تو در تو ---
for i in range(3):
    for j in range(3):
        print(i, j)

# --- الگوی چاپی ---
line = ""
for i in range(4):
    line += "~"
    print(line)

# --- [جدید] for با else ---
for i in range(3):
    print(i)
else:
    print("loop ended normally")

# else اجرا نمی‌شود اگر break بزنی:
for i in range(10):
    if i == 5:
        break
    print(i)
else:
    print("این چاپ نمی‌شود")


# =====================================================================
# بخش ۹ — break و continue
# =====================================================================

# --- continue: رد کردن این دور ---
for i in range(1, 6):
    if i == 2:
        continue               # دور 2 رد می‌شود
    print(i)                   # 1,3,4,5

# حذف بازه عددی
for j in range(1, 8):
    if 4 <= j <= 6:
        continue
    print(j)                   # 1,2,3,7

# --- [CV] continue برای رد کردن فایل خراب ---
paths = ["good.jpg", "missing.jpg", "good2.jpg"]
for p in paths:
    if not p.endswith(".jpg"):
        continue
    print(f"processing {p}")

# --- break: خروج از حلقه ---
for i in range(1, 10):
    if i >= 5:
        break
    print(i)                   # 1,2,3,4

# --- [CV] break برای توقف وقتی تصویر مورد نظر پیدا شد ---
for img in ["a.jpg", "b.jpg", "target.jpg", "c.jpg"]:
    if img == "target.jpg":
        print("found target")
        break
    print(f"skipping {img}")


# =====================================================================
# بخش ۱۰ — عملگرهای انتساب (Assignment Operators)
# =====================================================================

# --- self-assignment ساده ---
wallet = 5
wallet = wallet + 1
wallet = wallet - 3
print(wallet)                  # 3

# --- با عملگرهای اختصاری ---
wallet = 5
wallet += 5                    # 10
wallet -= 6                    # 4
wallet *= 5                    # 20
wallet /= 3                    # 6.666...
print(wallet)

# --- روی رشته ---
s = "hsw"
s += "562"                     # "hsw562"
s *= 3                         # "hsw562hsw562hsw562"
print(s)

# ⚠️ روی رشته فقط += و *= کار می‌کنند
# -= و /= روی رشته خطا می‌دهند

# --- سرعت و وضوح ---
speed = 200
speed += 20
print(f"speed : {speed} km/h")  # 220

# --- با اعداد منفی ---
owed = 0
owed -= 40
print(owed)                    # -40

# --- [CV] شمارش نمونه‌ها ---
count = 0
for img in ["a.jpg", "b.jpg", "c.jpg"]:
    count += 1
print(count)                   # 3


# =====================================================================
# بخش ۱۱ — لیست‌ها
# =====================================================================

# --- ساخت لیست ---
todo = ["read", "workout", "code"]
empty = []
single = ["fine"]

characters = ["mario", "luigi", "bowser", "peach"]
temperatures = [20, 16, 12, 30, 19]

# لیست با انواع مختلف
mixed = ["jalal", 21, 15.5, True]

# --- دسترسی با ایندکس ---
print(temperatures[1])         # 16
print(temperatures[-1])        # 19 (آخرین)
print(temperatures[-2])        # 30

# --- تغییر عضو ---
temperatures[2] = 5
print(temperatures)            # [20, 16, 5, 30, 19]

# --- [CV] لیست دوبعدی (ماتریس/تصویر) ---
image = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print(image[0][1])             # 20 (سطر اول، ستون دوم)
print(image[-1][0])            # 70 (سطر آخر، ستون اول)

# --- چاپ تمام اعضا با ایندکس ---
listoo = [i for i in range(-15, 40) if i % 2 == 0]
for i, item in enumerate(listoo):
    print(f"index: {i}, element: {item}")

# --- [CV] ساخت لیست تاپلی (مقدار، ایندکس) ---
shopping_items = ["dish soap", "kleenex", "batteries"]
new = [(item, index) for index, item in enumerate(shopping_items)]
print(new)                     # [('dish soap', 0), ('kleenex', 1), ('batteries', 2)]

# --- افزودن به لیست ---
users = ["jeremy", "adam", "Liza"]
users.append("sara")           # به آخر
print(users)

users.insert(2, "Erik")        # در ایندکس 2
print(users)

# --- حذف از لیست ---
fruits = ["apple", "orange", "banana", "coconut"]
fruits.pop()                   # حذف آخرین
print(fruits)

fruits.pop(2)                  # حذف ایندکس 2
print(fruits)

remove = fruits.pop(1)         # حذف و ذخیره مقدار حذف‌شده
print(remove)

# --- [CV] پیدا کردن ایندکس یک مقدار ---
listoq = [i for i in range(-15, 40) if i % 2 == 0]
print(listoq.index(28))        # ایندکس عدد 28

# --- [CV] پیدا کردن ایندکس تمام اعضای تکراری ---
listo2 = [2, 6, 5, 6, 8, 9, 5, 4, 1]
def find_all_indexes(target):
    for index, item in enumerate(listo2):
        if target == item:
            print(f"{item} index: {index}")
find_all_indexes(5)

# --- ساخت لیست از متغیرها ---
first = "John"
second = "Joseph"
third = "Donnie"
winners = [first, second, third]
print(winners[2])

# --- لیست boolean ---
quiz_answers = [False, False, True, False]
quiz_answers.pop()
print(quiz_answers)            # [False, False, True]

# --- [CV] عملیات روی اعضای لیست (لیست اصلی تغییر نمی‌کند) ---
minutes_worked = [123, 100, 99, 67]
for minutes in minutes_worked:
    print(minutes - 60)

# [CV] ساخت لیست جدید با تغییر اعضای قبلی
new_list = []
data_points = [99, 99, 99, 99]
for data in data_points:
    new_list.append(data + 1)
print(new_list)

# روش بهتر با کامپرهنشن:
data_points = [99, 99, 99, 99]
new_list = [d + 1 for d in data_points]
print(new_list)

# --- طول لیست ---
print(len(data_points))        # 4

if len(data_points) > 2:
    print("very good")

# --- [CV] بررسی موجودی/ظرفیت ---
ingredients = ["cafe", "lemon", "cream"]
if len(ingredients) > 2:
    print("bring a bag")

# --- [CV] به‌روزرسانی یکجای لیست رشته‌ای ---
names = ["vanilla", "chocolate", "pistachio"]
updated_names = [n + "_50" for n in names]
print(updated_names)

# --- [CV] منوی غذا با ایندکس ---
meals = ["omelet", "salad", "chicken"]
print(f"breakfast: {meals[0]}")
print(f"lunch: {meals[1]}")
meals[2] = "pizza"
print(f"dinner: {meals[2]}")

# --- [CV] لیست خرید ---
shopping_list = ["dish soap", "kleenex", "batteries"]
for item in shopping_list:
    print(f"Don't forget to buy {item}")

# --- [CV] بررسی وجود/نبود با in ---
sodas = ["fanta", "cocacola", "pepsi"]
if "fanta" in sodas:
    print("fanta is available")


# =====================================================================
# بخش ۱۲ — برش لیست (Slicing) — [CV] بسیار مهم
# =====================================================================

# [CV] در CV برش برای جدا کردن ناحیه تصویر، برش بچ داده،
# و جداسازی ستون ویژگی استفاده می‌شود.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# --- برش پایه ---
numbers[2:6]                   # [2, 3, 4, 5]
numbers[:4]                    # [0, 1, 2, 3]
numbers[7:]                    # [7, 8, 9]
numbers[:]                     # کپی کامل لیست

# --- برش با گام ---
numbers[::2]                   # [0, 2, 4, 6, 8]
numbers[1::2]                  # [1, 3, 5, 7, 9]

# --- برش با ایندکس منفی ---
letters = ["A", "B", "C", "D", "E", "F", "G"]
letters[-3:]                   # ['E', 'F', 'G'] سه تای آخر
letters[:-2]                   # همه به جز دو تای آخر
letters[-4:-1]                 # ['D', 'E', 'F']

# --- برش معکوس ---
colors = ["red", "orange", "yellow", "green", "blue"]
colors[::-1]                   # معکوس کامل
colors[3:0:-1]                 # ['green', 'yellow', 'orange']
colors[::-2]                   # معکوس، یک در میان

# --- [CV] برش روی ماتریس ---
image = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
# [CV] برش سطر (ناحیه‌ای از تصویر)
image[0:2]                     # دو سطر اول
image[-1]                      # آخرین سطر
# [CV] برش ستون
first_col = [row[0] for row in image]    # [1, 5, 9]

# ⚠️ تفاوت range و slicing:
# range(start, stop, step) — تابع، آرگومان‌ها با کاما
# list[start:stop:step]   — عملگر برش، بخش‌ها با دونقطه


# =====================================================================
# بخش ۱۳ — عملیات لیست: max, min, sum, sort
# =====================================================================

numbers = [12, 6, 5, 2, 7]

# --- max و min ---
print(max(numbers))            # 12
print(min(numbers))            # 2

max_list = max(numbers)
min_list = min(numbers)
print(max_list + min_list)     # 14

# --- [CV] استفاده آماری ---
confidences = [0.7, 0.95, 0.6, 0.85]
max_conf = max(confidences)
min_conf = min(confidences)
print(f"max: {max_conf}, min: {min_conf}")

# --- sum ---
signups = [12, 30, 40, 10, 4, 8]
print(sum(signups))            # 104

sumation = sum(signups)
print(sumation)

# --- [CV] میانگین ---
savings = [220, 50, 1000, 70]
total = sum(savings)
number = len(savings)
average = total / number
print(f"average: {average}")

# --- sort ---
scores = [10, 9.25, 8, 4.5, 17, 11.75]
scores.sort()                  # درجا، صعودی
print(scores)

# نزولی
scores.sort(reverse=True)
print(scores)

# ⚠️ sort() لیست را تغییر می‌دهد و None برمی‌گرداند
# print(scores.sort())  ← چاپ None می‌کند! اشتباه رایج

# --- sorted: لیست جدید ---
data = [3, 1, 4, 1, 5]
sorted_data = sorted(data)     # لیست جدید
print(sorted_data)             # [1, 1, 3, 4, 5]
print(data)                    # [3, 1, 4, 1, 5] (اصلی دست‌نخورده)

# --- مرتب‌سازی رشته ---
names = ["cloe", "bill", "ana"]
names.sort()
print(names)                   # ['ana', 'bill', 'cloe']

grades = ["A", "C", "F", "B", "G"]
grades.sort()
print(grades)                  # ['A', 'B', 'C', 'F', 'G']

# --- min روی لیست با اعداد تکراری ---
coordinates = [0, 0, 0]
print(min(coordinates))        # 0

# --- [CV] مرتب‌سازی بر اساس کلید سفارشی (lambda) ---
samples = [
    {"image": "a.jpg", "confidence": 0.7},
    {"image": "b.jpg", "confidence": 0.95},
    {"image": "c.jpg", "confidence": 0.8}
]
samples.sort(key=lambda s: s["confidence"], reverse=True)
print(samples)                 # b, c, a


# =====================================================================
# بخش ۱۴ — الحاق، شمارش، بررسی وجود
# =====================================================================

# --- الحاق با + ---
database_1 = [1, 2, 3]
database_2 = [4, 5]
combined = database_1 + database_2
print(combined)                # [1, 2, 3, 4, 5]

# --- الحاق انواع مختلف ---
seats = [1, 2, 3]
taken = [True, True, False]
print(seats + taken)           # [1, 2, 3, True, True, False]    #type:ignore
# type: ignore
# --- [CV] الحاق لیست مشتریان و سفارشات ---
consumers = ["jess", "mike", "lyne"]
order_numbers = [3, 2, 1]
print(consumers + order_numbers)   #type:ignore

# --- count ---
answers = ["yes", "no", "sometimes", "yes", "no"]
print(answers.count("yes"))    # 2

# --- [CV] شمارش برچسب‌ها ---
free_seats = [True, False, True, True, False]
print(free_seats.count(True))  # 3

flavors = ["vanilla", "chocolate", "strawberry", "vanilla"]
print(flavors.count("vanilla"))  # 2

# --- [CV] بررسی وجود با in ---
ingredients = ["milk", "sugar", "eggs", "flour", "butter"]
has_sugar = "sugar" in ingredients
print(has_sugar)               # True

winning_numbers = [2, 36, 40, 13]
print(13 in winning_numbers)   # True
print(20 in winning_numbers)   # False

# --- [CV] بررسی شرطی ---
savings_check = [220, 50, 1000, 70]
if 50 in savings_check:
    print("found 50")

# --- [CV] مثال ترکیبی: تحلیل داده ---
data = [15, 3, 8, 20, 3, 8]
print("Max:", max(data))
print("Min:", min(data))
print("Sum:", sum(data))
print("Count of 3:", data.count(3))
print("Sorted:", sorted(data))

# --- [CV] سیستم نمرات ---
grades_list = [85, 92, 78, 90, 65]
print("Highest:", max(grades_list))
print("Lowest:", min(grades_list))
print("Average:", sum(grades_list) / len(grades_list))
grades_list.sort()
print("Sorted:", grades_list)


# =====================================================================
# بخش ۱۵ — List Comprehension — [CV] بسیار مهم
# لیست کامپرهنشن
# ================================================================

# [CV] 80٪ کاربرد کامپرهنشن در CV این سه الگوست:
#   ۱. [func(x) for x in data]         — تبدیل
#   ۲. [x for x in data if condition]  — فیلتر
#   ۳. [(x, y) for x, y in zip(a, b)]  — زیپ

# --- روش سنتی ---
prices = [10, 38, 40, 58, 62]
halved = []
for price in prices:
    halved.append(price / 2)
print(halved)

# --- با کامپرهنشن ---
halved = [price / 2 for price in prices]
print(halved)

# --- الگوی ۱: تبدیل ---
meters = [100, 3800, 4000, 2500]
kilometers = [m / 1000 for m in meters]

celsius = [0, 20, 30, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]

numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]

answers = [True, False, False, True]
opposites = [not a for a in answers]

ages = [15, 20, 17, 25, 16]
adults = [age >= 18 for age in ages]

# --- [CV] تبدیل پیکسل (نرمال‌سازی) ---
pixels = [0, 50, 100, 150, 200, 255]
normalized = [p / 255 for p in pixels]

# [CV] افزایش روشنایی
image = [10, 20, 30, 40]
scaled = [pixel * 2 for pixel in image]

# [CV] سایر عملیات پیکسلی
# [p + 10 for p in pixels]       # افزایش روشنایی
# [p - 20 for p in pixels]       # کاهش روشنایی
# [p * 3 for p in pixels]        # افزایش کنتراست
# [p ** 2 for p in pixels]       # غیرخطی

# --- الگوی ۲: فیلتر ---
scores = [12, 47, 30, 29, 19, 35, 42]
high = [s for s in scores if s > 20]

prices = [150, 45, 200, 340, 80, 120]
expensive = [p for p in prices if p > 150]

websites = ["nytimes.com", "lemonde.fr", "economist.com", "figaro.fr"]
french = [w for w in websites if ".fr" in w]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [n for n in numbers if n % 2 == 0]

# --- [CV] فیلتر محدوده روشنایی ---
pixels = [10, 120, 200, 30, 250]
bright = [p for p in pixels if 100 < p < 240]

# [CV] فیلتر پسوند فایل — خیلی رایج
files = ["cat_1.jpg", "dog_1.jpg", "cat_2.png", "cat_3.jpg"]
jpgs = [f for f in files if f.endswith(".jpg")]

# [CV] فیلتر دیتاست بر اساس confidence
dataset = [
    {"label": "cat", "confidence": 0.9},
    {"label": "dog", "confidence": 0.4},
    {"label": "cat", "confidence": 0.8}
]
good = [item for item in dataset if item["confidence"] > 0.7]
cats = [item for item in dataset if item["label"] == "cat"]

# --- شرطی با if-else (تعداد خروجی حفظ می‌شود) ---
pixels = [10, 120, 200, 30]
mask = [1 if p > 100 else 0 for p in pixels]
# [0, 1, 1, 0]

# --- ترکیب تبدیل و فیلتر ---
temperatures = [15, 20, 25, 30, 35, 40]
hot_f = [(t * 9/5) + 32 for t in temperatures if t > 25]

# --- الگوی ۳: زیپ ---
images = ["img1", "img2"]
labels = ["cat", "dog"]
pairs = [(img, label) for img, label in zip(images, labels)]
# [('img1', 'cat'), ('img2', 'dog')]

# [CV] آماده‌سازی داده آموزش
train_data = [(img, label) for img, label in zip(images, labels)]

# --- [CV] ترکیب enumerate ---
pixels = [10, 20, 30]
indexed = [(i, p) for i, p in enumerate(pixels)]
# [(0, 10), (1, 20), (2, 30)]

# --- [CV] کامپرهنشن تودرتو برای تصویر ---
image_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# فلت کردن (2D → 1D)
flat = [pixel for row in image_2d for pixel in row]
# [1,2,3,4,5,6,7,8,9]

# تبدیل با حفظ ساختار تودرتو (افزایش روشنایی)
updated_list = [[p / 2 for p in row] for row in image_2d]

# فقط تغییر یک ستون
updated_img2 = [[p / 2 if i == 2 else p for i, p in enumerate(row)]
                for row in image_2d]

# [CV] ساخت ماسک باینری
mask = [[1 if p > 100 else 0 for p in row] for row in image_2d]

# [CV] نرمال‌سازی
normalized = [[p / 255 for p in row] for row in image_2d]

# --- [CV] تولید مختصات پیکسل ---
height = 3
width = 4
coords = [(row, col) for row in range(height) for col in range(width)]
# [(0,0),(0,1),...,(2,3)]

# --- جدول ضرب ---
table = [x * y for x in range(1, 4) for y in range(1, 4)]
# [1,2,3,2,4,6,3,6,9]

# --- فیلتر مختصات ---
pairs = [(x, y) for x in range(4) for y in range(4) if x == y]
# [(0,0),(1,1),(2,2),(3,3)]

coords = [(x, y) for x in range(5) for y in range(5) if x + y < 3]

# --- سه حلقه تو در تو ---
triples = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]

# --- [CV] پردازش تصویر واقعی ---
image_matrix = [
    [10, 50, 200],
    [30, 120, 255],
    [5, 80, 160]
]

# ۱. Thresholding
binary_mask = [[1 if p > 100 else 0 for p in row] for row in image_matrix]

# ۲. حذف نویز
filtered_noise = [[p if p > 20 else 0 for p in row] for row in image_matrix]

# ۳. افزایش روشنایی با سقف
brightened = [[min(p + 30, 255) for p in row] for row in image_matrix]

# ۴. نرمال‌سازی
normalized_img = [[p / 255 for p in row] for row in image_matrix]

# ۵. استخراج ویژگی
important_pixels = [p for row in image_matrix for p in row if p > 100]

# --- [CV] Dictionary Comprehension (label encoding) ---
labels = ["cat", "dog", "car"]
label_map = {label: i for i, label in enumerate(labels)}
# {'cat': 0, 'dog': 1, 'car': 2}

# [CV] فیلتر دیکشنری
annotations = {"img1": 0.9, "img2": 0.3, "img3": 0.8}
filtered = {img: score for img, score in annotations.items() if score > 0.5}

# [CV] تبدیل ساختار
boxes = {
    "img1": [10, 20, 30, 40],
    "img2": [5, 15, 25, 35]
}
scaled = {img: [v * 2 for v in box] for img, box in boxes.items()}

# --- [CV] Generator: صرفه‌جویی حافظه ---
pixels = [1, 2, 3, 4, 5]
gen = (p * 2 for p in pixels)  # پرانتز، نه کروشه

# هنوز چیزی محاسبه نشده
print(gen)                     # <generator object>

# با next اولین عنصر
print(next(gen))               # 2

# تبدیل به لیست (همه محاسبه می‌شود)
print(list(gen))               # [4, 6, 8, 10]

# [CV] برای دیتاست بزرگ تصاویر، generator حافظه کمتری مصرف می‌کند

# --- [CV] جنریتور برای بارگذاری دسته‌ای ---
def batch_loader(paths, batch_size=2):
    for i in range(0, len(paths), batch_size):
        yield paths[i:i+batch_size]

paths = ["a.jpg", "b.jpg", "c.jpg", "d.jpg", "e.jpg"]
for batch in batch_loader(paths):
    print(batch)

# --- [CV] ترکیب کامپرهنشن و تابع ---
def halve(number):
    return number / 2

prices = [100, 200, 300, 400]
halved_prices = [halve(p) for p in prices]

# [CV] توابع آماده استفاده در کامپرهنشن
# [int(x) for x in data]
# [float(x) for x in data]
# [str(x) for x in data]
# [abs(x) for x in data]
# [round(x, 2) for x in data]

# [CV] الگوی واقعی در CV
# image_paths = [f for f in files if f.endswith(".jpg")]
# images = [load_image(p) for p in image_paths]
# labels = [item["label"] for item in dataset]
# processed = [preprocess(img) for img in images]
# dataset = [x for x in dataset if x["confidence"] > 0.8]
# train_data = [(img, label) for img, label in zip(images, labels)]

# --- Best Practice ---
# کامپرهنشن فقط وقتی خوب است که:
#   - ساده باشد (حداکثر 1 یا 2 شرط)
#   - خوانا باشد
#   - کوتاه باشد
# اگر شرط‌ها پیچیده شدند، حلقه معمولی بهتر است.


# =====================================================================
# بخش ۱۶ — تاپل
# =====================================================================

# تاپل تغییرناپذیر است (immutable)

# --- ساخت ---
movie_data = ("Inception", 2010, "Christopher Nolan")
single_item = ("",)            # تاپل تک‌عنصری (کاما لازم است)

user_profile = ("john_doe", 30, "Engineer")

# --- دسترسی ---
print(user_profile[0])         # 'john_doe'
print(user_profile[1])         # 30
print(user_profile[2])         # 'Engineer'

# --- تغییرناپذیری ---
colors = ("red", "green", "blue")
# colors[0] = "yellow"         # TypeError

# --- حلقه روی تاپل ---
coordinates = (10, 20, 30)
for coord in coordinates:
    print(f"Coordinate: {coord}")

# --- [CV] تاپل‌ها در لیست ---
students_scores = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
print(students_scores[0])       # ('Alice', 95)
print(students_scores[1][1])    # 87

# --- [CV] چاپ ایندکس با enumerate ---
tupi = ("alan", "Reza", "Salam", "Fati", "Salme")
for index, item in enumerate(tupi):
    print(f"{item} index is: {index}")

# --- [CV] بازگرداندن تاپل از تابع ---
num_list = [i for i in range(10, 50, 3)]
def tuple_maker(item):
    return max(item), min(item)

result = tuple_maker(num_list)
print(result)

# [CV] مثال کامل‌تر
scores = [85, 92, 78, 96, 88]
def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

print(calculate_stats(scores))

# --- [CV] unpacking: تفکیک مقادیر بازگشتی ---
total, avg, mx, mn = calculate_stats(scores)

# یا با * برای بقیه
first, *others = calculate_stats(scores)
print(others)                  # لیست از بقیه

# --- [CV] unpack کردن لیست بدون تابع ---
num_range = [i for i in range(-20, 40, 6)]
head, *medium, last = num_range
print(medium)
print((head, last))

# --- تبدیل لیست به تاپل ---
nums = [i for i in range(-20, 40, 6)]
tupi = tuple(nums)
print(tupi)

# --- [CV] unpack در حلقه ---
points = [(1, 2), (3, 5), (0, 8)]
for x, y in points:
    print(f"x={x}, y={y}")

# [CV] unpack سه‌بعدی
points_3d = [(1, 2, 3), (4, 5, 6)]
for x, y, z in points_3d:
    print(x, y, z)

# [CV] unpack تودرتو
students = [
    ("Ali", [18, 20, 19]),
    ("Sara", [15, 14, 16])
]
for name, (chem, eco, math) in students:
    print(f"{name}: chem={chem}, eco={eco}, math={math}")


# =====================================================================
# بخش ۱۷ — دیکشنری
# =====================================================================

# --- ساخت ---
student = {
    "name": "Ali",
    "age": 22,
    "major": "Computer Science",
    "gpa": 3.8
}

empty_dict = {}

# انواع کلید و مقدار
sample = {
    "ali": 5,
    "hadi": True,
    "hasan": "a",
    "maryam": 5.5,
    "bala": (5, 6),
    "sara": [5, 6, 9],
    "neda": {"mala": 50},
    "meri": None
}

# کلید می‌تواند: رشته، عدد، تاپل، bool، None
# کلید نمی‌تواند: لیست، دیکشنری، مجموعه (چون تغییرپذیرند)

# --- دسترسی ---
print(student["name"])         # 'Ali' (اگر کلید نباشد KeyError)
print(student["age"])

# --- دسترسی امن با get ---
print(student.get("major"))    # 'Computer Science'
print(student.get("phone"))    # None
print(student.get("phone", "N/A"))  # 'N/A' (پیش‌فرض)

# --- به‌روزرسانی ---
car = {"brand": "Toyota", "model": "Camry", "year": 2020}
car["year"] = 2022
car["color"] = "blue"          # افزودن کلید جدید
print(car)

# --- حلقه روی دیکشنری ---
for key in car:
    print(f"{key}: {car[key]}")

# فقط کلیدها
for key in car.keys():
    print(key)

# فقط مقادیر
for value in car.values():
    print(value)

# هر دو
for key, value in car.items():
    print(f"{key}: {value}")

# --- [CV] کامپرهنشن از دیکشنری ---
dico = {"ali": 5, "hadi": True, "hasan": "a"}

# لیست کلیدها
keys = [k for k in dico]

# لیست مقادیر
values = [v for v in dico.values()]

# لیست تاپل‌های (key, value)
items = [item for item in dico.items()]

# فقط کلیدها با unpack
keys = [k for k, v in dico.items()]

# فقط مقادیر
values = [v for k, v in dico.items()]

# --- [CV] Nested indexing — مهم برای دیتاست‌های تودرتو ---
inventory_system = {
    "products": {
        "laptop": {"price": 1000, "stock": 15},
        "mouse": {"price": 25, "stock": 50},
        "keyboard": {"price": 75, "stock": 30}
    },
    "categories": {"electronics", "computers", "accessories"}
}

products = [
    (k, v["price"], v["stock"])
    for k, v in inventory_system["products"].items()
]
print(products)
# [('laptop', 1000, 15), ('mouse', 25, 50), ('keyboard', 75, 30)]

# --- بررسی وجود ---
print("brand" in car)              # True
print("price" in car.keys())       # False
print("Toyota" in car.values())    # True

# --- حذف ---
inventory = {"apples": 50, "oranges": 30, "bananas": 25}
print(inventory.pop("oranges"))    # 30
print(inventory.pop("harme", "we don't have")) # پیش‌فرض  #type:ignore

# popitem: حذف آخرین جفت (بدون آرگومان)
last = inventory.popitem()
print(last)

# --- [CV] dictionary comprehension (label encoding) ---
names = ("ali", "sara", "reza")
ages = [25, 40, 34]
cities = ["baneh", "mariwan", "saqez"]
jobs = ["enginer", "doctor", "teacher"]

dictionary_1 = {i: (names[i], ages[i], cities[i], jobs[i])
                for i in range(len(ages))}

# با enumerate
dictionary_enum = {i: [names[i], ages[i], cities[i], jobs[i]]
                   for i, city in enumerate(cities)}

# عناصر یکی از مجموعه‌ها به عنوان کلید
dictionary_2 = {names[i]: [ages[i], cities[i], jobs[i]]
                for i in range(len(jobs))}

# با zip
dictionary_zip = {i: [j, d, e]
                  for i, j, d, e in zip(names, ages, cities, jobs)}


# =====================================================================
# بخش ۱۸ — مجموعه (Set)
# =====================================================================

# --- ساخت ---
my_set = {1, 2, 3}
my_set = set([1, 2, 2, 3])     # {1, 2, 3} تکرار حذف می‌شود

# [CV] مجموعه خالی حتماً با set()
empty_set = set()              # نه {} (این دیکشنری است)

# --- set comprehension ---
sets = {(i, j, f, e) for i, j, f, e in zip(names, ages, cities, jobs)}

# --- عملیات ریاضی ---
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# اجتماع
print(A | B)                   # {1, 2, 3, 4, 5, 6}
print(A.union(B))

# اشتراک
print(A & B)                   # {3, 4}
print(A.intersection(B))

# تفاضل
print(A - B)                   # {1, 2}
print(A.difference(B))

# تفاضل متقارن
print(A ^ B)                   # {1, 2, 5, 6}
print(A.symmetric_difference(B))   #type:ignore

# --- افزودن و حذف ---
s = {1, 2}
s.add(3)                       # {1, 2, 3}
s.update([4, 5])               # {1, 2, 3, 4, 5}
s.remove(3)                    # {1, 2, 4, 5} (خطا اگر نباشد)
s.discard(10)                  # بی‌خطر (خطا نمی‌دهد)
item = s.pop()                 # حذف و برگرداندن تصادفی
s.clear()                      # خالی

# --- بررسی زیرمجموعه ---
A = {1, 2}
B = {1, 2, 3, 4}
print(A.issubset(B))           # True
print(A <= B)                  # True
print(B.issuperset(A))         # True
print(B >= A)                  # True

# --- بررسی عضویت ---
fruits = {"apple", "banana", "cherry"}
print("apple" in fruits)       # True
print("kiwi" not in fruits)    # True
print(len(fruits))             # 3

# --- عملگرهای ترکیبی ---
A = {1, 2, 3}
B = {3, 4, 5}
A |= B                         # اجتماع
A &= B                         # اشتراک
A -= B                         # تفاضل
A ^= B                         # تفاضل متقارن

# --- [CV] کاربرد اصلی: حذف تکراری‌ها ---
my_list = [1, 2, 2, 3, 4, 4]
unique = list(set(my_list))    # [1, 2, 3, 4]

# [CV] لیست لیبل‌های یونیک
labels = ["cat", "dog", "cat", "bird"]
unique_labels = list(set(labels))

# --- Frozenset (تغییرناپذیر) ---
frozen = frozenset([1, 2, 3])
# frozen.add(4)                # AttributeError
# می‌توان به عنوان کلید دیکشنری استفاده کرد


# =====================================================================
# بخش ۱۹ — توابع
# =====================================================================

# --- تابع void (بدون return) ---
def greet_ron():
    name = "Ron"
    print(f"hello, {name}")

greet_ron()

def user_status():
    status = "active"
    username = "bob"
    print(f"{username} is {status}")

user_status()

# --- تابع با پارامتر ---
def greet(name):
    print(f"hello, {name}")

greet("ana")
greet("barbara")

# --- تابع با محاسبه ---
def display_half(number):
    half = number / 2
    print(half)

display_half(18)

def double_number(number):
    result = number * 2
    print(result)
    print(f"half is {number/2}")

double_number(95)

# --- تابع pure (با return) ---
def age_label(age):
    label = "user_age:" + age
    return label

print(age_label("20"))

def add_ten(number):
    total = number + " number"
    return total

print(add_ten("30"))

def update(user):
    updater = "no emails:" + user
    return updater

result = update("Ann")
print(result)

# --- تابع با محاسبه pure ---
def student_numbers(number):
    sum_value = (5 * number) / 3
    return sum_value

print(student_numbers(50))

# --- تابع با چند پارامتر ---
def display(first, last):
    print(first + " " + last)

display("Alex", "Morgan")

def show_winners(first, second, third):
    print("First place: " + first)
    print("Second place: " + second)
    print("Third place: " + third)

show_winners("Kim", "Lee", "Ava")

def combine(first, second, third):
    return first + second + third

result = combine("big", "bad", "wolf")
print(result)

def create_email(name, year):
    return name + year + "@hutmail.com"

email = create_email("jo", "1998")
print(email)

def add_prefix(prefix, word):
    return prefix + word

new_word = add_prefix("re", "do")
print(new_word)

# --- [CV] نام‌گذاری توصیفی توابع ---
def get_final_price(price, tax):
    return price + tax

def is_freezing(temperature):
    return temperature < 0

freezing = is_freezing(-3)
print(freezing)

def calculate_difference(num_1, num_2):
    return num_1 - num_2

def generate_username(name, b_day):
    return f"{name}_{b_day}"

user = generate_username("ty", 17)
print(user)

def get_free_seats(booked, total):
    return total - booked

free = get_free_seats(13, 20)
print(free)

# --- [CV] توابع با پارامتر پیش‌فرض ---
def load_image(path, size=(224, 224), normalize=True):
    # پیاده‌سازی فرضی
    return f"loading {path} at {size}, normalize={normalize}"

load_image("cat.jpg")
load_image("cat.jpg", (512, 512))
load_image("cat.jpg", normalize=False)

# --- [جدید] محدوده متغیرها (scope) ---
shipping = 10

def calculate_total(cart):
    print(cart + shipping)     # می‌تواند از متغیر بیرونی بخواند

calculate_total(54)

# تغییر متغیر بیرونی داخل تابع نیاز به global دارد
balance = 5000

def calculate_sold(sell):
    global balance             # بدون این خط، خطا می‌دهد
    balance += sell
    print("your balance:", balance)
    return balance

calculate_sold(50)
calculate_sold(100)

# ⚠️ استفاده از global توصیه نمی‌شود. راه بهتر:
def calculate_sold_better(balance, sell):
    return balance + sell

balance = calculate_sold_better(balance, 50)
print(balance)

# --- [CV] تابع با شرط ---
def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")

add_shipping(45)
add_shipping(200)

def can_drive(age):
    if age >= 18:
        print("Yes they can!")

def has_low_battery(level):
    if level <= 20:
        print("Low battery!")

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"unknown: {operator}")

# [CV] تابع با شرط برای confidence
def get_label(confidence):
    if confidence > 0.8:
        return "confident"
    elif confidence > 0.5:
        return "uncertain"
    return "reject"

# --- [CV] تابع با لیست به عنوان آرگومان ---
def display_programme(movies):
    print("Airing tonight:")
    print(movies)

movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def count_passengers(passengers):
    print(len(passengers))

passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)

def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")

top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)

# ⚠️ نکته: اگر لیست را داخل تابع تغییر دهی، لیست اصلی تغییر می‌کند
def update_first_place(player_list, player):
    player_list[0] = player
    return player_list

player_list = ["Jay", "Meg", "Cy"]
print(player_list)
player_list = update_first_place(player_list, "Lena")
print(player_list)

# --- [CV] تابع با حلقه ---
def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")

# --- [CV] تابع با لیست و حلقه ---
def halve_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")

cart_list = [5, 20, 8]
halve_prices(cart_list)

def display_players(team):
    for index, name in enumerate(team):
        print(f"Player {index}: {name}")

team_1 = ["Kim", "Lee"]
display_players(team_1)

# --- [CV] تابع با لیست مسیرها ---
def show_programme(day):
    for event in day:
        print(f"Today: {event}")

monday = ["Swan Lake", "Ravel"]
show_programme(monday)


# =====================================================================
# بخش ۲۰ — کار با فایل — [CV] بسیار مهم
# =====================================================================
'''
# [CV] در CV مدام با فایل سروکار داری: labels.txt، annotations.csv،
# مسیر تصاویر، فایل‌های config.

# --- خواندن فایل متنی ---
with open("labels.txt", "r", encoding="utf-8") as f:
    content = f.read()         # کل محتوا
    # یا خط به خط:
    # for line in f:
    #     print(line.strip())

# [CV] with تضمین می‌کند فایل حتی در صورت خطا بسته شود

# --- نوشتن فایل ---
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("result: 0.95\n")
    f.write("result: 0.87\n")

# حالت‌ها:
# "r"  خواندن (پیش‌فرض)
# "w"  نوشتن (فایل قبلی پاک می‌شود)
# "a"  افزودن به آخر
# "rb" خواندن باینری (برای تصاویر)

# --- [CV] خواندن CSV با ماژول csv ---
import csv

with open("labels.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["image"], row["label"])

# --- [CV] نوشتن CSV ---
with open("results.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["image", "label", "confidence"])
    writer.writerow(["cat.jpg", "cat", 0.95])
    writer.writerow(["dog.jpg", "dog", 0.87])

# --- [CV] [جدید] کار با مسیر فایل با pathlib (روش مدرن) ---
from pathlib import Path

# ساخت مسیر
data_dir = Path("data/train")
img_path = data_dir / "cat_001.jpg"    # الحاق مسیر با /

# خواص مسیر
img_path.name       # "cat_001.jpg"
img_path.stem       # "cat_001"
img_path.suffix     # ".jpg"
img_path.parent     # "data/train"

# بررسی وجود
img_path.exists()   # True/False
data_dir.is_dir()   # True/False

# لیست کردن فایل‌ها
# for p in data_dir.glob("*.jpg"):
#     print(p)

# لیست کردن بازگشتی (شامل زیرپوشه‌ها)
# for p in data_dir.rglob("*.jpg"):
#     print(p)

# خواندن لیست فایل‌ها
# jpg_paths = [str(p) for p in data_dir.glob("*.jpg")]

'''
# =====================================================================
# بخش ۲۱ — مدیریت خطا — [CV] حیاتی برای خواندن تصاویر خراب
# =====================================================================

# --- try/except پایه ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("تقسیم بر صفر")

# --- خطاهای رایج ---
try:
    number = int("hello")
except ValueError:
    print("رشته عدد نیست")

try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError:
    print("ایندکس خارج محدوده")

try:
    my_dict = {"name": "Ali"}
    print(my_dict["email"])
except KeyError:
    print("کلید وجود ندارد")

try:
    result = 5 + "hello"
except TypeError:
    print("انواع ناسازگار")

try:
    print(undefined_variable)   #type:ignore
except NameError:
    print("متغیر تعریف نشده")

# --- [CV] مهم‌ترین: FileNotFoundError ---
try:
    with open("image.jpg", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("فایل پیدا نشد")

# --- finally: همیشه اجرا می‌شود ---
try:
    result = 10 / 0
except ZeroDivisionError:
    print("خطا")
finally:
    print("این خط همیشه اجرا می‌شود")

# --- else: اگر خطا نبود ---
try:
    result = 10 / 2
except ZeroDivisionError:
    print("خطا")
else:
    print(f"نتیجه: {result}")    # فقط اگر خطا نبود

# --- raise: پرتاب خطای سفارشی ---
def validate_confidence(value):
    if not 0 <= value <= 1:
        raise ValueError("confidence باید بین 0 و 1 باشد")
    return value

try:
    validate_confidence(1.5)
except ValueError as e:
    print(f"خطا: {e}")

# --- [CV] الگوی خواندن ایمن تصویر ---
def safe_load_image(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print(f"not found: {path}")
        return None
    except PermissionError:
        print(f"no permission: {path}")
        return None
    except Exception as e:
        print(f"error: {e}")
        return None

# --- [CV] الگوی پردازش دسته‌ای با مدیریت خطا ---
paths = ["a.jpg", "missing.jpg", "b.jpg"]
results = []
for p in paths:
    try:
        # img = cv2.imread(p)
        # if img is None:
        #     raise ValueError(f"failed to load {p}")
        results.append(p)
    except Exception as e:
        print(f"skipping {p}: {e}")
        continue

# --- [جدید] خطاهای رایج CV ---
# FileNotFoundError: مسیر اشتباه
# cv2.error: تصویر خوانده نشد (فایل خراب یا پسوند اشتباه)
# ValueError: shape اشتباه در numpy
# MemoryError: تصویر خیلی بزرگ


# =====================================================================
# بخش ۲۲ — lambda و sort سفارشی — [CV]
# =====================================================================

# [جدید] lambda یک تابع یک‌خطی بدون نام است.

# --- lambda ساده ---
double = lambda x: x * 2
print(double(5))               # 10

add = lambda a, b: a + b
print(add(3, 4))               # 7

# --- کاربرد اصلی: sort با کلید سفارشی ---
samples = [
    {"image": "a.jpg", "confidence": 0.7},
    {"image": "b.jpg", "confidence": 0.95},
    {"image": "c.jpg", "confidence": 0.8}
]

# مرتب‌سازی بر اساس confidence نزولی
samples.sort(key=lambda s: s["confidence"], reverse=True)
print(samples)

# --- [CV] مرتب‌سازی مسیر فایل‌ها بر اساس اندازه ---
from pathlib import Path
# files = list(Path("data").glob("*.jpg"))
# files.sort(key=lambda p: p.stat().st_size)

# --- [CV] مرتب‌سازی لیست تاپل (label, score) ---
predictions = [("cat", 0.7), ("dog", 0.95), ("bird", 0.8)]
predictions.sort(key=lambda x: x[1], reverse=True)
print(predictions)

# --- [CV] max با key ---
best = max(predictions, key=lambda x: x[1])
print(best)                    # ('dog', 0.95)


# =====================================================================
# بخش ۲۳ — کلاس‌ها (فقط آنچه در CV لازم می‌شود)
# =====================================================================

# [CV] در CV، کلاس معمولاً برای ساخت Dataset loader یا مدل استفاده می‌شود.

# --- کلاس ساده ---
class Person:
    species = "Human"           # متغیر کلاس

    def __init__(self, name, age):
        self.name = name        # متغیر نمونه
        self.age = age

    def introduce(self):
        return f"Hello, I'm {self.name} and I'm {self.age} years old."

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday! Now I'm {self.age} years old."

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(person1.introduce())
print(person2.introduce())

# دسترسی به متغیرها
print(f"Person1 name: {person1.name}")
print(f"All humans are: {Person.species}")

# --- [CV] کلاس Dataset با len و getitem ---
class ImageDataset:
    def __init__(self, image_paths, labels):
        self.image_paths = image_paths
        self.labels = labels
        self.num_samples = len(image_paths)

    def get_info(self):
        return f"{self.num_samples} samples"

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        return self.image_paths[idx], self.labels[idx]

dataset = ImageDataset(["a.jpg", "b.jpg"], ["cat", "dog"])
print(len(dataset))            # 2
print(dataset[0])              # ('a.jpg', 'cat')
print(dataset.get_info())

# --- [CV] کلاس با شرط و به‌روزرسانی ---
class BankAccount:
    bank_name = "Python Bank"
    interest_rate = 0.05

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds or invalid amount"

    def get_balance(self):
        return f"Balance: ${self.balance}"

# --- ارث‌بری (الگوی پایه) ---
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        return f"{self.brand} {self.model} engine started"

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)    # فراخوانی والد
        self.num_doors = num_doors

    def open_trunk(self):
        return f"Trunk of {self.brand} {self.model} is open"

    def get_info(self):
        # فراخوانی والد
        base_info = super().get_info()
        return f"{base_info} - Doors: {self.num_doors}"

car = Car("Toyota", "Camry", 2022, 4)
print(car.get_info())
print(car.start_engine())
print(car.open_trunk())

# --- [CV] کلاس Shape (پایه برای پیاده‌سازی شکل‌ها) ---
class Shape:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, width, height, color="Blue"):
        super().__init__("Rectangle", color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius, color="Red"):
        super().__init__("Circle", color)
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

rect = Rectangle(5, 3, "Green")
circle = Circle(4, "Yellow")
print(rect.area())
print(circle.area())


# =====================================================================
# بخش ۲۴ — [CV] الگوهای آماده و پرتکرار در CV
# =====================================================================

# [CV] این بخش الگوهای واقعی است که در مسیر یادگیری CV زیاد می‌بینی.

# --- ۱. بارگذاری دسته‌ای مسیر تصاویر ---
from pathlib import Path

# [CV] همه jpg های یک پوشه
# image_paths = [str(p) for p in Path("data/train").glob("*.jpg")]

# [CV] بازگشتی (شامل زیرپوشه‌ها)
# image_paths = [str(p) for p in Path("data").rglob("*.jpg")]

# [CV] فیلتر بر اساس الگو
# cat_images = [str(p) for p in Path("data").glob("cat_*.jpg")]

# --- ۲. فیلتر دیتاست بر اساس confidence ---
dataset = [
    {"image": "img1.jpg", "label": "cat", "confidence": 0.9},
    {"image": "img2.jpg", "label": "dog", "confidence": 0.4},
    {"image": "img3.jpg", "label": "cat", "confidence": 0.8}
]
filtered = [item for item in dataset if item["confidence"] > 0.7]

# --- ۳. جفت کردن تصویر و لیبل ---
images = ["img1.jpg", "img2.jpg"]
labels = ["cat", "dog"]
pairs = list(zip(images, labels))

# --- ۴. ساخت label map ---
unique_labels = sorted(set(labels))
label_to_id = {label: i for i, label in enumerate(unique_labels)}

# --- ۵. شمارش نمونه‌های هر کلاس ---
from collections import Counter
counts = Counter(labels)
print(counts)                  # Counter({'cat': 1, 'dog': 1})

# --- ۶. نرمال‌سازی مقادیر ---
pixels = [0, 128, 255]
normalized = [p / 255 for p in pixels]

# --- ۷. ساخت ماسک باینری ---
image = [[10, 200], [150, 50]]
mask = [[1 if p > 100 else 0 for p in row] for row in image]

# --- ۸. ساخت batch از دیتاست ---
def create_batches(data, batch_size=2):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

data = [1, 2, 3, 4, 5, 6]
for batch in create_batches(data):
    print(batch)

# --- ۹. خواندن CSV لیبل‌ها ---
import csv
# with open("labels.csv") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["image"], row["label"])

# --- ۱۰. ذخیره نتایج در CSV ---
# with open("results.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["image", "prediction", "confidence"])
#     for r in results:
#         writer.writerow(r)

# --- ۱۱. [CV] پیمایش دیتاست با enumerate ---
# for idx, (img, label) in enumerate(zip(images, labels)):
#     print(f"sample {idx}: {img} → {label}")

# --- ۱۲. [CV] ساخت مسیر خروجی ---
from pathlib import Path
# output_dir = Path("outputs")
# output_dir.mkdir(exist_ok=True)
# output_path = output_dir / "result.jpg"

# --- ۱۳. [CV] الگوی کامل پردازش دیتاست ---
# from pathlib import Path
#
# def load_dataset(root_dir):
#     root = Path(root_dir)
#     samples = []
#     for class_dir in root.iterdir():
#         if not class_dir.is_dir():
#             continue
#         label = class_dir.name
#         for img_path in class_dir.glob("*.jpg"):
#             samples.append({"image": str(img_path), "label": label})
#     return samples

# --- ۱۴. [CV] تقسیم دیتاست به train و val ---
# samples = load_dataset("data")
# split_idx = int(len(samples) * 0.8)
# train = samples[:split_idx]
# val = samples[split_idx:]


# =====================================================================
# بخش ۲۵ — نکات پایانی و بهترین روش‌ها
# =====================================================================

# --- ۱. خوانایی بر کوتاهی ---
# کامپرهنشن‌های پیچیده با شرط‌های تودرتو، اگر ناخوانا شوند،
# به حلقه معمولی تبدیل کن.

# --- ۲. همیشه with open ---
# with open("file.txt") as f:
#     ...
# نه: f = open(...); f.close()

# --- ۳. مسیرها را با pathlib بساز ---
# Path("data") / "train" / "cat.jpg"
# نه: "data" + "/" + "train" + "/" + "cat.jpg"

# --- ۴. برای خواندن تصویر خراب try/except بذار ---
# در CV رایج است که بعضی تصاویر خراب باشند.

# --- ۵. enumerate و zip را ملکه ذهن کن ---
# جای for i in range(len(data)): data[i]
# از for i, x in enumerate(data): استفاده کن

# --- ۶. sorted را به sort ترجیح بده ---
# مگر اینکه عمداً بخواهی لیست اصلی تغییر کند.

# --- ۷. is None بنویس، نه == None ---
# if x is None:
# نه: if x == None:

# --- ۸. if x بنویس، نه if x == True ---
# هر مقدار falsy: 0، ""، []، None، False، {}، ()

# --- ۹. snake_case برای متغیر و تابع ---
# UPPER_CASE برای ثابت
# PascalCase برای کلاس

# --- ۱۰. برای دیتاست بزرگ از generator استفاده کن ---
# (x for x in data) به جای [x for x in data]

# --- ۱۱. tuple برای داده تغییرناپذیر ---
# مختصات، bounding box، لیبل ثابت

# --- ۱۲. دیکشنری برای متادیتا ---
# {"image": path, "label": label, "confidence": score}

# --- ۱۳. [CV] مسیرها را همیشه با Path کار کن ---
# با pathlib کراس‌پلتفرم است (ویندوز و لینوکس)

# --- ۱۴. [CV] تابع __name__ == "__main__" ---
# اسکریپت‌های CV معمولاً هم قابل اجرا هستند هم قابل import

# --- ۱۵. [CV] مدیریت خطا در حلقه پردازش دیتاست ---
# با continue از نمونه خراب بگذر، نه اینکه کل حلقه را متوقف کنی


# =====================================================================
# پایان چیت‌شیت
# =====================================================================

# =====================================================================
# یادداشت پایانی: چه چیزهایی حذف شد و چه چیزهایی اضافه شد
# =====================================================================

"""
مطالب حذف‌شده (به دلیل عدم کاربرد در مسیر جونیور CV):

۱. ارتباط با API (فایل ۱۶ کامل):
   - درخواست‌های GET، POST، PUT، PATCH، DELETE
   - مدیریت کدهای وضعیت HTTP
   - هدرها و احراز هویت
   - Session و timeout
   - پروژه سیستم مدیریت کاربران

۲. مدیریت خطا در درخواست‌های HTTP (فایل ۱۷ کامل):
   - تمام مطالب مربوط به requests
   - logging برای درخواست‌های HTTP
   - پروژه Pokemon API

۳. متغیرهای محیطی و APIهای خصوصی (فایل ۱۸ کامل):
   - os.getenv و os.environ
   - فایل‌های .env و python-dotenv
   - Query parameters
   - پروژه Config Management

۴. برنامه‌نویسی شیءگرا پیشرفته (بخش‌هایی از فایل ۱۲):
   - چندریختی (Polymorphism) با مثال‌های Animal
   - انتزاع (Abstraction) با CoffeeMachine و Computer
   - سیستم مدیریت دانشگاه (UniversityMember)
   - مقایسه برنامه‌نویسی تابعی و شیءگرا
   (فقط ارث‌بری پایه و کلاس Dataset نگه داشته شد)

۵. ماشین حساب، UserProfile، Profile و مثال‌های غیرمرتبط با CV

۶. تابع input() و چت‌بات (فایل ۱۵):
   - فقط range، break، continue، else در حلقه‌ها نگه داشته شد

۷. مثال‌های تکراری و غیرضروری:
   - تکرار print با مقادیر مشابه
   - مثال‌های سرگرم‌کننده بدون کاربرد مستقیم
   - مثال‌های پرچم و پیام‌های تشویقی

۸. Syntax Error آموزش مستقیم با exec (فایل ۱۴):
   - فقط بخش try/except نگه داشته شد

مطالب اضافه‌شده (با برچسب [جدید] در متن):

۱. بخش ۰ کامل: پیش‌نیاز، ساختار اسکریپت با __name__
۲. قواعد نام‌گذاری (snake_case, UPPER_CASE, PascalCase)
۳. گرد کردن و درصد در f-string (فرمت :.2f و :.1%)
۴. فاصله‌دهی در f-string (راست‌چین، چپ‌چین، وسط‌چین)
۵. شرط یک‌خطی (ternary)
۶. بخش کامل کار با فایل (with open، حالت‌های r/w/a)
۷. ماژول csv برای خواندن و نوشتن CSV
۸. pathlib کامل (Path، glob، rglob، name، stem، suffix)
۹. بخش کامل مدیریت خطا (try/except/finally/else/raise)
۱۰. lambda و sort سفارشی با key
۱۱. متدهای اضافی رشته (upper، lower، strip، startswith، endswith)
۱۲. generator و batch_loader
۱۳. بخش [CV] الگوهای آماده (۲۴ الگو)
۱۴. نکات پایانی و Best Practices (۱۵ مورد)
۱۵. برچسب‌گذاری [CV] روی بخش‌های مهم برای بینایی کامپیوتر

مطالب تقویت‌شده نسبت به فایل‌های اصلی:

- بخش کامپرهنشن با تمرکز روی سه الگوی طلایی CV
- بخش تاپل و دیکشنری با مثال‌های CV-محور (label encoding، bounding box)
- بخش کلاس با تمرکز روی Dataset
- بخش لیست با تأکید روی برش (slicing) که در CV حیاتی است
- بخش حلقه‌ها با enumerate و zip که در CV زیاد استفاده می‌شوند
"""
