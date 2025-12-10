# month-02
# week-02
# Day-06

# هرکدام از موارد زیر را روی نمودار جداگانه رسم کن
import numpy as np
import matplotlib.pyplot as plt
p=print
x= np.linspace(-20,40,15,dtype=int)
# ساخت یک رنج از ایکس برای رسم همه نمودارها

y1 = x
plt.figure()
plt.xlabel("X")
plt.ylabel("y")
plt.title("y1=x Line Chart")
plt.plot(x,y1)
plt.show()

y2 = x**2
plt.figure()
plt.xlabel("X")
plt.ylabel("y")
plt.title("y2=x^2 Parabolic Chart")
plt.plot(x,y2)
plt.show()

y3 = np.sqrt(np.abs(x))
# چون رنج ایکس مقادیر منفی داشت برای تابع جذر ارور میداد
# پس از این رنج، قدر مطلق گرفتیم با تابع abs 
plt.figure()
plt.xlabel("X")
plt.ylabel("y")
plt.title("y3=sqrt(x) Square Root plot")
plt.plot(x,y3)
plt.show()

# میانگین، انحراف معیار y2 را حساب و گزارش کن
p("y2 mean:",np.mean(y2).round(3))
p("y2 std:",np.std(y2).round(3))
# اعشار میانگین و انحراف معیار، طولانی بودند پس آنها را رُند کردیم