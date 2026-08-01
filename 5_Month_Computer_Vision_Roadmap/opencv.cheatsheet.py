# 🎨 OpenCV Cheatsheet
'''
---------------------------------
مثال اولیه برای پردازش یکجای تصاویر
(آشنایی با ساختار حلقه و عملیات‌ها)

import cv2
from pathlib import Path
p = print

folder = Path(r"E:\\...\\Data\\input")
pathes = [str(i) for i in folder.glob("*.jpg")]

for i in pathes:
    img = cv2.imread(i)
    if img is None:
        p(f"error in reading: {i}")
        continue

    flipped = cv2.flip(img, 1)
    resized = cv2.resize(img, dsize=None, fx=0.6, fy=0.6)
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    h, w = img.shape[:2]
    roi = img[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]

    num = i.split("\\\\")[-1].split(".")[0]
    # cv2.imwrite(f"fliped_{num}.jpg",fliped)
    # cv2.imwrite(f"resized_{num}.jpg", resized)

----------------------------------------------------------------
ادامه آموزش (با تفکیک مراحل و جزئیات هر مرحله):

import cv2
import numpy as np
import matplotlib.pyplot as plt

path = r"E:\\...\\Data\\deers.jpg"

==============================================================================
✅ ۱. خواندن تصویر — cv2.imread()
==============================================================================
شکل رایج:
img = cv2.imread(path)
img_color = cv2.imread(path, cv2.IMREAD_COLOR)
img_gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

پارامترها:
path: مسیر فایل تصویری.
flag: نحوه خواندن تصویر. پیش‌فرض: cv2.IMREAD_COLOR (رنگی BGR).

مقادیر flag:
cv2.IMREAD_COLOR           → رنگی BGR (پیش‌فرض)
cv2.IMREAD_COLOR_RGB       → رنگی RGB
cv2.IMREAD_GRAYSCALE       → خاکستری
cv2.IMREAD_UNCHANGED       → با کانال آلفا
cv2.IMREAD_REDUCED_COLOR_2 → نصف ابعاد اصلی

نکته مهم: اگر می‌خواهیم تصویر را با OpenCV ذخیره کنیم، بهتر است با فلگ پیش‌فرض
(cv2.IMREAD_COLOR) بخوانیم. چون در مرحله ذخیره به صورت RGB ذخیره می‌شود.
اما اگر با cv2.IMREAD_COLOR_RGB بخوانیم، موقع ذخیره به صورت BGR ذخیره می‌شود!

بررسی موفقیت خواندن (ضروری برای پردازش دسته‌ای):
if img is None:
    print("خطا: تصویر خوانده نشد!")
    continue  # رد شدن از تصویر مشکل‌دار

مثال حل‌شده — حلقه با بررسی خطا:
for i in pathes:
    img = cv2.imread(i)
    if img is None:
        p(f"error in reading: {i}")
        continue
    rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(output / f"rotated_{name}.jpg", rotated)

==============================================================================
✅ ۲. نمایش تصویر با OpenCV — cv2.imshow()
==============================================================================
شکل رایج:
cv2.imshow(winname, img)

winname: نام پنجره (رشته)
img: آرایه تصویری

کنترل پنجره:
cv2.waitKey(0)           → صبر تا زدن کلید
cv2.waitKey(2000)        → نمایش ۲ ثانیه
cv2.destroyAllWindows()  → بستن همه پنجره‌ها

تنظیم اندازه پنجره برای رفع زوم‌شدگی:
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", width, height)

مثال نمایش یک تصویر:
cv2.imshow("My Image", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()

مثال نمایش چند تصویر:
cv2.imshow("small blur", small_blur)
cv2.imshow("medium blur", medium_blur)
cv2.imshow("extra blur", extra_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

==================================================================
✅ ۳. تبدیل رنگ تصویر — cv2.cvtColor()
==================================================================
شکل رایج:
converted_img = cv2.cvtColor(img, code)

پارامترها:
img: تصویر ورودی
code: کد تبدیل رنگ

کدهای پرکاربرد:
cv2.COLOR_BGR2GRAY  → رنگی به خاکستری
cv2.COLOR_BGR2RGB   → BGR به RGB (برای نمایش با Matplotlib)
cv2.COLOR_GRAY2BGR  → خاکستری به رنگی (۳ کاناله)

مثال:
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

سوال مهم: چه زمانی تصویر را با فلگ متفاوت بخوانیم و کی تبدیل کنیم؟

۱. فایل محلی روی SSD سریع: خواندن با فلگ متفاوت (حذف سربار تبدیل CPU)
۲. Raspberry Pi / SD Card کند: یک بار خواندن + cvtColor (خواندن از RAM سریع‌تر است)
۳. استریم دوربین / ویدئو: cvtColor اجباری (فقط یک فریم داریم)
۴. تصویر از قبل در حافظه: cvtColor اجباری (imread معنی ندارد)
۵. فایل روی شبکه (NAS/Cloud): یک بار خواندن + cvtColor
۶. پردازش بلادرنگ (Real-time): یک بار خواندن + cvtColor
۷. پردازش دسته‌ای روی SSD: خواندن با فلگ متفاوت (استفاده از کش سیستم‌عامل)

==================================================================
✅ ۴. ذخیره تصویر — cv2.imwrite()
==================================================================
شکل رایج:
cv2.imwrite(filename, img)

filename: مسیر و نام فایل با پسوند (می‌تواند فقط اسم فایل باشد یا مسیر کامل)
img: تصویر مورد نظر برای ذخیره

مثال ساده:
cv2.imwrite("gray_image.jpg", img_gray)

مثال با مسیر کامل:
cv2.imwrite(r"E:\\...\\Output\\lamborghini.jpg", img)

ساخت مسیر خروجی امن با pathlib:
from pathlib import Path

output = Path(r"E:\\...\\Output")
output.mkdir(parents=True, exist_ok=True)  # اگر پوشه نبود، می‌سازد
cv2.imwrite(output / f"resized_{name}.jpg", resized)

نکته: Path باید شکسته شود (پرانتز و اینتر):
output = Path(
    r"E:\\...\\Output"
)

==============================================================================
✅ ۵. تغییر اندازه — cv2.resize()
==============================================================================
شکل رایج با ابعاد دقیق:
resized = cv2.resize(img, (width, height))

شکل رایج با ضرایب مقیاس:
resized = cv2.resize(img, dsize=None, fx=0.6, fy=0.6)

پارامترها:
dsize: تاپل ابعاد خروجی (width, height). اگر None باشد باید از fx و fy استفاده کرد.
fx, fy: ضرایب مقیاس افقی و عمودی. مثال: fx=0.6 یعنی عرض ۶۰٪ اولیه.
interpolation: روش درون‌یابی.
    cv2.INTER_AREA    → بهترین برای کوچک‌سازی (پیشنهادی)
    cv2.INTER_LINEAR  → پیش‌فرض
    cv2.INTER_CUBIC   → بهترین برای بزرگ‌نمایی
    cv2.INTER_NEAREST → سریع (برای ماسک و باینری)

مثال — روش ساده (بدون حفظ نسبت):
resized = cv2.resize(img_color, (400, 300))

مثال — روش استاندارد (با حفظ نسبت):
h, w = img.shape[:2]
new_w = 400
new_h = int((h * new_w) / w)
resized = cv2.resize(img, (new_w, new_h))

==============================================================================
✅ ۶. برش تصویر — Crop / ROI
==============================================================================
ROI = Region of Interest = ناحیه مورد نظر

شکل رایج:
roi = img[y1:y2, x1:x2]

انواع برش:

۱. برش ۵۰٪ مرکزی (مناسب برای پردازش دسته‌ای):
h, w = img.shape[:2]
roi = img[h // 4 : 3 * h // 4, w // 4 : 3 * w // 4]

۲. برش دلخواه:
roi = img[100:300, 200:450]   → برش مستطیلی
roi = img[50:250, :]          → فقط برش عمودی
roi = img[:, 100:350]         → فقط برش افقی

نکته برای یافتن مختصات: تصویر را در Paint ویندوز باز کنید و مختصات پیکسلی موس را بخوانید.

مثال کامل:
roi = img_color[42:366, 301:534]
cv2.imshow("ROI", roi)

==============================================================================
✅ ۷. چرخش تصویر — Rotate
==============================================================================

الف) چرخش‌های ۹۰ درجه (ساده — مناسب پردازش دسته‌ای):
سه حالت:
rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
rotated = cv2.rotate(img, cv2.ROTATE_180)
rotated = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

------------------------------------------------------------------------

ب) چرخش با زاویه دلخواه (پیشرفته — ۴ مرحله):

مرحله ۱: ساخت ماتریس چرخش
h, w = img.shape[:2]
center = (w // 2, h // 2)
angle = 30    # مثبت → پادساعتگرد
scale = 1.0   # 1 = بدون تغییر اندازه
M = cv2.getRotationMatrix2D(center, angle, scale)

# ساختار ماتریس M (همیشه ۲×۳):
# [ cosθ   sinθ   tx ]
# [ -sinθ  cosθ   ty ]
# tx, ty: مولفه‌های انتقال (Translation vectors)

مرحله ۲: محاسبه ابعاد جدید (جلوگیری از بریدگی گوشه‌ها)
theta = np.radians(angle)
new_w = int(h * np.sin(theta) + w * np.cos(theta))
new_h = int(h * np.cos(theta) + w * np.sin(theta))

مرحله ۳: اصلاح مرکز ماتریس
M[0, 2] += (new_w - w) // 2  # جابه‌جایی افقی
M[1, 2] += (new_h - h) // 2  # جابه‌جایی عمودی

مرحله ۴: اعمال چرخش
rotated = cv2.warpAffine(img, M, (new_w, new_h))

مثال کامل:
img = cv2.imread(path)
h, w = img.shape[:2]
center = (w // 2, h // 2)
angle = 30
M = cv2.getRotationMatrix2D(center, angle, 1.0)

theta = np.radians(angle)
new_w = int(h * np.sin(theta) + w * np.cos(theta))
new_h = int(h * np.cos(theta) + w * np.sin(theta))

M[0, 2] += (new_w - w) // 2
M[1, 2] += (new_h - h) // 2

rotated = cv2.warpAffine(img, M, (new_w, new_h))

==============================================================================
✅ ۸. وارونه‌سازی — cv2.flip()
==============================================================================
شکل رایج:
flipped = cv2.flip(img, flipCode)

flipCode = 0  → عمودی (دور محور x)
flipCode = 1  → افقی - آینه‌ای (دور محور y)
flipCode = -1 → عمودی و افقی (معادل چرخش ۱۸۰°)

مثال:
flip_horizontal = cv2.flip(img, 1)
flip_vertical = cv2.flip(img, 0)
flip_both = cv2.flip(img, -1)

==============================================================================
✅ ۹. قاعده کلی ابعاد در OpenCV
==============================================================================
روش حفظ کردن:
img[row, col]  →  img[y, x]
size = (width, height)  →  (x, y)

قاعده:
هر جا size می‌دهیم → اول = عرض (width)
  cv2.resize(img, (width, height))
  cv2.warpAffine(img, M, (width, height))

هر جا از img.shape می‌گیریم → اول = ارتفاع (height)
  img.shape → (height, width, channels)
  h, w = img.shape[:2]

==============================================================================
✅ ۱۰. ماتریس‌های تبدیل
==============================================================================

۱. ماتریس انتقال (Translation):
M = np.float32([[1, 0, tx], [0, 1, ty]])
translated = cv2.warpAffine(img, M, (w, h))

۲. ماتریس تغییر مقیاس (Scaling):
resized = cv2.resize(img, None, fx=sx, fy=sy)

۳. ماتریس چرخش (Rotation):
M = cv2.getRotationMatrix2D(center, angle, scale)
rotated = cv2.warpAffine(img, M, (new_w, new_h))

۴. ماتریس برش (Shear):
M = np.float32([[1, k, 0], [0, 1, 0]])
sheared = cv2.warpAffine(img, M, (w, h))

۵. ماتریس آفین (Affine):
M = cv2.getAffineTransform(pts1, pts2)
warped = cv2.warpAffine(img, M, (w, h))

۶. ماتریس پرسپکتیو (Perspective):
M = cv2.getPerspectiveTransform(pts1, pts2)
warped = cv2.warpPerspective(img, M, (w, h))

====================================================
📝 کاربرد Matplotlib در OpenCV
====================================================
# استفاده از Matplotlib برای نمایش و رسم نمودار

img = cv2.imread("example.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 100, 200)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

--------------------------------------------------
۱. نمایش یک تصویر تکی
--------------------------------------------------
plt.figure(figsize=(8, 6))
plt.imshow(img_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

# ذخیره: خروجی عکس خام است → cv2.imwrite()
cv2.imwrite("output_image.jpg", img)

--------------------------------------------------
۲. نمایش تصویر خاکستری با نقشه رنگی مشخص
--------------------------------------------------
plt.figure(figsize=(8, 6))
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

# ذخیره: خروجی عکس خاکستری است → cv2.imwrite()
cv2.imwrite("output_gray.jpg", gray)

--------------------------------------------------
۳. نمایش چند تصویر در کنار هم (Subplot)
--------------------------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

axes[0].imshow(img_rgb)
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(gray, cmap="gray")
axes[1].set_title("Grayscale")
axes[1].axis("off")

axes[2].imshow(edges, cmap="gray")
axes[2].set_title("Canny Edges")
axes[2].axis("off")

plt.tight_layout()
plt.show()

# ذخیره گزارش (چون تیتر و چیدمان دارد): Matplotlib
fig.savefig("multipix.png", dpi=300, bbox_inches="tight")

# ذخیره برای پردازش مجدد (کلاژ): OpenCV
collage = np.hstack((img, cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR),
                     cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)))
cv2.imwrite("collage_for_processing.png", collage)

--------------------------------------------------
۴. نمایش و ذخیره‌سازی کلاژ (گزارشی)
--------------------------------------------------
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

# ذخیره: حتماً Matplotlib (چون تیتر و سوپ‌تایتل دارد)
plt.savefig("before_after.png", dpi=200, bbox_inches="tight")

--------------------------------------------------
۵. رسم هیستوگرام تصویر خاکستری
--------------------------------------------------
plt.figure(figsize=(10, 5))
plt.hist(gray.ravel(), bins=256, range=[0, 256], color="black")
plt.title("Grayscale Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)
plt.show()

# ذخیره: حتماً Matplotlib (خروجی نمودار است، نه عکس)
plt.savefig("histogram_gray.png", dpi=150, bbox_inches="tight")

--------------------------------------------------
۶. رسم هیستوگرام کانال‌های رنگی جداگانه
--------------------------------------------------
colors = ("b", "g", "r")
plt.figure(figsize=(10, 5))

for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col, label=f"Channel {col.upper()}")

plt.title("RGB Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# ذخیره: حتماً Matplotlib
plt.savefig("histogram_rgb.png", dpi=150, bbox_inches="tight")

--------------------------------------------------
۷. نمایش تصویر به همراه هیستوگرام در یک فیگور
--------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

ax1.imshow(img_rgb)
ax1.set_title("Image")
ax1.axis("off")

ax2.hist(gray.ravel(), bins=256, range=[0, 256], color="gray")
ax2.set_title("Histogram")
ax2.set_xlabel("Intensity")
ax2.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# ذخیره: حتماً Matplotlib
fig.savefig("image_with_histogram.png", dpi=150, bbox_inches="tight")

--------------------------------------------------
۸. رسم پروفایل شدت نور روی یک خط (Line Profile)
--------------------------------------------------
line_y = gray.shape[0] // 2
intensity_profile = gray[line_y, :]

plt.figure(figsize=(12, 4))
plt.plot(intensity_profile, color="blue", linewidth=0.8)
plt.title(f"Intensity Profile at y = {line_y}")
plt.xlabel("X Position")
plt.ylabel("Intensity")
plt.grid(alpha=0.3)
plt.show()

# ذخیره: حتماً Matplotlib
plt.savefig("line_profile.png", dpi=150, bbox_inches="tight")

--------------------------------------------------
۹. نمایش ماتریس اعداد به صورت Heatmap
--------------------------------------------------
feature_map = cv2.resize(gray, (50, 50))

plt.figure(figsize=(8, 6))
plt.imshow(feature_map, cmap="hot", interpolation="nearest")
plt.colorbar(label="Intensity")
plt.title("Feature Map / Heatmap")
plt.axis("off")
plt.show()

# ذخیره گزارش (با colorbar): Matplotlib
plt.savefig("heatmap.png", dpi=150, bbox_inches="tight")

# ذخیره داده خام: OpenCV
cv2.imwrite("feature_map_raw.png", feature_map)

--------------------------------------------------
۱۰. نمایش مراحل مختلف یک پایپلاین پردازشی
--------------------------------------------------
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

# ذخیره: Matplotlib (نمای کلی فرآیند)
fig.savefig("pipeline_steps.png", dpi=150, bbox_inches="tight")

--------------------------------------------------
خلاصه قوانین ذخیره‌سازی:
--------------------------------------------------
- فقط عکس خام (بدون نمودار/تیتر) → cv2.imwrite()
- هر چیزی که نمودار، هیستوگرام، یا چند subplot دارد → plt.savefig()
- کلاژ عکس برای پردازش مجدد → با np.hstack بسازید و cv2.imwrite() کنید

====================================================
📝 الگوی کامل پروژه ترکیبی (نمونه اجرایی)
====================================================

def sample_project_pipeline(path):
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
    img_resized = cv2.resize(img, (new_w, new_h))

    # ۴. برش — یک‌چهارم مرکزی تصویر
    h_r, w_r = img_resized.shape[:2]
    roi = img_resized[h_r//4 : 3*h_r//4, w_r//4 : 3*w_r//4]

    # ۵. چرخش ROI
    angle = 30
    h_c, w_c = roi.shape[:2]
    center = (w_c // 2, h_c // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
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

# sample_project_pipeline("your_image_path.jpg")

====================================================
📝 راهنمای استفاده از pathlib
====================================================
import cv2
from pathlib import Path
p = print

# برای یک تصویر تکی:
path = r"E:\\...\\Data\\input\\cow.jpg"
image = cv2.imread(path)

# برای تصاویر زیاد (منطقی‌تر):
folder = Path(r"E:\\...\\Data\\input")
pathes = [str(i) for i in folder.glob("*.jpg")]

for i in pathes:
    img = cv2.imread(i)
    name = Path(i).stem  # نام فایل بدون پسوند
    # پردازش تصویر...
    cv2.imwrite(output / f"processed_{name}.jpg", img)

# کد معادل استخراج نام (بدون pathlib):
# name = i.split("\\\\")[-1].split(".")[0]

--------------------------------------------------
بررسی آمادگی تصاویر
--------------------------------------------------
# ۱. آمادگی فنی (Image Processing Ready):
# ✅ تصویر خوانده می‌شود
# ✅ تغییر اندازه/برش/چرخش انجام می‌شود
# ✅ ذخیره خروجی انجام می‌شود

# ۲. آمادگی دیتاست برای مدل (Model Training Ready):
# ✅ اندازه استاندارد
# ✅ کانال‌های رنگ یکسان
# ✅ نور و کیفیت قابل قبول
# ✅ تنوع مناسب
# ✅ کلاس‌های متعادل
# ✅ حذف تصاویر خراب و تکراری

--------------------------------------------------
غربالگری تصاویر با انحراف معیار (کنتراست):
--------------------------------------------------
# اگر np.std(img) > 40 باشد → کنتراست خوب
# این معیار می‌تواند ۷۰-۸۰٪ تصاویر نامناسب را فیلتر کند

for i in pathes:
    img = cv2.imread(i, 0)
    if img is None:
        continue
    if np.std(img) > 60:
        name = Path(i).stem
        cv2.imshow(f"{name}_win", img)
        cv2.waitKey(0)

# ============================================================
🎨 فیلترها، آستانه‌گذاری و تشخیص لبه — Week 04
# ============================================================

import cv2
import numpy as np
from pathlib import Path
p = print

# ============================================================
✅ ۱. فیلتر Gaussian — کاهش نویز نرم
# ============================================================

شکل رایج:
blurred = cv2.GaussianBlur(img, ksize, sigmaX)

پارامترها:
img: تصویر ورودی (رنگی یا خاکستری)
ksize: اندازه کرنل — تاپل (width, height) — هر دو باید فرد باشند
       والیوهای رایج: (3,3) کم, (5,5) متوسط, (9,9) زیاد
sigmaX: انحراف معیار افقی. اگر 0 بدهید، OpenCV خودش از روی ksize حساب می‌کند (پیشنهادی)
sigmaY: انحراف معیار عمودی. پیش‌فرض 0 یعنی برابر با sigmaX (معمولاً تغییر نمی‌دهیم)

حالت اول (پیشنهادی): ksize دارید, sigmaX=0
حالت دوم: ksize=(0,0) می‌دهید, sigmaX را دستی تعیین می‌کنید

مثال:
img = cv2.imread(path)

small_blur = cv2.GaussianBlur(img, (3, 3), 0)
medium_blur = cv2.GaussianBlur(img, (5, 5), 0)
extra_blur = cv2.GaussianBlur(img, (9, 9), 0)

cv2.imshow("small blur (3,3)", small_blur)
cv2.imshow("medium blur (5,5)", medium_blur)
cv2.imshow("extra blur (9,9)", extra_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()

output = Path(r"E:\\...\\Output")
output.mkdir(parents=True, exist_ok=True)
cv2.imwrite(str(output / "man_small_blur.jpg"), small_blur)
cv2.imwrite(str(output / "man_medium_blur.jpg"), medium_blur)
cv2.imwrite(str(output / "man_extra_blur.jpg"), extra_blur)

# ============================================================
✅ ۲. فیلتر Median — حذف نویز نمک-فلفل
# ============================================================

شکل رایج:
median = cv2.medianBlur(img, ksize)

پارامترها:
img: تصویر ورودی (رنگی یا خاکستری)
ksize: اندازه کرنل — یک عدد فرد (نه تاپل! برخلاف Gaussian)
       والیوهای رایج: 3 (کم), 5 (متوسط، پیشنهادی), 9 (زیاد)

مقایسه با Gaussian:
Gaussian = میانگین وزن‌دار پیکسل‌های همسایه → نویز پخش می‌شود → لبه‌ها محو
Median   = میانه آماری پیکسل‌های همسایه → نویز حذف می‌شود → لبه‌ها تیز

مثال:
img = cv2.imread(path)

ksizes = [3, 5, 9]
for k in ksizes:
    gaussian = cv2.GaussianBlur(img, (k, k), 0)
    median = cv2.medianBlur(img, k)

    output = Path(r"E:\\...\\Output")
    output.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output / f"chaplin_gaussian_{k}.jpg"), gaussian)
    cv2.imwrite(str(output / f"chaplin_median_{k}.jpg"), median)

# ============================================================
✅ ۳. Thresholding ساده — آستانه‌گذاری سراسری
# ============================================================

شکل رایج:
ret, dst = cv2.threshold(src, thresh, maxval, type)

پارامترها:
src: تصویر ورودی — باید Grayscale باشد (تک کاناله)
thresh: عدد آستانه (0 تا 255)
        والیوهای رایج: 50 (روشن), 127 (متوسط، رایج‌ترین), 200 (تیره)
        thresh کم = تصویر سفیدتر | thresh زیاد = تصویر سیاه‌تر
maxval: مقدار پیکسل‌های عبورکرده از آستانه — معمولاً 255
type: نوع آستانه‌گذاری
      cv2.THRESH_BINARY      → بالای آستانه = maxval, پایین = 0 (پیشفرض ذهنی)
      cv2.THRESH_BINARY_INV  → معکوس حالت بالا
      cv2.THRESH_TRUNC       → بالای آستانه = خود آستانه, پایین = بدون تغییر
      cv2.THRESH_TOZERO      → بالای آستانه = بدون تغییر, پایین = 0

خروجی:
ret → همان مقدار thresh استفاده‌شده
dst → تصویر باینری شده

مثال:
img = cv2.imread(path)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

tresh_list = [50, 127, 200]
for t in tresh_list:
    ret, th = cv2.threshold(grey, t, 255, cv2.THRESH_BINARY)

    output = Path(r"E:\\...\\Output")
    output.mkdir(parents=True, exist_ok=True)
    cv2.imwrite(str(output / f"huawei_thresh_{t}.jpg"), th)

# ============================================================
✅ ۴. Adaptive Thresholding — آستانه‌گذاری تطبیقی
# ============================================================

شکل رایج:
dst = cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)

پارامترها (هر ۶ پارامتر اجباری هستند):
src: تصویر ورودی — باید Grayscale باشد
maxValue: مقدار پیکسل‌های سفید — معمولاً 255
adaptiveMethod:
    cv2.ADAPTIVE_THRESH_MEAN_C     → میانگین ساده همسایه‌ها
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C → میانگین وزن‌دار (بهتر، پیشنهادی)
thresholdType: معمولاً cv2.THRESH_BINARY
blockSize: اندازه ناحیه بررسی — یک عدد فرد
           والیوهای رایج: 11 (جزئیات بیشتر), 21 (نرم‌تر، پیشنهادی برای متون)
C: ثابت تصحیح — از میانگین محلی کم می‌شود
   والیوهای رایج: 2 (پیشفرض ذهنی), 3 (معمولی), 7 (خطوط پیوسته‌تر)
   بزرگتر = تصویر تیره‌تر و خطوط پیوسته‌تر

نکته — رفتار شبه‌کنی:
هرچه C بزرگتر ← پیوستگی خطوط بیشتر
هرچه blockSize کوچکتر ← خطوط باریکتر
در برخی تصاویر: adaptiveThreshold با C بالا و blockSize پایین
عملکردی مشابه Canny پیدا می‌کند

مثال:
img = cv2.imread(path, 0)

# آستانه‌گذاری ساده برای مقایسه
_, simple_thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# آستانه‌گذاری تطبیقی
adaptive_thresh = cv2.adaptiveThreshold(
    img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    21,  # blockSize
    3    # C
)

output = Path(r"E:\\...\\Output")
output.mkdir(parents=True, exist_ok=True)
cv2.imwrite(str(output / "simple_threshold_panther.jpg"), simple_thresh)
cv2.imwrite(str(output / "adaptive_threshold_panther.jpg"), adaptive_thresh)

# ============================================================
✅ ۵. تشخیص لبه — Canny Edge Detection
# ============================================================

شکل رایج:
edges = cv2.Canny(img, threshold1, threshold2)

پارامترها:
img: تصویر ورودی — ترجیحاً Grayscale
threshold1: حد پایین (minVal) — برای هیسترزیس
threshold2: حد بالا (maxVal) — برای هیسترزیس
            نسبت پیشنهادی: 1:2 یا 1:3 (مثلاً 50:150, 80:200, 80:240)
            بهترین مقادیر تجربی: (50,150) (80,200) (80,240)

منطق هیسترزیس Canny:
- اگر گرادیان > threshold2 → قطعاً لبه
- اگر گرادیان < threshold1 → قطعاً غیرلبه
- اگر بین این دو → لبه است فقط اگر به یک لبه قطعی متصل باشد

قانون طلایی: همیشه قبل از Canny بلور کن!

مثال:
folder = Path(r"E:\\...\\Data")
paths = [str(i) for i in folder.glob("*.jpg")]

thresholds = [(50, 150), (80, 200), (80, 240)]

for i in paths:
    img = cv2.imread(i, 0)
    if img is None:
        continue
    if np.std(img) > 50:  # غربالگری با کنتراست
        for minval, maxval in thresholds:
            # بدون بلور (نادرست)
            edge_raw = cv2.Canny(img, minval, maxval)
            # با بلور (صحیح)
            blurred = cv2.GaussianBlur(img, (5, 5), 0)
            edge_clean = cv2.Canny(blurred, minval, maxval)

            cv2.imshow(f"{minval}_{maxval}_raw", edge_raw)
            cv2.imshow(f"{minval}_{maxval}_clean", edge_clean)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

# ============================================================
✅ ۶. پایپلاین‌ها — قوانین و الگوها
# ============================================================

تعریف پایپلاین:
زنجیره‌ای از مراحل متوالی که خروجی هر مرحله = ورودی مرحله بعد

قانون اول — ترتیب Gray و Blur:
همیشه Gray را قبل از Blur انجام بده (پردازش Blur روی ۱ کانال سریع‌تر از ۳ کانال است)
✅ img >> gray >> blur
❌ img >> blur >> gray

قانون دوم — جدا بودن مسیر Threshold و Canny:
هدف Threshold = جداسازی و بخش‌بندی (Segmentation)
هدف Canny = تشخیص لبه و ویژگی (Edge Detection)
این دو هدف متفاوت دارند — در یک مسیر خطی قرار نمی‌گیرند

قانون سوم — Canny را روی Threshold نزن:
❌ blur >> threshold >> Canny
Threshold نویز تضعیف‌شده توسط Blur را دوباره تشدید می‌کند

قانون چهارم — Threshold را روی Canny نزن:
❌ blur >> Canny >> threshold
Canny خودش نوعی Threshold داخلی دارد (هیسترزیس)

نتیجه — دو مسیر موازی از یک ریشه:
پایپلاین اصلی (مشترک):
img >> gray >> blur
                  >> branch a) threshold >> save    (بخش‌بندی)
                  >> branch b) Canny >> save        (تشخیص لبه)

پایپلاین‌های استاندارد:
پایپلاین ۱: تشخیص لبه (تصاویر طبیعی)
    img >> gray >> GaussianBlur(5,5) >> Canny(50,150)

پایپلاین ۲: نویز نمک-فلفل
    img >> gray >> MedianBlur(5) >> Canny(50,150)

پایپلاین ۳: بخش‌بندی (Segmentation)
    img >> gray >> GaussianBlur(5,5) >> threshold(127) / adaptiveThreshold(...)

# ============================================================
✅ ۷. پایپلاین کامل — Mini Project با پایپلاین اصلاح‌شده
# ============================================================

folder = Path(r"E:\\...\\Data")
paths = [str(i) for i in folder.glob("*.jpg")]

for i in paths:
    # ۱. خواندن تصویر به صورت خاکستری
    img = cv2.imread(i, 0)
    if img is None:
        p(f"error reading: {i}")
        continue

    if np.std(img) > 50:
        # ۲. بلور کردن
        blurred = cv2.GaussianBlur(img, (5, 5), 0)

        # ۳. انشعاب a — آستانه‌گذاری (بخش‌بندی)
        _, simple_th = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY)
        adaptive_th = cv2.adaptiveThreshold(
            blurred, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11,  # blockSize
            7    # C — خطوط پیوسته‌تر
        )

        # ۴. انشعاب b — تشخیص لبه (روی blur، نه روی threshold!)
        thresholds = [(50, 150), (80, 200), (80, 240)]
        for minval, maxval in thresholds:
            edge = cv2.Canny(blurred, minval, maxval)

            # ۵. ذخیره خروجی‌ها
            output = Path(r"E:\\...\\Output")
            output.mkdir(parents=True, exist_ok=True)

            name = Path(i).stem
            cv2.imwrite(str(output / f"{name}_simple_threshold.jpg"), simple_th)
            cv2.imwrite(str(output / f"{name}_adaptive_threshold.jpg"), adaptive_th)
            cv2.imwrite(str(output / f"{name}_{minval}_{maxval}_canny.jpg"), edge)

# ============================================================
📌 خلاصه نهایی مفاهیم
# ============================================================

Gaussian Blur:
    فرمول: cv2.GaussianBlur(img, ksize, sigmaX)
    ksize = (فرد, فرد) | sigmaX=0 یعنی خودکار
    کاربرد: کاهش نویز عمومی، پیش‌پردازش قبل از Canny

Median Blur:
    فرمول: cv2.medianBlur(img, ksize)
    ksize = عدد فرد (نه تاپل)
    کاربرد: نویز نمک-فلفل

Simple Threshold:
    فرمول: ret, dst = cv2.threshold(src, thresh, maxval, type)
    src = Grayscale | thresh = 0 تا 255 | maxval = معمولاً 255
    کاربرد: تصاویر با نور یکنواخت

Adaptive Threshold:
    فرمول: dst = cv2.adaptiveThreshold(src, maxValue, method, type, blockSize, C)
    هر ۶ پارامتر اجباری | blockSize = عدد فرد | C = ثابت تصحیح
    کاربرد: تصاویر با نور غیریکنواخت (سایه‌دار)

Canny Edge:
    فرمول: edges = cv2.Canny(img, threshold1, threshold2)
    نسبت threshold1:threshold2 = 1:2 یا 1:3
    بهترین مقادیر تجربی: (50,150) (80,200) (80,240)
    قانون طلایی: همیشه قبل از Canny بلور کن

قوانین پایپلاین:
    ۱. Gray قبل از Blur (بهینه‌تر)
    ۲. Threshold و Canny هدف متفاوت دارند — در یک مسیر خطی نیستند
    ۳. Canny روی Threshold نزن (نویز تشدید می‌شود)
    ۴. Threshold روی Canny نزن (بی‌تأثیر است)
    الگوی صحیح: img >> gray >> blur >> [انشعاب a: threshold] [انشعاب b: Canny]

==============================================================
الگوریتم سیفت برای تشخیص نقاط کلیدی تصاویر
==============================================================
الگوی کامل SIFT:

sift = cv2.SIFT_create()                      # ساخت شیء SIFT
keypoints, descriptor = sift.detectAndCompute(img, None)  # تشخیص نقاط + توصیفگر
sift_result = cv2.drawKeypoints(img, keypoints, None)          # رسم نقاط روی تصویر
================================================================================
مثال کامل:
import cv2
import numpy as np
# ---------
img = cv2.imread("image.jpg", 0)
sift = cv2.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(img, None)
sift_result = cv2.drawKeypoints(img, keypoints, None)
# -----------
cv2.imshow("SIFT Keypoints", sift_result)
cv2.waitKey(0)
cv2.destroyAllWindows()

------------------------------------
بررسی اجزای هر سطر از الگوی سیفت
# ------------------------------
1. sift = cv2.SIFT_create()

متغیر sift: شیء الگوریتم سیفت با تمام متدهایش.

شکل رایج:
sift = cv2.SIFT_create()

پارامترهای اختیاری (همه پیش‌فرض مناسب دارند، در شکل رایج فرمول نوشته نمی‌شوند):
nfeatures=0            → حداکثر تعداد نقاط (0=نامحدود)
nOctaveLayers=3        → تعداد لایه در هر اکتاو
contrastThreshold=0.04 → آستانه حذف نقاط ضعیف
edgeThreshold=10       → آستانه حذف نقاط لبه
sigma=1.6              → سیگمای گاوسین اولیه


================================================================================
2. keypoints, descriptor = sift.detectAndCompute(img, None)
================================================================================

متغیر keypoints: لیستی از اشیاء KeyPoint (هر کدام شامل pt، size، angle، response، octave)
متغیر descriptor: آرایه NumPy با شکل (تعداد_نقاط, 128) و نوع float32

شکل رایج:
keypoints, descriptor = sift.detectAndCompute(img, None)

پارامترها به ترتیب:
۱. image         → img (تصویر خاکستری - تنها پارامتر اجباری)
۲. mask          → None که اینجاست (ناحیه جستجو - پیش‌فرض None یعنی کل تصویر)
۳. descriptors   → نوشته نمی‌شود، پیش‌فرض None یعنی خودش آرایه جدید بسازد


دقت کن: None که در شکل رایج نوشته شده، مربوط به پارامتر دوم یعنی mask است.
یعنی sift.detectAndCompute(img, None):
  img    ← آرگومان اول = پارامتر image
  None   ← آرگومان دوم = پارامتر mask (نه descriptors!)


================================================================================
3. sift_result = cv2.drawKeypoints(img, keypoints, None)
================================================================================

متغیر sift_result: تصویر جدید (آرایه NumPy) که نقاط روی آن رسم شده‌اند.

شکل رایج:
sift_result = cv2.drawKeypoints(img, keypoints, None)

پارامترها به ترتیب:
۱. image     → img (تصویر منبع)
۲. keypoints → keypoints (لیست نقاط)
۳. outImage  → None که اینجاست (تصویر مقصد - پیش‌فرض None یعنی تصویر جدید بساز)
۴. color     → نوشته نمی‌شود، پیش‌فرض: رنگ تصادفی
۵. flags     → نوشته نمی‌شود، پیش‌فرض: فقط دایره کوچک مرکز نقطه


دقت کن: None که در شکل رایج نوشته شده، مربوط به پارامتر سوم یعنی outImage است.
یعنی cv2.drawKeypoints(img, keypoints, None):
  img       ← آرگومان اول = پارامتر image
  keypoints ← آرگومان دوم = پارامتر keypoints
  None      ← آرگومان سوم = پارامتر outImage


================================================================================
متدهای دیگر sift:
================================================================================

الف) sift.detect(img, None) — فقط تشخیص نقاط کلیدی
keypoints = sift.detect(img, None)
پارامتر ۱: image ← img
پارامتر ۲: mask  ← None (همینجاست - پیش‌فرض: کل تصویر)


ب) sift.compute(img, keypoints) — فقط محاسبه توصیفگر
keypoints, descriptors = sift.compute(img, keypoints)
پارامتر ۱: image       ← img
پارامتر ۲: keypoints   ← keypoints
پارامتر ۳: descriptors ← نوشته نمی‌شود، پیش‌فرض None (خودش آرایه جدید بسازد)


================================================================================
خلاصه محل دقیق هر None:
================================================================================

sift.detectAndCompute(img, None)
                         ^^^^
                         این None = mask (پارامتر دوم)
                         پارامتر سوم descriptors اصلاً نوشته نمی‌شود

cv2.drawKeypoints(img, keypoints, None)
                                  ^^^^
                                  این None = outImage (پارامتر سوم)
                                  پارامترهای color و flags اصلاً نوشته نمی‌شوند


================================================================================
مقایسه: تشخیص و توصیف یک‌مرحله‌ای (detectAndCompute) در مقابل دو‌مرحله‌ای (detect + compute)
================================================================================

روش یک‌مرحله‌ای: تشخیص و توصیف همزمان با detectAndCompute (رایج و سریع‌تر)
sift = cv2.SIFT_create()
keypoints, descriptor = sift.detectAndCompute(img, None)   ← None = mask
sift_result = cv2.drawKeypoints(img, keypoints, None)           ← None = outImage

روش دو‌مرحله‌ای: تشخیص با detect سپس توصیف با compute (برای کنترل بیشتر)
sift = cv2.SIFT_create()
keypoints = sift.detect(img, None)                         ← None = mask
keypoints, descriptor = sift.compute(img, keypoints)       ← بدون None
sift_result = cv2.drawKeypoints(img, keypoints, None)           ← None = outImage

نکته: روش یک‌مرحله‌ای سریع‌تر است چون بعضی محاسبات میانی را یک بار انجام می‌دهد
و از نتیجه برای هر دو مرحله استفاده می‌کند. روش دو‌مرحله‌ای زمانی به کار می‌آید
که بخواهید بین تشخیص و توصیف، نقاط کلیدی را فیلتر یا مرتب کنید.
'''