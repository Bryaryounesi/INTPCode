# month-02
# week-02
# Day-07

# 1. با np.random یک دیتاست بساز
import numpy as np 
np.random.seed(1)
import pandas as pd
p=print
m=np.random.choice(range(-10,60),size=80)
mr=m.reshape(20,4)
df=pd.DataFrame(mr)
# p(df)

# 2. میانگین، واریانس، max/min محاسبه کن
p("datafram colomns min:")
p(df.min())
p("datafram columns max:")
p(df.max())
p("datafram columns mean:")
p(df.mean())
p("datafram columns variance:")
p(df.var().round())

# 3. یک هیستوگرام از داده‌ها رسم کن
import matplotlib.pyplot as plt
fig1,axs1=plt.subplots(2,1,constrained_layout=True)
axs1[0].hist(m,color="green",edgecolor="black")
axs1[0].set_title("Random Dataset histogram")
axs1[0].set_xlabel("digits")
axs1[0].set_ylabel("Frequency")

# 4. یک scatter از (داده، sqrt(داده)) 
m_sqrt_abs=np.sqrt(np.abs(m))
axs1[1].scatter(m,m_sqrt_abs,color="blue")
axs1[1].set_title("Random Dataset scatter")
axs1[1].set_xlabel("original data")
axs1[1].set_ylabel("square root of data")
# fig1.savefig(fname="fig1.png",dpi=300)

# 5. سه نمودار خطی مختلف ایجاد کن
fig2,axs2=plt.subplots()
df.iloc[::4,:3].plot(ax=axs2,label=True,title="Line Charts",xlabel=" Columns Original data",ylabel="Frequency")
fig2.savefig(fname="Line Charts fig.png",dpi=300)

# plt.show()
# به دلیل نوسان بیش از حد داده ها 
# هر 4 ردیف را در رسم نمودار میله ای
# با گذاشتن استپ برای ردیف ها یکی کردیم 

# 6. نتایج را جمع‌بندی کن
# از روی هیستوگرام میفهمیم که داده ها بیشتر مثبت هستند
# پس توزیع کاملا یکنواخت نیست و به سمت مثبت گرایش دارد
# از روی نمودارهای خطی نیز متوجه پراکندگی و نوسان بیش از حد داده ها میشویم

