
# Lists - لیست‌ها
# ============================================
print("Lesson: lists")
line = "--------------------------------"

# 🔥 ضروری → مدیریت مجموعه داده‌ها در اتوماسیون
todo = ["read", "workout", "code"]
print(todo)

active_users = ["fine"]
print("active:", active_users)

characters = ["mario", "luigi", "bowser", "peach"]
print(characters)

temperature = [20, 16, 12, 30, 19]
print(temperature)

# دسترسی و تغییر المنت با ایندکس
temperature[2] = 5
print(temperature)

top_speads = [100, 120, 200, 240]
top_speads[3] = 250
print(top_speads)

# اضافه کردن المنت‌ها
users = ["jeremy", "adam", "Liza"]
users.append("sara")
users.insert(2, "Erik")
print(users)

fruits = ["apple", "orange", "banana"]
fruits.insert(1, "coconut")
fruits.append("watermelon")
fruits[2] = "ananas"
print(fruits)

# حذف المنت‌ها
fruits.pop()
fruits.pop(2)
remove = fruits.pop(2)
print(remove)

# 🔥 ضروری → ترکیب لیست‌ها و متغیرها
first = "John"
second = "Joseph"
third = "Donnie"
winners = [first, second, third]
print(winners[2])

flavors = ["vanilla", "chocolate", "pistachio"]
flavors[2] = "strawberry"
print(flavors)

quiz_answer = [False, False, True, False]
quiz_answer.pop()
print(quiz_answer)

# ============================================
# For Loops روی لیست‌ها
# ============================================
# 🔥 ضروری → پردازش و اجرای خودکار روی مجموعه داده‌ها
numbers_list = [1, 2, 3, 4, 6, 8, 10]
for i in numbers_list:
    print(i)

artists = ["chagall", "lissitzky"]
for artist in artists:
    print(artist)

shopping_list = ["dish soap", "kleenex", "batteries", "aluminum foil", "pet food", "toothpaste", "lightbulbs"]
for shopping in shopping_list:
    print(f"Don't forget to buy {shopping}")

# عملیات ریاضی روی المنت‌ها
data_points = [99, 99, 99, 99, 99]
for data in data_points:
    print(data + 1)

minutes_worked = [123, 100, 99, 67]
for minutes in minutes_worked:
    print(minutes - 60)

# 🔥 ضروری → بررسی طول لیست و شرط‌ها
print(len(data_points))
if len(data_points) > 2:
    print("very good")

ingredients = ["cafee", "lemon", "cream"]
if len(ingredients) > 2:
    print("bring a bag")

update_version = [1.2, 3.5, 2]
for version in update_version:
    print(version + 1)

sodas = ["fanta", "cocacola", "pepsi"]
if len(sodas) >= 2:
    print("to much soda")

condidates = ["mishaeel"]
if len(condidates) < 2:
    print("one condidate needs opposition")

# ============================================
# مثال‌های کاربردی سیستم‌ها
# ============================================
# 🔥 ضروری → کاربرد واقعی در اتوماسیون
meals = ["omelet", "salad", "chicken"]
print(f"breakfast menu: {meals[0]}")
print(f"Lunch menu: {meals[1]}")
meals[2] = "pizza"
print(f"Dinner menu: {meals[2]}")

# سیستم بررسی موجودی
sodas_check = ["coke", "fanta"]
if len(sodas_check) > 3:
    print("Too much soda")
else:
    print("Reasonable amount of soda")

# سیستم لیست خرید
shopping = ["kiwis", "peas"]
shopping.insert(0, "lemon")
print("Shopping list:", shopping)

initials = ["RM", "LP"]
initials.append("LC")
initials.insert(1, "LS")
print("Initials:", initials)

todo_list = ["call mom", "dishes", "painting"]
todo_list.pop(1)
print("Todo after pop:", todo_list)

final_scores = [17, 22, 34, 13]
for score in final_scores:
    print(score)

consoles = ["Playstation", "Xbox"]
for console in consoles:
    print(console)

sports = ["Basketball", "Soccer"]
for sport in sports:
    print(sport)

tasks = ["dishes", "windows", "vacuum"]
if len(tasks) > 0:
    print("Ugh, more work!")

empty_users = []
print("Number of users in empty list:", len(empty_users))

# ============================================
# ⚠️ تمرینی / غیرضروری
# لیست خالی، لیست با یک المنت، چاپ خطوط جداکننده، حلقه‌های for با جداکننده ساده، لیست مخلوط و اضافه کردن تکراری المنت‌ها
todo = []
print(todo)
print(line)

active_users = ["fine"]
print("active:")
print(active_users)

print(line)

# حلقه for ساده روی لیست رشته‌ها با پیام اضافی
items = ["milk", "tomato", "apple"]
for item in items:
    print(item)
    print("-------")

suplies = ["pencil", "book"]
for value in suplies:
    print(value)

# مثال لیست مختلط
mixed_list = ["jalal", 21, 15.5, True]
print("Mixed list:", mixed_list)

transactions = [100, 5]
transactions.append(500)
print("Transactions:", transactions)

print("End of lists training file")