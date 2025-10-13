# مرور تمام دستورات: انتخاب، فیلتر، مرتب‌سازی
# 1.یک دیتاست را بخوان و  ستون‌های مهم را انتخاب کن
import pandas as pd
df = pd.read_csv(r"e:\python\test-project\pandas\student1.csv")
p = print
# نمایش اسامی ستون ها
# p(df.columns)

# نمایش تعداد ردیف های خالی هر ستون
# p(df.isna().sum())

# انتخاب چند ستون مهم
df = df.loc[:,['name', 'country', 'age',]]
'''
در این صورت بقیه ستون ها از داتافریم حذف میشوند
پس نیازی به حذف آنها با تابع 
drop 
نیست
'''
# 2. ردیف‌ها را بر اساس شرطی فیلتر کن
df.dropna(inplace=True)
'''
باید ردیف های خالی را حذف کنیم چون تابع 
str 
در شرط زیر ارور میده
'''
df = df.query("not country.str.contains('Ir') and age.gt(22)")
# 3. داده‌ها را مرتب کن
df.sort_values(by="age",inplace=True,ascending=False)
# داده ها را به صورت ستون سن و به صورت نزولی مرتب کردیم
df= df.reset_index(drop=True)
# 4. ستون جدید اضافه کن
# df.loc[:,["gender","solardum"]] = pd.NA
df[["gender","solardum"]] = None
# p(df)
# 5. خلاصه آمار (mean, max, min) را نمایش بده
# اعمال تکی توابع آماری برای یک ستون خاص
'''
p(df["age"].sum())
p(df["age"].count())
p(df["age"].mean())
p(df["age"].median())
p(df["age"].min())
p(df["age"].max())
p(df["age"].std())
'''
# اعمال یکجای چند تابع آماری روی یک ستون 
p(df.agg({"age":['count','sum','min','max','std','mean','median']}))