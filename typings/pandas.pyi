from typing import Any, Tuple, List
import numpy as np

# ============================================================
# Series
# ============================================================
def Series(data: Any = ..., index: Any = ..., dtype: Any = ..., name: Any = ..., copy: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    s = pd.Series(data)

    📌 پارامترها:
    - data: لیستی از مقادیر عددی یا غیر عددی
    - index (اختیاری): لیستی از ایندکس‌ها — پیش‌فرض: عددی از 0
    - dtype (اختیاری): نوع داده — پیش‌فرض: خودکار تشخیص می‌دهد
    - name (اختیاری): نام سری
    - copy (اختیاری): پیش‌فرض False — اگر True، یک کپی از داده‌ها می‌سازد

    📌 نکته:
    s.values ← آرایه NumPy
    s.values.tolist() ← لیست پایتونی
    s.index ← ایندکس‌ها
    """
    ...

# ============================================================
# DataFrame
# ============================================================
def DataFrame(data: Any = ..., index: Any = ..., columns: Any = ..., dtype: Any = ..., copy: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df = pd.DataFrame(data)

    📌 پارامترها:
    - data: dict، list، numpy array، Series یا DataFrame دیگر — پیش‌فرض None
    - index (اختیاری): برچسب ردیف‌ها — پیش‌فرض: عددی از 0
    - columns (اختیاری): نام ستون‌ها — پیش‌فرض: از کلیدهای dict استفاده می‌کند
    - dtype (اختیاری): نوع داده — پیش‌فرض: خودکار
    - copy (اختیاری): پیش‌فرض False

    📌 نکات مفید:
    df.columns.tolist() ← نام ستون‌ها
    df[col_name] ← محتوای یک ستون (Series)
    df[col_name].tolist() ← محتوای یک ستون (لیست)
    """
    ...

# ============================================================
# select_dtypes
# ============================================================
def select_dtypes(include: Any = ..., exclude: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df_num = df.select_dtypes(include="number")
    df_nonnum = df.select_dtypes(exclude="number")

    📌 پارامترها:
    - include: نوع داده‌هایی که می‌خواهی — "number", "object", "string"
    - exclude: نوع داده‌هایی که نمی‌خواهی

    📌 نکته:
    numcols = df.select_dtypes(include="number").columns ← لیست ستون‌های عددی
    """
    ...

# ============================================================
# fillna
# ============================================================
def fillna(value: Any = ..., method: Any = ..., axis: int = ..., inplace: bool = ..., limit: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df.fillna(value, inplace=True)

    📌 پارامترها:
    - value: مقدار جایگزین — عدد، dict، Series
    - method (اختیاری): 'ffill', 'bfill'
    - axis (اختیاری): 0 برای ردیف‌ها (پیش‌فرض) | 1 برای ستون‌ها
    - inplace (اختیاری): پیش‌فرض False — True یعنی روی خود df اعمال شود
    - limit (اختیاری): حداکثر تعداد پر کردن در هر ستون

    📌 نکات طلایی:
    # پرکردن ستون‌های عددی با میانه:
    df.fillna(df.median(numeric_only=True), inplace=True)

    # پرکردن ستون‌های رشته‌ای با پرتکرارترین:
    df.fillna(df.select_dtypes(include=["string","object"]).mode().iloc[0], inplace=True)
    """
    ...

# ============================================================
# bfill / ffill
# ============================================================
def bfill(axis: int = ..., inplace: bool = ..., limit: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df.bfill()

    📌 پارامترها:
    - axis (اختیاری): 0 (پیش‌فرض)
    - inplace (اختیاری): پیش‌فرض False
    - limit (اختیاری): حداکثر تعداد پر کردن

    📌 کاربرد: جایگزین df.fillna(method='bfill') — نسخه جدیدتر
    """
    ...

def ffill(axis: int = ..., inplace: bool = ..., limit: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df.ffill()

    📌 پارامترها:
    - axis (اختیاری): 0 (پیش‌فرض)
    - inplace (اختیاری): پیش‌فرض False
    - limit (اختیاری): حداکثر تعداد پر کردن

    📌 کاربرد: جایگزین df.fillna(method='ffill') — نسخه جدیدتر
    """
    ...

# ============================================================
# dropna
# ============================================================
def dropna(axis: int = ..., how: str = ..., thresh: Any = ..., subset: Any = ..., inplace: bool = ..., ignore_index: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.dropna(ignore_index=True, inplace=True)                     ← حذف ردیف‌ها
    df["col_name"].dropna(ignore_index=True)                       ← حذف سلول‌های خالی یک ستون

    📌 پارامترها:
    - axis (اختیاری): 0 = حذف ردیف (پیش‌فرض) | 1 = حذف ستون
    - how (اختیاری): 'any' = با یک NaN حذف شود (پیش‌فرض) | 'all' = همه NaN باشند حذف شود
    - thresh (اختیاری): حداقل تعداد غیرNaN برای زنده ماندن
    - subset (اختیاری): لیست ستون‌ها برای بررسی
    - inplace (اختیاری): پیش‌فرض False
    - ignore_index: پیش‌فرض False — بهتر True برای بازنشانی ایندکس
    """
    ...

# ============================================================
# drop
# ============================================================
def drop(labels: Any = ..., axis: int = ..., index: Any = ..., columns: Any = ..., inplace: bool = ..., ignore_index: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.drop("col_name", axis=1, inplace=True)                      ← حذف ستون
    df.drop(["col1","col2"], axis=1, inplace=True)                 ← حذف چند ستون
    df.drop(row_index, axis=0, inplace=True)                       ← حذف ردیف

    📌 پارامترها:
    - labels: نام ستون/ردیف یا لیست آن‌ها
    - axis: 1 = ستون | 0 = ردیف (پیش‌فرض)
    - inplace: پیش‌فرض False — بهتر True
    - ignore_index: پیش‌فرض False
    """
    ...

# ============================================================
# read_csv
# ============================================================
def read_csv(filepath_or_buffer: Any, index_col: Any = ..., usecols: Any = ..., nrows: Any = ..., dtype: Any = ..., skiprows: Any = ..., parse_dates: Any = ..., na_values: Any = ..., na_filter: bool = ..., converters: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df = pd.read_csv(path)

    📌 پارامترها:
    - filepath: مسیر فایل CSV
    - index_col (اختیاری): ستون ایندکس — None (پیش‌فرض)
    - usecols (اختیاری): انتخاب ستون‌های خاص
    - nrows (اختیاری): تعداد ردیف محدود
    - dtype (اختیاری): تعیین نوع داده ستون‌ها
    - skiprows (اختیاری): رد کردن n ردیف اول
    - parse_dates (اختیاری): مثلاً ["Date"] برای تبدیل خودکار به datetime
    - na_values (اختیاری): مقادیر معادل NaN (مثلاً 0)
    - na_filter: پیش‌فرض True — تبدیل مقادیر خالی به NaN
    - converters (اختیاری): اعمال تابع روی ستون هنگام خواندن

    📌 برمی‌گردونه: DataFrame
    """
    ...

# ============================================================
# read_excel / ExcelFile
# ============================================================
def ExcelFile(path_or_buffer: Any) -> Any:
    """
    📌 فرمول رایج:
    excel_file = pd.ExcelFile(path)

    📌 نکته:
    excel_file.sheet_names ← اسامی شیت‌ها

    📌 برمی‌گردونه: شیء ExcelFile
    """
    ...

def read_excel(io: Any, sheet_name: Any = ..., usecols: Any = ..., nrows: Any = ..., index_col: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df = pd.read_excel(path, sheet_name=0)
    df = pd.read_excel(path, sheet_name="Sheet1")
    df_all = pd.read_excel(path, sheet_name=None)    ← همه شیت‌ها در یک dict

    📌 پارامترها:
    - io: مسیر فایل اکسل
    - sheet_name: 0 یا "Sheet1" یا None (همه شیت‌ها)
    - usecols (اختیاری): انتخاب ستون‌ها
    - nrows (اختیاری): تعداد ردیف
    - index_col (اختیاری): ستون ایندکس

    📌 برمی‌گردونه: DataFrame (یا dict در صورت sheet_name=None)
    """
    ...

# ============================================================
# reset_index
# ============================================================
def reset_index(drop: bool = ..., inplace: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.reset_index(drop=True)              ← حذف کامل ستون ایندکس
    df.reset_index(inplace=True)           ← تبدیل ایندکس به ستون عادی

    📌 پارامترها:
    - drop: پیش‌فرض False — True یعنی ایندکس حذف شود نه تبدیل به ستون
    - inplace: پیش‌فرض False
    """
    ...

# ============================================================
# sample
# ============================================================
def sample(n: Any = ..., frac: Any = ..., replace: bool = ..., weights: Any = ..., random_state: Any = ..., ignore_index: bool = ..., axis: int = ...) -> Any:
    """
    📌 فرمول رایج:
    df.sample(frac=1, ignore_index=True, random_state=1)

    📌 پارامترها:
    - n: تعداد ردیف — اگر دادی، frac نده
    - frac: نسبت درصدی — 1 یعنی ۱۰۰٪ | 0.2 یعنی ۲۰٪
    - replace (اختیاری): پیش‌فرض False — True یعنی نمونه‌گیری با جایگذاری
    - weights (اختیاری): احتمال انتخاب هر ردیف
    - random_state: عدد ثابت برای تکرارپذیری (مثل seed)
    - ignore_index: پیش‌فرض False — بهتر True
    - axis (اختیاری): 0 = ردیف (پیش‌فرض)
    """
    ...

# ============================================================
# sort_values
# ============================================================
def sort_values(by: Any, axis: int = ..., ascending: bool = ..., inplace: bool = ..., ignore_index: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.sort_values(by="col_name", ignore_index=True, inplace=True)

    📌 پارامترها:
    - by: نام ستون یا لیست ستون‌ها
    - axis (اختیاری): 0 (پیش‌فرض) — 1 خطا می‌دهد
    - ascending: پیش‌فرض True (صعودی) | False (نزولی)
    - inplace: پیش‌فرض False — بهتر True
    - ignore_index: پیش‌فرض False — بهتر True
    """
    ...

# ============================================================
# to_excel / ExcelWriter
# ============================================================
def to_excel(excel_writer: Any, sheet_name: str = ..., index: bool = ...) -> None:
    """
    📌 فرمول رایج:
    df.to_excel(path, sheet_name="sh1", index=False)

    📌 پارامترها:
    - excel_writer: مسیر فایل خروجی
    - sheet_name: پیش‌فرض 'Sheet1'
    - index: پیش‌فرض True — بهتر False
    """
    ...

def ExcelWriter(path: Any, mode: str = ..., if_sheet_exists: str = ...) -> Any:
    """
    📌 فرمول رایج:
    with pd.ExcelWriter(path, mode='a', if_sheet_exists='new') as writer:
        df1.to_excel(writer, sheet_name="sh1", index=False)
        df2.to_excel(writer, sheet_name="sh2", index=False)

    📌 پارامترها:
    - path: مسیر فایل خروجی
    - mode: 'a' برای اضافه کردن به فایل موجود
    - if_sheet_exists: 'new' (بهتر) | 'replace' | 'error'
    """
    ...

# ============================================================
# concat
# ============================================================
def concat(objs: Any, axis: int = ..., ignore_index: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    pd.concat([df1, df2], ignore_index=True)           ← اتصال عمودی
    pd.concat([df1, df2], axis=1)                      ← اتصال افقی

    📌 پارامترها:
    - objs: لیست یا دیکشنری DataFrame ها
    - axis: 0 = عمودی (پیش‌فرض) | 1 = افقی
    - ignore_index: پیش‌فرض False — True = بازنشانی ایندکس (برای عمودی لازم)

    📌 نکته: برای اتصال افقی ignore_index نده (نام ستون‌ها عددی می‌شود)
    """
    ...

# ============================================================
# merge
# ============================================================
def merge(left: Any, right: Any, how: str = ..., on: Any = ..., left_on: Any = ..., right_on: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    dfm = pd.merge(left_df, right_df, how="outer", on="col_name")

    📌 پارامترها:
    - left: دیتافریم چپ
    - right: دیتافریم راست
    - how: 'outer' (بهتر) | 'inner' | 'left' | 'right'
    - on: نام ستون مشترک
    - left_on (اختیاری): نام ستون مشترک در دیتافریم چپ (اگر نام‌ها متفاوت)
    - right_on (اختیاری): نام ستون مشترک در دیتافریم راست (اگر نام‌ها متفاوت)
    """
    ...

# ============================================================
# groupby
# ============================================================
def groupby(by: Any, axis: int = ..., sort: bool = ..., as_index: bool = ..., dropna: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.groupby(by="col_name", as_index=False)[numcols].mean()
    df.groupby(by="col_name", as_index=False)[numcols].agg(["mean","max"])
    df.groupby(by="col_name", as_index=False).agg({"col1":["mean"], "col2":["min","max"]})

    📌 پارامترها:
    - by: نام ستون یا لیست ستون‌ها
    - axis (اختیاری): 0 (پیش‌فرض)
    - sort: پیش‌فرض True — False = سریع‌تر
    - as_index: پیش‌فرض True — False بهتر (ستون گروه‌بندی را در خروجی نگه می‌دارد)
    - dropna: پیش‌فرض True — False = گروه‌های NaN هم نگه داشته شوند

    📌 نکته: بعد از groupby حتماً تابع آماری (mean, sum, max, ...) را فراخوانی کن
    """
    ...

# ============================================================
# value_counts
# ============================================================
def value_counts(normalize: bool = ..., sort: bool = ..., ascending: bool = ..., dropna: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df["col_name"].value_counts()

    📌 پارامترها:
    - normalize: پیش‌فرض False — True = فراوانی نسبی
    - sort: پیش‌فرض True
    - ascending: پیش‌فرض False
    - dropna: پیش‌فرض True

    📌 نکته: روی Series اجرا می‌شود، خروجی Series است
    """
    ...

# ============================================================
# iloc
# ============================================================
def iloc(row_index: Any, col_index: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df.iloc[row_index]                 ← یک ردیف
    df.iloc[start:end]                 ← رنج ردیف‌ها
    df.iloc[:, col_index]              ← یک ستون
    df.iloc[:, start:end]              ← رنج ستون‌ها
    df.iloc[start:end, start2:end2]    ← رنج ردیف و ستون
    df.iloc[row_index, col_index]      ← یک عنصر
    """
    ...

# ============================================================
# توابع تحلیل داده
# ============================================================
def isnull() -> Any:
    """
    📌 فرمول رایج:
    df.isnull().sum()    ← تعداد مقادیر خالی در هر ستون
    """
    ...

def duplicated(subset: Any = ..., keep: str = ...) -> Any:
    """
    📌 فرمول رایج:
    df.duplicated().sum()    ← تعداد ردیف‌های تکراری
    """
    ...

def drop_duplicates(subset: Any = ..., keep: str = ..., inplace: bool = ..., ignore_index: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.drop_duplicates(inplace=True)
    """
    ...

def describe(percentiles: Any = ..., include: Any = ..., exclude: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df.describe()    ← خلاصه آماری ستون‌های عددی
    """
    ...

def info(verbose: Any = ..., buf: Any = ..., memory_usage: Any = ..., show_counts: Any = ...) -> None:
    """
    📌 فرمول رایج:
    df.info()    ← اطلاعات کلی DataFrame
    """
    ...

def head(n: int = ...) -> Any:
    """
    📌 فرمول رایج:
    df.head()     ← ۵ ردیف اول
    df.head(10)   ← ۱۰ ردیف اول
    """
    ...

def tail(n: int = ...) -> Any:
    """
    📌 فرمول رایج:
    df.tail()     ← ۵ ردیف آخر
    df.tail(10)   ← ۱۰ ردیف آخر
    """
    ...

def shape() -> Tuple[int, int]:
    """
    📌 فرمول رایج:
    df.shape    ← (تعداد ردیف, تعداد ستون)
    """
    ...

def columns() -> Any:
    """
    📌 فرمول رایج:
    df.columns.tolist()    ← لیست نام ستون‌ها
    """
    ...

# ============================================================
# توابع آماری — روی Series و DataFrame
# ============================================================
def min() -> Any:
    """📌 فرمول رایج: df["col"].min() — کمترین مقدار"""
    ...

def max() -> Any:
    """📌 فرمول رایج: df["col"].max() — بیشترین مقدار"""
    ...

def mean() -> Any:
    """📌 فرمول رایج: df["col"].mean() — میانگین"""
    ...

def median() -> Any:
    """📌 فرمول رایج: df["col"].median() — میانه"""
    ...

def mode() -> Any:
    """📌 فرمول رایج: df["col"].mode() — مُد (پرتکرارترین مقدار)"""
    ...

def std() -> Any:
    """📌 فرمول رایج: df["col"].std() — انحراف معیار"""
    ...

def var() -> Any:
    """📌 فرمول رایج: df["col"].var() — واریانس"""
    ...

def sum() -> Any:
    """📌 فرمول رایج: df["col"].sum() — مجموع"""
    ...

def count() -> Any:
    """
    📌 فرمول رایج: df["col"].count() — تعداد مقادیر غیرخالی

    📌 تفاوت با size():
    count() = فقط مقادیر غیرخالی
    size()  = همه ردیف‌ها (حتی NaN)
    """
    ...

def nunique() -> Any:
    """📌 فرمول رایج: df["label"].nunique() — تعداد مقادیر یکتا"""
    ...

def skew() -> Any:
    """
    📌 فرمول رایج:
    df["col"].skew()

    📌 تفسیر:
    نزدیک ۰ = متقارن | مثبت = دم راست بلند | منفی = دم چپ بلند
    """
    ...

def hist() -> Any:
    """📌 فرمول رایج: df["col"].hist() — رسم هیستوگرام"""
    ...

# ============================================================
# متدهای زنجیره‌ای — بعد از توابع اصلی استفاده می‌شوند
# ============================================================

def round(n: int = ...) -> Any:
    """
    📌 فرمول رایج:
    df.mean().round(2)           ← گرد کردن به ۲ رقم اعشار
    df.groupby().mean().round()  ← گرد کردن خروجی groupby

    📌 پارامترها:
    - n: تعداد ارقام اعشار — پیش‌فرض 0
    """
    ...

def astype(dtype: Any) -> Any:
    """
    📌 فرمول رایج:
    df.mean().astype(int)                          ← تبدیل به عدد صحیح
    df.astype({"age": "int", "score": "float"})    ← تبدیل چند ستون

    📌 پارامترها:
    - dtype: نوع داده — "int", "float", "str" | یا دیکشنری برای چند ستون
    """
    ...

def rename(columns: Any = ..., index: Any = ..., inplace: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    df.rename(columns={'old_name': 'new_name'})
    df.rename(columns={'col1': 'name1', 'col2': 'name2'}, inplace=True)

    📌 پارامترها:
    - columns: دیکشنری نگاشت نام قدیم به جدید
    - index: دیکشنری نگاشت ایندکس قدیم به جدید
    - inplace: پیش‌فرض False
    """
    ...

def to_list() -> List:
    """
    📌 فرمول رایج:
    df['col'].to_list()        ← تبدیل یک ستون به لیست
    df['col'].values.tolist()  ← روش معادل
    """
    ...

def to_numpy() -> Any:
    """
    📌 فرمول رایج:
    df['col'].to_numpy()    ← تبدیل به آرایه NumPy
    df.to_numpy()           ← تبدیل کل DataFrame
    """
    ...

def to_dict() -> dict:
    """
    📌 فرمول رایج:
    df.to_dict()    ← تبدیل DataFrame به دیکشنری
    """
    ...

def to_csv(path: Any, index: bool = ...) -> None:
    """
    📌 فرمول رایج:
    df.to_csv('output.csv', index=False)

    📌 پارامترها:
    - path: مسیر فایل خروجی
    - index: پیش‌فرض True — بهتر False
    """
    ...

def isin(values: Any) -> Any:
    """
    📌 فرمول رایج:
    df[df['col'].isin(['Tehran', 'Shiraz'])]   ← فیلتر با لیست
    df['col'].isin([1, 2, 3])                  ← True/False برای هر ردیف
    """
    ...

def nlargest(n: int, columns: Any) -> Any:
    """
    📌 فرمول رایج:
    df.nlargest(5, 'score')         ← ۵ بزرگترین بر اساس score
    df.nlargest(3, ['math', 'bio']) ← ۳ بزرگترین بر اساس چند ستون

    📌 پارامترها:
    - n: تعداد ردیف
    - columns: نام ستون یا لیست ستون‌ها
    """
    ...

def nsmallest(n: int, columns: Any) -> Any:
    """
    📌 فرمول رایج:
    df.nsmallest(3, 'price')    ← ۳ کوچکترین بر اساس price

    📌 پارامترها:
    - n: تعداد ردیف
    - columns: نام ستون یا لیست ستون‌ها
    """
    ...

def size() -> Any:
    """
    📌 فرمول رایج:
    df.groupby("country").size()    ← تعداد کل ردیف‌ها در هر گروه (شامل NaN)

    📌 تفاوت با count():
    size()  = همه ردیف‌ها (حتی NaN)
    count() = فقط مقادیر غیرخالی
    """
    ...

def plot(kind: str = ..., x: Any = ..., y: Any = ..., title: str = ..., xlabel: str = ..., ylabel: str = ..., color: str = ..., figsize: Any = ..., ax: Any = ..., subplots: bool = ..., layout: Any = ..., rot: int = ..., **kwargs: Any) -> Any:
    """
    📌 فرمول رایج:
    df.plot(kind="bar")                                     ← نمودار میله‌ای
    df.plot(kind="line", x="col1", y="col2")                ← نمودار خطی
    df.plot(kind="scatter", x="math", y="biology")          ← نمودار پراکندگی
    df.plot(kind="hist", bins=10)                           ← هیستوگرام
    df.plot(kind="box")                                     ← نمودار جعبه‌ای
    df["col"].value_counts().plot(kind="pie", autopct="%1.1f%%")  ← دایره‌ای

    📌 پارامترها:
    - kind: 'line', 'bar', 'barh', 'hist', 'box', 'scatter', 'pie'
    - x: ستون محور افقی
    - y: ستون محور عمودی
    - title: عنوان نمودار
    - xlabel: برچسب محور X
    - ylabel: برچسب محور Y
    - color: رنگ
    - figsize: (width, height)
    - ax: موقعیت در subplot
    - subplots: True برای رسم هر ستون جداگانه
    - layout: (nrows, ncols)
    - rot: چرخش برچسب‌های محور X
    """
    ...

# ============================================================
# query() — فیلتر شرطی با خوانایی بالا
# ============================================================
def query(expr: str) -> Any:
    """
    📌 فرمول رایج:
    df.query("age > 20 and city == 'Tehran'")
    df.query("age.between(40, 50) and country.isin(['Iran', 'Iraq'])")
    df.query("country not in ['Iran', 'Iraq']")
    df.query("not (age > 40 and math < 14)")
    df.query("name.str.startswith('b') or country.isin(['Turkey'])")
    df.query("country.str.contains('Ir')")
    df.query("score.isna() or country.notna()")

    📌 نکته: رشته‌ها با سینگل‌کوت، نام ستون‌ها بدون کوت
    📌 نکته: روی DataFrameهای MultiIndex کار نمی‌کند (بعد از agg)
    """
    ...

# ============================================================
# eval() — فیلتر شرطی با syntax پایتونی
# ============================================================
def eval(expr: str) -> Any:
    """
    📌 فرمول رایج:
    df[df.eval("age > 20 and (city == 'Tehran' or city == 'Shiraz')")]
    """
    ...

# ============================================================
# resample — گروه‌بندی حرفه‌ای زمانی
# ============================================================
def resample(rule: str) -> Any:
    """
    📌 فرمول رایج:
    df.set_index("Date").resample("M").size()
    df.set_index("Date").resample("M")["Volume"].sum()
    df.set_index("Date").resample("YE")["Volume"].sum()

    📌 مراحل:
    1. تبدیل به datetime
    2. حذف مقادیر خالی
    3. مرتب‌سازی
    4. set_index + resample

    📌 فرمت‌های رایج: "M"=ماهانه, "YE"=سالانه, "W"=هفتگی, "H"=ساعتی
    """
    ...

# ============================================================
# join — الحاق افقی
# ============================================================
def join(other: Any, lsuffix: str = ..., rsuffix: str = ...) -> Any:
    """
    📌 فرمول رایج:
    df1.join(df2)                                     ← اگر ستون یکسان نداشته باشیم
    df1.join(df2, lsuffix="left", rsuffix="right")    ← با پسوند برای ستون‌های تکراری
    """
    ...

# ============================================================
# loc — دسترسی با نام ایندکس
# ============================================================
def loc(row_index: Any, col_index: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    df.loc[0]                          ← ردیف با ایندکس 0
    df.loc[0:5]                        ← ردیف‌های 0 تا 5 (شامل هر دو)
    df.loc[:, 'col_name']              ← یک ستون
    df.loc[df['col'] > 10, 'col_name'] ← فیلتر شرطی
    df.loc[len(df)] = [val1, val2]     ← افزودن ردیف جدید

    📌 تفاوت با iloc:
    loc: با نام ایندکس، بازه بسته (شامل انتها)
    iloc: با موقعیت عددی، بازه نیمه‌باز
    """
    ...

# ============================================================
# شرط‌های رشته‌ای (str accessor)
# ============================================================
# df["name"].str.contains("Ali")        ← شامل
# df["name"].str.startswith("A")        ← شروع با
# df["name"].str.endswith("i")          ← پایان با
# df["name"].str.len() > 5             ← طول رشته بیشتر از 5
# ============================================================