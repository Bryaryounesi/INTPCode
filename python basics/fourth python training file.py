# فایل چهارم آموزش پایتون - حلقه‌ها (Loops)
# ==============================

print("lesson: loops")
# ========================
# عملگرهای انتساب (Assignment Operators)
# ==============================

# خود انتسابی (Self Assignment) با اعداد
wallet = 5
wallet = wallet
wallet = wallet + 1
wallet = wallet - 3
print(wallet)

print("--------------------")

# خود انتسابی با رشته‌ها
nam = "accont_name:"
nam = nam + "john"
nam = nam + " wick"
print(nam)

print("--------------------")

name = "hemn"
name = name + " mala fatih"
print(name)

print("--------------------")

# عملگرهای += و -=
likes = 6
likes += 1
print(likes)
likes -= 4
print(likes)

print("--------------------")

speed = 200
speed += 20
print(f"speed : {speed} km/h")

print("--------------------")

# عملگر += با رشته
title = "Dr."
title += " Jane Doe"
print(title)

print("--------------------")

# عملگر -= با اعداد منفی
owed = 0
owed -= 40
print(owed)

print("--------------------")

# ==============================
# حلقه while پایه
# ==============================

print("* important loops ***")

# حلقه while با شرط ساده
test = True
while test:
    print("to infinity")
    print("let's go")
    test = False

print("--------------------")

keep_playing = True
while keep_playing == True:
    print("Now Playing: Dolce Vita")
    keep_playing = False

print("--------------------")

auto_pilot = True
while auto_pilot == True:
    print("auto_pilot on : wroom")
    auto_pilot = False

print("--------------------")

is_on = True
while is_on == True:
    print("now playing: Yummy")
    is_on = False

print("--------------------")

# ==============================
# حلقه while با شمارنده
# ==============================

# حلقه افزایشی با قدم 2
counter = 1
while counter < 10:
    print(counter)
    counter += 2

print("----------×××××----------")

# حلقه افزایشی معمولی
speed = 2
while speed < 10:
    print(speed)
    speed += 1

print("--------------------")

# حلقه با افزایش قبل از پرینت
speed = 2
while speed < 10:
    speed += 1
    print(speed)

print("--------------------")

# حلقه با پیام و شمارنده
list_number = 1
while list_number < 11:
    print("Add entry..")
    print(list_number)
    list_number += 1

print("--------------------")

# حلقه کاهشی
counter = 3
while counter > 0:
    print(counter)
    counter -= 1

print("--------------------")

# حلقه کاهشی با پیام
lives = 4
while lives > -1:
    print(f"your lives is {lives}")
    lives -= 1
print("game over")

print("--------------------")

# حلقه افزایشی با پیام
level = 1
while level < 5:
    print(f"your level is {level}")
    level += 1

print("--------------------")

# حلقه با شمارنده منفی
print("--------negative counter------------")
counter = -1
while counter >= -5:
    print(counter)
    counter -= 1

print("--------------------")

# حلقه ساده با شرط عددی
i = 0
while i <= 3:
    print(i)
    i += 1

print("--------------------")

# حلقه while با شرط مرکب
print("--------join them (important example) ------------")
sales = 0
inventory = 10
while sales <= 10 and inventory >= 0:
    print(f'Sales: {sales}')
    print(f'Inventory: {inventory}')
    print("~~")
    sales += 1
    inventory -= 1

print("--------------------")

# حلقه یادآوری
reminder_count = 0
while reminder_count < 3:
    print("Reminder: Stop the bot!")
    reminder_count += 1

print("--------------------")

# ==============================
# پرچم آمریکا با حلقه while
# ==============================

print("America flag")
first_counter = 0
while first_counter < 5:
    print("**----------")
    first_counter += 1

second_counter = 0
while second_counter < 5:
    print("--------------------")
    second_counter += 1

print("--------------------")

# ==============================
# حلقه for پایه
# ==============================

print("-------for loop-------------")

# حلقه for ساده
for i in range(5):
    print("✓✓✓✓✓✓✓✓✓✓✓✓✓")

print("--------------------")

# حلقه for با نمایش شمارنده
for i in range(6):
    print(i)

print("--------------------")

# حلقه for با پیام و شمارنده
for i in range(5):
    print(i)
    print("for loops is great")

print("--------------------")

# حلقه for با عنوان و شمارنده
for x in range(5):
    print("level:")
    print(x)

print("--------------------")

# حلقه for با افزایش قبل از پرینت
print("-------for loop +- adding before print -------------")
for sales in range(5):
    print(f"sales :{sales}")

print("--------------------")

for sales in range(5):
    sales += 1
    print(f"sales :{sales}")

print("--------------------")

# نمایش اعداد 0 تا 4
print("zero to four:")
for repetation in range(5):
    print(repetation)

print("--------------------")

# ==============================
# حلقه‌های تو در تو و الگوها
# ==============================

print("*")
line = ""
for i in range(4):
    line += "~"
    print(line)

print("--------------------")

line_2 = "~~~"
for i in range(4):
    print(line_2)

print("--------------------")

# تولید کد با ضرب رشته
code = "XXXX " * 4
print("antivirus license : ")
print(code)

print("--------------------")

# ==============================
# حلقه‌های while جداگانه
# ==============================

print("-------2 while loops-------------")
sales = 0
inventory = 10

while sales <= 10:
    print(f"sales :{sales}")
    sales += 1

while inventory >= 0:
    print(f"inventory :{inventory}")
    inventory -= 1

print("--------------------")

# ==============================
# مثال‌های تمرینی از فایل اصلی
# ==============================

# حلقه while برای به‌روزرسانی حقوق
counter = 3
while counter < 11:
    print("Updating payroll")
    counter += 1

print("--------------------")

# حلقه while برای نمایش سال‌ها
year = 2020
while year <= 2025:
    print(f"its {year}")
    year += 1

print("--------------------")

# حلقه while با افزایش قبل از پرینت
trail = 1
while trail <= 3:
    trail += 1
print(trail)

print("--------------------")

trail = 1
while trail < 3:
    trail += 1
print(trail)

print("--------------------")

# حلقه while برای اعداد زوج
evens = 0
while evens < 10:
    evens += 2
    print(evens)

print("--------------------")

# حلقه while برای نمایش روزها
days = 0
while days < 7:
    days += 1
    print(days)

print("--------------------")

# ==============================
# سیستم‌های شماره‌بندی مختلف
# ==============================

print("سه مثال از ساخت شماره بندی با لوپ")

# با حلقه for
for i in range(6):
    i += 1
    print(f"age_{i} = ")

print("-------------")

# با حلقه while
x = 1
while x < 20:
    print(f"age_{x} = ")
    x += 1

print("-------------")

# با حلقه for و فرمت مختلف
for i in range(20):
    i += 1
    print(f"{i})")
    print("_____")

print("--------------------")

# ==============================
# حلقه for با range
# ==============================

# حلقه for برای پرچم (جایگزین while)
for i in range(5):
    print("**---------")

for i in range(4):
    print("-------------------")

print("--------------------")

# حلقه for برای تولد
for i in range(5):
    print("Happy birthday to you!")

print("--------------------")

# حلقه for ساده
for i in range(3):
    print("be like me")

print("--------------------")

# حلقه for با افزایش متغیر خارجی
x = 3
for i in range(5):
    print(x)

print("--------------------")

x = 3
for i in range(5):
    print(x)
    x += 2

print("--------------------")

x = 3
for i in range(5):
    x += 2
    print(x)

print("--------------------")

# حلقه for با رشته
x = "23"
for i in range(5):
    x += "~~"
    print(x)

print("--------------------")
x = "23"
for i in range(5):
    print(x)
    x += "~~"

print("End of loops training file")