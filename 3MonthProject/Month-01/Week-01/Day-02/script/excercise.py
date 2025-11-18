# month-01
# week-01
# Day-02

# ایجاد یک DataFrame با داده‌های نمونه

import pandas as pd
info = {"students":["raziya","soiba","halim","darya","hadiya"],
"math_points":[18,17,13.5,16,17],
"phisics_points":[17,18,14,13,15]}
stu_df= pd.DataFrame(info)
print(stu_df)

# دسترسی به ستون‌ها
print(stu_df["students"], stu_df["math_points"])

# دسترسی به ردیف‌ها
print(stu_df.iloc[0])
print(stu_df.iloc[1])

# نمایش head() و tail()
print(stu_df.head())
print(stu_df.tail())