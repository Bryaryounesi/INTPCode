# month-01
# week-03
# Day-03

import pandas as pd
p = print
# 1- دو DataFrame با ستون‌های مشابه بساز و با concat ترکیب 
path = r"e:\python\INTPCode\3MonthProject\Month-01\Week-03\Day-02\data\students_scores_w03d02.xlsx"
df1 = pd.read_excel(path,sheet_name=0)
df2 = pd.read_excel(path,sheet_name=1)
dfall = pd.concat([df1,df2],ignore_index=True)
# p(dfall)
# 2- دو DataFrame با ستون‌های متفاوت بساز و با axis=1 ترکیب کن
df3 = pd.read_excel(path,sheet_name=0,usecols=range(0,2))
df4 = pd.read_excel(path,sheet_name=1,usecols=range(3,6))
dfall2= pd.concat([df3,df4],axis=1)
# p(dfall2)
# 3- بعد از ترکیب، داده‌های تکراری یا مقادیر NaN را بررسی کن
dfall.dropna(inplace=True)
dfall.drop_duplicates(inplace=True)

# dfall2.dropna(inplace=True)
dfall2.drop_duplicates(inplace=True)

dfall.reset_index(drop=True,inplace=True)
dfall2.reset_index(drop=True,inplace=True)
p(dfall)
p(dfall2)
