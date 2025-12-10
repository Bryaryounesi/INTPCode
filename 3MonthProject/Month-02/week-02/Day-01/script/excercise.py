# month-02
# week-02
# Day-01

# 1- پنج نوع array مختلف بساز
import numpy as np
p=print

# with np.array()
data= [5,3,9,-2]
v= np.array(data)
m=np.array([data,data])

# with np.zeros()
v1=np.zeros(5)
m1= np.zeros((4,4),dtype=int)

# with np.ones()
v2= np.ones(6,dtype=int)
m2=np.ones((4,4))

# with np.arange
v3= np.arange(6)
m3=np.arange(15).reshape(3,5)

# with np.linspace
v4= np.linspace(2,9,num=4).round(2)
m4=np.linspace(3,10,num=12).round(2).reshape(3,4)

# 2- با np.arange چند بازه مختلف ایجاد کن
r1= np.arange(6)
# بازه از صفر تا 5 
r2=np.arange(2,10)
# بازه از 2 تا 9 
r3=np.arange(3,10,step=3)
# بازه از 3 تا 9 با گام حرکتی 3 تایی

# 3-یک بردار 10 تایی با linspace تولید و بررسی کن
v10= np.linspace(4,11,num = 10,dtype=int)
# p(v10)