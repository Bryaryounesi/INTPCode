import pandas as pd
df= pd.read_csv(r"e:\python\test-project\pandas_first_excercise\student1.csv")
print(df.dtypes)
p = print
df.dropna(inplace=True)
# 1- ردیف‌ها را با چند شرط فیلتر کن(فیلترسازی)
# p(df[ df["age"].between(40,60)])
# p(df.query("age> 40 and math>15 or biology>=18"))
# p(df.query("country.isin(['Iran','India']) or name=='Osman'"))
# p(df.query("age.between(20,28)or math.eq(19)"))
# p(df.query("name.str.startswith('b') or country.isin(['afganestan','Turkey'])"))
filtered_df = df.query("age.gt(50) or math.lt(12)")
# در میان چند شرط بالا آخرین شرط را انتخاب کردیم 
''' متوجه شدیم که فیلترکردن با شرط در دیتافریم تغییری ایجاد نمیکند
 پس این فیلتر کردن را در متغیری به نام  
filtered_df 
ذخیره کردیم
'''
# 2- نتیجه نهایی را مرتب کن
filtered_df.sort_values(by="id",inplace=True,ascending=False)
p(filtered_df)
# 3- چند ستون و چند ردیف را با هم انتخاب کن(محدودسازی)
p(filtered_df.iloc[:6,:3])
