# فایل نهم آموزش پایتون - تاپل‌ها، دیکشنری‌ها و مجموعه‌ها
# =====================================================

from email.policy import default


print("lesson name : tuples, dictionaries & sets operations")

# ==============================
# تاپل‌ها (Tuples)
# ==============================

print("=== بخش تاپل‌ها ===")

# ایجاد تاپل‌های ساده
movie_data = ("Inception", 2010, "Christopher Nolan")
print("Movie data tuple:", movie_data)

# تاپل تک عنصری
single_item = ("",)
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
# ---------------------------------------------------
p = print
# چاپ یکجای ایندکس عناصر یک تاپل با enumerate
tupi = ("alan","Reza","Salam","Fati","Salme")
for index,item in enumerate(tupi):
    p(f"{item} index is :{index}")
# ----------------------------------------
# ساخت لیست تاپلی با enumerate
tupist = [(item,index) for index,item in enumerate(tupi)] 
p(tupist)

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
p = print
num_list = [i for i in range(10,50,3)]
def tuple_maker(item):
    return max(item), min(item)    #تابع پرینت ندارد و از نوع pure
resut = tuple_maker(num_list)    #آرگومان یک لیست عددی است
p(resut)
# -------------------------------------
scores = [85, 92, 78, 96, 88]
def calculate_stats(numbers):
    """تابعی که چند مقدار را در قالب تاپل برمی‌گرداند"""
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum
p(calculate_stats(scores))
# -------------------------------------
# تفکیک مقادیر بازگشتی(unpacking) 
# یعنی ساخت یکجای چند متغیر از روی محتوای بازگشتی تابع

# (البته هر شیء تکرار پذیر اعم از لیست،تاپل، دیکشنری، رشته و ... 
# قابل آنپک است و نه الزاما مقدار بازگشتی تابع)

# میتوان به اندازه المنتای مقدار برگشتی متغیر ساخت 
# (تعداد متغیرها باید دقیقا با اعزای تاپل برابر باشد وگرنه ارور می دهد) 
# مثلا:
total, avg, max, min = calculate_stats(scores)

# یا به اندازه ای دلخواه، متغیر ساخت و بقیه محتوا را در یک متغیر ذخیره کرد مثلا: 
first , *others = calculate_stats(scores)
p(others)
# محتوای متغیر ستاره دار یک لیست خواهد بود حتی اگر مقدار بازگشتی ، یک تاپل باشد
# ----------------------------------------------
# مثال بعدی از unpacking
p = print
num_list = [i for i in range(10,50,3)]
def tuple_maker(item):
    return max(item), min(item), (sum(item)/len(item))      #مقدار برگشتی، یک تاپل است

first, *second = tuple_maker(num_list)
p(f"first  element is :{first} and  second is :{second}")
# ---------------------------------------------
# مثال برای آنپک یک لیست، بدون تابع
num_range = [i for i in range(-20,40,6)]
head, *medium, last = num_range
p(medium)  
p((head,last))
# ---------------------------------------
# تبدیل لیست به تاپل با تابع داخلی tuple
p = print
nums = [i for i in range(-20,40,6)]
tupi  = tuple(nums)
p(tupi)

print("-------------------------")
# ==============================
# دیکشنری‌ها (Dictionaries)
# ==============================
print("=== بخش دیکشنری‌ها ===")
# dic = {key1:value1, key2:value2, . . .}  الگوی ساخت دیکشنری 
# -----------------------------------------
# انواع کلید و مقدار در ساخت دیکشنری
sample = {"ali":5 ,
       "hadi" : True , 
       "hasan" : "a",
       "mryam" : 5.5,
       "bala" : (5,6) , 
       "sara" : [5,6,9,8] , 
       "neda" :{"mala" : 50} ,
       "meri" : None , 
       1 : "any above items " , 
       2.5 :"any above items " , 
       (2,3) : "any above items " , 
       }
p(sample)
# کلید نمیتواند لیست ،دیکشنری یا مجموعه باشد
# کلید میتواند بولین یا ناون باشد ولی چندان رایج نیست
# -----------------------------------------
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
# p(dic_name[key])    طبق این الگو 
# اگر کلید وجود نداشته باشد، ارور میدهد
# -------------------------------------
print("Student name:", student["name"])
print("Student age:", student["age"])

# -------------------------------------
# دسترسی امن با get()
# p(dic_name.get(key))   طبق این الگو
# اگر کلید موجود نباشد ارور نداده و ناون را برمیگرداند
# میتوان یک والیوی پیش فرض دلخواه به تابع بدهیم که اگر کلید وجود نداشت به جای ناون برگرداند
# مثلا:
# p(dic_name.get(key, default_value)
# ---------------------------------------
print("Student major:", student.get("major"))

print("Unknown key:", student.get("phone", "Not available"))
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
# for i/any other name  in dic:          طبق الگو
    # p(i , dic[i])          #i بیانگر کلید هاست      #dic[i]  بیانگر والیوهاست
# ----------------------------------------
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
# لیست کامپرهنشن از دیکشنری ها (تبدیل دیکشنری ها به لیستی از مجموعه های دیگر با لیست کامپرهنشن)
# خیلی مهم

# List Comprehension from Dictionaries
# فقط کلیدها (لوپ مستقیم روی دیکشنری)

# این دیکشنری را داریم که میخواهیم با لیست کامپرهنشن آن را به لیستی از چیزی دیگر تبدیل کنیم
p = print
dico = {"ali":5 ,
       "hadi" : True , 
       "hasan" : "a",
       "mryam" : 5.5,
       "bala" : (5,6) , 
       "sara" : [5,6,9,8] , 
       "neda" :{"mala" : 50} ,
       "meri" : None , 
       1 : "any above items " , 
       2.5 :"any above items " , 
       (2,3) : "any above items " , 
       }

[i for i in dico]
# فقط کلیدها (keys)
# با این کد، لیستی از کلید ها میسازیم 
# ------------------------------------
[i for i in dico.keys()]
# این هم  فقط کلیدها (keys)
# ----------------------------------
[i for i in dico.values()]
# فقط مقدارها (values)
# لیستی از والیوهای دیکشنری
# --------------------------------
[i for i in dico.items()]
# لیست تاپل‌های (key, value)
# لیستی از تاپل های متشکل از کلید و مقدار آنها
# ----------------------------------------------------
[key for key, value in dico.items()]
# فقط کلیدها (باز کردن items)
# تاپل هایی کلید مقداری ساخته میشود ولی تنها کلید های آنها را میگیریم
# نکته میتوان به جای کِی و والیو هر پارامتر دیگری را نوشت. مهم آنپک کردن مقدار بازگشتی آیتم است
# مثلا:
new = [i for i,j in dico.items() ]
# ----------------------------------
[value for key, value in dico.items()]
# فقط مقدارها (باز کردن items)
# تاپل هایی کلید مقداری ساخته میشود ولی تنها مقدار های آنها را میگیریم
# مثال با پارامترهایی با اسامی متفاوت
new2 = [j for i,j in dico.items()]
# --------------------------------------
[(key, value) for key, value in dico.items()]
# لیست تاپل‌های (key, value) به صورت صریح
# تاپل هایی کلید مقداری ساخته میشود و ما این تاپل ها را در یک لیست میچینیم و لیستی از آنها میسازیم
new3 = [(i,j) for i,j in dico.items()]
# --------------------------------------
[[key, value] for key, value in dico.items()]

# لیست از لیست‌های [key, value]
# تاپل هایی کلید مقداری ساخته میشود ولی ما آنها را به لیست تبدیل کرده و لیستی از این لیست ها میسازیم
# --------------------------------------
[i[0] for i in dico.items()]
# کلیدها با ایندکسینگ روی items
# تاپل هایی کلید مقداری ساخته میشود ولی ما با ایندکس تنها بخشی از آنها را در یک لیست میچینیم
# --------------------------------------
[i[1] for i in dico.items()]

# مقدارها با ایندکسینگ روی items
# تاپل هایی کلید مقداری ساخته میشود ولی ما با ایندکس تنها بخشی از آنها را در یک لیست میچینیم
# --------------------------------------
[i[1][0] for i in dico.items()]
# ایندکسینگ تودرتو روی value های چندبخشی(nested indexing----nested dictionaries)
# تاپل هایی کلید مقداری ساخته میشود  ما با ایندکس،
# بخشی از این تاپل را که خود یک مجموعه از اجزایی کوچکتر است جدا میکنیم(با ایندکس درون کروشه اول)
# سپس بخشی از این اجزای کوچکتر را دوباره با ایندکس مشخص میکنیم(با ایندکس درون کروشه های بعدی)
# ----------------------------------------
#  مثال برای ساخت لیست هایی دلخواه از یک دیکشنری با ایندکسینگ تودرتو
# بسیار مهم
p = print
inventory_system = {
    "products": {
        "laptop": {"price": 1000, "stock": 15},
        "mouse": {"price": 25, "stock": 50},
        "keyboard": {"price": 75, "stock": 30}
    },
    "categories": {"electronics", "computers", "accessories"}
}
products = [(i[0], i[1]["price"], i[1]["stock"]) for i in inventory_system["products"].items()]
# دو کلید اصلی در دیکشنری داریم با مقادیر مختلف،
# پس ساخت لیست از هر کدام را به صورت مجزا انجام میدهیم
# inventory_system["products"].items() # میگه کلید مقدارهای کلید اصلی اول رو به شکل تاپلی برگردان
# i[0]  #کلید های فرعی کلید اول  
# i[1]["price"]  والیوهای کلید پرایس از والیوی دیکشنریِ کلیدهای فرعی
# i[1]["stock"]   والیوهای کلید استوک از والیوی دیکشنریِ کلیدهای فرعی
categories = [(i[0],list(inventory_system["categories"])) for i in inventory_system.items() if i[0] =="categories"]
# i[0] اسامی کلید های اصلی یعنی پروداکز و کتگوری
# if i[0] =="categories"  بعد با این شرط میگه صرفا کتگوری رو بررسی کن
# list(inventory_system["categories"])   محتوای تبدیل به لیست شده کلید کتگوری

# p(products + categories)   الحاق دو لیست به هم
# --------------------------------------------------------
# بررسی وجود کلید در دیکشنری
print("Is 'brand' in car?", "brand" in car)       # بررسی در کل دیکشنری
print("Is 'price' in car?", "price" in car.keys())    #بررسی وجود در کلید ها
print("Is 'price' in car?", "price" in car.values())    #بررسی وجود در والیوها
# ------------------------------------------------------
# حذف از دیکشنری
# dictionary_name.pop(key,default_value)

# اگر کلید در دیکشنری باشد، کلید مقدار را حذف میکند
# اگر نباشد و این عبارت را پرینت کنیم، ارور میدهد مگر اینکه یک والیوی پیشفرض به پاپ بدیم 
# تا در پرینت، آن والیو چاپ شود و ارور نبینیم
# اگر پرانتز پاپ را خالی بگذاریم، برخلاف لیستها در دیکشنری ها  المنت آخر حذف نمیشود و ارور میدهد
inventory = {
    "apples": 50,
    "oranges": 30,
    "bananas": 25,
    "grapes": 40
}
print("Original inventory:", inventory)

# حذف با pop
p(inventory.pop("oranges"))
p(inventory.pop("harme", "we dont have this fruit"))
# ---------------------------------------
# حذف آخرین کلید مقدار  با popitem 
# dic_name.popitem()   الگو

# این تابع، هیچ آرگومانی ندارد پس همیشه باید پرانتزش خالی باشد
# آخرین کلید مقدار دیکشنری را حذف میکند مثل list.pop()
last_item = inventory.popitem()
print(f"Removed last item: {last_item}")
print("After popitem:", inventory)
# ----------------------------------------------
# حذف در دیکشنری با ایندکس
# دیکشنری، ایندکس عددی ندارد و صرفا با کلید میتوان عناصر آن را حذف کرد

# ----------------------------------------------------------
# ساخت دیکشنری با دیکشنری کامپرهنشن
# دیکشنری کامپرهنشن دقیقا شبیه لیست کامپرهنشن است
# با این تفاوت که باید به جای کروشه یک آکولاد بازکنیم و سپس یک کلید تعریف کنیم
p = print

names = ("ali","sara","reza")
ages = [25,40,34]
cities = ["baneh","mariwan","saqez"]
jobs = ["enginer","doctor","teacher"]
dictionary_1 ={i : (names[i],ages[i],cities[i],jobs[i]) for i in range(len(ages))}
# p(dictionary_1)
# ایندکس تبدیل به کلید میشود و عناصر لیست ها تبدیل به والیوی تاپلی
# -------------------------------------------------
dictionary_enum = { i: [names[i],ages[i],cities[i],jobs[i]] for i,city in enumerate(cities)}
p(dictionary_enum)

# همان مثال بالا با enumerate
# -----------------------------------------------------------------
dictionary_2 = {names[i] : [ages[i],cities[i],jobs[i]] for i in range(len(jobs))}
# p(dictionary_2)
# عناصر یکی از مجموعه ها تبدیل به کلید میشوند 
# اگر در رنج، لیستی را بیاریم که عناصر بیشتری از بقیه دارد، کد ارور میدهد
# -----------------------------------------------------------------
dictionary_zip = {i : [ j , d , e] for i , j , d, e in zip(names,ages,cities,jobs)}
# p(dictionary_zip)
# همان مثال بالا با زیپ
# ----------------------------------------------
# ==============================
# مجموعه‌ها (Sets)
# کیفی با تنها یک نسخه از مدارک (با عناصر غیر تکراری و یونیک) و بدون ترتیب مشخص (بدون ایندکس)
# ==============================

print("=== بخش مجموعه‌ها ===")

# ۱. ساخت مجموعه
# با آکولاد
my_set = {1, 2, 3}
# -------------------------------------
# (ساخت ست از روی لیست (تکرارها حذف می‌شوند
my_set = set([1, 2, 2, 3])  # {1, 2, 3}
# -----------------------------------------------
p = print
names = ("ali","sara","reza")
ages = [25,40,34]
cities = ["baneh","mariwan","saqez"]
jobs = ["enginer","doctor","teacher"]

# ساخت ست با ست کامپرهنشن
sets = {(i,j,f,e) for i,j,f,e in zip(names,ages,cities,jobs)}
# ---------------------------------------------------
#  ساخت مجموعه خالی (حتما با set())

empty_set = set()  # استفاده از {} دیکشنری می‌سازد
# ---------------------------------------
# ۲. عملیات اصلی مجموعه ها (برگرفته از ریاضیات)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
# اجتماع (Union)
# همه اعضای دو مجموعه، بدون تکرار.

A | B           # {1, 2, 3, 4, 5, 6}
A.union(B)      # معادل متدی
# تقریبا کار + در الحاق لیست ها را در مجموعه ها می کند
# -----------------------------------
# اشتراک (Intersection)
# اعضای مشترک در هر دو مجموعه.

A & B           # {3, 4}
A.intersection(B)
# -----------------------------------
# تفاضل (Difference)
# اعضایی که در اولی هست ولی در دومی نیست.

A - B           # {1, 2}
A.difference(B)

B - A           # {5, 6}
# --------------------------------------
# تفاضل متقارن (Symmetric Difference)
# اعضایی که یا در اولی هستند یا در دومی، اما نه در هر دو.

A ^ B           # {1, 2, 5, 6}
A.symmetric_difference(B)
# ----------------------------------------------
# ۳. اضافه و حذف عضو در ست
# افزودن به ست 
# حذف از ست

s = {1, 2}

# اضافه کردن یک عضو به ست
s.add(3)        # {1, 2, 3}

# اضافه کردن چند عضو به ست
s.update([4, 5])  # {1, 2, 3, 4, 5}

# حذف عضو (خطا می دهد اگر عضو  در ست موجود نباشد)
s.remove(3)     # {1, 2, 4, 5}

# حذف امن از ست (بدون خطا اگر نباشد)
s.discard(10)   # مجموعه تغییر نمی‌کند

# حذف و برگرداندن یک عضو تصادفی
item = s.pop()
# p(item) منطور از برگرداندن یعنی اگر پرینت کنیم، والیو چاپ میشود

# خالی کردن مجموعه
s.clear()       # set()
# -----------------------------------------------
# ۴. بررسی زیرمجموعه و فرامجموعه در ست ها

A = {1, 2}
B = {1, 2, 3, 4}

A.issubset(B)   # True - آیا A زیرمجموعه B است؟
A <= B          # True

B.issuperset(A) # True - آیا B فرامجموعه A است؟
B >= A          # True

# زیرمجموعه/فرامجموعه محض (برابر نباشند)
A < A           # False (زیرمجموعه محض)
A <= A          # True (زیرمجموعه)
# ------------------------------------------------
# ۵. بررسی عضویت و طول مجموعه

fruits = {"apple", "banana", "cherry"}

"apple" in fruits     # True
"kiwi" not in fruits  # True

len(fruits)           # 3
# --------------------------------------
# ۶. عملگرهای ترکیبی (درجا، سلف اساینمنت)
# این عملگرها مجموعه اصلی را تغییر می‌دهند.


A = {1, 2, 3}
B = {3, 4, 5}

A |= B   # A = A | B → {1, 2, 3, 4, 5}  تبدیل ئا به اجتماع ئا و بِ
A &= B   # A = A & B → {3, 4, 5}      تبدیل ئا به اشتراک ئا و بِ
A -= B   # A = A - B → set()
A ^= B   # A = A ^ B
# ---------------------------------------
# ۷. مجموعه‌های منجمد (Frozenset)
# اگر به مجموعه‌ای تغییرناپذیر نیاز دارید (مثلاً به عنوان کلید دیکشنری):

frozen = frozenset([1, 2, 3])  
# frozen.add(4)  # خطا: AttributeError
# در اینجا یک لیست به عنوان یک شیء تکرار شونده به فروزنست داده شده تا به مجموعه منجمد تبدلش کند

d = {frozen: "مقدار"}  # مجاز است
# نکته کاربردی مفید: یکی از بهترین کاربردهای مجموعه، حذف سریع مقادیر تکراری از لیست و بررسی عضویت است.


my_list = [1, 2, 2, 3, 4, 4]
unique = list(set(my_list))  # [1, 2, 3, 4] (ترتیب حفظ نمی‌شود)

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
# ساخت دیکشنری با لوپ فور
students_dict = {}
for student_id, name, gpa in students:
    students_dict[student_id] = {"name": name, "gpa": gpa}
# -----------------------------------------------------    
# روش بهتر برای تبدیل لیست به دیکشنری با لیست کامپرهنشن
# ساخت دیکشنری با دیکشنری کامپرهنشن و ایندکسینگ تاپل
dicti = {i[0]: [i[1],i[2]] for i in students}
# p(dicti)
# -----------------------------------------------------

# مثال برای ایندکس گذاری تودرتو(nested indexing)
# مثلا یک لیست داریم که سه تا تاپل داره
p(students[1][2])    #اینجا میگه در تاپل دوم المنت سوم رو بده
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
survey_a = {"", "java", "javascript", "c++"}
survey_b = {"", "javascript", "go", "rust"}

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
# p(group1 & group2 & group3) میتوان به این شکل هم نوشت

print("Common courses in all groups:", common_courses)

# تمام دروس منحصر به فرد
all_unique_courses = group1.union(group2, group3)
print("All unique courses:", all_unique_courses)

print("End of tuples, dictionaries & sets training")