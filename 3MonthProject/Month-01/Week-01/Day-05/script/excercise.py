# month-01
# week-01
# Day-05


# گام ۱: راه‌اندازی و خواندن داده‌ها
# کتابخانه pandas را ایمپورت کن.
# فایل students.csv را بخوان و آن را در یک DataFrame به نام df ذخیره کن.
# از ستون student_id به عنوان ایندکس DataFrame استفاده کن.
import pandas as pd
df = pd.read_csv(r"e:\python\INTPCode\3MonthProject\Month-01\Week-01\data\student1.csv",index_col="id")

# گام ۲: بررسی اولیه داده‌ها
# پنج سطر اول داده‌ها را نمایش بده.
# خلاصه اطلاعات DataFrame را با استفاده از info() چاپ کن.
print(df.head())
print(df.info())

# آمار توصیفی داده‌های عددی را با describe() نمایش بده. گام ۳: 
print(df.describe())
# مدیریت مقادیر خالی
# تعداد مقادیر خالی در هر ستون را پیدا کن.
# مقادیر خالی ستون‌های عددی (age, math_score, science_score) را با میانگین همان ستون پر کن.
# مقادیر خالی ستون‌های غیرعددی را با مقدار "Unknown" پر کن.
print(df.isna().sum())
for i in ["age", "math", "chemistry", "biology"]:
    df[i].fillna(df[i].mean().round(), inplace=True)
for x in ["name", "country"]:
    df[x].fillna("UNKNOWN", inplace=True)
print(df)

# گام ۴: تغییر ساختار داده‌ها
# نام ستون‌ها را به فارسی تغییر بده (یا برعکس): name → نام age → سن grade → مقطع math_score → نمره_ریاضی science_score → نمره_علوم
# ستون student_id را حذف کن (چون قبلاً آن را به عنوان ایندکس انتخاب 
#کردی).
df.columns=["namha","keshwarha","sen","riyazi","zist","shimi"]
# حذف نام ستون ایندکس
df.index.name = None
print(df)


# گام ۵: فیلتر و انتخاب داده‌ها
# فقط دانش‌آموزانی را نمایش بده که سن آن‌ها بیشتر از ۲۰ سال است.
# فقط ستون‌های نام و نمره_ریاضی را برای تمام دانش‌آموزان انتخاب کن.
# با استفاده از iloc، ردیف‌های ۵ تا ۱۰ و ستون‌های ۱ تا ۳ را انتخاب کن.

print(df.query("sen>20"))
print(df[["namha","riyazi"]])
print(df.iloc[5:10,0:3])
# با استفاده از loc، ردیف‌های با ایندکس ۱۰۱ تا ۱۰۵ و ستون‌های نام و سن را انتخاب کن.
# این امکانپذیر نیست چون خود ردیف هاایندکس خودشون رو دارن 


# گام ۶: مرتب‌سازی
# داده‌ها را بر اساس نمره_ریاضی به صورت نزولی مرتب کن. 2*. داده‌ها را ابتدا بر اساس سن (صعودی) و سپس بر اساس ریاضی (نزولی) مرتب کن.

# df.sort_values(by="riyazi",inplace=True,ascending=False)
# print(df)
# دادن پارامتر ascending به صورت لیست برای دو ستون
sorted_df= df.sort_values(by=["sen","riyazi"],ascending=[True,False])
print(sorted_df)

# ذخیره داتافریم مرتب شده در فایل سی اس وی 
expath=r"e:\python\INTPCode\3MonthProject\Month-01\Week-01\Day-05\data\sorted_df.csv"
sorted_df.to_csv(expath,index=False)
dfall= pd.read_csv(expath)
print(dfall)
