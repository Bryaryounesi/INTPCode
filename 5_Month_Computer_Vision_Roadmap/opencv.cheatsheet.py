'''
# ============================================================
# 📖 OpenCV CheatSheet — فرمول‌محور و موضوعی
# ============================================================
این چیت‌شیت شامل تمام مباحث پردازش تصویر با OpenCV است:
خواندن و ذخیره تصویر، تغییرات هندسی، فیلترها، آستانه‌گذاری،
لبه و کانتور، مورفولوژی، بهبود کنتراست، و ابزارهای کمکی.

import cv2
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from itertools import product, combinations, permutations, chain

p = print

# ============================================================
# ۱. خواندن، تبدیل رنگ و ذخیره تصویر
# ============================================================

خواندن تصویر:
img = cv2.imread(path)                                      # رنگی BGR (پیش‌فرض)
img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)           # خاکستری
img_unchanged = cv2.imread(path, cv2.IMREAD_UNCHANGED)      # با کانال آلفا

فلگ‌های پرکاربرد:
cv2.IMREAD_COLOR           → رنگی BGR (پیش‌فرض)
cv2.IMREAD_COLOR_RGB       → رنگی RGB
cv2.IMREAD_GRAYSCALE       → خاکستری
cv2.IMREAD_UNCHANGED       → با آلفا
cv2.IMREAD_REDUCED_COLOR_2 → نصف ابعاد

بررسی خطا (ضروری برای پردازش دسته‌ای):
if img is None:
    print("خطا در خواندن تصویر")
    continue

تبدیل رنگ:
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # برای نمایش با Matplotlib
bgr_from_gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

کدهای پرکاربرد:
cv2.COLOR_BGR2GRAY   → رنگی به خاکستری
cv2.COLOR_BGR2RGB    → BGR به RGB (برای Matplotlib)
cv2.COLOR_GRAY2BGR   → خاکستری به رنگی (۳ کاناله)

چه زمانی با فلگ متفاوت بخوانیم و کی cvtColor کنیم؟
فایل محلی روی SSD سریع → خواندن با فلگ متفاوت (حذف سربار CPU)
Raspberry Pi / SD Card کند → یک بار خواندن + cvtColor
استریم دوربین / ویدئو → cvtColor اجباری (فقط یک فریم داریم)
تصویر از قبل در حافظه → cvtColor اجباری (imread معنی ندارد)
فایل روی شبکه (NAS/Cloud) → یک بار خواندن + cvtColor
پردازش بلادرنگ → یک بار خواندن + cvtColor
پردازش دسته‌ای روی SSD → خواندن با فلگ متفاوت

ذخیره تصویر:
cv2.imwrite("output.jpg", img)
cv2.imwrite(str(output_dir / f"name_{suffix}.jpg"), img)

ساخت مسیر خروجی امن با pathlib:
output = Path(r"E:\\...\\Output")
output.mkdir(parents=True, exist_ok=True)
cv2.imwrite(str(output / f"resized_{name}.jpg"), resized)

قانون ذخیره‌سازی:
فقط عکس خام (بدون نمودار/تیتر) → cv2.imwrite()
هر چیزی که نمودار، هیستوگرام، یا چند subplot دارد → plt.savefig()
کلاژ عکس برای پردازش مجدد → np.hstack/np.vstack + cv2.imwrite()

# ============================================================
# ۲. تغییرات هندسی
# ============================================================

تغییر اندازه با ابعاد دقیق:
resized = cv2.resize(img, (width, height))

تغییر اندازه با ضرایب مقیاس:
resized = cv2.resize(img, dsize=None, fx=0.6, fy=0.6)

روش‌های درون‌یابی:
cv2.INTER_AREA    → بهترین برای کوچک‌سازی (پیشنهادی)
cv2.INTER_LINEAR  → پیش‌فرض
cv2.INTER_CUBIC   → بهترین برای بزرگ‌نمایی
cv2.INTER_NEAREST → سریع (برای ماسک و باینری)

تغییر اندازه با حفظ نسبت:
h, w = img.shape[:2]
new_w = 400
new_h = int((h * new_w) / w)
resized = cv2.resize(img, (new_w, new_h))

برش (ROI):
roi = img[y1:y2, x1:x2]              # برش مستطیلی
roi = img[50:250, :]                 # فقط برش عمودی
roi = img[:, 100:350]                # فقط برش افقی

برش ۵۰٪ مرکزی (مناسب برای پردازش دسته‌ای):
h, w = img.shape[:2]
roi = img[h//4 : 3*h//4, w//4 : 3*w//4]

نکته برای یافتن مختصات: تصویر را در Paint ویندوز باز کنید و مختصات پیکسلی موس را بخوانید.

چرخش‌های ۹۰ درجه (ساده):
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated = cv2.rotate(img, cv2.ROTATE_180)
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

چرخش با زاویه دلخواه (۴ مرحله):

مرحله ۱: ساخت ماتریس چرخش
h, w = img.shape[:2]
center = (w // 2, h // 2)
angle = 30        # مثبت → پادساعتگرد
scale = 1.0
M = cv2.getRotationMatrix2D(center, angle, scale)

ساختار ماتریس M (همیشه ۲×۳):
[ cosθ   sinθ   tx ]
[ -sinθ  cosθ   ty ]
tx, ty: مولفه‌های انتقال

مرحله ۲: محاسبه ابعاد جدید (جلوگیری از بریدگی گوشه‌ها)
theta = np.radians(angle)
new_w = int(h * np.sin(theta) + w * np.cos(theta))
new_h = int(h * np.cos(theta) + w * np.sin(theta))

مرحله ۳: اصلاح مرکز ماتریس
M[0, 2] += (new_w - w) // 2
M[1, 2] += (new_h - h) // 2

مرحله ۴: اعمال چرخش
rotated = cv2.warpAffine(img, M, (new_w, new_h))

وارونه‌سازی:
flip_vertical = cv2.flip(img, 0)      # عمودی (دور محور x)
flip_horizontal = cv2.flip(img, 1)    # افقی - آینه‌ای (دور محور y)
flip_both = cv2.flip(img, -1)         # هر دو (معادل چرخش ۱۸۰°)

ماتریس‌های تبدیل:

انتقال:
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, M, (w, h))

تغییر مقیاس:
resized = cv2.resize(img, None, fx=sx, fy=sy)

برش (Shear):
M = np.float32([[1, k, 0], [0, 1, 0]])
sheared = cv2.warpAffine(img, M, (w, h))

آفین:
M = cv2.getAffineTransform(pts1, pts2)
warped = cv2.warpAffine(img, M, (w, h))

پرسپکتیو:
M = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(img, M, (w, h))


# ============================================================
# ۳. قاعده ابعاد در OpenCV
# ============================================================

img[row, col] → img[y, x]
size = (width, height) → (x, y)

هر جا size می‌دهیم → اول = عرض (width)
  cv2.resize(img, (width, height))
  cv2.warpAffine(img, M, (width, height))

هر جا از img.shape می‌گیریم → اول = ارتفاع (height)
  img.shape → (height, width, channels)
  h, w = img.shape[:2]


# ============================================================
# ۴. نمایش تصویر
# ============================================================

نمایش با OpenCV:
cv2.imshow("window_name", img)
cv2.waitKey(0)               # صبر تا زدن کلید
cv2.waitKey(2000)            # نمایش ۲ ثانیه
cv2.destroyAllWindows()      # بستن همه پنجره‌ها

تنظیم اندازه پنجره برای رفع زوم‌شدگی:
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", width, height)

نمایش با Matplotlib:

نمایش یک تصویر:
plt.figure(figsize=(8, 6))
plt.imshow(rgb, cmap="gray")     # برای خاکستری cmap="gray"
plt.title("Title")
plt.axis("off")
plt.show()

نمایش چند تصویر کنار هم (Subplot):
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(img1, cmap="gray")
axes[0].set_title("Title 1")
axes[0].axis("off")
axes[1].imshow(img2, cmap="gray")
axes[1].set_title("Title 2")
axes[1].axis("off")
axes[2].imshow(img3, cmap="gray")
axes[2].set_title("Title 3")
axes[2].axis("off")
plt.tight_layout()
plt.show()

ذخیره با Matplotlib (برای نمودار و گزارش):
fig.savefig("output.png", dpi=300, bbox_inches="tight")

مقایسه افقی با OpenCV (سریع برای کلاژ):
comparison = np.hstack([img1, img2, img3])
cv2.imshow("Comparison", comparison)

مقایسه عمودی:
comparison_v = np.vstack([img1, img2])

نکته: برای hstack همه تصاویر باید هم ارتفاع باشند
برای vstack همه تصاویر باید هم عرض باشند
اگر نبودند، اول resize کنید.


# ============================================================
# ۵. فیلترها و کاهش نویز
# ============================================================

Gaussian Blur (کاهش نویز نرم):
blurred = cv2.GaussianBlur(img, (5, 5), 0)

پارامترها:
img: تصویر ورودی (رنگی یا خاکستری)
ksize: اندازه کرنل — تاپل (width, height) — هر دو باید فرد باشند
       والیوهای رایج: (3,3) کم | (5,5) متوسط | (9,9) زیاد
sigmaX: انحراف معیار افقی. اگر 0 بدهید، OpenCV خودش حساب می‌کند (پیشنهادی)
sigmaY: پیش‌فرض 0 یعنی برابر با sigmaX

حالت اول (پیشنهادی): ksize دارید, sigmaX=0
حالت دوم: ksize=(0,0) می‌دهید, sigmaX را دستی تعیین می‌کنید

Median Blur (حذف نویز نمک-فلفل):
median = cv2.medianBlur(img, 5)

پارامترها:
img: تصویر ورودی (رنگی یا خاکستری)
ksize: اندازه کرنل — یک عدد فرد (نه تاپل! برخلاف Gaussian)
       والیوهای رایج: 3 (کم) | 5 (متوسط، پیشنهادی) | 9 (زیاد)

مقایسه Gaussian و Median:
Gaussian = میانگین وزن‌دار پیکسل‌های همسایه → نویز پخش می‌شود → لبه‌ها محو
Median   = میانه آماری پیکسل‌های همسایه → نویز حذف می‌شود → لبه‌ها تیز
Median برای نویز نمک-فلفل بهترین است.


# ============================================================
# ۶. آستانه‌گذاری (Thresholding)
# ============================================================

Threshold ساده (آستانه‌گذاری سراسری):
ret, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

پارامترها:
gray: تصویر ورودی — باید Grayscale باشد (تک کاناله)
thresh: عدد آستانه (0 تا 255)
        والیوهای رایج: 50 (روشن) | 127 (متوسط، رایج‌ترین) | 200 (تیره)
        ترش کم = تصویر سفیدتر | ترش زیاد = تصویر سیاه‌تر
maxval: مقدار پیکسل‌های عبورکرده از آستانه — معمولاً 255

type: نوع آستانه‌گذاری
      cv2.THRESH_BINARY      → بالای آستانه = maxval, پایین = 0
      cv2.THRESH_BINARY_INV  → معکوس حالت بالا
      cv2.THRESH_TRUNC       → بالای آستانه = خود آستانه, پایین = بدون تغییر
      cv2.THRESH_TOZERO      → بالای آستانه = بدون تغییر, پایین = 0

خروجی:
ret → همان مقدار thresh استفاده‌شده
th  → تصویر باینری شده

نکته: تابع threshold یک تاپل برمی‌گرداند پس باید دو متغیر را مقداردهی کنید.

Otsu Threshold (آستانه‌گذاری خودکار):
blur = cv2.GaussianBlur(gray, (5, 5), 0)     # بلور قبل از اوتسو لازم است
ret, thresh_otsu = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

مناسب برای:
تصاویر با کنتراست بالا
تصاویر دوقله‌ای (هیستوگرام دو قله دارد)
نورپردازی نسبتاً یکنواخت
پس زمینه غیر شلوغ

Adaptive Threshold (آستانه‌گذاری تطبیقی):
adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 3)

پارامترها (هر ۶ پارامتر اجباری هستند):
gray: تصویر ورودی — باید Grayscale باشد
maxValue: مقدار پیکسل‌های سفید — معمولاً 255
adaptiveMethod:
    cv2.ADAPTIVE_THRESH_MEAN_C     → میانگین ساده همسایه‌ها
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C → میانگین وزن‌دار (بهتر، پیشنهادی)
thresholdType: معمولاً cv2.THRESH_BINARY
blockSize: اندازه ناحیه بررسی — یک عدد فرد
           والیوهای رایج: 11 (جزئیات بیشتر) | 21 (نرم‌تر، پیشنهادی برای متون)
C: ثابت تصحیح — از میانگین محلی کم می‌شود
   والیوهای رایج: 2 (پیش‌فرض) | 3 (معمولی) | 7 (خطوط پیوسته‌تر)
   بزرگتر = تصویر تیره‌تر و خطوط پیوسته‌تر

نکته — رفتار شبه‌کنی:
هرچه C بزرگتر ← پیوستگی خطوط بیشتر
هرچه blockSize کوچکتر ← خطوط باریکتر
در برخی تصاویر: adaptiveThreshold با C بالا و blockSize پایین
عملکردی مشابه Canny پیدا می‌کند

نکته — C منفی (راه‌حل تله تُنال برای شیء طرح‌دار با پس‌زمینه سفید):
C را منفی بگیر: ۲- تا ۱۵- (آزمون و خطا کن)
این کار آستانه را بالا می‌برد و مرزهای محوی که همرنگ پس‌زمینه می‌زدند را سفید می‌کند
پارگی لبه بسته می‌شود
blockSize را بالا ببر: ۲۱ به بالا (فقط اعداد فرد)
پنجره بزرگ، جزئیات ریز و طرح‌های داخلی را نادیده می‌گیرد و فقط ساختار کلی شیء را می‌بیند
نتیجه: مرز بیرونی بسته و یکپارچه، داخل شلوغ (پر از سوراخ و طرح)

معکوس‌سازی تصویر باینری:
روش ۱: هنگام threshold
_, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

روش ۲: روی باینری آماده
inverted = cv2.bitwise_not(th)

نکته مهم: عملیات مورفولوژی (Erosion, Dilation) فرض می‌کنند
شیء سفید و پس‌زمینه سیاه است. اگر برعکس است، از THRESH_BINARY_INV استفاده کن.

راه‌حل تله تُنال (نشت پس‌زمینه به درون اشیاء بافت‌دار):
مشکل: تصاویر با پس‌زمینه سفید ولی شیء بافت‌دار → احتمال تله تُنال

راه‌حل دستی:
بالا بردن آستانه در threshold ساده تا کل شی سیاه شود
منفی کردن پارامتر C در adaptive تا کل پس‌زمینه سیاه شود

راه‌حل خودکار (پردازش دسته‌ای):
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
_, binary = cv2.threshold(tophat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
binary = cv2.morphologyEx(binary, cv2.MORPH_CLOSE,
                          cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (25, 25)))
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# ============================================================
# ۷. تشخیص لبه (Canny Edge Detection)
# ============================================================

edges = cv2.Canny(img, threshold1, threshold2)

پارامترها:
img: تصویر ورودی — ترجیحاً Grayscale
threshold1: حد پایین (minVal) — برای هیسترزیس
threshold2: حد بالا (maxVal) — برای هیسترزیس
            نسبت پیشنهادی: 1:2 یا 1:3
            مقادیر تجربی خوب: (50,150) | (80,200) | (80,240)

منطق هیسترزیس Canny:
اگر گرادیان > threshold2 → قطعاً لبه
اگر گرادیان < threshold1 → قطعاً غیرلبه
اگر بین این دو → لبه است فقط اگر به لبه قطعی متصل باشد

قانون طلایی: همیشه قبل از Canny بلور کن!
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)


# ============================================================
# ۸. کانتور (Contour)
# ============================================================

پیدا کردن کانتور:
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

پارامترها:
binary: تصویر باینری ورودی (خروجی Threshold)
mode: نحوه بازیابی کانتورها
    cv2.RETR_EXTERNAL → فقط کانتورهای بیرونی (پرکاربردترین)
    cv2.RETR_LIST     → همه کانتورها بدون سلسله‌مراتب
    cv2.RETR_TREE     → همه کانتورها با روابط تو در تو
    cv2.RETR_CCOMP    → همه کانتورها با سلسله‌مراتب دو سطحی

method: نحوه ذخیره نقاط
    cv2.CHAIN_APPROX_SIMPLE → فقط نقاط ضروری (پرکاربردترین)
    cv2.CHAIN_APPROX_NONE   → تمام نقاط مرزی

خروجی:
contours: لیستی از آرایه‌های نامپی
hierarchy: آرایه نامپی که روابط تو در تو را نشان می‌دهد

رسم کانتور:
output = img.copy()     # حتماً کپی بگیر! نه output = img
cv2.drawContours(output, contours, -1, (0, 255, 0), 3)

پارامترها:
output: تصویری که کانتور روی آن رسم می‌شود (باید رنگی/BGR باشد)
contours: خروجی findContours
contourIdx: اندیس کانتور | -1 یعنی همه کانتورها
color: رنگ خط به‌صورت (B, G, R) | (0, 255, 0) سبز
thickness: ضخامت خط | 2 یا 3 رایج

نکته مهم: این تابع None برمی‌گرداند! مستقیماً روی تصویر تغییر ایجاد می‌کند.
قبل از استفاده حتماً img.copy() بگیر.

مساحت و محیط:
area = cv2.contourArea(contour)                  # مساحت داخل کانتور
perimeter = cv2.arcLength(contour, closed=True)  # محیط کانتور

مساحت همه کانتورها:
areas = [cv2.contourArea(c) for c in contours]

انتخاب بزرگ‌ترین کانتور:
biggest = max(contours, key=cv2.contourArea)

مرتب‌سازی بر حسب مساحت (بزرگ به کوچک):
sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

انتخاب ۱۵ کانتور بزرگ:
greatest = sorted(contours, key=cv2.contourArea, reverse=True)[:15]

Bounding Box (رسم کادر دور شیء):
x, y, w, h = cv2.boundingRect(biggest)
boxes = img.copy()
cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 10)

ROI از Bounding Box:
roi = img[y : y + h, x : x + w]

Mask (جداسازی دقیق شکل شیء):
mask = np.zeros(gray.shape, dtype=np.uint8)    # یا np.zeros_like(gray)
cv2.drawContours(mask, [biggest], -1, 255, -1)
masked = cv2.bitwise_and(img, img, mask=mask)

پارامترها:
gray.shape: ابعاد تصویر خاکستری (تک کاناله)
[biggest]: لیست یک عنصری از کانتور (حتماً لیست باشد)
255: مقدار سفید برای داخل کانتور
-1: ضخامت -1 یعنی پر کردن کامل داخل کانتور

نکته: ماسک را حتماً تک‌کاناله (dtype=np.uint8) بساز.

ترکیب bitwise_and:
masked = cv2.bitwise_and(thresh_adapt, dilated, mask=mask)

نکته: عملیات AND جابجایی‌پذیر است → ترتیب تصاویر مهم نیست
پیکسل فقط وقتی سفید می‌ماند که در هر دو تصویر سفید باشد.

قوانین طلایی کانتور:
۱. همیشه قبل از drawContours یک img.copy() بگیر
۲. ماسک حتماً تک‌کاناله (dtype=np.uint8) باشد
۳. کانتور روی باینری (Threshold) زده می‌شود، نه روی Canny
۴. RETR_EXTERNAL برای استخراج مرز بیرونی از تصویر باینری شلوغ


# ============================================================
# ۹. مورفولوژی (Morphology)
# ============================================================

مفهوم Structuring Element (کرنل، عنصر ساختاری):
کرنل یک ماتریس کوچک (مثلاً 3×3 یا 5×5) با شکل مشخص است که روی تمام پیکسل‌های
تصویر باینری حرکت می‌کند (Sliding Window). زیر هر پیکسل محاسبه ریاضی انجام می‌دهد
و پیکسل‌ها را حذف یا اضافه می‌کند.
محتوای کرنل فقط ۰ و ۱ دارد (برخلاف کرنل بلور که مقادیر اعشاری دارد).

ساخت کرنل:
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

پارامترها:
shape: نوع شکل عنصر ساختاری
    cv2.MORPH_RECT     → مستطیل/مربع (همه مقادیر ۱)
                         برای اشیاء با خطوط و لبه‌های صاف
    cv2.MORPH_ELLIPSE  → بیضی/دایره‌ای
                         برای اشیاء گرد و ارگانیک (سکه، سلول)
                         برای اشیاء نامنظم یا چرخیده (برگ، لکه، سنگ)
                         انتخاب پیش‌فرض و امن
    cv2.MORPH_CROSS    → ضربدر (+)

ksize: سایز کرنل به‌صورت تاپل (عرض، ارتفاع) مثل (5, 5)
       اجباری است — مقدار پیش‌فرض ندارد
       هرچه بزرگ‌تر → تأثیر عملیات قوی‌تر
       همیشه عدد فرد (3، 5، 7، ...)
       باید نسبت به اندازه نویز تنظیم شود، نه اندازه کل تصویر

anchor: نقطه لنگر (مرکز) کرنل
        پیش‌فرض (-1, -1) یعنی مرکز خودکار
        تقریباً همیشه از پیش‌فرض استفاده می‌شود

خروجی: آرایه نامپی uint8 با شکل ksize که فقط شامل ۰ و ۱ است

نکات کلیدی کرنل:
shape قرار نیست شبیه شکل شیء داخل تصویر باشد!
کرنل فقط روش پیمایش و تصمیم‌گیری است، نه قالبی برای مطابقت با شکل شیء.
کرنل خودش هیچ‌وقت نمی‌چرخد پس برای اشیاء چرخیده از ELLIPSE استفاده کن.
MORPH_RECT عملاً همان np.ones است ولی استفاده از تابع رسمی OpenCV
باعث سازگاری بهتر با بقیه توابع مورفولوژی می‌شود.
میانبر np.ones فقط برای RECT جواب می‌دهد، برای ELLIPSE و CROSS
چاره‌ای جز استفاده از getStructuringElement نداری.
انتخاب shape و ksize فرآیندی تجربی (آزمون و خطا) است، نه فرمول ثابت.
# -------------------------------------------------------------------------
Erosion (فرسایش):
eroded = cv2.erode(binary/gray, kernel, 1/2/3)

پارامترها:
src: تصویر ورودی — باینری یا گری‌اسکیل (شیء سفید، پس‌زمینه سیاه)
kernel: ماتریس کرنل ساخته شده با getStructuringElement
iterations: تعداد دفعات تکرار عملیات
            پیش‌فرض: 1 | رایج: 1 تا 3
            بیشتر = فرسایش شدیدتر

ایده ساده: کرنل روی تصویر حرکت می‌کند و چک می‌کند آیا تمام پیکسل‌های زیر
کرنل سفید (۱) هستند یا نه. اگر حتی یک پیکسل سیاه (۰) باشد، پیکسل مرکزی
هم سیاه می‌شود. نتیجه: لبه‌های اشیاء سفید کوچک می‌شوند.

کاربرد:
حذف نویزهای ریز سفید (نقطه‌های کوچک اضافی)
نازک کردن اشیاء
جدا کردن دو شیء که به هم چسبیده‌اند
# --------------------------------------------------------------------------
Dilation (گسترش):
dilated = cv2.dilate(binary/gray, kernel, 1/2/3)

پارامترها: مشابه erode

ایده ساده: کرنل روی تصویر حرکت می‌کند و چک می‌کند آیا حداقل یکی از پیکسل‌های
زیر کرنل سفید (۱) هست یا نه. اگر حتی یک پیکسل سفید باشد، پیکسل مرکزی هم
سفید می‌شود. نتیجه: لبه‌های اشیاء سفید بزرگ می‌شوند.

کاربرد:
پر کردن سوراخ‌های کوچک داخل شیء
وصل کردن قطعاتی از شیء که به‌خاطر نویز از هم جدا شده‌اند
بزرگ کردن ناحیه یک شیء بعد از Erosion
# ----------------------------------------------------------------------------
Opening:
opened = cv2.morphologyEx(binary/gray, cv2.MORPH_OPEN, kernel)

تعریف: Erosion سپس Dilation

چرا این ترتیب؟ ابتدا Erosion نویزهای ریز سفید را پاک می‌کند (چون کوچک‌تر
از کرنل هستند و کامل حذف می‌شوند)، سپس Dilation شیء اصلی را به اندازه اولیه
برمی‌گرداند بدون اینکه نویز حذف‌شده برگردد.

کاربرد: پاک‌سازی نویزهای ریز سفید بدون کوچک شدن دائمی شیء اصلی
# ------------------------------------------------------------------------
Closing:
closed = cv2.morphologyEx(binary/gray, cv2.MORPH_CLOSE, kernel)

تعریف: Dilation سپس Erosion

چرا این ترتیب؟ ابتدا Dilation سوراخ‌های کوچک داخل شیء را پر می‌کند یا قطعات
نزدیک را وصل می‌کند، سپس Erosion شیء را به اندازه اولیه برمی‌گرداند بدون اینکه
سوراخ‌ها دوباره باز شوند.

کاربرد: پر کردن سوراخ‌های کوچک یا وصل کردن قطعات جدا از هم بدون بزرگ شدن دائمی

Top Hat:
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)

کاربرد: حذف بافت‌های سطحی و جدا کردن شی از زمینه سفید

خلاصه تأثیرات:
Erosion: اشیاء سفید باریک‌تر و کوچک‌تر می‌شوند
         نقاط ریز سفید (نویز) کاملاً حذف می‌شوند
         با افزایش iteration، اشیاء کوچک کاملاً ناپدید می‌شوند

Dilation: اشیاء سفید ضخیم‌تر و بزرگ‌تر می‌شوند
          حفره‌های سیاه داخل اشیاء پر می‌شوند
          اشیاء نزدیک به هم به یکدیگر می‌چسبند

تأثیر Kernel Size:
کرنل بزرگتر = تغییرات سریع‌تر و شدیدتر
کرنل 7x7 با 3 iteration تقریباً ساختار اصلی را از بین می‌برد

تأثیر شکل کرنل:
RECT: تغییرات یکنواخت در همه جهات
CROSS: تغییرات بیشتر در جهت‌های عمودی و افقی
ELLIPSE: تغییرات نرم‌تر و طبیعی‌تر

چه زمانی تکی و چه زمانی ترکیبی؟
فقط کوچیک کردن شیء (جدا کردن دو شیء چسبیده) → Erosion تنها
فقط بزرگ کردن شیء (پررنگ‌تر کردن ناحیه نازک) → Dilation تنها
حذف نویز بدون تغییر اندازه شیء → Opening
پر کردن سوراخ بدون تغییر اندازه شیء → Closing
# ----------------------------------------------------------
بهترین روش مورفولوژی (پایپلاین کامل):

مرحله ۱: پیش‌پردازش
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh_adapt = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY_INV, 21, 3)

مرحله ۲: Opening خفیف برای حذف نویز ریز
kernel_soft = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
opened = cv2.morphologyEx(thresh_adapt, cv2.MORPH_OPEN, kernel_soft)

مرحله ۳: Dilate تهاجمی برای ترمیم حاشیه و بستن سوراخ‌ها
kernel_aggressive = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
dilated = cv2.dilate(opened, kernel_aggressive)

مرحله ۴: یافتن کانتور اصلی از تصویر بهبود یافته
contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
biggest = max(contours, key=cv2.contourArea)

مرحله ۵: ساخت ماسک
mask = np.zeros_like(thresh_adapt)
cv2.drawContours(mask, [biggest], -1, 255, -1)

مرحله ۶: اعمال ماسک — ترکیب هوشمندانه
masked = cv2.bitwise_and(thresh_adapt, dilated, mask=mask)

مزیت: نویز بیرون از کانتور کاملاً حذف می‌شود
نویز داخل شی با AND حذف می‌شود
الگوهای واقعی داخل شی حفظ می‌شوند
حاشیه ترمیم شده و سوراخ‌ها بسته شده‌اند


# ============================================================
# ۱۰. بهبود کنتراست
# ============================================================

مفهوم Histogram:
هیستوگرام تصویر یعنی نمودار توزیع فرکانس مقادیر روشنایی پیکسل‌ها از ۰ تا ۲۵۵.
محور افقی: مقدار روشنایی
محور عمودی: تعداد پیکسل‌ها

Histogram Equalization (یکسان‌سازی سراسری):
equalized = cv2.equalizeHist(gray)

پارامترها:
gray: تصویر ورودی — حتماً Grayscale و uint8
      این تابع روی تصویر رنگی (BGR سه‌کاناله) مستقیماً کار نمی‌کند

خروجی: تصویر جدید با همان ابعاد و نوع

مفهوم: گسترش دادن توزیع روشنایی به‌طوری که مقادیر در کل بازه ۰ تا ۲۵۵ پخش شوند
نه اینکه فقط در یک بازه باریک (مثلاً ۱۰۰ تا ۱۵۰) متمرکز باشند.

کاربردها:
تصاویر پزشکی (X-ray, MRI, CT scan) — جزئیات مخفی نمایان می‌شوند
پیش‌پردازش برای الگوریتم‌های بینایی ماشین (تشخیص لبه، OCR، تشخیص چهره)
تصاویر ماهواره‌ای و هوایی
تصاویر علمی و تحقیقاتی (میکروسکوپی، نجومی)

نامناسب برای:
عکس‌های طبیعی و هنری (پرتره، منظره)
تصاویری که قرار است انسان ببیند و لذت ببرد
هرجا که «زیبایی» مهم است، نه «استخراج اطلاعات»
تصاویر با پس‌زمینه سفید (بخشی از پس‌زمینه را خراب می‌کند)

CLAHE (Contrast Limited Adaptive Histogram Equalization):
clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
clahe_img = clahe.apply(gray)

پارامترها:
clipLimit: سقف محدودسازی کنتراست
           پیش‌فرض: 40 (خیلی زیاد است!)
           مقدار رایج: 2 تا 4
           بزرگ‌تر = کنتراست بیشتر ولی نویز بیشتر

tileGridSize: اندازه گرید بلوک‌بندی تصویر
              پیش‌فرض: (8, 8) = ۶۴ بلوک
              مقدار رایج: (8, 8)

خروجی: این تابع یک شیء CLAHE برمی‌گرداند (نه تصویر)
سپس باید متد apply() صدا زده شود.

تفاوت equalizeHist و CLAHE:
equalizeHist → سراسری (Global) | یک بار روی کل تصویر
CLAHE → موضعی (Local) | تصویر به بلوک‌های کوچک تقسیم، هر بلوک جدا equalize،
        نرم‌سازی بین بلوک‌ها

چه زمانی CLAHE؟
نور نامتقارن (بخشی روشن، بخشی تاریک)
عکس‌های طبیعی که هم زیبایی مهم است و هم استخراج جزئیات
تصاویر با نویز در نواحی یکنواخت (clipLimit از تشدید نویز جلوگیری می‌کند)

نمایش هیستوگرام:

هیستوگرام تصویر خاکستری:
plt.hist(gray.ravel(), bins=256, range=[0, 256], color="black")
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()

هیستوگرام کانال‌های رنگی جداگانه:
colors = ("b", "g", "r")
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=f"Channel {col.upper()}")
plt.legend()
plt.show()

مقایسه تصویر + هیستوگرام (۲×۲):
fig, axes = plt.subplots(2, 2, constrained_layout=True)
axes[0, 0].imshow(gray, cmap="gray")
axes[0, 0].set_title("Original")
axes[0, 1].hist(gray.ravel(), bins=256, range=(0, 255))
axes[0, 1].set_title("Original Histogram")
axes[1, 0].imshow(equalized, cmap="gray")
axes[1, 0].set_title("Equalized")
axes[1, 1].hist(equalized.ravel(), bins=256, range=(0, 255))
axes[1, 1].set_title("Equalized Histogram")
plt.show()

مقایسه سه حالته (Original vs Global vs CLAHE):
fig, axes = plt.subplots(1, 3, constrained_layout=True)
axes[0].imshow(gray, cmap="gray")
axes[0].set_title("Original")
axes[1].imshow(equalized, cmap="gray")
axes[1].set_title("Global Equalize")
axes[2].imshow(clahe_img, cmap="gray")
axes[2].set_title("CLAHE")
plt.show()


# ============================================================
# ۱۱. نمایش پروفایل شدت نور و Heatmap
# ============================================================

Line Profile (پروفایل شدت نور روی یک خط):
line_y = gray.shape[0] // 2
intensity_profile = gray[line_y, :]

plt.plot(intensity_profile, color="blue", linewidth=0.8)
plt.title(f"Intensity Profile at y = {line_y}")
plt.xlabel("X Position")
plt.ylabel("Intensity")
plt.show()

Heatmap (نمایش ماتریس اعداد):
feature_map = cv2.resize(gray, (50, 50))

plt.imshow(feature_map, cmap="hot", interpolation="nearest")
plt.colorbar(label="Intensity")
plt.title("Feature Map / Heatmap")
plt.axis("off")
plt.show()


# ============================================================
# ۱۲. itertools برای تست پارامترها
# ============================================================

ایمپورت:
from itertools import product, permutations, combinations, chain

product — ضرب دکارتی (مهم‌ترین تابع برای CV):
جایگزین حلقه‌های تودرتو

مثال پایه با ۲ لیست:
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
for color, size in product(colors, sizes):
    print(color, size)

مثال با ۳ لیست:
for j, k, d in product(list1, list2, list3):
    print(j, k, d)

با پارامتر repeat:
for combo in product([1, 2], repeat=3):
    print(combo)

با لیست‌های پویا:
lists = [[1, 2], ['a', 'b'], [True, False]]
for combo in product(*lists):     # * یعنی باز کردن لیست
    print(combo)

مثال کاربردی در پردازش تصویر:
thresholds = [100, 150, 200]
kernel_sizes = [3, 5, 7]
shapes = [cv2.MORPH_RECT, cv2.MORPH_ELLIPSE, cv2.MORPH_CROSS]
iterations = [1, 2, 3]

for thresh, ksize, shape, itr in product(thresholds, kernel_sizes, shapes, iterations):
    kernel = cv2.getStructuringElement(shape, (ksize, ksize))
    _, binary = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)
    result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=itr)

permutations — جایگشت (ترتیب مهم است):
for perm in permutations(['A', 'B', 'C'], 2):
    print(perm)
خروجی: ('A','B') ('A','C') ('B','A') ('B','C') ('C','A') ('C','B')

combinations — ترکیب (ترتیب مهم نیست):
for comb in combinations(['A', 'B', 'C'], 2):
    print(comb)
خروجی: ('A','B') ('A','C') ('B','C')

chain — اتصال چند لیست:
for item in chain(list1, list2, list3):
    print(item)

نکات itertools:
کتابخانه استاندارد است — نیازی به نصب ندارد
توابع lazy هستند — مقادیر را یکی‌یکی تولید می‌کنند (حافظه کارآمد)
خروجی iterator است — برای لیست از list() استفاده کن
product با بیش از ۲ لیست کار می‌کند

چه زمانی product و چه زمانی لوپ تودرتو؟
از product استفاده کن وقتی:
فقط ترکیب ساده می‌خواهی
تعداد لیست‌ها زیاد است (بیش از ۳)
کد خواناتر می‌خواهی
تعداد لیست‌ها پویا است

از لوپ تودرتو استفاده کن وقتی:
تعداد لیست‌ها کم است (۲ یا ۳)
منطق پیچیده بین لوپ‌ها داری
در هر سطح پردازش خاصی انجام می‌دهی


# ============================================================
# ۱۳. pathlib برای مدیریت مسیرها
# ============================================================

import cv2
from pathlib import Path

برای یک تصویر تکی:
path = r"E:\\...\\Data\\input\\cow.jpg"
image = cv2.imread(path)

برای تصاویر زیاد:
folder = Path(r"E:\\...\\Data\\input")
output = Path(r"E:\\...\\Output")
output.mkdir(parents=True, exist_ok=True)    # ساخت پوشه اگر نبود

paths = [str(i) for i in folder.glob("*.jpg")]

for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    name = Path(i).stem      # نام فایل بدون پسوند
    # پردازش...
    cv2.imwrite(str(output / f"processed_{name}.jpg"), img)

معادل بدون pathlib:
name = i.split("\\\\")[-1].split(".")[0]


# ============================================================
# ۱۴. الگوی حلقه دوم (Nested Loop) و نام‌گذاری خروجی
# ============================================================

علامت نیاز به حلقه دوم:
وقتی برای یک ورودی، عملیات مشابه را با پارامترهای مختلف تکرار می‌کنی
وقتی داری کد را کپی-پیست می‌کنی و فقط ۱-۲ مقدار عوض می‌شود

قانون کوتاه:
حلقه اول = روی چیزی که از بیرون میاد (folder)
حلقه دوم = روی چیزی که خودت داخل کد تعریف می‌کنی

ساخت مجموعه حلقه دوم — ۴ قدم ثابت:
قدم ۱: چی ثابته بین تکرارها؟ → بیرون حلقه دوم بمونه
قدم ۲: چی متغیره بین تکرارها؟ → بره داخل یک لیست از تاپل
قدم ۳: هر المنت تاپلی باید همه چیز لازم برای یک اجرای کامل رو داشته باشه
قدم ۴: اسم متغیرهای موقت حلقه دوم باید معنادار باشه

الگوی همیشگی:
collection_2nd_loop = [
    (نام۱, داده۱, پارامتر۱),
    (نام۲, داده۲, پارامتر۲),
]
for name, data, param in collection_2nd_loop:
    # پردازش...

مثال واقعی:
binaries = [
    ("Ad_th", ad_th, (0, 255, 0)),
    ("th", th, (0, 0, 255)),
    ("edge", edge, (0, 255, 0))
]
for thresh_type, binary_img, color in binaries:
    contours, _ = cv2.findContours(binary_img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    # پردازش...

قانون نام‌گذاری خروجی:
هر فایل خروجی باید نام یکتا داشته باشد.
ترکیب: «چی بود» + «چه کاری روش شد»
مثال: f"{name}_{thresh_type}_contours.jpg"

چه زمانی تودرتو لازم است:
وقتی حلقه دوم به داده‌ای نیاز دارد که فقط داخل یک تکرار خاص از حلقه اول ساخته می‌شود

چه زمانی تودرتو لازم نیست:
وقتی دو حلقه روی داده‌های مستقل کار می‌کنند

قانون تشخیص سریع:
نیاز به متغیر همان تکرار حلقه اول → تودرتو
نیاز فقط به خروجی نهایی حلقه اول → پشت‌سرهم و مجزا


# ============================================================
# ۱۵. غربالگری تصاویر
# ============================================================

غربالگری با انحراف معیار (کنتراست):
for i in paths:
    img = cv2.imread(i, 0)
    if img is None:
        continue
    if np.std(img) > 60:      # کنتراست خوب
        # پردازش...

np.std(img) > 40 → کنتراست خوب | فیلتر ۷۰-۸۰٪ تصاویر نامناسب

آمادگی فنی (Image Processing Ready):
✅ تصویر خوانده می‌شود
✅ تغییر اندازه/برش/چرخش انجام می‌شود
✅ ذخیره خروجی انجام می‌شود

آمادگی دیتاست برای مدل (Model Training Ready):
✅ اندازه استاندارد
✅ کانال‌های رنگ یکسان
✅ نور و کیفیت قابل قبول
✅ تنوع مناسب
✅ کلاس‌های متعادل
✅ حذف تصاویر خراب و تکراری


# ============================================================
# ۱۶. قوانین پایپلاین‌ها
# ============================================================

تعریف پایپلاین:
زنجیره‌ای از مراحل متوالی که خروجی هر مرحله = ورودی مرحله بعد

قانون اول — ترتیب Gray و Blur:
همیشه Gray را قبل از Blur انجام بده (پردازش Blur روی ۱ کانال سریع‌تر است)
✅ img >> gray >> blur
❌ img >> blur >> gray

قانون دوم — جدا بودن مسیر Threshold و Canny:
هدف Threshold = جداسازی و بخش‌بندی (Segmentation)
هدف Canny = تشخیص لبه و ویژگی (Edge Detection)
این دو هدف متفاوت دارند — در یک مسیر خطی قرار نمی‌گیرند

قانون سوم — Canny روی Threshold نزن:
❌ blur >> threshold >> Canny
Threshold نویز تضعیف‌شده توسط Blur را دوباره تشدید می‌کند

قانون چهارم — Threshold روی Canny نزن:
❌ blur >> Canny >> threshold
Canny خودش نوعی Threshold داخلی دارد (هیسترزیس)

نتیجه — دو مسیر موازی از یک ریشه:
img >> gray >> blur
                  >> branch a) threshold >> save    (بخش‌بندی)
                  >> branch b) Canny >> save        (تشخیص لبه)

پایپلاین‌های استاندارد:

پایپلاین ۱: تشخیص لبه (تصاویر طبیعی)
    img >> gray >> GaussianBlur(5,5) >> Canny(50,150)

پایپلاین ۲: نویز نمک-فلفل
    img >> gray >> MedianBlur(5) >> Canny(50,150)

پایپلاین ۳: بخش‌بندی
    img >> gray >> GaussianBlur(5,5) >> threshold/adaptiveThreshold

پایپلاین ۴: استخراج شیء
    img >> gray >> threshold >> contour >> [BoundingBox | Mask | Crop]

پایپلاین ۵: پیش‌پردازش کامل
    img >> gray >> CLAHE >> Opening >> Closing


# ============================================================
# ۱۷. چیت‌شیت انتخاب روش مناسب
# ============================================================

کی Global Threshold را رد کنم؟
نور غیریکنواخت یا سایه (عکس موبایلی از کتاب)
شیء طرح‌دار یا چندتُن (مکعب روبیک، گاو سیاه و سفید)
چند شیء با روشنایی‌های متفاوت
تله تُنال: بخشی از شیء همرنگ پس‌زمینه باشد

کی Adaptive Threshold را رد کنم؟
پس‌زمینه بافت‌دار و شلوغ (چمن، فرش، پارچه)
نویز شدید نمک و فلفل
اشیاء با اندازه‌های خیلی متفاوت

کی Canny را رد کنم؟
تصویر زیادی بلور شده → لبه‌ها گنگ و تکه‌تکه
پس‌زمینه بافت‌دار → هزاران لبه کاذب
بافت داخلی غالب روی شیء (مو، پر، پولک) → طرح کلی گم می‌شود
نویز شدید → نقاط ریز همه جا
مرزهای محو → کانتور پاره

کی Contour را رد کنم؟
لبه‌های پاره و ناپیوسته (اولویت با پیوستگی است)
نویز ریز در پس‌زمینه (هر نقطه یک کانتور آشغال)
اشیاء چسبیده به هم (بزرگ‌ترین تله برای شمارش)
شیء چسبیده به لبه تصویر (مساحت و محیط اشتباه)

رد مشترک برای هر چهار روش:
پس‌زمینه شلوغ و بافت‌دار
همپوشانی شدید تُن و بافت بین شیء و پس‌زمینه

باورهای غلط:
کانتور روی کَنی زده نمی‌شود. کانتور روی خروجی ترشولد (باینری) زده می‌شود.
ترشولد ساده همیشه نقطه شروع نیست. برای تله تُنال، آداپتیو با C منفی معجزه می‌کند.
لبه ایده‌آل، لبه پیوسته است، نه لبه ۱ پیکسلی. پیوستگی را فدای نازکی نکن.
RETR_EXTERNAL دوست توست. فقط مرز بیرونی باید بسته باشد.

شش سوال سریع قبل از انتخاب روش:
۱. شیء تک‌تُن است؟ اگر نه و پس‌زمینه ساده است ← آداپتیو با C منفی.
۲. پس‌زمینه ساده است؟ اگر نه ← همه روش‌ها آرتیفکت می‌دهند.
۳. چند شیء با اندازه‌های مختلف داری؟ اگر زیاد است ← فاجعه.
۴. لبه‌ها با چشم غیرمسلح هم شارپ‌اند؟ اگر نه ← کَنی کور است.
۵. طرح کلی می‌خواهی یا بافت داخلی؟ اگر طرح کلی ← کاری به داخل شیء نداشته باش.
۶. تصویر باینری مرز بیرونی بسته دارد؟ اگر بله ← RETR_EXTERNAL و تمام.
   اگر نه ← بستن مورفولوژی قبل از کانتور.

شرایط ایده‌آل:
Global: یک شیء تک‌تُن، پس‌زمینه یکدست، نور یکنواخت.
Adaptive استاندارد: یک شیء تک‌تُن، پس‌زمینه صاف، نور غیریکنواخت.
Adaptive با C منفی: یک شیء طرح‌دار، پس‌زمینه ساده و یکدست، تله تُنال در مرز.
Canny: لبه‌های شارپ، پس‌زمینه صاف، هدف خود لبه‌هاست.
Contour: تصویر باینری با مرز بیرونی بسته. داخل می‌تواند شلوغ باشد.


# ============================================================
# ۱۸. Virtual Environment (venv)
# ============================================================

تعریف:
محیط مجازی یک پوشه ساده است که داخل پوشه پروژه ساخته می‌شود و یک کپی سبک
از پایتون و pip دارد. هر کتابخانه‌ای که نصب کنی، فقط داخل همین پوشه می‌رود.

مراحل ساخت:
cd "E:\\python\\Project_Folder"        # رفتن به پوشه پروژه
python -m venv venv                   # ساخت محیط مجازی
venv\\Scripts\\activate                 # فعال‌سازی (ویندوز)
source venv/bin/activate              # فعال‌سازی (مک/لینوکس)
deactivate                            # غیرفعال‌سازی

نصب کتابخانه:
pip install opencv-python
pip install opencv-python numpy matplotlib
pip install -r requirements.txt       # نصب از فایل قفل

ذخیره و قفل نسخه‌ها:
pip freeze > requirements.txt

چک و آپدیت:
pip list                              # دیدن کتابخانه‌های نصب شده
pip list --outdated                   # دیدن کتابخانه‌های قدیمی
pip install --upgrade numpy           # آپدیت یک کتابخانه

تست سلامت محیط:
pip -V                                # دیدن مسیر pip
python -c "import sys; print(sys.prefix)"  # چک مسیر پایتون
اگر مسیر venv اومد → فعاله
اگر Program Files یا AppData اومد → فعال نیست

قوانین طلایی venv:
همیشه requirements.txt داشته باش
پروژه کار می‌کند = آپدیت نکن
قبل آپدیت، requirements.txt را کپی کن
پوشه venv/ را توی gitignore بذار
اسم پوشه بدون فاصله باشد
فعال‌سازی فقط برای همان یک ترمینال است


# ============================================================
# ۱۹. Git و GitHub
# ============================================================

دستورات اصلی:
git init                              # ساخت Repository جدید
git status                            # بررسی وضعیت
git add .                             # آماده کردن تمام تغییرات
git commit -m "پیام توضیحی"           # ثبت تغییرات
git remote add origin URL             # اتصال به ریپوی آنلاین
git push -u origin main               # ارسال به گیت‌هاب (اولین بار)
git push                              # ارسال (دفعات بعد)
git clone URL                         # کپی کامل یک ریپو
git pull origin main                  # دریافت آخرین تغییرات

نکته مهم:
قبل از شروع کار روزانه روی پروژه تیمی، اول پول بزن.


# ============================================================
# ۲۰. ساختار استاندارد پروژه
# ============================================================

ساختار حرفه‌ای:
Object_Extraction/
├── data/              ← داده‌های ورودی
│   └── image.jpg
├── src/               ← کدهای اصلی
│   └── extraction.py
├── outputs/           ← خروجی‌های پروژه
│   └── result.jpg
├── requirements.txt   ← وابستگی‌ها
├── main.py            ← فایل اصلی اجرا
└── venv/              ← محیط مجازی

جریان کلی:
data (ورودی‌ها) → src (پردازش) → outputs (نتایج)
'''