
# builtins.pyi — چیت‌شیت توابع داخلی پایتون
from typing import Any, Tuple, List, Dict, Set, Iterable, Union

# ============================================================
# print
# ============================================================
def print(*args: Any, sep: str = ..., end: str = ...) -> None:
    """
    📌 فرمول رایج:
    print("hello")
    print("name:", name)
    print("a", "b", "c", sep="-")

    📌 پارامترها:
    - *args: هر تعداد مقدار (با کاما جدا می‌شوند)
    - sep (اختیاری): جداکننده بین مقادیر — پیش‌فرض: فاصله (' ')
    - end (اختیاری): انتهای خروجی — پیش‌فرض: خط جدید ('\\n')
    """
    ...

# ============================================================
# type
# ============================================================
def type(obj: Any) -> Any:
    """
    📌 فرمول رایج:
    print(type(name))        ← <class 'str'>
    print(type(35))          ← <class 'int'>
    print(type(True))        ← <class 'bool'>

    📌 برمی‌گردونه: نوع داده
    """
    ...

# ============================================================
# تبدیل انواع
# ============================================================
def int(x: Any) -> int:
    """
    📌 فرمول رایج:
    int("18")           ← 18
    int(12.3)           ← 12 (روند می‌شود)
    int(True)           ← 1

    📌 نکته: رشته فقط وقتی تبدیل می‌شود که عدد خالص باشد
    """
    ...

def float(x: Any) -> float:
    """
    📌 فرمول رایج:
    float(12)           ← 12.0
    float("65.5")       ← 65.5
    float(True)         ← 1.0
    """
    ...

def str(x: Any) -> str:
    """
    📌 فرمول رایج:
    str(25)             ← "25"
    str(True)           ← "True"
    """
    ...

def bool(x: Any) -> bool:
    """
    📌 فرمول رایج:
    bool(12)            ← True (هر عدد غیرصفر)
    bool(0)             ← False
    bool("hello")       ← True (هر رشته غیرخالی)
    bool("")            ← False (رشته خالی)
    bool([])            ← False (لیست خالی)
    bool(None)          ← False
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
    """
    ...

# ============================================================
# max / min / sum / sorted
# ============================================================
def max(*args: Any) -> Any:
    """
    📌 فرمول رایج:
    max([12, 6, 5, 2, 7])    ← 12

    📌 برمی‌گردونه: بزرگترین مقدار
    """
    ...

def min(*args: Any) -> Any:
    """
    📌 فرمول رایج:
    min([12, 6, 5, 2, 7])    ← 2

    📌 برمی‌گردونه: کوچکترین مقدار
    """
    ...

def sum(iterable: Any, start: int = ...) -> Any:
    """
    📌 فرمول رایج:
    sum([12, 30, 40, 10])    ← 92

    📌 پارامترها:
    - iterable: لیست/تاپل اعداد
    - start (اختیاری): مقدار شروع — پیش‌فرض 0

    📌 برمی‌گردونه: مجموع
    """
    ...

def sorted(iterable: Any, reverse: bool = ...) -> List[Any]:
    """
    📌 فرمول رایج:
    sorted([3, 1, 2])                    ← [1, 2, 3]
    sorted([3, 1, 2], reverse=True)      ← [3, 2, 1]

    📌 نکته: لیست اصلی را تغییر نمی‌دهد (برخلاف list.sort())
    """
    ...

# ============================================================
# enumerate
# ============================================================
def enumerate(iterable: Any, start: int = ...) -> Any:
    """
    📌 فرمول رایج:
    for index, item in enumerate(my_list):
        print(index, item)

    📌 پارامترها:
    - iterable: لیست، تاپل، رشته و ...
    - start (اختیاری): شروع شمارش — پیش‌فرض 0

    📌 برمی‌گردونه: جفت‌های (index, value)
    """
    ...

# ============================================================
# zip
# ============================================================
def zip(*iterables: Any) -> Any:
    """
    📌 فرمول رایج:
    for a, b in zip(list1, list2):
        print(a, b)

    list(zip([1, 2], ["a", "b"]))    ← [(1, 'a'), (2, 'b')]

    📌 نکته: از کوتاه‌ترین لیست پیروی می‌کند
    """
    ...

# ============================================================
# range
# ============================================================
def range(start: int, stop: int = ..., step: int = ...) -> Any:
    """
    📌 فرمول رایج:
    range(5)                ← 0, 1, 2, 3, 4
    range(2, 10, 2)         ← 2, 4, 6, 8

    📌 پارامترها:
    - start: شروع — اگر فقط یک عدد بدی، stop محسوب می‌شود
    - stop: پایان (غیر شامل)
    - step: گام — پیش‌فرض 1
    """
    ...

# ============================================================
# list / tuple / dict / set
# ============================================================
def list(iterable: Any = ...) -> List[Any]:
    """
    📌 فرمول رایج:
    list("hello")           ← ['h', 'e', 'l', 'l', 'o']
    list(range(5))          ← [0, 1, 2, 3, 4]
    list({"a": 1})          ← ['a']  (کلیدهای دیکشنری)

    📌 کاربرد: تبدیل هر مجموعه تکرارشونده به لیست
    """
    ...

def tuple(iterable: Any = ...) -> Tuple:
    """
    📌 فرمول رایج:
    tuple([1, 2, 3])        ← (1, 2, 3)

    📌 کاربرد: تبدیل به تاپل (غیرقابل تغییر)
    """
    ...

def dict(iterable: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    dict([("a", 1), ("b", 2)])   ← {'a': 1, 'b': 2}

    📌 کاربرد: ساخت دیکشنری از لیست تاپل‌های (کلید, مقدار)
    """
    ...

def set(iterable: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    set([1, 2, 2, 3])       ← {1, 2, 3}

    📌 کاربرد: حذف تکراری‌ها — خروجی مجموعه (بدون ترتیب)
    """
    ...

# ============================================================
# input
# ============================================================
def input(prompt: str = ...) -> str:
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
def any(iterable: Any) -> bool:
    """
    📌 فرمول رایج:
    any([False, False, True])    ← True

    📌 برمی‌گردونه: True اگر حداقل یک عنصر True باشد
    """
    ...

def all(iterable: Any) -> bool:
    """
    📌 فرمول رایج:
    all([True, True, True])      ← True
    all([True, False, True])     ← False

    📌 برمی‌گردونه: True اگر همه عناصر True باشند
    """
    ...

# ============================================================
# isinstance
# ============================================================
def isinstance(obj: Any, class_or_tuple: Any) -> bool:
    """
    📌 فرمول رایج:
    isinstance(5, int)           ← True
    isinstance("hi", str)        ← True
    isinstance(5, (int, float))  ← True

    📌 برمی‌گردونه: True اگر obj از نوع مشخص شده باشد
    """
    ...

# ============================================================
# open
# ============================================================
def open(file: str, mode: str = ..., encoding: str = ...) -> Any:
    """
    📌 فرمول رایج:
    with open("file.txt", "r", encoding="utf-8") as f:
        content = f.read()

    📌 پارامترها:
    - file: مسیر فایل
    - mode: 'r' خواندن | 'w' نوشتن | 'a' افزودن | 'rb' باینری
    - encoding: 'utf-8' برای متن فارسی

    📌 نکته: همیشه با with استفاده کن تا فایل خودکار بسته شود
    """
    ...

# ============================================================
# متدهای لیست (list)
# ============================================================
class list:
    def append(self, x: Any) -> None:
        """
        📌 فرمول رایج:
        lst.append(5)

        📌 کاربرد: افزودن یک عنصر به انتهای لیست
        """
        ...

    def extend(self, iterable: Iterable) -> None:
        """
        📌 فرمول رایج:
        lst.extend([1, 2, 3])

        📌 کاربرد: افزودن چند عنصر به انتهای لیست
        """
        ...

    def insert(self, index: int, x: Any) -> None:
        """
        📌 فرمول رایج:
        lst.insert(0, 'a')

        📌 کاربرد: درج عنصر در موقعیت مشخص
        """
        ...

    def remove(self, x: Any) -> None:
        """
        📌 فرمول رایج:
        lst.remove('a')

        📌 کاربرد: حذف اولین occurrence مقدار داده‌شده
        """
        ...

    def pop(self, index: int = ...) -> Any:
        """
        📌 فرمول رایج:
        lst.pop()       ← آخرین عنصر
        lst.pop(0)      ← عنصر اول

        📌 کاربرد: حذف و برگرداندن عنصر در موقعیت مشخص
        """
        ...

    def clear(self) -> None:
        """
        📌 فرمول رایج:
        lst.clear()

        📌 کاربرد: خالی کردن کل لیست
        """
        ...

    def index(self, x: Any) -> int:
        """
        📌 فرمول رایج:
        lst.index('a')

        📌 کاربرد: برگرداندن ایندکس اولین occurrence
        """
        ...

    def count(self, x: Any) -> int:
        """
        📌 فرمول رایج:
        lst.count(5)

        📌 کاربرد: شمارش تعداد occurrence یک مقدار
        """
        ...

    def sort(self, reverse: bool = ...) -> None:
        """
        📌 فرمول رایج:
        lst.sort()                  ← صعودی
        lst.sort(reverse=True)      ← نزولی

        📌 کاربرد: مرتب‌سازی لیست درجا (خود لیست تغییر می‌کند)
        """
        ...

    def reverse(self) -> None:
        """
        📌 فرمول رایج:
        lst.reverse()

        📌 کاربرد: معکوس کردن ترتیب لیست درجا
        """
        ...

    def copy(self) -> List[Any]:
        """
        📌 فرمول رایج:
        new = lst.copy()

        📌 کاربرد: کپی سطحی از لیست
        """
        ...

# ============================================================
# متدهای دیکشنری (dict)
# ============================================================
class dict:
    def keys(self) -> Any:
        """
        📌 فرمول رایج:
        d.keys()

        📌 کاربرد: برگرداندن همه کلیدها
        """
        ...

    def values(self) -> Any:
        """
        📌 فرمول رایج:
        d.values()

        📌 کاربرد: برگرداندن همه مقادیر
        """
        ...

    def items(self) -> Any:
        """
        📌 فرمول رایج:
        for k, v in d.items():
            print(k, v)

        📌 کاربرد: برگرداندن جفت‌های (کلید, مقدار)
        """
        ...

    def get(self, key: Any, default: Any = ...) -> Any:
        """
        📌 فرمول رایج:
        d.get('a', 0)    ← اگر 'a' نباشد، 0 برمی‌گرداند

        📌 کاربرد: دریافت امن مقدار (بدون ارور KeyError)
        """
        ...

    def update(self, other: Any) -> None:
        """
        📌 فرمول رایج:
        d.update({'b': 2})

        📌 کاربرد: به‌روزرسانی دیکشنری با دیکشنری دیگر
        """
        ...

    def pop(self, key: Any) -> Any:
        """
        📌 فرمول رایج:
        d.pop('a')

        📌 کاربرد: حذف کلید و برگرداندن مقدار آن
        """
        ...

    def popitem(self) -> Tuple:
        """
        📌 فرمول رایج:
        d.popitem()

        📌 کاربرد: حذف و برگرداندن آخرین جفت (کلید, مقدار)
        """
        ...

    def clear(self) -> None:
        """
        📌 فرمول رایج:
        d.clear()

        📌 کاربرد: خالی کردن کل دیکشنری
        """
        ...

    def copy(self) -> Dict:
        """
        📌 فرمول رایج:
        new = d.copy()

        📌 کاربرد: کپی سطحی از دیکشنری
        """
        ...

    def setdefault(self, key: Any, default: Any = ...) -> Any:
        """
        📌 فرمول رایج:
        d.setdefault('a', 0)

        📌 کاربرد: اگر کلید نباشد، آن را با مقدار پیش‌فرض می‌سازد
        """
        ...

# ============================================================
# متدهای رشته (str)
# ============================================================
class str:
    def lower(self) -> str:
        """
        📌 فرمول رایج:
        "HELLO".lower()      ← "hello"
        """
        ...

    def upper(self) -> str:
        """
        📌 فرمول رایج:
        "hello".upper()      ← "HELLO"
        """
        ...

    def title(self) -> str:
        """
        📌 فرمول رایج:
        "hello world".title() ← "Hello World"
        """
        ...

    def capitalize(self) -> str:
        """
        📌 فرمول رایج:
        "hello world".capitalize() ← "Hello world"
        """
        ...

    def strip(self, chars: str = ...) -> str:
        """
        📌 فرمول رایج:
        "  hi  ".strip()     ← "hi"

        📌 کاربرد: حذف فاصله (یا کاراکترهای مشخص) از دو طرف
        """
        ...

    def lstrip(self, chars: str = ...) -> str:
        """
        📌 فرمول رایج:
        "  hi  ".lstrip()    ← "hi  "

        📌 کاربرد: حذف فاصله از سمت چپ
        """
        ...

    def rstrip(self, chars: str = ...) -> str:
        """
        📌 فرمول رایج:
        "  hi  ".rstrip()    ← "  hi"

        📌 کاربرد: حذف فاصله از سمت راست
        """
        ...

    def split(self, sep: str = ...) -> List[str]:
        """
        📌 فرمول رایج:
        "a,b,c".split(',')   ← ['a', 'b', 'c']
        "hello world".split() ← ['hello', 'world']

        📌 کاربرد: تبدیل رشته به لیست
        """
        ...

    def join(self, iterable: Iterable) -> str:
        """
        📌 فرمول رایج:
        ','.join(['a', 'b', 'c']) ← "a,b,c"

        📌 کاربرد: اتصال عناصر لیست با جداکننده
        """
        ...

    def replace(self, old: str, new: str) -> str:
        """
        📌 فرمول رایج:
        "hello".replace('l', 'x') ← "hexxo"

        📌 کاربرد: جایگزینی همه occurrenceهای old با new
        """
        ...

    def find(self, sub: str) -> int:
        """
        📌 فرمول رایج:
        "hello".find('e')    ← 1
        "hello".find('x')    ← -1

        📌 کاربرد: جستجوی ایندکس اولین occurrence (-1 اگر نباشد)
        """
        ...

    def rfind(self, sub: str) -> int:
        """
        📌 فرمول رایج:
        "hello".rfind('l')   ← 3

        📌 کاربرد: جستجوی ایندکس آخرین occurrence
        """
        ...

    def count(self, sub: str) -> int:
        """
        📌 فرمول رایج:
        "hello".count('l')   ← 2

        📌 کاربرد: شمارش تعداد occurrence
        """
        ...

    def startswith(self, prefix: str) -> bool:
        """
        📌 فرمول رایج:
        "hello".startswith('he') ← True

        📌 کاربرد: بررسی شروع رشته
        """
        ...

    def endswith(self, suffix: str) -> bool:
        """
        📌 فرمول رایج:
        "script.py".endswith('.py') ← True

        📌 کاربرد: بررسی پایان رشته
        """
        ...

    def isdigit(self) -> bool:
        """
        📌 فرمول رایج:
        "123".isdigit()      ← True
        "12a".isdigit()      ← False

        📌 کاربرد: بررسی عددی بودن (فقط 0-9)
        """
        ...

    def isalpha(self) -> bool:
        """
        📌 فرمول رایج:
        "hello".isalpha()    ← True
        "hi5".isalpha()      ← False

        📌 کاربرد: بررسی حروفی بودن (فقط a-z A-Z)
        """
        ...

    def isalnum(self) -> bool:
        """
        📌 فرمول رایج:
        "hi5".isalnum()      ← True

        📌 کاربرد: بررسی عدد یا حروف بودن (بدون فاصله و نماد)
        """
        ...

    def islower(self) -> bool:
        """
        📌 فرمول رایج:
        "hello".islower()    ← True
        """
        ...

    def isupper(self) -> bool:
        """
        📌 فرمول رایج:
        "HELLO".isupper()    ← True
        """
        ...

    def isspace(self) -> bool:
        """
        📌 فرمول رایج:
        "   ".isspace()      ← True

        📌 کاربرد: بررسی فضای خالی بودن
        """
        ...

    def isnumeric(self) -> bool:
        """
        📌 فرمول رایج:
        "۱۲۳".isnumeric()    ← True (اعداد فارسی هم)

        📌 کاربرد: بررسی عددی بودن (شامل اعداد فارسی و رومی)
        """
        ...

    def format(self, *args: Any) -> str:
        """
        📌 فرمول رایج:
        "{} is {}".format("Ali", 20) ← "Ali is 20"

        📌 کاربرد: فرمت کردن رشته
        """
        ...

    def zfill(self, width: int) -> str:
        """
        📌 فرمول رایج:
        "42".zfill(5)        ← "00042"

        📌 کاربرد: پر کردن سمت چپ با صفر
        """
        ...

    def encode(self, encoding: str = ...) -> bytes:
        """
        📌 فرمول رایج:
        "hello".encode('utf-8')

        📌 کاربرد: تبدیل رشته به بایت
        """
        ...

# ============================================================
# متدهای مجموعه (set)
# ============================================================
class set:
    def add(self, x: Any) -> None:
        """
        📌 فرمول رایج:
        s.add(5)

        📌 کاربرد: افزودن یک عنصر به مجموعه
        """
        ...

    def remove(self, x: Any) -> None:
        """
        📌 فرمول رایج:
        s.remove(5)

        📌 کاربرد: حذف عنصر (ارور اگر نباشد)
        """
        ...

    def discard(self, x: Any) -> None:
        """
        📌 فرمول رایج:
        s.discard(5)

        📌 کاربرد: حذف عنصر (بدون ارور اگر نباشد)
        """
        ...

    def pop(self) -> Any:
        """
        📌 فرمول رایج:
        s.pop()

        📌 کاربرد: حذف و برگرداندن یک عنصر تصادفی
        """
        ...

    def clear(self) -> None:
        """
        📌 فرمول رایج:
        s.clear()

        📌 کاربرد: خالی کردن کل مجموعه
        """
        ...

    def union(self, other: Set) -> Set:
        """
        📌 فرمول رایج:
        s.union(t)

        📌 کاربرد: اجتماع دو مجموعه
        """
        ...

    def intersection(self, other: Set) -> Set:
        """
        📌 فرمول رایج:
        s.intersection(t)

        📌 کاربرد: اشتراک دو مجموعه
        """
        ...

    def difference(self, other: Set) -> Set:
        """
        📌 فرمول رایج:
        s.difference(t)

        📌 کاربرد: تفاضل دو مجموعه
        """
        ...

    def issubset(self, other: Set) -> bool:
        """
        📌 فرمول رایج:
        s.issubset(t)

        📌 کاربرد: بررسی زیرمجموعه بودن
        """
        ...

    def issuperset(self, other: Set) -> bool:
        """
        📌 فرمول رایج:
        s.issuperset(t)

        📌 کاربرد: بررسی فرامجموعه بودن
        """
        ...

    def copy(self) -> Set:
        """
        📌 فرمول رایج:
        new = s.copy()

        📌 کاربرد: کپی سطحی از مجموعه
        """
        ...

# ============================================================
# متدهای تاپل (tuple)
# ============================================================
class tuple:
    def count(self, x: Any) -> int:
        """
        📌 فرمول رایج:
        t.count(5)

        📌 کاربرد: شمارش تعداد occurrence یک مقدار
        """
        ...

    def index(self, x: Any) -> int:
        """
        📌 فرمول رایج:
        t.index(5)

        📌 کاربرد: برگرداندن ایندکس اولین occurrence
        """
        ...
