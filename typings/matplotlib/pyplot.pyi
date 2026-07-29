from typing import Any, Tuple, List

# ============================================================
# ۱. نمایش و ذخیره
# ============================================================
def show() -> None:
    """📌 فرمول رایج: plt.show() — نمایش تمام نمودارها"""
    ...

def savefig(fname: str, dpi: int = ..., bbox_inches: str = ...) -> None:
    """
    📌 فرمول رایج:
    plt.savefig("chart.png", dpi=300)

    📌 پارامترها:
    - fname: نام فایل با پسوند (مثلاً "plot.png")
    - dpi: وضوح تصویر — 300 بهتر
    - bbox_inches: 'tight' برای جلوگیری از برش

    📌 نکته: حتماً قبل از plt.show() بیاید، وگرنه صفحه خالی ذخیره می‌شود
    """
    ...

def close() -> None:
    """📌 فرمول رایج: plt.close() — بستن نمودار بدون نمایش"""
    ...

# ============================================================
# ۲. تنظیمات نمودار
# ============================================================
def title(label: str, fontsize: int = ..., fontweight: str = ...) -> None:
    """
    📌 فرمول رایج:
    plt.title("Chart Title")

    📌 پارامترها:
    - label: متن عنوان
    """
    ...

def xlabel(xlabel: str, fontsize: int = ...) -> None:
    """
    📌 فرمول رایج:
    plt.xlabel("X-axis label")
    """
    ...

def ylabel(ylabel: str, fontsize: int = ...) -> None:
    """
    📌 فرمول رایج:
    plt.ylabel("Y-axis label")
    """
    ...

def legend(loc: str = ...) -> None:
    """
    📌 فرمول رایج:
    plt.legend(loc='best')

    📌 پارامترها:
    - loc: 'best', 'upper right', 'lower left'
    """
    ...

def grid(visible: bool = ..., alpha: float = ...) -> None:
    """
    📌 فرمول رایج:
    plt.grid(True, alpha=0.3)
    """
    ...

def xticks(ticks: Any = ..., rotation: int = ..., ha: str = ...) -> None:
    """
    📌 فرمول رایج:
    plt.xticks(df.index, rotation=45, ha='right')

    📌 پارامترها:
    - rotation: زاویه چرخش برچسب‌ها
    - ha: 'right' برای جلوگیری از بیرون‌زدگی
    """
    ...

def tight_layout() -> None:
    """
    📌 فرمول رایج:
    plt.tight_layout() — جلوگیری از روی‌هم‌افتادن نمودارها

    📌 نکته: بعد از همه ساب‌پلات‌ها و قبل از savefig/show
    """
    ...

# ============================================================
# ۳. ساخت Figure و Subplot
# ============================================================
def figure(
    num: Any = ...,
    figsize: Tuple[float, float] = ...,
    dpi: int = ...,
    facecolor: str = ...,
    edgecolor: str = ...,
) -> Any:
    """
    📌 فرمول رایج:
    plt.figure(figsize=(8, 6))

    📌 پارامترها:
    - num: شماره یا نام فیگور
    - figsize: (width, height) به اینچ — پیش‌فرض (6.4, 4.8)
    - dpi: رزولوشن — پیش‌فرض 100
    - facecolor: رنگ پس‌زمینه — پیش‌فرض 'white'
    """
    ...

def subplot(nrows: int, ncols: int, index: int) -> Any:
    """
    📌 فرمول رایج:
    plt.subplot(2, 1, 1)     ← دو ردیف، یک ستون، خانه اول

    📌 پارامترها:
    - nrows: تعداد ردیف‌ها
    - ncols: تعداد ستون‌ها
    - index: شماره خانه (از ۱ شروع می‌شود)
    """
    ...

def subplots(
    nrows: int = ...,
    ncols: int = ...,
    figsize: Tuple[float, float] = ...,
    constrained_layout: bool = ...,
) -> Tuple[Any, Any]:
    """
    📌 فرمول رایج:
    fig, axs = plt.subplots(nrows, ncols, figsize=(12, 8), constrained_layout=True)

    📌 پارامترها:
    - nrows: تعداد ردیف — برای یک نمودار نده
    - ncols: تعداد ستون — برای یک نمودار نده
    - figsize: اندازه کل صفحه — (width, height)
    - constrained_layout: پیش‌فرض False — True بهتر (جایگزین tight_layout)

    📌 نکته: جایگزین plt.figure() + plt.subplot() + plt.tight_layout()
    """
    ...

# ============================================================
# ۴. نمودار خطی
# ============================================================
def plot(
    x: Any = ...,
    y: Any = ...,
    color: str = ...,
    linestyle: str = ...,
    marker: str = ...,
    linewidth: float = ...,
    label: str = ...,
    ax: Any = ...,
) -> Any:
    """
    📌 فرمول رایج:
    plt.plot(x, y, marker='o', color='black', linestyle='--', label='data')

    📌 پارامترها:
    - x: مقادیر محور افقی — اختیاری (اگر ندهی، 0,1,2,... جایگزین می‌شود)
    - y: مقادیر محور عمودی — اگر فقط y بدهی، به عنوان محور ایگریک در نظر گرفته می‌شود
    - color: رنگ خط — پیش‌فرض 'blue'
    - linestyle: '-' (پیوسته) | '--' (خط‌چین) | ':' (نقطه‌چین)
    - marker: 'o', '*', 'x', '+'
    - linewidth: ضخامت خط — پیش‌فرض 1
    - label: برچسب برای legend
    - ax: موقعیت در subplot — مثلاً ax=axs[0]

    📌 نکات:
    - اگر x نداشته باشی و y یک Series باشد، ایندکس Series به عنوان x استفاده می‌شود
    - برای s.value_counts(): از plt.plot(s.index, s.values) استفاده کن
    """
    ...

# ============================================================
# ۵. نمودار پراکندگی
# ============================================================
def scatter(
    x: Any,
    y: Any,
    c: Any = ...,
    s: Any = ...,
    marker: str = ...,
    color: str = ...,
    alpha: float = ...,
    label: str = ...,
) -> Any:
    """
    📌 فرمول رایج:
    plt.scatter(x, y, c='black', marker='o', s=20, alpha=0.5)

    📌 پارامترها:
    - x: مقادیر محور افقی (اجباری)
    - y: مقادیر محور عمودی (اجباری)
    - c: رنگ نقاط یا ستون سوم برای رنگ‌گذاری (مثلاً c=df["age"])
    - s: اندازه نقاط — پیش‌فرض 20 | می‌تواند ستون سوم باشد (مثلاً s=df["score"]*50)
    - marker: 'o', 'x', '*'
    - color: رنگ ثابت — اگر c دادی، color نده
    - alpha: شفافیت — 0.5 برای دیدن تراکم
    - label: برچسب برای legend

    📌 نکته: همیشه بهتر است با متپلات‌لیب خالص رسم شود (نه پانداس)
    """
    ...

def colorbar(label: str = ...) -> None:
    """
    📌 فرمول رایج:
    plt.colorbar(label="Age") — بعد از scatter با پارامتر c
    """
    ...

# ============================================================
# ۶. نمودار میله‌ای
# ============================================================
def bar(
    x: Any,
    height: Any,
    width: float = ...,
    color: str = ...,
    edgecolor: str = ...,
    label: str = ...,
) -> Any:
    """
    📌 فرمول رایج:
    plt.bar(x, height, edgecolor='black')

    📌 پارامترها:
    - x: موقعیت دسته‌ها روی محور افقی (اجباری)
    - height: ارتفاع میله‌ها (اجباری)
    - width: پهنای میله‌ها — پیش‌فرض 0.8
    - color: رنگ — پیش‌فرض 'blue'
    - edgecolor: رنگ حاشیه — 'black' بهتر
    - label: برچسب برای legend

    📌 نکته: برای value_counts() از plt.bar(s.index, s.values) استفاده کن
    """
    ...

# ============================================================
# ۷. هیستوگرام
# ============================================================
def hist(
    x: Any,
    bins: Any = ...,
    color: str = ...,
    edgecolor: str = ...,
    alpha: float = ...,
    density: bool = ...,
    cumulative: bool = ...,
) -> Any:
    """
    📌 فرمول رایج:
    plt.hist(data, bins=10, edgecolor='black')

    📌 پارامترها:
    - x: داده‌ها (اجباری) — فقط ایگریک، محور X بازه‌هاست
    - bins: تعداد بازه‌ها — پیش‌فرض 10 | می‌تواند لیست مرزها باشد
    - color: رنگ — پیش‌فرض 'blue'
    - edgecolor: رنگ حاشیه — 'black' بهتر
    - alpha: شفافیت — 0.5 برای همپوشانی چند هیستوگرام
    - density: پیش‌فرض False — True = چگالی احتمال (مساحت کل = 1)
    - cumulative: پیش‌فرض False — True = تجمعی

    📌 نکته برای بازه‌های دقیق:
    bins = np.arange((df["col"].min()-0.5), (df["col"].max()+0.5), 1)
    """
    ...

# ============================================================
# ۸. نمودار جعبه‌ای
# ============================================================
def boxplot(x: Any, vert: bool = ..., grid: bool = ...) -> Any:
    """
    📌 فرمول رایج:
    plt.boxplot(data) — تشخیص پراکندگی و outlier

    📌 پارامترها:
    - x: داده‌ها (فقط ایگریک)
    - vert: پیش‌فرض True — False = افقی
    """
    ...

# ============================================================
# ۹. نمایش تصویر
# ============================================================
def imshow(X: Any, cmap: str = ..., interpolation: str = ...) -> Any:
    """
    📌 فرمول رایج:
    plt.imshow(img_rgb)
    plt.imshow(gray, cmap='gray')

    📌 پارامترها:
    - X: آرایه تصویر
    - cmap: 'gray', 'hot', 'viridis'
    - interpolation: 'nearest'
    """
    ...

def axis(option: str = ...) -> None:
    """
    📌 فرمول رایج:
    plt.axis('off') — حذف محورها (برای نمایش تصویر)
    """
    ...

# ============================================================
# ۱۰. text — اضافه کردن متن روی نمودار
# ============================================================
def text(
    x: float, y: float, s: str, ha: str = ..., va: str = ..., fontsize: int = ...
) -> None:
    """
    📌 فرمول رایج:
    ax.text(i, value + 0.5, str(value), ha='center', va='bottom')

    📌 پارامترها:
    - x, y: مختصات
    - s: متن
    - ha: 'center'
    - va: 'bottom'
    """
    ...

# ============================================================
# نمودار دایره‌ای (pie)
# ============================================================
def pie(
    x: Any,
    labels: Any = ...,
    autopct: str = ...,
    startangle: int = ...,
    ylabel: str = ...,
) -> Any:
    """
    📌 فرمول رایج:
    df["gender"].value_counts().plot(kind="pie", autopct="%1.1f%%", ylabel="")

    📌 پارامترها:
    - x: داده‌ها
    - labels: برچسب‌ها
    - autopct: فرمت درصد — '%1.1f%%'
    - startangle: زاویه شروع
    - ylabel: '' برای حذف برچسب محور
    """
    ...

# ============================================================
# ۱۱. متدهای شیء Axes (ax) — اضافه‌شده
# ============================================================
def set_title(label: str, fontsize: int = ..., fontweight: str = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_title("Chart Title")

    📌 پارامترها:
    - label: متن عنوان
    """
    ...

def set_xlabel(xlabel: str, fontsize: int = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_xlabel("X-axis label")
    """
    ...

def set_ylabel(ylabel: str, fontsize: int = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_ylabel("Y-axis label")
    """
    ...

def set_xlim(left: float = ..., right: float = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_xlim(0, 100) — محدوده محور X
    """
    ...

def set_ylim(bottom: float = ..., top: float = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_ylim(0, 100) — محدوده محور Y
    """
    ...

def set_xticks(ticks: Any = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_xticks([1, 2, 3]) — تعیین تیک‌های X
    """
    ...

def set_yticks(ticks: Any = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_yticks([1, 2, 3]) — تعیین تیک‌های Y
    """
    ...

def set_xticklabels(labels: Any = ..., rotation: int = ..., ha: str = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_xticklabels(['A', 'B', 'C'], rotation=45)
    """
    ...

def set_yticklabels(labels: Any = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_yticklabels(['A', 'B', 'C'])
    """
    ...

def set_facecolor(color: str = ...) -> None:
    """
    📌 فرمول رایج:
    ax.set_facecolor('lightgray') — رنگ پس‌زمینه نمودار
    """
    ...

def tick_params(axis: str = ..., rotation: int = ..., labelsize: int = ...) -> None:
    """
    📌 فرمول رایج:
    ax.tick_params(axis='x', rotation=45) — تنظیم تیک‌ها
    """
    ...

def legend(loc: str = ..., title: str = ...) -> None:
    """
    📌 فرمول رایج:
    ax.legend(loc='best', title='Subject') — راهنما روی Axes
    """
    ...

def grid(visible: bool = ..., alpha: float = ...) -> None:
    """
    📌 فرمول رایج:
    ax.grid(True, alpha=0.3) — شبکه روی Axes
    """
    ...

def text(x: float, y: float, s: str, ha: str = ..., va: str = ..., fontsize: int = ...) -> None:
    """
    📌 فرمول رایج:
    ax.text(i, value + 0.5, str(value), ha='center', va='bottom')
    """
    ...

def twinx() -> Any:
    """
    📌 فرمول رایج:
    ax2 = ax.twinx() — محور Y دوم برای رسم دو مقیاس متفاوت
    """
    ...

def fill_between(x: Any, y1: Any, y2: Any = ..., alpha: float = ..., color: str = ...) -> None:
    """
    📌 فرمول رایج:
    ax.fill_between(x, y1, y2, alpha=0.3, color='blue') — پر کردن بین دو خط
    """
    ...

def axhline(y: float = ..., color: str = ..., linestyle: str = ..., linewidth: float = ...) -> None:
    """
    📌 فرمول رایج:
    ax.axhline(y=0, color='r', linestyle='--') — خط افقی
    """
    ...

def axvline(x: float = ..., color: str = ..., linestyle: str = ..., linewidth: float = ...) -> None:
    """
    📌 فرمول رایج:
    ax.axvline(x=0, color='r', linestyle='--') — خط عمودی
    """
    ...

def invert_xaxis() -> None:
    """
    📌 فرمول رایج:
    ax.invert_xaxis() — معکوس کردن محور X
    """
    ...

def invert_yaxis() -> None:
    """
    📌 فرمول رایج:
    ax.invert_yaxis() — معکوس کردن محور Y
    """
    ...

# ============================================================
# ۱۲. متدهای شیء Figure (fig) — اضافه‌شده
# ============================================================
def savefig(fname: str, dpi: int = ..., bbox_inches: str = ..., facecolor: str = ...) -> None:
    """
    📌 فرمول رایج:
    fig.savefig("plot.png", dpi=300, bbox_inches='tight')
    ⚠️ این متد روی fig هست، نه plt: fig.savefig(...)
    """
    ...

def set_size_inches(w: float, h: float) -> None:
    """
    📌 فرمول رایج:
    fig.set_size_inches(10, 8) — تغییر اندازه شکل بعد از ساخت
    """
    ...

def subplots_adjust(
    left: float = ..., right: float = ..., top: float = ...,
    bottom: float = ..., hspace: float = ..., wspace: float = ...
) -> None:
    """
    📌 فرمول رایج:
    fig.subplots_adjust(hspace=0.5, wspace=0.3) — تنظیم فاصله ساب‌پلات‌ها
    """
    ...

def tight_layout(pad: float = ..., h_pad: float = ..., w_pad: float = ...) -> None:
    """
    📌 فرمول رایج:
    fig.tight_layout() — تنظیم خودکار فاصله‌ها (متعلق به fig، نه plt)
    """
    ...

# ============================================================
# اورلپ نمودارهای میله‌ای (widthهای مختلف)
# ============================================================
# plt.bar(x, y1, width=0.6, label="A", color="brown", edgecolor="black")
# plt.bar(x, y2, width=0.4, label="B", color="lightgrey", edgecolor="black")
# plt.bar(x, y3, width=0.2, label="C", color="yellow", edgecolor="black")
# ============================================================