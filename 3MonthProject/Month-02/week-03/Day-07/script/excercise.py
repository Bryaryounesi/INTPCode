# month-02
# week-03
# Day-07

# 1. یک دیتاست کوچک بساز یا دانلود کن (مثلاً نمرات دانش‌آموزان + جنسیت + کلاس)
from matplotlib import axes
import numpy as np
import random
random.seed(2)
np.random.seed(2)
p=print

m=np.random.choice(range(6,19),size=500,replace=True).reshape(100,5)
# p(m)
# یک ماتریس ساختیم
import pandas as pd
df=pd.DataFrame(m)
df.columns=["math","biology","geology","chemistry","ecology"]
# ماتریس رو به داتافریم تبدیل و نام ستون ها رو درج کردیم

gender=np.random.choice(["M","L"],size=len(df),replace=True)
df["gender"]=gender
classo = random.choices(population=["A","B","C"],k=len(df),weights=[0.5,0.3,0.2])
df["class"] =classo
# دو ستون دسته ای به داتافریم اضافه کردیم

# 2. میانگین، واریانس، انحراف معیار هر ستون عددی را محاسبه کن
numcols=df.select_dtypes(include="number")
p(numcols.describe().round())
# میانگین و انحراف معیار در دسکرایب هست پس از آن استفاده شد
p("numcols variance:",numcols.var().round())

# 3. تعداد هر دسته را با value_counts() محاسبه کن
p("gender column value counts:",df["gender"].value_counts())
p("class column value counts:",df["class"].value_counts())

# 4. نمودار هیستوگرام و میله‌ای رسم کن
import matplotlib.pyplot as plt

fig1,axs1=plt.subplots(2,1,figsize=None)
df["gender"].value_counts().plot(kind="bar",ax=axs1[0],title=" Students Gender Bar Chart",color="green",edgecolor="black")
# اکس یک بعدی است پس به صورت یک عدد درون کروشه می آید مثلا
# ax=axs1[1] یا ax=axs[0] 
# ax=axs[1,0] اشتباه است

df["class"].value_counts().plot(kind="bar",ax=axs1[1],title="Students Class Bar Chart",color="grey",edgecolor="black")
plt.tight_layout()
# برای داده های دسته ای نمودار میله ای رسم کردیم 

fig1.savefig(fname="Value_counts bar Cahrt.png",dpi=300)

p("-------------------------------------")
fig2 ,axs2=plt.subplots(2,2,figsize=(12,10),constrained_layout=True)
#>> پارامتر constrained_layout=True  بهتر از  تابع plt.tight_layout عمل می کند 

df["math"].plot(kind="hist",ax=axs2[0,0],color="grey",edgecolor="black",label=True,title="math Hist")

df["chemistry"].plot(kind="hist",color="green",edgecolor="black",label=True,title="Chemistry Hist",ax=axs2[0,1])

df["ecology"].plot(kind="hist",color="brown",edgecolor="black",label=True,title="Ecology Hist",ax=axs2[1,0])

df["biology"].plot(kind="hist",color="pink",edgecolor="black",label=True,title="Biology Hist",ax=axs2[1,1])
# برای ستون های عددی هیستوگرام رسم شد

fig2.savefig(fname="Students Scores Histograms.png",dpi=300)
plt.show()

# 5. خلاصه تحلیلی از داده‌ها بنویس
'''
از آنجایی که داده ها با تابع راندوم چویز نامپی تولید شده اند 
تا حد زیادی شبیه توزیع نرمال هستند پس اغلب حول میانگین خود هستند
و چندان داده پرت و نویز قابل توجهی ندارند
پس نیاز به تحلیل نیست و از قبل معلوم است چه وضعیتی دارند
'''