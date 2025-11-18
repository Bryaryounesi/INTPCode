# month-01
# week-04
# Day-03
# 1- داده‌ها را بر اساس یک ستون (مثلاً "محصول" یا "کلاس") گروه‌بندی کن
import pandas as pd
p = print
path = r"e:\python\INTPCode\3MonthProject\Month-01\Week-04\Day-03\data\student_data.xlsx"
df = pd.read_excel(path)
p(df.columns)
del path
# محاسبه درصد تکرار برای انتخاب بهترین ستون ها برای مبنای گروهبندی
for i in df.select_dtypes(exclude="number").columns:
    percent= 1-(df[i].nunique()/len(df[i]))
    percent = round(percent,2)
    p(f"{i} %:{percent}")
# ستون کانتری برای مبنای گروهبندی انتخاب شد
result= df.groupby(by="country")   
# شیء گروهبندی ساخته شد 

# 2- جمع فروش یا میانگین نمره را برای هر گروه محاسبه کن

numcols = df.select_dtypes(include="number").drop("age",axis=1).columns
# تمام ستون های عددی به غیر از ستون سن
# برای اعمال توابع آماری انتخاب شدند 
result= df.groupby(by="country",as_index=False)[numcols].mean().round()
p(result)
# 3- نتیجه را در یک داتافریم جدید ذخیره کن

expath=r"e:\python\INTPCode\3MonthProject\Month-01\Week-04\Day-03\data\groupby.xlsx"
'''
with pd.ExcelWriter(expath,mode="a",if_sheet_exists="replace") as writer:
    result.to_excel(writer,sheet_name="sh1",index=False)
'''    