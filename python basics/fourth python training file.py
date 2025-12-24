# ============================================
# Assignment Operators - عملگرهای انتساب
# ============================================
# 🔥 ضروری → تغییر مقدار متغیرها و محاسبات در اتوماسیون
wallet = 5
wallet += 1
wallet -= 3
print(wallet)

nam = "accont_name:"
nam += "john"
nam += " wick"
print(nam)

likes = 6
likes += 1
likes -= 4
print(likes)

speed = 200
speed += 20
print(f"speed : {speed} km/h")

title = "Dr."
title += " Jane Doe"
print(title)

# ⚠️ تمرینی / تکراری
owed = 0
owed -= 40
print(owed)
name = "hemn"
name += " mala fatih"
print(name)

# ============================================
# While Loops - حلقه‌های while پایه
# ============================================
# 🔥 ضروری → تکرار وظایف و بررسی شرایط در اتوماسیون
test = True
while test:
    print("to infinity")
    print("let's go")
    test = False

sales = 0
inventory = 10
while sales <= 10 and inventory >= 0:
    print(f'Sales: {sales}')
    print(f'Inventory: {inventory}')
    print("~~")
    sales += 1
    inventory -= 1

# ⚠️ تمرینی / غیرضروری
keep_playing = True
while keep_playing:
    print("Now Playing: Dolce Vita")
    keep_playing = False

auto_pilot = True
while auto_pilot:
    print("auto_pilot on : wroom")
    auto_pilot = False

is_on = True
while is_on:
    print("now playing: Yummy")
    is_on = False

# ============================================
# While Loops with Counter - شمارنده
# ============================================
# 🔥 ضروری → شمارش تکرارها در اتوماسیون
counter = 1
while counter < 10:
    print(counter)
    counter += 2

speed = 2
while speed < 10:
    print(speed)
    speed += 1

# ⚠️ تمرینی / غیرضروری
speed = 2
while speed < 10:
    speed += 1
    print(speed)

list_number = 1
while list_number < 11:
    print("Add entry..")
    print(list_number)
    list_number += 1

counter = 3
while counter > 0:
    print(counter)
    counter -= 1

lives = 4
while lives > -1:
    print(f"your lives is {lives}")
    lives -= 1
print("game over")

level = 1
while level < 5:
    print(f"your level is {level}")
    level += 1

counter = -1
while counter >= -5:
    print(counter)
    counter -= 1

i = 0
while i <= 3:
    print(i)
    i += 1

reminder_count = 0
while reminder_count < 3:
    print("Reminder: Stop the bot!")
    reminder_count += 1

# ============================================
# For Loops - حلقه‌های for
# ============================================
# 🔥 ضروری → تکرار مجموعه‌ای از دستورات در اتوماسیون
for i in range(5):
    print("✓✓✓✓✓✓✓✓✓✓✓✓✓")

for i in range(6):
    print(i)

for i in range(5):
    print(i)
    print("for loops is great")

# ⚠️ تمرینی / غیرضروری
for x in range(5):
    print("level:")
    print(x)

for sales in range(5):
    print(f"sales :{sales}")
for sales in range(5):
    sales += 1
    print(f"sales :{sales}")

# ============================================
# Nested Loops & Patterns - حلقه‌های تو در تو و الگوها
# ============================================
# 🔥 ضروری → تولید الگوها و گزارشات اتوماتیک
line = ""
for i in range(4):
    line += "~"
    print(line)

code = "XXXX " * 4
print("antivirus license : ")
print(code)

# ⚠️ تمرینی / غیرضروری
line_2 = "~~~"
for i in range(4):
    print(line_2)

# ============================================
# Numbering Systems - سیستم‌های شماره‌بندی
# ============================================
# 🔥 ضروری → ایجاد لیست‌ها و شماره‌گذاری خودکار
for i in range(6):
    i += 1
    print(f"age_{i} = ")

x = 1
while x < 20:
    print(f"age_{x} = ")
    x += 1

for i in range(20):
    i += 1
    print(f"{i})")
    print("_____")

# ============================================
# End of Loops Training File
# ============================================
print("End of loops training file")