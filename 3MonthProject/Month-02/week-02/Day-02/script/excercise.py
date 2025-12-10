# month-02
# week-02
# Day-02

# 1-  روی دو array مختلف جمع/ضرب/تقسیم انجام بده

import numpy as np
import random
np.random.seed(2)
random.seed(2)
p=print
v1=np.linspace(-7,9,5,dtype=int)
v2=random.choices(population=range(-7,9),k=5)
p("Array Addition:",v1+v2)
p("Array substraction:",v1-v2)
p("Array multiplication:",v1*v2)
p("Array divition:",v1/v2)


# 2- برای یک لیست 20تایی sqrt و log را حساب کن
L20= np.linspace(1,40,20,dtype=int)
L20_sqrt=np.sqrt(L20).round(2)
p("L20 list sqrt:",L20_sqrt)
# جذر لیست را حساب و پرینت کردیم

L20_log=np.log(L20).round(2)
p("L20 list logaritm:",L20_log)

# 3- یک تابع ریاضی y = x² + 3x روی بازه 0–50 بساز
# منظور از این تمرین آخر اینه که یک رنج ساخته بشه
# رنجی که در واقع یک آرایه است 
# و سپس این رنج به جای ایکس قرار بگیره تا رنجی از ایگریک به ما بده

x= np.arange(0,51)
# p(x)
# متغیر ایکس که خود یک بازه است ساخته شد
y=x**2 + 3*x
# متغیر ایگریک از روی ایکس ساخته شد 
# p(y)

