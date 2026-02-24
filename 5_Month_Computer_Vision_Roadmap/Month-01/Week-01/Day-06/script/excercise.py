# Month-01
# Week-01
# Day-06

# 1-دو ماتریس هم‌اندازه بساز
import numpy as np
p=print
np.random.seed(3)
m1=np.random.randint(-17,37,(5,6))
m2=np.random.randint(-15,45,(5,6))

# 2-جمع و ضرب ماتریسی آن‌ها را انجام بده
p("matrix_addition: ")
p(m1+m2)

p("matrix_multiplication: ")
m2= m2.reshape(6,5) #ماتریس دوم رو ریشیپ کردیم تا با ارور مواجه نشویم
multiplication= np.dot(m1,m2)
p(multiplication)

# 3-خروجی را توضیح بده
'''جمع دو ماتریس به صورت عنصر به عنصر انجام شده
ولی ضرب دو ماتریس به صورت عنصر به عنصر نیست و یک ضرب ماتریسی است 
که از فرمول ضرب ماتریسی پیروی میکند '''