# month-01
# week-04
# Day-04

# 1- یک لیست ساده بساز و نمودار خطی و ستونی رسم کن
data1 = [i for i in range(80)]
import random
random.seed(1)
p= print
data2= random.choices(data1,k=15)
# p(data2)
# لیست ساده ساخته شد به کمک کتابخانه راندوم 
import matplotlib.pyplot as plt

# ساخت نمودار خطی 
plt.plot(data2,marker="*",color="black",linestyle="--",label="data2 scores")

# ساخت نمودار میله ای 
# نمودار میله ای نیاز به یک محور ایکس جداگانه دارد
x= range(len(data2))
plt.bar(x,data2,color="lightgreen",edgecolor="black",width=0.2)
plt.xlabel("indexes")
plt.ylabel("data2 list elements")
plt.title("data2 chart")
plt.legend(loc="best")

# 2- نمایش نمودار با plt.show()
plt.show()
