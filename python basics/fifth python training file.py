# فایل پنجم آموزش پایتون - لیست‌ها (Lists)
# ==============================

print("Lesson: lists")
# ==============================
# ایجاد و نمایش لیست‌ها
# ==============================

# لیست پایه
todo = ["read", "workout", "code"]
print(todo)

print("--------------------------")

# لیست خالی
todo = []
print(todo)

print("--------------------------")

# لیست با یک المنت
active_users = ["fine"]
print("active:")
print(active_users)

print("--------------------------")

# لیست رشته‌ها
characters = ["mario", "luigi", "bowser", "peach"]
print(characters)

print("--------------------------")

# لیست اعداد
temperature = [20, 16, 12, 30, 19]
print(temperature)

print("--------------------------")

# ==============================
# دسترسی به المنت‌ها با ایندکس
# ==============================

# دسترسی به المنت خاص
print(temperature[1])

# تغییر المنت با ایندکس
temperature[2] = 5
print(temperature)

print("--------------------------")

# دسترسی و تغییر المنت
top_speads = [100, 120, 200, 240]
print(top_speads[3])
top_speads[3] = 250
print(top_speads)

print("--------------------------")
# ==============================
# اضافه کردن المنت به لیست
# ==============================
# بدون نیاز به سلف اساینمنت. ذخیره مستقیم تغییرات بر لیست
# اضافه کردن به انتهای لیست با append
users = ["jeremy", "adam", "Liza"]
users.append("sara")
print(users)

print("--------------------------")
# بدون نیاز به سلف اساینمنت. ذخیره مستقیم تغییرات بر لیست

# درج المنت در موقعیت خاص با insert
users.insert(2, "Erik")
print(users)

print("--------------------------")

# ترکیب insert و append
fruits = ["apple", "orange", "banana"]
fruits.insert(1, "coconut")
print(fruits)
fruits.append("watermelon")
print(fruits)

# تغییر المنت موجود
fruits[2] = "ananas"
print(fruits)

print("--------------------------")
# ✴️مقایسه بین اجزای بازه در تولید لیست و برش لیست✴️

# 🧩تولید لیست بر اساس بازه و گام 🧩

# List=[i for i in range(start,stop,step)]

# range 
# ،یک تابع است و در تمام توابع پایتون
# پارامتر ها با کاما از هم جدا می شوند
# ---------------------------------------------

# 🧩برش لیست بر اساس بازه و گام🧩
# List_slice=List[start:stop:step]

# این یکی، عملگر برش است و تابع نیست
# در این عملگر، سه بخش بازه با علامت : از هم جدا میشوند

# ==============================
# حذف المنت از لیست
# ==============================
# پاپ، نیازی به سلف اساینمنت ندارد و مستقیم بر لیست اصلی تاثیر می گذارد
# حذف آخرین المنت
fruits.pop()
print(fruits)

# حذف المنت با ایندکس خاص
fruits.pop(2)
print(fruits)

print("--------------------------")

# ذخیره المنت حذف شده
remove = fruits.pop(2)
print(remove)

print("--------------------------")

# ==============================
# کار با لیست‌های مختلف
# ==============================

# لیست از متغیرها
first = "John"
second = "Joseph"
third = "Donnie"
winners = [first, second, third]
print(winners[2])

print("--------------------------")
# تغییر المنت در لیست
flavors = ["vanilla", "chocolate", "pistachio"]
flavors[2] = "strawberry"
print(flavors)

print("--------------------------")

# لیست boolean و حذف المنت
quiz_answer = [False, False, True, False]
quiz_answer.pop()
print(quiz_answer)

print("--------------------------")

# ==============================
#   حلقه فور روی لیست‌ها برای پیمایش عناصر
# ==============================

# حلقه for ساده روی لیست
numbers_list = [1, 2, 3, 4, 6, 8, 10]
for i in numbers_list:
    print(i)

print("--------------------------")

# حلقه for روی لیست رشته‌ها
artists = ["chagall", "lissitzky"]
for artist in artists:
    print(artist)
    print("---------")

print("--------------------------")

# حلقه for با جداکننده
items = ["milk", "tomato", "apple"]
for item in items:
    print(item)
    print("-------")

print("--------------------------")

# حلقه فور با نام متغیر متفاوت
suplies = ["pencil", "book"]
for value in suplies:
    print(value)
print("--------------------------")

# عملیات ریاضی روی المنت‌های لیست در حلقه

# اجازه عملیات ریاضی روی کل لیست وجود ندارد
# پس باید روی لیست حلقه بزنیم 
# و روی متغیر کانترِ لوپ، عملیات ریاضی را اعمال کنیم
# البته باید یک لیست خالی قبل از لوپ بسازیم و این کانتر رو با اپند به آن بیفزاییم 

new_list=[]
data_points = [99, 99, 99, 99, 99]
for data in data_points:
    i+=1
    new_list.append(i)
print(new_list)    
# روش دوم: ساخت لیست با لیست کامپرهنشنِ لیست قبلی 
# مثلا:
data_points2=[i+1 for i in data_points]
# در این صورت، لیست جدید در واقع تغییر یافته لیست قبلی است
print("--------------------------")

# عملیات تفریق در حلقه
minutes_worked = [123, 100, 99, 67]
for minutes in minutes_worked:
    print(minutes - 60)
# البته این فقط برای نمایش است و روی لیست اصلی اعمال نمیشه
# مگر با ساخت لیست جدید و اپند مینوتز به آن
print("--------------------------")

# ==============================
# طول لیست و شرط‌ها
# ==============================

# محاسبه طول لیست
print(len(data_points))

print("--------------------------")

# شرط با طول لیست
if len(data_points) > 2:
    print("very good")

print("--------------------------")

# شرط عملی با طول لیست
ingredients = ["cafee", "lemon", "cream"]
if len(ingredients) > 2:
    print("bring a bag")

print("--------------------------")

# به‌روزرسانی مقادیر در حلقه
update_version = [1.2, 3.5, 2]
for version in update_version:
    print(version + 1)

print("--------------------------")

# شرط با لیست رشته‌ها
sodas = ["fanta", "cocacola", "pepsi"]
if len(sodas) >= 2:
    print("to much soda")

print("--------------------------")

# شرط برای لیست کوتاه
condidates = ["mishaeel"]
condidates_number = len(condidates)
if condidates_number < 2:
    print("one condidate needs opposition")

print("--------------------------")

# ==============================
# مثال‌های کاربردی
# ==============================
# سیستم منوی غذا
meals = ["omelet", "salad", "chicken"]
print(f"breakfast menu: {meals[0]}")
print(f"Lunch menu: {meals[1]}")
meals[2] = "pizza"
print(f"Dinner menu: {meals[2]}")

print("--------------buying list------------------")

# لیست خرید با حلقه
shopping_list = ["dish soap", "kleenex", "batteries", "aluminum foil", "pet food", "toothpaste", "lightbulbs"]

for shopping in shopping_list:
    print(f"Don't forget to buy {shopping}")

print("--------------------------")

# ==============================
# مثال‌های تکمیلی از فایل اصلی
# ==============================

# لیست با انواع مختلف داده
mixed_list = ["jalal", 21, 15.5, True]
print("Mixed list:", mixed_list)

print("--------------------------")

# اضافه کردن المنت‌های مختلف
transactions = [100, 5]
transactions.append(500)
print("Transactions:", transactions)

print("--------------------------")

# درج در موقعیت خاص
shopping = ["kiwis", "peas"]
shopping.insert(0, "lemon")
print("Shopping list:", shopping)

print("--------------------------")

# ترکیب append و insert
initials = ["RM", "LP"]
initials.append("LC")
initials.insert(1, "LS")
print("Initials:", initials)

print("--------------------------")

# حذف المنت خاص
todo_list = ["call mom", "dishes", "painting"]
todo_list.pop(1)
print("Todo after pop:", todo_list)

print("--------------------------")

# حلقه for روی لیست نمرات
final_scores = [17, 22, 34, 13]
print("Final scores:")
for score in final_scores:
    print(score)

print("--------------------------")

# حلقه for روی لیست کنسول‌ها
consoles = ["Playstation", "Xbox"]
print("Consoles:")
for console in consoles:
    print(console)

print("--------------------------")

# حلقه for روی لیست ورزش‌ها
sports = ["Basketball", "Soccer"]
print("Sports:")
for sport in sports:
    print(sport)

print("--------------------------")

# شرط با طول لیست
tasks = ["dishes", "windows", "vacuum"]
if len(tasks) > 0:
    print("Ugh, more work!")

print("--------------------------")

# لیست خالی و طول
empty_users = []
number_of_users = len(empty_users)
print("Number of users in empty list:", number_of_users)

print("--------------------------")

# سیستم بررسی موجودی
sodas_check = ["coke", "fanta"]
if len(sodas_check) > 3:
    print("Too much soda")
else:
    print("Reasonable amount of soda")

print("End of lists training file")