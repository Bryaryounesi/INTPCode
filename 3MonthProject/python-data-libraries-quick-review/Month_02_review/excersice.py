'''
هفته اول
Pandas - راهنمای مرور سریع (Junior Computer Vision)

==============================

==============================

۱. مفاهیم پایه و ساختارها

==============================

import pandas as pd

Series: آرایه یک‌بعدی با ایندکس (مثل ستون اکسل)

s = pd.Series([30, 32, 13, 40], index=['a', 'b', 'c', 'd'])
s = pd.Series([85, 90, 78], index=["Ali", "Sara", "Reza"])
print(s["Sara"])           # دسترسی با ایندکس
s["Sara"] = 95             # تغییر مقدار
print(s + 10)              # عملیات برداری روی همه مقادیر

DataFrame: جدول دوبعدی (مجموعه‌ای از Series)

ساخت از دیکشنری (هر کلید = یک ستون)

df = pd.DataFrame({
"name": ["Ali", "Sara", "Reza"],
"age": [25, 30, 22],
"score": [85, 90, 78]
})

ساخت از لیست با نام ستون‌ها

df = pd.DataFrame(
[["ali", 25], ["hadi", 40], ["sima", 34]],
columns=["name", "age"]
)

ایندکس دلخواه برای ردیف‌ها

df = pd.DataFrame(
{"Name": ["Alice", "Bob"], "Age": [25, 30]},
index=["A1", "B1"]
)

==============================

۲. خواندن و نوشتن فایل

==============================

df = pd.read_csv("file.csv")                      # خواندن CSV
df = pd.read_csv("file.csv", delimiter=";")       # جداکننده غیر کاما
df = pd.read_csv("file.csv", index_col="id")      # ستون ایندکس از فایل

df.to_csv("output.csv", index=False)              # ذخیره (بدون ایندکس)

==============================

۳. مرور اولیه داده‌ها (ضروری قبل از هر کار)

==============================

df.head()           # ۵ ردیف اول
df.tail()           # ۵ ردیف آخر
df.shape            # (تعداد ردیف, تعداد ستون)
df.info()           # نوع داده و تعداد مقادیر غیرخالی
df.describe()       # آمار توصیفی ستون‌های عددی
df.columns          # لیست نام ستون‌ها
df.dtypes           # نوع داده هر ستون

==============================

۴. انتخاب داده (Indexing & Slicing)

==============================

--- ستون‌ها ---

df["age"]                    # یک ستون (Series)
df[["name", "age"]]          # چند ستون (DataFrame)

--- ردیف‌ها با loc (بر اساس نام ایندکس) ---

df.loc[0]                    # ردیف با ایندکس 0
df.loc[0:2]                  # بازه ردیف‌ها (حد انتها شامل می‌شود)
df.loc[0:2, "name"]          # ردیف‌های 0 تا 2، فقط ستون name
df.loc[0:2, ["name", "age"]] # ردیف‌های 0 تا 2، ستون‌های name و age
df.loc[:, "name":]           # همه ردیف‌ها، ستون name تا آخر

--- ردیف‌ها با iloc (بر اساس موقعیت عددی) ---

df.iloc[0]                   # ردیف اول
df.iloc[0:3]                 # سه ردیف اول (حد انتها شامل نمی‌شود)
df.iloc[0:3, 0:2]            # سه ردیف اول، دو ستون اول
df.iloc[[0, 2, 5]]           # ردیف‌های خاص با لیست

--- تفاوت کلیدی loc و iloc ---

loc:   با نام ایندکس کار می‌کند، بازه شامل انتهاست

iloc:  با موقعیت عددی کار می‌کند، بازه شامل انتها نیست (مثل لیست)

==============================

۵. فیلتر شرطی (Boolean Indexing)

==============================

شرط ساده

df[df["age"] >= 20]
df[df["name"] == "Ali"]
df[df["city"] != "Tehran"]

شرط روی متن

df[df["name"].str.contains("Ali")]      # شامل
df[df["name"].str.startswith("A")]      # شروع با
df[df["name"].str.endswith("i")]        # پایان با

شرط عضویت در لیست

df[df["city"].isin(["Tehran", "Shiraz"])]

شرط مقادیر خالی

df[df["score"].isna()]                  # تهی‌ها
df[df["score"].notna()]                 # غیرتهی‌ها

ترکیب شرط‌ها با & (and) و | (or)

df[(df["age"] > 20) & (df["score"] > 80)]
df[(df["city"] == "Tehran") | (df["city"] == "Shiraz")]

==============================

۶. مقادیر گمشده (Missing Data)

==============================

--- تشخیص ---

df.isna().sum()              # تعداد NaN در هر ستون (ضروری‌ترین بررسی)

--- حذف ---

df.dropna(inplace=True)      # حذف ردیف‌های دارای NaN
df.dropna(axis=1, inplace=True)  # حذف ستون‌های دارای NaN

--- پر کردن با مقدار ثابت ---

df.fillna(0, inplace=True)
df["name"].fillna("UNKNOWN", inplace=True)

--- پر کردن با آماره ---

df["age"].fillna(df["age"].mean(), inplace=True)    # میانگین
df["age"].fillna(df["age"].median(), inplace=True)  # میانه
df["name"].fillna(df["name"].mode()[0], inplace=True) # مد (بیشترین تکرار)

نکته: mode() یک Series برمیگرداند، [0] اولین مقدار را می‌گیرد

--- پر کردن با مقدار قبلی/بعدی (برای داده‌های زمانی) ---

df.ffill(inplace=True)
df.bfill(inplace=True)

--- پر کردن با نمونه‌گیری تصادفی از همان ستون (پیشرفته) ---

for col in df.columns:
non_null = df[col].dropna(ignore_index=True)
n_missing = df[col].isna().sum()
samples = non_null.sample(n=n_missing, replace=True, random_state=42)
df.loc[df[col].isna(), col] = samples.values

--- اصلاح نوع داده بعد از پر کردن (مهم) ---

num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].round().astype(int)

==============================

۷. دستکاری و تمیزکاری داده

==============================

--- تغییر نام ستون ---

df.rename(columns={"old_name": "new_name"}, inplace=True)
df.columns = ["new1", "new2", "new3"]  # تغییر همه ستون‌ها

--- حذف ستون ---

df.drop("column_name", axis=1, inplace=True)
del df["column_name"]

--- حذف ردیف ---

df.drop(0, axis=0, inplace=True)
df.drop([3, 5, 7], axis=0, inplace=True)

--- ریست ایندکس ---

df.reset_index(drop=True, inplace=True)  # ایندکس جدید 0 تا n-1

==============================

۸. مرتب‌سازی

==============================

df.sort_values(by="age", inplace=True)                     # صعودی
df.sort_values(by="age", ascending=False, inplace=True)    # نزولی
df.sort_values(by=["age", "score"], ascending=[True, False], inplace=True)  # چندستونه

==============================

۹. توابع آماری

==============================

روی یک ستون

df["age"].sum()
df["age"].mean()
df["age"].median()
df["age"].max()
df["age"].min()
df["age"].std()
df["age"].count()        # تعداد مقادیر غیرخالی
df["age"].nunique()      # تعداد مقادیر یکتا
df["age"].mode()         # بیشترین تکرار (خروجی Series)

روی کل DataFrame

df.sum()
df.mean()
df.describe()            # خلاصه آماری کامل

روی ردیف‌ها

df.sum(axis=1)

چند تابع روی چند ستون با agg

df.agg({
"age": ["max", "sum", "std"],
"math": ["sum", "std", "min"]
})

==============================

۱۰. عملیات برداری (Vectorized - سریعترین روش)

==============================

df["double_age"] = df["age"] * 2
df["full_name"] = df["first"] + " " + df["last"]
df["passed"] = df["score"] >= 60

==============================

۱۱. groupby (ضروری برای تحلیل)

==============================

df.groupby("city")["age"].mean()              # میانگین سن به تفکیک شهر
df.groupby("city").agg({"age": "mean", "score": "max"})  # چند تابع

==============================

۱۲. merge و join (ترکیب جداول)

==============================

pd.merge(df1, df2, on="id")                   # اشتراکی (INNER JOIN)
pd.merge(df1, df2, on="id", how="left")       # همه df1 + تطابق df2

==============================

خلاصه چک‌لیست روزمره

==============================

1. df.head() → df.info() → df.isna().sum()

2. پر کردن/حذف NaN

3. اصلاح نوع داده‌ها (astype)

4. تحلیل با describe, groupby, شرط‌ها

==============================
هفته دوم

Pandas - راهنمای مرور سریع (بخش دوم: عملیات پیشرفته)

==============================

==============================

۱. انتخاب و محدودسازی (Selection & Limiting)

==============================

--- انتخاب ستون ---

df["age"]                     # یک ستون (Series)
df[["name", "age", "math"]]   # چند ستون (DataFrame)

--- انتخاب با iloc (موقعیت عددی - بازه نیمه‌باز: انتها شامل نمی‌شود) ---

df.iloc[:5]                   # پنج ردیف اول (0 تا 4)
df.iloc[1:4]                  # ردیف‌های 1 تا 3
df.iloc[-5:]                  # پنج ردیف آخر (ایندکس منفی)

--- انتخاب با loc (برچسب - بازه بسته: انتها شامل می‌شود) ---

df.loc[0:4]                   # پنج ردیف اول (0 تا 4)
df.loc[:, "name":"math"]      # همه ردیف‌ها، ستون name تا math

--- انتخاب همزمان ردیف و ستون ---

df.iloc[:6, :3]               # ۶ ردیف اول، ۳ ستون اول
df.loc[:, ["name", "age"]]    # همه ردیف‌ها، ستون‌های مشخص

--- ذخیره انتخاب به‌عنوان دیتافریم جدید ---

df = df.loc[:, ["name", "age"]]  # جایگزینی دیتافریم با ستون‌های انتخاب‌شده

--- head/tail با iloc (روش دوم) ---

df.iloc[:5]    # معادل head(5)
df.iloc[-5:]   # معادل tail(5)

==============================

۲. فیلتر شرطی پیشرفته (Advanced Filtering)

==============================

--- اپراتورهای منطقی (&, |, ~) ---

نکته: هر شرط باید داخل پرانتز باشد

df[(df["age"] > 20) & (df["city"] == "Tehran")]        # AND
df[(df["age"] < 18) | (df["city"] == "Isfahan")]       # OR
df[~(df["city"] == "Tehran")]                           # NOT
df[~df["city"].isin(["Tehran", "Mashhad"])]             # NOT IN

--- ترکیب پیچیده ---

df[((df["age"] > 18) & (df["city"] == "Tehran")) | (df["name"] == "Maryam")]

--- متدهای شرطی ساده‌تر ---

df[df["age"].between(20, 30)]          # بازه عددی
df[df["city"].isin(["Tehran", "Shiraz"])]  # عضویت در لیست

--- فیلتر با query() (خوانایی بالاتر) ---

نکته: داخل query رشته‌ها با سینگل‌کوت، نام ستون‌ها بدون کوت

df.query("age > 20 and city == 'Tehran'")
df.query("age.between(40, 50) and country.isin(['Iran', 'Iraq'])")
df.query("country not in ['Iran', 'Iraq']")               # NOT IN در query
df.query("not (age > 40 and math < 14)")                  # نفی ترکیبی
df.query("not age > 40 and not math < 14")                # روش بهتر نفی
df.query("name.str.startswith('b') or country.isin(['Turkey'])")  # شرط متنی

--- فیلتر با eval() ---

df[df.eval("age > 20 and (city == 'Tehran' or city == 'Shiraz')")]

--- ذخیره نتیجه فیلتر ---

filtered_df = df.query("age > 50 or math < 12")

==============================

۳. مرتب‌سازی (Sorting)

==============================

--- تک‌ستونه ---

df.sort_values(by="age", inplace=True)
df.sort_values(by="age", ascending=False, inplace=True)   # نزولی

--- چندستونه ---

df.sort_values(by=["age", "math"], inplace=True)
df.sort_values(by=["age", "math"], ascending=[True, False], inplace=True)

--- ریست ایندکس بعد از مرتب‌سازی (مهم) ---

df.reset_index(drop=True, inplace=True)

==============================

۴. تغییر نوع داده‌ها (Type Conversion)

==============================

--- بررسی نوع داده ---

df.info()               # خلاصه کامل با Dtype
df.dtypes               # نوع هر ستون
df["age"].dtype         # نوع یک ستون خاص

--- تبدیل نوع با astype ---

df["age"] = df["age"].astype(int)

--- تبدیل یکجای چند ستون ---

df = df.astype({
"age": "int",
"biology": "int",
"chemistry": "int"
})

--- تبدیل به datetime (حرفه‌ای) ---

df["date"] = pd.to_datetime(df["date"], errors="coerce")

--- حذف تاریخ‌های نامعتبر (NaT) ---

df = df.dropna(subset=["date"])

--- بررسی NaT ---

df["date"].isna().sum()

==============================

۵. گروه‌بندی زمانی (Time Grouping)

==============================

--- گروه‌بندی با dt (ساده و کاربردی) ---

df.groupby(df["date"].dt.year).size()             # سالانه
df.groupby(df["date"].dt.month).size()            # ماهانه
df.groupby(df["date"].dt.date).size()             # روزانه

--- ترکیب سال و ماه (جلوگیری از قاطی شدن سال‌ها) ---

df.groupby([df["date"].dt.year, df["date"].dt.month]).size()

--- گروه‌بندی با ستون عددی ---

df.groupby(df["date"].dt.month)["sales"].sum()

--- resample (روش حرفه‌ای) ---

df.set_index("date").resample("M").size()

--- چک‌لیست قبل از groupby زمانی ---

1. ستون datetime واقعی باشد

2. NaT نداشته باشد

3. داده مرتب زمانی باشد (sort_values)

==============================

۶. افزودن ستون جدید

==============================

--- از روی ستون‌های موجود ---

df["sum"] = df["math"] + df["chemistry"]
df["remath"] = df["math"] - 20

--- ستون خالی ---

df["new_col"] = None
df[["new1", "new2"]] = None
df.loc[:, "new_col"] = pd.NA

--- ستون با مقدار ثابت ---

df["passed"] = True

==============================

۷. افزودن ردیف جدید

==============================

--- با loc (بهترین روش) ---

df.loc[len(df)] = [25, "Ali", 180]         # افزودن به انتها
df.loc[4] = [30, "Sara", 165]             # جایگزینی ردیف با ایندکس 4
df.loc[20] = [25, "Ali", 180]             # ساخت ردیف با ایندکس جدید

--- با iloc (فقط تغییر ردیف موجود) ---

df.iloc[5, 2] = "new_value"               # تغییر یک سلول خاص

df.iloc[len(df)] = [...]  ❌ اشتباه - iloc ردیف جدید نمی‌سازد

==============================

۸. ساخت دیتافریم خالی از صفر

==============================

cols = ['name', 'gender', 'country']
rows = pd.Series(range(30))

df = pd.DataFrame(columns=cols, index=rows.index)

--- پر کردن با Series (با reindex برای تطابق طول) ---

s_name = pd.Series(['ali', 'jalal', 'shamal', 'soren'])
df['name'] = s_name.reindex(df.index)

--- پر کردن با نمونه‌گیری (برای داده‌های محدود) ---

s_name_comp = s_name.sample(n=30, replace=True, ignore_index=True)
df = df.assign(name=s_name_comp)

--- پاکسازی نهایی ---

df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)

==============================

۹. مراحل استاندارد کار با داده

==============================

1. بارگذاری

df = pd.read_csv("file.csv")

2. بررسی اولیه

df.columns
df.head()
df.shape
df.info()
df.describe()
df.isnull().sum()

3. پاکسازی

df.dropna(inplace=True)           # یا fillna
df["age"] = df["age"].astype(int) # اصلاح نوع داده

4. فیلتر

filtered = df.query("age > 20")

5. مرتب‌سازی

filtered.sort_values(by="age", inplace=True)
filtered.reset_index(drop=True, inplace=True)

6. محدودسازی

result = filtered.loc[:, ["name", "age", "math"]]

7. تحلیل آماری

result.agg({"age": ["mean", "max", "min"], "math": ["sum", "std"]})

==============================

خلاصه چک‌لیست هفتگی

==============================

1. انتخاب: df[["col1", "col2"]], df.iloc[:5], df.loc[:, "name":]

2. فیلتر: query("age > 20 and city == 'Tehran'") یا شرط‌های & | ~

3. مرتب‌سازی: sort_values(by="col"), سپس reset_index

4. تغییر نوع: astype() یا pd.to_datetime

5. ستون جدید: df["new"] = df["a"] + df["b"]

6. تحلیل: groupby(), agg(), describe()

==============================
هفته سوم

Pandas - راهنمای مرور سریع (بخش سوم: فایل، ترکیب و تولید داده)

==============================

==============================

۱. خواندن و نوشتن فایل Excel

==============================

--- خواندن فایل Excel ---

df = pd.read_excel("file.xlsx")                     # فقط شیت اول
df = pd.read_excel("file.xlsx", sheet_name="Sales") # شیت خاص با نام
df = pd.read_excel("file.xlsx", sheet_name=0)       # شیت خاص با ایندکس (از 0)
df_all = pd.read_excel("file.xlsx", sheet_name=None) # همه شیت‌ها (دیکشنری df)

--- پارامترهای مهم read_excel ---

df = pd.read_excel("file.xlsx", usecols=["Name", "Age"])     # ستون‌های خاص
df = pd.read_excel("file.xlsx", usecols=range(0, 3))         # بازه عددی ستون‌ها
df = pd.read_excel("file.xlsx", nrows=100)                   # فقط n ردیف اول
df = pd.read_excel("file.xlsx", dtype={"Age": int})          # نوع داده
df = pd.read_excel("file.xlsx", skiprows=2)                  # رد کردن ردیف‌های ابتدایی

--- دسترسی به شیت‌ها از دیکشنری همه شیت‌ها ---

df_all = pd.read_excel("file.xlsx", sheet_name=None)
df_book = df_all["book"]                         # دسترسی به یک شیت
print(df_all.keys())                             # لیست نام همه شیت‌ها

--- نوشتن در Excel ---

df.to_excel("output.xlsx", index=False)                       # ذخیره یک شیت
df.to_excel("output.xlsx", sheet_name="Students", index=False)

--- نوشتن چند شیت در یک فایل (حفظ شیت‌های قبلی) ---

with pd.ExcelWriter("file.xlsx", mode="a", if_sheet_exists="replace") as writer:
df1.to_excel(writer, sheet_name="Sh1", index=False)
df2.to_excel(writer, sheet_name="Sh2", index=False)

پارامتر if_sheet_exists:

"error"   : خطا اگر شیت وجود داشته باشد

"replace" : جایگزینی شیت موجود

"new"     : ساخت شیت با نام جدید

==============================

۲. ترکیب داده‌ها با concat (اتصال ساده)

==============================

--- اتصال عمودی (ردیف‌ها زیر هم) ---

df_combined = pd.concat([df1, df2], axis=0, ignore_index=True)

--- اتصال افقی (ستون‌ها کنار هم) ---

df_combined = pd.concat([df1, df2], axis=1)

نکته: در اتصال عمودی، ستون‌های غیرمشترک با NaN پر می‌شوند

نکته: ignore_index=True ایندکس را از 0 بازسازی می‌کند

--- حذف ردیف‌های تکراری بعد از ترکیب ---

df.drop_duplicates(inplace=True, ignore_index=True)

پارامتر subset: فقط ستون‌های خاص را برای تشخیص تکرار بررسی کن

df.drop_duplicates(subset=["name", "age"], inplace=True)

==============================

۳. ترکیب داده‌ها با merge (مشابه SQL JOIN)

==============================

--- ساختار کلی ---

pd.merge(left, right, how='inner', on='column_name')

--- انواع join ---

df_inner = pd.merge(df1, df2, how="inner", on="id")   # فقط مقادیر مشترک
df_left  = pd.merge(df1, df2, how="left", on="id")    # همه df1 + تطابق df2
df_right = pd.merge(df1, df2, how="right", on="id")   # همه df2 + تطابق df1
df_outer = pd.merge(df1, df2, how="outer", on="id")   # همه ردیف‌های هر دو

--- merge با نام ستون‌های متفاوت ---

pd.merge(df1, df2, left_on="id", right_on="student_id")

--- merge روی چند ستون مشترک ---

pd.merge(df1, df2, on=["name", "age", "country"])

==============================

۴. ساخت داده‌های آزمایشی با Faker

==============================

from faker import Faker
import random

--- تنظیم seed برای ثابت ماندن داده‌ها ---

random.seed(6)
Faker.seed(6)

--- ساخت شیء Faker ---

fake = Faker()

fake = Faker('fa_IR')  # برای داده‌های فارسی

--- توابع پرکاربرد Faker ---

fake.name()              نام کامل

fake.first_name()        نام کوچک

fake.country()           کشور

fake.city()              شهر

fake.email()             ایمیل

fake.phone_number()      شماره تلفن

fake.job()               شغل

fake.random_int(min=, max=)  عدد تصادفی

fake.date()              تاریخ

--- random.choices (برای داده‌های محدود با وزن) ---

random.choices(population, weights=None, k=تعداد)

gender = random.choices(["M", "F", None], weights=[0.8, 0.1, 0.1], k=80)

--- الگوی کامل ساخت دیتافریم با Faker ---

random.seed(6)
Faker.seed(6)
fake = Faker()

data = [{
"name": fake.first_name(),
"country": fake.country() if random.random() < 0.8 else None,  # 20% NaN
"age": fake.random_int(min=16, max=65) if random.random() < 0.9 else None
} for _ in range(70)]

df = pd.DataFrame(data)

--- افزودن ستون جدید با Faker ---

df["phone"] = [fake.phone_number() for _ in range(len(df))]

--- ذخیره در Excel ---

with pd.ExcelWriter("file.xlsx", mode="a", if_sheet_exists="replace") as writer:
df.to_excel(writer, sheet_name="sh6", index=False)

==============================

۵. پارامترهای مشترک read_csv و read_excel (مرور)

==============================

usecols       → انتخاب ستون‌های خاص

nrows         → تعداد ردیف محدود

dtype         → تعیین نوع داده ستون‌ها

skiprows      → رد کردن n ردیف اول

index_col     → ستون ایندکس

parse_dates   → تبدیل خودکار به datetime

na_values     → مقادیر معادل NaN

converters    → اعمال تابع روی ستون هنگام خواندن

==============================

چک‌لیست ترکیب داده‌ها

==============================

1. خواندن: read_csv / read_excel با sheet_name و usecols

2. ترکیب عمودی: concat([df1, df2], axis=0) → drop_duplicates

3. ترکیب بر اساس کلید: merge(df1, df2, how="inner/left/right/outer", on="id")

4. مدیریت NaN: isnull().sum() → fillna / dropna

5. ذخیره: to_excel با ExcelWriter برای چند شیت

==============================
هفته چهارم 
Pandas - راهنمای مرور سریع (بخش چهارم: groupby و matplotlib)

==============================

==============================

۱. groupby - گروه‌بندی و خلاصه‌سازی داده‌ها

==============================

--- ساختار کلی ---

df.groupby(by="col_name")["target_col"].تابع_آماری()

--- پارامترهای مهم ---

by:        ستون(های) مبنای گروه‌بندی

as_index:  False → ستون گروه‌بندی در خروجی می‌ماند (توصیه می‌شود)

sort:      False → سریع‌تر، ترتیب اصلی حفظ می‌شود

--- انتخاب ستون هدف برای محاسبات ---

df.groupby("country", as_index=False)["math"].mean()                     # یک ستون
df.groupby("country", as_index=False)[["math", "biology"]].sum()         # چند ستون

--- انتخاب خودکار همه ستون‌های عددی ---

num_cols = df.select_dtypes(include="number").columns
df.groupby("country", as_index=False)[num_cols].mean().round()

حذف یک ستون عددی از محاسبات

num_cols = df.select_dtypes(include="number").drop("age", axis=1).columns

--- توابع آماری رایج بعد از groupby ---

df.groupby("country")["math"].mean()      # میانگین
df.groupby("country")["math"].sum()       # جمع
df.groupby("country")["math"].max()       # بیشترین
df.groupby("country")["math"].min()       # کمترین
df.groupby("country")["math"].count()     # تعداد مقادیر غیرخالی
df.groupby("country").size()              # تعداد کل ردیف‌ها (با NaN)
df.groupby("country")["math"].median()    # میانه
df.groupby("country")["math"].std()       # انحراف معیار
df.groupby("country")["city"].nunique()   # تعداد مقادیر یکتا

--- agg: چند تابع همزمان ---

df.groupby("country", as_index=False).agg({
"math": ["mean", "max"],
"biology": ["min", "median"]
})

یا با نام‌گذاری دلخواه:

df.groupby("country", as_index=False).agg(
math_mean=("math", "mean"),
bio_max=("biology", "max")
)

--- get_group: استخراج یک گروه خاص ---

grouped = df.groupby("country")
print(grouped.get_group("Germany"))

معادل: df.query("country == 'Germany'")

--- مشاهده نام همه گروه‌ها ---

print(grouped.groups.keys())

--- فیلتر قبل و بعد از groupby ---

df.query("math > 9").groupby("country", as_index=False)["math"].mean()          # قبل
df.groupby("country", as_index=False)["math"].mean().query("math > 15")         # بعد (HAVING)

--- محاسبه درصد مقادیر گمشده هر ستون (برای انتخاب ستون groupby مناسب) ---

for col in df.columns:
pct_missing = df[col].isna().sum() / len(df[col])
print(f"{col}: {pct_missing:.1%}")

--- محاسبه درصد تکرار مقادیر (تکرار کم = نامناسب برای groupby) ---

for col in df.select_dtypes(exclude="number").columns:
pct_unique = 1 - (df[col].nunique() / len(df[col]))
print(f"{col} repeat%: {pct_unique:.1%}")

==============================

۲. matplotlib - رسم نمودار

==============================

import matplotlib.pyplot as plt

--- نمودار خطی (plot) ---

plt.plot(df["age"], df["math"], marker="*", color="black",
linestyle="--", label="Math Scores")

پارامترها: marker (شکل نقاط), color, linestyle, label (برای legend)

--- نمودار میله‌ای (bar) ---

نیاز به محور x جداگانه برای لیست‌ها:

plt.bar(range(len(data)), data, color="green", edgecolor="black",
width=0.3, label="Scores")

با ستون‌های دیتافریم (نیاز به x جداگانه نیست):

plt.bar(df["country"], df["math"], width=0.6, label="Math")

--- نمودار پراکندگی (scatter) ---

plt.scatter(x_data, y_data, color="red", marker="o", s=50, label="Points")

--- هیستوگرام (hist) ---

plt.hist(df["math"], bins=10, color="blue", edgecolor="black")

نکته: برای داده‌های گروه‌بندی‌شده مناسب نیست

--- تنظیمات نمودار ---

plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Chart Title")
plt.legend(loc="best")
plt.show()                            # نمایش نمودار

--- ذخیره نمودار ---

plt.savefig(fname="chart.png", dpi=300)

==============================

۳. اورلپ نمودارهای میله‌ای (Overlapping)

==============================

با تغییر width و color می‌توان چند bar را روی هم انداخت:

plt.bar(df["country"], df["math"], width=0.6, label="Math",
color="brown", edgecolor="black")
plt.bar(df["country"], df["biology"], width=0.4, label="Biology",
color="lightgrey", edgecolor="black")
plt.bar(df["country"], df["physics"], width=0.2, label="Physics",
color="yellow", edgecolor="black")
plt.xlabel("Countries")
plt.ylabel("Scores")
plt.title("Overlapped Bar Chart")
plt.legend(loc="best")
plt.show()

==============================

۴. ترکیب کامل: groupby + نمودار

==============================

مرحله ۱: گروه‌بندی و محاسبه میانگین

num_cols = df.select_dtypes(include="number").columns
grouped = df.groupby("country", as_index=False)[num_cols].mean().round()

مرحله ۲: مرتب‌سازی (برای نمودار منظم)

grouped.sort_values(by="age", ignore_index=True, inplace=True)

مرحله ۳: رسم نمودار ترکیبی (خطی + میله‌ای)

plt.bar(grouped["country"], grouped["chemistry"], color="green",
edgecolor="black", width=0.3, label="Chemistry Mean")
plt.plot(grouped["math"], marker="*", linestyle="--", color="black",
label="Math Mean")
plt.xlabel("Countries")
plt.ylabel("Scores")
plt.title("Grouped Data Chart")
plt.legend(loc="best")
plt.show()

==============================

۵. چرخه کامل تحلیل داده (Data Analysis Pipeline)

==============================

1. خواندن داده

df = pd.read_excel("file.xlsx", sheet_name="data")

2. بررسی اولیه

print(df.info())
print(df.isna().sum())

3. پاکسازی

df.fillna(df.mode().iloc[0], inplace=True)  # پر کردن با پرتکرارترین مقدار

4. گروه‌بندی و خلاصه‌سازی

num_cols = df.select_dtypes(include="number").columns
result = df.groupby("country", as_index=False)[num_cols].mean().round()

5. ترسیم نمودار

plt.bar(result["country"], result["math"])
plt.title("Average Math Score by Country")
plt.show()

6. ذخیره نتایج

result.to_excel("output.xlsx", index=False)
plt.savefig("chart.png", dpi=300)

==============================

خلاصه چک‌لیست

==============================

groupby: df.groupby("col", as_index=False)["target"].mean()

agg:     df.groupby("col").agg({"a": "mean", "b": ["min", "max"]})

plt:     plot (خطی), bar (میله‌ای), scatter (پراکندگی), hist (هیستوگرام)

تنظیمات: xlabel, ylabel, title, legend, savefig

==============================
'''