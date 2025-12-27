# فایل ششم آموزش پایتون - عملیات لیست
print("lesson: list operations")
# ============================================

# 🔥 ضروری → پیدا کردن بزرگترین و کوچکترین مقدار
numbers = [12, 6, 5, 2, 7]
print("List:", numbers)
print("Max:", max(numbers))
print("Min:", min(numbers))

max_list = max(numbers)
min_list = min(numbers)
print("Max + Min:", max_list + min_list)

# 🔥 عملی → حداکثر سود هفتگی
weekly_profits = [20, 59, 43, 76, 24, 60]
max_profit = max(weekly_profits)
print(f"max profit: {max_profit} usd")
for profit in weekly_profits:
    print(f"Profit: {profit}")

# 🔥 ضروری → مرتب‌سازی لیست‌ها
scores = [10, 9.25, 8, 4.5, 17, 11.75]
scores.sort()
print("Sorted scores:", scores)

temperature = [10, 4, -1, 7, -5, 16, 0]
temperature.sort()
print("Sorted temperatures:", temperature)

names = ["cloe", "bill", "ana"]
names.sort()
print("Sorted names:", names)

grades = ["A", "C", "F", "B", "G"]
grades.sort()
print("Sorted grades:", grades)

oxygen_level = [19.99, 21.2, 20.85]
oxygen_level.sort()
print("Sorted oxygen levels:", oxygen_level)

# 🔥 جمع زدن لیست
signups = [12, 30, 40, 10, 4, 8]
print("Sum of signups:", sum(signups))
sumation = sum(signups)
print("Sum stored:", sumation)

coordinates = [0, 0, 0]
print("Min coordinate:", min(coordinates))

# 🔥 الحاق لیست‌ها (+)
database_1 = [1, 2, 3]
database_2 = [4, 5]
combine = database_1 + database_2
print("Combined databases:", combine)

seats = [1, 2, 3]
taken = [True, True, False]
print("Combined seats + status:", seats + taken)

consumers = ["jess", "mike", "lyne"]
order_numbers = [3, 2, 1]
print("Consumers + orders:", consumers + order_numbers)

team_1 = ["ana", 78, "kim", 25, "rose", 40]
team_2 = ["jerry", 24, "henry", 28]
print("Combined teams:", team_1 + team_2)

day_1 = [3.5, 2, 4]
day_2 = [1, 2]
overview = day_1 + day_2
print("Overview:", overview)

# 🔥 شمارش المنت‌ها (count)
answers = ["yes", "no", "sometimes", "yes", "no"]
print("Count of 'yes':", answers.count("yes"))

free_seats = [True, False, True, True, False]
seats_count = free_seats.count(True)
print("Count of True seats:", seats_count)

missions = ["mars", "moon", "mars", "ISS"]
print("Count of 'mars':", missions.count("mars"))

flavors = ["vanilla", "chocolate", "strawberry", "vanilla", "vanilla"]
print("Count of 'vanilla':", flavors.count("vanilla"))

code = [0, 3, 2, 0, 1, 0]
print("Count of 0:", code.count(0))

# 🔥 بررسی وجود المنت (in)
ingredients = ["milk", "suger", "eggs", "flour", "butter"]
has_suger = "suger" in ingredients
print("'suger' in ingredients:", has_suger)

winning_numbers = [2, 36, 40, 13]
has_21 = 21 in winning_numbers
print("13 in winning numbers:", 13 in winning_numbers)
print("20 in winning numbers:", 20 in winning_numbers)
print("Has 21 stored:", has_21)

schedule = ["ballet", "swimming", "running", "ballet"]
print("'ballet' in schedule:", "ballet" in schedule)
print("'running' in schedule:", "running" in schedule)
print("'going' in schedule:", "going" in schedule)

# 🔥 مثال‌های ترکیبی و کاربردی
students_1 = ["Anna", 16, "Kim", 16]
students_2 = ["Joe", 17, "Lee", 15]
print("All students:", students_1 + students_2)

customers = ["Jess", "Mike", "Lynn"]
order_numbers = [3, 1, 2]
orders = customers + order_numbers
print("Orders list:", orders)

savings = [220, 50, 1000, 70]
total = sum(savings)
number = len(savings)
average = total / number
print("Total savings:", total)
print("Average savings:", average)

savings_check = [220, 50, 1000, 70]
if 50 in savings_check:
    print("Found 50 in savings")

data = [15, 3, 8, 20, 3, 8]
print("Data:", data)
print("Max:", max(data))
print("Min:", min(data))
print("Sum:", sum(data))
print("Count of 3:", data.count(3))
print("Sorted:", sorted(data))

inventory = [10, 5, 8, 3, 15]
print("Inventory:", inventory)
print("Max stock:", max(inventory))
print("Min stock:", min(inventory))
print("Total items:", sum(inventory))
if min(inventory) < 5:
    print("Warning: Low stock alert!")

grades_list = [85, 92, 78, 90, 65]
print("Grades:", grades_list)
print("Highest grade:", max(grades_list))
print("Lowest grade:", min(grades_list))
print("Average grade:", sum(grades_list)/len(grades_list))
grades_list.sort()
print("Sorted grades:", grades_list)

print("End of list operations training")