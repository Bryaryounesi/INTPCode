print("lesson: list operations")
print("----------------------------")
list = [12 , 6 , 5 , 2 , 7]
print(max(list))
print(min(list))
print("----------------------------")
max_list = max(list)
min_list = min(list)
print(max_list + min_list)

print("----------------------------")
weekly_profits = [20 , 59 , 43 , 76 , 24 , 60]
max_profit = max(weekly_profits)
print(f"max profit :{max_profit} usd")

print("----------------------------")
for profit in weekly_profits:
     print(f"{weekly_profits[2]}, {profit} , {profit}")
     
print("----------------------------")  
scores = [10 , 9.25 , 8 , 4.5 , 17 , 11.75] 
scores.sort() 
print(scores)
print("----------------------------")  
tempreture = [ 10 , 4 , -1 , 7 , -5 , 16 , 0]
tempreture.sort()
print(tempreture)

print("----------------------------")  
names = ["cloe" , "bill" , "ana"]
names.sort()
print(names)
print("----------------------------")  
signups = [12 , 30 , 40 , 10 , 4 , 8 ]
print(sum(signups))
sumation = sum(signups)
print(sumation)
print("----------------------------")  
cordinates = [0 ,0 ,0]
print(min(cordinates))
print("----------------------------")  
oxygen_level = [19.99, 21.2, 20.85]
oxygen_level.sort()
print("----------------------------")
grades = ["A" , "C" , "F" , "B" , "G"]
grades.sort()
print(grades)
print("----------------------------") 
database_1 = [1 , 2 , 3]
database_2 = [4 , 5]
print(database_1 + database_2)

print("----------------------------")
seats = [1 , 2 , 3]
taken = [True , True , False]
print(seats + taken)

print("----------------------------")
combine = database_1 + database_2
print(combine)

print("----------------------------")
consumers = ["jess" , "mike" , "lyne"]
order_numbers = [3 , 2 , 1]
print(consumers + order_numbers)

print("----------------------------")
team_1 = ["ana" , 78 , "kim" , 25 , "rose" , 40]
team_2 = ["jerry" , 24 , "henry" , 28]
print(team_1 + team_2)

print("----------------------------")
answers = ["yes" , "no" , "sometimes" , "yes" , "no"]
print(answers.count("yes"))
  
print("----------------------------") 
free_seats = [True , False , True , True , False ]
print(free_seats.count(True))

print("----------------------------")
seats_count = free_seats.count(True)
print(seats_count)

print("----------------------------")
ingredients = ["milk" ,"suger" , "eggs",  "flour" ,"butter" ]
print("suger" in ingredients)
print("----------------------------")
has_suger = "suger" in ingredients 
print(has_suger)
print("----------------------------")
missions = ["mars" , "moon" , "mars" , "ISS"]
print(missions.count("mars"))
print("----------------------------")
flavors = ["vanilla", "chocolate", "strawberry", "vanilla", "vanilla"]
print(flavors.count("vanilla"))

print("----------------------------")
winning_numbers = [2, 36, 40, 13] 

print(13 in winning_numbers)
print(20 in winning_numbers)
has_21 = 21 in winning_numbers
print(has_21)
print("----------------------------")
students_1 = ["Anna", 16, "Kim", 16]
students_2 = ["Joe", 17, "Lee", 15]

print(students_1 + students_2)   
print("----------------------------")
customers = ["Jess", "Mike", "Lynn"]
order_number = [3, 1, 2]
orders = customers + order_number
print(orders)
print("----------------------------")
day_1 = [3.5 , 2 , 4]
day_2 = [1, 2]
overview = day_1 + day_2
print(overview)
print("----------------------------")
code = [0 , 3 , 2 , 0 , 1 , 0]
print(code.count(0))

print("----------------------------")
flavors = ["vanilla", "chocolate", "strawberry", "vanilla", "vanilla"]
print(flavors.count("vanilla"))

print("----------------------------")
schedule = ["ballet", "swimming", "running", "ballet"]
print("ballet" in schedule)
print("running" in schedule)
print("going" in schedule)

print("----------------------------")
customers = ["Jess", "Mike", "Lynn"]
order_numbers = [3, 1, 2]
orders =  customers + order_numbers 
print(orders)

print("----------------------------")