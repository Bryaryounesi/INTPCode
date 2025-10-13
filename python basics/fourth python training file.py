print("fourth python training file")
print("subject: Other statments")

available = True
if available :
    print("In stock")
if not available :
    print("out of stock")
    
available = False
if not available :
    print("out of stock")
    
available = False
if available :
    print("that's here")
else :
        print("anybody not here")
        
is_day = True
if is_day :
    print("lights off")
else : 
    print("lights on")    

is_subscribed = True
if is_subscribed :
    print("injoy 10% off")
else :
    print("become a subscriber")
    
choosen_number = 7
if choosen_number == 12 :
    print("your gussed right")
else  : 
    print("choice another number")
    
common_friends = 3
if common_friends > 2 :
    print("friend suggestion: sure")
else : 
    print("no friend suggestion")
    
membership = "gold"
if membership == "gold":
  print("Add to dataset 1")
else:
  print("Add to dataset 2")
  
points = 7600
points_needed = 8000
if points >= points_needed:
  print("You're Level 2!")
else:
  left = points_needed - points
  print("Points till Level 2:")
  print(left)
  
do_countdown = True
wait = False
if wait :
  print("3")
  print("2")
  print("1")
else:
    print("just a moment...")
    
paid = not True
if paid:
  print("Thank you for your purchase")
else: 
    print("Your not paid")
    
score = 100
if score > 50:
  print("new highest score!")
  
  subject = "math"
  grade  = "A"
  if grade != "A" :
      print(f"give{subject} a chance")
if subject == "math":
    print("let's go to solving")
    
carbon_level = 200
if carbon_level < 300 :
    print(f"{carbon_level} ppm is not enough carbon for photosynthesis")   

character = "wizard"
power = "potions" 
if character == "wizard" :
    print(f"special power is {power}") 
    
print("corporative_elif")

hour = 13
if hour < 12 :
  print("good morning")
elif hour < 17 :
    print("good afternoon") 
elif hour < 19 :
    print("good evening")    
else :
    print("good night")
    
score = 61
if score > 80 : 
    print("your grade is A")
elif score > 60 :
    print("your grade is B")
elif score > 50 :
    print("your grade is c")
else :
    print("your grade is D")
 
age = 50
if age < 18 :
     print("you'r too young for driving")
elif age < 60 :
     print("you can driving")
else :
     print("you'r too old for driving") 
     
age = 32
permission = True
if age >= 18 and permission :
    print("you can drive")
else :
    print("you can't drive")
    
average_grade = "A"
final_score = "1400"
won_complication = True
if average_grade == "B" or final_score >= "1500" or won_complication :
    print("certification achieved")
    
is_summer = False
is_warm = True
if is_summer or is_warm :
    print("go to a swim")
    	
is_vacation = True
is_weekend = False
if is_vacation or is_weekend :
    print("go to roadtrip") 
    
mobile_internet = True
wifi = False
if mobile_internet or wifi :
  print("loading...")
 
promote_article = False
likes = 40
shares = 50
comments = 70
if likes > 50 or shares >= 80 or comments >= 70 :
    promote_article = True
  
language = "english"
message = ""
 
if language  == "english" :
     message = "thank you"
elif language == "german" :
    message = "Tanke"
elif language == "spanish" :
     message = "gracias"
print(message)   

read = False
time_elapse = 50
if read or time_elapse > 40 :
    print("can't delete the message") 
    
number_pressed = 2
message = ""  
if number_pressed == 1 :
    print("to hear store hourse")
elif number_pressed == 2 :
    print("to call to manager")
elif number_pressed == 3 :
    print("to record a message")
elif number_pressed == 4 :
    print("to hear again")
else :
    print("invalid option")    
response = "maybe"    
if response == "yes" :
    print("you picked yes")
elif response == "no" :
    print("you picked no")
else :
    print("you must pick yes or no")   
    
direction = "left"
if direction == "left" :
    print("turn left")
elif direction == "u_turn" :
    print("u_turn")
elif direction == "right" :
    print("turn right")
else :
    print("go straight") 
       
volume = 40
if volume < 20 :
    print("i dont hear that")
elif volume >= 70 :
    print("its a little loud")
else :
     print("perfect level")   

caffeine = True
time = "night" 
if caffeine and time == "night" :
    print("awake all night")  
else :
    print("good night's sleep") 

read = 5
unread = 7
if unread != 0 :
    print(f"you have {unread} unread messages ")
else :
    print(f"you have no unread massage, review {read} read message")  

age = 21
hasReservation = True
result = False
if age >= 18 and hasReservation:
 result = True

print(f"Entry granted: {result}")