print("Lesson: lists")

todo = ["read" , "workout" , "code"]
print(todo)

line = "--------------------------------"
print(line)

todo = []
print(todo)

print("--------------------------------")

active_users = ["fine"]
print("active:")
print(active_users)

print("--------------------------------")
characters = ["mario" , "luigi" , "bowser" , "peach" ]
print(characters)

print("--------------------------------")
temperature = [ 20 , 16 , 12 , 30 , 19]
print(temperature)


print("--------------------------------")

print(temperature [1])
temperature [2] = 5
print(temperature)

print("--------------------------------")
top_speads = [100 , 120 , 200 , 240]
print(top_speads [3])
top_speads [3] = 250
print(top_speads)


print("--------------------------------")

users = ["jeremy" , "adam" , "Liza"]
users.append("sara")
print(users)
print("--------------------------------")

users.insert(2 , "Erik") 
print(users)

print("--------------------------------")
fruits = ["apple" , "orange" , "banana"] 
fruits.insert(1 , "coconut") 
print(fruits)
fruits.append("watermelon")
print(fruits)
fruits[2] = "ananas"
print(fruits)

print("--------------------------------")
fruits.pop()
print(fruits)
fruits.pop(2)
print(fruits)
print("--------------------------------")
remove = fruits.pop(2)
print(remove)

print("--------------------------------")
first = "John"
second = "Joseph"
third = "Donnie"
winners = [first, second, third]

print(winners[2])
print("--------------------------------")
flavors = ["vanilla" , "chocolate" , "pistachio"]
flavors [2] = "strawberry"
print(flavors)
print("--------------------------------")
quiz_answer = [False , False , True , False]
quiz_answer.pop()
print(quiz_answer)

print("--------------------------------")
list = [1, 2 , 3 , 4 , 6 , 8 , 10 ]
for i in list :
     print (i)
print("--------------------------------") 
artists = ["chagall" , "lissitzky"]
for artist in artists :
    print(artist)
    print("---------")
print("--------------------------------") 
 
items = ["milk" , "tomato" , "apple"]
for item in items:
     print(item)
     print("-------")
print("--------------------------------")
suplies = ["pencil" , "book"] 
for value in suplies :
    print(value)
    
print("--------------------------------") 
data_points = [99 , 99 , 99 , 99 , 99]  
for data in data_points :
    print(data + 1)   
print("--------------------------------") 
minutes_worked = [123, 100, 99, 67]

for minutes in minutes_worked:
  print(minutes - 60)    
print("--------------------------------")  
print(len(data_points))
print("--------------------------------")  
if len(data_points) > 2 :
    print("very good")
print("--------------------------------")  
ingredients = ["cafee" , "lemon" , "cream" ]    
if len(ingredients) > 2 :
    print("bring a bag")  
print("--------------------------------") 
update_version = [1.2 , 3.5 , 2] 
for version in update_version : 
    print(version + 1) 
print("--------------------------------") 
sodas = ["fanta" , "cocacola" + "pepsi"]  
if len(sodas) >= 2 :
    print("to much soda") 
print("--------------------------------") 
condidates = ["mishaeel"]  
condidates_number = len(condidates)   
if condidates_number < 2 :
    print("one condidate needs opposition ")  
print("--------------------------------")
meals = ["omelet" , "salad" , "chicken"]
print(f"breakfast menu: {meals[0]}")
print(f"Lunch menu: {meals[1]}")
meals[2] = "pizza"
print(f"Dinner menu: {meals[2]}")
print("--------------buying list------------------") 

shopping_list = ["dish soap", "kleenex", "batteries", "aluminum foil", "pet food", "toothpaste", "lightbulbs"]

for shopping in shopping_list:
 print(f"Don't forget to buy {shopping}")