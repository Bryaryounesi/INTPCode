# month-02
# week-04
# weekly excercise

p=print

p("-----------------------------")
p("Day-01")

#1- یک دیتاست واقعی دانلود کن (مثلاً داده فروش یا نمرات دانش‌آموزان)
# یک داتاست از سایت کاگال دانلود شد 

#2- با pd.read_csv() یا pd.read_excel() بخوان
import pandas as pd
path=r"e:\python\INTPCode\3MonthProject\Month-02\week-04\Data\students_exam_scores.xlsx"
df=pd.read_excel(path)
# p(df)

#3- با info(), head(), describe() ساختار و آمار پایه را بررسی کن
p("df info:")
p(df.info())

p("df first 100 rows:")
p(df.head(100))

p("df numberic columns description:")
p(df.describe().round())
p("---------------------------------------------")
p("Day-02") 

# 1-شناسایی مقادیر گمشده (isnull())
p(df.isna().sum())
# مقادیر گمشده رو تشخیص نمیده این تابع چون این مقادیر به صورت 
# none 
# نوشته شده اند با حرف ان کوچک

df= df.replace("none",None)
# با تابع ریپلیس مقادیر خالی را اصلاح کردیم
p(df.isna().sum())
# مشخص شد که تنها یک ستون مقادیر خالی دارد 

# 2-حذف مقادیر گمشده (dropna())
# ولی به دلیل بالا بودن مقادیر خالی در آن ستون
# بهتر است به کلی، ستون را حذف کنیم

del df["test preparation course"]

# 3- جایگزینی مقادیر گمشده (fillna()) با میانگین هر ستون
p("-------------------------------------------")
p("Day-03") 

# 1-ستون‌های عددی دیتاست را تحلیل کن
numcols=df.select_dtypes(include="number")
p("df numberic columns:")
p(numcols)

# 2-میانگین، واریانس و انحراف معیار هر ستون را محاسبه کن
p("numcols variance:")
p(numcols.var().round())
p("------------------------")
p("numcols std:")
p(numcols.std().round())
p("------------------------")
# 3-بیشترین و کمترین مقدار هر ستون را مشخص کن
p("numcols max:")
p(numcols.max())
p("------------------------")
p("numcols min:")
p(numcols.min())
p("------------------------------------------")

p("Day-04")
# 1-ستون‌های دسته‌ای (مثلاً جنسیت، کلاس، محصول) را بررسی کن
p(df.info())
# با اینفو ستون های آبچکت را تشخیص دادیم 
# اغلب ستون های دسته ای از نوع آبجکت هستند 
df_objects=df.select_dtypes(include="object")
# ستون های آجکت را برای بررسی بیشتر، جدا کردیم
p("number of unique items of object columns:")
p(df_objects.nunique())
# تایید دسته ای بودن ستون ها به دلیل کم تعداد بودن مقادیر یونیک در آنها

# 2-تعداد هر دسته را با value_counts() محاسبه کن
p("First column value counts:")
p(df_objects.iloc[:,0].value_counts())

p("-------------------------")
p("Second column value counts:")
p(df_objects.iloc[:,1].value_counts())

p("-------------------------")
p("Third column value counts:")
p(df_objects.iloc[:,2].value_counts())
p("-------------------------")
p("Fourth column value counts:")
p(df_objects.iloc[:,3].value_counts())

p("-------------------------")
# 3-میانگین یا جمع یک ستون عددی را بر اساس گروه‌ها محاسبه کن (groupby)
numcols_list= numcols.columns.tolist()
groupers_list= df_objects.columns.tolist()


group=df.groupby(by=groupers_list,as_index=False)[numcols_list].mean().reset_index(drop=True).round()
# میانگین کل ستون های عددی رو بر اساس ستون های دسته ای حساب کردم و 
# در یک داتافریم جدید ذخیره کردم

path2=r"e:\python\INTPCode\3MonthProject\Month-02\week-04\Data\grouped.xlsx"
'''
with pd.ExcelWriter(path2,mode='a',if_sheet_exists= "new") as writer:
    group.to_excel(writer,sheet_name="sh1",index=False)
'''
# نتیجه در یک اکسل جدید ذخیره شد ولی
# اسامی ستون های عددی در این اکسل جدید نیز، بدون تغییر باقی ماند
# منتها محتوای این ستون ها در اکسل جدید، تغییر کرده 
# و تبدیل به میانگین بر اساس گروهبندی شده است 
p("-------------------------")
p("Day-05")

# 1-یک ستون عددی را هیستوگرام کن
import matplotlib.pyplot as plt

fig1,axs1=plt.subplots()
numcols.plot(kind="hist",y=numcols.columns[1],ax=axs1,color="green",edgecolor="black",title="Students Reading Score Histogram")
# دی اف پلات هیستوگرام ستون منتخب، رسم شد

# 2-یک ستون دسته‌ای را نمودار میله‌ای رسم کن
fig2,axs2=plt.subplots()

df_objects.iloc[:,1].value_counts().plot(kind="bar",ax=axs2,color="green",edgecolor="black",title="race/ethnicity value counts bar",xlabel="scores bins")
# سری پلات میله ای ستون دسته ای منتخب رسم شد

# fig1.savefig(fname="Students Reading Score Histogram.png",dpi=300)
# fig2.savefig(fname="race ethnicity value counts bar.png",dpi=300)

# 3-یک رابطه دو ستون عددی را با scatter plot نمایش بده
fig3,axs3=plt.subplots()
numcols.plot(kind="scatter",x=numcols.columns[0],y=numcols.columns[1],ax=axs3,color="green",title="math score reading score scatter")
# fig3.savefig(fname="math score reading score scatter.png",dpi=300)

p("--------------------------------------")


