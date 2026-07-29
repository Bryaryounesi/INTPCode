from typing import Any, Tuple
import numpy as np

# ============================================================
# ۱. خواندن تصویر
# ============================================================
def imread(filename: str, flags: int = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.imread(path)
    cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    📌 پارامترها:
    - filename: مسیر فایل تصویری
    - flags (اختیاری): نحوه خواندن — پیش‌فرض: cv2.IMREAD_COLOR (رنگی BGR)
        cv2.IMREAD_GRAYSCALE: خاکستری
        cv2.IMREAD_UNCHANGED: با کانال آلفا
        cv2.IMREAD_COLOR_RGB: رنگی RGB

    📌 برمی‌گردونه: آرایه NumPy تصویر (None اگر خطا دهد)
    """
    ...

# ============================================================
# ۲. نمایش تصویر
# ============================================================
def imshow(winname: str, img: Any) -> None:
    """
    📌 فرمول رایج:
    cv2.imshow("Window Name", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    📌 پارامترها:
    - winname: نام پنجره (رشته دلخواه)
    - img: آرایه تصویری
    """
    ...

def waitKey(delay: int = ...) -> int:
    """
    📌 فرمول رایج:
    cv2.waitKey(0)

    📌 پارامترها:
    - delay: میلی‌ثانیه صبر — 0 یعنی تا زدن یک کلید | 2000 یعنی ۲ ثانیه

    📌 برمی‌گردونه: کد ASCII کلید فشرده شده
    """
    ...

def destroyAllWindows() -> None:
    """📌 فرمول رایج: cv2.destroyAllWindows() — بستن همه پنجره‌ها"""
    ...

def destroyWindow(winname: str) -> None:
    """
    📌 فرمول رایج:
    cv2.destroyWindow("win") — بستن یک پنجره خاص
    """
    ...

def namedWindow(winname: str, flags: int = ...) -> None:
    """
    📌 فرمول رایج:
    cv2.namedWindow("win", cv2.WINDOW_NORMAL)

    📌 پارامترها:
    - winname: نام پنجره
    - flags: cv2.WINDOW_NORMAL (قابل تغییر اندازه) | cv2.WINDOW_AUTOSIZE (پیش‌فرض)
    """
    ...

def resizeWindow(winname: str, width: int, height: int) -> None:
    """
    📌 فرمول رایج:
    cv2.resizeWindow("win", 800, 600)

    📌 پارامترها:
    - winname: نام پنجره
    - width: عرض به پیکسل
    - height: ارتفاع به پیکسل
    """
    ...

def getWindowProperty(winname: str, prop_id: int) -> float:
    """
    📌 فرمول رایج:
    cv2.getWindowProperty("win", cv2.WND_PROP_VISIBLE)

    📌 پارامترها:
    - winname: نام پنجره
    - prop_id: شناسه ویژگی — cv2.WND_PROP_VISIBLE برای بررسی باز بودن پنجره

    📌 برمی‌گردونه: مقدار ویژگی (مثلاً 1.0 یعنی باز است)
    """
    ...

# ============================================================
# ۳. تبدیل رنگ
# ============================================================
def cvtColor(src: Any, code: int) -> Any:
    """
    📌 فرمول رایج:
    cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    📌 پارامترها:
    - src: تصویر ورودی
    - code: کد تبدیل رنگ
        cv2.COLOR_BGR2GRAY: رنگی BGR به خاکستری
        cv2.COLOR_BGR2RGB: BGR به RGB (برای نمایش با Matplotlib)
        cv2.COLOR_GRAY2BGR: خاکستری به رنگی ۳ کاناله
        cv2.COLOR_BGR2HSV: BGR به HSV
        cv2.COLOR_HSV2BGR: HSV به BGR
        cv2.COLOR_RGB2BGR: RGB به BGR

    📌 برمی‌گردونه: تصویر تبدیل‌شده
    """
    ...

# ============================================================
# ۴. ذخیره تصویر
# ============================================================
def imwrite(filename: str, img: Any) -> bool:
    """
    📌 فرمول رایج:
    cv2.imwrite("output.jpg", img)

    📌 پارامترها:
    - filename: مسیر و نام فایل با پسوند (مثلاً "result.jpg")
    - img: تصویر مورد نظر برای ذخیره

    📌 برمی‌گردونه: True اگر موفق بود
    """
    ...

# ============================================================
# ۵. تغییر اندازه
# ============================================================
def resize(
    src: Any,
    dsize: Tuple[int, int] | None,
    fx: float = ...,
    fy: float = ...,
    interpolation: int = ...,
) -> Any:
    """
    📌 فرمول رایج:
    cv2.resize(img, (width, height))                    ← با ابعاد دقیق
    cv2.resize(img, None, fx=0.6, fy=0.6)               ← با ضریب مقیاس

    📌 پارامترها:
    - src: تصویر ورودی
    - dsize: ابعاد خروجی (width, height) — اگر None، باید fx و fy را بدهی
    - fx (اختیاری): ضریب مقیاس افقی — 0.6 یعنی ۶۰٪ عرض اولیه
    - fy (اختیاری): ضریب مقیاس عمودی — 0.6 یعنی ۶۰٪ ارتفاع اولیه
    - interpolation (اختیاری): روش درون‌یابی — پیش‌فرض: cv2.INTER_LINEAR
        cv2.INTER_AREA: بهترین برای کوچک‌سازی (پیشنهادی)
        cv2.INTER_CUBIC: بهترین برای بزرگ‌نمایی
        cv2.INTER_NEAREST: سریع (برای ماسک)

    📌 برمی‌گردونه: تصویر تغییر اندازه داده شده
    """
    ...

# ============================================================
# ۶. چرخش
# ============================================================
def rotate(src: Any, rotateCode: int) -> Any:
    """
    📌 فرمول رایج:
    cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    📌 پارامترها:
    - src: تصویر ورودی
    - rotateCode:
        cv2.ROTATE_90_CLOCKWISE: ۹۰° ساعتگرد
        cv2.ROTATE_180: ۱۸۰°
        cv2.ROTATE_90_COUNTERCLOCKWISE: ۹۰° پادساعتگرد

    📌 برمی‌گردونه: تصویر چرخانده شده
    """
    ...

def getRotationMatrix2D(center: Tuple[float, float], angle: float, scale: float) -> Any:
    """
    📌 فرمول رایج:
    cv2.getRotationMatrix2D((w//2, h//2), 30, 1.0)

    📌 پارامترها:
    - center: مرکز چرخش (x, y) — معمولاً (w//2, h//2)
    - angle: زاویه به درجه — مثبت = پادساعتگرد
    - scale: ضریب مقیاس — 1.0 یعنی بدون تغییر اندازه

    📌 برمی‌گردونه: ماتریس تبدیل ۲×۳ برای warpAffine
    """
    ...

def warpAffine(src: Any, M: Any, dsize: Tuple[int, int]) -> Any:
    """
    📌 فرمول رایج:
    cv2.warpAffine(img, M, (new_w, new_h))

    📌 پارامترها:
    - src: تصویر ورودی
    - M: ماتریس تبدیل ۲×۳ (از getRotationMatrix2D)
    - dsize: ابعاد خروجی (width, height)

    📌 برمی‌گردونه: تصویر تبدیل‌شده
    """
    ...

# ============================================================
# ۷. وارونه‌سازی
# ============================================================
def flip(src: Any, flipCode: int) -> Any:
    """
    📌 فرمول رایج:
    cv2.flip(img, 1)

    📌 پارامترها:
    - src: تصویر ورودی
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
    📌 فرمول رایج:
    cv2.GaussianBlur(img, (5, 5), 0)

    📌 پارامترها:
    - src: تصویر ورودی (رنگی یا خاکستری)
    - ksize: اندازه کرنل (width, height) — هر دو باید فرد باشند
        (3,3): کم | (5,5): متوسط (پیشنهادی) | (9,9): زیاد
    - sigmaX: انحراف معیار افقی — 0 یعنی خودکار از ksize (پیشنهادی)
    - sigmaY (اختیاری): انحراف معیار عمودی — پیش‌فرض = sigmaX

    📌 برمی‌گردونه: تصویر بلور شده
    """
    ...

# ============================================================
# ۹. Median Blur
# ============================================================
def medianBlur(src: Any, ksize: int) -> Any:
    """
    📌 فرمول رایج:
    cv2.medianBlur(img, 5)

    📌 پارامترها:
    - src: تصویر ورودی
    - ksize: اندازه کرنل — یک عدد فرد (نه تاپل!)
        3: کم | 5: متوسط (پیشنهادی) | 9: زیاد

    📌 برمی‌گردونه: تصویر بلور شده
    📌 کاربرد: حذف نویز نمک-فلفل (لبه‌ها را تیز نگه می‌دارد)
    """
    ...

# ============================================================
# ۱۰. Threshold ساده
# ============================================================
def threshold(src: Any, thresh: float, maxval: float, type: int) -> Tuple[float, Any]:
    """
    📌 فرمول رایج:
    ret, dst = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)

    📌 پارامترها:
    - src: تصویر Grayscale (تک کاناله)
    - thresh: عدد آستانه (0 تا 255) — کم = سفیدتر | زیاد = سیاه‌تر
        127: رایج‌ترین | 50: روشن | 200: تیره
    - maxval: مقدار پیکسل‌های عبورکرده — معمولاً 255
    - type: نوع آستانه‌گذاری
        cv2.THRESH_BINARY: بالای آستانه = maxval (پیشفرض ذهنی)
        cv2.THRESH_BINARY_INV: معکوس حالت بالا
        cv2.THRESH_TRUNC: بالای آستانه = خود آستانه
        cv2.THRESH_TOZERO: پایین آستانه = 0
        cv2.THRESH_TOZERO_INV: معکوس TOZERO

    📌 برمی‌گردونه: (ret, dst) — ret = thresh استفاده‌شده | dst = تصویر باینری
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
    📌 فرمول رایج:
    cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

    📌 پارامترها (هر ۶ تا اجباری):
    - src: تصویر Grayscale
    - maxValue: مقدار پیکسل‌های سفید — معمولاً 255
    - adaptiveMethod:
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C: میانگین وزن‌دار (پیشنهادی)
        cv2.ADAPTIVE_THRESH_MEAN_C: میانگین ساده
    - thresholdType: معمولاً cv2.THRESH_BINARY
    - blockSize: اندازه ناحیه — عدد فرد
        11: جزئیات بیشتر | 21: نرم‌تر (پیشنهادی برای متون)
    - C: ثابت تصحیح — از میانگین کم می‌شود
        2: پیش‌فرض | 3: معمولی | 7: خطوط پیوسته‌تر
        بزرگتر = تصویر تیره‌تر و پیوسته‌تر

    📌 برمی‌گردونه: تصویر باینری تطبیقی
    📌 کاربرد: تصاویر با نور غیریکنواخت (سایه‌دار)
    """
    ...

# ============================================================
# ۱۲. Canny Edge Detection
# ============================================================
def Canny(image: Any, threshold1: float, threshold2: float) -> Any:
    """
    📌 فرمول رایج:
    cv2.Canny(blurred_img, 50, 150)

    📌 پارامترها:
    - image: تصویر Grayscale (حتماً قبلش بلور کن!)
    - threshold1: حد پایین هیسترزیس
    - threshold2: حد بالا هیسترزیس
    نسبت پیشنهادی 1:2 یا 1:3
    بهترین مقادیر تجربی: (50,150) | (80,200) | (80,240)

    📌 برمی‌گردونه: تصویر لبه‌ها
    📌 قانون طلایی: همیشه قبل از Canny بلور کن!
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
    📌 فرمول رایج:
    sift = cv2.SIFT_create()
    keypoints, descriptor = sift.detectAndCompute(img, None)
    result = cv2.drawKeypoints(img, keypoints, None)

    📌 پارامترهای اختیاری:
    - nfeatures: حداکثر تعداد نقاط — 0 = نامحدود (پیش‌فرض)
    - nOctaveLayers: تعداد لایه در هر اکتاو — پیش‌فرض 3
    - contrastThreshold: آستانه حذف نقاط ضعیف — پیش‌فرض 0.04
    - edgeThreshold: آستانه حذف نقاط لبه — پیش‌فرض 10
    - sigma: سیگمای گاوسین اولیه — پیش‌فرض 1.6

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
    📌 فرمول رایج:
    cv2.drawKeypoints(img, keypoints, None)

    📌 پارامترها:
    - image: تصویر منبع
    - keypoints: لیست نقاط کلیدی
    - outImage: تصویر مقصد — None یعنی تصویر جدید بساز
    - color (اختیاری): رنگ نقاط — پیش‌فرض: تصادفی
    - flags (اختیاری): نحوه رسم — پیش‌فرض: فقط دایره مرکز

    📌 برمی‌گردونه: تصویر با نقاط رسم‌شده
    """
    ...

# ============================================================
# ۱۴. تبدیلات هندسی دیگر
# ============================================================
def getAffineTransform(src: Any, dst: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.getAffineTransform(pts1, pts2)

    📌 پارامترها:
    - src: ۳ نقطه مبدأ
    - dst: ۳ نقطه مقصد

    📌 برمی‌گردونه: ماتریس تبدیل ۲×۳
    """
    ...

def getPerspectiveTransform(src: Any, dst: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.getPerspectiveTransform(pts1, pts2)

    📌 پارامترها:
    - src: ۴ نقطه مبدأ
    - dst: ۴ نقطه مقصد

    📌 برمی‌گردونه: ماتریس تبدیل ۳×۳
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
        📌 فرمول رایج:
        keypoints, descriptor = sift.detectAndCompute(img, None)

        📌 پارامترها:
        - image: تصویر خاکستری (تنها پارامتر اجباری)
        - mask: ناحیه جستجو — None یعنی کل تصویر
        - descriptors: نوشته نمی‌شود — پیش‌فرض None (خودش آرایه جدید می‌سازد)

        📌 برمی‌گردونه:
        - keypoints: لیست اشیاء KeyPoint (شامل pt، size، angle، response، octave)
        - descriptor: آرایه NumPy با شکل (تعداد_نقاط, 128) — نوع float32

        📌 نکته: None که نوشته می‌شود = mask (پارامتر دوم)، نه descriptors
        """
        ...

    def detect(self, image: Any, mask: Any = ...) -> Any:
        """
        📌 فرمول رایج:
        keypoints = sift.detect(img, None)

        📌 پارامترها:
        - image: تصویر خاکستری
        - mask: ناحیه جستجو — None یعنی کل تصویر

        📌 برمی‌گردونه: لیست نقاط کلیدی (KeyPoint)
        📌 کاربرد: فقط تشخیص نقاط، بدون محاسبه توصیف‌گر
        """
        ...

    def compute(self, image: Any, keypoints: Any, descriptors: Any = ...) -> Tuple[Any, Any]:
        """
        📌 فرمول رایج:
        keypoints, descriptors = sift.compute(img, keypoints)

        📌 پارامترها:
        - image: تصویر خاکستری
        - keypoints: لیست نقاط کلیدی
        - descriptors: نوشته نمی‌شود — پیش‌فرض None (خودش آرایه جدید می‌سازد)

        📌 برمی‌گردونه: (keypoints, descriptors)
        📌 کاربرد: فقط محاسبه توصیف‌گر برای نقاط موجود
        """
        ...


# ============================================================
# کلاس KeyPoint
# ============================================================
class KeyPoint:
    pt: Tuple[float, float]    # مختصات نقطه (x, y)
    size: float                # اندازه نقطه
    angle: float               # زاویه نقطه
    response: float            # قدرت پاسخ
    octave: int                # اکتاو
    class_id: int              # شناسه کلاس

def warpPerspective(src: Any, M: Any, dsize: Tuple[int, int]) -> Any:
    """
    📌 فرمول رایج:
    cv2.warpPerspective(img, M, (w, h))

    📌 پارامترها:
    - src: تصویر ورودی
    - M: ماتریس ۳×۳
    - dsize: ابعاد خروجی (width, height)

    📌 برمی‌گردونه: تصویر تبدیل‌شده
    """
    ...

# ============================================================
# ۱۵. عملیات مورفولوژی و هیستوگرام
# ============================================================
def dilate(src: Any, kernel: Any, iterations: int = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.dilate(binary_img, None, iterations=1)

    📌 پارامترها:
    - src: تصویر باینری
    - kernel: کرنل — None یعنی کرنل پیش‌فرض ۳×۳
    - iterations (اختیاری): تعداد تکرار — پیش‌فرض 1

    📌 برمی‌گردونه: تصویر Dilated (نواحی سفید گسترش یافته)
    """
    ...

def erode(src: Any, kernel: Any, iterations: int = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.erode(binary_img, None, iterations=1)

    📌 پارامترها:
    - src: تصویر باینری
    - kernel: کرنل — None یعنی کرنل پیش‌فرض ۳×۳
    - iterations (اختیاری): تعداد تکرار — پیش‌فرض 1

    📌 برمی‌گردونه: تصویر Eroded (نواحی سفید باریک شده)
    """
    ...

def morphologyEx(src: Any, op: int, kernel: Any, iterations: int = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel) — Opening (حذف نویز)
    cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel) — Closing (پر کردن حفره)
    """
    ...

def calcHist(images: Any, channels: Any, mask: Any, histSize: Any, ranges: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.calcHist([img], [0], None, [256], [0, 256])

    📌 پارامترها:
    - images: لیست تصاویر — [img]
    - channels: اندیس کانال — [0] برای خاکستری, [0],[1],[2] برای BGR
    - mask: ماسک — None یعنی کل تصویر
    - histSize: تعداد bins — [256]
    - ranges: بازه مقادیر — [0, 256]

    📌 برمی‌گردونه: آرایه هیستوگرام
    """
    ...

# ============================================================
# ۱۶. عملیات بیتی و ترکیب تصاویر
# ============================================================
def split(m: Any) -> Tuple[Any, Any, Any]:
    """
    📌 فرمول رایج:
    b, g, r = cv2.split(img) — جدا کردن کانال‌های BGR
    """
    ...

def merge(mv: Tuple[Any, Any, Any]) -> Any:
    """
    📌 فرمول رایج:
    cv2.merge([b, g, r]) — ترکیب کانال‌ها
    """
    ...

def bitwise_and(src1: Any, src2: Any, mask: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.bitwise_and(img1, img2, mask=None) — AND بیتی
    """
    ...

def bitwise_or(src1: Any, src2: Any, mask: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.bitwise_or(img1, img2) — OR بیتی
    """
    ...

def bitwise_not(src: Any, mask: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.bitwise_not(img) — NOT بیتی (معکوس)
    """
    ...

def bitwise_xor(src1: Any, src2: Any, mask: Any = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.bitwise_xor(img1, img2) — XOR بیتی
    """
    ...

def addWeighted(src1: Any, alpha: float, src2: Any, beta: float, gamma: float) -> Any:
    """
    📌 فرمول رایج:
    cv2.addWeighted(img1, 0.7, img2, 0.3, 0) — ترکیب دو تصویر با وزن
    """
    ...

def add(src1: Any, src2: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.add(img1, img2) — جمع دو تصویر
    """
    ...

def subtract(src1: Any, src2: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.subtract(img1, img2) — تفریق دو تصویر
    """
    ...

def convertScaleAbs(src: Any, alpha: float = ..., beta: float = ...) -> Any:
    """
    📌 فرمول رایج:
    cv2.convertScaleAbs(img, alpha=1.5, beta=0) — تبدیل مقیاس و قدرمطلق
    """
    ...

def normalize(src: Any, dst: Any, alpha: float, beta: float, norm_type: int) -> Any:
    """
    📌 فرمول رایج:
    cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX) — نرمال‌سازی
    """
    ...

def equalizeHist(src: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.equalizeHist(gray_img) — یکسان‌سازی هیستوگرام
    """
    ...

# ============================================================
# ۱۷. کانتور و اشکال
# ============================================================
def findContours(image: Any, mode: int, method: int) -> Tuple[Any, Any]:
    """
    📌 فرمول رایج:
    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    """
    ...

def drawContours(
    image: Any,
    contours: Any,
    contourIdx: int,
    color: Tuple[int, int, int],
    thickness: int,
) -> Any:
    """
    📌 فرمول رایج:
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
    """
    ...

def boundingRect(contour: Any) -> Tuple[int, int, int, int]:
    """
    📌 فرمول رایج:
    x, y, w, h = cv2.boundingRect(contour) — مستطیل محصورکننده
    """
    ...

def contourArea(contour: Any) -> float:
    """
    📌 فرمول رایج:
    area = cv2.contourArea(contour) — مساحت کانتور
    """
    ...

def arcLength(curve: Any, closed: bool) -> float:
    """
    📌 فرمول رایج:
    perimeter = cv2.arcLength(contour, True) — محیط کانتور
    """
    ...

def approxPolyDP(curve: Any, epsilon: float, closed: bool) -> Any:
    """
    📌 فرمول رایج:
    approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True) — تقریب چندضلعی
    """
    ...

def moments(array: Any) -> dict:
    """
    📌 فرمول رایج:
    M = cv2.moments(contour) — گشتاورهای کانتور
    cx = int(M['m10'] / M['m00'])  # مرکز X
    cy = int(M['m01'] / M['m00'])  # مرکز Y
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
) -> Any:
    """
    📌 فرمول رایج:
    cv2.putText(img, "Hello", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    📌 پارامترها:
    - img: تصویر
    - text: متن
    - org: مختصات شروع (x, y)
    - fontFace: نوع فونت — cv2.FONT_HERSHEY_SIMPLEX
    - fontScale: اندازه فونت
    - color: رنگ (B, G, R)
    - thickness: ضخامت — -1 یعنی توپر
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
    📌 فرمول رایج:
    cv2.rectangle(img, (0, 0), (100, 100), (0, 255, 0), 2) — ضخامت -1 = توپر
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
    📌 فرمول رایج:
    cv2.circle(img, (50, 50), 30, (255, 0, 0), -1) — ضخامت -1 = توپر
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
    📌 فرمول رایج:
    cv2.line(img, (0, 0), (100, 100), (0, 0, 255), 2)
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
    📌 فرمول رایج:
    cv2.arrowedLine(img, (0, 0), (100, 100), (255, 0, 0), 2) — خط با فلش
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
    📌 فرمول رایج:
    cv2.ellipse(img, (100, 100), (50, 30), 45, 0, 360, (0, 255, 0), 2)
    """
    ...

def fillPoly(img: Any, pts: Any, color: Tuple[int, int, int]) -> Any:
    """
    📌 فرمول رایج:
    cv2.fillPoly(img, [pts], (255, 0, 0)) — پر کردن چندضلعی
    """
    ...

def polylines(
    img: Any, pts: Any, isClosed: bool, color: Tuple[int, int, int], thickness: int
) -> Any:
    """
    📌 فرمول رایج:
    cv2.polylines(img, [pts], True, (0, 255, 0), 2) — رسم چندضلعی
    """
    ...

# ============================================================
# ۱۸. متدهای NumPy روی آرایه تصویر (img) — کاربردی در OpenCV
# ============================================================

# این متدها روی آرایه‌های NumPy (از جمله تصاویر OpenCV) کار می‌کنند:
# img.shape      → ابعاد تصویر: (height, width, channels)
# img.dtype      → نوع داده: np.uint8
# img.copy()     → کپی تصویر
# img.astype()   → تبدیل نوع
# img.ravel()    → تبدیل به آرایه ۱ بعدی
# img.flatten()  → مسطح کردن
# img.reshape()  → تغییر شکل

# ============================================================
# ۱۹. توابع کمکی OpenCV
# ============================================================
def getStructuringElement(shape: int, ksize: Tuple[int, int]) -> Any:
    """
    📌 فرمول رایج:
    cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) — ساخت کرنل
    """
    ...

def inRange(src: Any, lowerb: Any, upperb: Any) -> Any:
    """
    📌 فرمول رایج:
    cv2.inRange(hsv, lower_bound, upper_bound) — ماسک رنگی
    """
    ...

def countNonZero(src: Any) -> int:
    """
    📌 فرمول رایج:
    cv2.countNonZero(binary) — شمارش پیکسل‌های غیرصفر
    """
    ...

def minMaxLoc(
    src: Any, mask: Any = ...
) -> Tuple[float, float, Tuple[int, int], Tuple[int, int]]:
    """
    📌 فرمول رایج:
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(img)

    📌 برمی‌گردونه: (کمینه, بیشینه, موقعیت کمینه, موقعیت بیشینه)
    """
    ...

def matchTemplate(image: Any, templ: Any, method: int) -> Any:
    """
    📌 فرمول رایج:
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED) — تطبیق الگو
    """
    ...

def copyMakeBorder(
    src: Any, top: int, bottom: int, left: int, right: int, borderType: int
) -> Any:
    """
    📌 فرمول رایج:
    cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT) — اضافه کردن حاشیه
    """
    ...

# ============================================================
# ۲۰. ثابت‌ها و enumهای OpenCV
# ============================================================

# --- خواندن تصویر ---
IMREAD_COLOR: int
IMREAD_GRAYSCALE: int
IMREAD_UNCHANGED: int
IMREAD_COLOR_RGB: int
IMREAD_REDUCED_COLOR_2: int

# --- تبدیل رنگ ---
COLOR_BGR2GRAY: int
COLOR_BGR2RGB: int
COLOR_GRAY2BGR: int
COLOR_RGB2BGR: int
COLOR_BGR2HSV: int
COLOR_HSV2BGR: int

# --- چرخش ۹۰ درجه ---
ROTATE_90_CLOCKWISE: int
ROTATE_180: int
ROTATE_90_COUNTERCLOCKWISE: int

# --- پنجره ---
WINDOW_NORMAL: int
WINDOW_AUTOSIZE: int
WINDOW_FULLSCREEN: int
WINDOW_FREERATIO: int
WINDOW_KEEPRATIO: int
WND_PROP_VISIBLE: int

# --- Threshold ---
THRESH_BINARY: int
THRESH_BINARY_INV: int
THRESH_TRUNC: int
THRESH_TOZERO: int
THRESH_TOZERO_INV: int
THRESH_OTSU: int
THRESH_TRIANGLE: int

# --- Adaptive Threshold ---
ADAPTIVE_THRESH_MEAN_C: int
ADAPTIVE_THRESH_GAUSSIAN_C: int

# --- Interpolation ---
INTER_LINEAR: int
INTER_AREA: int
INTER_CUBIC: int
INTER_NEAREST: int
INTER_LANCZOS4: int

# --- فونت ---
FONT_HERSHEY_SIMPLEX: int
FONT_HERSHEY_PLAIN: int
FONT_HERSHEY_DUPLEX: int
FONT_HERSHEY_COMPLEX: int
FONT_HERSHEY_TRIPLEX: int
FONT_HERSHEY_COMPLEX_SMALL: int
FONT_HERSHEY_SCRIPT_SIMPLEX: int
FONT_HERSHEY_SCRIPT_COMPLEX: int
FONT_ITALIC: int

# --- خط ---
LINE_AA: int
LINE_4: int
LINE_8: int
FILLED: int

# --- Contour ---
RETR_EXTERNAL: int
RETR_LIST: int
RETR_CCOMP: int
RETR_TREE: int
CHAIN_APPROX_NONE: int
CHAIN_APPROX_SIMPLE: int
CHAIN_APPROX_TC89_L1: int
CHAIN_APPROX_TC89_KCOS: int

# --- Morphology ---
MORPH_RECT: int
MORPH_CROSS: int
MORPH_ELLIPSE: int
MORPH_OPEN: int
MORPH_CLOSE: int
MORPH_GRADIENT: int
MORPH_TOPHAT: int
MORPH_BLACKHAT: int

# --- Norm ---
NORM_MINMAX: int
NORM_L1: int
NORM_L2: int
NORM_INF: int

# --- Border ---
BORDER_CONSTANT: int
BORDER_REFLECT: int
BORDER_REPLICATE: int
BORDER_WRAP: int

# --- Template Matching ---
TM_SQDIFF: int
TM_SQDIFF_NORMED: int
TM_CCORR: int
TM_CCORR_NORMED: int
TM_CCOEFF: int
TM_CCOEFF_NORMED: int
