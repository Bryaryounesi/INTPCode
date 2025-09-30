print("lesson name : string operations")
new_users = "Ann Jon Alex"
users_list = new_users.split()
print(users_list)
print(new_users.split())

print("-------------------------")
words = "gear fault lights build-up"

word_list = words.split(" ")
print(word_list)

print("-------------------------")
user = "Lauren_25 F Architect"
print(user.split("_"))

print("-------------------------")
numbers = "1 2 3 35 56 27 75 21 56 78 24"
list = numbers.split()
print(list)
list.sort()
print(list)
print("-------------------------")
sales = "24K 29K 7K"
sales_list = sales.split()
print(sales_list)
print("-------------------------")
polution = "40ppm 55ppm 60ppm"
polution_list = polution.split()
print(polution_list)

print("-------------------------")
path = "getmimo.com/glossary/python"
path_list = path.split("/")
print(path_list)

print("-------------------------")
levels = ["c" , "b" , "a" , "g"]
codes = "2 3 9 0"
levels.sort()
print(levels)

codes_list = codes.split()
print(codes_list)
codes_list.sort()
print(codes_list)
 
print("-------------------------")
special = "today's special is pizza" 
new_special = special.replace("pizza" , "pasta")
print(new_special)
special = special.replace("pizza" , "spaghetti")
print(special)

print("-------------------------")
sport = "todays sport is football"
sport= sport.replace("footbal" , "ping pong")
print(sport)
print("-------------------------")
june = "June sales target updated. Let's rock June!"
july = june.replace("June", "July")
print(july)
print("-------------------------")
news = "israeel military force in ghaza"
report = news.replace("israeel" , "usa")
print(report)
print("---------------------")
age_group = "twenty-five to thirty"

updated = age_group.replace("thirty","thirty-five")

print(updated)
print("---------------------")
age ="forty five to fifty"
update_age = age.replace("five" , "two")
print(update_age)
print("-------------------------")
monthly = "Monthly reduction is 25%"

monthly = monthly.replace("25%","15%")

print(monthly)
print("-------------------------")
off = "weakly off is 23 %"
update_off = off.replace("23" , "30")
print(update_off)

print("-------------------------")
release_date = "relrase date : 24th september"
update = release_date.replace("24th september" , "16th november")
print(update)
print("-------------------------")
welcome = "welcome to the company"
print(welcome.replace("the" , "our"))
print("-------------------------")
tech_stack = "angular node mongo express"
tech_stack = tech_stack.replace("angular" , "react")
tech_stack_list = tech_stack.split()
print(tech_stack_list)
print("-------------------------")
old_top_movies = "the power of the dog - trapped - tenet"
new_top_movies = old_top_movies.replace("trapped" , "moonfall")
print(new_top_movies)


