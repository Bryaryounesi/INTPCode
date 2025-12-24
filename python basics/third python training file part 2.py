
# If-Else Basics - دستورات شرطی پایه
# ============================================
# 🔥 ضروری → تصمیم‌گیری و کنترل جریان در اتوماسیون
available = False
if available:
    print("In stock")
else:
    print("Out of stock")

is_day = False
if is_day:
    print("lights off")
else:
    print("lights on")

is_subscribed = True
if is_subscribed:
    print("Enjoy 10% off!")
else:
    print("Become a subscriber!")

chosen_number = 7
if chosen_number == 12:
    print("You guessed right!")
else:
    print("Have another go")

# ⚠️ غیرضروری / تمرینی
common_friends = 3
if common_friends > 2:
    print("Friend suggestions: Sue")
else:
    print("No new friend suggestions")
membership = "gold"
if membership == "gold":
    print("Add to database 1")
else:
    print("Add to database 2")
points = 7600
points_needed = 8000
if points >= points_needed:
    print("You're Level 2!")
else:
    left = points_needed - points
    print(f"Need {left} more points for Level 2")
paid = False
if paid:
    print("Thank you for your purchase")
else:
    print("Payment required")

# ============================================
# Elif Chains - شرط‌های زنجیره‌ای
# ============================================
# 🔥 ضروری → تصمیم‌گیری چندشاخه در اتوماسیون
hour = 13
if hour < 12:
    print("Good morning")
elif hour < 17:
    print("Good afternoon")
elif hour < 21:
    print("Good evening")
else:
    print("Good night")

score = 75
if score >= 90:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >= 50:
    print("Your grade is C")
else:
    print("Your grade is D")

# ⚠️ غیرضروری / تمرینی
age = 25
if age < 18:
    print("You're too young for driving")
elif age < 60:
    print("You can drive")
else:
    print("You're too old for driving")
temperature = 5
if temperature < 0:
    print("Brr...")
elif temperature == 0:
    print("It's freezing!")
elif temperature < 10:
    print("It's cold out")
else:
    print("Nice temperature")
volume = 40
if volume < 20:
    print("I can't hear that")
elif volume >= 70:
    print("It's too loud")
else:
    print("Perfect volume level")

# ============================================
# Logical AND - همه شرایط باید True باشند
# ============================================
# 🔥 ضروری → ترکیب شرط‌ها برای تصمیم‌گیری دقیق
age = 19
has_permit = True
if age >= 18 and has_permit:
    print("You can drive")
else:
    print("You can't drive")

# ⚠️ غیرضروری / تمرینی
caffeine = True
time = "night"
if caffeine and time == "night":
    print("Awake all night")
else:
    print("Good night's sleep")
age = 21
has_reservation = True
if age >= 18 and has_reservation:
    print("Entry granted")
else:
    print("Entry denied")

# ============================================
# Logical OR - حداقل یک شرط True باشد
# ============================================
# 🔥 ضروری → تصمیم‌گیری چندگزینه‌ای
average_grade = "B"
final_score = 1400
won_competition = True
if average_grade == "A" or final_score >= 1500 or won_competition:
    print("Certificate achieved!")

# ⚠️ غیرضروری / تمرینی
is_summer = False
is_warm = True
if is_summer or is_warm:
    print("Go for a swim")
else:
    print("Stay indoors")
mobile_internet = True
wifi = False
if mobile_internet or wifi:
    print("Loading...")
else:
    print("No internet connection")
likes = 40
shares = 50
comments = 70
if likes > 50 or shares >= 80 or comments >= 70:
    print("Article promoted!")
else:
    print("Article needs more engagement")

# ============================================
# Menu & Selection Systems - سیستم‌های منو و انتخاب
# ============================================
# 🔥 ضروری → انتخاب گزینه‌ها در اتوماسیون
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

# ⚠️ غیرضروری / تمرینی
response = "maybe"
if response == "yes":
    print("You picked YES")
elif response == "no":
    print("You picked NO")
else:
    print("You must pick YES or NO")
direction = "left"
if direction == "left":
    print("Turn left")
elif direction == "u_turn":
    print("Make U-turn")
elif direction == "right":
    print("Turn right")
else:
    print("Go straight")

# ============================================
# Multi-language & Message Management - سیستم‌های چندزبانه و پیام
# ============================================
# 🔥 ضروری → گزارش و تعامل هوشمند با کاربر
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
    message = "Thank you"
print(message)

read_messages = 5
unread_messages = 7
if unread_messages > 0:
    print(f"You have {unread_messages} unread messages")
else:
    print(f"No unread messages, {read_messages} messages read")

# ⚠️ غیرضروری / تمرینی
read_status = False
time_elapsed = 50
if read_status or time_elapsed > 40:
    print("Can't delete the message")
else:
    print("Message deleted")

# ============================================
# Smart Systems - سیستم‌های هوشمند
# ============================================
# 🔥 ضروری → شرط‌های پیچیده و تصمیم‌گیری در اتوماسیون هوشمند
battery_level = 15
if battery_level <= 20:
    print("Low battery warning!")
    if battery_level <= 10:
        print("Critical battery level!")
else:
    print("Battery level is good")

email = "user@example.com"
if email == "admin@system.com":
    print("Welcome, Administrator")
elif email == "manager@system.com":
    print("Hello, Manager")
elif "user" in email:
    print("Welcome, User")
else:
    print("Unknown email address")

# ============================================
# Advanced Conditional Systems - شرط‌های پیشرفته
# ============================================
# 🔥 ضروری → ترکیب AND/OR و تصمیم‌گیری هوشمند
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

weather = "sunny"
day_type = "weekend"
has_car = True
if weather == "sunny" and (day_type == "weekend" or has_car):
    print("Perfect day for a trip!")
elif weather == "rainy" and day_type == "weekend":
    print("Good day for indoor activities")
else:
    print("Normal day")

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