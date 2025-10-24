# 1- دو df بساز: یکی شامل اطلاعات دانش‌آموزان، یکی شامل نمرات
import pandas as pd
p =print
path = r"e:\python\INTPCode\pandas\to_excel.xlsx"
df1 = pd.read_excel(path,sheet_name=0,usecols=range(0,3))
df1= df1.query("age.gt(30)")
df1.dropna(inplace=True,ignore_index=True)
df2 = pd.read_excel(path,sheet_name=1,usecols=[0,3,4,5])
# 2- با ستون مشترک (مثل "نام") ادغام کن
dfout= pd.merge(df1,df2,how="outer",on="name")
# 3- هر چهار نوع join را امتحان کن و تفاوتشان را ببین
# outer 
p("outer:",dfout)

# inner
dfin= pd.merge(df1,df2,how="inner",on="name")
p("inner:",dfin)

# left merge
dfl= pd.merge(df1,df2,how="left",on="name")
p("left:",dfl)

# right merge nulls ordered in last by duckdb
dfr= pd.merge(df1,df2,how="right",on="name")
import duckdb
dfr=duckdb.sql("select * from dfr order by country nulls last").df()
# مرتب کردن مقادیر خالی در آخر داتافریم
# یک ستون را که مقادیر خالی زیادی قرار دارد مبنای مرتب سازی قرار میدهیمو بقیه هم مرتب میشوند
p("right:",dfr)

# 4- در خروجی، فقط چند ستون خاص را نگه دار
dfout= duckdb.sql("select name, age, biology from dfout order by age desc").df()
dfout.fillna(dfout["biology"].mean(),inplace=True)
p(dfout)