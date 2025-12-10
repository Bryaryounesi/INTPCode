# month-02
# week-02
# Day-04

# 1-یک نمودار خطی از y = x² رسم کن
from matplotlib.lines import lineStyles
import numpy as np
import matplotlib.pyplot as plt
p=print
x= np.linspace(-10,20,15,dtype=int)
# p(x)
y=x**2
# p(y)

plt.plot(x,y,color="black",marker="*",linestyle="--")

# 2-عنوان، xlabel، ylabel اضافه کن
plt.xlabel("X")
plt.ylabel("Y")
plt.title("y=x^2 chart")
# plt.show()

# 3- نمودار را ذخیره کن (مثلاً plot1.png)
plt.savefig(fname="chart.png",dpi=300)


