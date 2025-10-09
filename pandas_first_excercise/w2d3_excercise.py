import pandas as pd
df= pd.read_csv(r"e:\python\test-project\pandas_first_excercise\student1.csv")
print(df.dtypes)
p = print
# subject : sort values
# 1- داده‌ها را بر اساس یک ستون مرتب کن
'''df.sort_values(by="id",inplace=True)
p(df)'''
# 2- داده‌ها را بر اساس دو ستون مرتب کن (مثلاً اول جنسیت، بعد سن)
'''df.sort_values(by=["age","math"],inplace=True)
p(df)'''
# 3- مرتب‌سازی نزولی برای ستون عددی
'''df.sort_values(by=["biology","math"],ascending=False)
p(df)'''
# 4- مرتب سازی 
df.sort_values(by=["math","biology","chemistry"],inplace=True,ascending = True)
df.dropna(inplace=True)
#  محدود کردن نتایج
p(df.head(8))
p(df.iloc[-6: , 0:])