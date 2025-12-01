# month-02
# week-01
# Day-05

# 1-یک دستگاه دو معادله و دو مجهول تعریف کن
import numpy as np
import random
p=print
np.random.seed(4)
a=np.random.randint(-7,8,size=(2,2))
# ماتریس ضرایب را با کتابخانه راندوم ساختیم
b=random.choices(population=range(-5,9),k=2)
# بردار باقی مانده های دستگاه نیز ساخته شد

# 2- با np.linalg.solve() حلش کن
a_det=np.linalg.det(a)
# p(a_det)
# از روی دترمینان درمیابیم که ماتریس منفرد نیست و معکوس دارد
# یعنی دترمینان صفر نیست 
# تعداد مجهول ها هم با تعداد معادلات مساوی است
# پس می شود با solve دستگاه را حل کرد

x= np.linalg.solve(a,b)
p(x)
# نتیجه را بررسی کن
# ماتریس به صورت موفقیت آمیزی حل شد