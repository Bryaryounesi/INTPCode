# فایل پانزدهم آموزش پایتون - توابع input و کنترل لوپ
# ==============================================

print("lesson name : input function and loop control")

# ==============================
# تابع input() - دریافت ورودی از کاربر
# ==============================

# دریافت ساده نام
print("What's your name?")
name_input = input()
print(f"Hi, {name_input}!")

print("-------------------------")

# استفاده از prompt درون تابع input
user_input = input("Enter your name: ")
print(f"Thanks, {user_input}!")

print("-------------------------")

# دریافت چند ورودی مختلف
user_input_1 = input("Enter a number: ")
user_input_2 = input("Enter another number: ")
print("First input:", user_input_1)
print("Second input:", user_input_2)
print("Type of inputs:", type(user_input_1), type(user_input_2))

print("-------------------------")

# تبدیل رشته به عدد
number = input("Input your number: ")
print("As string (repeated 3 times):", number * 3)
print("As float:", float(number))
print("As integer:", int(number))

print("-------------------------")

# استفاده از input در شرط
age_string = input("Enter your age: ")
if int(age_string) < 21:
    print("Under 21")
else:
    print("21 or older")

print("-------------------------")

# دریافت شغل
job = input("Enter your job title: ")
print("Job title:", job)

print("-------------------------")

# ==============================
# پروژه چت بات با input
# ==============================

print("=== Chat Bot Project ===")
name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}!")

age_input = input("How old are you? ")
age = int(age_input)
bot_age = 3
age_difference = age - bot_age
print(f"You are {age_difference} years older than me. I'm only {bot_age} years old!")

color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")

print("-------------------------")

# ==============================
# تابع range با پارامترهای مختلف
# ==============================

# range با یک پارامتر (end)
print("Range with end only (0 to 4):")
for i in range(5):
    print(i)

print("-------------------------")

# range با دو پارامتر (start, end)
print("Range with start and end (2 to 4):")
for i in range(2, 5):
    print(i)

print("-------------------------")

# range با سه پارامتر (start, end, step)
print("Range with step (2 to 8 with step 2):")
for i in range(2, 10, 2):
    print(i)

print("-------------------------")

# ==============================
# دستور continue در لوپ‌ها
# ==============================

# continue قبل از print - هیچ خروجی ندارد
print("Continue before print - no output:")
for i in range(1, 6):
    continue
    print(i)  # این خط هیچگاه اجرا نمی‌شود

print("-------------------------")

# continue با شرط - حذف عدد 2
print("Continue with condition - skip number 2:")
for i in range(1, 6):
    if i == 2:
        continue
    print(i)

print("-------------------------")

# حذف آیتم از لیست خرید
shopping_list = ["apples", "bananas", "bread", "milk", "chips", "eggs"]
print("Shopping list without chips:")
for item in shopping_list:
    if item == "chips":
        continue
    print(f"Don't forget to buy {item}")

print("-------------------------")

# حذف بازه عددی در for
print("Skip numbers 4 to 6 in for loop:")
for j in range(1, 8):
    if j >= 4 and j <= 6:
        continue
    print(j)

print("-------------------------")

# حذف بازه عددی در while
print("Skip numbers 2 to 5 in while loop:")
i = 0
while i < 10:
    i += 1
    if i >= 2 and i <= 5:
        continue
    print(i)

print("-------------------------")

# جایگزینی با پیام خاص
print("Replace number 8 with 'fart':")
for j in range(0, 10):
    if j == 8:
        print("fart")
        continue
    print(j)

print("-------------------------")

# ==============================
# دستور break در لوپ‌ها
# ==============================

# break در for loop
print("Break loop when i >= 5:")
for i in range(1, 10):
    if i >= 5:
        break
    print(i)

print("-------------------------")

# سیستم ورود رمز با while و break
print("=== Password System ===")
password = "4040"
while True:
    user_password = input("Enter the password: ")
    if user_password == password:
        print("Access granted!")
        break
    print("Incorrect password. Try again.")

print("-------------------------")

# سیستم ورود با else برای if
print("=== Password System with else ===")
password = "2020"
while True:
    user_input = input("Please enter your pass: ")
    if user_input == password:
        print("Welcome!")
        break
    else:
        print("Wrong, try again")

print("-------------------------")

# ==============================
# else در لوپ‌ها
# ==============================

# else در for loop (اجرا می‌شود)
print("For loop with else (executes):")
for i in range(1, 6):
    print(i)
else:
    print('Loop has ended normally')

print("-------------------------")

# else در for loop (اجرا نمی‌شود به دلیل break)
print("For loop with else (doesn't execute due to break):")
for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print("This won't print due to break")

print("-------------------------")

# else در while loop (اجرا نمی‌شود)
print("While loop with else (doesn't execute):")
i = 0
while i < 10:
    i += 1
    if i > 4 and i < 9:
        break
    print(i)
else:
    print("loop has ended - this won't print")

print("-------------------------")

# نمایش لیست سریال‌ها با else
shows = ["The Office", "Dexter", "Friends"]
print("My favorite shows:")
for show in shows:
    print(show)
else:
    print("Those are my favorite shows!")

print("-------------------------")

# ==============================
# مثال‌های کاربردی ترکیبی
# ==============================

# پردازش لیست وظایف با while و continue
print("=== Task Processor ===")
tasks = ["pending", "completed", "pending", "pending"]
index = 0

print("Processing with continue:")
while index < len(tasks):
    if tasks[index] == "completed":
        print(f"Skipping task {index + 1}")
        index += 1
        continue
    print(f"Processing task {index + 1}")
    index += 1

print("-------------------------")

# روش جایگزین بدون continue
print("Alternative method without continue:")
tasks = ["pending", "completed", "pending", "pending"]
index = 0
while index < len(tasks):
    if tasks[index] == "pending":
        print(f"Processing task {index + 1}")
    else:
        print(f"Skipping task {index + 1}")
    index += 1

print("-------------------------")

# جستجوی وظیفه فوری با break
print("=== Urgent Task Finder ===")
tasks = ["email boss", "fix bug", "attend meeting"]

for task in tasks:
    if task == "fix bug":
        print("Urgent task found: fix bug")
        break
    print(f"Working on: {task}")

print("-------------------------")

# ==============================
# سیستم مدیریت وظایف پیشرفته
# ==============================

print("=== Advanced Task Manager ===")
tasks = []
print("Enter your tasks (type 'done' to finish):")

while True:
    task = input("Enter a task: ")
    if task.lower() == 'done':
        break
    tasks.append(task)

print("\nYour tasks:")
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
else:
    print("All tasks listed successfully!")

print("-------------------------")

# سیستم جمع‌آوری نمرات
print("=== Grade Collector ===")
grades = []
print("Enter student grades (type 'stop' to finish):")

while True:
    grade_input = input("Enter grade: ")
    if grade_input.lower() == 'stop':
        break
    
    try:
        grade = float(grade_input)
        if grade < 0 or grade > 20:
            print("Grade must be between 0 and 20")
            continue
        grades.append(grade)
    except ValueError:
        print("Please enter a valid number")
        continue

if grades:
    average = sum(grades) / len(grades)
    print(f"\nAverage grade: {average:.2f}")
    print(f"Highest grade: {max(grades)}")
    print(f"Lowest grade: {min(grades)}")
else:
    print("No grades entered")

print("End of input and loop control training")