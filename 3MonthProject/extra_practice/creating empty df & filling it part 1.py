# ساخت داتافریم خالی از صفر و پر کردن آن
import pandas as pd
p = print
# 1 - ابتدا یک لیست از اسامی ستون ها بسازید. اسم لیست مثلا col 
col = ['name','gender','country']
# 2- با تابع range یک سری عددی بسازید 
rows = pd.Series(range(0,30))

'''3- در فرمول داتافریم این لیست و این سری را برای دو پارامتر 
colomns و index وارد کنید.
در پارامتر ایندکس ، بعد از نام سری، یک نقطه ایندکس لازم است
در پایان این مرحله شما یک داتافریم خالی دارید
با تعداد ستون ها و ردیف های مشخص ولی خالی.
'''
df = pd.DataFrame(columns=col,index=rows.index)
p(df)
# داتافریم خالی ساخته شد

# .....پرکردن ستون های داتافریم ....
'''
پرکردن ستون های خالی داتافریم با سری 
هر ستون یک سری است 
بنابراین برای هر ستون یک سری میسازیم
'''
sname = pd.Series(['ali','jalal','shamal','soren',None])
sgender = pd.Series(['M','L',None])
scountry = pd.Series(['Iran','Iraq','India','Austria','Japan', None])
# .... ری ایندکس کردن سری هر ستون.....
'''
اگر با ارور عدم تطابق تعداد داده ها 
با ایندکس داتافریم مواجه شدید این عبارت را به انتهای سری
اضافه کنید
.reindex(df.index)
'''
# df['name'] = sname.reindex(df.index)
# p(df)

# ...سمپل گرفتن از سری ها برای پر کردن داتافریم ....
'''
شاید تنها در هرستون از داتافریم 
تنها چند آیتم داریم که بارها 
تکرار میشوند مثلا چند کشور محدود 
پس میتوانیم برای نمونه های آموزشی 
سری های منشا اینگونه ستون ها را خودمان 
بسط دهیم. با کمک تابع 
sample
و طبق الگوی زیر:
new_sery = old_sery.sample()

:پارامتر های تابع ایندکس 
n=تعداد ستون هایی تولیدی
replace=True/False
اگر ترو یعنی تکرار جایز است
ignor_index=True/False
اگر فولز یعنی ایندکس اصلی حفظ شود
 اغلب این سه تا الزامی اند 
'''
snamecomp = sname.sample(n=30,replace=True,ignore_index=True)
sgendercomp = sgender.sample(n=30,replace=True,ignore_index=True)
scountrycomp = scountry.sample(n=30,replace=True,ignore_index=True)

'''.....پرکردن ستون ها به صورت یکجا با تابع 
assign.....
در این تابع نام هر ستون را مساوی 
سری طویل شده آن قرار می دهیم 
'''
df = df.assign(name=snamecomp,gender=sgendercomp,country=scountrycomp)
p(df)
'''
داتافریم پر شد
کاری که میتوانستیم در اکسل انجام دهیم 
و اینجا فایلش رو ایمپورت کنیم
'''
p("............................")
'''
اصلاح ایندکس های بهم ریخته 
بعد از حذف ستون های حاوی مقادیر خالی
'''
df.dropna(inplace=True)
p(df)
# ایندکس ها به هم ریخته اند در اینجا
p("............................")
df = df.reset_index(drop=True)
p(df)
