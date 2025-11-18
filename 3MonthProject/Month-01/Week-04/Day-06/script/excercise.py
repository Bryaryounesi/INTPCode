# month-01
# week-04
# Day-06

# 1. خواندن فایل Excel
import pandas as pd
path =r"e:\python\INTPCode\3MonthProject\Month-01\Week-04\Day-06\data\scores.xlsx"
df= pd.read_excel(path)
p=print
p(df)
del path
# 2. پاک‌سازی داده‌ها
# محاسبه درصد داده های خالی 
p(df.isna().sum())
for i in df.columns:
    percent= df[i].isna().sum()/len(df[i])
    p(f"{i} % : {percent}")
# چون درصد داده های خالی کمه از مود یا همان پرتکرارترین آیتم هر ستون
# برای پر کردن مقادیر خالی استفاده می کنیم
dfm= df.fillna(df.mode().iloc[0])
# p(dfm)

# 3. خلاصه‌سازی آماری (groupby, mean, sum) # dfm.groupby()
# جایگزینی محتوای ستون کانتری با مقادیر بهتر برای گروهبندی
countries= ["Germany","India","Romania","Iran","USA","UK","China","Russia","Japan","Iraq","France","UAE","Kurdistan"]
import random
random.seed(1)
countriesall= random.choices(population=countries,k=79)
dfm["country"]=countriesall
# p(dfm)
numcols= dfm.select_dtypes(include="number").columns
# گروهبندی بر اساس ستون کانتری وگرفتن میانگین رند شده ستون های عددی
dfm = dfm.groupby("country",as_index=False)[numcols].mean().round()
p(dfm)

# 4. ترسیم نمودار ساده با Matplotlib
import matplotlib.pyplot as plt
# اگر ستونی را که به عنوان محور ایکس انتخاب می کنیم مرتب نباشد یک نمودار به هم ریخته به ما میده
# پس ما ستون بیولوژی رو ابتدا مرتب می کنیم
dfm.sort_values(by="biology",ignore_index=True,inplace=True)
plt.bar(range(len(dfm["biology"])),dfm["biology"],color="green",edgecolor="black",width=0.7,label="biology")
plt.bar(range(len(dfm["biology"])),dfm["chemistry"],color="yellow",edgecolor="black",width=0.5,label="chemistry")
plt.bar(range(len(dfm["biology"])),dfm["math"],color="grey",edgecolor="black",width=0.2,label="math")
plt.xlabel("age")
plt.ylabel("score")
plt.title("students scores-age chart")
plt.legend(loc="best")
plt.show()
# 5. ذخیره خروجی نهایی در اکسل و نمودار در فایل تصویر
expath=r"e:\python\INTPCode\3MonthProject\Month-01\Week-04\Day-06\data\cleaned&groupedby.xlsx"
'''
with pd.ExcelWriter(expath,mode="a",if_sheet_exists="replace") as writer:
    dfm.to_excel(writer,sheet_name="sh1",index=False)
'''    
# داتافریم در اکسل جدید ذخیره شد 
# plt.savefig(fname="chart.png",dpi=300)

# نمودار هم ذخیره شد 
