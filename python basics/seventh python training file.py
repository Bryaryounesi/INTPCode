# فایل هفتم آموزش پایتون - عملیات رشته‌ها
# ==============================

print("lesson name : string operations")

# ==============================
# تقسیم رشته‌ها (split)
# ==============================

# تقسیم رشته با فاصله پیش‌فرض
new_users = "Ann Jon Alex"
users_list = new_users.split()
print("Original string:", new_users)
print("Split list:", users_list)
print("Direct split:", new_users.split())

print("-------------------------")

# تقسیم رشته با جداکننده مشخص
words = "gear fault lights build-up"
word_list = words.split(" ")
print("Original:", words)
print("Split with space:", word_list)

print("-------------------------")

# تقسیم رشته با آندراسکور
user = "Lauren_25 F Architect"
print("Original:", user)
print("Split with underscore:", user.split("_"))

print("-------------------------")

# تقسیم اعداد در رشته
numbers = "1 2 3 35 56 27 75 21 56 78 24"
numbers_list = numbers.split()
print("Original numbers string:", numbers)
print("Numbers list:", numbers_list)
numbers_list.sort()
print("Sorted numbers list:", numbers_list)

print("-------------------------")

# تقسیم داده‌های فروش
sales = "24K 29K 7K"
sales_list = sales.split()
print("Sales string:", sales)
print("Sales list:", sales_list)

print("-------------------------")

# تقسیم داده‌های آلودگی
pollution = "40ppm 55ppm 60ppm"
pollution_list = pollution.split()
print("Pollution string:", pollution)
print("Pollution list:", pollution_list)

print("-------------------------")

# تقسیم مسیر URL
path = "indiano.com/glossary/python"
path_list = path.split("/")
print("Path string:", path)
print("Path list:", path_list)

print("-------------------------")

# تقسیم و مرتب‌سازی همزمان
levels = ["c", "b", "a", "g"]
codes = "2 3 9 0"
levels.sort()
print("Sorted levels:", levels)

codes_list = codes.split()
print("Codes string:", codes)
print("Codes list:", codes_list)
codes_list.sort()
print("Sorted codes list:", codes_list)

print("-------------------------")

# ==============================
# جایگزینی در رشته‌ها (replace)
# ==============================

# جایگزینی ساده
special = "today's special is pizza"
new_special = special.replace("pizza", "pasta")
print("Original:", special)
print("After replace:", new_special)

# تلاش برای تغییر بدون ذخیره‌سازی
special = "today's special is pizza"
special.replace("pizza", "spaghetti")
print("Without assignment:", special)  # تغییری نمی‌کند

print("-------------------------")

# جایگزینی با self-assignment
sport = "todays sport is football"
sport = sport.replace("football", "ping pong")
print("Sport after replace:", sport)

print("-------------------------")

# جایگزینی تمام تکرارها
june = "June sales target updated. Let's rock June!"
july = june.replace("June", "July")
print("Original:", june)
print("After replace:", july)

print("-------------------------")

# جایگزینی در اخبار
news = "israeel military force in ghaza"
report = news.replace("israeel", "usa")
print("Original news:", news)
print("Updated report:", report)

print("-------------------------")

# جایگزینی در گروه سنی
age_group = "twenty-five to thirty"
updated = age_group.replace("thirty", "thirty-five")
print("Original age group:", age_group)
print("Updated age group:", updated)

print("-------------------------")

# جایگزینی بخشی از عدد
age = "forty five to fifty"
update_age = age.replace("five", "two")
print("Original age:", age)
print("Updated age:", update_age)

print("-------------------------")

# جایگزینی درصد
monthly = "Monthly reduction is 25%"
monthly = monthly.replace("25%", "15%")
print("Monthly update:", monthly)

print("-------------------------")

# جایگزینی درصد با فاصله
off = "weakly off is 23 %"
update_off = off.replace("23", "30")
print("Original off:", off)
print("Updated off:", update_off)

print("-------------------------")

# جایگزینی تاریخ
release_date = "relrase date : 24th september"
update = release_date.replace("24th september", "16th november")
print("Original date:", release_date)
print("Updated date:", update)

print("-------------------------")
# جایگزینی مستقیم در print
welcome = "welcome to the company"
print("Welcome message:", welcome.replace("the", "our"))

print("-------------------------")

# ترکیب replace و split
tech_stack = "angular node mongo express"
tech_stack = tech_stack.replace("angular", "react")
tech_stack_list = tech_stack.split()
print("Original tech stack:", "angular node mongo express")
print("Updated tech stack:", tech_stack)
print("Tech stack list:", tech_stack_list)

print("-------------------------")

# جایگزینی در لیست فیلم‌ها
old_top_movies = "the power of the dog - trapped - tenet"
new_top_movies = old_top_movies.replace("trapped", "moonfall")
print("Original movies:", old_top_movies)
print("Updated movies:", new_top_movies)

print("-------------------------")

# ==============================
# مثال‌های تکمیلی از فایل اصلی
# ==============================

# تقسیم با جداکننده مختلف
signups = "44-22-44-11"
signups_list = signups.split("-")
print("Signups string:", signups)
print("Signups list:", signups_list)

print("-------------------------")

# جایگزینی با self-assignment
yearly = "Discount increased to 2%"
yearly = yearly.replace("2%", "4%")
print("Yearly discount:", yearly)

print("-------------------------")

# تبدیل رشته اعداد به int (با حذف فاصله)
numbers_example = "1 2 3 35 56 27 75 21 56 78 24"
print("Original numbers string:", numbers_example)
print("Type before:", type(numbers_example))

# حذف فاصله‌ها
numbers_no_space = numbers_example.replace(" ", "")
print("After removing spaces:", numbers_no_space)

# تبدیل به int
try:
    numbers_int = int(numbers_no_space)
    print("As integer:", numbers_int)
    print("Type after:", type(numbers_int))
except ValueError:
    print("Cannot convert to integer - contains multiple numbers")

print("-------------------------")

# تقسیم کدهای منطقه‌ای
area_codes = "1150 1190 1100 1700"
codes_list = area_codes.split()
print("Area codes string:", area_codes)
print("Area codes list:", codes_list)

print("-------------------------")

# تقسیم با جداکننده نقطه
decimal_numbers = "1150, 11.24, 89.20,11.90.11. 35. 89. 67"
decimal_list = decimal_numbers.split(".")
print("Decimal string:", decimal_numbers)
print("Split with dot:", decimal_list)

print("-------------------------")

# تقسیم نام‌ها با نقطه
names = "gard.sima.tar.orion. polin. tare.vava.werd.24.34.89.34.90"
names_list = names.split(".")
print("Names string:", names)
print("Names split with dot:", names_list)

print("-------------------------")

# جایگزینی برای اصلاح غلط املایی
answer = "The answer is INcorrect"
updated_answer = answer.replace("INcorrect", "incorrect")
print("Original answer:", answer)
print("Corrected answer:", updated_answer)

print("-------------------------")

# جایگزینی واحد پول
price = "50 Dollars"
new_price = price.replace("Dollars", "$")
print("Original price:", price)
print("Updated price:", new_price)

print("-------------------------")

# جایگزینی جداکننده اعداد
value = "44,000"
fixed_value = value.replace(",", ".")
print("Original value:", value)
print("Fixed value:", fixed_value)

print("-------------------------")

# جایگزینی در هشتگ‌ها
tags = ".code .today"
hash_tag = tags.replace(".", "#")
print("Original tags:", tags)
print("Hashtags:", hash_tag)

print("-------------------------")

# ==============================
# مثال‌های کاربردی ترکیبی
# ==============================

# پردازش داده‌های کاربر
user_data = "john_doe_25_M_developer"
user_info = user_data.split("_")
print("User data string:", user_data)
print("User info list:", user_info)

# فرمت‌بندی مجدد
formatted_user = " ".join(user_info)
print("Formatted user:", formatted_user)

print("-------------------------")

# پردازش لاگ‌های سیستم
log_entry = "ERROR 2024-01-15 14:30:25 Database connection failed"
log_parts = log_entry.split()
print("Log entry:", log_entry)
print("Log parts:", log_parts)

# استخراج نوع خطا
error_type = log_parts[0]
print("Error type:", error_type)

print("-------------------------")

# پردازش CSV داده
csv_data = "name,age,city,john,25,new york,jane,30,los angeles"
csv_list = csv_data.split(",")
print("CSV data:", csv_data)
print("CSV list:", csv_list)

# گروه‌بندی داده‌ها
records = []
for i in range(0, len(csv_list), 3):
    record = csv_list[i:i+3]
    records.append(record)
print("Grouped records:", records)

print("End of string operations training")