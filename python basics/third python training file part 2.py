# فایل چهارم آموزش پایتون - دستورات شرطی پیشرفته
# ==============================

print("fourth python training file")
print("subject: else and elif statements")

# ==============================
# دستورات if و else پایه
# ==============================

# سیستم موجودی کالا
available = False
if available:
    print("In stock")
else:
    print("Out of stock")

# سیستم کنترل نور
is_day = False
if is_day:
    print("lights off")
else:
    print("lights on")

# سیستم اشتراک
is_subscribed = True
if is_subscribed:
    print("Enjoy 10% off!")
else:
    print("Become a subscriber!")

# سیستم حدس عدد
chosen_number = 7
if chosen_number == 12:
    print("You guessed right!")
else:
    print("Have another go")

# سیستم پیشنهاد دوستان
common_friends = 3
if common_friends > 2:
    print("Friend suggestions: Sue")
else:
    print("No new friend suggestions")

# سیستم مدیریت کاربران
membership = "gold"
if membership == "gold":
    print("Add to database 1")
else:
    print("Add to database 2")

# سیستم سطح‌بندی
points = 7600
points_needed = 8000
if points >= points_needed:
    print("You're Level 2!")
else:
    left = points_needed - points
    print(f"Need {left} more points for Level 2")

# سیستم پرداخت
paid = False
if paid:
    print("Thank you for your purchase")
else:
    print("Payment required")

# ==============================
# دستورات elif (شرط‌های زنجیره‌ای)
# ==============================

# سیستم سلام بر اساس ساعت
hour = 13
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")

# سیستم نمره‌دهی
score = 75
if score >= 90:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >= 50:
    print("Your grade is C")
else:
    print("Your grade is D")

# سیستم رانندگی بر اساس سن
age = 25
if age < 18:
    print("You're too young for driving")
elif age < 60:
    print("You can drive")
else:
    print("You're too old for driving")

# سیستم درجه‌بندی دما
temperature = 5
if temperature < 0:
    print("Brr...")
elif temperature == 0:
    print("It's freezing!")
elif temperature < 10:
    print("It's cold out")
else:
    print("Nice temperature")

# سیستم کنترل صدا
volume = 40
if volume < 20:
    print("I can't hear that")
elif volume >= 70:
    print("It's too loud")
else:
    print("Perfect volume level")

# ==============================
# عملگر AND (همه شرایط باید True باشند)
# ==============================

# سیستم رانندگی با چند شرط
age = 19
has_permit = True
if age >= 18 and has_permit:
    print("You can drive")
else:
    print("You can't drive")

# سیستم خواب با شرایط ترکیبی
caffeine = True
time = "night"
if caffeine and time == "night":
    print("Awake all night")
else:
    print("Good night's sleep")

# سیستم ورود با احراز هویت
age = 21
has_reservation = True
if age >= 18 and has_reservation:
    print("Entry granted")
else:
    print("Entry denied")

# ==============================
# عملگر OR (حداقل یک شرط باید True باشد)
# ==============================

# سیستم دریافت گواهینامه
average_grade = "B"
final_score = 1400
won_competition = True
if average_grade == "A" or final_score >= 1500 or won_competition:
    print("Certificate achieved!")
else:
    print("Certificate not achieved")

# سیستم فعالیت‌های تفریحی
is_summer = False
is_warm = True
if is_summer or is_warm:
    print("Go for a swim")
else:
    print("Stay indoors")

# سیستم اتصال اینترنت
mobile_internet = True
wifi = False
if mobile_internet or wifi:
    print("Loading...")
else:
    print("No internet connection")

# سیستم ارتقای مقاله
likes = 40
shares = 50
comments = 70
if likes > 50 or shares >= 80 or comments >= 70:
    print("Article promoted!")
else:
    print("Article needs more engagement")

# ==============================
# سیستم‌های منو و انتخاب
# ==============================
# سیستم تلفن گویا
number_pressed = 2
if number_pressed == 1:
    print("To hear store hours")
elif number_pressed == 2:
    print("To call the manager")
elif number_pressed == 3:
    print("To record a message")
elif number_pressed == 4:
    print("To hear options again")
else:
    print("Invalid option")
# سیستم پاسخ‌دهی
response = "maybe"
if response == "yes":
    print("You picked YES")
elif response == "no":
    print("You picked NO")
else:
    print("You must pick YES or NO")

# سیستم مسیریابی
direction = "left"
if direction == "left":
    print("Turn left")
elif direction == "u_turn":
    print("Make U-turn")
elif direction == "right":
    print("Turn right")
else:
    print("Go straight")

# ==============================
# سیستم‌های چندزبانه
# ==============================

language = "english"
if language == "english":
    message = "Thank you"
elif language == "german":
    message = "Danke"
elif language == "spanish":
    message = "Gracias"
elif language == "french":
    message = "Merci"
else:
    message = "Thank you"  # پیش‌فرض
print(message)

# ==============================
# سیستم‌های مدیریت پیام
# ==============================

# سیستم پیام‌های خوانده نشده
read_messages = 5
unread_messages = 7
if unread_messages > 0:
    print(f"You have {unread_messages} unread messages")
else:
    print(f"No unread messages, {read_messages} messages read")

# سیستم حذف پیام
read_status = False
time_elapsed = 50
if read_status or time_elapsed > 40:
    print("Can't delete the message")
else:
    print("Message deleted")

# ==============================
# سیستم‌های هوشمند
# ==============================

# سیستم توصیه فیلم
rating = 87
if rating >= 90:
    print("Buy movie tickets - Highly recommended!")
elif rating >= 70:
    print("Watch at home - Good choice")
else:
    print("Skip this one")

# سیستم هشدار باتری
battery_level = 15
if battery_level <= 20:
    print("Low battery warning!")
    if battery_level <= 10:
        print("Critical battery level!")
else:
    print("Battery level is good")

# سیستم مدیریت ایمیل
email = "user@example.com"
if email == "admin@system.com":
    print("Welcome, Administrator")
elif email == "manager@system.com":
    print("Hello, Manager")
elif "user" in email:
    print("Welcome, User")
else:
    print("Unknown email address")

# ==============================
# سیستم‌های پیشرفته با ترکیب شرط‌ها
# ==============================

# سیستم تخفیف هوشمند
age = 65
is_student = False
is_vip = True

if age >= 65 or is_student:
    discount = 25
elif is_vip and age >= 18:
    discount = 15
else:
    discount = 0

print(f"Your discount: {discount}%")

# سیستم توصیه سفر
weather = "sunny"
day_type = "weekend"
has_car = True

if weather == "sunny" and (day_type == "weekend" or has_car):
    print("Perfect day for a trip!")
elif weather == "rainy" and day_type == "weekend":
    print("Good day for indoor activities")
else:
    print("Normal day")

# سیستم مدیریت آلارم
alarm_set = True
is_holiday = False
is_sick = False

if alarm_set and not is_holiday and not is_sick:
    print("Alarm will ring at 7:00 AM")
elif is_holiday:
    print("Alarm disabled - Holiday")
elif is_sick:
    print("Alarm disabled - Sick day")
else:
    print("No alarm set")

print("End of fourth training file")