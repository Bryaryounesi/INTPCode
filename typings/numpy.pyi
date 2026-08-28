from typing import Any, Tuple, List, Optional, Union
import numpy as np

# ============================================================
# Data Types (نوع داده‌ها)
# ============================================================
uint8: Any  # 8-bit unsigned integer (0 to 255) - پرکاربردترین برای تصاویر
uint16: Any  # 16-bit unsigned integer (0 to 65535)
uint32: Any  # 32-bit unsigned integer
uint64: Any  # 64-bit unsigned integer
int8: Any  # 8-bit signed integer (-128 to 127)
int16: Any  # 16-bit signed integer (-32768 to 32767)
int32: Any  # 32-bit signed integer
int64: Any  # 64-bit signed integer
float16: Any  # 16-bit floating point
float32: Any  # 32-bit floating point - رایج برای SIFT descriptors
float64: Any  # 64-bit floating point - پیش‌فرض NumPy
float128: Any  # 128-bit floating point
complex64: Any  # 64-bit complex number
complex128: Any  # 128-bit complex number
bool_: Any  # Boolean type
str_: Any  # String type
bytes_: Any  # Bytes type
object_: Any  # Object type

# ============================================================
# ۱. ساخت آرایه
# ============================================================
def array(data: Any, dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    a = np.array(data)
    a = np.array(data, dtype=np.uint8)
    a = np.array(data, dtype=np.float32)

    📌 پارامترها:
    - data: لیست (بردار) یا لیستی از لیست‌ها (ماتریس)
    - dtype (اختیاری): np.uint8, np.float32, np.int32 — پیش‌فرض: خودکار

    📌 نکته:
    a.tolist() ← تبدیل آرایه به لیست
    """
    ...

# ============================================================
# ۲. توابع ساخت بردار و ماتریس
# ============================================================
def zeros(shape: Any, dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.zeros(n)              ← بردار n خانه‌ای
    np.zeros((m, n))         ← ماتریس m×n
    np.zeros((m, n), dtype=np.uint8)  ← ماتریس با نوع داده مشخص
    # -------------------------------------
    📌 کاربرد ویژه در Mask (جداسازی دقیق شیء):
        mask = np.zeros(gray.shape, dtype=np.uint8)
        cv2.drawContours(mask, [biggest], -1, 255, -1)
        masked = cv2.bitwise_and(img, img, mask=mask)
    # -------------------------------------
    📌 پارامترها:
    - shape: عدد (بردار) یا تاپل (ماتریس)
    - dtype (اختیاری): np.uint8, np.float32 — پیش‌فرض float64
    """
    ...

def ones(shape: Any, dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.ones(n) / np.ones((m, n))
    np.ones((m, n), dtype=np.int32)
    """
    ...

def full(shape: Any, fill_value: Any, dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.full((m, n), value)
    np.full((m, n), 255, dtype=np.uint8)
    """
    ...

def eye(N: int, M: int = ..., k: int = ..., dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.eye(n)                  ← ماتریس همانی n×n
    np.identity(n)             ← معادل eye

    📌 پارامترها:
    - N: تعداد ردیف
    - M (اختیاری): تعداد ستون — پیش‌فرض = N
    - dtype (اختیاری): np.float64, np.int32
    """
    ...

def arange(start: Any, stop: Any = ..., step: Any = ..., dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.arange(n)                       ← 0 تا n-1
    np.arange(start, stop, step)       ← بازه با گام

    📌 نکته: برای ماتریس، reshape کن
    """
    ...

def linspace(start: Any, stop: Any, num: int = ..., dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.linspace(start, stop, num)

    📌 پارامترها:
    - start: شروع بازه
    - stop: پایان بازه
    - num: تعداد نقاط — پیش‌فرض 50
    - dtype (اختیاری): نوع داده خروجی

    📌 نکته: برای ماتریس، حاصلضرب m×n باید = num باشد
    """
    ...

# ============================================================
# ۳. تغییر شکل آرایه
# ============================================================
def reshape(a: Any, newshape: Any) -> Any:
    """
    📌 فرمول رایج:
    a.reshape(m, n)

    📌 پارامترها:
    - a: آرایه ورودی
    - newshape: (تعداد سطر, تعداد ستون) — یکی می‌تواند -1 باشد (خودکار)

    📌 نکته: حاصلضرب ابعاد باید = تعداد کل عناصر
    """
    ...

def flatten(a: Any) -> Any:
    """
    📌 فرمول رایج:
    a.flatten()    ← تبدیل ماتریس به بردار
    """
    ...

# ============================================================
# ۴. توابع آماری
# ============================================================
def sum(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.sum(v)               ← مجموع بردار
    np.sum(m)               ← مجموع کل ماتریس
    np.sum(m, axis=0)       ← مجموع ستون‌ها
    np.sum(m, axis=1)       ← مجموع ردیف‌ها
    """
    ...

def mean(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.mean(v)
    np.mean(m, axis=0)      ← میانگین ستون‌ها
    np.mean(m, axis=1)      ← میانگین ردیف‌ها
    """
    ...

def std(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.std(v)               ← انحراف معیار بردار
    np.std(m, axis=0)       ← انحراف معیار ستون‌ها
    """
    ...

def var(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.var(v)
    np.var(m, axis=0)       ← واریانس ستون‌ها
    """
    ...

def max(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.max(v)
    np.max(m, axis=0)       ← بیشینه ستون‌ها
    """
    ...

def min(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.min(v)
    np.min(m, axis=0)       ← کمینه ستون‌ها
    """
    ...

def median(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.median(v)
    np.median(m, axis=0)    ← میانه ستون‌ها
    """
    ...

def size(a: Any) -> int:
    """
    📌 فرمول رایج:
    np.size(v)              ← تعداد عناصر (معادل len)
    m.size                  ← تعداد کل عناصر ماتریس
    m.shape[0]              ← تعداد ردیف‌ها
    m.shape[1]              ← تعداد ستون‌ها
    """
    ...

# ============================================================
# ۵. میانگین وزندار
# ============================================================
def average(a: Any, axis: Any = ..., weights: Any = ..., returned: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    np.average(data, weights=w)

    📌 پارامترها:
    - a: آرایه مقادیر
    - axis (اختیاری): 0 = ستون‌ها | 1 = ردیف‌ها
    - weights: آرایه وزن‌ها — طول = تعداد ردیف‌ها (axis=0) یا تعداد ستون‌ها (axis=1)
    - returned (اختیاری): پیش‌فرض False — True = مجموع وزن‌ها را هم برگرداند
    """
    ...

# ============================================================
# ۶. توابع ریاضی (Element-wise)
# ============================================================
def sqrt(a: Any) -> Any:
    """📌 فرمول رایج: np.sqrt(v) ← ریشه دوم"""
    ...

def cbrt(a: Any) -> Any:
    """📌 فرمول رایج: np.cbrt(v) ← ریشه سوم"""
    ...

def exp(a: Any) -> Any:
    """📌 فرمول رایج: np.exp(v) ← e^x"""
    ...

def power(x1: Any, x2: Any) -> Any:
    """
    📌 فرمول رایج:
    np.power(v, 3)       ← v^3
    np.power(2, v)       ← 2^v

    📌 نکته: اگر توان منفی، پایه را float کن
    """
    ...

def log(a: Any) -> Any:
    """📌 فرمول رایج: np.log(v) ← لگاریتم طبیعی (ln)"""
    ...

def log2(a: Any) -> Any:
    """📌 فرمول رایج: np.log2(v) ← لگاریتم مبنای 2"""
    ...

def log10(a: Any) -> Any:
    """📌 فرمول رایج: np.log10(v) ← لگاریتم مبنای 10"""
    ...

def abs(a: Any) -> Any:
    """📌 فرمول رایج: np.abs(v) ← قدر مطلق"""
    ...

def ceil(a: Any) -> Any:
    """📌 فرمول رایج: np.ceil(v) ← گرد به بالا"""
    ...

def floor(a: Any) -> Any:
    """📌 فرمول رایج: np.floor(v) ← گرد به پایین"""
    ...

def round(a: Any, decimals: int = ...) -> Any:
    """📌 فرمول رایج: np.round(v) ← گرد معمولی"""
    ...

def clip(a: Any, a_min: Any, a_max: Any) -> Any:
    """
    📌 فرمول رایج:
    np.clip(v, 0, 1)    ← محدود کردن بین min و max
    """
    ...

def sign(a: Any) -> Any:
    """📌 فرمول رایج: np.sign(v) ← علامت (-1, 0, 1)"""
    ...

# ============================================================
# ۷. توابع مثلثاتی
# ============================================================
def sin(a: Any) -> Any:
    """📌 فرمول رایج: np.sin(v)"""
    ...

def cos(a: Any) -> Any:
    """📌 فرمول رایج: np.cos(v)"""
    ...

def tan(a: Any) -> Any:
    """📌 فرمول رایج: np.tan(v)"""
    ...

def arcsin(a: Any) -> Any:
    """📌 فرمول رایج: np.arcsin(v)"""
    ...

def arccos(a: Any) -> Any:
    """📌 فرمول رایج: np.arccos(v)"""
    ...

def arctan(a: Any) -> Any:
    """📌 فرمول رایج: np.arctan(v)"""
    ...

# ============================================================
# ۸. جبر خطی
# ============================================================
def dot(a: Any, b: Any) -> Any:
    """
    📌 فرمول رایج:
    c = A @ B
    c = np.dot(A, B)

    📌 شرط: A.shape[1] == B.shape[0]
    """
    ...

def transpose(a: Any, axes: Any = ...) -> Any:
    """📌 فرمول رایج: np.transpose(m) ← ترانهاده ماتریس"""
    ...

def trace(a: Any, offset: int = ..., axis1: int = ..., axis2: int = ...) -> Any:
    """📌 فرمول رایج: np.trace(m) ← مجموع قطر اصلی"""
    ...

# ============================================================
# ۹. linalg
# ============================================================
def norm(x: Any, ord: Any = ..., axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.linalg.norm(v)    ← طول بردار
    """
    ...

def det(a: Any) -> Any:
    """
    📌 فرمول رایج:
    np.linalg.det(m)     ← دترمینان (فقط ماتریس مربعی)

    📌 نکته: اگر det != 0، ماتریس معکوس دارد
    """
    ...

def inv(a: Any) -> Any:
    """
    📌 فرمول رایج:
    np.linalg.inv(m)     ← معکوس ماتریس (فقط مربعی)

    📌 شرط: det(m) != 0
    """
    ...

def solve(a: Any, b: Any) -> Any:
    """
    📌 فرمول رایج:
    x = np.linalg.solve(A, b)

    📌 پارامترها:
    - A: ماتریس ضرایب (مربعی، معکوس‌پذیر)
    - b: بردار نتایج — تعداد = تعداد ردیف‌های A

    📌 نکته: اول چک کن det(A) != 0
    """
    ...

def lstsq(a: Any, b: Any, rcond: Any = ...) -> Tuple[Any, Any, Any, Any]:
    """
    📌 فرمول رایج:
    x = np.linalg.lstsq(A, b, rcond=None)[0]

    📌 پارامترها:
    - A: ماتریس ضرایب (بیش‌تعداد: ردیف > ستون)
    - b: بردار نتایج
    - rcond: None یا -1 (فیلتر خودکار)

    📌 کاربرد: دستگاه‌های بیش‌تعداد و داده‌های نویزی
    """
    ...

def pinv(a: Any) -> Any:
    """
    📌 فرمول رایج:
    x = np.linalg.pinv(A) @ b

    📌 کاربرد: دستگاه‌های کم‌تعداد (بی‌نهایت جواب) — ردیف < ستون
    """
    ...

def svd(a: Any) -> Tuple[Any, Any, Any]:
    """📌 فرمول رایج: np.linalg.svd(m) ← تجزیه SVD"""
    ...

def eig(a: Any) -> Tuple[Any, Any]:
    """📌 فرمول رایج: np.linalg.eig(m) ← مقادیر ویژه (فقط مربعی)"""
    ...

def matrix_rank(a: Any) -> int:
    """📌 فرمول رایج: np.linalg.matrix_rank(m) ← رتبه ماتریس"""
    ...

# ============================================================
# ۱۰. چسباندن و تقسیم
# ============================================================
def concatenate(arrays: Any, axis: int = ...) -> Any:
    """
    📌 فرمول رایج:
    np.concatenate((a1, a2), axis=0)    ← عمودی (ردیف‌ها جمع می‌شوند)
    np.concatenate((a1, a2), axis=1)    ← افقی (ستون‌ها جمع می‌شوند)

    📌 نکته: آرایه‌ها باید ابعاد یکسان داشته باشند
    """
    ...

def vstack(tup: Any) -> Any:
    """
    📌 فرمول رایج:
    np.vstack((a1, a2))    ← چسباندن عمودی (ردیف‌ها)

    📌 پارامترها:
    - tup: تاپل یا لیست آرایه‌ها — باید تعداد ستون یکسان داشته باشند

    📌 نکته: معادل np.concatenate((a1, a2), axis=0) برای ماتریس‌ها
    """
    ...

def hstack(tup: Any) -> Any:
    """
    📌 فرمول رایج:
    np.hstack((a1, a2))    ← چسباندن افقی (ستون‌ها)

    📌 پارامترها:
    - tup: تاپل یا لیست آرایه‌ها — باید تعداد سطر یکسان داشته باشند

    📌 نکته: معادل np.concatenate((a1, a2), axis=1) برای ماتریس‌ها
    """
    ...

def split(ary: Any, indices_or_sections: Any, axis: int = ...) -> List[Any]:
    """
    📌 فرمول رایج:
    np.split(arr, parts, axis=0)       ← برش عمودی
    np.split(arr, parts, axis=1)[0]    ← برش افقی، پارت اول

    📌 نکته: خروجی لیستی از آرایه‌هاست — [0] یعنی پارت اول
    """
    ...

# ============================================================
# ۱۱. مرتب‌سازی
# ============================================================
def sort(a: Any, axis: int = ...) -> Any:
    """
    📌 فرمول رایج:
    np.sort(arr)    ← مرتب‌سازی از کوچک به بزرگ
    """
    ...

# ============================================================
# ۱۲. تولید داده تصادفی (NumPy)
# ============================================================
def rand(*args: Any) -> Any:
    """
    📌 فرمول رایج:
    np.random.rand(m, n)    ← ماتریس m×n با اعداد تصادفی بین 0 و 1

    📌 نکته: از .round() برای گرد کردن استفاده کن
    """
    ...

def randint(low: int, high: int = ..., size: Any = ..., dtype: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.randint(min, max, size=(m, n))    ← ماتریس تصادفی در رنج
    np.random.randint(min, max, size=n)         ← بردار تصادفی

    📌 پارامترها:
    - low: کمترین عدد (شامل)
    - high: بیشترین عدد (غیر شامل)
    - size: تعداد / ابعاد
    - dtype (اختیاری): np.int32, np.int64
    """
    ...

def uniform(low: float, high: float, size: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.uniform(low, high, size)

    📌 پارامترها:
    - low: کمینه
    - high: بیشینه
    - size: تعداد / ابعاد

    📌 کاربرد: مقداردهی اولیه وزن‌ها، شبیه‌سازی بدون سوگیری
    """
    ...

def normal(loc: float, scale: float, size: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.normal(mean, std, size)

    📌 پارامترها:
    - loc: میانگین
    - scale: انحراف معیار
    - size: تعداد / ابعاد

    📌 کاربرد: مدل‌سازی نویز، داده‌های طبیعی

    📌 قاعده پایداری (CV = std/mean):
    CV < 0.1: بسیار پایدار (میانگین ≈ ۱۰× انحراف معیار)
    0.1 ≤ CV < 0.3: نوسان معمول (میانگین ≈ ۳ تا ۱۰×)
    0.3 ≤ CV < 1: نوسان زیاد (میانگین ≈ ۱ تا ۳×)
    CV ≥ 1: نوسان شدید (انحراف ≥ میانگین)
    """
    ...

def choice(a: Any, size: Any = ..., replace: bool = ..., p: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.choice(a, size=n, replace=False)

    📌 پارامترها:
    - a: آرایه یا range منبع
    - size: تعداد خروجی
    - replace: پیش‌فرض True — False = بدون تکرار (یونیک)
    - p (اختیاری): وزن‌ها — مجموع باید = 1
    """
    ...

def seed(seed_value: int) -> None:
    """📌 فرمول رایج: np.random.seed(42) ← ثابت‌سازی خروجی تصادفی"""
    ...

# ============================================================
# ۱۳. تبدیل نوع و دسترسی
# ============================================================
def astype(a: Any, dtype: Any) -> Any:
    """
    📌 فرمول رایج:
    arr.astype(np.uint8)    ← تبدیل نوع داده
    arr.astype(np.float32)
    """
    ...

def histogram(a: Any, bins: int = ..., range: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.histogram(img, bins=256)    ← هیستوگرام
    """
    ...

def percentile(a: Any, q: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.percentile(img, 95)    ← حذف outlier
    """
    ...

def pad(array: Any, pad_width: Any, mode: str = ...) -> Any:
    """
    📌 فرمول رایج:
    np.pad(img, pad_width=1, mode='constant')    ← Padding
    """
    ...

# ============================================================
# ۱۴. FFT
# ============================================================
def fft2(a: Any) -> Any:
    """📌 فرمول رایج: np.fft.fft2(gray) ← تبدیل فوریه دوبعدی"""
    ...

def ifft2(a: Any) -> Any:
    """📌 فرمول رایج: np.fft.ifft2(freq) ← معکوس FFT"""
    ...

def fftshift(a: Any) -> Any:
    """📌 فرمول رایج: np.fft.fftshift(freq) ← جابجایی فرکانس صفر به مرکز"""
    ...

# ============================================================
# ۱۵. توابع فعال‌سازی (Computer Vision)
# ============================================================
def maximum(x1: Any, x2: Any) -> Any:
    """
    📌 فرمول رایج:
    np.maximum(0, x)    ← ReLU
    """
    ...

def tanh(a: Any) -> Any:
    """📌 فرمول رایج: np.tanh(x) ← تانژانت هیپربولیک"""
    ...

def cov(m: Any) -> Any:
    """📌 فرمول رایج: np.cov(W) ← ماتریس کوواریانس (برای PCA)"""
    ...

def argmax(a: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.argmax(predictions, axis=1)    ← پیش‌بینی کلاس
    """
    ...

# ============================================================
# ۱۶. عملیات روی تصویر
# ============================================================
def rot90(m: Any, k: int = ...) -> Any:
    """📌 فرمول رایج: np.rot90(img) ← چرخش 90 درجه"""
    ...

def flip(m: Any, axis: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.flip(img, axis=0)    ← آینه عمودی
    """
    ...

def where(condition: Any, x: Any = ..., y: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.where(gray > 127, 255, 0)    ← آستانه‌گذاری باینری
    """
    ...

def stack(arrays: Any, axis: int = ...) -> Any:
    """
    📌 فرمول رایج:
    np.stack([r, g, b], axis=-1)    ← ترکیب کانال‌ها
    """
    ...

# ============================================================
# توزیع‌های آماری — پارامترهای کلیدی
# ============================================================
def binomial(n: int, p: float, size: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.binomial(n=10, p=0.5, size=100)
    📌 پارامترها: n=تعداد آزمایش, p=احتمال موفقیت
    """
    ...

def poisson(lam: float, size: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.poisson(lam=5, size=100)
    📌 پارامترها: lam=میانگین رویداد
    """
    ...

def exponential(scale: float, size: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    np.random.exponential(scale=2, size=100)
    📌 پارامترها: scale=1/نرخ
    """
    ...
