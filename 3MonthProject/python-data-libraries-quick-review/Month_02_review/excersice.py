'''
# ============================================================
# NumPy - راهنمای مرور سریع نامپی (مرتب شده بر اساس موضوع)
# ============================================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# مبحث ۱: ساخت آرایه (Array Creation)
# ============================================================

# --- بردار (1D) ---
v = np.array([1, 2, 3, 4])                    # از لیست
v = np.zeros(5)                               # پر از صفر
v = np.ones(4, dtype=int)                     # پر از یک
v = np.full(6, 7)                             # پر از عدد دلخواه
v = np.arange(5)                              # 0 تا 4
v = np.arange(2, 10, 2)                       # 2 تا 8 با گام 2
v = np.linspace(0, 10, 5)                     # 5 عدد با فاصله مساوی
v = np.random.rand(4)                         # 4 عدد اعشاری بین 0 و 1
v = np.random.randint(-5, 10, size=8)         # 8 عدد صحیح تصادفی

# --- ماتریس (2D) ---
m = np.array([[1, 2, 3], [4, 5, 6]])          # از لیست تودرتو
m = np.zeros((3, 4), dtype=int)                # 3×4 پر از صفر
m = np.ones((2, 5))                            # 2×5 پر از یک
m = np.eye(3)                                  # ماتریس واحد 3×3
m = np.full((2, 3), 7)                         # پر از عدد دلخواه
m = np.arange(12).reshape(3, 4)                # اعداد 0 تا 11 به شکل 3×4
m = np.random.rand(2, 3).round(2)              # اعشاری تصادفی
m = np.random.randint(-5, 10, size=(3, 3))     # صحیح تصادفی

# --- تبدیل شکل (ضروری برای شبکه‌های عصبی) ---
v_col = v.reshape(-1, 1)    # بردار → ستون
v_row = v.reshape(1, -1)    # بردار → سطر
flat = m.flatten()          # ماتریس → بردار یک‌بعدی

# خلاصه ساخت آرایه:
# 1. از لیست: np.array()
# 2. از توابع کمکی: zeros, ones, full, arange, linspace
# 3. تصادفی: rand, randint
# 4. تبدیل شکل: reshape, flatten

# ============================================================
# مبحث ۲: دسترسی به عناصر (Indexing & Slicing)
# ============================================================

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# --- یک عنصر ---
m[1, 2]          # ردیف دوم، ستون سوم → 6

# --- یک ردیف کامل ---
m[1]             # ردیف دوم → [4, 5, 6]
m[1, :]          # همان

# --- یک ستون کامل ---
m[:, 1]          # ستون دوم → [2, 5, 8]

# --- برش (Slicing) ---
m[0:2, 1:3]      # ردیف‌های 0 تا 1، ستون‌های 1 تا 2
m[:3, :2]        # سه ردیف اول، دو ستون اول
m[1:, :]         # از ردیف دوم تا آخر

# --- انتخاب چند ردیف/ستون غیرمتوالی ---
m[[0, 2], :]     # ردیف‌های اول و سوم
m[:, [0, 2]]     # ستون‌های اول و سوم

# --- تغییر مقادیر ---
m[1, 1] = 99             # تغییر یک عنصر
m[2] = [10, 10, 10]      # تغییر کل ردیف سوم
m[:, 0] = [6, 6, 6]      # تغییر کل ستون اول

# خلاصه دسترسی:
# 1. عنصر: m[سطر, ستون]
# 2. ردیف: m[سطر]
# 3. ستون: m[:, ستون]
# 4. برش: m[start:end, start:end]
# 5. غیرمتوالی: m[[سطرها], :] یا m[:, [ستون‌ها]]

# ============================================================
# مبحث ۳: عملیات عددی (Arithmetic Operations)
# ============================================================

v = np.array([1, 2, 3, 4])

# --- عملیات با عدد (برداری) ---
v + 2       # جمع
v - 3       # تفریق
v * 4       # ضرب اسکالر
v / 2       # تقسیم
v ** 2      # توان

# --- عملیات دو آرایه (هم‌اندازه) ---
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
v1 + v2     # جمع عنصر به عنصر
v1 - v2     # تفریق
v1 * v2     # ضرب هادامارد
v1 / v2     # تقسیم

# --- توابع ریاضی پرکاربرد  در نامپی---
np.sqrt(v)      # جذر (ریشه دوم)
np.exp(v)       # تابع نمایی e^x
np.log(v)       # لگاریتم طبیعی (حتماً v > 0)

# نکته: اگر بردار شامل صفر یا منفی باشد، قبل از log اصلاح کن:
v = np.array([0, 1, 2, 3, -1])
v = np.abs(v)               # منفی → مثبت
v = np.where(v == 0, 1, v)  # صفر → یک
np.log(v)

# خلاصه عملیات:
# 1. برداری: +, -, *, /, ** با عدد
# 2. دوتایی: +, -, *, / بین دو آرایه هم‌اندازه
# 3. ریاضی: sqrt, exp, log

# ============================================================
# مبحث ۴: توابع آماری (Statistical Functions)
# ============================================================

v = np.array([1, 2, 3, 4, 5])
m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# --- روی کل آرایه ---
np.mean(v)      # میانگین
np.median(v)    # میانه
np.std(v)       # انحراف معیار
np.var(v)       # واریانس (var = std²)
np.max(v)       # بیشینه
np.min(v)       # کمینه
np.sum(v)       # مجموع
v.size          # تعداد عناصر

# --- روی محور خاص (ماتریس) ---
# نکته: axis=0 → ستون‌ها | axis=1 → ردیف‌ها
np.sum(m, axis=0)    # مجموع هر ستون
np.mean(m, axis=1)   # میانگین هر ردیف
np.std(m, axis=0)    # انحراف معیار هر ستون

# --- میانگین وزنی ---
weights = np.array([0.1, 0.2, 0.3, 0.2, 0.2])
weighted_avg = np.average(v, weights=weights)

# خلاصه آمار:
# 1. کل آرایه: mean, median, std, var, max, min, sum
# 2. روی محور: با axis=0 (ستون) یا axis=1 (ردیف)
# 3. وزنی: np.average(data, weights=w)

# ============================================================
# مبحث ۵: ضرب ماتریسی (Matrix Multiplication)
# ============================================================

A = np.array([[1, 2], [3, 4]])  # 2×2
B = np.array([[5, 6], [7, 8]])  # 2×2

# --- شرط ضرب: ستون‌های اولی = سطرهای دومی ---
# A(m×n) @ B(n×p) = C(m×p)

# --- دو روش ضرب ---
C1 = A @ B          # روش اول: اپراتور @ (توصیه می‌شود)
C2 = np.dot(A, B)   # روش دوم: np.dot

# --- بررسی سازگاری ابعاد ---
if A.shape[1] == B.shape[0]:
    result = A @ B
else:
    print("ابعاد سازگار نیستند")

# --- تفاوت ضرب عنصر به عنصر با ضرب ماتریسی ---
A * B    # ضرب عنصر به عنصر (هادامارد) - نیاز به ابعاد برابر
A @ B    # ضرب ماتریسی واقعی - نیاز به سازگاری ابعاد

# خلاصه ضرب ماتریسی:
# 1. شرط: ستون اول = سطر دوم
# 2. روش: A @ B یا np.dot(A, B)
# 3. تفاوت: * برای ضرب عنصری، @ برای ضرب ماتریسی

# ============================================================
# مبحث ۶: جبر خطی (Linear Algebra)
# ============================================================

m = np.array([[1, 2], [3, 4]])

# --- دترمینان (فقط مربعی) ---
det = np.linalg.det(m)

# --- معکوس (فقط مربعی با det ≠ 0) ---
if det != 0:
    inv = np.linalg.inv(m)
else:
    print("ماتریس معکوس‌پذیر نیست")

# --- حل دستگاه معادلات خطی ---
# دستگاه: 2x + 3y = 8
#          -x + 2y = 3

A = np.array([[2, 3], [-1, 2]])  # ماتریس ضرایب
b = np.array([8, 3])             # بردار سمت راست

# ۱. solve: دستگاه مربعی + ماتریس معکوس‌پذیر (بهترین)
if np.linalg.det(A) != 0:
    x_solve = np.linalg.solve(A, b)

# ۲. inv: A_inv @ b (کندتر، فقط برای مربعی)
x_inv = np.linalg.inv(A) @ b

# ۳. lstsq: معادلات > مجهول‌ها (کمترین مربعات)
A_over = np.array([[1, 1], [2, 1], [3, 1]])  # ۳ معادله، ۲ مجهول
b_over = np.array([2, 3, 4])
x_lstsq = np.linalg.lstsq(A_over, b_over, rcond=None)[0]

# ۴. pinv: معادلات < مجهول‌ها یا ماتریس منفرد (شبه‌معکوس)
A_under = np.array([[1, 1, 1], [2, 1, 1]])  # ۲ معادله، ۳ مجهول
b_under = np.array([3, 4])
x_pinv = np.linalg.pinv(A_under) @ b_under

# --- سایر توابع جبر خطی ---
np.linalg.norm(v)        # طول بردار (نرم)
np.linalg.matrix_rank(m) # رتبه ماتریس
np.transpose(m)          # ترانهاده
np.trace(m)              # اثر (مجموع قطر اصلی)

# خلاصه جبر خطی:
# 1. دترمینان: np.linalg.det()
# 2. معکوس: np.linalg.inv()
# 3. حل دستگاه: solve (مربعی), lstsq (بیش‌تعداد), pinv (کم‌تعداد)
# 4. نرم: np.linalg.norm()
# 5. رتبه: np.linalg.matrix_rank()

# ============================================================
# مبحث ۷: تبدیل داده‌ها (Data Transformation)
# ============================================================

v = np.array([1, 2, 3, 4, 5, 6])
m = np.array([[1, 2, 3], [4, 5, 6]])

# --- تغییر نوع داده ---
v.astype(float)
v.astype(int)

# --- تغییر شکل ---
v.reshape(2, 3)           # بردار ۶ تایی → ماتریس ۲×۳
m.reshape(3, -1)          # تغییر شکل (ستون خودکار)
m.flatten()               # ماتریس → بردار یک‌بعدی

# --- چسباندن آرایه‌ها ---
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

np.concatenate((v1, v2))           # چسباندن افقی (بردارها)
np.concatenate((m1, m2), axis=0)   # چسباندن عمودی (زیر هم)
np.concatenate((m1, m2), axis=1)   # چسباندن افقی (کنار هم)

# --- تقسیم آرایه ---
np.split(v, 3)            # تقسیم به ۳ بخش مساوی

# --- مرتب‌سازی ---
np.sort(v)                # صعودی

# خلاصه تبدیل داده:
# 1. نوع: astype()
# 2. شکل: reshape(), flatten()
# 3. چسباندن: concatenate()
# 4. تقسیم: split()
# 5. مرتب‌سازی: sort()

# ============================================================
# مبحث ۸: توزیع‌های داده (Data Distributions)
# ============================================================

np.random.seed(42)

# --- توزیع نرمال (Gaussian) ---
normal_data = np.random.normal(loc=50, scale=10, size=1000)
# loc=میانگین, scale=انحراف معیار

# --- توزیع یکنواخت (Uniform) ---
uniform_data = np.random.uniform(low=-20, high=40, size=1000)


# --- سنجش پایداری داده (CV) ---
یعنی بررسی رابطه عددی بین میانگین و انحراف معیار در توزیع نرمال
loc = میانگین
scale = نحراف معیار
cv = scale / loc

cv = 10 / 50  # scale / loc
# CV < 0.1: بسیار پایدار
# CV < 0.3: نوسان معمول
# CV < 1: نوسان زیاد
# CV >= 1: نوسان شدید

# خلاصه توزیع‌ها:
# 1. نرمال: normal(loc, scale, size)
# 2. یکنواخت: uniform(low, high, size)

# ============================================================
# مبحث ۹: رسم نمودار آرایه ها با Matplotlib
# ============================================================

# --- الگوی کلی ---
x = np.linspace(-10, 10, 100)
y = 2 * x + 5

plt.plot(x, y, color="black", marker="*", linestyle="--", label="y = f(x)")
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Chart Title")
plt.legend(loc="best")
plt.grid(True)
# plt.savefig("chart.png", dpi=300)
plt.show()

# --- هیستوگرام (توزیع داده) ---
data = np.random.randint(0, 100, 500)
plt.hist(data, bins=30, color="green", edgecolor="black")
plt.show()

# --- نمودار پراکندگی (Scatter) ---
plt.scatter(x, y, color="red", marker="o", s=50, label="Points")
plt.show()

# --- نمودار میله‌ای (Bar) ---
categories = ['A', 'B', 'C']
values = [10, 20, 15]
plt.bar(categories, values, color="blue", edgecolor="black", width=0.6)
plt.show()

# --- subplots مدرن (چند نمودار در یک صفحه) ---
fig, axs = plt.subplots(2, 2, figsize=(12, 10), constrained_layout=True)
axs[0, 0].plot(x, np.sin(x))
axs[0, 1].plot(x, np.cos(x))
axs[1, 0].scatter(x, np.tan(x))
axs[1, 1].hist(data, bins=20)
plt.show()

# --- الگوی تشخیص نیاز به x ---
# توزیع (hist, boxplot): x لازم نیست
# روند (plot): x می‌تواند مصنوعی باشد
# مقایسه/رابطه (scatter, bar): x باید واقعی باشد

# خلاصه رسم نمودار:
# 1. خطی: plot(x, y)
# 2. هیستوگرام: hist(data, bins)
# 3. پراکندگی: scatter(x, y)
# 4. میله‌ای: bar(x, y)
# 5. subplots: plt.subplots(rows, cols)

# ============================================================
# مبحث ۱۰: تحلیل داده با Pandas (جامع)
# ============================================================

# --- ساخت DataFrame نمونه ---
df = pd.DataFrame({
    'id': range(1, 6),
    'name': ['Ali', 'Sara', 'Reza', 'Neda', 'Hassan'],
    'age': [25, 30, 22, 28, 35],
    'math': [18, 15, 19, 14, 17],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'score': [85, 92, 78, 88, 95]
})

# --- مرحله ۱: شناخت ساختار داده ---
df.shape           # تعداد سطر و ستون
df.columns         # نام ستون‌ها
df.info()          # نوع داده، تعداد NaN
df.head()          # چند ردیف اول

# --- مرحله ۲: بررسی کیفیت داده ---
df.isnull().sum()           # تعداد NaN هر ستون
df.duplicated().sum()       # تعداد ردیف‌های تکراری
# df.drop_duplicates(inplace=True)

# --- مرحله ۳: درک عددی اولیه ---
df.describe()               # خلاصه آماری
df.min(), df.max()          # بازه مقادیر

# --- مرحله ۴: درک توزیع عددی ---
num_cols = df.select_dtypes(include="number")
num_cols.mean()             # میانگین هر ستون
num_cols.median()           # میانه
num_cols.std()              # انحراف معیار
num_cols.skew()             # چولگی (نزدیک ۰ = متقارن)

# --- مرحله ۵: درک توزیع دسته‌ها ---
cat_cols = df.select_dtypes(include="object")
cat_cols.nunique()                      # تعداد مقادیر یکتا
df["gender"].value_counts()             # شمارش هر دسته
df["gender"].value_counts(normalize=True)  # نسبت (درصد)

# --- مرحله ۶: گروه‌بندی ---
df.groupby("gender", as_index=False)["math"].mean().round()
df.groupby(["gender"], as_index=False)[num_cols.columns].mean().round()

# --- مرحله ۷: پاکسازی داده ---
# تشخیص مقادیر گمشده غیراستاندارد
df = df.replace("none", None)
df = df.replace("?", None)

# حذف
df.dropna(inplace=True)            # حذف ردیف‌های دارای NaN
# del df["column_name"]            # حذف کل ستون

# پر کردن
df["col"].fillna(df["col"].mean(), inplace=True)    # میانگین
df["col"].fillna(df["col"].median(), inplace=True)  # میانه
df["col"].fillna("Unknown", inplace=True)           # مقدار ثابت

# پر کردن پیشرفته با نمونه‌گیری
for col in df.columns:
    non_null = df[col].dropna(ignore_index=True)
    n_missing = df[col].isna().sum()
    if n_missing > 0 and len(non_null) > 0:
        samples = non_null.sample(n=n_missing, replace=True, random_state=42)
        df.loc[df[col].isna(), col] = samples.values

# --- مرحله ۸: رسم نمودار از Pandas ---
df.plot(kind="hist", y="math", bins=10, edgecolor="black")
df["gender"].value_counts().plot(kind="bar", edgecolor="black")
df.plot(kind="scatter", x="age", y="score")
df.plot(kind="box", y="math")

# --- subplots با Pandas ---
fig, axs = plt.subplots(1, 2, figsize=(12, 5), constrained_layout=True)
df["math"].plot(kind="hist", ax=axs[0], title="Math Distribution", edgecolor="black")
df["gender"].value_counts().plot(kind="bar", ax=axs[1], title="Gender", edgecolor="black")
plt.show()

# خلاصه تحلیل داده:
# 1. ساختار: shape, columns, info(), head()
# 2. کیفیت: isnull().sum(), duplicated().sum()
# 3. عددی: describe(), skew(), min(), max()
# 4. دسته‌ای: nunique(), value_counts(), groupby()
# 5. تصویر: hist, bar, scatter, box
# 6. پاکسازی: dropna(), fillna(), replace()

# ============================================================
# چک‌لیست نهایی
# ============================================================

print("\n" + "="*60)
print("چک‌لیست نهایی NumPy:")
print("="*60)
print("""
1. ساخت: array, zeros, ones, full, arange, linspace, random
2. دسترسی: m[سطر, ستون], m[:, ستون], m[سطر], slicing
3. عملیات: +, -, *, /, ** (برداری), sqrt, exp, log
4. آمار: mean, median, std, var, max, min, sum
5. ضرب ماتریسی: A @ B (شرط: ستون اول = سطر دوم)
6. جبر خطی: det, inv, solve, lstsq, pinv, norm
7. تبدیل: astype, reshape, flatten, concatenate, sort
8. توزیع‌ها: normal, uniform, binomial, poisson, exponential
9. رسم: plot, scatter, hist, bar, subplot
10. تحلیل: info(), describe(), value_counts(), groupby()
""")

# ============================================================
# نکات کلیدی و تفاوت‌ها
# ============================================================

print("\n" + "="*60)
print("نکات کلیدی:")
print("="*60)
print("""
1. axis در NumPy: axis=0 → ستون‌ها | axis=1 → ردیف‌ها
2. axis در Pandas: axis=0 → ردیف‌ها | axis=1 → ستون‌ها (برعکس!)
3. ضرب عنصری: * | ضرب ماتریسی: @
4. reshape(-1, 1): بردار → ستون | reshape(1, -1): بردار → سطر
5. log فقط برای اعداد مثبت: abs و where برای اصلاح
6. solve فقط برای دستگاه‌های مربعی با det ≠ 0
7. lstsq برای دستگاه‌های بیش‌تعداد (معادلات > مجهول‌ها)
8. pinv برای دستگاه‌های کم‌تعداد (معادلات < مجهول‌ها)
""")

# ============================================================
# پایان راهنمای مرور سریع
# ============================================================
'''