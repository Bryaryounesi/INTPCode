'''
read_csv()
شکل رایج 
df = pd.read_csv(path)
# هر پارامتری پیش فرض دارد میتواند نوشته نشود
-path = r"مسیر فایل"
- index_col = "column_name"/None پیش فرض 

-----کمتر مورد استفاده---------

-nrows = تعداد ردیف
-use_cols = انتخاب ستون ها ، حالت ها در پایین

۱. با ایندکس حروفی اکسل:
usecols=["A", "C"]
۲. با نام خود ستون‌ها:
usecols=["Name", "Age"]
۳. با ایندکس عددی (شروع از ۰):
usecols=[1, 2]  
# ستون‌های دوم و سوم
۴. با بازه ایندکسی عددی:
usecols=range(1, 4) 
 # ستون‌های دوم، سوم و چهارم
۵. با بازه حروف اکسل:
usecols="A:C" 
 # تمام ستون‌های از A تا C
۶. ترکیب چندین بازه:
usecols="A:C, E:G"  # ستون‌های A-C و E-G
--------------------------------------------------
read_excel()
شکل رایج
dfall = pd.read_excel(path,sheet_name=None)
df2 = pd.read_excel(path,sheet_name=1)

-path = r"مسیر فایل"
-sheet_name = "names"/Noneبهتر/پیشفرض 0 

- use_cols = حالت ها در بالا توضیح داده شده اند
- nrows = عدد
- index_col = "column_name"/ None پیش فرض 

--------------------------------------------------
to_excel()

شکل رایج 
df.to_excel(expath,sheetname="sh1",index=False)

-expath
-sheet_name= پیشفرض sheet1 .../"sh1"بهتر/2
-index = True پیشفرض /False بهتر 

-----------------------------------------
pd.excelWriter()
شکل رایج
with pd.ExcelWriter(expath,mode='a',if_sheet_exists= "new") as writer:
    df1.to_excel(writer,sheet_name="sh1",index=False)
  
    df2 .....

expath
mode = "a"
if_sheet_exists= "new"بهتر /"replace"/"error"
-----------------------------------------------
pd.concat
شکل رایج
dfall = pd.concat([df1,df2,...],ignore_index=True)

objs = [,] / (,)
ignore_index = False بهتر/ پیشفرض True 
axis = پیش فرض 0 / 1

-----------------------------------------------
pd.merge
شکل رایج 

df = pd.merge(L,R, how='inner', on='col_name')
left	 = سمت چپ df
right	 =  سمت راست df 

how	 = نوع join ('inner', 'left', 'right', 'outer')

on	 = نام ستون مشترک بین دو df

left_on	= 
اگر نام ستون در df سمت چپ متفاوت باشد

right_on	= 
اگر نام ستون در df  سمت راست متفاوت باشد
'''