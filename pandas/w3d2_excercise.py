# 1 - یک داتافریم ساده بساز 
import pandas as pd
p = print
path = r"e:\python\INTPCode\pandas\student1.csv"
df1= pd.read_csv(path)
# متغیر مسیر فایل مرجع حذف شد تا به اشتباه در مراحل بعدی تغییر نیابد 
del path

# 2- داتافریم را با تابع to_excel ذخیره کن
# ساخت مسیر فایل اکسل  محل ذخیره داتافریم ها
expath = r"e:\python\INTPCode\pandas\to_excel.xlsx"
# وارد کردن تکی داتافریم ها
# df1.to_excel(inpath,sheet_name= "sh1",index= False)

'''
3- دوباره فایل ذخیره شده را با 
read_excel 
بخوان تا مطمئن بشی ذخیره شده 
'''
# باید کل فایل اکسل را تبدیل به یک داتافریم کلی کنیم تا قابل خواندن شود
# dfall = pd.read_excel(expath,sheet_name=None)
# p(dfall)

# 4- دو شیت مختلف روی این فایل اکسل ذخیره کن
'''
ابتدا باید 
to_excel 
سوال دوم را تبدیل به کامنت کنیم
البته بعد از یک بار اجرا و ساخت شیت اول
'''
# روش اصلی وارد کردن داتافریم ها در اصل مثل زیر است
# ابتدا ساخت داتافریم های ثانویه از روی داتافریم اول
df2 = df1.query("math > 9 and chemistry>9 and biology >9")
df2.fillna(method="ffill",inplace=True)
df2.reset_index(drop=True, inplace=True)
# p(df2)
'''
with pd.ExcelWriter(expath,mode='a',if_sheet_exists= "error") as writer:
    df1.to_excel(writer,sheet_name="sh1",index=False)
    df2.to_excel(writer,sheet_name="sh2",index=False)  
    ''' 
dfall = pd.read_excel(inpath,sheet_name=None)
p(dfall)