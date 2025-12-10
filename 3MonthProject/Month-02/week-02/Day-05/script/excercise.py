# month-02
# week-02
# Day-05

# 1- از یک array تصادفی 500تایی یک هیستوگرام بساز
import numpy as np
import random
random.seed(1)
p=print
a=random.choices(population=range(-50,300),k=500)
# یک لیست 500 والیویی ساخته شد
a.sort()
# لیست به صورت صعودی مرتب شد
A= np.array(a)
# لیست مرتب شده به آرایه تبدیل شد

import matplotlib.pyplot as plt
plt.subplot(2,1,1)
# تابع ساب پلات را اگر در ابتدای هر نمودار درج کنیم
# نمودارها را به صورت مجزا ولی در یک صفحه رسم میکند
plt.hist(A,edgecolor="black",color="green",bins=30)
plt.title("A array chart")
plt.xlabel("x")
plt.ylabel("y")

# 2- یک scatter از دو array تصادفی X,Y رسم کن
plt.subplot(2,1,2)
X= np.linspace(-10,13,10,dtype=int)
Y=np.linspace(-10,15,10,dtype=int)
plt.scatter(X,Y,color="black")
plt.title("X and Y array chart")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
# تابع تای لایوت در پایان و بعد از همه ساب پلات ها درج میشود
# تا مانع تداخل اجزای نمودارها با هم شده و بین آنها فاصله بدهد
plt.show()
# 3- رابطه داده‌ها را بررسی کن (پراکنده؟ خطی؟ تصادفی؟)

# رابطه داده های بین دو آرایه ایکس و ایگریک از نوع خطی است
# چون نقطه ها تقریبا روی یک خط صعودی، ردیف شده اند