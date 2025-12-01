# month-02
# week-01
# Day-06

# 1- ساخت چند ماتریس مختلف
import numpy as np
import random
np.random.seed(1)
random.seed(1)
p=print
m1=np.random.randint(-7,9,size=(3,3))
m2=np.random.randint(-7,9,size=(3,3))
# p(m1)
# p(m2)

# 2- جمع، تفریق، ضرب ماتریسی
p("Matrix Addition:",m1+m2)
p("Matrix Subtraction:",m1-m2)
p("Matrix Multiplication:",m1@m2)

# 3- محاسبه دترمینان و معکوس
m1_det= np.linalg.det(m1)
m1_inv=np.linalg.inv(m1)

m2_det=np.linalg.det(m2)
m2_inv=np.linalg.inv(m2)

# 4- حل یک دستگاه ۳ معادله ۳ مجهول
b1=random.choices(population=range(-7,9),k=3)
b2=random.choices(population=range(-7,9),k=3)
# ساخت بردار باقی مانده ها برای هر دو ماتریس با راندوم 
m1_solve= np.linalg.solve(m1,b1).round(3)
m2_solve= np.linalg.solve(m2,b2)
# هر دو دستگاه معادلات را حل کردیم 

p("m1 solve:",m1_solve)
p("m2 solve:",m2_solve)

# 5- بررسی کن کدام ماتریس‌ها معکوس‌ پذیر هستند

# در بخش سوال سوم بررسی شد و معلوم شد که هر دو معکوس دارند