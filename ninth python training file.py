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


    



    
      


