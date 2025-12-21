# month-02
# week-03
# Day-05


# 1-ستون دسته‌ای (مثلاً جنسیت، کلاس یا گروه محصول) در داتافریم بساز
import pandas as pd
import numpy as np
import random
random.seed(2)
p=print
np.random.seed(2)
m=np.random.uniform(6,20,500).astype(int).reshape(100,5)
df=pd.DataFrame(m)
df.columns=["math","biology","chemistry","geology","physics"]


gender=random.choices(population=["M","F"],weights=[0.7,0.3],k=len(df))
df["gender"]=gender
# یک ستون دسته ای به نام جندر برای داتافریم ساختیم

id = np.random.choice(range(10000,100000),size=len(df),replace=False).astype(str)
# به جای ساخت یک ستون از اسامی، ستونی از آیدی برای دانش آموزان ساختیم
df["students_id"] = id
# p(df)

# 2-تعداد هر دسته را با df['column'].value_counts() محاسبه کن
p("gender column value count:",df["gender"].value_counts(normalize=True))
p("gender column value count by groupby:",df.groupby(by="gender").size())
# انجام همان کار با تابع df.groupby().size()

# 3-نمودار میله‌ای ساده با Matplotlib از فراوانی داده‌ها رسم کن
import matplotlib.pyplot as plt
a=df["gender"].value_counts()
plt.bar(a.index,a.values,color="green",edgecolor="black")
plt.title("Gender bar chart")
# plt.savefig(fname="bar chart.png",dpi=300)
