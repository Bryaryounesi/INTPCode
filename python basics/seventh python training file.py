# فایل هفتم آموزش پایتون - عملیات رشته‌ها (Strings)
# ==============================
print("lesson: string operations")
line = "----------------------------"

# ==============================
# بخش ۱: تقسیم رشته‌ها (split)
# ==============================

# 🔥 ضروری: تقسیم رشته با فاصله پیش‌فرض
new_users = "Ann Jon Alex"
users_list = new_users.split()  # تقسیم بر اساس space
print("Original string:", new_users)
print("Split list:", users_list)

print(line)

# 🔥 ضروری: تقسیم رشته با جداکننده مشخص
words = "gear fault lights build-up"
word_list = words.split(" ")
print("Original:", words)
print("Split with space:", word_list)

print(line)

# ✅ تمرینی: تقسیم رشته با آندراسکور
user = "Lauren_25 F Architect"
user_list = user.split("_")
print("Original:", user)
print("Split with underscore:", user_list)

print(line)

# 🔥 ضروری: تقسیم رشته اعداد و مرتب‌سازی
numbers = "1 2 3 35 56 27 75 21 56 78 24"
numbers_list = numbers.split()
numbers_list.sort()
print("Original numbers string:", numbers)
print("Numbers list:", numbers_list)
print("Sorted numbers list:", numbers_list)

print(line)

# ✅ تمرینی: تقسیم داده‌های فروش
sales = "24K 29K 7K"
sales_list = sales.split()
print("Sales string:", sales)
print("Sales list:", sales_list)

print(line)

# ✅ تمرینی: تقسیم مسیر URL
path = "indiano.com/glossary/python"
path_list = path.split("/")
print("Path string:", path)
print("Path list:", path_list)

print(line)

# ==============================
# بخش ۲: جایگزینی در رشته‌ها (replace)
# ==============================

# 🔥 ضروری: جایگزینی ساده
special = "today's special is pizza"
new_special = special.replace("pizza", "pasta")
print("Original:", special)
print("After replace:", new_special)

print(line)

# ✅ تمرینی: جایگزینی با self-assignment
sport = "todays sport is football"
sport = sport.replace("football", "ping pong")
print("Sport after replace:", sport)

print(line)

# 🔥 ضروری: جایگزینی تمام تکرارها
june = "June sales target updated. Let's rock June!"
july = june.replace("June", "July")
print("Original:", june)
print("After replace:", july)

print(line)

# 🔥 ضروری: جایگزینی درصد و تاریخ
monthly = "Monthly reduction is 25%"
monthly = monthly.replace("25%", "15%")
print("Monthly update:", monthly)

release_date = "release date : 24th september"
update_date = release_date.replace("24th september", "16th november")
print("Original date:", release_date)
print("Updated date:", update_date)

print(line)

# ✅ تمرینی: جایگزینی مستقیم در print
welcome = "welcome to the company"
print("Welcome message:", welcome.replace("the", "our"))

print(line)

# 🔥 ضروری: ترکیب replace و split
tech_stack = "angular node mongo express"
tech_stack = tech_stack.replace("angular", "react")
tech_stack_list = tech_stack.split()
print("Original tech stack:", "angular node mongo express")
print("Updated tech stack:", tech_stack)
print("Tech stack list:", tech_stack_list)

print(line)

# ==============================
# بخش ۳: مثال‌های ترکیبی و کاربردی
# ==============================

# 🔥 ضروری: پردازش داده‌های کاربر
user_data = "john_doe_25_M_developer"
user_info = user_data.split("_")
print("User data string:", user_data)
print("User info list:", user_info)

# 🔥 ضروری: فرمت‌بندی مجدد برای نمایش
formatted_user = " ".join(user_info)
print("Formatted user:", formatted_user)

print(line)

# 🔥 ضروری: پردازش لاگ‌های سیستم
log_entry = "ERROR 2024-01-15 14:30:25 Database connection failed"
log_parts = log_entry.split()
print("Log entry:", log_entry)
print("Log parts:", log_parts)

# 🔥 ضروری: استخراج نوع خطا
error_type = log_parts[0]
print("Error type:", error_type)

print(line)

# 🔥 ضروری: پردازش CSV داده
csv_data = "name,age,city,john,25,new york,jane,30,los angeles"
csv_list = csv_data.split(",")
print("CSV data:", csv_data)
print("CSV list:", csv_list)

# 🔥 ضروری: گروه‌بندی داده‌ها به رکوردهای ۳تایی
records = []
for i in range(0, len(csv_list), 3):
    record = csv_list[i:i+3]
    records.append(record)
print("Grouped records:", records)

print(line)

# ==============================
# بخش ۴: مثال‌های تمرینی تکمیلی
# ==============================

# ✅ تمرینی: جایگزینی واحد پول
price = "50 Dollars"
new_price = price.replace("Dollars", "$")
print("Original price:", price)
print("Updated price:", new_price)

# ✅ تمرینی: جایگزینی جداکننده اعداد
value = "44,000"
fixed_value = value.replace(",", ".")
print("Original value:", value)
print("Fixed value:", fixed_value)

# ✅ تمرینی: جایگزینی در هشتگ‌ها
tags = ".code .today"
hash_tag = tags.replace(".", "#")
print("Original tags:", tags)
print("Hashtags:", hash_tag)

print(line)

print("End of string operations training")