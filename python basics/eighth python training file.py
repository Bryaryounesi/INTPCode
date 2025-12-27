# فایل هشتم آموزش پایتون - توابع (Functions)
# ==============================
print("Lesson: Functions")
line = "----------------------------"

# ==============================
# 🔥 ضروری: توابع پایه بدون پارامتر
# ==============================
def greet_ron():  # ضروری
    name = "Ron"
    print(f"Hello, {name}")
greet_ron()

def greet_lesli():  # ضروری
    name = "Lesli"
    print(f"Hello, {name}")
greet_lesli() 

print(line)

# ==============================
# 🔥 ضروری: توابع با متغیرهای داخلی
# ==============================
def user_status():  # ضروری
    status = "active"
    username = "Bob"
    print(f"{username} is {status}")
user_status()

def lamp_status():  # ضروری
    power = True
    print(f"Powered on: {power}")
lamp_status()

print(line)

# ==============================
# 🔥 ضروری: توابع با پارامتر
# ==============================
def greet(name):  # ضروری
    print(f"Hello, {name}")
greet("Ana")
greet("Barbara")

def month(name):  # ضروری
    print(f"In {name} I go to travel")
month("April")
month("November")
month("October")

def user_status_param(status):  # ضروری
    print(f"Bob is {status}")
user_status_param("inactive") 

print(line)

# ==============================
# 🔥 ضروری: توابع با پارامتر عددی
# ==============================
def display_half(number):  # ضروری
    half = number / 2
    print(half)
display_half(18)

def double_number(number):  # ضروری
    result = number * 2
    print(result)
    print(f"Half is {number / 2}")
double_number(95)

print(line)

# ==============================
# ✅ تمرینی: توابع بازگشتی یا return
# ==============================
def age_label(age):  # تمرینی
    label = "User age: " + age
    return label
print(age_label("20"))

def add_ten(number):  # تمرینی
    total = number + " number"
    return total
print(add_ten("30"))
print(add_ten("20"))

def update(user):  # تمرینی
    updater = "No emails: " + user
    return updater
result = update("Ann")
print(result)

print(line)

# ==============================
# 🔥 ضروری: توابع با چند پارامتر
# ==============================
def display(first, last):  # ضروری
    print(first + " " + last)
display("Alex", "Morgan")

def show_winners(first, second, third):  # ضروری
    print("First place: " + first)
    print("Second place: " + second)
    print("Third place: " + third)
show_winners("Kim", "Lee", "Ava")

def combine(first, second, third):  # ضروری
    return first + second + third
result = combine("big", "bad", "wolf")
print(result)

def create_email(name, year):  # ضروری
    return name + year + "@hutmail.com"
email = create_email("Jo", "1998")
print(email)

print(line)

# ==============================
# 🔥 ضروری: توابع با لیست
# ==============================
def display_programme(movies):  # ضروری
    print("Airing tonight:")
    print(movies)
movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def count_passengers(passengers):  # ضروری
    print(len(passengers))
passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)

def is_booked(passengers):  # ضروری
    print(len(passengers) > 4)
passengers = ["June", "Sam", "Lee"]
is_booked(passengers)

print(line)

# ==============================
# ✅ تمرینی: توابع با حلقه
# ==============================
def onboard_passengers(bookings):  # تمرینی
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1
onboard_passengers(5)

def display_progress(total_files):  # تمرینی
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")
display_progress(3)

def do_countdown(counter):  # تمرینی
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")  
do_countdown(3)

print(line)

# ==============================
# 🔥 ضروری: محدوده متغیرها (Variable Scope)
# ==============================
# Global scope
shipping = 10
def calculate_total(cart):  # ضروری
    print(cart + shipping)
calculate_total(54)

# Local scope
def add_bonus(salary):  # ضروری
    bonus = 100
    print(salary + bonus)
add_bonus(1900)

def apply_discount(price):  # ضروری
    discount = 10
    return price - discount
final_price = apply_discount(50)
print(final_price)

print(line)

# ==============================
# 🔥 ضروری: توابع با شرط
# ==============================
def add_shipping(cart):  # ضروری
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")
add_shipping(45)
add_shipping(200)

def can_drive(age):  # ضروری
    if age >= 18:
        print("Yes they can!")
can_drive(19)

def has_low_battery(level):  # ضروری
    if level <= 20:
        print("Low battery!")
has_low_battery(15)

print(line)

# ==============================
# ✅ تمرینی: مثال‌های ترکیبی و پیشرفته
# ==============================
def display_instructions(add_sugar):  # تمرینی
    if add_sugar:
        print("Enter amount of sugar")
    print("Select coffee type")
display_instructions(False)

def get_score_data(score_list, new):  # تمرینی
    score_list[4] = new
    print(f"New list: {score_list}")
    return score_list
score_list = [12, 19, 11.5, 10.25, 16, 15.4] 
get_score_data(score_list, True)    
get_score_data(score_list, False)    

def has_red(rgb_values):  # تمرینی
    if rgb_values[0] > 0:
        print("Red is in the mix!")
rgb = [153, 255, 51]
has_red(rgb)

def is_valid(parts):  # تمرینی
    print(len(parts) == 2)
email = "laurie@gmail.com"
user_and_domain = email.split("@")
is_valid(user_and_domain)

print("End of functions training file")