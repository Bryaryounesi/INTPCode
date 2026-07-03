'''
# ============================================================
# Pandas & Matplotlib - راهنمای مرور سریع (مرتب شده بر اساس موضوع)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# مبحث ۱: ساختارهای پایه (Series و DataFrame)
# ============================================================

# --- Series (آرایه یک‌بعدی با ایندکس) ---
s = pd.Series([30, 32, 13, 40], index=['a', 'b', 'c', 'd'])
s = pd.Series([85, 90, 78], index=["Ali", "Sara", "Reza"])
s = pd.Series(range(10, 20, 3))
s = pd.Series([i for i in range(5, 40, 6) if i % 2 == 1])

# دسترسی و تغییر
print(s["Sara"])
s["Sara"] = 95
print(s + 10)  # عملیات برداری

# --- DataFrame (جدول دوبعدی) ---
# از دیکشنری (هر کلید = یک ستون)
df = pd.DataFrame({
    "name": ["Ali", "Sara", "Reza"],
    "age": [25, 30, 22],
    "score": [85, 90, 78]
})

# از لیست با نام ستون‌ها
df = pd.DataFrame(
    [["ali", 25], ["hadi", 40], ["sima", 34]],
    columns=["name", "age"]
)

# با ایندکس دلخواه
df = pd.DataFrame(
    {"Name": ["Alice", "Bob"], "Age": [25, 30]},
    index=["A1", "B1"]
)

# DataFrame خالی
df = pd.DataFrame(columns=["name", "age", "scores"], index=range(10))

# ============================================================
# مبحث ۲: خواندن و نوشتن فایل
# ============================================================

# --- خواندن CSV ---
df = pd.read_csv("file.csv")
df = pd.read_csv("file.csv", delimiter=";")
df = pd.read_csv("file.csv", index_col="id")

# --- خواندن Excel ---
df = pd.read_excel("file.xlsx")
df = pd.read_excel("file.xlsx", sheet_name="Sales")
df = pd.read_excel("file.xlsx", sheet_name=0)
df_all = pd.read_excel("file.xlsx", sheet_name=None)  # همه شیت‌ها

# پارامترهای مهم read_excel
df = pd.read_excel("file.xlsx", usecols=["Name", "Age"])
df = pd.read_excel("file.xlsx", usecols=range(0, 3))
df = pd.read_excel("file.xlsx", nrows=100)
df = pd.read_excel("file.xlsx", dtype={"Age": int})
df = pd.read_excel("file.xlsx", skiprows=2)

# --- نوشتن ---
df.to_csv("output.csv", index=False)
df.to_excel("output.xlsx", sheet_name="sh1", index=False)

# --- نوشتن چند شیت در یک فایل ---
with pd.ExcelWriter("file.xlsx", mode="a", if_sheet_exists="replace") as writer:
    df1.to_excel(writer, sheet_name="Sh1", index=False)
    df2.to_excel(writer, sheet_name="Sh2", index=False)

# ============================================================
# مبحث ۳: مرور اولیه داده‌ها
# ============================================================

df.head()           # ۵ ردیف اول
df.tail()           # ۵ ردیف آخر
df.shape            # (تعداد ردیف, تعداد ستون)
df.info()           # نوع داده و تعداد مقادیر غیرخالی
df.describe()       # آمار توصیفی ستون‌های عددی
df.columns          # لیست نام ستون‌ها
df.dtypes           # نوع داده هر ستون
df.isnull().sum()   # تعداد NaN در هر ستون (ضروری‌ترین بررسی)

# ============================================================
# مبحث ۴: انتخاب و دسترسی به داده
# ============================================================

# --- ستون‌ها ---
df["age"]                    # یک ستون (Series)
df[["name", "age"]]          # چند ستون (DataFrame)

# --- loc (بر اساس نام ایندکس، بازه بسته) ---
df.loc[0]                    # ردیف با ایندکس 0
df.loc[0:2]                  # ردیف‌های 0 تا 2 (شامل)
df.loc[0:2, "name"]          # ردیف‌های 0 تا 2، فقط ستون name
df.loc[0:2, ["name", "age"]] # ردیف‌های 0 تا 2، ستون‌های مشخص
df.loc[:, "name":]           # همه ردیف‌ها، ستون name تا آخر
df.loc[:, ["id", "name", "gender", "age", "passed"]]  # تغییر ترتیب ستون‌ها

# --- iloc (بر اساس موقعیت عددی، بازه نیمه‌باز) ---
df.iloc[0]                   # ردیف اول
df.iloc[0:3]                 # سه ردیف اول (0 تا 2)
df.iloc[0:3, 0:2]            # سه ردیف اول، دو ستون اول
df.iloc[[0, 2, 5]]           # ردیف‌های خاص با لیست
df.iloc[:5]                  # پنج ردیف اول (معادل head)
df.iloc[-5:]                 # پنج ردیف آخر (معادل tail)
df.iloc[:6, :3]              # ۶ ردیف اول، ۳ ستون اول

# ============================================================
# مبحث ۵: فیلتر شرطی (Boolean Indexing)
# ============================================================

# --- شرط ساده ---
df[df["age"] >= 20]
df[df["name"] == "Ali"]
df[df["city"] != "Tehran"]

# --- شرط روی متن ---
df[df["name"].str.contains("Ali")]        # شامل
df[df["name"].str.startswith("A")]        # شروع با
df[df["name"].str.endswith("i")]          # پایان با

# --- شرط عضویت در لیست ---
df[df["city"].isin(["Tehran", "Shiraz"])]

# --- شرط مقادیر خالی ---
df[df["score"].isna()]                    # تهی‌ها
df[df["score"].notna()]                   # غیرتهی‌ها

# --- ترکیب شرط‌ها با & (and) و | (or) ---
df[(df["age"] > 20) & (df["score"] > 80)]
df[(df["city"] == "Tehran") | (df["city"] == "Shiraz")]
df[~(df["city"] == "Tehran")]                           # NOT
df[~df["city"].isin(["Tehran", "Mashhad"])]             # NOT IN

# --- فیلتر با query() (خوانایی بالاتر) ---
# نکته: رشته‌ها با سینگل‌کوت، نام ستون‌ها بدون کوت
df.query("age > 20 and city == 'Tehran'")
df.query("age.between(40, 50) and country.isin(['Iran', 'Iraq'])")
df.query("country not in ['Iran', 'Iraq']")
df.query("not (age > 40 and math < 14)")
df.query("name.str.startswith('b') or country.isin(['Turkey'])")
df.query("country.str.contains('Ir')")
df.query("score.isna() or country.notna()")

# --- فیلتر با eval() ---
df[df.eval("age > 20 and (city == 'Tehran' or city == 'Shiraz')")]

# ============================================================
# مبحث ۶: مقادیر گمشده (Missing Data)
# ============================================================

# --- تشخیص ---
df.isna().sum()              # تعداد NaN در هر ستون

# --- حذف ---
df.dropna(inplace=True)      # حذف ردیف‌های دارای NaN
df.dropna(axis=1, inplace=True)  # حذف ستون‌های دارای NaN
df.dropna(subset=["date"])   # حذف فقط بر اساس ستون‌های خاص

# --- پر کردن با مقدار ثابت ---
df.fillna(0, inplace=True)
df["name"].fillna("UNKNOWN", inplace=True)

# --- پر کردن با آماره ---
df["age"].fillna(df["age"].mean(), inplace=True)    # میانگین
df["age"].fillna(df["age"].median(), inplace=True)  # میانه
df["name"].fillna(df["name"].mode()[0], inplace=True)  # مد (بیشترین تکرار)

# --- پر کردن دیکشنری‌دار (چند ستون همزمان) ---
df[["math", "biology", "chemistry"]].fillna({
    "math": df["math"].mean(),
    "biology": df["chemistry"].max(),
    "chemistry": df["chemistry"].min()
}, inplace=True)

# --- پر کردن با مقدار قبلی/بعدی ---
df.ffill(inplace=True)   # forward fill
df.bfill(inplace=True)   # backward fill

# --- پر کردن با نمونه‌گیری تصادفی (پیشرفته) ---
for col in df.columns:
    non_null = df[col].dropna(ignore_index=True)
    n_missing = df[col].isna().sum()
    if n_missing > 0 and len(non_null) > 0:
        samples = non_null.sample(n=n_missing, replace=True, random_state=42)
        df.loc[df[col].isna(), col] = samples.values

# ============================================================
# مبحث ۷: تغییر نوع داده‌ها
# ============================================================

# --- بررسی ---
df.info()               # خلاصه کامل با Dtype
df.dtypes               # نوع هر ستون
df["age"].dtype         # نوع یک ستون خاص

# --- تبدیل با astype ---
df["age"] = df["age"].astype(int)
df = df.astype({
    "age": "int",
    "biology": "int",
    "chemistry": "int"
})

# --- تبدیل به datetime ---
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df = pd.read_csv("file.csv", parse_dates=["Date"])  # هنگام خواندن

# --- حذف تاریخ‌های خالی ---
df = df.dropna(subset=["date"])
df["date"].isna().sum()

# ============================================================
# مبحث ۸: تغییر نام، حذف و ریست ایندکس
# ============================================================

# --- تغییر نام ستون ---
df.rename(columns={"old_name": "new_name"}, inplace=True)
df.columns = ["new1", "new2", "new3"]  # تغییر همه ستون‌ها

# --- حذف ستون ---
df.drop("column_name", axis=1, inplace=True)
del df["column_name"]

# --- حذف ردیف ---
df.drop(0, axis=0, inplace=True)
df.drop([3, 5, 7], axis=0, inplace=True)

# --- ریست ایندکس (مهم) ---
df.reset_index(drop=True, inplace=True)  # ایندکس جدید 0 تا n-1

# نکته: drop و reset_index را جدا بنویسید
df.drop([5, 6, 8, 10], axis=0, inplace=True)
df.reset_index(drop=True, inplace=True)

# ============================================================
# مبحث ۹: مرتب‌سازی
# ============================================================

# --- تک‌ستونه ---
df.sort_values(by="age", inplace=True, ignore_index=True)
df.sort_values(by="age", ascending=False, inplace=True)

# --- چندستونه ---
df.sort_values(by=["age", "score"], ascending=[True, False], inplace=True)

# --- ریست ایندکس بعد از مرتب‌سازی ---
df.reset_index(drop=True, inplace=True)

# ============================================================
# مبحث ۱۰: افزودن ستون و ردیف جدید
# ============================================================

# --- افزودن ستون ---
df["double_age"] = df["age"] * 2
df["full_name"] = df["first"] + " " + df["last"]
df["passed"] = df["score"] >= 60  # ستون بولین
df["sum"] = df["math"] + df["chemistry"]
df["remath"] = df["math"] - 20

# --- ستون خالی ---
df["new_col"] = None
df[["new1", "new2"]] = None

# --- ستون با مقدار ثابت ---
df["passed"] = True

# --- افزودن ردیف با loc (بهترین روش) ---
df.loc[len(df)] = [25, "Ali", 180]         # افزودن به انتها
df.loc[4] = [30, "Sara", 165]              # جایگزینی ردیف با ایندکس 4
df.loc[20] = [25, "Ali", 180]              # ساخت ردیف با ایندکس جدید

# --- تغییر یک سلول با iloc ---
df.iloc[5, 2] = "new_value"

# ============================================================
# مبحث ۱۱: توابع آماری
# ============================================================

# --- روی یک ستون ---
df["age"].sum()
df["age"].mean()
df["age"].median()
df["age"].max()
df["age"].min()
df["age"].std()
df["age"].count()        # تعداد مقادیر غیرخالی
df["age"].nunique()      # تعداد مقادیر یکتا
df["age"].mode()         # بیشترین تکرار (خروجی Series)

# --- روی کل DataFrame ---
df.sum()
df.mean()
df.describe()            # خلاصه آماری کامل

# --- روی ردیف‌ها (axis=1) ---
# توجه: در Pandas axis=1 یعنی ردیف‌ها (برعکس NumPy)
df.sum(axis=1)
df.mean(axis=1)

# --- چند تابع با agg ---
df.agg({
    "age": ["max", "sum", "std"],
    "math": ["sum", "std", "min"]
})

# روی همه ستون‌های عددی
num_cols = df.select_dtypes(include="number").drop("id", axis=1)
num_cols.agg(["median", "sum", "nunique"])

# ============================================================
# مبحث ۱۲: groupby (گروه‌بندی و خلاصه‌سازی)
# ============================================================

# --- ساختار کلی ---
# df.groupby(by="col_name", as_index=False)["target_col"].تابع_آماری()

# --- پارامترهای مهم ---
# by: ستون(های) مبنای گروه‌بندی
# as_index: False → ستون گروه‌بندی در خروجی می‌ماند (توصیه می‌شود)
# sort: False → سریع‌تر، ترتیب اصلی حفظ می‌شود

# --- یک ستون ---
df.groupby("country", as_index=False)["math"].mean()
df.groupby("country", as_index=False)["math"].sum()
df.groupby("country", as_index=False)["math"].max()
df.groupby("country", as_index=False)["math"].count()
df.groupby("country").size()  # تعداد کل ردیف‌ها (با NaN)

# --- چند ستون ---
df.groupby("country", as_index=False)[["math", "biology"]].sum()

# --- همه ستون‌های عددی ---
num_cols = df.select_dtypes(include="number").columns
df.groupby("country", as_index=False)[num_cols].mean().round()

# --- حذف یک ستون عددی از محاسبات ---
num_cols = df.select_dtypes(include="number").drop("age", axis=1).columns

# --- agg: چند تابع همزمان ---
df.groupby("country", as_index=False).agg({
    "math": ["mean", "max"],
    "biology": ["min", "median"]
})

# --- با نام‌گذاری دلخواه ---
df.groupby("country", as_index=False).agg(
    math_mean=("math", "mean"),
    bio_max=("biology", "max")
)

# --- مشاهده نام همه گروه‌ها ---
print(grouped.groups.keys())

# --- فیلتر قبل از groupby ---
df.query("math > 9").groupby("country", as_index=False)["math"].mean()

# --- فیلتر بعد از groupby (HAVING) ---
df.groupby("country", as_index=False)["math"].mean().query("math > 15")

# --- محاسبه درصد مقادیر گمشده هر ستون ---
for col in df.columns:
    pct_missing = df[col].isna().sum() / len(df[col])
    print(f"{col}: {pct_missing:.1%}")

# --- محاسبه درصد تکرار مقادیر (برای انتخاب ستون groupby مناسب) ---
for col in df.select_dtypes(exclude="number").columns:
    pct_unique = 1 - (df[col].nunique() / len(df[col]))
    print(f"{col} repeat%: {pct_unique:.1%}")

# --- گروه‌بندی زمانی با dt ---
df["date"] = pd.to_datetime(df["date"])
df.groupby(df["date"].dt.year).size()             # سالانه
df.groupby(df["date"].dt.month).size()            # ماهانه
df.groupby([df["date"].dt.year, df["date"].dt.month]).size()  # ترکیب سال و ماه
df.groupby(df["date"].dt.month)["sales"].sum()

# --- گروه‌بندی زمانی با resample (حرفه‌ای) ---
# 1. تبدیل به datetime
df["Date"] = pd.to_datetime(df["Date"])
# 2. حذف مقادیر خالی
df = df.dropna(subset=["Date"])
# 3. مرتب‌سازی
df = df.sort_values(by="Date")
# 4. set_index + resample
df.set_index("Date").resample("M").size()
df.set_index("Date").resample("M")["Volume"].sum()
df.set_index("Date").resample("YE")["Volume"].sum()

# ============================================================
# مبحث ۱۳: ترکیب داده‌ها (concat و merge)
# ============================================================

# --- concat: اتصال ساده ---
# اتصال عمودی (ردیف‌ها زیر هم)
df_combined = pd.concat([df1, df2], axis=0, ignore_index=True)

# اتصال افقی (ستون‌ها کنار هم)
df_combined = pd.concat([df1, df2], axis=1)

# حذف ردیف‌های تکراری بعد از ترکیب
df.drop_duplicates(inplace=True, ignore_index=True)
df.drop_duplicates(subset=["name", "age"], inplace=True)

# --- join: الحاق افقی با مدیریت ستون‌های تکراری ---
joined = df1.join(df2)  # اگر ستون یکسان نداشته باشیم
joined = df1.join(df2, lsuffix="left", rsuffix="right")  # با پسوند

# --- merge: مشابه SQL JOIN ---
# ساختار کلی: pd.merge(left, right, how='inner', on='column_name')

df_inner = pd.merge(df1, df2, how="inner", on="id")   # فقط مقادیر مشترک
df_left  = pd.merge(df1, df2, how="left", on="id")    # همه df1 + تطابق df2
df_right = pd.merge(df1, df2, how="right", on="id")   # همه df2 + تطابق df1
df_outer = pd.merge(df1, df2, how="outer", on="id")   # همه ردیف‌های هر دو

# --- merge با نام ستون‌های متفاوت ---
pd.merge(df1, df2, left_on="id", right_on="student_id")

# --- merge روی چند ستون ---
pd.merge(df1, df2, on=["name", "age", "country"])

# ============================================================
# مبحث ۱۴: ساخت داده‌های آزمایشی با Faker
# ============================================================

from faker import Faker
import random

# --- تنظیم seed برای ثابت ماندن داده‌ها ---
random.seed(6)
Faker.seed(6)

# --- ساخت شیء Faker ---
fake = Faker()
fake = Faker('fa_IR')  # برای داده‌های فارسی

# --- توابع پرکاربرد Faker ---
fake.name()              # نام کامل
fake.first_name()        # نام کوچک
fake.country()           # کشور
fake.city()              # شهر
fake.email()             # ایمیل
fake.phone_number()      # شماره تلفن
fake.job()               # شغل
fake.random_int(min=, max=)  # عدد تصادفی
fake.date()              # تاریخ

# --- random.choices (برای داده‌های محدود با وزن) ---
gender = random.choices(["M", "F", None], weights=[0.8, 0.1, 0.1], k=80)

# --- الگوی کامل ساخت DataFrame با Faker ---
random.seed(6)
Faker.seed(6)
fake = Faker()

data = [{
    "name": fake.first_name(),
    "country": fake.country() if random.random() < 0.8 else None,  # 20% NaN
    "age": fake.random_int(min=16, max=65) if random.random() < 0.9 else None
} for _ in range(70)]

df = pd.DataFrame(data)

# --- افزودن ستون جدید با Faker ---
df["phone"] = [fake.phone_number() for _ in range(len(df))]

# ============================================================
# مبحث ۱۵: رسم نمودار با Matplotlib
# ============================================================

# --- نمودار خطی (plot) ---
plt.plot(df["age"], df["math"], marker="*", color="black",
         linestyle="--", label="Math Scores")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Chart Title")
plt.legend(loc="best")
plt.grid(True)
plt.show()
plt.savefig("chart.png", dpi=300)

# --- نمودار میله‌ای (bar) ---
plt.bar(df["country"], df["math"], width=0.6, label="Math",
        color="brown", edgecolor="black")
plt.bar(df["country"], df["biology"], width=0.4, label="Biology",
        color="lightgrey", edgecolor="black")

# --- نمودار پراکندگی (scatter) ---
plt.scatter(df["age"], df["math"], color="red", marker="o", s=50)

# --- هیستوگرام (hist) ---
plt.hist(df["math"], bins=10, color="blue", edgecolor="black")

# --- subplots با Pandas ---
fig, axs = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
df["math"].plot(kind="hist", ax=axs[0], title="Math Distribution", edgecolor="black")
df["gender"].value_counts().plot(kind="bar", ax=axs[1], title="Gender", edgecolor="black")
plt.show()

# --- رسم مستقیم از Pandas ---
df.plot(kind="hist", y="math", bins=10, edgecolor="black")
df["gender"].value_counts().plot(kind="bar", edgecolor="black")
df.plot(kind="scatter", x="age", y="score")
df.plot(kind="box", y="math")

# --- اورلپ نمودارهای میله‌ای با Pandas ---
df[["math", "biology", "chemistry", "age"]].plot(
    kind="bar", x="age", edgecolor="black",
    ylabel="scores", title="Students Score by Age Chart"
)
plt.show()

# --- ترکیب: groupby + نمودار ---
num_cols = df.select_dtypes(include="number").columns
grouped = df.groupby("country", as_index=False)[num_cols].mean().round()
grouped.sort_values(by="age", ignore_index=True, inplace=True)

plt.bar(grouped["country"], grouped["chemistry"], color="green",
        edgecolor="black", width=0.3, label="Chemistry Mean")
plt.plot(grouped["math"], marker="*", linestyle="--", color="black",
         label="Math Mean")
plt.xlabel("Countries")
plt.ylabel("Scores")
plt.title("Grouped Data Chart")
plt.legend(loc="best")
plt.show()

# ============================================================
# مبحث ۱۶: چرخه کامل تحلیل داده (Data Analysis Pipeline)
# ============================================================

# 1. خواندن داده
df = pd.read_excel("file.xlsx", sheet_name="data")

# 2. بررسی اولیه
print(df.info())
print(df.isna().sum())

# 3. پاکسازی
df.fillna(df.mode().iloc[0], inplace=True)
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].round().astype(int)

# 4. گروه‌بندی و خلاصه‌سازی
num_cols = df.select_dtypes(include="number").columns
result = df.groupby("country", as_index=False)[num_cols].mean().round()

# 5. ترسیم نمودار
plt.bar(result["country"], result["math"])
plt.title("Average Math Score by Country")
plt.show()

# 6. ذخیره نتایج
result.to_excel("output.xlsx", index=False)
plt.savefig("chart.png", dpi=300)

# ============================================================
# توضیحات اضافه فایل اصلی
# ============================================================

"""
توضیحات اضافه فایل اصلی - بخش ۱: تفاوت loc و iloc

📍 loc: با نام ایندکس کار می‌کند، بازه شامل انتهاست
📍 iloc: با موقعیت عددی کار می‌کند، بازه شامل انتها نیست (مثل لیست)

مثال مقایسه:
df.loc[0:2]   → ردیف‌های 0، 1، 2 (۳ ردیف)
df.iloc[0:2]  → ردیف‌های 0، 1 (۲ ردیف)
"""

"""
توضیحات اضافه فایل اصلی - بخش ۲: axis در Pandas vs NumPy

📍 در Pandas: axis=0 → ردیف‌ها | axis=1 → ستون‌ها
📍 در NumPy:  axis=0 → ستون‌ها | axis=1 → ردیف‌ها

⚠️ این دو برعکس هم عمل می‌کنند!

مثال:
df.sum(axis=1)   # مجموع هر ردیف در Pandas
np.sum(m, axis=1) # مجموع هر ردیف در NumPy (اینجا یکی شد!)
"""

"""
توضیحات اضافه فایل اصلی - بخش ۳: کار نکردن query روی DataFrameهای MultiIndex

اگر بعد از groupby با agg چند تابع، DataFrame MultiIndex شود، query کار نمی‌کند.

مثال:
grouped = df.groupby("country", as_index=False)[num_cols].agg(["mean", "max"])
grouped.query("country == 'Iran'")  # ❌ ارور می‌دهد

راه حل:
grouped[grouped["country"] == "Iran"]  # ✅ کار می‌کند
"""

"""
توضیحات اضافه فایل اصلی - بخش ۴: نکات مهم در groupby

1. as_index=False: ستون گروه‌بندی در خروجی می‌ماند (توصیه می‌شود)
2. sort=False: سریع‌تر، ترتیب اصلی حفظ می‌شود
3. groupby().size(): تعداد کل ردیف‌ها (با NaN) را محاسبه می‌کند
4. groupby()["col"].count(): تعداد مقادیر غیرخالی را محاسبه می‌کند
"""

"""
توضیحات اضافه فایل اصلی - بخش ۵: گروه‌بندی زمانی با resample

مراحل:
1. تبدیل ستون به datetime: pd.to_datetime()
2. حذف مقادیر خالی: dropna(subset=["date"])
3. مرتب‌سازی: sort_values(by="date")
4. set_index() + resample()

فرمت‌های رایج:
"M"  → ماهانه
"YE" → سالانه
"W"  → هفتگی
"H"  → ساعتی
"""

"""
توضیحات اضافه فایل اصلی - بخش ۶: پارامترهای مهم read_csv/read_excel

usecols    → انتخاب ستون‌های خاص
nrows      → تعداد ردیف محدود
dtype      → تعیین نوع داده ستون‌ها
skiprows   → رد کردن n ردیف اول
index_col  → ستون ایندکس
parse_dates → تبدیل خودکار به datetime
na_values  → مقادیر سفارشی معادل NaN
"""

# ============================================================
# مثال‌های اضافه فایل اصلی
# ============================================================

"""
مثال اضافه فایل اصلی - ۱: پاکسازی جداگانه ستون‌های عددی و غیرعددی

# جداسازی
unnumcols = df.select_dtypes(exclude="number")
numcols = df.select_dtypes(include="number").drop("id", axis=1)

# پر کردن غیرعددی با bfill
unnumcols.bfill(inplace=True)

# پر کردن عددی با مقادیر مختلف
numcols.fillna({
    "age": numcols["age"].sum(),
    "math": numcols["math"].max(),
    "biology": numcols["biology"].mean(),
    "chemistry": numcols["chemistry"].min()
}, inplace=True)

# جایگزینی در دیتافریم اصلی
df[numcols.columns] = numcols.round().astype(int)
df[unnumcols.columns] = unnumcols
"""

"""
مثال اضافه فایل اصلی - ۲: ساخت DataFrame خالی و پر کردن آن

cols = ['name', 'gender', 'country']
rows = pd.Series(range(30))
df = pd.DataFrame(columns=cols, index=rows.index)

# پر کردن با Series (با reindex)
s_name = pd.Series(['ali', 'jalal', 'shamal', 'soren'])
df['name'] = s_name.reindex(df.index)

# پر کردن با نمونه‌گیری
s_name_comp = s_name.sample(n=30, replace=True, ignore_index=True)
df = df.assign(name=s_name_comp)

# پاکسازی نهایی
df.dropna(inplace=True)
df.reset_index(drop=True, inplace=True)
"""

"""
مثال اضافه فایل اصلی - ۳: نوشتن چند شیت در Excel با ExcelWriter

with pd.ExcelWriter("file.xlsx", mode="a", if_sheet_exists="replace") as writer:
    df1.to_excel(writer, sheet_name="Sh1", index=False)
    df2.to_excel(writer, sheet_name="Sh2", index=False)

پارامتر if_sheet_exists:
"error"   : خطا اگر شیت وجود داشته باشد
"replace" : جایگزینی شیت موجود
"new"     : ساخت شیت با نام جدید
"""

"""
مثال اضافه فایل اصلی - ۴: کار نکردن query روی groupby شده

# ❌ این کار نمی‌کند:
grouped = df.groupby("country", as_index=False)[num_cols].agg(["mean", "max"])
grouped.query("country == 'Iran'")

# ✅ این کار می‌کند:
grouped[grouped["country"] == "Iran"]

# راه حل دیگر: فیلتر قبل از groupby
df.query("math > 9").groupby("country", as_index=False)["math"].mean()
"""

"""
مثال اضافه فایل اصلی - ۵: اورلپ نمودارهای میله‌ای با Matplotlib

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
"""

# ============================================================
# چک‌لیست نهایی Pandas
# ============================================================

print("\n" + "="*60)
print("چک‌لیست نهایی Pandas:")
print("="*60)
print("""
1. ساختار: Series, DataFrame
2. خواندن/نوشتن: read_csv, read_excel, to_csv, to_excel
3. مرور: head(), info(), describe(), isnull().sum()
4. انتخاب: df["col"], df.loc[], df.iloc[]
5. فیلتر: شرط‌های &, |, ~ و query()
6. مقادیر گمشده: dropna(), fillna()
7. تغییر نوع: astype(), pd.to_datetime()
8. تغییر نام/حذف: rename(), drop()
9. مرتب‌سازی: sort_values()
10. آمار: mean(), sum(), agg()
11. groupby: groupby().mean(), agg()
12. ترکیب: concat(), merge()
13. رسم: plot, bar, scatter, hist, subplot
14. Faker: ساخت داده‌های آزمایشی
""")

# ============================================================
# نکات کلیدی و تفاوت‌ها
# ============================================================

print("\n" + "="*60)
print("نکات کلیدی:")
print("="*60)
print("""
1. axis در Pandas: axis=0 → ردیف‌ها | axis=1 → ستون‌ها (برعکس NumPy!)
2. loc: با نام ایندکس، بازه بسته (شامل انتها)
3. iloc: با موقعیت عددی، بازه نیمه‌باز (شامل انتها نیست)
4. groupby: as_index=False برای حفظ ستون گروه‌بندی در خروجی
5. query: خوانایی بهتر برای شرط‌های پیچیده
6. fillna دیکشنری‌دار: برای پر کردن همزمان چند ستون با مقادیر مختلف
7. resample: گروه‌بندی حرفه‌ای داده‌های زمانی
8. merge: ترکیب مانند SQL (inner, left, right, outer)
""")

# ============================================================
# پایان راهنمای مرور سریع Pandas & Matplotlib
# ============================================================
'''