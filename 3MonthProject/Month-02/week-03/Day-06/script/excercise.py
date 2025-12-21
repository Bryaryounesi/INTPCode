# month-02
# week-03
# Day-06

# 1-از یک دیتاست واقعی یا مصنوعی استفاده کن
import pandas as pd
p=print
path=r"e:\python\INTPCode\3MonthProject\Month-02\week-03\Day-06\Data\student_data_m1_w4_d3_share.XLSX"
df=pd.read_excel(path)
# از یک داتافریم ماه اولِ پروژه سه ماهه استفاده کردیم
# p(df.columns)

del df["names"]
del df["job"]
del df["age"]
# ستون نام ها و ستون شغل رو حذف کردیم چون نیازی به آن نداریم


# 2-محاسبه میانگین، واریانس، انحراف معیار
numcols=df.select_dtypes(include="number")
# p(numcols)
# ستون های عددی را از بقیه جدا کردیم

p("df numberic columns means:",numcols.mean().round(2))
p("df numberic columns variance:",numcols.var().round(2))
p("df numberic columns std:",numcols.std().round(2))
p("---------------------------------")

# 3-بررسی توزیع مقادیر عددی و دسته‌ای
p("df info:",df.info())
p("df null number:",df.isna().sum())
unnumcols= df.select_dtypes(include="object")
# ستون های مشکوک به دسته ای را تشخیص دادیم

p("gender unique number per 100 rows:",df["gender"].nunique())
p("contry unique number per 100 rows:",df["country"].nunique())
# تایید دسته ای بودن دو ستون جندر و کانتری به دلیل مقادیر کم یونیک

p(df["gender"].value_counts())
p(df["country"].value_counts(normalize=True).round(2))
# بررسی تعداد و نسبت دسته ها در ستون های دسته ای 
# یکی بر حسب درصد و یکی دیگر تنها تعداد 
# بررسی توزیع ستون های دسته ای کامل شد
p("-------------------------------")
numcols = df.select_dtypes(include="number")
p(numcols.describe().round(2)) 
p("numcols meidan:",numcols.median())
p("numcols skewness:",numcols.skew())
#بررسی توزیع ستون های عددی نیز با تابع های مربوطه انجام شد

# 4- رسم هیستوگرام برای یک ستون عددی

import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(2,1,1)
numcols.iloc[:,1].plot(kind="hist",color="green",edgecolor="black",legend=True,title="math histogram chart")

# 5-رسم نمودار میله‌ای برای یک ستون دسته‌ای
plt.subplot(2,1,2)
df["country"].value_counts().plot(kind="bar",color="blue",edgecolor="black",title="county bar chart",label=True)
plt.ylabel("Frequency")
plt.tight_layout()
# plt.savefig(fname="Descriptive Data Analysis",dpi=300)
plt.show()