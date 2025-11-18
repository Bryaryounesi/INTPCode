# month-01
# week-03
# Day-06

# ۱- دو فایل Excel بخوان (مثلاً اطلاعات پایه و نمرات)
import pandas as pd
p= print
path1 = r"e:\python\INTPCode\3MonthProject\Month-01\Week-03\Day-06\data\students_base_info.xlsx"
path2=r"e:\python\INTPCode\3MonthProject\Month-01\Week-03\Day-06\data\students_scores.xlsx"
df1 = pd.read_excel(path1)
df2= pd.read_excel(path2)

# 2- آنها را با merge ترکیب کن
dfm = pd.merge(df1,df2,how="outer",on="user_id")
# از ستون یوزرآیدی برای مرج استفاده کردیم که در هر دو داتافریم وجود دارد و مقادیری یونیک دارد
# در غیر این صورت مرج سبب تکثیر غیر منطقی ردیف ها و مقادیر خالی می شود
# p(dfm)
# داده‌های گمشده را پیدا کن و پر کن
p(dfm.isna().sum())
# پرکردن به روش سمپل گیری از هر ستون و جایگزینی سمپل ها با مقادیر گمشده 

for i in dfm.columns:
    cleaned= dfm[i].dropna(ignore_index=True)
    sampled = cleaned.sample(n=dfm[i].isna().sum(),replace = True, random_state=1)
    dfm.loc[dfm[i].isna(),i] = sampled.values
p(dfm)

# 3- خروجی نهایی را در فایل Excel جدید ذخیره کن 
expath=r"e:\python\INTPCode\3MonthProject\Month-01\Week-03\Day-06\data\merged.xlsx"

'''
with pd.ExcelWriter(expath,mode="a",if_sheet_exists= "replace") as writer:
    dfm.to_excel(writer,sheet_name="sh1",index=False)
'''       
df3 = pd.read_excel(expath,sheet_name="sh1") 
p(df3)  

# 4- بعد از ذخیره، بررسی کن که فایل نهایی کامل و بدون NaN باشد
p(df3.isna().sum())
# فایل نهایی کامل و بدون مقادیر خالی است 

# متاسفانه در فایل اکسل نهایی، کل ستون ها ایندکس هستند درنتیجه این داتافریم برای استفاده بعدی قابل استفاده نیست



