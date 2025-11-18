# month-01
# week-01
# Day-04

# 1-  مرور داده ها 
import pandas as pd
path= r"e:\python\INTPCode\3MonthProject\Month-01\data\student1.csv"
p=print
df= pd.read_csv(path)
p(df.info())
p(df.shape)
# 2- دستکاری اولیه داده‌ها
p(df.isna().sum())
# بررسی مقادیر خالی
df.bfill(inplace=True)
# پرکردن مقادیر خالی با مقدار قبلی در همان ستون
# چون مقادیر خالی کم بودند از این روش پرکردن استفاده کردیم
p(df.isna().sum())

# 3- فیلتر ردیف‌ها با شرط ساده (مثلاً سن > 20)
filtered_df= df.query("age>25")
p(filtered_df)


# 4- مرتب‌سازی داده‌ها با sort_values
filtered_df.sort_values(by="age",ignore_index=True,inplace=True)
p(filtered_df)

# 5- دسترسی به ستون‌ها و ردیف‌ها، انتخاب چند ستون، slicing(محدود سازی نتایج)

limited_df= filtered_df.iloc[:,0:6]
# کل ردیف ها و همه ستون ها به غیر ستون آخر را انتخاب کردیم
# داتافریم نتیجه را در یک فایل سی اس وی ذخیره کردیم
expath= r"e:\python\INTPCode\3MonthProject\Month-01\Week-01\Day-04\data\limited_df.csv"
# limited_df.to_csv(expath,index=False)

# دوباره فایل سی اس وی جدید را خواندیم
dfall= pd.read_csv(expath)
p(dfall)