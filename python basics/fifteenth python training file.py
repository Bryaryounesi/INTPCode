# فایل پانزدهم آموزش پایتون - توابع input و کنترل لوپ
# ====================================================
print("lesson name : input function and loop control")

# 🔥 ضروری برای دریافت داده از کاربر
# ==============================
# تابع input() - دریافت ورودی از کاربر
# ==============================
print("=== Basic input examples ===")

# دریافت ساده نام
name_input = input("What's your name? ")
print(f"Hi, {name_input}!")

# چند ورودی
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
print("First input:", num1, "Second input:", num2)
print("Types:", type(num1), type(num2))

# تبدیل رشته به عدد
number = input("Input your number: ")
print("As string:", number * 3)
print("As float:", float(number))
print("As integer:", int(number))

# استفاده از input در شرط
age = int(input("Enter your age: "))
if age < 21:
    print("Under 21")
else:
    print("21 or older")

# دریافت شغل
job = input("Enter your job title: ")
print("Job title:", job)

print("-------------------------")

# ✅ تمرینی: پروژه چت بات با input
print("=== Chat Bot Project ===")
name = input("Hello! What is your name? ")
age = int(input("How old are you? "))
bot_age = 3
print(f"You are {age - bot_age} years older than me. I'm only {bot_age} years old!")
color = input("What's your favorite color? ")
print(f"Oh, {color} is a beautiful color!")

print("-------------------------")

# 🔥 ضروری برای مدیریت حلقه‌ها
# ==============================
# تابع range با پارامترهای مختلف
print("=== Range examples ===")
for i in range(5):  # end only
    print(i)

for i in range(2, 5):  # start, end
    print(i)

for i in range(2, 10, 2):  # start, end, step
    print(i)

print("-------------------------")

# 🔥 ضروری: دستور continue
print("=== Continue examples ===")
for i in range(1, 6):
    if i == 2:
        continue
    print(i)

shopping_list = ["apples", "bananas", "bread", "milk", "chips", "eggs"]
for item in shopping_list:
    if item == "chips":
        continue
    print(f"Don't forget to buy {item}")

# continue در while
i = 0
while i < 10:
    i += 1
    if i >= 2 and i <= 5:
        continue
    print(i)

# جایگزینی با پیام خاص
for j in range(0, 10):
    if j == 8:
        print("fart")
        continue
    print(j)

print("-------------------------")

# 🔥 ضروری: دستور break
print("=== Break examples ===")
for i in range(1, 10):
    if i >= 5:
        break
    print(i)

# سیستم ورود رمز
password = "4040"
while True:
    user_password = input("Enter the password: ")
    if user_password == password:
        print("Access granted!")
        break
    print("Incorrect password. Try again.")

print("-------------------------")

# ✅ تمرینی: else در لوپ‌ها
print("=== Loop else examples ===")
for i in range(1, 6):
    print(i)
else:
    print("Loop has ended normally")

for i in range(1, 11):
    if i == 5:
        break
    print(i)
else:
    print("This won't print due to break")

print("-------------------------")

# ✅ تمرینی: مثال‌های ترکیبی continue + while
print("=== Task Processor ===")
tasks = ["pending", "completed", "pending", "pending"]
index = 0
while index < len(tasks):
    if tasks[index] == "completed":
        print(f"Skipping task {index + 1}")
        index += 1
        continue
    print(f"Processing task {index + 1}")
    index += 1

# جایگزین بدون continue
tasks = ["pending", "completed", "pending", "pending"]
index = 0
while index < len(tasks):
    if tasks[index] == "pending":
        print(f"Processing task {index + 1}")
    else:
        print(f"Skipping task {index + 1}")
    index += 1

# ✅ تمرینی: جستجوی وظیفه فوری با break
tasks = ["email boss", "fix bug", "attend meeting"]
for task in tasks:
    if task == "fix bug":
        print("Urgent task found: fix bug")
        break
    print(f"Working on: {task}")

print("-------------------------")

# 🔥 ضروری: سیستم مدیریت وظایف پیشرفته با while + break
print("=== Advanced Task Manager ===")
tasks = []
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

# ✅ تمرینی: سیستم جمع‌آوری نمرات
print("=== Grade Collector ===")
grades = []
while True:
    grade_input = input("Enter grade (stop to finish): ")
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
    print(f"\nAverage grade: {sum(grades)/len(grades):.2f}")
    print(f"Highest grade: {max(grades)}")
    print(f"Lowest grade: {min(grades)}")
else:
    print("No grades entered")

print("End of input and loop control training")