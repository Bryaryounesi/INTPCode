# فایل هشتم آموزش پایتون - توابع (Functions)
# ==============================
print("lesson: functions")
# ==============================
# توابع پایه بدون پارامتر
def greet_ron():
    name = "Ron"
    print(f"hello , {name}")
greet_ron()

def greet_lesli():
    name = "lesli"
    print(f"hello , {name}")
greet_lesli() 

print("-----------two variable---------------------")

def user_status():
    status = "active"
    username = "bob"
    print(f"{username} is {status}")
user_status()

print("------------boolin variable-------------------")

def lamp_status():
    power = True
    print(f"powerd on : {power}")
lamp_status()

print("-----------parameter------------------")

def greet(name):
    print(f"hello , {name}")
greet("ana")
greet("barbara")

print("--------------------------------")

def mounth(name):
    print(f"in {name} I go to travel")
mounth("april")
mounth("november")
mounth("october")

print("-------------------------------------")
def user_status(status):
    print(f"bob is {status}")
user_status("inactive") 

print("------------number parameter-------------------")

def display_half(number):
    half = number/2
    print(half)
display_half(18)

print("--------------------------------")

def double_number(number):
    result = number*2
    print(result)
    print(f"half is {number/2}")
double_number(95)

print("-------------------------------------")
def greet(name):
    print(f"good morning {name}")
greet("johanna")

print("---------------return ----------------------")

def age_label(age):
    label = "user_age:" + age
    return label

print(age_label("20"))

print("-------------------------------------")

def add_ten(number):
    total = number + " number"
    return total
print(add_ten("30"))
print(add_ten("20"))

print("-------------------------------------")

def update(user):
    updater = "no emails:" + user
    return updater
result = update("Ann")
print(result)

print("---------best examples--------------")

def one():
    print(1)
    print(2)
    print(3)
one()

print("--------------")

def two():
     name = "Ali"
     print(name) 
two() 

print("--------------")

def three():
    username = "nahid" 
    print(f"hello , {username}")
three()    

print("--------------")

def five():
    user = "bahram"
    user_2 = "sasan"
    print(f"my workers name is {user} and {user_2}")
five() 

print("--------------")

def six(name):
    print(f"hello , {name}")
six("hadi")
six("andi") 
six("fati")
six("hena")

print("-----boolin---------")

def user_sleeping(check):
    user = "shadi"
    print(f"{user} is awake: {check}")
user_sleeping(True)    
user_sleeping(False)

print("-----------number---------------")

def student_numbers(number):
    classroom_1 = 85/number
    classroom_2 = 46/number
    sum = (classroom_1 + classroom_2)*number
    print(f"students number: {sum}")
student_numbers(3)

print("------return--------")

def student_numbers(number):
    sum = (5*number)/3
    return sum
print(student_numbers(50))
print(student_numbers(40))

print("-------------------------------------")
# توابع با پارامترهای چندگانه
def display(first, last):
    print(first + " " + last)
display("Alex", "Morgan")

def show_winners(first, second, third):
    print("First place: " + first)
    print("Second place: " + second)
    print("Third place: " + third)
show_winners("Kim", "Lee", "Ava")

def combine(first, second, third):
    return first + second + third
result = combine("big", "bad", "wolf")
print(result)

def create_email(name, year):
    return name + year + "@hutmail.com"
email = create_email("jo", "1998")
print(email)

def add_prefix(prefix, word):
    return prefix + word
new_word = add_prefix("re", "do")
print(new_word)

def show_queue(current, up_next):
    print("now playing: " + current)
    print("up next: " + up_next)
show_queue("Hey Joe", "Purple Haze")

def mix(first, second, third):
    print(first + second + third)
mix("Peter", "Piper", "Picked")

print("-------------------------------------")
# نام‌گذاری توصیفی توابع
def get_final_price(price, tax):
    return price + tax
price = get_final_price(30, 1.5)
print(price)

def create_email(name):
    return name + "@hutmail.com"
email = create_email("jo")
print(email)

def get_telephone(prefix, number):
    return prefix + number

def calculate_sum(num_1, num_2):
    return num_1 + num_2

def is_freezing(temperature):
    return temperature < 0
freezing = is_freezing(-3)
print(freezing)

def calculate_sum(num_1, num_2):
    return num_1 + num_2

def calculate_difference(num_1, num_2):
    return num_1 - num_2

def display_item_price(item, price):
    print(f"{item}: ${price}")
display_item_price("chocolate", 3)

def generate_username(name, b_day):
    return f"{name}_{b_day}"
user = generate_username("ty", 17)
print(user)

def get_free_seats(booked, total):
    return total - booked
free = get_free_seats(13, 20)
print(free)

def get_successor(number):
    return number + 1

def get_predecessor(number):
    return number - 1

successor = get_successor(1)
print(successor)
predecessor = get_predecessor(1)
print(predecessor)

print("-------------------------------------")
# محدوده متغیرها (Variable Scope)
# ==============================
# Global scope
shipping = 10
def calculate_total(cart):
    print(cart + shipping)
calculate_total(54)

rent = 1000
def calculate_spendings(groceries):
    print(f"Total: {rent + groceries}")
print(f"Rent: {rent}")
calculate_spendings(300)

# Local scope
def add_bonus(salary):
    bonus = 100
    print(salary + bonus)
add_bonus(1900)

def apply_discount(price):
    discount = 20
    discount = 10
    return price - discount
final_price = apply_discount(50)
print(final_price)

print("-------------------------------------")
# ==============================
# توابع با شرط‌ها
def add_shipping(cart):
    if cart < 100:
        print(f"Total: {cart + 10}")
    else:
        print(f"Total: {cart}")
add_shipping(45)
add_shipping(200)

def can_drive(age):
    if age >= 18:
        print("Yes they can!")
can_drive(19)
can_drive(20)

def has_low_battery(level):
    if level <= 20:
        print("Low battery!")
has_low_battery(15)

def get_waiting_list(signups):
    if signups > 200:
        print(f"Waiting list: {signups - 200}")
get_waiting_list(250)
get_waiting_list(100)

def calculate(operator, x, y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x - y)
    else:
        print(f"unknown: {operator}")
calculate("-", 30, 10)

def show_progress(points):
    if points > 1000:
        print("New highest score!")
    print("Ready for the next level?")
show_progress(900)

def show_status(inbox):
    if inbox > 1000:
        print("Inbox full!")
    print("You have new messages!")
show_status(900)

def get_off(price, discount):
    if price >= 100:
        print(f"price is {price - discount}$ ")
    else:
        print(f"price is {price}$")
get_off(50, 20) 
get_off(102, 20) 

def show_score(score):
    if score < 30:
        print("Score too low")
    elif score == 100:
        print("Top score!")
    else:
        print("On to the next level!")
show_score(100)

print("-------------------------------------")
# ==============================
# توابع با لیست‌ها
# ==============================

def display_programme(movies):
    print("Airing tonight:")
    print(movies)
movie_list = ["Alien", "Moon"]
display_programme(movie_list)

def count_passengers(passengers):
    print(len(passengers))
passengers = ["June", "Sam", "Lee"]
count_passengers(passengers)

def is_booked(passengers):
    print(len(passengers) > 4)
passengers = ["June", "Sam", "Lee"]
is_booked(passengers)

def has_two_for_one(basket):
    print(len(basket) >= 2)
basket_items = ["t-shirt", "jeans", "jeans"]
has_two_for_one(basket_items)

def is_multiplayer(players):
    print(len(players) == 2)
players = ["Amy", "Jay"]
is_multiplayer(players)

def get_winner(top_players):
    winner = top_players[0]
    print(f"Game winner: {winner}")
top_players = ["Jay", "Meg", "Cy"]
get_winner(top_players)

def update_first_place(player_list, player):
    player_list[0] = player
    return player_list
player_list = ["Jay", "Meg", "Cy"]
print(player_list)
player_list = update_first_place(player_list, "Lena")
print(player_list)

def set_initials(names, initial):
    names[0] = initial
    print(names)
author_names = ["Francis", "Scott", "Fitzgerald"]
set_initials(author_names, "F.")  

def tabeh(names, fav): 
    print(names)
    names[3] = fav
    print(names)
    return names
names = ["barbi", "gala", "hadi", "jamal", "yana"]  
tabeh(names, "raha")

def add_sports(plans):
    plans[0] = "jogging"
plans = ["reading", "brunch with Meg", "cooking", "netflix"]
add_sports(plans)
print(plans)

print("-------------------------------------")
# ==============================
# توابع با حلقه‌ها
def onboard_passengers(bookings):
    counter = 1
    while counter <= bookings:
        print(f"Passenger {counter} on board")
        counter += 1
onboard_passengers(5)

def functiona(books):
    counter = 1
    while counter < books:
        print(f"we have anything")
        counter += 1
functiona(4)

def display_progress(total_files):
    for i in range(total_files):
        print(f"Downloading file {i} out of {total_files}")
display_progress(3)

def do_countdown(counter):
    while counter > 0:
        print(counter)
        counter -= 1
    print("Go!")  
do_countdown(3)

def display_stars(rows):
    counter = 0
    while counter < rows:
        print("***")
        counter += 1
display_stars(2)

def show_progress(total):
    for i in range(total):
        print(f"Installing next update")
show_progress(3)

def display_progress():
    for i in range(3):
        print(f"Downloading file {i} out of 3")
display_progress()

def show_notifications(messages):
    for i in range(messages):
        print("Failed to send message")
show_notifications(3)

def halve_prices(cart):
    for price in cart:
        print(f"New price: {price/2}")
cart_list = [5, 20, 8]
new_cart_list = [20, 15, 35, 60]
halve_prices(cart_list)
halve_prices(new_cart_list)

def display_players(team):
    number = 1
    for name in team:
        print(f"Player {number}: {name}")
team_1 = ["Kim", "Lee"]
team_2 = ["Meg", "Jo"]
display_players(team_1)

def show_next_track():
    playlist = ["Hey Jude", "Helter Skelter", "Something"]
    for track in playlist:
        print(f"Next up: {track}")
show_next_track()

def show_next_track(playlist):
    for track in playlist:
        print(f"Next up: {track}")
beatles = ["Hey Jude", "Helter Skelter", "Something"]
beethoven = ["Symphony No. 1", "Symphony No. 9"]
show_next_track(beethoven)
show_next_track(beatles)

def showing_list(film): 
    for movie in film:
        print(f"my favourite movie is {movie}")
movie_list = ["terminator", "lusy"]
movie_list_2 = ["seven", "lust", "gone girl", "falling"]
showing_list(movie_list)
showing_list(movie_list_2)  

print("-------------------------------------")
# ==============================
# مثال‌های ترکیبی و پیشرفته
# ==============================

alarm_time = 7
def set_alarm():
    print(f"New alarm set for {alarm_time}AM")
set_alarm()

def display_instructions(add_sugar):
    if add_sugar:
        print("Enter amount of sugar")
    print("Select coffee type")
display_instructions(False)

def get_score_data(listo, new):
    score_list[4] = new
    print(f"new list : {score_list}")
    return score_list
score_list = [12, 19, 11.5, 10.25, 16, 15.4] 
print(f"primary list :{score_list}")
get_score_data(score_list, True)    
get_score_data(score_list, False)    
score_list.append(-12000)
get_score_data(score_list, 9)    

def has_red(rgb_values):
    if rgb_values[0] > 0:
        print("Red is in the mix!")
rgb = [153, 255, 51]
has_red(rgb)

def is_valid(parts):
    print(len(parts) == 2)
email = "laurie@gmail.com"
user_and_domain = email.split("@")
is_valid(user_and_domain)

def onboard_passengers(bookings):
    counter = 0
    while counter <= bookings:
        counter += 1
    print("Onboarding passenger")
onboard_passengers(5)

def help_customers(customers):
    counter = 1
    while counter < customers:
        print(f"Customer no.{counter} go to the next free desk")
        counter += 1
help_customers(3)

def show_programme(day):
    for event in day:
        print(f"Today: {event}")
monday = ["Swan Lake", "Ravel - Piano Concerto"]
tuesday = ["La Boheme"]
show_programme(monday)
show_programme(tuesday)

print("End of functions training")