print("hello world")
name = "hasan"
print(type(name))
number = 35
print(type(number))
sum = 18.26
print(type(sum))
alive  = True
print(type(alive))

age = "18"
print(type(age))
age_convered = int(age)
print(age_convered)
print(type(age_convered))
print(age_convered <= 18)

price = 12.3
price_converted = int(price)
print(price_converted)
print(int(price))

week = 12
print(float(week))

member = True
not_member = False
value = int(member)
second_value = int(not_member)
print(value)
print(second_value)
print(int(member))
print(int(not_member))

member_name = "sam"
middle_name = "" 
sibling = 0 
foot_size = 8.5
print(bool(member_name))
print(bool(sibling))
print(bool(foot_size))
print(bool(middle_name))

detail = "i love you"
response = bool(detail)
print(response)

print(f"{12} new masage")
print("comment_number:" + "12")
print(12+5)
print(f"{13} comments")
print(f"{23} new message")
print(f"{4+3} new message and {50} comments")
apple = 40
orange = 36
print(f"{apple*orange} new message and {24} comments")

new = 51
status = f"{new} new massage"
print(status)

print(f"I would walk  {500}  miles")
price = 40
print(f"glasses price: {price} dollar")

vehicle = "airplane"
vehicle = "train"
vehicle = "bus"
event = "movie"
ticket_price = 50
currency = "dollar"
currency = "euro"
print(f"{vehicle} ticket price: {ticket_price} {currency}")
print(f"{event} ticket price: {ticket_price} {currency}")
ticket_price = 30
print(f"{event} ticket price: {ticket_price} {currency}")


author= "agatha christi"
description = f"a book by {author}"
print(description)

age = 15
legal_age = age >= 18
print(age >= legal_age)
if legal_age :
    print("welcom")

charge = 30
low_charge = charge <= 20
print(low_charge)
if low_charge : 
    print("battery is low")
