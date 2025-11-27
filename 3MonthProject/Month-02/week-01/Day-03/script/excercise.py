# month-02
# week-01
# Day-03

# 1- دو ماتریس 2×2 بساز
import numpy as np
import random
np.random.seed(1)
random.seed(1)
p=print
m1= np.random.randint(-5,25,size=(2,2))
m2= np.random.randint(-8,28,size=(2,2))
# برای ساخت ماتریس ها از یکی از توابع کتابخانه راندوم استفاده می کنیم

# 2- بررسی سازگاری ابعاد قبل از ضرب ماتریس ها
# 3- انجام ضرب ماتریسی
# انجام هر دو مرحله بالا در قالب یک شرط
if m1.shape[1]== m2.shape[0]:
    c=m1@m2
    # c=np.dot(m1,m2)
    p("matrix multiplication:",c)
else:
    p("Two matrix was not matched")    


