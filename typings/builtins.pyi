# builtins.pyi — چیت‌شیت توابع و کلاس‌های داخلی پایتون
# نسخه ۵ — با docstring روی همه متدها برای hover کامل
from typing import Any, Iterable, Union, Optional, Callable, TypeVar, overload, Generic

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")

# ============================================================
# راهنمای سریع f-string
# ============================================================
# 📌 سینتکس پایه:
#     f"{variable}"  |  f"{expression}"  |  f"text {variable}"
#
# 📌 فرمت‌بندی عدد اعشاری:
#     f"{value:.2f}"       ← دو رقم اعشار        مثال: 3.14
#     f"{value:.0f}"       ← بدون اعشار           مثال: 3
#     f"{value:+.2f}"      ← با علامت             مثال: +3.14
#     [CV] f"accuracy: {acc:.4f}"    ← accuracy: 0.9568
#
# 📌 درصد:
#     f"{value:.1%}"       ← یک رقم اعشار درصد   مثال: 95.7%
#     f"{value:.2%}"       ← دو رقم اعشار درصد   مثال: 95.68%
#     [CV] f"precision: {p:.1%}"     ← precision: 95.7%
#
# 📌 عدد صحیح:
#     f"{value:d}"         ← عدد صحیح
#     f"{value:5d}"        ← حداقل 5 کاراکتر
#     f"{value:05d}"       ← پر با صفر
#     f"{value:+d}"        ← با علامت
#     [CV] f"image_{idx:04d}.jpg"    ← image_0042.jpg
#
# 📌 جداکننده هزارگان:
#     f"{value:,}"         ← 1,234,567
#     f"{value:_}"         ← 1_234_567
#
# 📌 تراز (Alignment):
#     f"{value:>10}"       ← راست‌چین
#     f"{value:<10}"       ← چپ‌چین
#     f"{value:^10}"       ← وسط‌چین
#     [CV] جدول متریک‌ها:
#     for name, acc, loss in results:
#         print(f"{name:<15} acc: {acc:>6.2%} loss: {loss:>8.4f}")
#
# 📌 پر کردن با کاراکتر دلخواه:
#     f"{value:*>10}"      ← *******42
#     f"{value:0<10}"      ← 4200000000
#     f"{value:->10}"      ← --------42
#
# 📌 فرمت‌های خاص:
#     f"{value:e}"         ← علمی
#     f"{value:.2e}"       ← علمی با دو اعشار
#     f"{value:g}"         ← عمومی
#     f"{value:b}"         ← باینری
#     f"{value:o}"         ← اکتال
#     f"{value:x}"         ← هگز کوچک
#     f"{value:X}"         ← هگز بزرگ
#
# 📌 ترکیب چند فرمت:
#     f"{value:>10.2f}"    ← راست‌چین با دو اعشار
#     f"{value:<10.2%}"    ← چپ‌چین با فرمت درصد
#     f"{value:08.2f}"     ← پر با صفر، دو اعشار
#
# 📌 فراخوانی متد و attribute داخل {}:
#     f"{name.upper()}"
#     f"{data['label']}"
#     f"{image.shape[0]} x {image.shape[1]}"
#
# 📌 شرط یک‌خطی داخل {}:
#     f"{'yes' if valid else 'no'}"
#     f"{'OK' if conf > 0.8 else 'low'}"
#     [CV] f"image_{idx:04d}: {'OK' if ok else 'FAIL'}"
#
# 📌 نکات:
#     - داخل {} می‌شود هر عبارت معتبر پایتون نوشت.
#     - برای نمایش { یا } از {{ و }} استفاده کن.
#     - !r برای repr، !s برای str (پیش‌فرض).
#     - f-string از پایتون 3.6 به بعد وجود دارد.
# ============================================================

# ============================================================
# print
# ============================================================
def print(
    *args: Any,
    sep: Optional[str] = ...,
    end: Optional[str] = ...,
    file: Any = ...,
    flush: bool = ...
) -> None:
    """
    📌 فرمول رایج:
    print("hello")
    print("name:", name)
    print("a", "b", "c", sep="-")

    📌 پارامترها:
    - *args: هر تعداد مقدار (با کاما جدا می‌شوند)
    - sep (اختیاری): جداکننده بین مقادیر — پیش‌فرض: فاصله (' ')
    - end (اختیاری): انتهای خروجی — پیش‌فرض: خط جدید ('\n')
    - file (اختیاری): خروجی به فایل
    - flush (اختیاری): فلاش کردن بافر

    📌 [CV] برای چاپ لاگ پردازش دیتاست:
    print(f"loaded {n} images", flush=True)

    📌 مثال‌ها:
    print("hello", "world")              # hello world
    print("a", "b", sep="-")             # a-b
    print("loading", end="...")          # بدون خط جدید
    """
    ...

# ============================================================
# ord / chr
# ============================================================
def ord(c: str) -> int:
    """
    📌 فرمول رایج:
    ord('q')        ← 113
    ord('a')        ← 97

    📌 پارامترها:
    - c: یک کاراکتر (رشته تک‌حرفی)

    📌 برمی‌گردونه: کد ASCII/Unicode کاراکتر

    📌 [CV] کاربرد کلاسیک در OpenCV:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    """
    ...

def chr(i: int) -> str:
    """
    📌 فرمول رایج:
    chr(113)        ← 'q'
    chr(97)         ← 'a'

    📌 پارامترها:
    - i: کد ASCII/Unicode

    📌 برمی‌گردونه: کاراکتر مربوط به کد
    """
    ...

# ============================================================
# len
# ============================================================
def len(obj: Any) -> int:
    """
    📌 فرمول رایج:
    len([1, 2, 3])      ← 3
    len("hello")        ← 5
    len({"a": 1})       ← 1

    📌 برمی‌گردونه: تعداد عناصر

    📌 [CV] تعداد نمونه‌های دیتاست:
    num_images = len(image_paths)
    """
    ...

# ============================================================
# max / min / sum / sorted
# ============================================================
@overload
def max(
    iterable: Iterable[T],
    *,
    key: Optional[Callable[[T], Any]] = ...,
    default: Optional[T] = ...
) -> T: ...
@overload
def max(arg1: T, arg2: T, *args: T, key: Optional[Callable[[T], Any]] = ...) -> T: ...
def max(*args: Any, **kwargs: Any) -> Any:
    """
    📌 فرمول رایج:
    max([12, 6, 5, 2, 7])                    ← 12
    max(contours, key=cv2.contourArea)       ← بزرگترین کانتور
    max(contours, key=lambda c: cv2.contourArea(c))

    📌 پارامترها:
    - iterable: لیست/تاپل/مجموعه
    - key (اختیاری): تابع کلید برای تعیین معیار مقایسه
    - default (اختیاری): مقدار پیش‌فرض اگر iterable خالی باشد

    📌 برمی‌گردونه: بزرگترین مقدار (یا آیتم با بیشترین مقدار key)

    📌 [CV] بزرگترین تصویر:
    largest = max(images, key=lambda img: img.shape[0] * img.shape[1])
    """
    ...

@overload
def min(
    iterable: Iterable[T],
    *,
    key: Optional[Callable[[T], Any]] = ...,
    default: Optional[T] = ...
) -> T: ...
@overload
def min(arg1: T, arg2: T, *args: T, key: Optional[Callable[[T], Any]] = ...) -> T: ...
def min(*args: Any, **kwargs: Any) -> Any:
    """
    📌 فرمول رایج:
    min([12, 6, 5, 2, 7])                    ← 2
    min(contours, key=cv2.contourArea)       ← کوچکترین کانتور

    📌 پارامترها:
    - iterable: لیست/تاپل/مجموعه
    - key (اختیاری): تابع کلید برای تعیین معیار مقایسه
    - default (اختیاری): مقدار پیش‌فرض اگر iterable خالی باشد

    📌 برمی‌گردونه: کوچکترین مقدار (یا آیتم با کمترین مقدار key)
    """
    ...

def sum(iterable: Iterable, start: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    sum([12, 30, 40, 10])    ← 92

    📌 پارامترها:
    - iterable: لیست/تاپل اعداد
    - start (اختیاری): مقدار شروع — پیش‌فرض 0

    📌 برمی‌گردونه: مجموع
    """
    ...

@overload
def sorted(
    iterable: Iterable[T],
    *,
    key: Optional[Callable[[T], Any]] = ...,
    reverse: bool = ...
) -> list: ...
@overload
def sorted(
    iterable: Iterable[T],
    cmp: Callable[[T, T], int],
    *,
    key: Optional[Callable[[T], Any]] = ...,
    reverse: bool = ...
) -> list: ...
def sorted(iterable: Iterable, *args: Any, **kwargs: Any) -> list:
    """
    📌 فرمول رایج:
    sorted([3, 1, 2])                    ← [1, 2, 3]
    sorted([3, 1, 2], reverse=True)      ← [3, 2, 1]
    sorted(contours, key=cv2.contourArea, reverse=True)

    📌 پارامترها:
    - iterable: لیست/تاپل/مجموعه
    - key (اختیاری): تابع کلید برای مرتب‌سازی
    - reverse (اختیاری): True برای نزولی

    📌 نکته: لیست اصلی را تغییر نمی‌دهد (برخلاف list.sort())
    """
    ...

# ============================================================
# enumerate
# ============================================================
def enumerate(iterable: Iterable, start: int = ...) -> Iterable[tuple]:
    """
    📌 فرمول رایج:
    for index, item in enumerate(my_list):
        print(index, item)

    📌 پارامترها:
    - iterable: لیست، تاپل، رشته و ...
    - start (اختیاری): شروع شمارش — پیش‌فرض 0

    📌 برمی‌گردونه: جفت‌های (index, value)

    📌 [CV] پیمایش دیتاست با ایندکس:
    for idx, path in enumerate(image_paths):
        print(f"processing image {idx}: {path}")
    """
    ...

# ============================================================
# zip
# ============================================================
def zip(*iterables: Iterable) -> Iterable[tuple]:
    """
    📌 فرمول رایج:
    for a, b in zip(list1, list2):
        print(a, b)

    list(zip([1, 2], ["a", "b"]))    ← [(1, 'a'), (2, 'b')]

    📌 نکته: از کوتاه‌ترین لیست پیروی می‌کند

    📌 [CV] جفت کردن تصویر و لیبل:
    for img, label in zip(images, labels):
        ...
    """
    ...

# ============================================================
# input
# ============================================================
def input(prompt: Optional[str] = ...) -> str:
    """
    📌 فرمول رایج:
    name = input("Enter your name: ")

    📌 پارامترها:
    - prompt (اختیاری): پیام نمایشی

    📌 برمی‌گردونه: رشته — همیشه! (برای عدد باید int/float کنی)
    """
    ...

# ============================================================
# any / all
# ============================================================
def any(iterable: Iterable) -> bool:
    """
    📌 فرمول رایج:
    any([False, False, True])    ← True
    any([])                       ← False

    📌 برمی‌گردونه: True اگر حداقل یک عنصر True باشد

    📌 [CV] بررسی وجود حداقل یک تصویر خراب:
    has_broken = any(img is None for img in images)
    """
    ...

def all(iterable: Iterable) -> bool:
    """
    📌 فرمول رایج:
    all([True, True, True])      ← True
    all([True, False, True])     ← False
    all([])                       ← True   (توجه!)

    📌 برمی‌گردونه: True اگر همه عناصر True باشند

    📌 [CV] بررسی اطمینان همه پیش‌بینی‌ها:
    all_confident = all(c > 0.8 for c in confidences)
    """
    ...

# ============================================================
# isinstance / issubclass / callable
# ============================================================
def isinstance(obj: Any, class_or_tuple: Union[type, tuple]) -> bool:
    """
    📌 فرمول رایج:
    isinstance(5, int)           ← True
    isinstance("hi", str)        ← True
    isinstance(5, (int, float))  ← True

    📌 برمی‌گردونه: True اگر obj از نوع مشخص شده باشد

    📌 نکته: isinstance بهتر از type() == است، چون ارث‌بری را
    در نظر می‌گیرد.
    """
    ...

def issubclass(cls: type, class_or_tuple: Any) -> bool:
    """
    📌 فرمول رایج:
    issubclass(bool, int)    ← True

    📌 بررسی ارث‌بری یک کلاس از کلاس دیگر.
    """
    ...

def callable(obj: Any) -> bool:
    """
    📌 فرمول رایج:
    callable(print)    ← True
    callable(5)        ← False

    📌 بررسی اینکه آیا یک شیء قابل فراخوانی است یا نه.
    """
    ...

# ============================================================
# open
# ============================================================
def open(
    file: Union[str, bytes, int],
    mode: str = ...,
    buffering: int = ...,
    encoding: Optional[str] = ...,
    errors: Optional[str] = ...,
    newline: Optional[str] = ...,
    closefd: bool = ...,
    opener: Optional[Callable] = ...,
) -> Any:
    """
    📌 فرمول رایج:
    with open("file.txt", "r", encoding="utf-8") as f:
        content = f.read()

    📌 پارامترها:
    - file: مسیر فایل
    - mode: 'r' خواندن | 'w' نوشتن | 'a' افزودن | 'rb' باینری
    - encoding: 'utf-8' برای متن فارسی

    📌 نکته: همیشه با with استفاده کن تا فایل خودکار بسته شود

    📌 [CV] برای خواندن تصویر باینری از mode='rb' استفاده کن:
    with open("image.jpg", "rb") as f:
        data = f.read()
    """
    ...

# ============================================================
# abs / round / divmod / pow
# ============================================================
def abs(x: Any) -> Any:
    """
    📌 فرمول رایج:
    abs(-5)          ← 5
    abs(-2.5)        ← 2.5
    abs(3.14)        ← 3.14

    📌 برمی‌گردونه: قدر مطلق (مقدار بدون علامت)
    """
    ...

def round(number: float, ndigits: Optional[int] = ...) -> Any:
    """
    📌 فرمول رایج:
    round(3.14159, 2)     ← 3.14
    round(3.7)            ← 4
    round(2.5)            ← 2    (banker's rounding)

    📌 برای گرد کردن دقیق‌تر در CV از f-string استفاده کن:
    f"{value:.2f}"
    """
    ...

def divmod(a: Any, b: Any) -> tuple:
    """
    📌 فرمول رایج:
    divmod(10, 3)    ← (3, 1)   # (خارج قسمت، باقی‌مانده)
    divmod(20, 5)    ← (4, 0)
    """
    ...

def pow(base: Any, exp: Any, mod: Optional[Any] = ...) -> Any:
    """
    📌 فرمول رایج:
    pow(2, 3)        ← 8
    pow(2, 3, 5)     ← 3     # 2**3 % 5
    """
    ...

# ============================================================
# iter / next / map / filter / reversed
# ============================================================
def iter(obj: Iterable) -> Any:
    """
    📌 فرمول رایج:
    it = iter([1, 2, 3])
    next(it)             ← 1
    next(it)             ← 2
    """
    ...

def next(iterator: Any, default: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    next(iter([1, 2, 3]))     ← 1
    next(iter([]), "end")     ← "end"

    📌 بدون default → StopIteration وقتی تمام شود.
    """
    ...

def map(func: Callable, *iterables: Iterable) -> Any:
    """
    📌 فرمول رایج:
    list(map(int, ["1", "2", "3"]))    ← [1, 2, 3]

    📌 برمی‌گردونه iterator، نه لیست.
    📌 معادل کامپرهنشن: [func(x) for x in data]
    """
    ...

def filter(func: Optional[Callable], iterable: Iterable) -> Any:
    """
    📌 فرمول رایج:
    list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   ← [2, 4]

    📌 معادل کامپرهنشن: [x for x in data if condition(x)]
    """
    ...

def reversed(seq: Any) -> Any:
    """
    📌 فرمول رایج:
    list(reversed([1, 2, 3]))    ← [3, 2, 1]

    📌 برمی‌گردونه iterator، نه لیست.
    """
    ...

# ============================================================
# bin / oct / hex
# ============================================================
def bin(x: int) -> str:
    """
    📌 فرمول رایج:
    bin(10)     ← '0b1010'
    """
    ...

def oct(x: int) -> str:
    """
    📌 فرمول رایج:
    oct(10)     ← '0o12'
    """
    ...

def hex(x: int) -> str:
    """
    📌 فرمول رایج:
    hex(255)    ← '0xff'

    📌 [CV] نمایش کد رنگ RGB:
    hex(0xFF0000)    ← '0xff0000' (قرمز)
    """
    ...

# ============================================================
# repr / hash / id / format
# ============================================================
def repr(obj: Any) -> str:
    """
    📌 فرمول رایج:
    repr("hello")     ← "'hello'"
    repr([1, 2])      ← "[1, 2]"

    📌 تفاوت با str: repr برای دیباگ، str برای نمایش کاربر.
    """
    ...

def hash(obj: Any) -> int:
    """
    📌 فرمول رایج:
    hash("hello")    ← مقدار hash

    📌 فقط اشیاء تغییرناپذیر قابل hash هستند.
    """
    ...

def id(obj: Any) -> int:
    """
    📌 فرمول رایج:
    id(x)    ← آدرس حافظه

    📌 x is y  معادل  id(x) == id(y)
    """
    ...

def format(value: Any, format_spec: str = ...) -> str:
    """
    📌 فرمول رایج:
    format(3.14159, ".2f")    ← "3.14"
    format(255, "08b")        ← "11111111"

    📌 معادل f-string: f"{value:.2f}"
    """
    ...

# ============================================================
# super
# ============================================================
def super() -> Any:
    """
    📌 فرمول رایج در ارث‌بری:
    class Car(Vehicle):
        def __init__(self, brand, model, year, doors):
            super().__init__(brand, model, year)
            self.doors = doors

    📌 برای فراخوانی متد کلاس والد استفاده می‌شود.
    """
    ...

# ============================================================
# vars / dir / globals / locals
# ============================================================
def vars(obj: Any = ...) -> dict:
    """📌 vars(obj) ← __dict__ شیء"""
    ...

def dir(obj: Any = ...) -> list:
    """📌 dir("hello") ← لیست متدهای رشته"""
    ...

def globals() -> dict:
    """📌 متغیرهای سراسری به شکل دیکشنری."""
    ...

def locals() -> dict:
    """📌 متغیرهای محلی به شکل دیکشنری."""
    ...

# ============================================================
# getattr / setattr / hasattr / delattr
# ============================================================
def getattr(obj: Any, name: str, default: Any = ...) -> Any:
    """📌 getattr(img, "shape", None)"""
    ...

def setattr(obj: Any, name: str, value: Any) -> None:
    """📌 setattr(obj, "threshold", 0.5)"""
    ...

def hasattr(obj: Any, name: str) -> bool:
    """📌 hasattr(img, "shape") ← True"""
    ...

def delattr(obj: Any, name: str) -> None:
    """📌 delattr(obj, "temp")"""
    ...

# ============================================================
# eval / exec / compile
# ============================================================
def eval(source: Any, globals: Any = ..., locals: Any = ...) -> Any:
    """
    📌 eval("2 + 3") ← 5

    ⚠️ خطر امنیتی: هرگز روی ورودی کاربر استفاده نکن.

    📌 نکته: برای تست NameError در try/except، به جای متغیر
    تعریف‌نشده که Pylance خطا می‌ده، از eval("undefined_var")
    استفاده کن.
    """
    ...

def exec(source: Any, globals: Any = ..., locals: Any = ...) -> None:
    """
    📌 اجرای کد پایتون از رشته.

    ⚠️ خطر امنیتی: هرگز روی ورودی کاربر استفاده نکن.
    """
    ...

def compile(source: Any, filename: str, mode: str) -> Any:
    """📌 کامپایل کد به bytecode."""
    ...
# ============================================================
# type
# ============================================================
class type:
    """
    📌 فرمول رایج:
    type(5)          ← <class 'int'>
    type("hi")       ← <class 'str'>
    type([1, 2])     ← <class 'list'>

    📌 نکته: برای بررسی نوع، isinstance بهتر است:
    isinstance(5, int)    ✅
    type(5) == int        ⚠️ (در ارث‌بری مشکل دارد)
    """
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __call__(self, *args: Any, **kwargs: Any) -> Any: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __name__(self) -> str: ...
    def __qualname__(self) -> str: ...
    def __module__(self) -> str: ...
    def __bases__(self) -> tuple: ...
    def __mro__(self) -> tuple: ...
    def __subclasses__(self) -> list: ...
    def __instancecheck__(self, instance: Any) -> bool: ...
    def __subclasscheck__(self, subclass: Any) -> bool: ...

# ============================================================
# property
# ============================================================
class property:
    """
    📌 فرمول رایج:
    class Circle:
        def __init__(self, r):
            self._r = r

        @property
        def area(self):
            return 3.14 * self._r ** 2

    📌 property یک متد را مثل attribute قابل دسترسی می‌کند.
    """
    def __init__(
        self,
        fget: Optional[Callable] = ...,
        fset: Optional[Callable] = ...,
        fdel: Optional[Callable] = ...,
        doc: Optional[str] = ...,
    ) -> None: ...
    def getter(self, fget: Callable) -> property:
        """
        📌 فرمول رایج:
        @property
        def x(self):
            return self._x

        @x.getter
        def x(self):
            return self._x
        """
        ...
    def setter(self, fset: Callable) -> property:
        """
        📌 فرمول رایج:
        @x.setter
        def x(self, value):
            self._x = value
        """
        ...
    def deleter(self, fdel: Callable) -> property:
        """📌 @x.deleter برای تعریف حذف attribute."""
        ...
    def __get__(self, obj: Any, objtype: Any = ...) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...
    def __delete__(self, obj: Any) -> None: ...

# ============================================================
# staticmethod / classmethod
# ============================================================
class staticmethod:
    """
    📌 فرمول رایج:
    class Utils:
        @staticmethod
        def add(a, b):
            return a + b

    Utils.add(2, 3)    ← بدون نیاز به ساخت نمونه
    """
    def __init__(self, f: Callable) -> None: ...
    def __get__(self, obj: Any, objtype: Any = ...) -> Any: ...

class classmethod:
    """
    📌 فرمول رایج:
    class Dataset:
        @classmethod
        def from_folder(cls, path):
            return cls(...)

    📌 پارامتر اول cls است، نه self.
    """
    def __init__(self, f: Callable) -> None: ...
    def __get__(self, obj: Any, objtype: Any = ...) -> Any: ...

# ============================================================
# Exception classes
# ============================================================
class BaseException:
    """📌 ریشه همه Exception ها."""
    def __init__(self, *args: Any) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def with_traceback(self, tb: Any) -> BaseException: ...
    @property
    def args(self) -> tuple: ...
    @property
    def __traceback__(self) -> Any: ...

class Exception(BaseException):
    """📌 ریشه Exception های معمولی."""
    def __init__(self, *args: Any) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

class ValueError(Exception):
    """📌 مقدار نامعتبر. int("nana") → ValueError"""
    def __init__(self, *args: Any) -> None: ...

class TypeError(Exception):
    """📌 نوع ناسازگار. 5 + "hello" → TypeError"""
    def __init__(self, *args: Any) -> None: ...

class KeyError(Exception):
    """📌 کلید دیکشنری وجود ندارد. {"a": 1}["b"] → KeyError"""
    def __init__(self, *args: Any) -> None: ...

class IndexError(Exception):
    """📌 ایندکس خارج محدوده. [1,2,3][10] → IndexError"""
    def __init__(self, *args: Any) -> None: ...

class AttributeError(Exception):
    """📌 attribute وجود ندارد. (5).append(1) → AttributeError"""
    def __init__(self, *args: Any) -> None: ...

class ImportError(Exception):
    """📌 ماژول پیدا نمی‌شود."""
    def __init__(self, *args: Any) -> None: ...

class ModuleNotFoundError(ImportError):
    """📌 ماژول مشخص پیدا نمی‌شود."""
    def __init__(self, *args: Any) -> None: ...

class FileNotFoundError(OSError):
    """📌 [CV] بسیار رایج: مسیر تصویر اشتباه."""
    def __init__(self, *args: Any) -> None: ...

class IOError(OSError):
    """📌 خطای ورودی/خروجی (نام قدیمی OSError)."""
    def __init__(self, *args: Any) -> None: ...

class OSError(Exception):
    """📌 خطای سیستم‌عامل. پایه FileNotFound, Permission, ..."""
    def __init__(self, *args: Any) -> None: ...

class FileExistsError(OSError):
    """📌 فایل از قبل وجود دارد."""
    def __init__(self, *args: Any) -> None: ...

class PermissionError(OSError):
    """📌 [CV] دسترسی به فایل/پوشه وجود ندارد."""
    def __init__(self, *args: Any) -> None: ...

class IsADirectoryError(OSError):
    """📌 عملیات فایل روی دایرکتوری."""
    def __init__(self, *args: Any) -> None: ...

class NotADirectoryError(OSError):
    """📌 عملیات دایرکتوری روی فایل."""
    def __init__(self, *args: Any) -> None: ...

class InterruptedError(OSError):
    """📌 عملیات وقفه خورد."""
    def __init__(self, *args: Any) -> None: ...

class ConnectionError(OSError):
    """📌 خطای اتصال."""
    def __init__(self, *args: Any) -> None: ...

class TimeoutError(OSError):
    """📌 عملیات timeout شد."""
    def __init__(self, *args: Any) -> None: ...

class RuntimeError(Exception):
    """📌 خطای عمومی زمان اجرا."""
    def __init__(self, *args: Any) -> None: ...

class NotImplementedError(RuntimeError):
    """📌 متد یا تابع پیاده‌سازی نشده."""
    def __init__(self, *args: Any) -> None: ...

class RecursionError(RuntimeError):
    """📌 بازگشت بی‌نهایت."""
    def __init__(self, *args: Any) -> None: ...

class ZeroDivisionError(ArithmeticError):
    """📌 تقسیم بر صفر. 10/0 → ZeroDivisionError"""
    def __init__(self, *args: Any) -> None: ...

class ArithmeticError(Exception):
    """📌 پایه خطاهای حسابی."""
    def __init__(self, *args: Any) -> None: ...

class OverflowError(ArithmeticError):
    """📌 سرریز عددی."""
    def __init__(self, *args: Any) -> None: ...

class FloatingPointError(ArithmeticError):
    """📌 خطای نقطه شناور."""
    def __init__(self, *args: Any) -> None: ...

class NameError(Exception):
    """📌 متغیر تعریف‌نشده."""
    def __init__(self, *args: Any) -> None: ...

class UnboundLocalError(NameError):
    """📌 متغیر محلی قبل از تخصیص استفاده شده."""
    def __init__(self, *args: Any) -> None: ...

class StopIteration(Exception):
    """📌 پایان iterator. next(iter([])) → StopIteration"""
    def __init__(self, *args: Any) -> None: ...

class StopAsyncIteration(Exception):
    """📌 پایان iterator async."""
    def __init__(self, *args: Any) -> None: ...

class AssertionError(Exception):
    """📌 assert نادرست."""
    def __init__(self, *args: Any) -> None: ...

class LookupError(Exception):
    """📌 پایه KeyError و IndexError."""
    def __init__(self, *args: Any) -> None: ...

class SyntaxError(Exception):
    """📌 خطای سینتکس."""
    def __init__(self, *args: Any) -> None: ...

class IndentationError(SyntaxError):
    """📌 خطای تورفتگی."""
    def __init__(self, *args: Any) -> None: ...

class TabError(IndentationError):
    """📌 ترکیب tab و space."""
    def __init__(self, *args: Any) -> None: ...

class SystemError(Exception):
    """📌 خطای داخلی مفسر."""
    def __init__(self, *args: Any) -> None: ...

class UnicodeError(ValueError):
    """📌 پایه خطاهای یونیکد."""
    def __init__(self, *args: Any) -> None: ...

class UnicodeDecodeError(UnicodeError):
    """📌 خطای decode یونیکد."""
    def __init__(self, *args: Any) -> None: ...

class UnicodeEncodeError(UnicodeError):
    """📌 [CV] خطای encode یونیکد — مثل خطای cp1252 ویندوز."""
    def __init__(self, *args: Any) -> None: ...

class UnicodeTranslateError(UnicodeError):
    """📌 خطای translate یونیکد."""
    def __init__(self, *args: Any) -> None: ...

class KeyboardInterrupt(BaseException):
    """📌 Ctrl+C توسط کاربر."""
    def __init__(self, *args: Any) -> None: ...

class SystemExit(BaseException):
    """📌 sys.exit() یا پایان اسکریپت."""
    def __init__(self, *args: Any) -> None: ...

class GeneratorExit(BaseException):
    """📌 خروج ژنراتور."""
    def __init__(self, *args: Any) -> None: ...

class Warning(Exception):
    """📌 پایه هشدارها."""
    def __init__(self, *args: Any) -> None: ...

# ============================================================
# object
# ============================================================
class object:
    """📌 ریشه همه کلاس‌ها."""
    def __init__(self) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __format__(self, format_spec: str) -> str: ...
    def __sizeof__(self) -> int: ...
    def __reduce__(self) -> Any: ...
    def __reduce_ex__(self, protocol: int) -> Any: ...
    def __dir__(self) -> list: ...
    def __init_subclass__(cls) -> None: ...

# ============================================================
# int
# ============================================================
class int:
    """
    📌 مثال:
    x = 10
    y = int("20")

    📌 [CV] ایندکس و شمارنده.
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: Union[str, float, int, bool, bytes]) -> None: ...
    @overload
    def __init__(self, x: str, base: int) -> None: ...
    def __add__(self, other: Any) -> int: ...
    def __sub__(self, other: Any) -> int: ...
    def __mul__(self, other: Any) -> int: ...
    def __truediv__(self, other: Any) -> float: ...
    def __floordiv__(self, other: Any) -> int: ...
    def __mod__(self, other: Any) -> int: ...
    def __pow__(self, other: Any) -> int: ...
    def __neg__(self) -> int: ...
    def __pos__(self) -> int: ...
    def __abs__(self) -> int: ...
    def __invert__(self) -> int: ...
    def __and__(self, other: Any) -> int: ...
    def __or__(self, other: Any) -> int: ...
    def __xor__(self, other: Any) -> int: ...
    def __lshift__(self, other: Any) -> int: ...
    def __rshift__(self, other: Any) -> int: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def bit_length(self) -> int:
        """
        📌 فرمول رایج:
        (10).bit_length()    ← 4   (1010 در باینری، 4 بیت)

        📌 برمی‌گردونه: تعداد بیت‌های لازم برای نمایش عدد.
        """
        ...
    def to_bytes(self, length: int, byteorder: str, *, signed: bool = ...) -> bytes:
        """
        📌 فرمول رایج:
        (255).to_bytes(2, "big")     ← b'\\x00\\xff'
        (255).to_bytes(2, "little")  ← b'\\xff\\x00'
        """
        ...

# ============================================================
# float
# ============================================================
class float:
    """
    📌 [CV] اعداد اعشاری برای confidence، نرمال‌سازی.

    📌 فرمت در f-string:
    f"{value:.2f}"     ← دو رقم اعشار
    f"{value:.1%}"     ← درصد
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: Union[str, float, int, bool]) -> None: ...
    def __add__(self, other: Any) -> float: ...
    def __sub__(self, other: Any) -> float: ...
    def __mul__(self, other: Any) -> float: ...
    def __truediv__(self, other: Any) -> float: ...
    def __floordiv__(self, other: Any) -> float: ...
    def __mod__(self, other: Any) -> float: ...
    def __pow__(self, other: Any) -> float: ...
    def __neg__(self) -> float: ...
    def __pos__(self) -> float: ...
    def __abs__(self) -> float: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: Any) -> bool: ...
    def __le__(self, other: Any) -> bool: ...
    def __gt__(self, other: Any) -> bool: ...
    def __ge__(self, other: Any) -> bool: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def is_integer(self) -> bool:
        """
        📌 فرمول رایج:
        (3.0).is_integer()    ← True
        (3.14).is_integer()   ← False

        📌 بررسی اینکه float مقدار صحیح است یا نه.
        """
        ...
    def hex(self) -> str:
        """📌 (3.14).hex() ← '0x1.91eb851eb851fp+1'"""
        ...

# ============================================================
# complex
# ============================================================
class complex:
    """📌 اعداد مختلط (کم‌کاربرد در CV جونیور)."""
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, real: float, imag: float = ...) -> None: ...
    @overload
    def __init__(self, real: str) -> None: ...
    def real(self) -> float: ...
    def imag(self) -> float: ...
    def conjugate(self) -> complex:
        """
        📌 فرمول رایج:
        (3+4j).conjugate()    ← (3-4j)

        📌 مزدوج مختلط.
        """
        ...
    def __add__(self, other: Any) -> complex: ...
    def __sub__(self, other: Any) -> complex: ...
    def __mul__(self, other: Any) -> complex: ...
    def __truediv__(self, other: Any) -> complex: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __abs__(self) -> float: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...

# ============================================================
# bool
# ============================================================
class bool:
    """
    📌 فقط True و False.
    📌 bool زیرکلاس int است: True == 1, False == 0.

    📌 مقادیر falsy: 0, 0.0, "", [], {}, (), set(), None, False

    📌 [CV] ماسک باینری و شرط confidence.
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: Any) -> None: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __and__(self, other: Any) -> bool: ...
    def __or__(self, other: Any) -> bool: ...
    def __xor__(self, other: Any) -> bool: ...
    def __invert__(self) -> bool: ...
    def __int__(self) -> int: ...
    def __float__(self) -> float: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...

# ============================================================
# str
# ============================================================
class str:
    """
    📌 رشته تغییرناپذیر.

    📌 [CV] مسیر فایل، پارس لاگ، CSV.

    📌 فرمت‌بندی با f-string:
    f"{name}_{version}"
    f"{accuracy:.2f}"
    f"{accuracy:.1%}"
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, x: Any) -> None: ...
    @overload
    def __init__(self, x: bytes, encoding: str = ..., errors: str = ...) -> None: ...
    def __add__(self, other: str) -> str: ...
    def __mul__(self, other: int) -> str: ...
    def __mod__(self, other: Any) -> str: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: str) -> bool: ...
    def __le__(self, other: str) -> bool: ...
    def __gt__(self, other: str) -> bool: ...
    def __ge__(self, other: str) -> bool: ...
    def __len__(self) -> int: ...
    def __contains__(self, other: str) -> bool: ...
    def __getitem__(self, index: Union[int, slice]) -> str: ...
    def __iter__(self) -> Any: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

    def encode(self, encoding: str = ..., errors: str = ...) -> bytes:
        """
        📌 فرمول رایج:
        "hello".encode("utf-8")    ← b'hello'

        📌 تبدیل رشته به bytes (برای نوشتن در فایل باینری).
        """
        ...

    def format(self, *args: Any, **kwargs: Any) -> str:
        """
        📌 فرمول رایج (روش قدیمی، قبل از f-string):
        "{}: {}".format("acc", 0.95)    ← "acc: 0.95"
        "{name}: {value}".format(name="acc", value=0.95)

        📌 در پایتون 3.6+ از f-string استفاده کن.
        """
        ...

    def format_map(self, mapping: Any) -> str:
        """📌 "{name}".format_map({"name": "yolo"}) ← 'yolo'"""
        ...

    def split(self, sep: Optional[str] = ..., maxsplit: int = ...) -> list:
        """
        📌 فرمول رایج:
        "Ann Jon Alex".split()             ← ['Ann', 'Jon', 'Alex']
        "44-22-44-11".split("-")           ← ['44', '22', '44', '11']
        "a.b.c".split(".")                 ← ['a', 'b', 'c']

        📌 پارامترها:
        - sep: جداکننده (پیش‌فرض: هر فاصله‌ای)
        - maxsplit: حداکثر تعداد تقسیم

        📌 [CV] پارس مسیر فایل:
        "data/train/cat.jpg".split("/")    ← ['data', 'train', 'cat.jpg']

        📌 [CV] پارس CSV:
        "name,age,city".split(",")         ← ['name', 'age', 'city']
        """
        ...

    def rsplit(self, sep: Optional[str] = ..., maxsplit: int = ...) -> list:
        """
        📌 فرمول رایج:
        "a.b.c".rsplit(".", 1)    ← ['a.b', 'c']

        📌 مثل split ولی از راست شروع می‌کند.
        """
        ...

    def splitlines(self, keepends: bool = ...) -> list:
        """📌 "line1\\nline2\\nline3".splitlines() ← ['line1', 'line2', 'line3']"""
        ...

    def join(self, iterable: Iterable[str]) -> str:
        """
        📌 فرمول رایج:
        "--".join(['a', 'b', 'c'])    ← 'a--b--c'
        "".join(['a', 'b', 'c'])      ← 'abc'
        "/".join(["data", "train"])   ← 'data/train'

        📌 [CV] ساخت مسیر:
        "/".join(["data", "train", "cat.jpg"])    ← 'data/train/cat.jpg'
        """
        ...

    def replace(self, old: str, new: str, count: int = ...) -> str:
        """
        📌 فرمول رایج:
        "hello".replace("l", "L")        ← 'heLLo'
        "hello".replace("l", "L", 1)     ← 'heLlo'

        ⚠️ رشته تغییرناپذیر است، پس نیاز به self-assignment دارد:
        s = "hello"
        s.replace("h", "j")              # s تغییر نمی‌کند
        s = s.replace("h", "j")          # حالا درست
        """
        ...

    def find(self, sub: str, start: int = ..., end: int = ...) -> int:
        """
        📌 فرمول رایج:
        "hello".find("l")     ← 2
        "hello".find("z")     ← -1   (اگر نباشد)

        📌 برمی‌گردونه: ایندکس اولین occurrence، یا -1 اگر نبود.
        """
        ...

    def rfind(self, sub: str, start: int = ..., end: int = ...) -> int:
        """📌 مثل find ولی از راست جستجو می‌کند."""
        ...

    def index(self, sub: str, start: int = ..., end: int = ...) -> int:
        """
        📌 مثل find ولی اگر نباشد ValueError می‌دهد.
        """
        ...

    def rindex(self, sub: str, start: int = ..., end: int = ...) -> int:
        """📌 مثل index ولی از راست."""
        ...

    def count(self, sub: str, start: int = ..., end: int = ...) -> int:
        """
        📌 فرمول رایج:
        "hello".count("l")    ← 2
        "a.b.c".count(".")    ← 2
        """
        ...

    def startswith(self, prefix: Union[str, tuple], start: int = ..., end: int = ...) -> bool:
        """
        📌 فرمول رایج:
        "cat.jpg".startswith("cat")    ← True
        "img.png".startswith(("cat", "dog"))   ← False

        📌 [CV] فیلتر فایل‌ها:
        [f for f in files if f.startswith("cat_")]
        """
        ...

    def endswith(self, suffix: Union[str, tuple], start: int = ..., end: int = ...) -> bool:
        """
        📌 فرمول رایج:
        "cat.jpg".endswith(".jpg")             ← True
        "img.png".endswith((".jpg", ".png"))   ← True

        📌 [CV] فیلتر پسوند:
        [f for f in files if f.endswith(".jpg")]
        """
        ...

    def lower(self) -> str:
        """
        📌 فرمول رایج:
        "Hello World".lower()    ← 'hello world'

        📌 [CV] نرمال‌سازی لیبل‌ها:
        "Cat".lower()            ← 'cat'
        """
        ...

    def upper(self) -> str:
        """📌 "hello".upper() ← 'HELLO'"""
        ...

    def title(self) -> str:
        """📌 "hello world".title() ← 'Hello World'"""
        ...

    def capitalize(self) -> str:
        """📌 "hello world".capitalize() ← 'Hello world'"""
        ...

    def casefold(self) -> str:
        """📌 مثل lower ولی برای مقایسه یونیکد."""
        ...

    def swapcase(self) -> str:
        """📌 "Hello".swapcase() ← 'hELLO'"""
        ...

    def center(self, width: int, fillchar: str = ...) -> str:
        """📌 "hi".center(10, "*") ← '****hi****'"""
        ...

    def ljust(self, width: int, fillchar: str = ...) -> str:
        """📌 "hi".ljust(10, "*") ← 'hi********'"""
        ...

    def rjust(self, width: int, fillchar: str = ...) -> str:
        """📌 "hi".rjust(10, "*") ← '********hi'"""
        ...

    def zfill(self, width: int) -> str:
        """📌 "42".zfill(5) ← '00042'"""
        ...

    def strip(self, chars: Optional[str] = ...) -> str:
        """
        📌 فرمول رایج:
        "  hello  ".strip()        ← 'hello'
        "xxhelloxx".strip("x")     ← 'hello'

        📌 [CV] پاک کردن whitespace از خطوط فایل:
        for line in f:
            line = line.strip()
        """
        ...

    def lstrip(self, chars: Optional[str] = ...) -> str:
        """📌 فقط از چپ: "  hi".lstrip() ← 'hi'"""
        ...

    def rstrip(self, chars: Optional[str] = ...) -> str:
        """📌 فقط از راست: "hi  ".rstrip() ← 'hi'"""
        ...

    def isdigit(self) -> bool:
        """📌 "123".isdigit() ← True ، "12.3".isdigit() ← False"""
        ...

    def isalpha(self) -> bool:
        """📌 "abc".isalpha() ← True"""
        ...

    def isalnum(self) -> bool:
        """📌 "abc123".isalnum() ← True"""
        ...

    def islower(self) -> bool:
        """📌 "abc".islower() ← True"""
        ...

    def isupper(self) -> bool:
        """📌 "ABC".isupper() ← True"""
        ...

    def isspace(self) -> bool:
        """📌 "   ".isspace() ← True"""
        ...

    def isnumeric(self) -> bool:
        """📌 مثل isdigit ولی ارقام یونیکد را هم شامل می‌شود."""
        ...

    def isdecimal(self) -> bool:
        """📌 فقط ارقام اعشاری (0-9)."""
        ...

    def isidentifier(self) -> bool:
        """📌 "my_var".isidentifier() ← True"""
        ...

    def isprintable(self) -> bool:
        """📌 بررسی قابل چاپ بودن."""
        ...

    def istitle(self) -> bool:
        """📌 "Hello World".istitle() ← True"""
        ...

    def partition(self, sep: str) -> tuple:
        """📌 "a=b=c".partition("=") ← ('a', '=', 'b=c')"""
        ...

    def rpartition(self, sep: str) -> tuple:
        """📌 "a=b=c".rpartition("=") ← ('a=b', '=', 'c')"""
        ...

    def expandtabs(self, tabsize: int = ...) -> str:
        """📌 تبدیل tab به فاصله."""
        ...

# ============================================================
# bytes
# ============================================================
class bytes:
    """
    📌 [CV] خواندن فایل تصویر به صورت باینری.
    with open("img.jpg", "rb") as f:
        data = f.read()
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, int_value: int) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[int]) -> None: ...
    @overload
    def __init__(self, string: str, encoding: str = ..., errors: str = ...) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: Union[int, slice]) -> Union[int, bytes]: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: Union[int, bytes]) -> bool: ...
    def __add__(self, other: bytes) -> bytes: ...
    def __mul__(self, other: int) -> bytes: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: bytes) -> bool: ...
    def __le__(self, other: bytes) -> bool: ...
    def __gt__(self, other: bytes) -> bool: ...
    def __ge__(self, other: bytes) -> bool: ...
    def __hash__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...

    def decode(self, encoding: str = ..., errors: str = ...) -> str:
        """
        📌 فرمول رایج:
        b'hello'.decode("utf-8")    ← 'hello'

        📌 تبدیل bytes به رشته.
        """
        ...

    def hex(self) -> str:
        """📌 b'\\xff'.hex() ← 'ff'"""
        ...

    @classmethod
    def fromhex(cls, string: str) -> bytes:
        """📌 bytes.fromhex("ff") ← b'\\xff'"""
        ...

    def join(self, iterable: Iterable[bytes]) -> bytes:
        """📌 b",".join([b"a", b"b"]) ← b'a,b'"""
        ...

    def split(self, sep: Optional[bytes] = ..., maxsplit: int = ...) -> list:
        """📌 b"a,b,c".split(b",") ← [b'a', b'b', b'c']"""
        ...

    def rsplit(self, sep: Optional[bytes] = ..., maxsplit: int = ...) -> list:
        """📌 مثل split ولی از راست."""
        ...

    def startswith(self, prefix: Union[bytes, tuple]) -> bool:
        """📌 b"hello".startswith(b"he") ← True"""
        ...

    def endswith(self, suffix: Union[bytes, tuple]) -> bool:
        """📌 b"hello.jpg".endswith(b".jpg") ← True"""
        ...

    def find(self, sub: bytes, start: int = ..., end: int = ...) -> int: ...
    def rfind(self, sub: bytes, start: int = ..., end: int = ...) -> int: ...
    def count(self, sub: bytes, start: int = ..., end: int = ...) -> int: ...

    def replace(self, old: bytes, new: bytes, count: int = ...) -> bytes:
        """📌 b"hello".replace(b"l", b"L") ← b'heLLo'"""
        ...

    def strip(self, chars: Optional[bytes] = ...) -> bytes: ...
    def lstrip(self, chars: Optional[bytes] = ...) -> bytes: ...
    def rstrip(self, chars: Optional[bytes] = ...) -> bytes: ...
    def upper(self) -> bytes: ...
    def lower(self) -> bytes: ...
    def title(self) -> bytes: ...
    def capitalize(self) -> bytes: ...

# ============================================================
# bytearray
# ============================================================
class bytearray:
    """📌 نسخه تغییرپذیر bytes."""
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, source: Union[int, Iterable[int], bytes]) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> int: ...
    def __setitem__(self, index: int, value: int) -> None: ...
    def __iter__(self) -> Any: ...
    def append(self, item: int) -> None:
        """📌 افزودن یک بایت (عدد 0-255)."""
        ...
    def extend(self, iterable: Iterable[int]) -> None:
        """📌 افزودن چند بایت."""
        ...
    def decode(self, encoding: str = ..., errors: str = ...) -> str: ...

# ============================================================
# memoryview
# ============================================================
class memoryview:
    """📌 نمایش حافظه بدون کپی."""
    def __init__(self, obj: Any) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> Any: ...
    @property
    def shape(self) -> tuple: ...
    @property
    def format(self) -> str: ...
    @property
    def itemsize(self) -> int: ...
    @property
    def nbytes(self) -> int: ...

# ============================================================
# slice
# ============================================================
class slice:
    """
    📌 فرمول رایج:
    s = slice(1, 5, 2)
    my_list[s]        ← معادل my_list[1:5:2]
    """
    @overload
    def __init__(self, stop: int) -> None: ...
    @overload
    def __init__(
        self, start: Optional[int], stop: Optional[int], step: Optional[int] = ...
    ) -> None: ...
    def start(self) -> Optional[int]: ...
    def stop(self) -> Optional[int]: ...
    def step(self) -> Optional[int]: ...
    def indices(self, len: int) -> tuple: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> int: ...
    def __repr__(self) -> str: ...

# ============================================================
# range
# ============================================================
class range:
    """
    📌 فرمول رایج:
    range(5)              ← 0,1,2,3,4
    range(2, 10, 2)       ← 2,4,6,8
    range(10, 0, -1)      ← 10,9,...,1

    📌 [CV] پیمایش batch:
    for i in range(0, len(paths), batch_size):
        batch = paths[i:i+batch_size]
    """
    @overload
    def __init__(self, stop: int) -> None: ...
    @overload
    def __init__(self, start: int, stop: int, step: int = ...) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self) -> int: ...
    def __getitem__(self, index: int) -> int: ...
    def __contains__(self, item: int) -> bool: ...
    def __reversed__(self) -> Any: ...
    def count(self, value: int) -> int:
        """📌 range(5).count(2) ← 1"""
        ...
    def index(self, value: int) -> int:
        """📌 range(5).index(2) ← 2"""
        ...

# ============================================================
# list
# ============================================================
class list(Generic[T]):
    """
    📌 [CV] لیست مسیر تصاویر، لیست لیبل‌ها، لیست batch ها.

    📌 متدهای ضروری:
    - append, extend, insert, pop, remove, clear
    - index, count, sort, reverse, copy
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[T]) -> None: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> list[T]: ...
    def __setitem__(self, index: int, value: T) -> None: ...
    def __delitem__(self, index: int) -> None: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: T) -> bool: ...
    def __add__(self, other: list[T]) -> list[T]: ...
    def __mul__(self, other: int) -> list[T]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: list[T]) -> bool: ...
    def __le__(self, other: list[T]) -> bool: ...
    def __gt__(self, other: list[T]) -> bool: ...
    def __ge__(self, other: list[T]) -> bool: ...
    def __hash__(self) -> None: ...

    def append(self, x: T) -> None:
        """
        📌 فرمول رایج:
        users = ["jeremy", "adam", "Liza"]
        users.append("sara")    ← ["jeremy", "adam", "Liza", "sara"]

        📌 به آخر لیست اضافه می‌کند (بدون self-assignment).

        📌 [CV] افزودن مسیر تصویر:
        image_paths = []
        image_paths.append("cat.jpg")
        """
        ...

    def extend(self, iterable: Iterable[T]) -> None:
        """
        📌 فرمول رایج:
        a = [1, 2]
        a.extend([3, 4])    ← [1, 2, 3, 4]

        📌 تفاوت با append:
        a.append([3, 4])    ← [1, 2, [3, 4]]    (لیست تودرتو)
        a.extend([3, 4])    ← [1, 2, 3, 4]      (تخت شده)
        """
        ...

    def insert(self, index: int, x: T) -> None:
        """
        📌 فرمول رایج:
        users = ["jeremy", "adam", "Liza"]
        users.insert(2, "Erik")    ← ["jeremy", "adam", "Erik", "Liza"]

        📌 در ایندکس مشخص درج می‌کند (بقیه جابه‌جا می‌شوند).
        """
        ...

    def remove(self, x: T) -> None:
        """
        📌 فرمول رایج:
        a = [1, 2, 3, 2]
        a.remove(2)    ← [1, 3, 2]

        📌 اولین occurrence را حذف می‌کند.
        ⚠️ اگر مقدار نباشد ValueError می‌دهد.
        """
        ...

    def pop(self, index: int = ...) -> T:
        """
        📌 فرمول رایج:
        fruits = ["apple", "orange", "banana"]
        fruits.pop()       ← "banana" (حذف آخرین، برگرداندن آن)
        fruits.pop(0)      ← "apple"  (حذف ایندکس 0)

        📌 [CV] حذف آخرین تصویر از لیست:
        image_paths.pop()

        📌 برمی‌گردونه: مقدار حذف‌شده (می‌توانی ذخیره‌اش کنی).
        """
        ...

    def clear(self) -> None:
        """📌 a.clear() ← [] (خالی کردن لیست)"""
        ...

    def index(self, x: T) -> int:
        """
        📌 فرمول رایج:
        [10, 20, 30].index(20)    ← 1

        📌 برمی‌گردونه: ایندکس اولین occurrence.
        ⚠️ اگر نباشد ValueError می‌دهد.
        """
        ...

    def count(self, x: T) -> int:
        """
        📌 فرمول رایج:
        [1, 2, 2, 3].count(2)    ← 2

        📌 تعداد occurrence های x.
        """
        ...

    def sort(
        self, key: Optional[Callable[[T], Any]] = ..., reverse: bool = ...
    ) -> None:
        """
        📌 فرمول رایج:
        scores = [10, 9.25, 8, 4.5]
        scores.sort()                  ← [4.5, 8, 9.25, 10]
        scores.sort(reverse=True)      ← [10, 9.25, 8, 4.5]

        📌 با key سفارشی:
        samples.sort(key=lambda s: s["confidence"], reverse=True)

        ⚠️ لیست را درجا تغییر می‌دهد و None برمی‌گرداند.
        برای لیست جدید از sorted() استفاده کن.
        """
        ...

    def reverse(self) -> None:
        """
        📌 فرمول رایج:
        [1, 2, 3].reverse()    ← [3, 2, 1]

        📌 درجا معکوس می‌کند.
        """
        ...

    def copy(self) -> list[T]:
        """
        📌 فرمول رایج:
        a = [1, 2, 3]
        b = a.copy()    ← کپی مستقل

        📌 بدون این، b = a فقط ارجاع می‌دهد.
        """
        ...

# ============================================================
# tuple
# ============================================================
class tuple(Generic[T]):
    """
    📌 تغییرناپذیر (immutable).

    📌 [CV] مختصات، bounding box، بازگرداندن چند مقدار از تابع.
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[T]) -> None: ...
    def __len__(self) -> int: ...
    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> tuple[T, ...]: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: T) -> bool: ...
    def __add__(self, other: tuple[T, ...]) -> tuple[T, ...]: ...
    def __mul__(self, other: int) -> tuple[T, ...]: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: tuple[T, ...]) -> bool: ...
    def __le__(self, other: tuple[T, ...]) -> bool: ...
    def __gt__(self, other: tuple[T, ...]) -> bool: ...
    def __ge__(self, other: tuple[T, ...]) -> bool: ...
    def __hash__(self) -> int: ...

    def count(self, x: T) -> int:
        """📌 (1, 2, 2, 3).count(2) ← 2"""
        ...

    def index(self, x: T) -> int:
        """📌 (10, 20, 30).index(20) ← 1"""
        ...

# ============================================================
# dict
# ============================================================
class dict(Generic[K, V]):
    """
    📌 [CV] متادیتا: {"image": path, "label": label, "confidence": score}

    📌 متدهای ضروری:
    - keys, values, items, get, pop, update
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[tuple[K, V]]) -> None: ...
    @overload
    def __init__(self, **kwargs: V) -> None: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: K) -> V: ...
    def __setitem__(self, key: K, value: V) -> None: ...
    def __delitem__(self, key: K) -> None: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, key: K) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __hash__(self) -> None: ...

    def keys(self) -> Any:
        """
        📌 فرمول رایج:
        car = {"brand": "Toyota", "year": 2020}
        list(car.keys())    ← ['brand', 'year']

        📌 برای پیمایش:
        for key in car.keys():
            print(key)
        """
        ...

    def values(self) -> Any:
        """
        📌 فرمول رایج:
        list(car.values())    ← ['Toyota', 2020]

        📌 بررسی وجود مقدار:
        "Toyota" in car.values()    ← True
        """
        ...

    def items(self) -> Any:
        """
        📌 فرمول رایج:
        list(car.items())    ← [('brand', 'Toyota'), ('year', 2020)]

        📌 پیمایش کلید-مقدار:
        for key, value in car.items():
            print(f"{key}: {value}")

        📌 [CV] فیلتر دیکشنری:
        filtered = {k: v for k, v in annotations.items() if v > 0.5}
        """
        ...

    def get(self, key: K, default: Optional[V] = ...) -> Optional[V]:
        """
        📌 فرمول رایج:
        car = {"brand": "Toyota"}
        car.get("brand")           ← 'Toyota'
        car.get("color")           ← None
        car.get("color", "unknown") ← 'unknown'

        📌 دسترسی امن (بدون KeyError).
        """
        ...

    def update(self, other: dict[K, V]) -> None:
        """
        📌 فرمول رایج:
        car = {"brand": "Toyota"}
        car.update({"year": 2020, "color": "blue"})
        # ← {"brand": "Toyota", "year": 2020, "color": "blue"}

        📌 ادغام دو دیکشنری (کلیدهای تکراری overwrite می‌شوند).
        """
        ...

    def pop(self, key: K, default: Optional[V] = ...) -> Optional[V]:
        """
        📌 فرمول رایج:
        inventory = {"apples": 50, "oranges": 30}
        inventory.pop("oranges")           ← 30
        inventory.pop("missing")           ← KeyError
        inventory.pop("missing", "N/A")    ← 'N/A' (بدون خطا)

        📌 ⚠️ برخلاف لیست، pop() بدون آرگومان خطا می‌دهد.
        باید حتماً کلید بدهی.
        """
        ...

    def popitem(self) -> tuple[K, V]:
        """
        📌 فرمول رایج:
        inventory.popitem()    ← ('apples', 50) - آخرین جفت

        📌 آخرین جفت کلید-مقدار را حذف و برمی‌گرداند.
        """
        ...

    def clear(self) -> None:
        """📌 d.clear() ← {} (خالی کردن)"""
        ...

    def copy(self) -> dict[K, V]:
        """
        📌 کپی مستقل:
        d2 = d1.copy()
        """
        ...

    def setdefault(self, key: K, default: Optional[V] = ...) -> Optional[V]:
        """
        📌 فرمول رایج:
        car = {"brand": "Toyota"}
        car.setdefault("year", 2020)    ← 2020 (اضافه می‌شود)
        car.setdefault("brand", "X")    ← 'Toyota' (تغییر نمی‌کند)

        📌 اگر کلید موجود باشد، مقدار فعلی را برمی‌گرداند.
        📌 اگر نباشد، default را اضافه و برمی‌گرداند.
        """
        ...

# ============================================================
# set
# ============================================================
class set(Generic[T]):
    """
    📌 [CV] حذف تکراری‌ها از لیست لیبل‌ها:
    unique_labels = set(labels)

    📌 عملیات ریاضی:
    |, &, -, ^
    """
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[T]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: T) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __lt__(self, other: set[T]) -> bool: ...
    def __le__(self, other: set[T]) -> bool: ...
    def __gt__(self, other: set[T]) -> bool: ...
    def __ge__(self, other: set[T]) -> bool: ...
    def __or__(self, other: set[T]) -> set[T]: ...
    def __and__(self, other: set[T]) -> set[T]: ...
    def __sub__(self, other: set[T]) -> set[T]: ...
    def __xor__(self, other: set[T]) -> set[T]: ...
    def __hash__(self) -> None: ...

    def add(self, x: T) -> None:
        """
        📌 فرمول رایج:
        s = {1, 2}
        s.add(3)    ← {1, 2, 3}
        s.add(1)    ← {1, 2, 3}  (تکراری نادیده)

        📌 افزودن یک عضو (تکرار اضافه نمی‌شود).
        """
        ...

    def remove(self, x: T) -> None:
        """
        📌 فرمول رایج:
        s = {1, 2, 3}
        s.remove(2)    ← {1, 3}

        ⚠️ اگر نباشد KeyError می‌دهد.
        """
        ...

    def discard(self, x: T) -> None:
        """
        📌 فرمول رایج:
        s.discard(10)    ← بی‌خطر (خطا نمی‌دهد اگر نباشد)

        📌 مثل remove ولی امن.
        """
        ...

    def pop(self) -> T:
        """
        📌 فرمول رایج:
        s = {1, 2, 3}
        s.pop()    ← یک عضو تصادفی حذف و برگردانده می‌شود

        ⚠️ چون set ترتیب ندارد، نمی‌دانیم کدام حذف می‌شود.
        """
        ...

    def clear(self) -> None:
        """📌 s.clear() ← set() (خالی کردن)"""
        ...

    def update(self, *others: Iterable[T]) -> None:
        """
        📌 فرمول رایج:
        s = {1, 2}
        s.update([3, 4])       ← {1, 2, 3, 4}
        s.update({5}, {6})     ← {1, 2, 3, 4, 5, 6}

        📌 افزودن چند عضو یکجا.
        """
        ...

    def union(self, *others: set[T]) -> set[T]:
        """
        📌 فرمول رایج:
        {1, 2}.union({3, 4})    ← {1, 2, 3, 4}
        {1, 2} | {3, 4}         ← {1, 2, 3, 4}

        📌 اجتماع (بدون تغییر مجموعه اصلی).
        """
        ...

    def intersection(self, *others: set[T]) -> set[T]:
        """
        📌 فرمول رایج:
        {1, 2, 3}.intersection({2, 3, 4})    ← {2, 3}
        {1, 2, 3} & {2, 3, 4}                ← {2, 3}

        📌 اشتراک.
        """
        ...

    def difference(self, *others: set[T]) -> set[T]:
        """
        📌 فرمول رایج:
        {1, 2, 3}.difference({2, 3, 4})    ← {1}
        {1, 2, 3} - {2, 3, 4}              ← {1}

        📌 اعضایی که در اولی هستند ولی در دومی نیستند.
        """
        ...

    def symmetric_difference(self, other: set[T]) -> set[T]:
        """
        📌 فرمول رایج:
        {1, 2, 3}.symmetric_difference({2, 3, 4})    ← {1, 4}
        {1, 2, 3} ^ {2, 3, 4}                        ← {1, 4}

        📌 اعضایی که در یکی هستند ولی نه در هر دو.
        """
        ...

    def intersection_update(self, *others: set[T]) -> None:
        """📌 درجا اشتراک می‌گیرد."""
        ...

    def difference_update(self, *others: set[T]) -> None:
        """📌 درجا تفاضل می‌گیرد."""
        ...

    def symmetric_difference_update(self, other: set[T]) -> None:
        """📌 درجا تفاضل متقارن می‌گیرد."""
        ...

    def issubset(self, other: set[T]) -> bool:
        """
        📌 فرمول رایج:
        {1, 2}.issubset({1, 2, 3, 4})    ← True
        {1, 2} <= {1, 2, 3, 4}           ← True

        📌 آیا زیرمجموعه است؟
        """
        ...

    def issuperset(self, other: set[T]) -> bool:
        """
        📌 فرمول رایج:
        {1, 2, 3, 4}.issuperset({1, 2})    ← True

        📌 آیا فرامجموعه است؟
        """
        ...

    def isdisjoint(self, other: set[T]) -> bool:
        """
        📌 فرمول رایج:
        {1, 2}.isdisjoint({3, 4})    ← True
        {1, 2}.isdisjoint({2, 3})    ← False

        📌 آیا هیچ عضو مشترکی ندارند؟
        """
        ...

    def copy(self) -> set[T]:
        """📌 کپی مستقل."""
        ...

# ============================================================
# frozenset
# ============================================================
class frozenset(Generic[T]):
    """📌 نسخه تغییرناپذیر set. قابل استفاده به عنوان کلید دیکشنری."""
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, iterable: Iterable[T]) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: T) -> bool: ...
    def __eq__(self, other: Any) -> bool: ...
    def __ne__(self, other: Any) -> bool: ...
    def __or__(self, other: frozenset[T]) -> frozenset[T]: ...
    def __and__(self, other: frozenset[T]) -> frozenset[T]: ...
    def __sub__(self, other: frozenset[T]) -> frozenset[T]: ...
    def __xor__(self, other: frozenset[T]) -> frozenset[T]: ...
    def __hash__(self) -> int: ...
    def union(self, *others: frozenset[T]) -> frozenset[T]: ...
    def intersection(self, *others: frozenset[T]) -> frozenset[T]: ...
    def difference(self, *others: frozenset[T]) -> frozenset[T]: ...
    def symmetric_difference(self, other: frozenset[T]) -> frozenset[T]: ...
    def issubset(self, other: frozenset[T]) -> bool: ...
    def issuperset(self, other: frozenset[T]) -> bool: ...
    def isdisjoint(self, other: frozenset[T]) -> bool: ...
    def copy(self) -> frozenset[T]: ...