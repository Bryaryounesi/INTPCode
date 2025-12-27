# مثال‌های متغیرها (Variables)
# ==============================

# ذخیره مقدار رشته در متغیر
Car_1 = "porsche"
City = "miami"

# متغیرهای شخصی شما
greating = "hello world"
first_name = "Elizabeth"
last_name = "tailor"
name = "Elizabeth tailor"
city = "las vegas"
person_name = "Elizabeth tailor"
city_name = "Washington DC"
sport = "B-ball"
frequency = "daily"
job = "sherif"

# ==============================
# مثال‌های دستور print()
# ==============================

# چاپ مستقیم رشته
print("3 , 2 , 1")
print("go")
print("hello world")
print("have a delicious time")
print("bye")

# چاپ مقدار یک متغیر
greeting = "hello world"
name = "daenerys"
print(name)
print(greating)
print(person_name)
print(city_name)
print(sport)
print(frequency)

# ==============================
# چاپ با فرمت concatenation
# ==============================

print("job:" + job)
print("sport:" + sport)
print("name:" + person_name)
print("city:" + city_name)
print("singer:" + person_name)
print("job:" + "artist")

label = "name:" + "joe"
print(label)

likes = "20"
print("likes:" + likes)

# ==============================
# مثال‌های آپدیت متغیرها
# ==============================

# تغییر مقدار متغیر
status = "whatching HBO"
status = "relaxing in bed"
print(status)

# انتساب مقدار یک متغیر به متغیر دیگر
default_option = "upload"
new_status = "download"
new_status = default_option
print(new_status)

# مثال دیگر برای تغییر مقدار متغیر
temperature = "0 degree"
temperature = "100 degree"
print(temperature)

# ==============================
# مثال‌های اعداد و محاسبات
# ==============================

# متغیرهای عددی و محاسبات
ticket = 200
ticket2 = ticket * 10
print(ticket2)

# عملیات ریاضی با چند متغیر
private = 32
public = 10 - 5
total = public + private
print(total)
print(total - private - 10)
print("student:")
print(private * 10)

# عملیات ریاضی در فایل اصلی
active_users = 5
print(active_users + 1)
active_users = 5 + 1
print(active_users)

percent = 0.5 * 100
print(percent)

private_old = 56
public_old = 30
total_old = private_old + public_old
print(total_old)
print(private_old - public_old)

# ==============================
# عملیات روی رشته‌ها
# ==============================

ticket = "1000"
print(ticket)

ticket_3 = "baba"
ticket_4 = ticket_3 * 10
test = city_name * 10
print(ticket_4)
print(test)

# ==============================
# نمایش دما و واحدها
# ==============================

tempreture = "15"
print(tempreture)
print("tempreture:" + tempreture + " degrees")
print(tempreture + " degrees")

# ==============================
# مثال‌های Boolean و عملگر not
# ==============================

print("-------bool variable---------------")
restart = True
shutdown = False
prevent_logout = False
print(shutdown)
print(not restart)
print(prevent_logout)
print(not True)
print(not False)
print(restart)
print(not restart)

available = True
print(not available)
unavailable = not available
print(unavailable)

# مقادیر boolean از فایل اصلی
powered_on = True
print(powered_on)

# نفی مستقیم مقدار
print(not False)

# نفی مقدار یک متغیر
open = True
close = not open
print(close)

# نفی در هنگام چاپ
open = True
print(not open)

# مثال دیگر از نفی
morning = True
evening = not morning
print(evening)

# ==============================
# مثال‌های عملگرهای مقایسه‌ای
# ==============================

# عملگر برابری
print(10 == 9)  # از یادداشت شما
print(10 == 10)  # از فایل اصلی
print(10 == 9)   # از فایل اصلی

# مقایسه با متغیرها
entered_pin = 5448
expected_pin = 5440

one = 1
two = 2
print(one == two)

votes = 120
winning_target = 130
im_winner = votes == winning_target
print(im_winner)

level = 10
highest_level = 50
print(level == highest_level)

# عملگر نابرابری
print(1 != 10)  # از فایل اصلی

result = 1 != 10
print(result)

one = 1
two = 2
print(one != two)

# ==============================
# مثال‌های f-strings
# ==============================

# f-string با مقدار مستقیم
print(f"{2} new message")
print(f"{3} friends")

# f-string با متغیر
new_message = 4
print(f"{new_message} new messages")

# f-string با عملیات ریاضی
new = 5
read = 2
print(f"{new - read} unread messages")

# f-string با چندین متغیر
print(f"{3} new messages and {5} friend requests")

# f-string با فرمول پیچیده‌تر
x = 2
y = 5
t = f"{x/2} + {y/2}"
print(t)

# مثال‌های دیگر f-string
degree = 70
print(f"temperature: {degree} F")

movie = "vertigo"
display = f"airing tonight: {movie}"
print(display)

# ==============================
# مثال‌های عبارت‌ها (Expressions)
# ==============================

# الحاق رشته‌ها با عملگر +
print("folower :" + "55")

user = "snopdoge"
print("username:" + user)

temperature = "45"
print("temperature:" + temperature + "degree")

# الحاق رشته‌ها بدون فاصله
print("John" + "athan")

title = "Ms."
name = "Irene"
print(title + name)