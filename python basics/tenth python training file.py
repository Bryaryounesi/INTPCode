# فایل دهم آموزش پایتون - List Comprehensions و مفاهیم پیشرفته

# =======================================================
print("lesson name : list comprehensions & advanced concepts")
# نکته : این جزوه بسیار طولانی و برای مسیر کامپیوتر ویژن آپدیت شده ولی بخش بزرگی از مطالب شاید در پروژه های واقعی کامپیوتر ویژن هرگز استفاده نشوند. برای تمرکز بهتر روی این سه الگوی مهم تمرکز کنید : 

# 80 درصد کاربرد واقعی کامپرهنشن ها در پروژه های کامپیوتر ویژن مربوط به این سه الگوست:
# 1- [func(x) for x in data]     #استفاده از توابع درکامپرهنشن

# 2- [x for x in data if condition]   کامپرهنشن های فیلتر کننده  
# 3- [(x, y) for x, y in zip(a, b)]       کامپرهنشن های ساخته شده با زیپ
# ------------------------------
'''
جاهایی از کامپیوتر ویژن که زیاد از کامپرهنشن ها استفاده می‌شود ✅

1. مدیریت مسیر فایل‌ها
image_paths = [f for f in files if f.endswith(".jpg")]
-------------
2. بارگذاری تصاویر
images = [load_image(p) for p in image_paths]
--------------
3. استخراج لیبل‌ها
labels = [item["label"] for item in dataset]
--------------
4. فیلتر کردن دیتاست
dataset = [x for x in dataset if x["confidence"] > 0.8]
---------------
5. آماده‌سازی داده برای آموزش
train_data = [(img, label) for img, label in zip(images, labels)]
-------------
6. اعمال یک تابع روی مجموعه تصاویر
processed = [preprocess(img) for img in images]
-------------------------------------------
جاهایی که معمولاً از Comprehension استفاده نمی‌شود ❌

پردازش پیکسل‌ها
به جای:
[pixel / 255 for row in image for pixel in row]
معمولاً:
image = image / 255
------------
تغییر روشنایی
به جای:
[pixel + 20 for row in image for pixel in row]
معمولاً:
image = image + 20
--------------
فیلترهای تصویر
به جای Comprehension:
cv2.GaussianBlur(...)
cv2.Canny(...)
cv2.resize(...)
cv2.cvtColor(...)
--------------
مدل‌های یادگیری عمیق
معمولاً با PyTorch یا TensorFlow کار می‌شود نه Comprehension.
'''

# ==============================
# List Comprehensions (خلاصه‌سازی لیست)
# ==============================

#  روش سنتی ساخت لیست جدید با لوپ فور
print("--- روش سنتی ---")
prices = [10, 38, 40, 58, 62]
halved = []
for price in prices:
    half_price = price / 2
    halved.append(half_price)
print("Original prices:", prices)
print("Halved prices (traditional):", halved)
# --------------------------------------------------
# روش بهتر :  ساخت لیست با لیست کامپرهنشن
# List Comprehension
# یعنی ساخت لیست جدید از روی داده قابل پیمایش (Iterable)
# -------------------------------------------------
# new_listo = [i for i in data]   الگوی لیست کامپرهنشن
# ---------------------------------
# اجزای این الگو:
# first i : عبارت خروجی که تعیین کننده المنت های سازنده لیست جدید است
# ئای میتواند هر اسم دیگری داشته باشد اما باید عینا در لوپ هم تکرار شود
# مثلا :[pixel for pixel in image]
# second i : متغیر موقت لوپ فور که نماینده مقادیر اصلی منبع داتاست
# data : (مجموعه ای که روی آن حلقه میزنیم.(منبع داتای لیست کامپرهنشن
# داتا میتواند تاپل،رشته،دیکشنری ،ست،فایل یا خروجی توابعی مثل زیپ و اینامریت باشد
# --------------------------------------------------------
# تبدیل (transformation) و کپی (copy) مقدار اصلی در لیست کامپرهنشن
# [i/*+- & .... for i in data]   تبدیل مقدار اصلی
# [i for i in data]     کپی مقادیر داتای منبع در لیست
# --------------------------------------
# هدف از لیست کامپرهنشن در کامپیوتر ویژن:
#تبدیل پیکسل‌ها(با هدف نورمالیزه کردن، تغییر روشنایی و ...)
# - ساخت feature
# - آماده‌سازی دیتاست
# --------------------------------------------
# چند مثال برای لیست کامپرهنشن با تبدیل مقدار اصلی
# 1
halved_comprehension = [price / 2 for price in prices]
print("Halved prices (comprehension):", halved_comprehension)
# ----------------------------------------
# 2
# تبدیل متر به کیلومتر
meters = [100, 3800, 4000, 2500]
kilometers = [m / 1000 for m in meters]
print("Meters:", meters)
print("Kilometers:", kilometers)
# -------------------------
# 3
# تبدیل درجه سانتیگراد به فارنهایت
celsius = [0, 20, 30, 100]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)

# ------------------------------
# 4
# محاسبه مربع اعداد
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print("Numbers:", numbers)
print("Squares:", squares)
# ------------------------------------
# 5
# تبدیل بولین‌ها
answers = [True, False, False, True]
opposites = [not answer for answer in answers]
print("Answers:", answers)
print("Opposites:", opposites)
# ---------------------------------
# 6 تبدیل به بولین با عملگرهای مقایسه ای :(مهم

# بررسی سن قانونی
ages = [15, 20, 17, 25, 16]
adults = [age >= 18 for age in ages]
print("Ages:", ages)
print("Adults:", adults)
# -----------------------------------
# فصل ۱ : List Comprehension Fundamentals (CV Edition)
# آپدیت شده متناسب با مسیر آموزشی کامپیوتر ویژن
# ==============================
# تبدیل پیکسل (نورمالایزکردن) با لیست کامپرهنشن (ساخت لیست جدید بدون تغییر لیست اولیه)
p = print
pixels = [0, 50, 100, 150, 200, 255]

# هدف: تبدیل پیکسل ها به بازه استاندارد 0 تا 1 (Normalization)

normalized = [p / 255 for p in pixels]
# p همان متغیر موقتی است که اعمال تغییر روی آن روی تمام المنت ها اعمال میشود

print("Normalization:")
print("Original:", pixels)
print("Normalized:", normalized)
print()
# -------------------------------------------------------
# مثال بعدی:
# تبدیل پیکسل ها (مشابه افزایش روشنایی)
image = [10, 20, 30, 40]

scaled = [pixel * 2 for pixel in image]
#              ↑         ↑
#              |         └─ این حلقه پیمایش است
#              └─ کاری که روی هر پیکسل انجام می‌شود

print("Scaling image:")
print("Original:", image)
print("Scaled:", scaled)
print()
# -----------------------------------------------------
# سایر مثال های مشابه 
[p + 10 for p in pixels]
[p - 20 for p in pixels]
[p * 3 for p in pixels]
[p / 255 for p in pixels]
[p ** 2 for p in pixels]
# =======================================================
# فصل ۲ : Conditional Comprehension (if-else)
# شرطی کردن مقدار خروجی
# شرط، قبل از لوپ می آید
# =======================================================

# (به اندازه داتای اولیه پارامتر خروجی داشته باشیم) وقتی می‌خواهیم مقدار تغییر کند ولی حذف نشود
# به ازای هر ورودی، یک خروجی داریم (تعداد عناصر تغییر نمی‌کند)
# 
# شکل:
# [A if condition else B for item in data]
#  ↑          ↑      ↑
#  |          |      └─ اگر شرط غلط بود، مقدار B برمی‌گردد
#  |          └─ این شرط بررسی می‌شود
#  └─ اگر شرط درست بود، مقدار A برمی‌گردد

# نکته : اگر شرط 
# else 
# نداشته باشد، ارور میدهد
# -------------------------------------------------------
# مثال برای ساخت ماسک از یک لیست 
pixels = [10, 120, 200, 30]

# توضیح اجزای این مثال:
# ساخت mask یعنی مشخص کردن ناحیه مهم تصویر
# شرط این است: p > 100 (آیا پیکسل روشن است؟)
# 1 if p > 100 : اگر پیکسل از 100 روشن‌تر بود، مقدار 1 بگذار
# else 0 : در غیر این صورت، مقدار 0 بگذار
# خروجی mask یک لیست باینری از 0 و 1 است

mask = [
    1 if p > 100 else 0
    # ↑      ↑       ↑
    # |      |       └─ اگر شرط غلط بود
    # |      └─ شرط: آیا پیکسل از 100 روشن‌تر است؟
    # └─ اگر شرط درست بود
    for p in pixels
]

print("Binary Mask:")
print("Pixels:", pixels)
print("Mask:", mask)
print()

# نکته مهم:
# این دقیقاً پایه segmentation در CV است
# در segmentation واقعی، mask نشان می‌دهد کدام پیکسل‌ها متعلق به هدف هستند

# =======================================================
# فصل سوم :  فیلتر کردن با یک چند شرط 
# (filtering with one or Multiple Conditions)
# در اینجا حذف عنصر داریم (تعداد خروجی ممکن است کمتر از تعداد ورودی باشد)
# =======================================================
# شرط یا شرط ها بعد از لوپ می آیند
# --------------------------------------------
# مثال های فیلتر کردن با یک شرط واحد 

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
# -------------------------------------------------------
# فیلتر کردن با چند شرط 

pixels = [10, 120, 200, 30, 250]

bright = [
    p                                   # این مقداری است که نگه داشته می‌شود
    for p in pixels                     # حلقه پیمایش روی همه پیکسل‌ها
    if p > 100 and p < 240              # شرط: فقط اگر هم >100 و هم <240 باشد
    #    ↑         ↑
    #    |         └─ شرط دوم
    #    └─ شرط اول
]

print("Filtered pixels (brightness range):")
print("Original:", pixels)
print("Filtered:", bright)
print()

# نکته:
# این همان thresholding ساده است
# در CV واقعی، این روش برای حذف نویز یا استخراج محدوده خاصی از روشنایی استفاده می‌شود
# ------------------------------------------------------
# سایر مثال های فیلتر سازی با چند شرط 

# Filter with AND
pixels = [10, 50, 120, 200, 250]
result = [p for p in pixels if p > 100 and p < 240]


# Filter with OR
pixels = [10, 50, 120, 200, 250]
result = [p for p in pixels if p < 20 or p > 230]


# Filter with NOT
pixels = [10, 50, 120, 200, 250]
result = [p for p in pixels if not p > 100]


# Range Filter
pixels = [10, 50, 120, 200, 250]
result = [p for p in pixels if 100 <= p <= 200]


# Dictionary Filter
dataset = [
    {"label": "cat", "confidence": 0.9},
    {"label": "dog", "confidence": 0.4},
    {"label": "cat", "confidence": 0.8}
]

result = [
    item
    for item in dataset
    if item["confidence"] > 0.7
    and item["label"] == "cat"
]


# Multiple Conditions
dataset = [
    {"width": 120, "height": 150, "confidence": 0.9},
    {"width": 80, "height": 90, "confidence": 0.8}
]

result = [
    item
    for item in dataset
    if item["confidence"] > 0.7
    and item["width"] > 100
    and item["height"] > 100
]


# Even Number Filter
pixels = [10, 51, 120, 201, 250]
result = [
    p
    for p in pixels
    if p % 2 == 0 and p > 100
]


# Membership Filter
labels = ["cat", "dog", "car", "tree"]

result = [
    label
    for label in labels
    if label in ["cat", "dog"]
]


# File Name Filter
files = [
    "cat_1.jpg",
    "dog_1.jpg",
    "cat_2.png",
    "cat_3.jpg"
]

result = [
    file
    for file in files
    if file.endswith(".jpg")
    and "cat" in file]
# ------------------------------------------------------------------------
                             # فصل چهارم:
# چند حلقه فور  در List Comprehension
# الگو: [ result  for x in data1 for y in data2]
# کاربرد در کامپیوتر ویژن:
# ساخت مختصات تصویر یا grid
# -------------------------------------------------
# (مجموعه هایی مجزا یا زیرمجموعه هم)هر لوپ روی یک مجموعه مجزا کار می کند 

# اگر مجموعه مورد پیمایش هر لوپ از دیگری مجزا باشد هر لوپ متغیر خاص خود را دارد مثلا: 
pairs = [x+y for x in range(3) for y in range(2)]  
# میتوان از یکی یا همه این متغیرها در عبارت خروجی استفاده کرد 
# --------------------------------------------
# لیست کامپرهنشن چند لوپی با  مجموعه های زیرمجموعه هم :
# (لیست کامپرهنشن تودرتو nested list comprehension)
# الگو : [pixel for row in image for pixel in row ]

# در عبارت خروجی تنها از متغیر لوپ داخلی یا جزئی تر استفاده میشود
# اگر هر دو مجموعه را از یک مجموعه بدست بیاوریم مثلا از یک لیست تودرتو یا یک ماتریس، لوپ دوم از متغیر لوپ اول استفاده می کند مثلا 

image_2d = [
    [1, 2, 3],    
    [4, 5, 6],    
    [7, 8, 9] 
]
updated_list = [p/2 
               for row in image_2d 
               for p in row]
p(updated_list)  
# -------------------------------------------------
# لوپ داخلی و خارجی در لیست کامپرهنشن

# حلقه اول، حلقه بیرونی و کلی تر است و حلقه بعدی حلقه داخلی و جزئی تر
# یعنی اگر لیست کامپرهنشن نبود و یک لوپ فور صرف بود حلقه دوم در 
# تورفتگی حلقه اول قرار میگرفت مثل حلقه زیر 

# pairs = []
# for x in range(3):
#     for y in range(2):
#         pairs.append((x, y))
# ---------------------------------------------
# درک نحوه جفت شدن المنت های لوپ اول و دوم در مجموعه های مجزا

#  لوپ اول، اولین المنت رنج اول را با تمام المنت های رنج دوم جفت میکند سپس میرود المنت بعدی و تا آخر
p =print
pairs = [
    (x, y)
    for x in range(2)
    for y in range(3)
]

print(pairs)

# روند اجرا:
# Execution Flow:

# x = 0
#     y = 0
#     y = 1
#     y = 2
#
# x = 1
#     y = 0
#     y = 1
#     y = 2

# خروجی:
# Output:
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)] یک لیست فلت شده از تاپل ها 
#------------------------------------------------------
# حفظ ساختار تودرتوی داتای منبع 
# در لیست جدید حاصل از لیست کامپرهنشنی که چند حلقه دارد
# (مربوط به فصل ششم Matrix Processing)
# اگر بخواهیم ساختار تودرتوی داتای منبع حفظ شود باید یک کروشه درونی تعریف کنیم و لوپ بیرونی یا جزئی تر را درون آن بگذاریم و لوپ بزرگ تر بعد از این کروشه بیاید
updated_img = [[p/2 for p in row ] for row in image_2d]
# ------------------------------------------------------
# اعمال تغییر تنها روی یک ستون با حفظ ساختار تودرتو
updated_img2 = [[p/2 if i ==2 else p for i,p in enumerate(row)] for row in image_2d]
p(updated_img2)
# ------------------------------------------------------
# اعمال تغییر تنها روی یک ردیف با ایندکسینگ . با حفظ ساختار تودرتو
updated_img_3 = [[L[0]/2,L[1],L[2]] for L in image_2d]
p(updated_img_3)
# -------------------------------------------------------------
# استخراج ستون یا ردیف دلخواه از لیست های تودرتو با لیست کامپرهنشن
image_2d = [
    [1, 2, 3],    
    [4, 5, 6],    
    [7, 8, 9] 
]
first_colomn = [i[0] for i in image_2d]    #ستون اول کپی شده
first_row = [i*2 for i in image_2d[0]]        #ردیف اول تبدیل شده
# -------------------------------------------------------

# سایر مثال های لیست کامپرهنشن چند لوپه با مجموعه های مجزا
# مثال 3 - تولید مختصات
# Example 3 - Coordinate Generation

coords = [
    (x, y)
    for x in range(3)
    for y in range(3)
]

print(coords)

# کاربرد:
# Use Case:
# ساخت مختصات یک شبکه (Grid)
# ----------------------------------
# مثال 4 - جدول ضرب

table = [
    x * y
    for x in range(1, 4)
    for y in range(1, 4)
]

print(table)

# خروجی:
# Output:
# [1, 2, 3, 2, 4, 6, 3, 6, 9]
# --------------------------------------
# مثال 5 - استفاده از شرط
# Example 5 - filtering with a Condition

pairs = [
    (x, y)
    for x in range(4)
    for y in range(4)
    if x == y
]

print(pairs)

# فقط مختصات قطر اصلی
# Only diagonal coordinates

# خروجی:
# Output:
# [(0,0), (1,1), (2,2), (3,3)]
# -----------------------------------------------
# مثال 6 - فیلتر کردن مختصات
# Example 6 - Filtering Coordinates

coords = [
    (x, y)
    for x in range(5)
    for y in range(5)
    if x + y < 3
]

print(coords)

# فقط مختصات‌هایی نگه داشته می‌شوند
# که مجموع x و y کمتر از 3 باشد
# -------------------------------------------
# مثال 7 - سه حلقه تو در تو
# Example 7 - Three For Loops

triples = [
    (x, y, z)
    for x in range(2)
    for y in range(2)
    for z in range(2)
]

print(triples)

# معادل:

# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             ...
# ------------------------------------
# مثال 8 - کاربرد واقعی در Computer Vision
# Example 8 - Real CV Example

height = 3
width = 4

pixels = [
    (row, col)
    for row in range(height)
    for col in range(width)
]

print(pixels)

# خروجی:
# [
#   (0,0),(0,1),(0,2),(0,3),
#   (1,0),(1,1),(1,2),(1,3),
#   (2,0),(2,1),(2,2),(2,3)
# ]
# ----------------------------------------------------------------------
# فصل 5 : Nested List Comprehension (تصویر واقعی)
# الگو : [pixel for row in image for pixel in row ]

# کاربرد در کامپیوتر ویژن : فلات کردن تصویر 
# flatten 
# یعنی تبدیل تصویر دوبعدی به یک لیست یک بعدی 
# این کار در کامپیوتر ویژن برای ورودی دادن به مدل‌ها لازم است
# --------------------------------------------
# درک مفهوم بُعد در کامپیوتر ویژن:
# در کامپیوتر ویژن هر جفت کروشه بیانگر یک بعد مثلا
# [ ] → ۱ بعد (لیست ساده)
# [[ ]] → ۲ بعد (ماتریس)
# [[[ ]]] → ۳ بعد (مکعب یا تصویر RGB)
# ---------------------------------------------------
# مثال برای فلت کردن تصویر با لیست کامپرهنشن تودرتو

flat = [
    pixel                           # مقدار خروجی
    for row in image_2d  
    # حلقه بیرونی در لیست کامپرهنشن برای فلت کردن،  اولین لوپ ماست
    # حرکت روی ردیف ها
     # متغیر حلقه بیرونی همان ردیف ها یا سطرها هستش  : row        
    for pixel in row                # حلقه داخلی: حرکت روی پیکسل‌های هر 
]

print("Flatten Image:")
print("Original 2D:", image_2d)
print("Flattened:", flat)
print()

# نکته مهم:
# ترتیب حلقه‌ها مهم است
# اول "for row" می‌آید، بعد "for pixel"

# ==============================
# فصل ۶ : Matrix Processing (مهم‌ترین بخش CV)
# این همان مبحث تبدیل در لیست کامپرهنشن تودرتو همراه با حفظ ساختار تودرتوی اولیه است
# الگو: [[p*/+n for p in rows] for rows in image]
# [لوپ درونی روی ردیف ها  عبارت خروجی] لوپ بیرونی روی کل ماتریس تصویر ] 
# کاربرد در کامپیوتر ویژن : افزایش روشنایی پیکسل ها
# =======================================================

image_dark = [
    [10, 20],      # سطر اول: دو پیکسل
    [30, 40]       # سطر دوم: دو پیکسل
]

# توضیح اجزای این مثال:
# افزایش روشنایی یعنی اضافه کردن مقدار ثابت به همه پیکسل‌ها

brightened = [
    [pixel + 10 for pixel in row]   # این یک List Comprehension داخلی است
    #  ↑           ↑
    #  |           └─ لوپ داخلی که بر خلاف معمول بعد از مقدار خروجی است  (لوپ درون لیست کامپرهنشن داخلی، لوپ داخلی است) 
    #  └─ تبدیل مقدار خروجی با متغیر لوپ کوچکتر(درونی)
    for row in image_dark            
    # حلقه بیرونی: خارج از لیست کامپرهنشن داخلی (کروشه داخلی) قرار میگیرد
]

print("Brightness adjustment:")
print("Original:", image_dark)
print("Brightened:", brightened)
print()

# نکته:
# این پایه فیلترهای تصویر است
# در OpenCV، کارهایی مثل این را انجام می‌دهی اما خیلی سریع‌تر
# ----------------------------------------------------------------
# فصل ۷ : Dictionary Comprehension
# ساخت دیکشنری با تابع اینامریت و دیکشنری کامپرهنشن از لیست
# الگو : {key : index for index, key in enumerate(list_name)}

# تابع اینامریت یک جفت تاپلی از ایندکس و والیو را برمیگرداند و خود ما این مقادیر را به شکل دلخواه در دیکشنری میچینیم
# دقت شود که هر چه اول، بعد از لوپ فور کامپرهنشن بیاید به عنوان ایندکس درنظر گرفته میشود(صرف نظر از نام آن)
# =======================================================
labels = ["cat", "dog", "car"]    #لیست داتای منبع ما

label_map = {
    label: i                        # کلید: label ، مقدار ایندکسی: i
    for i, label in enumerate(labels)
    #  ↑    ↑        ↑
    #  |    |        └─ enumerate هر بار یک جفت (index, value) برمی‌گرداند
    #  |    └─ label همان value است (اسم دسته)
    #  └─ i همان index است (شماره دسته)
}

print("Label encoding:")
print("Original labels:", labels)
print("Label map (label → ID):", label_map)
print()

# نکته:
# این کار در کامپیوتر ویژن برای تبدیل اسم دسته‌ها به عدد قبل از آموزش مدل استفاده می‌شود

# =======================================================
# فصل ۸ : Dictionary Filtering
#ساخت دیکشنری از دیکشنری اولیه با دیکشنری کامپرهنشن و تابع آیتمز
# الگو  new_dic = {key:value for key,value in first_dic_name.items()}
# تابع آیتمز نیز کلید مقدار های دیکشنری اولیه را به شکل تاپل برمیگرداند

# ما دو المنت این تاپل را در دیکشنری جدید میچینیم 
# اگر جای کلید و مقدار را در عبارت خروجی یا عبارت لوپ جابجا کنیم جای کلید ها و مقدارها در دیکشنری جدید جابجا میشوند
# =======================================================

annotations = {
    "img1": 0.9,    #کلید مقدار اول دیکشنری منبع
    "img2": 0.3,    #کلید مقدار بعدی 
    "img3": 0.8     
}

filtered = {
    img: score                      # همان جفت کلید-مقدار را نگه می‌دارد
    for img, score in annotations.items()   # پیمایش روی همه جفت‌ها
    #    ↑    ↑           ↑
    #    |    |           └─ items() سه جفت برمی‌گرداند
    #    |    └─ مقدار (score)
    #    └─ کلید (img)
    if score > 0.5                  
    # شرط : if score > 0.5 :
    # فقط زوج‌هایی را که اطمینان بالای 0.5 دارند را نگه دار
}

print("Filtered annotations:")
print("All:", annotations)
print("Filtered (confidence > 0.5):", filtered)
print()

# =======================================================
# فصل ۹ : Dictionary Transformation
# این همان مبحث ماتریس پروسِسینگ ولی اینجا در قالب یک دیکشنری است
# یعنی دو لوپ داریم که  یکی کلی تر و بیرونی(حرکت روی کلید مقدارها) و یکی درونی (حرکت روی مقدارها) و این لوپ داخلی باید در قالبی مشابه به قالب والیوها و همراه با عبارت خروجی بیاید .
# لوپ بیرونی خارج از این قالب  نوشته میشود ولی در آن هم نام کلید و هم مقدار باید بیاید و روی نام دیکشنری همراه با تابع آیتمز اجرا میشود 

# الگو 
# new_dic = {[v*2 for v in value] for key, value in dic_name.items(()}
# =======================================================

boxes = {
    "img1": [10, 20, 30, 40],   # bounding box: [x, y, w, h]
    "img2": [5, 15, 25, 35]
}


scaled = {
    img: [v * 2 for v in box]      # برای هر bbox، همه اعداد را 2 برابر کن
    for img, box in boxes.items()  # روی همه جفت‌های دیکشنری پیمایش کن
    #    ↑    ↑
    #    |    └─ box همان لیست مثل [10,20,30,40]
    #    └─ img کلید مثل "img1"
}

print("Scaled bounding boxes:")
print("Original:", boxes)
print("Scaled (x2):", scaled)
print()

# =======================================================
# فصل ۱۰ : Generator Expression
# جنریتور یک قالب داده ای با شکل ضاهریِ شبیه به تاپل است که با کامپرهنشن قابل تولید است. 
# الگو : new_gen = (p*/+-n for p in data)

# هدف از ساخت جنریتور، حفظ حافظه رم است چون تا جریتور در زمان ساخت هیچ حافظه ای مصرف نمیکند و در هنگام فراخوانی اطلاعات درون آن تازه شروه به مصرف حافظه می کند

# =======================================================

pixels = [1, 2, 3, 4, 5]

gen = (p * 2 for p in pixels)      # پرانتز = generator
#      ↑
#      └─ هیچ محاسبه‌ای الان انجام نمی‌شود، فقط دستورالعمل ذخیره می‌شود

print("Generator output:")
print("Generator object:", gen)    # این یک شیء generator است، نه لیست
print("Convert to list:", list(gen))  # حالا محاسبه انجام می‌شود
print()
# -------------------------------
# روش های فراخوانی داده از درون جنریتور :
# 1 - با تابع نکست p(next(gen_name))  استخراج اولین عنصر جنریتور
# -----------------
# 2- با تبدیل جنریتور به لیست یا تاپل 
p(list(gen))
p(tuple(gen))
# --------------
# 3- با حلقه زدن روی جنریتور 
for i in gen:
    p(i)
# =======================================================
# فصل ۱۱ : enumerate + Comprehension
# ساخت لیستی از تاپل ها با لیست کامپرهنشن و تابع اینامریت
# الگو : tupi_list = [(idx,pixel) for idx , pixel in enumerate(data)]
# میتوان لیستی از ست ها، دیکشنری، ها لیست ها نیز ساخت با این تابع 
# =======================================================

pixels = [10, 20, 30]

result = [
    (i, p)                          # یک تاپل شامل (موقعیت، مقدار)
    for i, p in enumerate(pixels)   # i=index , p=value
    #    ↑    ↑        ↑
    #    |    |        └─ enumerate هر بار یک جفت (index, value) می‌دهد
    #    |    └─ p مقدار پیکسل است
    #    └─ i موقعیت پیکسل است
]

print("Indexed pixels (position, value):")
print("Pixels:", pixels)
print("Result:", result)
print()

# =======================================================
# فصل ۱۲ : zip + Comprehension
# مثل حالت بالاست فقط به جای ایندکس المنت لیست دوم را میگذاریم 
# میتوانیم هر مجموعه ای را در قالب لیست کامپرهنشن ، یا سایر کامپرهنشن ها به کمک زیپ بسازیم
# الگو: new_tupi_list = [(b, a) for a,b in zip(list_1 , list_2)] 
# اولین المنتی که بعد از لوپ فور درج میشود المنت لیست اول درون پرانتز زیپ است
# ترتیب و تکرار و تبدیل در عبارت خروجی کامپرهنشن میتواند متفاوت از عبارت درون لوپ باشد مثلا: test = [(b,b,a) for a,b in zip(list_1,list_2)]
# =======================================================

images = ["img1", "img2"]      # لیست نام تصاویر
labels = ["cat", "dog"]        # لیست لیبل‌ها

pairs = [
    (img, label)                         # یک جفت شامل تصویر و لیبل آن
    for img, label in zip(images, labels)  # زیپ کردن دو لیست
    #    ↑    ↑         ↑
    #    |    |         └─ zip دو لیست را جفت می‌کند
    #    |    └─ label از لیست دوم
    #    └─ img از لیست اول
]

print("Image-label pairs (using zip):")
print("Images:", images)
print("Labels:", labels)
print("Pairs:", pairs)
print()

# =======================================================
# فصل ۱۳ : Data Structure Conversion
# تنها مثال مربوط به تبدیل لیستی تاپلی به یک دیکشنری 
# الگو : new_dictionary = {values:key for key,values in data}
# میتوان در عبارت خروجی به دلخواه ترتیب کلید و مقدار رو عوض کرد
# =======================================================

data = [("img1", "cat"), ("img2", "dog")]   # لیستی از تاپل‌ها

dict_data = {
    k: v                            # کلید و مقدار
    for k, v in data                # پیمایش روی لیست تاپل‌ها
    #    ↑    ↑   ↑
    #    |    |   └─ data لیستی از تاپل‌هاست
    #    |    └─ v دومین عضو هر تاپل (value)
    #    └─ k اولین عضو هر تاپل (key)
}

print("Converted dict (list of tuples → dictionary):")
print("Original list:", data)
print("Converted dict:", dict_data)
print()

# =======================================================
# فصل ۱۴ : Best Practices 
# =======================================================

# توضیح:
# Comprehension فقط وقتی خوب است که:
# - ساده باشد (حداکثر 1 یا 2 شرط)
# - قابل خواندن باشد
# - کوتاه باشد

# اشتباه ❌ (این کد خیلی شلوغ و نامفهوم است):
# [x if x > 0 else 0 for x in data if x > 10]

# چرا بد است؟
# 1. هم فیلتر دارد (if x > 10)
# 2. هم if-else دارد (x if x > 0 else 0)
# 3. ذهن را خسته می‌کند

# بهتر ✅ (استفاده از حلقه معمولی):
# result = []
# for x in data:
#     if x > 10:
#         result.append(x if x > 0 else 0)

print("Best practice: readability > short code")
print()

# =======================================================
# مرحله CV واقعی : Image Processing
# =======================================================

# یک تصویر 3x3 شطرنجی ساده
image_matrix = [
    [10, 50, 200],   # سطر اول: سه پیکسل
    [30, 120, 255],  # سطر دوم: سه پیکسل (255 = سفید کامل)
    [5, 80, 160]     # سطر سوم: سه پیکسل
]

print("=" * 50)
print("Image Processing Examples (Real CV)")
print("=" * 50)
print("Original image matrix (3x3):")
for row in image_matrix:
    print(row)
print()

# -------------------------------------------------------
# ۱. Thresholding (ساخت باینری ماسک)
# -------------------------------------------------------

binary_mask = [
    [1 if pixel > 100 else 0 for pixel in row]   # در هر سطر، شرط را روی هر پیکسل اعمال کن
    for row in image_matrix                       # روی همه سطرها پیمایش کن
]

print("1. Binary Mask (1 if pixel > 100 else 0):")
print("توضیح: هر پیکسل روشن‌تر از 100 می‌شود 1، بقیه می‌شوند 0")
for row in binary_mask:
    print(row)
print()

# -------------------------------------------------------
# ۲. حذف نویز (Noise Filtering)
# -------------------------------------------------------

filtered_noise = [
    [pixel if pixel > 20 else 0 for pixel in row]   # اگر پیکسل <=20 بود، تبدیل به 0 کن
    for row in image_matrix
]

print("2. Noise Filtering (remove pixels <=20):")
print("توضیح: پیکسل‌های خیلی تاریک (<=20) نویز فرض می‌شوند و حذف می‌شوند (تبدیل به 0)")
for row in filtered_noise:
    print(row)
print()

# -------------------------------------------------------
# ۳. افزایش روشنایی (Brightness Adjustment)
# -------------------------------------------------------

brightened_img = [
    [min(pixel + 30, 255) for pixel in row]   # 30 واحد اضافه کن، ولی از 255 بیشتر نشود
    for row in image_matrix
]

print("3. Brightness Adjustment (+30, max 255):")
print("توضیح: به هر پیکسل 30 واحد اضافه می‌شود اما حداکثر 255 (سفید کامل)")
for row in brightened_img:
    print(row)
print()

# -------------------------------------------------------
# ۴. نرمال‌سازی (Normalization)
# -------------------------------------------------------

normalized_img = [
    [pixel / 255 for pixel in row]   # تقسیم بر 255 تا عدد بین 0 تا 1 شود
    for row in image_matrix
]

print("4. Normalization (convert 0-255 range to 0-1):")
print("توضیح: در یادگیری ماشین، داده‌ها باید معمولاً در بازه 0 تا 1 باشند")
for row in normalized_img:
    print([round(p, 2) for p in row])   # round فقط برای نمایش بهتر
print()

# -------------------------------------------------------
# ۵. استخراج ویژگی‌ها (Feature Extraction)
# -------------------------------------------------------

important_pixels = [
    pixel                           # مقدار پیکسل
    for row in image_matrix         # حلقه بیرونی: روی سطرها
    for pixel in row                # حلقه داخلی: روی پیکسل‌ها
    if pixel > 100                  # شرط: فقط پیکسل‌های روشن (>100)
]

print("5. Feature Extraction (pixels > 100):")
print("توضیح: فقط پیکسل‌های روشن از تصویر استخراج می‌شوند (تبدیل 2D به 1D)")
print("Important pixels:", important_pixels)
print()

# =======================================================
# مرحله Data Pipeline (دیتاست در CV)
# =======================================================

dataset = [
    {"image": "img1", "label": "cat", "confidence": 0.9},
    {"image": "img2", "label": "dog", "confidence": 0.4},
    {"image": "img3", "label": "cat", "confidence": 0.8}
]

print("=" * 50)
print("Data Pipeline Examples (CV Dataset)")
print("=" * 50)
print("Original dataset:")
for item in dataset:
    print(item)
print()

# -------------------------------------------------------
# ۱. فیلتر کردن دیتاست
# -------------------------------------------------------

filtered_dataset = [
    item                                # کل آیتم را نگه می‌دارد
    for item in dataset                 # روی همه آیتم‌ها پیمایش می‌کند
    if item["confidence"] > 0.7         # شرط: فقط آیتم‌هایی با اطمینان بالا
]

print("1. Dataset filtering (confidence > 0.7):")
print("توضیح: نمونه‌هایی که اطمینان مدل در آنها پایین است حذف می‌شوند")
for item in filtered_dataset:
    print(item)
print()

# -------------------------------------------------------
# ۲. استخراج لیبل‌ها
# -------------------------------------------------------

labels_extracted = [
    item["label"]               # فقط فیلد label هر آیتم را می‌گیرد
    for item in dataset         # روی همه آیتم‌ها پیمایش می‌کند
]

print("2. Label extraction:")
print("توضیح: از هر آیتم فقط لیبل آن استخراج می‌شود")
print("Labels:", labels_extracted)
print()

# -------------------------------------------------------
# ۳. تبدیل لیبل به عدد (Encoding)
# -------------------------------------------------------

label_map_cv = {"cat": 0, "dog": 1}   # فرهنگ تبدیل اسم به عدد

encoded = [
    label_map_cv[item["label"]]        # مقدار عددی مربوط به هر لیبل
    for item in dataset                # روی همه آیتم‌ها پیمایش می‌کند
]

print("3. Label encoding (cat→0, dog→1):")
print("توضیح: مدل‌های یادگیری ماشین عدد می‌فهمند نه اسم، پس لیبل‌ها را عدد می‌کنیم")
print("Encoded labels:", encoded)
print()

# -------------------------------------------------------
# ۴. ساخت دیتاست آماده آموزش
# -------------------------------------------------------

train_data = [
    (item["image"], item["label"])      # یک جفت (تصویر، لیبل)
    for item in dataset                 # روی همه آیتم‌ها پیمایش می‌کند
]

print("4. Training data preparation:")
# --------------------------------------------------------------------------
# توابع در کامپرهنشن ها در کامپیوتر ویژن 
# Function Calls Inside Comprehensions
# =====================================================
# Pattern 1 - Function Call
# الگوی پایه :# [func(x) for x in data]
# -----------------------------------------------------
# رایج‌ترین مثال‌ها:

[int(x) for x in data]          # تبدیل به عدد صحیح

[float(x) for x in data]        # تبدیل به اعشاری

[str(x) for x in data]          # تبدیل به رشته

[abs(x) for x in data]          # قدر مطلق

[round(x, 2) for x in data]     # گرد کردن

[len(x) for x in data]          # طول داده

[sorted(x) for x in data]       # مرتب سازی

[sum(x) for x in data]          # جمع عناصر

[max(x) for x in data]          # بیشترین مقدار

[min(x) for x in data]          # کمترین مقدار

# -----------------------------------------------------
# Pattern 2 - Function + Condition
# تابع همراه با فیلتر

# [func(x) for x in data if condition]
# -----------------------------------------------------
# رایج‌ترین مثال‌ها:
[int(x) for x in data if x > 0]

[abs(x) for x in data if x < 0]

[round(x, 2) for x in data if x > 100]

[str(x) for x in data if x != 0]

[len(x) for x in data if len(x) > 3]

# -----------------------------------------------------
# Pattern 3 - Nested Function Call
# تابع روی عناصر ماتریس یا تصویر

# [func(pixel) for row in image for pixel in row]
# -----------------------------------------------------

# رایج‌ترین مثال‌ها:
[int(pixel) for row in image for pixel in row]

[float(pixel) for row in image for pixel in row]

[round(pixel, 2) for row in image for pixel in row]

[abs(pixel) for row in image for pixel in row]

# -----------------------------------------------------
# Pattern 4 - Custom Function
# تابعی که خودمان نوشته‌ایم
# -----------------------------------------------------
# [preprocess(img) for img in dataset]

# رایج‌ترین مثال‌ها در CV:
'''
[load_image(path) for path in image_paths]

[resize_image(img) for img in images]

[normalize(img) for img in images]

[extract_features(img) for img in images]

[augment(img) for img in images]

[to_grayscale(img) for img in images]

[preprocess(img) for img in images]

[get_label(img) for img in images]

'''
# -----------------------------------------------------
# Pattern 5 - Nested Custom Function
# تابع روی تک تک پیکسل‌های تصویر
# [preprocess_pixel(pixel) for row in image for pixel in row ]
# -----------------------------------------------------
# رایج‌ترین مثال‌ها:
'''
[
    threshold(pixel)
    for row in image
    for pixel in row
]

[
    normalize_pixel(pixel)
    for row in image
    for pixel in row
]

[
    remove_noise(pixel)
    for row in image
    for pixel in row
]

[
    adjust_brightness(pixel)
    for row in image
    for pixel in row
]

'''
# -----------------------------------------------------
# مهم‌ترین کاربردهای واقعی در Computer Vision
# -----------------------------------------------------

# بارگذاری تصاویر
# [load_image(path) for path in image_paths]

# تغییر اندازه تصاویر
# [resize_image(img) for img in images]

# نرمال سازی تصاویر
# [normalize(img) for img in images]

# تبدیل به خاکستری
# [to_grayscale(img) for img in images]

# استخراج ویژگی
# [extract_features(img) for img in images]

# افزایش داده (Data Augmentation)
# [augment(img) for img in images]

# استخراج لیبل‌ها
# [get_label(img) for img in images]

# پیش پردازش کامل دیتاست
# [preprocess(img) for img in images]

# .......مطالب مهم کامپرهنشن ها در رابطه با کامپیوتر ویژن به پایان رسید ...............
# -----------end of comprehension subject about computer vision ----------------------




# سایر مثال های پایتون در مبحث لیست کامپرهنشن، سلایسینگ لیست و ...
# توابع در لیست کامپرهنشن و ...
# ---------------------------------------------------------------
# استفاده از توابع در List Comprehensions
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