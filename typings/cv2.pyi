from typing import Any, Tuple, Optional
import numpy as np

# ============================================================
# 🏷️ سطح‌بندی موضوعی توابع (مطابق با cvt.find_level):
# [Config] = تنظیمات | [Preprocess] = پیش‌پردازش | [Analyze] = تحلیل
# [Visualize] = نمایش/رسم | [Main] = اصلی
# ============================================================

# ============================================================
# ۱. خواندن تصویر
# ============================================================
def imread(filename: str, flags: int = ...) -> Any:
    """
    🏷️ [I/O]
    def read_img(path):
        img = cv2.imread(path)
        return img

    📌 فرمول رایج:
    img = cv2.imread(path)
    img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    img_unchanged = cv2.imread(path, cv2.IMREAD_UNCHANGED)

    📌 پارامترها:
    - filename: مسیر فایل تصویری
    - flags (اختیاری): نحوه خواندن — پیش‌فرض: cv2.IMREAD_COLOR (رنگی BGR)
        cv2.IMREAD_GRAYSCALE: خاکستری
        cv2.IMREAD_UNCHANGED: با کانال آلفا
        cv2.IMREAD_COLOR_RGB: رنگی RGB
        cv2.IMREAD_REDUCED_COLOR_2: نصف ابعاد

    📌 برمی‌گردونه: آرایه NumPy تصویر (None اگر خطا دهد)

    📌 بررسی خطا (ضروری):
    if img is None:
        print("خطا در خواندن تصویر")
        continue
    """
    ...

# ============================================================
# ۲. نمایش تصویر
# ============================================================
def imshow(winname: str, img: Any) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.imshow("Window Name", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    📌 پارامترها:
    - winname: نام پنجره (رشته دلخواه) — رایج: "win", "Result", "Output"
    - img: آرایه تصویری — رایج: img, gray, th, boxes, edges
    """
    ...

def waitKey(delay: int = ...) -> int:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.waitKey(0)

    📌 پارامترها:
    - delay: میلی‌ثانیه صبر — 0 یعنی تا زدن یک کلید | 2000 یعنی ۲ ثانیه
        رایج: 0 (برای نمایش ثابت), 1 (برای حلقه ویدئو)

    📌 برمی‌گردونه: کد ASCII کلید فشرده شده — رایج: ord('q'), ord('s'), 27 (ESC)
    """
    ...

def destroyAllWindows() -> None:
    """🏷️ [Visualize] — فرمول رایج: cv2.destroyAllWindows() — بستن همه پنجره‌ها"""
    ...

def destroyWindow(winname: str) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.destroyWindow("win") — بستن یک پنجره خاص

    📌 پارامترها:
    - winname: نام پنجره — رایج: "win", "Result"
    """
    ...

def namedWindow(winname: str, flags: int = ...) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.namedWindow("win", cv2.WINDOW_NORMAL)

    📌 پارامترها:
    - winname: نام پنجره — رایج: "win", "Output"
    - flags: cv2.WINDOW_NORMAL (قابل تغییر اندازه) | cv2.WINDOW_AUTOSIZE (پیش‌فرض)
    """
    ...

def resizeWindow(winname: str, width: int, height: int) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.resizeWindow("win", 800, 600)

    📌 پارامترها:
    - winname: نام پنجره — رایج: "win"
    - width: عرض به پیکسل — رایج: 800, 1024, 1280
    - height: ارتفاع به پیکسل — رایج: 600, 768, 720
    """
    ...

def getWindowProperty(winname: str, prop_id: int) -> float:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.getWindowProperty("win", cv2.WND_PROP_VISIBLE)

    📌 پارامترها:
    - winname: نام پنجره — رایج: "win"
    - prop_id: شناسه ویژگی — cv2.WND_PROP_VISIBLE برای بررسی باز بودن پنجره

    📌 برمی‌گردونه: مقدار ویژگی (مثلاً 1.0 یعنی باز است)
    """
    ...

# ============================================================
# Trackbar (نوار لغزنده)
# ============================================================
def createTrackbar(
    trackbarName: str, windowName: str, value: int, count: int, onChange: Any = ...
) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.createTrackbar("Threshold", "Window", 0, 255, nothing)
    # یا بدون callback:
    cv2.createTrackbar("Threshold", "Window", 0, 255, lambda x: None)

    📌 پارامترها:
    - trackbarName: نام نوار لغزنده — رایج: "Threshold", "Value", "Kernel Size"
    - windowName: نام پنجره‌ای که نوار در آن قرار می‌گیرد — رایج: "Window", "win"
    - value: مقدار اولیه (پیش‌فرض) — رایج: 0, 127, 5
    - count: حداکثر مقدار (معمولاً 255 برای تصاویر) — رایج: 255, 100, 50
    - onChange (اختیاری): تابع callback که با تغییر مقدار صدا زده می‌شود
        رایج: lambda x: None یا تابع nothing

    📌 نکته: callback در OpenCV 4 اختیاری است، اما در برخی نسخه‌ها اجباری است
    """
    ...

def getTrackbarPos(trackbarName: str, windowName: str) -> int:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    value = cv2.getTrackbarPos("Threshold", "Window")

    📌 پارامترها:
    - trackbarName: نام نوار لغزنده — رایج: "Threshold", "Value"
    - windowName: نام پنجره حاوی نوار — رایج: "Window", "win"

    📌 برمی‌گردونه: مقدار فعلی نوار لغزنده (عدد صحیح)

    📌 کاربرد رایج:
    # در حلقه while:
    while True:
        thresh = cv2.getTrackbarPos("Threshold", "Window")
        # استفاده از thresh برای پردازش تصویر
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    """
    ...

def setTrackbarPos(trackbarName: str, windowName: str, pos: int) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.setTrackbarPos("Threshold", "Window", 128)

    📌 پارامترها:
    - trackbarName: نام نوار لغزنده — رایج: "Threshold"
    - windowName: نام پنجره حاوی نوار — رایج: "Window"
    - pos: مقدار جدید برای نوار — رایج: 0-255

    📌 کاربرد: تنظیم مقدار نوار از داخل برنامه
    """
    ...

# ============================================================
# ۳. تبدیل رنگ
# ============================================================
def cvtColor(src: Any, code: int) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    bgr_from_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img (BGR), gray, hsv
    - code: کد تبدیل رنگ
        cv2.COLOR_BGR2GRAY: رنگی BGR به خاکستری (رایج‌ترین)
        cv2.COLOR_BGR2RGB: BGR به RGB (برای نمایش با Matplotlib)
        cv2.COLOR_GRAY2BGR: خاکستری به رنگی ۳ کاناله
        cv2.COLOR_BGR2HSV: BGR به HSV (برای تشخیص رنگ)
        cv2.COLOR_HSV2BGR: HSV به BGR
        cv2.COLOR_RGB2BGR: RGB به BGR

    📌 برمی‌گردونه: تصویر تبدیل‌شده

    📌 چه زمانی با فلگ متفاوت بخوانیم و کی cvtColor کنیم؟
    فایل محلی روی SSD سریع → خواندن با فلگ متفاوت (حذف سربار CPU)
    Raspberry Pi / SD Card کند → یک بار خواندن + cvtColor
    استریم دوربین / ویدئو → cvtColor اجباری (فقط یک فریم داریم)
    تصویر از قبل در حافظه → cvtColor اجباری (imread معنی ندارد)
    فایل روی شبکه (NAS/Cloud) → یک بار خواندن + cvtColor
    پردازش بلادرنگ → یک بار خواندن + cvtColor
    پردازش دسته‌ای روی SSD → خواندن با فلگ متفاوت
    """
    ...

# ============================================================
# ۴. ذخیره تصویر
# ============================================================
def imwrite(filename: str, img: Any) -> bool:
    """
    🏷️ [I/O]
    def save_img(path, img):
        cv2.imwrite(str(path),img)

    📌 فرمول رایج:
    cv2.imwrite("output.jpg", img)
    cv2.imwrite(str(output_dir / f"name_{suffix}.jpg"), img)

    📌 پارامترها:
    - filename: مسیر و نام فایل با پسوند (مثلاً "result.jpg")
        رایج: "output.jpg", "result.png", str(path / "img.jpg")
    - img: تصویر مورد نظر برای ذخیره — رایج: img, boxes, result, thresh

    📌 برمی‌گردونه: True اگر موفق بود

    📌 قانون ذخیره‌سازی:
    فقط عکس خام (بدون نمودار/تیتر) → cv2.imwrite()
    هر چیزی که نمودار، هیستوگرام، یا چند subplot دارد → plt.savefig()
    کلاژ عکس برای پردازش مجدد → np.hstack/np.vstack + cv2.imwrite()
    """
    ...

# ============================================================
# ۵. تغییر اندازه
# ============================================================
def resize(
    src: Any,
    dsize: Optional[Tuple[int, int]],
    fx: float = ...,
    fy: float = ...,
    interpolation: int = ...,
) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    resized = cv2.resize(img, (400, 300))                    ← با ابعاد دقیق
    resized = cv2.resize(img, dsize=None, fx=0.6, fy=0.6)    ← با ضریب مقیاس

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img, gray, th
    - dsize: ابعاد خروجی (width, height) — اگر None، باید fx و fy را بدهی
        رایج: (400, 300), (800, 600), (224, 224), None
    - fx (اختیاری): ضریب مقیاس افقی — 0.6 یعنی ۶۰٪ عرض اولیه
        رایج: 0.5, 0.75, 1.0, 2.0
    - fy (اختیاری): ضریب مقیاس عمودی — 0.6 یعنی ۶۰٪ ارتفاع اولیه
        رایج: 0.5, 0.75, 1.0, 2.0
    - interpolation (اختیاری): روش درون‌یابی — پیش‌فرض: cv2.INTER_LINEAR
        cv2.INTER_AREA: بهترین برای کوچک‌سازی (پیشنهادی)
        cv2.INTER_CUBIC: بهترین برای بزرگ‌نمایی
        cv2.INTER_NEAREST: سریع (برای ماسک)

    📌 برمی‌گردونه: تصویر تغییر اندازه داده شده

    📌 تغییر اندازه با حفظ نسبت:
    h, w = img.shape[:2]
    new_w = 400
    new_h = int((h * new_w) / w)
    resized = cv2.resize(img, (new_w, new_h))
    """
    ...

# ============================================================
# ۶. چرخش
# ============================================================
def rotate(src: Any, rotateCode: int) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    rotated = cv2.rotate(img, cv2.ROTATE_180)
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img
    - rotateCode:
        cv2.ROTATE_90_CLOCKWISE: ۹۰° ساعتگرد
        cv2.ROTATE_180: ۱۸۰°
        cv2.ROTATE_90_COUNTERCLOCKWISE: ۹۰° پادساعتگرد

    📌 برمی‌گردونه: تصویر چرخانده شده
    """
    ...

def getRotationMatrix2D(center: Tuple[float, float], angle: float, scale: float) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    M = cv2.getRotationMatrix2D((w//2, h//2), 30, 1.0)

    📌 پارامترها:
    - center: مرکز چرخش (x, y) — معمولاً (w//2, h//2)
        رایج: (w//2, h//2), (0, 0)
    - angle: زاویه به درجه — مثبت = پادساعتگرد
        رایج: 30, 45, 90, -45
    - scale: ضریب مقیاس — 1.0 یعنی بدون تغییر اندازه
        رایج: 1.0, 0.5, 1.5

    📌 برمی‌گردونه: ماتریس تبدیل ۲×۳ برای warpAffine

    📌 چرخش کامل با جلوگیری از بریدگی:
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    angle = 30
    scale = 1.0
    M = cv2.getRotationMatrix2D(center, angle, scale)
    theta = np.radians(angle)
    new_w = int(h * np.sin(theta) + w * np.cos(theta))
    new_h = int(h * np.cos(theta) + w * np.sin(theta))
    M[0, 2] += (new_w - w) // 2
    M[1, 2] += (new_h - h) // 2
    rotated = cv2.warpAffine(img, M, (new_w, new_h))
    """
    ...

def warpAffine(src: Any, M: Any, dsize: Tuple[int, int]) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    rotated = cv2.warpAffine(img, M, (new_w, new_h))

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img
    - M: ماتریس تبدیل ۲×۳ (از getRotationMatrix2D)
        رایج: M, matrix
    - dsize: ابعاد خروجی (width, height) — رایج: (w, h), (new_w, new_h)

    📌 برمی‌گردونه: تصویر تبدیل‌شده
    """
    ...

# ============================================================
# ۷. وارونه‌سازی
# ============================================================
def flip(src: Any, flipCode: int) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    flip_vertical = cv2.flip(img, 0)
    flip_horizontal = cv2.flip(img, 1)
    flip_both = cv2.flip(img, -1)

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img
    - flipCode:
        0: عمودی (دور محور x)
        1: افقی - آینه‌ای (دور محور y) — پرکاربردترین
        -1: عمودی و افقی (معادل چرخش ۱۸۰°)

    📌 برمی‌گردونه: تصویر وارونه شده
    """
    ...

# ============================================================
# ۸. Gaussian Blur
# ============================================================
def GaussianBlur(
    src: Any, ksize: Tuple[int, int], sigmaX: float, sigmaY: float = ...
) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    blurred = cv2.GaussianBlur(img, (5, 5), 0)

    📌 پارامترها:
    - src: تصویر ورودی (رنگی یا خاکستری) — والیوی رایج: img, gray
    - ksize: اندازه کرنل (width, height) — هر دو باید فرد باشند
        (3,3): کم | (5,5): متوسط (پیشنهادی) | (9,9): زیاد
        رایج: (5, 5), (3, 3), (7, 7), (9, 9)
    - sigmaX: انحراف معیار افقی — 0 یعنی خودکار از ksize (پیشنهادی)
        رایج: 0, 1.0, 1.5, 2.0
    - sigmaY (اختیاری): انحراف معیار عمودی — پیش‌فرض = sigmaX
        رایج: 0, 1.0, 1.5

    📌 برمی‌گردونه: تصویر بلور شده

    📌 نکته: نیازی به نوشتن نام پارامتر sigmaX نیست، فقط 0 را بنویس.
    """
    ...

# ============================================================
# ۹. Median Blur
# ============================================================
def medianBlur(src: Any, ksize: int) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    median = cv2.medianBlur(img, 5)

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img, gray
    - ksize: اندازه کرنل — یک عدد فرد (نه تاپل!)
        3: کم | 5: متوسط (پیشنهادی) | 9: زیاد
        رایج: 3, 5, 7, 9

    📌 برمی‌گردونه: تصویر بلور شده

    📌 کاربرد: حذف نویز نمک-فلفل (لبه‌ها را تیز نگه می‌دارد)
    📌 نکته: نیازی به نوشتن نام پارامتر ksize نیست، فقط عدد را بنویس.

    📌 مقایسه:
    Gaussian = میانگین وزن‌دار → نویز پخش می‌شود → لبه‌ها محو
    Median   = میانه آماری → نویز حذف می‌شود → لبه‌ها تیز
    """
    ...

# ============================================================
# ۱۰. Threshold ساده
# ============================================================
def threshold(src: Any, thresh: float, maxval: float, type: int) -> Tuple[float, Any]:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    📌 پارامترها:
    - src: تصویر Grayscale — والیوی رایج: gray, blurred
    - thresh: عدد آستانه (0 تا 255) — کم = سفیدتر | زیاد = سیاه‌تر
        127: رایج‌ترین | 50: روشن | 200: تیره
        رایج: 127, 100, 150, 200
    - maxval: مقدار پیکسل‌های عبورکرده — معمولاً 255
        رایج: 255, 1
    - type: نوع آستانه‌گذاری
        cv2.THRESH_BINARY: بالای آستانه = maxval (پیشفرض ذهنی)
        cv2.THRESH_BINARY_INV: معکوس حالت بالا
        cv2.THRESH_TRUNC: بالای آستانه = خود آستانه
        cv2.THRESH_TOZERO: پایین آستانه = 0
        cv2.THRESH_TOZERO_INV: معکوس TOZERO
        cv2.THRESH_BINARY + cv2.THRESH_OTSU: آستانه‌گذاری خودکار

    📌 برمی‌گردونه: (ret, th) — ret = thresh استفاده‌شده | th = تصویر باینری

    📌 نکته: نیازی به نوشتن نام پارامترها نیست، فقط مقادیر را بنویس.

    📌 Otsu (آستانه‌گذاری خودکار):
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh_otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    مناسب برای: تصاویر دوقله‌ای با کنتراست بالا، نور یکنواخت
    """
    ...

# ============================================================
# ۱۱. Adaptive Threshold
# ============================================================
def adaptiveThreshold(
    src: Any,
    maxValue: float,
    adaptiveMethod: int,
    thresholdType: int,
    blockSize: int,
    C: float,
) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    thresh_adapt = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

    📌 پارامترها (هر ۶ تا اجباری):
    - src: تصویر Grayscale — والیوی رایج: gray
    - maxValue: مقدار پیکسل‌های سفید — معمولاً 255
        رایج: 255
    - adaptiveMethod:
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C: میانگین وزن‌دار (پیشنهادی)
        cv2.ADAPTIVE_THRESH_MEAN_C: میانگین ساده
    - thresholdType: معمولاً cv2.THRESH_BINARY
        رایج: cv2.THRESH_BINARY, cv2.THRESH_BINARY_INV
    - blockSize: اندازه ناحیه — عدد فرد
        11: جزئیات بیشتر | 21: نرم‌تر (پیشنهادی برای متون)
        رایج: 11, 15, 21, 31, 51
    - C: ثابت تصحیح — از میانگین کم می‌شود
        2: پیش‌فرض | 3: معمولی | 7: خطوط پیوسته‌تر
        بزرگتر = تصویر تیره‌تر و پیوسته‌تر
        رایج: 2, 3, 5, 7, 10

    📌 برمی‌گردونه: تصویر باینری تطبیقی
    📌 کاربرد: تصاویر با نور غیریکنواخت (سایه‌دار)

    📌 نکته — C منفی (راه‌حل تله تُنال):
    C را منفی بگیر: ۲- تا ۱۵- | blockSize را بالا ببر: ۲۱ به بالا
    نتیجه: مرز بیرونی بسته و یکپارچه، داخل شلوغ
    """
    ...

# ============================================================
# ۱۲. Canny Edge Detection
# ============================================================
def Canny(image: Any, threshold1: float, threshold2: float) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    edges = cv2.Canny(gray, 50, 150)

    📌 پارامترها:
    - image: تصویر Grayscale — والیوی رایج: gray, blurred (حتماً قبلش بلور کن!)
    - threshold1: حد پایین هیسترزیس
        رایج: 30, 50, 80, 100
    - threshold2: حد بالا هیسترزیس
        رایج: 100, 150, 200, 240
    نسبت پیشنهادی 1:2 یا 1:3
    مقادیر تجربی خوب: (50,150) | (80,200) | (80,240)

    📌 برمی‌گردونه: تصویر لبه‌ها

    📌 قانون طلایی: همیشه قبل از Canny بلور کن!
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    📌 منطق هیسترزیس:
    گرادیان > threshold2 → قطعاً لبه
    گرادیان < threshold1 → قطعاً غیرلبه
    بین این دو → لبه فقط اگر به لبه قطعی متصل باشد

    📌 نکته: نیازی به نوشتن نام پارامترها نیست، فقط اعداد را بنویس.
    """
    ...

# ============================================================
# ۱۳. SIFT
# ============================================================
def SIFT_create(
    nfeatures: int = ...,
    nOctaveLayers: int = ...,
    contrastThreshold: float = ...,
    edgeThreshold: float = ...,
    sigma: float = ...,
) -> SIFT:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    sift = cv2.SIFT_create()
    keypoints, descriptor = sift.detectAndCompute(gray, None)
    result = cv2.drawKeypoints(img, keypoints, None)

    📌 پارامترهای اختیاری:
    - nfeatures: حداکثر تعداد نقاط — 0 = نامحدود (پیش‌فرض)
        رایج: 0, 500, 1000
    - nOctaveLayers: تعداد لایه در هر اکتاو — پیش‌فرض 3
        رایج: 3
    - contrastThreshold: آستانه حذف نقاط ضعیف — پیش‌فرض 0.04
        رایج: 0.04, 0.02, 0.06
    - edgeThreshold: آستانه حذف نقاط لبه — پیش‌فرض 10
        رایج: 10, 5, 15
    - sigma: سیگمای گاوسین اولیه — پیش‌فرض 1.6
        رایج: 1.6, 1.2, 2.0

    📌 برمی‌گردونه: شیء SIFT با متدهای detectAndCompute, detect, compute
    """
    ...

def drawKeypoints(
    image: Any,
    keypoints: Any,
    outImage: Any,
    color: Tuple[int, int, int] = ...,
    flags: int = ...,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.drawKeypoints(img, keypoints, None)

    📌 پارامترها:
    - image: تصویر منبع — والیوی رایج: img
    - keypoints: لیست نقاط کلیدی — از sift.detectAndCompute
    - outImage: تصویر مقصد — None یعنی تصویر جدید بساز
        رایج: None, img.copy()
    - color (اختیاری): رنگ نقاط — پیش‌فرض: تصادفی
        رایج: (0, 255, 0), (0, 0, 255)
    - flags (اختیاری): نحوه رسم — پیش‌فرض: فقط دایره مرکز
        رایج: cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS

    📌 برمی‌گردونه: تصویر با نقاط رسم‌شده
    """
    ...

# ============================================================
# ۱۴. تبدیلات هندسی دیگر
# ============================================================
def getAffineTransform(src: Any, dst: Any) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    M = cv2.getAffineTransform(pts1, pts2)
    warped = cv2.warpAffine(img, M, (w, h))

    📌 پارامترها:
    - src: ۳ نقطه مبدأ — والیوی رایج: pts1, np.float32([[0,0],[w,0],[0,h]])
    - dst: ۳ نقطه مقصد — والیوی رایج: pts2

    📌 برمی‌گردونه: ماتریس تبدیل ۲×۳
    """
    ...

def getPerspectiveTransform(src: Any, dst: Any) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    M = cv2.getPerspectiveTransform(pts1, pts2)
    warped = cv2.warpPerspective(img, M, (w, h))

    📌 پارامترها:
    - src: ۴ نقطه مبدأ — والیوی رایج: pts1, np.float32([[0,0],[w,0],[0,h],[w,h]])
    - dst: ۴ نقطه مقصد — والیوی رایج: pts2

    📌 برمی‌گردونه: ماتریس تبدیل ۳×۳
    """
    ...

def warpPerspective(src: Any, M: Any, dsize: Tuple[int, int]) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    warped = cv2.warpPerspective(img, M, (w, h))

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: img
    - M: ماتریس ۳×۳ — از getPerspectiveTransform
    - dsize: ابعاد خروجی (width, height) — رایج: (w, h)

    📌 برمی‌گردونه: تصویر تبدیل‌شده
    """
    ...

# ============================================================
# کلاس SIFT
# ============================================================
class SIFT:
    def detectAndCompute(
        self, image: Any, mask: Any, descriptors: Any = ...
    ) -> Tuple[Any, Any]:
        """
        🏷️ [Analyze]

        📌 فرمول رایج:
        keypoints, descriptor = sift.detectAndCompute(gray, None)

        📌 پارامترها:
        - image: تصویر خاکستری — والیوی رایج: gray
        - mask: ناحیه جستجو — None یعنی کل تصویر
            رایج: None
        - descriptors: نوشته نمی‌شود — پیش‌فرض None (خودش آرایه جدید می‌سازد)
            رایج: None

        📌 برمی‌گردونه:
        - keypoints: لیست اشیاء KeyPoint
        - descriptor: آرایه NumPy با شکل (تعداد_نقاط, 128) — نوع float32

        📌 نکته: None که نوشته می‌شود = mask (پارامتر دوم)، نه descriptors
        """
        ...

    def detect(self, image: Any, mask: Any = ...) -> Any:
        """
        🏷️ [Analyze]

        📌 فرمول رایج:
        keypoints = sift.detect(gray, None)

        📌 پارامترها:
        - image: تصویر خاکستری — والیوی رایج: gray
        - mask: ناحیه جستجو — None یعنی کل تصویر
            رایج: None

        📌 برمی‌گردونه: لیست نقاط کلیدی (KeyPoint)
        """
        ...

    def compute(
        self, image: Any, keypoints: Any, descriptors: Any = ...
    ) -> Tuple[Any, Any]:
        """
        🏷️ [Analyze]

        📌 فرمول رایج:
        keypoints, descriptors = sift.compute(gray, keypoints)

        📌 پارامترها:
        - image: تصویر خاکستری — والیوی رایج: gray
        - keypoints: لیست نقاط کلیدی
        - descriptors: نوشته نمی‌شود — پیش‌فرض None
            رایج: None

        📌 برمی‌گردونه: (keypoints, descriptors)
        """
        ...

# ============================================================
# کلاس KeyPoint
# ============================================================
class KeyPoint:
    pt: Tuple[float, float]  # مختصات نقطه (x, y)
    size: float  # اندازه نقطه
    angle: float  # زاویه نقطه
    response: float  # قدرت پاسخ
    octave: int  # اکتاو
    class_id: int  # شناسه کلاس

# ============================================================
# ۱۵. عملیات مورفولوژی
# ============================================================
def getStructuringElement(shape: int, ksize: Tuple[int, int]) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

    📌 پارامترها:
    - shape: نوع شکل عنصر ساختاری
        cv2.MORPH_RECT: مستطیل/مربع — برای خطوط و لبه‌های صاف
        cv2.MORPH_ELLIPSE: بیضی/دایره‌ای — برای اشیاء گرد و ارگانیک (پیشنهادی)
        cv2.MORPH_CROSS: ضربدر (+)
    - ksize: سایز کرنل (عرض, ارتفاع) — اجباری، همیشه عدد فرد
        (3,3): کم | (5,5): متوسط | (7,7): زیاد
        رایج: (3, 3), (5, 5), (7, 7), (9, 9)
        باید نسبت به اندازه نویز تنظیم شود، نه اندازه کل تصویر

    📌 برمی‌گردونه: آرایه NumPy uint8 با شکل ksize (فقط ۰ و ۱)

    📌 نکات کلیدی:
    shape قرار نیست شبیه شکل شیء باشد!
    کرنل فقط روش پیمایش است، نه قالبی برای مطابقت با شکل شیء.
    کرنل خودش نمی‌چرخد — برای اشیاء چرخیده از ELLIPSE استفاده کن.
    """
    ...

def erode(src: Any, kernel: Any, iterations: int = ...) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    eroded = cv2.erode(th, kernel, 1)

    📌 پارامترها:
    - src: تصویر ورودی — باینری یا گری‌اسکیل (شیء سفید، پس‌زمینه سیاه)
           والیوی رایج: th, gray, dilated
    - kernel: کرنل ساختاری — از getStructuringElement
        رایج: kernel, np.ones((5,5), np.uint8)
    - iterations (اختیاری): تعداد تکرار — پیش‌فرض: 1 | رایج: 1 تا 3
        بیشتر = فرسایش شدیدتر
        رایج: 1, 2, 3
        نیازی به نوشتن نام پارامتر نیست، فقط عدد را بنویس.

    📌 برمی‌گردونه: تصویر Eroded (نواحی سفید باریک شده)

    📌 کاربرد:
    حذف نویزهای ریز سفید
    نازک کردن اشیاء
    جدا کردن دو شیء چسبیده
    """
    ...

def dilate(src: Any, kernel: Any, iterations: int = ...) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    dilated = cv2.dilate(th, kernel, 1)

    📌 پارامترها: مشابه erode
    - src: والیوی رایج: th, gray, eroded
    - kernel: کرنل ساختاری — رایج: kernel
    - iterations: نیازی به نوشتن نام پارامتر نیست، فقط عدد را بنویس.
        رایج: 1, 2, 3, 5

    📌 برمی‌گردونه: تصویر Dilated (نواحی سفید گسترش یافته)

    📌 کاربرد:
    پر کردن سوراخ‌های کوچک داخل شیء
    وصل کردن قطعات جدا شده
    بزرگ کردن ناحیه شیء
    """
    ...

def morphologyEx(src: Any, op: int, kernel: Any, iterations: int = ...) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    opened = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)     — Opening (حذف نویز)
    closed = cv2.morphologyEx(th, cv2.MORPH_CLOSE, kernel)    — Closing (پر کردن حفره)
    tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel) — Top-Hat

    📌 پارامترها:
    - src: تصویر ورودی — والیوی رایج: th یا gray
    - op: نوع عملیات
        cv2.MORPH_OPEN: Erode سپس Dilate — حذف نویز سفید بدون تغییر اندازه
        cv2.MORPH_CLOSE: Dilate سپس Erode — پر کردن حفره بدون تغییر اندازه
        cv2.MORPH_GRADIENT: Dilate - Erode — لبه‌ها
        cv2.MORPH_TOPHAT: src - Opening — حذف بافت سطحی
        cv2.MORPH_BLACKHAT: Closing - src — پیدا کردن حفره‌های تیره
    - kernel: کرنل ساختاری — از getStructuringElement
        رایج: kernel
    - iterations (اختیاری): تعداد تکرار — پیش‌فرض: 1
        رایج: 1, 2

    📌 برمی‌گردونه: تصویر مورفولوژی‌شده

    📌 چه زمانی تکی و چه زمانی ترکیبی؟
    فقط کوچیک کردن شیء → Erosion تنها
    فقط بزرگ کردن شیء → Dilation تنها
    حذف نویز بدون تغییر اندازه → Opening
    پر کردن سوراخ بدون تغییر اندازه → Closing
    """
    ...

# ============================================================
# ۱۶. بهبود کنتراست
# ============================================================
def equalizeHist(src: Any) -> Any:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    equalized = cv2.equalizeHist(gray)

    📌 پارامترها:
    - src: تصویر ورودی — حتماً Grayscale و uint8
           والیوی رایج: gray

    📌 برمی‌گردونه: تصویر با هیستوگرام یکسان‌سازی شده

    📌 کاربردها:
    تصاویر پزشکی (X-ray, MRI, CT)
    پیش‌پردازش برای تشخیص لبه، OCR، تشخیص چهره
    تصاویر ماهواره‌ای و هوایی

    📌 نامناسب برای:
    عکس‌های طبیعی و هنری (پرتره، منظره)
    تصاویر با پس‌زمینه سفید
    """
    ...

def createCLAHE(clipLimit: float = ..., tileGridSize: Tuple[int, int] = ...) -> CLAHE:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray)

    📌 پارامترها:
    - clipLimit: سقف محدودسازی کنتراست
        پیش‌فرض: 40 (خیلی زیاد!) | مقدار رایج: 2 تا 4
        بزرگ‌تر = کنتراست بیشتر ولی نویز بیشتر
        رایج: 2.0, 3.0, 4.0, 10.0
    - tileGridSize: اندازه گرید بلوک‌بندی
        پیش‌فرض: (8, 8) = ۶۴ بلوک | مقدار رایج: (8, 8)
        رایج: (8, 8), (16, 16), (4, 4)

    📌 برمی‌گردونه: شیء CLAHE — باید متد apply() صدا زده شود

    📌 تفاوت:
    equalizeHist → سراسری (Global) — [Analyze]
    CLAHE → موضعی (Local) — [Preprocess] — برای نور نامتقارن بهتر است
    """
    ...

# ============================================================
# کلاس CLAHE
# ============================================================
class CLAHE:
    def apply(self, src: Any) -> Any:
        """
        🏷️ [Preprocess]

        📌 فرمول رایج:
        clahe_img = clahe.apply(gray)

        📌 پارامترها:
        - src: تصویر ورودی — والیوی رایج: gray

        📌 برمی‌گردونه: تصویر پردازش‌شده
        """
        ...

# ============================================================
# ۱۷. کانتور و اشکال
# ============================================================
def findContours(image: Any, mode: int, method: int) -> Tuple[Any, Any]:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    contours, hierarchy = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    📌 پارامترها:
    - image: تصویر باینری ورودی (خروجی Threshold)
              والیوی رایج: th, thresh, binary, mask
    - mode: نحوه بازیابی کانتورها
        cv2.RETR_EXTERNAL: فقط کانتورهای بیرونی (پرکاربردترین)
        cv2.RETR_LIST: همه کانتورها بدون سلسله‌مراتب
        cv2.RETR_TREE: همه کانتورها با روابط تو در تو
        cv2.RETR_CCOMP: همه کانتورها با سلسله‌مراتب دو سطحی
    - method: نحوه ذخیره نقاط
        cv2.CHAIN_APPROX_SIMPLE: فقط نقاط ضروری (پرکاربردترین)
        cv2.CHAIN_APPROX_NONE: تمام نقاط مرزی

    📌 برمی‌گردونه: (contours, hierarchy)
    - contours: لیستی از آرایه‌های NumPy
    - hierarchy: آرایه NumPy شامل اطلاعات تو در تو

    📌 قوانین طلایی:
    کانتور روی باینری (Threshold) زده می‌شود، نه روی Canny
    RETR_EXTERNAL برای استخراج مرز بیرونی از تصویر باینری شلوغ
    """
    ...

def drawContours(
    image: Any,
    contours: Any,
    contourIdx: int,
    color: Tuple[int, int, int],
    thickness: int,
) -> None:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    output = img.copy()
    cv2.drawContours(output, contours, -1, (0, 255, 0), 3)

    📌 ساخت ماسک با drawContours:
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [biggest], -1, 255, -1)

    📌 پارامترها:
    - image: تصویری که کانتور روی آن رسم می‌شود — والیوی رایج: output (کپی از img), mask
    - contours: خروجی findContours — رایج: contours, [biggest], biggest_closed_contours
    - contourIdx: اندیس کانتور — -1 یعنی همه
        رایج: -1, 0, 1
    - color: رنگ خط (B, G, R) — برای ماسک: 255
        رایج: (0, 255, 0), (0, 0, 255), (255, 0, 0), 255
    - thickness: ضخامت خط — -1 یعنی توپر (FILLED)
        رایج: 2, 3, 5, -1

    📌 خروجی: None — تصویر ورودی مستقیماً تغییر می‌کند (In-place)
    📌 نکته: حتماً قبل از رسم، img.copy() بگیر.
    """
    ...

def boundingRect(contour: Any) -> Tuple[int, int, int, int]:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    x, y, w, h = cv2.boundingRect(biggest)
    cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)
    roi = img[y:y+h, x:x+w]

    📌 پارامترها:
    - contour: یک کانتور واحد — معمولاً بزرگ‌ترین کانتور
        رایج: biggest, contour, max(contours, key=cv2.contourArea)

    📌 برمی‌گردونه: (x, y, w, h)
    """
    ...

def contourArea(contour: Any) -> float:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    area = cv2.contourArea(contour)

    📌 انتخاب بزرگ‌ترین کانتور:
    biggest = max(contours, key=cv2.contourArea)

    📌 پارامترها:
    - contour: کانتور واحد — رایج: contour, c, biggest
    """
    ...

def arcLength(curve: Any, closed: bool) -> float:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    perimeter = cv2.arcLength(contour, True)

    📌 پارامترها:
    - curve: کانتور — رایج: contour, c
    - closed: آیا کانتور بسته است؟ — رایج: True
    """
    ...

def approxPolyDP(curve: Any, epsilon: float, closed: bool) -> Any:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

    📌 پارامترها:
    - curve: کانتور — رایج: contour
    - epsilon: حداکثر فاصله از کانتور اصلی
        رایج: 0.02 * perimeter, 0.01 * perimeter, 0.05 * perimeter
    - closed: آیا کانتور بسته است؟ — رایج: True
    """
    ...

def moments(array: Any) -> dict:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    M = cv2.moments(contour)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])

    📌 پارامترها:
    - array: کانتور — رایج: contour, c
    """
    ...

def putText(
    img: Any,
    text: str,
    org: Tuple[int, int],
    fontFace: int,
    fontScale: float,
    color: Tuple[int, int, int],
    thickness: int,
    lineType: int = ...,
    bottomLeftOrigin: bool = ...,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.putText(img, "Hello", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    📌 پارامترها:
    - img: تصویری که متن روی آن رسم می‌شود — رایج: img, boxes, result
    - text: متن مورد نظر برای نمایش — رایج: "Hello", f"Area: {area}", "Object"
    - org: مختصات گوشه پایین-چپ متن (x, y) — رایج: (10, 50), (20, 30)
    - fontFace: نوع فونت — رایج: cv2.FONT_HERSHEY_SIMPLEX
    - fontScale: ضریب مقیاس فونت (1 = اندازه معمولی) — رایج: 0.5, 1.0, 2.0
    - color: رنگ متن به فرمت BGR — رایج: (0, 0, 255), (0, 255, 0), (255, 255, 255)
    - thickness: ضخامت خطوط متن (پیکسل) — رایج: 1, 2, 3
    - lineType (اختیاری): نوع خط — پیش‌فرض: cv2.LINE_8 — رایج: cv2.LINE_AA
    - bottomLeftOrigin (اختیاری): مبدأ مختصات — پیش‌فرض: False

    📌 برمی‌گردونه: تصویر با متن رسم‌شده
    """
    ...

def rectangle(
    img: Any,
    pt1: Tuple[int, int],
    pt2: Tuple[int, int],
    color: Tuple[int, int, int],
    thickness: int,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 2)

    📌 پارامترها:
    - img: تصویر مقصد — رایج: boxes, img, output
    - pt1: گوشه بالا-چپ (x, y) — رایج: (x, y), (0, 0)
    - pt2: گوشه پایین-راست (x+w, y+h) — رایج: (x+w, y+h), (100, 100)
    - color: رنگ مستطیل BGR — رایج: (0, 255, 0), (0, 0, 255)
    - thickness: ضخامت خط — رایج: 2, 3, 5, -1 (توپر)

    📌 برمی‌گردونه: تصویر با مستطیل رسم‌شده
    """
    ...

def circle(
    img: Any,
    center: Tuple[int, int],
    radius: int,
    color: Tuple[int, int, int],
    thickness: int,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.circle(img, (50, 50), 30, (255, 0, 0), -1)

    📌 پارامترها:
    - img: تصویر مقصد — رایج: img, output
    - center: مرکز دایره (x, y) — رایج: (cx, cy), (50, 50)
    - radius: شعاع دایره — رایج: 30, 50, 100
    - color: رنگ دایره BGR — رایج: (255, 0, 0), (0, 255, 0)
    - thickness: ضخامت خط — رایج: 2, 3, -1 (توپر)

    📌 برمی‌گردونه: تصویر با دایره رسم‌شده
    """
    ...

def line(
    img: Any,
    pt1: Tuple[int, int],
    pt2: Tuple[int, int],
    color: Tuple[int, int, int],
    thickness: int,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.line(img, (0, 0), (100, 100), (0, 0, 255), 2)

    📌 پارامترها:
    - img: تصویر مقصد — رایج: img, output
    - pt1: نقطه شروع (x, y) — رایج: (0, 0), (x1, y1)
    - pt2: نقطه پایان (x, y) — رایج: (100, 100), (x2, y2)
    - color: رنگ خط BGR — رایج: (0, 0, 255), (255, 0, 0)
    - thickness: ضخامت خط — رایج: 2, 3, 5

    📌 برمی‌گردونه: تصویر با خط رسم‌شده
    """
    ...

def arrowedLine(
    img: Any,
    pt1: Tuple[int, int],
    pt2: Tuple[int, int],
    color: Tuple[int, int, int],
    thickness: int,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.arrowedLine(img, (0, 0), (100, 100), (255, 0, 0), 2)

    📌 پارامترها:
    - img: تصویر مقصد — رایج: img
    - pt1: نقطه شروع — رایج: (0, 0)
    - pt2: نقطه پایان — رایج: (100, 100)
    - color: رنگ BGR — رایج: (255, 0, 0)
    - thickness: ضخامت — رایج: 2, 3
    """
    ...

def ellipse(
    img: Any,
    center: Tuple[int, int],
    axes: Tuple[int, int],
    angle: float,
    startAngle: float,
    endAngle: float,
    color: Tuple[int, int, int],
    thickness: int,
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.ellipse(img, (100, 100), (50, 30), 45, 0, 360, (0, 255, 0), 2)

    📌 پارامترها:
    - img: تصویر مقصد — رایج: img
    - center: مرکز بیضی — رایج: (100, 100), (cx, cy)
    - axes: نیم‌محورها (عرض, ارتفاع) — رایج: (50, 30), (100, 50)
    - angle: زاویه چرخش بیضی — رایج: 0, 45, 90
    - startAngle: زاویه شروع — رایج: 0
    - endAngle: زاویه پایان — رایج: 360
    - color: رنگ BGR — رایج: (0, 255, 0)
    - thickness: ضخامت — رایج: 2, -1
    """
    ...

def fillPoly(img: Any, pts: Any, color: Tuple[int, int, int]) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.fillPoly(img, [pts], (255, 0, 0))

    📌 پارامترها:
    - img: تصویر مقصد — رایج: img, mask
    - pts: نقاط چندضلعی — رایج: [pts], [contour]
    - color: رنگ BGR — رایج: (255, 0, 0), 255
    """
    ...

def polylines(
    img: Any, pts: Any, isClosed: bool, color: Tuple[int, int, int], thickness: int
) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    cv2.polylines(img, [pts], True, (0, 255, 0), 2)

    📌 پارامترها:
    - img: تصویر مقصد — رایج: img
    - pts: نقاط چندضلعی — رایج: [pts], [contour]
    - isClosed: بسته بودن شکل — رایج: True, False
    - color: رنگ BGR — رایج: (0, 255, 0)
    - thickness: ضخامت — رایج: 2, 3
    """
    ...

# ============================================================
# ۱۸. عملیات بیتی و ترکیب تصاویر
# ============================================================
def bitwise_and(src1: Any, src2: Any, mask: Any = ...) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    masked = cv2.bitwise_and(img, img, mask=mask)

    📌 کاربرد ویژه در Mask (جداسازی دقیق شیء):
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [biggest], -1, 255, -1)
    masked = cv2.bitwise_and(img, img, mask=mask)

    📌 پارامترها:
    - src1: تصویر اول — والیوی رایج: img
    - src2: تصویر دوم — والیوی رایج: img (وقتی ماسک داریم)
    - mask: ماسک تک‌کاناله — فقط پیکسل‌های سفید ماسک باقی می‌مانند
        رایج: mask, None

    📌 برمی‌گردونه: تصویر ترکیب‌شده
    """
    ...

def bitwise_or(src1: Any, src2: Any, mask: Any = ...) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.bitwise_or(img1, img2) — OR بیتی

    📌 پارامترها:
    - src1: تصویر اول — رایج: img1
    - src2: تصویر دوم — رایج: img2
    - mask: ماسک — رایج: None, mask
    """
    ...

def bitwise_not(src: Any, mask: Any = ...) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    inverted = cv2.bitwise_not(th) — NOT بیتی (معکوس)

    📌 پارامترها:
    - src: تصویر — رایج: th, img
    - mask: ماسک — رایج: None
    """
    ...

def bitwise_xor(src1: Any, src2: Any, mask: Any = ...) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.bitwise_xor(img1, img2) — XOR بیتی

    📌 پارامترها:
    - src1: تصویر اول — رایج: img1
    - src2: تصویر دوم — رایج: img2
    - mask: ماسک — رایج: None
    """
    ...

def addWeighted(src1: Any, alpha: float, src2: Any, beta: float, gamma: float) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    blended = cv2.addWeighted(img1, 0.7, img2, 0.3, 0) — ترکیب دو تصویر با وزن

    📌 پارامترها:
    - src1: تصویر اول — رایج: img1, img
    - alpha: وزن تصویر اول — رایج: 0.5, 0.7, 0.3
    - src2: تصویر دوم — رایج: img2, overlay
    - beta: وزن تصویر دوم — رایج: 0.5, 0.3, 0.7
    - gamma: مقدار اضافه — رایج: 0

    📌 برمی‌گردونه: تصویر ترکیبی
    """
    ...

def add(src1: Any, src2: Any) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.add(img1, img2) — جمع دو تصویر

    📌 پارامترها:
    - src1: تصویر اول — رایج: img1
    - src2: تصویر دوم — رایج: img2
    """
    ...

def subtract(src1: Any, src2: Any) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.subtract(img1, img2) — تفریق دو تصویر

    📌 پارامترها:
    - src1: تصویر اول — رایج: img1
    - src2: تصویر دوم — رایج: img2
    """
    ...

def convertScaleAbs(src: Any, alpha: float = ..., beta: float = ...) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

    📌 پارامترها:
    - src: تصویر — رایج: img
    - alpha: ضریب مقیاس — رایج: 1.0, 1.5, 2.0
    - beta: مقدار اضافه — رایج: 0, 50, 100
    """
    ...

def normalize(src: Any, dst: Any, alpha: float, beta: float, norm_type: int) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    result = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

    📌 پارامترها:
    - src: تصویر ورودی — رایج: img, gray
    - dst: تصویر خروجی — رایج: None
    - alpha: حد پایین — رایج: 0
    - beta: حد بالا — رایج: 255
    - norm_type: نوع نرمال‌سازی — رایج: cv2.NORM_MINMAX
    """
    ...

def split(m: Any) -> Tuple[Any, Any, Any]:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    b, g, r = cv2.split(img) — جدا کردن کانال‌های BGR

    📌 پارامترها:
    - m: تصویر رنگی — رایج: img, hsv
    """
    ...

def merge(mv: Tuple[Any, Any, Any]) -> Any:
    """
    🏷️ [Visualize]

    📌 فرمول رایج:
    merged = cv2.merge([b, g, r]) — ترکیب کانال‌ها

    📌 پارامترها:
    - mv: لیست کانال‌ها — رایج: [b, g, r], [h, s, v]
    """
    ...

# ============================================================
# ۱۹. توابع کمکی OpenCV
# ============================================================
def inRange(src: Any, lowerb: Any, upperb: Any) -> Any:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    📌 پارامترها:
    - src: تصویر — رایج: hsv, img
    - lowerb: حد پایین — رایج: np.array([0, 50, 50])
    - upperb: حد بالا — رایج: np.array([10, 255, 255])
    """
    ...

def countNonZero(src: Any) -> int:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    count = cv2.countNonZero(th)

    📌 پارامترها:
    - src: تصویر باینری — رایج: th, mask
    """
    ...

def minMaxLoc(
    src: Any, mask: Any = ...
) -> Tuple[float, float, Tuple[int, int], Tuple[int, int]]:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray)

    📌 پارامترها:
    - src: تصویر — رایج: gray, result
    - mask: ماسک — رایج: None
    """
    ...

def matchTemplate(image: Any, templ: Any, method: int) -> Any:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    📌 پارامترها:
    - image: تصویر اصلی — رایج: img, gray
    - templ: الگو — رایج: template
    - method: روش تطبیق — رایج: cv2.TM_CCOEFF_NORMED
    """
    ...

def copyMakeBorder(
    src: Any, top: int, bottom: int, left: int, right: int, borderType: int
) -> Any:
    """
    🏷️ [Preprocess]

    📌 فرمول رایج:
    bordered = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)

    📌 پارامترها:
    - src: تصویر — رایج: img
    - top: حاشیه بالا — رایج: 10
    - bottom: حاشیه پایین — رایج: 10
    - left: حاشیه چپ — رایج: 10
    - right: حاشیه راست — رایج: 10
    - borderType: نوع حاشیه — رایج: cv2.BORDER_CONSTANT
    """
    ...

def calcHist(images: Any, channels: Any, mask: Any, histSize: Any, ranges: Any) -> Any:
    """
    🏷️ [Analyze]

    📌 فرمول رایج:
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    📌 پارامترها:
    - images: لیست تصاویر — [img]
        رایج: [img], [gray]
    - channels: اندیس کانال — [0] برای خاکستری, [0],[1],[2] برای BGR
        رایج: [0]
    - mask: ماسک — None یعنی کل تصویر
        رایج: None
    - histSize: تعداد bins — [256]
        رایج: [256]
    - ranges: بازه مقادیر — [0, 256]
        رایج: [0, 256]

    📌 برمی‌گردونه: آرایه هیستوگرام
    """
    ...

# ============================================================
# ۲۰. ثابت‌ها و enumهای OpenCV
# ============================================================

# --- خواندن تصویر --- [Preprocess]
IMREAD_COLOR: int  # = 1
IMREAD_GRAYSCALE: int  # = 0
IMREAD_UNCHANGED: int  # = -1
IMREAD_COLOR_RGB: int  # = 4
IMREAD_REDUCED_COLOR_2: int  # = 17

# --- تبدیل رنگ --- [Preprocess]
COLOR_BGR2GRAY: int  # = 6
COLOR_BGR2RGB: int  # = 4
COLOR_GRAY2BGR: int  # = 8
COLOR_RGB2BGR: int  # = 2
COLOR_BGR2HSV: int  # = 40
COLOR_HSV2BGR: int  # = 54

# --- چرخش ۹۰ درجه --- [Preprocess]
ROTATE_90_CLOCKWISE: int  # = 0
ROTATE_180: int  # = 1
ROTATE_90_COUNTERCLOCKWISE: int  # = 2

# --- پنجره --- [Visualize]
WINDOW_NORMAL: int  # = 0x00000000
WINDOW_AUTOSIZE: int  # = 0x00000001
WINDOW_FULLSCREEN: int  # = 1
WINDOW_FREERATIO: int  # = 0x00000100
WINDOW_KEEPRATIO: int  # = 0x00000000
WND_PROP_VISIBLE: int  # = 0

# --- Threshold --- [Preprocess]
THRESH_BINARY: int  # = 0
THRESH_BINARY_INV: int  # = 1
THRESH_TRUNC: int  # = 2
THRESH_TOZERO: int  # = 3
THRESH_TOZERO_INV: int  # = 4
THRESH_OTSU: int  # = 8
THRESH_TRIANGLE: int  # = 16

# --- Adaptive Threshold --- [Preprocess]
ADAPTIVE_THRESH_MEAN_C: int  # = 0
ADAPTIVE_THRESH_GAUSSIAN_C: int  # = 1

# --- Interpolation --- [Preprocess]
INTER_LINEAR: int  # = 1
INTER_AREA: int  # = 3
INTER_CUBIC: int  # = 2
INTER_NEAREST: int  # = 0
INTER_LANCZOS4: int  # = 4

# --- فونت --- [Visualize]
FONT_HERSHEY_SIMPLEX: int  # = 0
FONT_HERSHEY_PLAIN: int  # = 1
FONT_HERSHEY_DUPLEX: int  # = 2
FONT_HERSHEY_COMPLEX: int  # = 3
FONT_HERSHEY_TRIPLEX: int  # = 4
FONT_HERSHEY_COMPLEX_SMALL: int  # = 5
FONT_HERSHEY_SCRIPT_SIMPLEX: int  # = 6
FONT_HERSHEY_SCRIPT_COMPLEX: int  # = 7
FONT_ITALIC: int  # = 16

# --- خط --- [Visualize]
LINE_AA: int  # = 16
LINE_4: int  # = 4
LINE_8: int  # = 8
FILLED: int  # = -1

# --- Contour --- [Analyze]
RETR_EXTERNAL: int  # = 0
RETR_LIST: int  # = 1
RETR_CCOMP: int  # = 2
RETR_TREE: int  # = 3
CHAIN_APPROX_NONE: int  # = 1
CHAIN_APPROX_SIMPLE: int  # = 2
CHAIN_APPROX_TC89_L1: int  # = 3
CHAIN_APPROX_TC89_KCOS: int  # = 4

# --- Morphology --- [Preprocess]
MORPH_RECT: int  # = 0
MORPH_CROSS: int  # = 1
MORPH_ELLIPSE: int  # = 2
MORPH_OPEN: int  # = 2
MORPH_CLOSE: int  # = 3
MORPH_GRADIENT: int  # = 4
MORPH_TOPHAT: int  # = 5
MORPH_BLACKHAT: int  # = 6

# --- Norm --- [Visualize]
NORM_MINMAX: int  # = 32
NORM_L1: int  # = 2
NORM_L2: int  # = 4
NORM_INF: int  # = 1

# --- Border --- [Preprocess]
BORDER_CONSTANT: int  # = 0
BORDER_REFLECT: int  # = 2
BORDER_REPLICATE: int  # = 1
BORDER_WRAP: int  # = 3

# --- Template Matching --- [Analyze]
TM_SQDIFF: int  # = 0
TM_SQDIFF_NORMED: int  # = 1
TM_CCORR: int  # = 2
TM_CCORR_NORMED: int  # = 3
TM_CCOEFF: int  # = 4
TM_CCOEFF_NORMED: int  # = 5