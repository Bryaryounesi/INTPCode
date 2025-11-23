# month-02
# week-01
# Day-01

import numpy as np
# 1- ساخت یک بردار با np.array
p=print
num=[4,-2,3]
v=np.array(num)
# 2- انجام جمع، تفریق و ضرب عددی
p("v:",v)
p("v*2:",v*4)
p("v+4:", v+4)
p("v-3:",v-3)
# 3- طول بردار (np.linalg.norm)
length= np.linalg.norm(v).round(2)
# طول بردار اعشاری بود و با 
# تابع راند آن را تا دو رقم اعشار رند کردیم
p(length)