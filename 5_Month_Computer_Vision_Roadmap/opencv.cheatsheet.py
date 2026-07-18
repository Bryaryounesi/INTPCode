'''
🎨Opencv Cheatsheet
---------------------------------------
مثال اولیه برای انجام یکجای چند عملیات رو تصاویر
(برای پرهیز از درگیر شدن در سینتکس مراحل عملیات ها)
# حلقه زدن روی عملیات تصویر
# انجام یکجای عملیات تصویر
-----------------
import cv2
from pathlib import Path    #پزلیب برای دسترسی یکجا به تصاویر
# from cvtools import cvt  #ماژول شخصی
p = print

نمونه ساخته شده از کلاس پز(اسم نمونه فولدر است)
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\input")
pathes = [str(i) for i in folder.glob("*.jpg")]   لیست کل مسیرهای تصاویر
# -------------
for i in pathes:     #حلقه زدن روی لیست مسیر ها
    img = cv2.imread(i)
    fliped = cv2.flip(img,1)
    resized = cv2.resize(img, dsize=None, fx=0.6, fy=0.6, interpolation=cv2.INTER_AREA)
    rotated = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)  #چرخش بدون ماتریس
    h, w = img.shape[:2]
    roi = img[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]    #برش پنجاه درصد مرکزی
    # ----------------------------------
    # ساخت اسامیِ بدون پسوند از مسیر تصاویر
    num = i.split("\\")[-1].split(".")[0]
    # ذخیره تمام تصاویر تغییر یافته
    # cv2.imwrite(f"fliped_{num}.jpg",fliped)
    # cv2.imwrite(f"resized_{num}.jpg", resized)
    # cv2.imwrite(f"rotated_{num}.jpg", rotated)
    # cv2.imwrite(f"roi_{num}.jpg", roi)
----------------------------------------------------------------
---------------------------------------------------------------
ادامه آموزش (با تفکیک مراحل و جزئیات هر مرحله):

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-01\Data\deers.jpg"
==============================================================================
✅ ۱. خواندن تصویر — cv2.imread()
خواندن فایل و تبدیل به آرایه NumPy
==============================================================================
شکل رایج:
img = cv2.imread(path, flag)

پارامتر ها :
path = پارامتری به این نام نداریم و این یک متغیر است حاوی مسیر فایل
flag =پارامتری به این اسم نیست و مستقیما درج والیوی آن. تعیین کننده نوع خوانده شدن تصویر
اگر درج نشود حالت پیشفرض آن اعمال میشود
---------------
والیو های پارامتر فلگ:

cv2.IMREAD_COLOR     → رنگی BGR (پیش‌فرض)
cv2.IMREAD_COLOR_RGB   تصویر را به صورت آرجی بی میخواند
cv2.IMREAD_GRAYSCALE  → خاکستری
cv2.IMREAD_UNCHANGED → با کانال آلفا
cv2.IMREAD_REDUCED_COLOR_2 → نصف ابعاد اصلی
نکته :اگر میخواهیم تصویر را با اپن سیوی ذخیره کنیم بهتر است آن را با فلگ پیشفرض آن  بخوانیم
(هر چند به صورت جی بی آر نمایش داده میشود)
چون در مرحله ذخیره به صورت آرجی بی و مثل تصویر های معمولی ذخیره میشود
ولی اگر آن را در مرحله خواندن به صورت آر جی بی بخوانیم ، به صورت جی بی آر ذخیره میشود

مثال:
img_color = cv2.imread(path, cv2.IMREAD_COLOR)
img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

بررسی موفقیت خواندن:
if img_color is None:
    print("خطا: تصویر خوانده نشد!")
بهتر است در خواندن تصاویر پر تعداد این کد را بلافاصله بعد از خواندن تصاویر درج کنیم مثلا :

for i in pathes:
    img = cv2.imread(i)     #خواندن تصویر
    if img is None:         #کد جلوگیری از ارور در صورت مشکل دار بودن تصاویر
        p(f"error in reading: {i}")
        continue  #اگر تصویر مشکل داشت ارور نمیدهد و از آن تصویر رد میشود
        # انجام مراحل بعدی کار
    rotated = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(output / f"rotated_{name}.jpg", rotated)
==============================================================================
✅ ۲. نمایش تصویر با OpenCV — cv2.imshow()
==============================================================================

شکل رایج:
cv2.imshow("winname", img)

winname: نام پنجره (رشته) — همیشه اولین پارامتر
img: آرایه تصویری

کنترل پنجره:
cv2.waitKey(0)           → صبر تا زدن کلید
cv2.waitKey(2000)        → نمایش ۲ ثانیه
cv2.destroyAllWindows()  → بستن همه پنجره‌ها

تنظیم اندازه پنجره برای رفع زوم‌شدگی:
cv2.namedWindow("win", cv2.WINDOW_NORMAL)  # قابل تغییر با موس
cv2.resizeWindow("win", width, height)      # ابعاد دلخواه
نیاز به تنظیم پنجره با ماژول شخصی برطرف شد

مثال:
cv2.imshow("My Image", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

نکته : یک ماژول در پروژه تعریف کردم که نیاز به توابع کنترل پنجره را از بین میبرد تنها کافیست آن را ایمپورت کنیم و برپایه آن فایل را بخوانیم به این صورت:
from cvtools import cvt
cvt.imshow("win",img)
==================================================================
✅ ۳. نمایش تصویر با Matplotlib — plt.imshow()
در بحث کاربرد مت پلات لیب در اپن سیوی توضیح داده شده
==================================================================
✅ ۴. تبدیل رنگ تصویر — cv2.cvtColor()
روش معمول در برنامه پنج ماهه، یک بار خواندن تصویر و تبدیل رنگ های بعدی است (چون بهینه تر است)
و نه چند بار خواندن با فلگ های متفاوت

شکل رایج:
converted_img = cv2.cvtColor(img, code)

پارامتر ها :
img =متغیر حاوی تصویر اولیه
code = کد های تبدیل ، پارامتر یا متغیری به این نام نداریم

کدهای پرکاربرد:
cv2.COLOR_BGR2GRAY  → رنگی به خاکستری
cv2.COLOR_BGR2RGB   → BGR به RGB (برای Matplotlib)
cv2.COLOR_GRAY2BGR  → خاکستری به رنگی (۳ کاناله)
اگر هدف نهایی ما ذخیره تصویر به صورت آرجی بی بود نیاز به تبدیل تصویر رنگی خوانده شدۀ اولیه نیست

مثال:
img = cv2.imread(path,cv2.IMREAD_COLOR) تصویر رنگی خوانده شده
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) تبدیل به خاکستری
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) تبدیل به آرجی بی
--------------------------------------
سوال مهم : چه زمانی تصویر را رنگی بخوانیم و تبدیل کنیم
و کی به جای تبدیل، تصویر را با فلگ های متفاوت بخوانیم؟
# تبدیل رنگ یا چند بار خواندن تصویر
# یک بار خواندن یا چندبارخواندن با فلگ

۱. فایل محلی روی SSD سریع:
   روش بهینه: خواندن با فلگ متفاوت
   دلیل: سربار تبدیل CPU رو حذف می‌کنه

۲. Raspberry Pi / SD Card کند:
   روش بهینه: یک بار خوندن + cvtColor
   دلیل: خواندن از RAM سریع‌تر از دیسکه
(پس روش معمول در مباحث برنامه 5 ماهه، یک بار خواندن و تبدیل بعدی  است)

۳. استریم دوربین / ویدئو:
   روش بهینه: cvtColor اجباری
   دلیل: فقط یک فریم داری

۴. تصویر از قبل در حافظه (NumPy):
   روش بهینه: cvtColor اجباری
   دلیل: imread اصلاً معنی نداره

۵. فایل روی شبکه (NAS/Cloud):
   روش بهینه: یک بار خوندن + cvtColor
   دلیل: تأخیر شبکه > تأخیر CPU

۶. پردازش بلادرنگ (Real-time):
   روش بهینه: یک بار خوندن + cvtColor
   دلیل: کاهش I/O Wait

۷. پردازش دسته‌ای (Batch) روی SSD:
   روش بهینه: خواندن با فلگ متفاوت
   دلیل: استفاده از کش سیستم‌عامل

==================================================================
✅ ۵. ذخیره تصویر — cv2.imwrite()
ذخیره تصاویر اغلب با اپن سیوی
در مواردی خاص استفاده از مت پلات لیب برای ذخیره سازی
این موارد در بخش کاربرد  متپلات لیب در اپن سیوی توضیخ داده شده اند
==================================================================

شکل رایج:
cv2.imwrite(filename, img)

filename: مسیر و نام فایل با پسوند (مثلاً "output.jpg")
یعنی میتوانیم صرفا یک اسم رشته ای پشوند دار بدهیم مثل :
"output.jpg"
یا یک پَز بدهیم که انتهای آن اسم تصویری باشد که ذخیره میکنیم. مثلا :
"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-03\Data\lamborghini.jpg"

img:متغیر حاوی تابع خواندن تصویری که میخاهیم ذخیره کنیم

مثال:
cv2.imwrite("gray_image.jpg", img_gray)
# --------------------------------------------------------------------
# ذخیره تصویر خروجی در پوشه دلخواه
---------------------------------------------------------------------
# باید مسیر پوشه دلخواه را به ابتدای اسامی فایل های خروجی اضافه کنیم
# برای کوتاه کردن مسیر پوشه از کتابخانه پزلیب استفاده میکنیم
output = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Output"
    )
output.mkdir(parents= True,exist_ok=True)
cv2.imwrite(output / f"resized_{name}.jpg",resized)
# ---------------------------------------
نکات مهم:
# 1)
# حتما باید بعد از واژه پز، پرانتز بگذاریم و سپس یک اینتر بزنیم که پرانتز بشکند
# اگر واژه پز جدا باشد یا کل پز رو در یک خط بنویسیم ارور خواهیم داشت
مثلا output = Path(
    r"مسیر پوشه خروجی"
)
# 2)کد ایمنی در برابر نبود احتمالی پوشه خروجی
output.mkdir(parents= True,exist_ok=True)
# اگر پوشه وجود نداشت خودش پوشه ای به این نام میسازد
==============================================================================
✅ ۶. تغییر اندازه — Resize: cv2.resize()
==============================================================================

شکل رایج:
resized = cv2.resize(img, dsize = (width, height), interpolation=cv2.INTER_AREA)
الگوی دوم با ضرایب مقیاس
resized = cv2.resize(img, dsize =None,fx= 0.6, fy = 0.6, interpolation=cv2.INTER_AREA)

پارامتر ها :
---> img =  تصویر ورودی (تصویر حاصل از خوانده شدن پز)
--->  dsize = (width, height)
تاپلی از عرض و ارتفاع تصویر - اسم دی سایز لازم نیست
اگر بخواهیم از شیپ عکس دی سایز را بگیریم باید از آنپک کردن سلایسنگ شیپ استفاده کنیم
با این کار عرض و ارتفاع به عنوان دو متغیر والیو میگیرند و والیوی کانال ها از سلایس شیپ حذف میشود
w,h = img.shape[:2]  تنها المنت اول و دوم یعنی عرض و ارتفاع تصویر در سلایس شیپ هستند
# -------------------------------------
----> interpolation: پارامتری برای تعیین نحوه ترمیم پیکسل ها بعد از ریسایز
در صورت تعریف این پارامتر در ریسایز، ذکر نام خود پارامتر ضروری است
اگر پارامتر را تعریف نکنیم به صورت پیش فرش روی اینتر لاینیر است

interpolation = cv2.INTER_AREA    → بهترین برای کوچک‌سازی
interpolation = cv2.INTER_LINEAR  → پیش‌فرض (تغییرات جزئی)
interpolation = cv2.INTER_CUBIC   → بهترین برای بزرگ‌نمایی
interpolation = cv2.INTER_NEAREST → سریع (برای ماسک و باینری)
------------------------------
ضرایب مقیاس : fx , fy
هر وقت از ضرایب مقیاس استفاده کنیم باید
dsize = None
باشد.
-----> fx = عددی اعشاری و بزرگ تر از صفر
ضریب مقیاس در جهت افقی
مثلا fx = 0.6   عرض تصویر 60 درصد عرض اولیه باشد
fx = 1.5   عرض تصویر یک و نیم برابر عرض اولیه باشد
# ------------
fy = مثل اف ایکس ولی برای تغییر ارتفاع

--- روش ساده (بدون حفظ نسبت) ---
img_resized = cv2.resize(img_color, (400, 300), interpolation=cv2.INTER_AREA)

--- روش استاندارد: حفظ نسبت تصویر با محاسبه دستی ---
h, w = img.shape[:2]                         # ارتفاع، عرض اصلی
new_w = 400                                  # عرض جدید دلخواه
new_h = int((h * new_w) / w)                 # ارتفاع متناسب با تناسب
resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
==============================================================================
✅ ۷. برش تصویر — Crop / ROI (Slicing آرایه NumPy)
==============================================================================

ROI = Region of Interest = ناحیه مورد نظر برای برش

شکل رایج (برش مستطیلی):
roi = img[y1:y2, x1:x2]

y1:y2 → بازه ارتفاع (ردیف‌ها)
x1:x2 → بازه عرض (ستون‌ها)
------------------------
# انواع برش
-----------------
1- برش 50 درصد مرکزی (مناسب برای برش اتوماتیک و یکجای تعداد زیادی تصویر)
# روش توصیه شده
h, w = img.shape[:2]
    roi = img[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]
----------------------------
2 - برش دلخواه(برای برش های دلخواه و بیشتر برای تصاویر تکی)

roi = img[100:300, 200:450]   → برش مستطیلی کامل
roi = img[50:250, :]          → فقط برش عمودی (کل عرض حفظ می‌شود)
roi = img[:, 100:350]         → فقط برش افقی (کل ارتفاع حفظ می‌شود)

نکته: برای یافتن مختصات دقیق، تصویر را در Paint ویندوز باز کنید
و مختصات پیکسلی موس را بخوانید.
میتوانید تصویر را با مت پلات لیب هم بخوانید و همین کار را انجام دهید
# -----------------------------
نحوه پیدا کردن مختصات برش :
موس را ابتدا در ارتفاع تصویر حرکت دهید و اول و آخر بخشی از مختصات موس را که تغییر میکند(محدوده ارتفاعی دلخواه برش) بنویسید
سپس موس را در عرض تصویر حرکت داده و نقطه اول و آخر بخشی از مختصات رو که عوض میشه(محدوده عرضی برش ) بنویسید
سپس اینها رو در سلایس ایمیج درج میکنیم
حال میتوانید برش تصویر خود را نمایش یا ذخیره کنید

مثال:
roi = img_color[42:366, 301:534]
cvt.imshow("win",roi)

==============================================================================
✅ ۸. چرخش تصویر — Rotate (چهار مرحله)
کل مراحل چرخش، با ماژول شخصیِ وی اس تی تولز ، اتوماتیک شده اند
پس برای چرخش تنها کافیست این کد را درج کنیم:
import cv2
from cvtools import cvt
rotated = cvt.rotate(img,degree)
=============================================================================
# چرخش تصویر بدون ماتریس چرخش ( چرخش مضرب 90)
# نوع ساده ای از چرخش  و مناسب برای چرخواندن یکجای تعداد زیادی تصویر
سه حالت داره که هر حالت به دو شکل نوشته میشه

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated = cv2.rotate(img, 0)

rotated =cv2.rotate(img, cv2.ROTATE_180)
rotated =cv2.rotate(img, 1)

rotated =cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
rotated =cv2.rotate(img,2)
---------------------------------
# چرخش تصویر با ماتریس چرخش
نوع تخصصی تری از چرخش با مراحل زیاد و پیچیده

--- مرحله ۱: ساخت ماتریس چرخش ---
پیشنیاز ها :
خواندن تصویر:
img = cv2.imread(path)
# -----------------
بدست آوردن ابعاد اولیه تصویر از شیپ آن:
h,w = img.shape[:2]
# -------------------
بدست آوردن پارامترهای ماتریس چرخش :
center = (w // 2, h // 2)     # مرکز تصویر (تقسیم صحیح)
angle = 30                     # مثبت → پادساعتگرد
scale = 1                      # 1 = بدون تغییر اندازه
# ---------------
در نهایت ساخت ماتریس چرخش
M = cv2.getRotationMatrix2D(center, angle, scale)
# -----------------------------
# توضیح اجزا و ابعاد ماتریس چرخش:

ابعاد ماتریس چرخش تصویر:
همیشه ماتریسی دو بعدی است (2 ردیف و سه ستون )
p(M.shape) = (2,3)
---------------------------
محتوای ماتریس چرخش (هر المنت ماتریس دقیقا از چی ساخته شده)
حتماً.

[ cos(θ)*s   sin(θ)*s   tx ]
[ -sin(θ)*s  cos(θ)*s   ty ]
θ : رادیان شده درجه چرخش است
s= مقیاس ماست عددی بین صفر و یک
# ------------------
tx , ty : مولفه های انتقال یا بردارهای جابجایی هستند
(Translation vectors)
جابجاکننده تصویر چرخیده شده برای قرارگیری درست در پنجره نهایی تصویر
tx = جابجاکننده تصویر درجهت محور ایکس(افقی)
ty =جابجاکننده تصویر درجهت محور ایگریک(عمودی)
# -------------
دسترسی به مولفه های انتقال با ایندکس ماتریس انتقال
tx = rotaion_matrix[0,2]   #پارامتر ردیف اول و ستون سوم
ty = rotation_matrix[1,2]     #پارامتر ردیف دوم، ستون سوم

--- مرحله ۲: محاسبه ابعاد جدید (جلوگیری از بریدگی گوشه‌ها) ---
اگر بریده شدن گوشه ها مهم نیست میتوانیم مستقیما از مرحله اول برویم مرحله چهارم

theta = np.radians(angle)                      # تبدیل درجه چرخش به رادیان
# --------------
ساخت ابعاد جدید با سین و کوسینوس این رادیان:
new_w = int(h * np.sin(theta) + w * np.cos(theta))          # عرض جدید
new_h = int(h * np.cos(theta) + w * np.sin(theta))          # ارتفاع جدید
⚠️ خروجی باید int شود

--- مرحله ۳: اصلاح مرکز ماتریس چرخش---
اصلاح مرکز ماتریس چرخش برای سازگاری با قاب تصویر جدید بعد از چرخش
این کار در واقع یعنی افزودن نصف تفاضل تغییرات ابعاد جدید و قدیم به مولفه های انتقال در ماتریس چرخش
ماتریس M یک آرایه ۲×۳ است:
M[0, 2] → جابه‌جایی افقی (محور x)
M[1, 2] → جابه‌جایی عمودی (محور y)
M[0, 2] += (new_w - w) // 2   نصف تفاضل عرض جدید و قدیم به تی ایکس افزوده شده
M[1, 2] += (new_h - h) // 2    نصف تفاضل ارتفاع جدیدوقدیم به تی ایگریک اضافه شده
تقسیم صحیح برای اعشاری نشدن نتیجه تقسیم است که گاها توصیه نمیشود چون سبب نیم پیکسل گرد شدگی میشود

--- مرحله ۴: اعمال چرخش ---
rotated = cv2.warpAffine(img, M, (new_w, new_h))

مثال کامل:
img = cv2.imread(path)
# ------------------
angle = 30
h, w = img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1)
# --------------------------
theta = np.radians(angle)
new_w = int(h * np.sin(theta) + w * np.cos(theta))
new_h = int(h * np.cos(theta) + w * np.sin(theta))
# --------------------
M[0, 2] += (new_w - w) // 2
M[1, 2] += (new_h - h) // 2
# ---------------------
rotated = cv2.warpAffine(img, M, (new_w, new_h))
cv2.imshow("win",rotated)

==============================================================================
✅ ۹. وارونه‌سازی — Flip: cv2.flip()
==============================================================================

شکل رایج:
flipped = cv2.flip(img, flipCode)

flipCode = 0  → وارونه عمودی (سر و ته، دور محور x)
flipCode = 1  → وارونه افقی (مانند آینه، دور محور y)
flipCode = -1 → وارونه دو طرفه (معادل چرخش ۱۸۰°)

مثال:
flip_horizontal = cv2.flip(img, 1)
flip_vertical = cv2.flip(img, 0)
flip_both = cv2.flip(img, -1)


==============================================================================
✅ ۱۰. قاعده کلی ابعاد در OpenCV
==============================================================================

⚡ روش حفظ کردن:
img[row, col]  →  img[y, x]
size = (width, height)  →  (x, y)

📌 قاعده:
هر جا size می‌دهیم: اول = عرض (width)
  cv2.resize(img, (width, height))
  cv2.warpAffine(img, M, (width, height))

هر جا از img.shape می‌گیریم: اول = ارتفاع (height)
  img.shape → (height, width, channels)
  h, w = img.shape[:2]


==============================================================================
✅ ۱۱. انواع ماتریس‌های تبدیل
==============================================================================

۱. ماتریس انتقال (Translation):
M = np.float32([[1, 0, tx], [0, 1, ty]])
cv2.warpAffine(img, M, (w, h))

۲. ماتریس تغییر مقیاس (Scaling):
cv2.resize(img, None, fx=sx, fy=sy, interpolation=cv2.INTER_AREA)

۳. ماتریس چرخش (Rotation):
M = cv2.getRotationMatrix2D(center, angle, scale)
cv2.warpAffine(img, M, (new_w, new_h))

۴. ماتریس برش (Shear):
M = np.float32([[1, k, 0], [0, 1, 0]])
cv2.warpAffine(img, M, (w, h))

۵. ماتریس آفین (Affine):
M = cv2.getAffineTransform(pts1, pts2)
cv2.warpAffine(img, M, (w, h))

۶. ماتریس پرسپکتیو (Perspective):
M = cv2.getPerspectiveTransform(pts1, pts2)
cv2.warpPerspective(img, M, (w, h))
====================================================
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# راهنمای جامع استفاده از Matplotlib در پروژه‌های OpenCV
# هر بخش شامل: ۱. کد نمایش  ۲. روش صحیح ذخیره‌سازی
# ============================================================
# کاربرد متپلات لیب در اپن سیوی
# استفاده از متپلات لیب در اپن سیوی
# رسم با مت پلات لیب
--------------
# تصویر نمونه برای تست (خودتان مسیر را عوض کنید)
img = cv2.imread("example.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)

# تبدیل کلی BGR به RGB برای تمام نمایش‌های رنگی
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# ============================================================
# ۱. نمایش یک تصویر تکی
# ============================================================
plt.figure(figsize=(8, 6))
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

# روش ذخیره: حتماً با OpenCV (کیفیت پیکسلی بدون افت)
cv2.imwrite("output_image.jpg", img)

# ============================================================
# ۲. نمایش تصویر خاکستری با نقشه رنگی مشخص
# ============================================================
plt.figure(figsize=(8, 6))
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# روش ذخیره: OpenCV (خود تصویر خاکستری را ذخیره می‌کنیم)
cv2.imwrite("output_gray.jpg", gray)

# ============================================================
# ۳. نمایش چند تصویر در کنار هم (Subplot)
# ============================================================
# رسم چند عکس با مت پلات لیب

fig, axes = plt.subplots(1, 3, figsize=(15, 5),contrained_layout = True)

axes[0].imshow(img_rgb)
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(gray, cmap="gray")
axes[1].set_title("Grayscale")
axes[1].axis("off")

axes[2].imshow(edges, cmap="gray")
axes[2].set_title("Canny Edges")
axes[2].axis("off")

# plt.tight_layout() پارامتر کانستریند لایوت جای این تابع را میگیرد
# plt.show() نباید قبل از ذخیره کردن، تصویر را نمایش دهیم چون صفحه خالی ذخیره میشود

# روش ذخیره (گزارشی): Matplotlib (چون تیتر و چیدمان مهم است)
fig.savefig(fname="multipix.png",dpi=300,bbox_inches ="tight")

# روش ذخیره (پردازشی): OpenCV (اگر کلاژ برای پردازش بعدی لازم دارید)
collage = np.hstack((img, cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)))
cv2.imwrite("collage_for_processing.png", collage)

# ============================================================
# ۴. نمایش و ذخیره‌سازی کلاژ در Matplotlib (گزارشی)
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.imshow(img_rgb)
ax1.set_title("Before")
ax1.axis("off")

ax2.imshow(edges, cmap="gray")
ax2.set_title("After Edge Detection")
ax2.axis("off")

plt.suptitle("Processing Result", fontsize=16)
plt.tight_layout()
plt.show()

# روش ذخیره: حتماً Matplotlib
plt.savefig("before_after.png", dpi=200, bbox_inches="tight")

# ============================================================
# ۵. رسم هیستوگرام تصویر خاکستری
# ============================================================
plt.figure(figsize=(10, 5))
plt.hist(gray.ravel(), bins=256, range=[0, 256], color="black")
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.grid(alpha=0.3)
plt.show()

# روش ذخیره: حتماً Matplotlib (خروجی نمودار است، نه عکس)
plt.savefig("histogram_gray.png", dpi=150, bbox_inches="tight")

# ============================================================
# ۶. رسم هیستوگرام کانال‌های رنگی جداگانه
# ============================================================
colors = ("b", "g", "r")
plt.figure(figsize=(10, 5))

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=f"Channel {col.upper()}")

plt.title("RGB Histogram (Note: OpenCV stores as BGR, but plot shows RGB order)")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# روش ذخیره: حتماً Matplotlib
plt.savefig("histogram_rgb.png", dpi=150, bbox_inches="tight")

# ============================================================
# ۷. نمایش تصویر به همراه نمودار هیستوگرام در یک فیگور
# ============================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.imshow(img_rgb)
ax1.set_title("Image")
ax1.axis("off")

ax2.hist(gray.ravel(), bins=256, range=[0, 256], color="gray")
ax2.set_title("Histogram")
ax2.set_xlabel("Intensity")
ax2.set_ylabel("Count")
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# روش ذخیره: حتماً Matplotlib
fig.savefig("image_with_histogram.png", dpi=150, bbox_inches="tight")

# ============================================================
# ۸. رسم پروفایل شدت نور روی یک خط دلخواه (Line Profile)
# ============================================================
# کشیدن یک خط افقی وسط تصویر
line_y = gray.shape[0] // 2
intensity_profile = gray[line_y, :]

plt.figure(figsize=(12, 4))
plt.plot(intensity_profile, color="blue", linewidth=0.8)
plt.title(f"Intensity Profile at y = {line_y}")
plt.xlabel("X Position (pixel)")
plt.ylabel("Intensity")
plt.grid(alpha=0.3)
plt.show()

# روش ذخیره: حتماً Matplotlib
plt.savefig("line_profile.png", dpi=150, bbox_inches="tight")

# ============================================================
# ۹. نمایش ماتریس اعداد به صورت Heatmap (مثلاً ماتریس کانفیوژن یا نقشه ویژگی)
# ============================================================
# یک ماتریس نمونه
feature_map = cv2.resize(gray, (50, 50))

plt.figure(figsize=(8, 6))
plt.imshow(feature_map, cmap="hot", interpolation="nearest")
plt.colorbar(label="Intensity")
plt.title("Feature Map / Heatmap")
plt.axis("off")
plt.show()

# روش ذخیره گزارش: Matplotlib (چون colorbar و تیتر دارد)
plt.savefig("heatmap.png", dpi=150, bbox_inches="tight")

# روش ذخیره داده خام: OpenCV (اگر فقط ماتریس برای شما مهم است)
cv2.imwrite("feature_map_raw.png", feature_map)

# ============================================================
# ۱۰. نمایش مراحل مختلف یک پایپلاین پردازشی
# ============================================================
# شبیه‌سازی چند مرحله پردازش
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
dilated = cv2.dilate(thresh, None, iterations=1)

fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

titles = ["Original Gray", "Gaussian Blur", "Binary Threshold", "Dilated"]
images = [gray, blurred, thresh, dilated]

for i in range(4):
    axes[i].imshow(images[i], cmap="gray")
    axes[i].set_title(titles[i])
    axes[i].axis("off")

plt.suptitle("Image Processing Pipeline", fontsize=16)
plt.tight_layout()
plt.show()

# روش ذخیره: Matplotlib (نمای کلی از فرآیند)
fig.savefig("pipeline_steps.png", dpi=150, bbox_inches="tight")

# ============================================================
# خلاصه قوانین ذخیره‌سازی:
# ============================================================
# - فقط عکس خام (بدون نمودار/تیتر) → cv2.imwrite()
# - هر چیزی که نمودار، هیستوگرام، یا چند subplot دارد → plt.savefig()
# - کلاژ عکس برای پردازش مجدد → با np.hstack بسازید و cv2.imwrite() کنید
# ============================================================
print("end of matplotlip usenesses in opencv")

====================================================
📝 الگوی کامل پروژه ترکیبی (نمونه اجرایی)
ترکیب تمام مهارت‌ها: خواندن، تبدیل، resize، crop، rotate، flip، ذخیره
=======================================================

def sample_project_pipeline(path):
    """
    نمونه کامل از ترکیب تمام مهارت‌های هفته ۳
    """
    # ۱. خواندن تصویر
    img = cv2.imread(path)
    if img is None:
        print("تصویر یافت نشد!")
        return

    # ۲. تبدیل به RGB برای نمایش صحیح
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ۳. تغییر اندازه با حفظ نسبت
    h, w = img.shape[:2]
    new_w = 400
    new_h = int((h * new_w) / w)
    img_resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # ۴. برش — یک‌چهارم مرکزی تصویر
    h_r, w_r = img_resized.shape[:2]
    y1, y2 = h_r // 4, 3 * h_r // 4
    x1, x2 = w_r // 4, 3 * w_r // 4
    roi = img_resized[y1:y2, x1:x2]

    # ۵. چرخش ROI
    angle = 30
    h_c, w_c = roi.shape[:2]
    center = (w_c // 2, h_c // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1)
    theta = np.radians(angle)
    new_w_rot = int(h_c * np.sin(theta) + w_c * np.cos(theta))
    new_h_rot = int(h_c * np.cos(theta) + w_c * np.sin(theta))
    M[0, 2] += (new_w_rot - w_c) // 2
    M[1, 2] += (new_h_rot - h_c) // 2
    rotated = cv2.warpAffine(roi, M, (new_w_rot, new_h_rot))

    # ۶. Flip افقی
    flipped = cv2.flip(rotated, 1)

    # ۷. ذخیره تصویر نهایی
    cv2.imwrite("final_output.jpg", flipped)

    # ۸. نمایش مقایسه‌ای
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    axes[0].imshow(img_rgb)
    axes[0].set_title("Original")
    axes[0].axis("off")

    roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
    axes[1].imshow(roi_rgb)
    axes[1].set_title("Cropped")
    axes[1].axis("off")

    final_rgb = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    axes[2].imshow(final_rgb)
    axes[2].set_title(f"Rotated {angle}° + Flipped")
    axes[2].axis("off")

    plt.tight_layout()
    plt.savefig("comparison_output.png", dpi=150, bbox_inches="tight")
    plt.show()

# برای اجرا، مسیر تصویر را تنظیم و خط زیر را از کامنت خارج کنید:
# sample_project_pipeline(DEFAULT_IMAGE_PATH)
'''
# ----------------------------------------------------------------
# راهنمای استفاده از کتابخانه pathlib
# -----------------------------------------------------------------
import cv2
p = print

# برای یک تصویر تکی پز تصویر رو به شکل زیر وارد میکنیم
# تا بعدا از آن در فرمول خواندن تصویر استفاده کنیم
# قبل از پَز ها باید یک آر درج کنیم تا پزها قابل خواندن
# ----
# اگر پز رو از خود ویندوز بگیریم و نه وی اس کد نیازی به این آر ها نیست
# ولی علامت / تبدیل به \ یا \\ میشوند

path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\input\cow.jpg"
image = cv2.imread(path)
'''
ولی برای تصاویر بیشتر، منطقی نیست پَز ها رو تک تک وارد کنیم
بهتر است تصاویر منبع را در یک پوشه، ذخیره کنیم و پز پوشه را به کتابخانه پَزلیب بدهیم تا لیستی از اسامی تصاویر به ما بده
'''
# --------------------------------
# نحوه استفاده از پزلیب
# 1) ایمپورت کردن کلاس پَز از کتابخانه پَزلیب
from pathlib import Path
# -----------------
# 2) ساخت یک نمونه از کلاسِ پَز به نام فولدر و به کمک پَز پوشه منبع
folder = Path(r"folder_path")
# مثلا:
folder = Path(r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\input")
# -------------------
# 3) ساخت لیست های دلخواه از این نمونه با لیست کامپرهنشن

pathes = [str(i) for i in folder.glob("*.jpg")]
# لیست مسیر های کامل تصاویر پوشه
# برای خواندن یکجای تصاویر کاربرد دارد(کاربردی ترین نوع لیست )
# مثلا:
# for i in pathes:
#     img = cv2.imread(i)
#     cvt.imshow("win",img)
# ------------------------
# ساخت نام بدون پسوند تصاویر از پز ها برای استفاده در اسامی تصاویر خروجی در مرحله ذخیره
# name = Path(i).stem   در این مثال روی لیست مسیرها حلقه زدیم پس از متغیر حلقه استفاده شده
# cv2.imwrite(output / f"roi_{name}.jpg", roi)
# --------------------------
# مثال کامل:
'''
import cv2
from pathlib import Path
# from cvtools import cvt
p = print
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data")
pathes = [str(i) for i in folder.glob("*.jpg")]
# ---------------------------------------------
for i in pathes:
    img = cv2.imread(i)     #خواندن تصویر
    # ----------------------------
    resized = cv2.resize(img,dsize=None,fx=0.7,fy = 0.7,interpolation=cv2.INTER_LINEAR)  #ریسایز
    # ------------------------------
    # ساخت نام بدون پسوند تصاویر
    name = Path(i).stem
    # name = i.split("\\")[-1].split(".")[0]   کد معادل
    # --------------------------------------
    # ساخت مسیر خروجی :
    output = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Output"
    )
    output.mkdir(parents= True,exist_ok=True)
    # --------------------------------
    # خواندن تصویر:
    # cv2.imwrite(output / f"resized_{name}.jpg",resized)
'''
# ------------------------------------------------------------
# بررسی آمادگی فنی تصاویر خروجی و آمادگی تصاویر برای آموزش مدل
# تفاوت آمادگی فنی با آمادگی دیتاست

# 1) Image processing ready آمادگی فنی تصاویر
# این نوع آمادگی با آمادگی برای آموزش مدل فرق میکند و سطحی ابتدایی تر از آمادگی است

# چک لیست آمادگی فنی:
# ✅ تصویر خوانده می‌شود
# ✅ تغییر اندازه انجام می‌شود
# ✅ برش انجام می‌شود
# ✅ چرخش انجام می‌شود
# ✅ ذخیره خروجی انجام می‌شود
# یعنی:
# ابزارها و عملیات پایه روی تصاویر درست کار می‌کنند.
# -------------------------------------
# 2) آماده‌سازی دیتاست برای مدل (Model Training Ready)
# چک لیست:
# ✅ همه تصاویر اندازه استاندارد داشته باشند
# ✅ کانال‌های رنگ یکسان باشند
# ✅ نور و کیفیت قابل قبول باشد
# ✅ داده‌ها تنوع مناسب داشته باشند
# ✅ برچسب‌ها درست باشند
# ✅ کلاس‌ها متعادل باشند
# ✅ تصاویر خراب و تکراری حذف شوند

# این مرحله زمانی مهم می‌شود که بخواهیم:
# - CNN آموزش دهیم
# - YOLO استفاده کنیم
# - مدل تشخیص یا طبقه‌بندی بسازیم
# -------------------------------------------------------
