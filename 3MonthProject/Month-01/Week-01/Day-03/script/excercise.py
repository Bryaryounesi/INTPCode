# month-01
# week-01
# Day-03

# 1-دانلود یک CSV ساده (مثلاً داده‌های فروش یا دانش‌آموزان)
path=r"e:\python\INTPCode\3MonthProject\Month-01\data\student1.csv"
# 2-خواندن فایل با pd.read_csv
import pandas as pd
p=print
df= pd.read_csv(path)

# 3- مشاهده info(), describe()
p(df.info())
p(df.describe())

