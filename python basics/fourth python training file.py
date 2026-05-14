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
# ---------------------------------
# خود انتصابی با عملگر ها 
p = print
wallet = 5
wallet +=5
wallet -= 6
wallet *=5
wallet /=3
p(wallet)
# به کمک خود انتصابی تمام عملیات های ریاضی، 
# روی متغیرهای عددی، قابل اعمال  هستند
# ------------------------------------
str = "hsw"
str += "562"
str *= 3
p(str)
#با خود انتصابی، تنها ضرب و جمع ، قابل اعمال روی رشته ها هستند
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
likes = 6
likes += 1
# معادل likes = likes +1
print(likes)
likes -= 4
# معادل likes = likes -4
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
# ----------------------------------------------------
# خود انتصابی به کمک تابع مشروط
number = 5
p = print
def adding(new,alamat):
    global number
    if alamat == "+":
        number += new
    elif alamat == "-":
        number -= new
    elif alamat == "*":
        number *= new  
    elif alamat == "/":
        number /= new           
    p(number)
adding(5 , "-")
adding(50 , "+")
adding(60 , "*") 
adding(9 , "/") 
# ==============================
# حلقه while پایه
# حلقه وایل
# لوپ وایل
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
# شمارنده یعنی همان کانتر
# کانتر، باید به عدد مورد مقایسه در شرط لوپ برسد تا لوپ متوقف شود
# پس اگر کانتر بزرگتر است باید شمارنده کانتر نزولی و اگر کوچکتر، باید صعودی باشد
# شرط لوپ وایل باید ترو باشد پس اگر کانتر کوچکتر است در شرط لوپ، علامت کوچکتر بگذارید و برعکس
# حلقه افزایشی با قدم 2
counter = 1  #کانتر لوپ
while counter < 10:  # لوپ و شرط آن
    print(counter)   # پیام لوپ
    counter += 2     # پیام لوپ
    # counter = counter + 2 معادل سطر بالایی 
# کانتر از 10 کوچکتر پس باید شمارنده آن صعودی باشد

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
# اگر بخواهیم بعد از پایان لوپ وایل چیزی بنویسیم،
# باید آن پیام خارج از تورفتگی لوپ نوشته شود
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
# حلقه با بیش از یک کانتر
print("--------join them (important example) ------------")
sales = 0
inventory = 10
while sales <= 10 and inventory >= 0:
    print(f'Sales: {sales}')
    print(f'Inventory: {inventory}')
    print("~~")
    sales += 1
    inventory -= 1
# حلقه با شرط مرکب یعنی حلقه ای که شرط آن 
# از ترکیب چند شرط ساده با 
# and یا or 
# ساخته شده و نه الزاما بیش از یک کانتر 
# ----------------------------------------------------

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
#  تمام مثال های بالا تنها برای تکرار پیام لوپ،
# پرینت نسخه شماره دار شده آن و پرینت رنج درون شرط لوپ بودن
# ==============================
# حلقه for پایه
# ==============================
print("-------for loop-------------")
# حلقه فور
# لوپ فور

# حلقه for ساده
for i in range(5):
    print("***************")
    
#  متغیر لوپ فور
# کانتر لوپ فور
# for loop variable
# for loop counter      #کانتر حلقه فور
'''
اگر با لوپ فور روی یک بازه عددی(رنج) پیمایش کنیم
متغیر لوپ (i)
کانتر یا شمارنده هم هست 
ولی برای پیمایش اعضای یک موجموعه غیر عددی، کانتر نیست و متغیر موقت لوپ است. 
'''
# بهتراست جاهایی که متغیر لوپ، کانتر نیست از 
# چیز دیگری به جای i 
# استفاده شود
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
# --------------------------------------------------    
# شرط توقف لوپ while
# --------------------------------------------------    

p = print
i = 10
while i >0:
    p(i)
    i -= 1
    if i == 5:
        break
# --------------------------------------------------    
# شرط توقف لوپ for
# --------------------------------------------------    
 
for j in range(15):
    p("time: ", j)
    if j == 6:
        break
# ----------------------------------------------
# حلقه وایل, با شرط مرکب دو کانتری و شرط توقف ترکیبی
a = -10
j = 50
p = print

while a > -40 and j > 0:
    p("i love you pmc", a , j )
    a -= 1
    j -=1
    if (a + j) == 12:
        p("bingo")
        break
# ==============================
# حلقه‌های تو در تو و الگوها
# ==============================

print("*")
line = ""
for i in range(4):
    line += "~"
    print(line)
# نمونه از اعمال یک تغییر ثابت به دفعات لوپ بر یک متغیر بیرونی
print("--------------------")

line_2 = "~~~"
for i in range(4):
    print(line_2)

print("--------------------")

# تولید کد با ضرب رشته
code = "XXXX " * 4
print("antivirus license : ")
print(code)
# این مثال هیچ ربطی به لوپ ندارد
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

print("3 mesal az sakhtare shomarebandi ba loop")

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
# تغییر متغیر خارجی با لوپ فور (مهم)

x = 3
for i in range(5):
    print(x)
# فقط متغیر رو 5 بار تکرار میکند
print("--------------------")

x = 3
for i in range(5):
    print(x)
    x += 2  # اضافه کردن یک افزاینده به لوپ فور
# پنج بار عدد 2 به متغیر خارجی اضافه میشود با حفظ مقادیر افزوده شده قبلی
# سایر شمارنده های قابل استفاده : -= ، *=، **=
print("-------------------------------------------")
''' سایر انواعِ متغیر های خارجی که میتوان با لوپ فور، خود(یا عناصر آنها) را تغییر داد '''
# تغییر داتافریم با لوپ  #تغییر ستون با لوپ  #تغییر سری با لوپ
print("-------------------------------------------")

'''x1= df["col1"]   # (با لیست کامپرهنشن بهتر از لوپ)یک ستون داتافریم
مثال :
for i in range(5): #میتوان از رنج استفاده کرد یا از خود متغیر
for i in x1:    
    x1 -= 20
p(df)     '''
print("----------")  
''' x2 = df          # (با لیست کامپرهنشن بهتر از لوپ)یک داتافریم
مثال :
for i in x2:    
    x2 += 40
p(df)  '''  
print("-------------") 
 
'''x3 = np.array([i for i in range(-6,30,4)])  
# (با عملیات برداری بهتر از لوپ)یک لیست آرایه شده

for i in range(5):
    x3 *= 20 '''
# خود لیست ها را مستقیما نمیتوان با لوپ تغییر داد
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
    
# ------------------------------------------------
# ساخت کانتر برای لوپ فور با تابع داخلی 
# enumerate
# ---------------------------------------------
p = print
days = ["satureday","sunday","monday","tuesday"]
for index,i in enumerate(days):     
    p(f"{index}: Today is {i} ")       # i 
# ایندکس (که میتواند هر اسمی داشته باشد) کانتر تابع 
# حرف ئای (که بهتر است نام دیگری داشته باشد) کانتر نیست 
# چون مجموعه عددی نداریم
# و این حرف،  متغیر لوپ است
# --------------------------------------------
# حلقه فور با بیش از یک متغیر لوپ
# --------------------------------------------
# لوپ چند متغیری#   چند متغیر در لوپ فور
# for loop with multi variable

'''
کاربرد لوپ های چند متغری
برای پیمایش مجموعه های چند جزئی و قابل آنپک شدن در پایتون 
مثلا تاپل ها، دیکشنری ها، لیست های تودرتو، مجموعه های زیپ شده به هم  هنگام استفاده از تابع enumerate '''
# ------------------------------------------------
print("End of loops training file")