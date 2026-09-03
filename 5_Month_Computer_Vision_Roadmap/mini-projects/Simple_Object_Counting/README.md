
# 💠 Simple Object Counting

A classical OpenCV pipeline that counts multiple separate objects placed on a simple background in an image, using thresholding, morphology, and contour detection — no HSV, no Watershed, no deep learning.

پای‌پلاینی کلاسیک با OpenCV برای شمارش چند شیء جدا از هم روی یک پس‌زمینه ساده، فقط با Threshold، Morphology و Contour — بدون HSV، بدون Watershed، بدون یادگیری عمیق.



## 📁 Dataset

**English:**
A self-collected dataset was created for this project, because most publicly available datasets (bottles with clustered/touching balls, pre-cropped single-coin images, etc.) did not match the requirement.

**Requirement:** Multiple, clearly separated (non-touching) objects on a simple background, so contours can be drawn individually.

**فارسی:**
برای این پروژه یک دیتاست شخصی ساخته شد، چون اکثر دیتاست‌های آماده (بطری با گوی‌های چسبیده، عکس‌های تک‌سکه‌ای از قبل جداشده و…) با نیاز این پروژه سازگار نبودن.

**نیاز پروژه:** چند شیء مجزا و کاملاً جدا از هم (بدون چسبیدگی) روی یک پس‌زمینه ساده، تا کانتور هر شیء جدا قابل رسم باشه.



## 🔧 Pipeline

Read Image → Grayscale → Adaptive Threshold → Opening → Dilation → Find Contours → Filter by Area → Draw Boxes → Save Result



## 🧱 Code Structure

**English:**
The project is written in a function-based style rather than one long loop:

| Function | Description |
|-|-|
| `preprocess(img)` | Grayscale conversion, Adaptive Threshold, Opening, Dilation |
| `find_objects(dilated)` | Contour detection and area-based filtering |
| `draw_boxes(img, contours)` | Draws a bounding box per detected object and the total count on the image |

The main loop only reads each image, calls the three functions above in order, and saves the result.

**فارسی:**
کد به‌صورت تابع‌محور نوشته شده، نه یک حلقه یک‌تکه:

| تابع | توضیح |
||-|
| `preprocess(img)` | تبدیل به خاکستری، Adaptive Threshold، Opening، Dilation |
| `find_objects(dilated)` | پیدا کردن کانتورها و فیلتر بر اساس مساحت |
| `draw_boxes(img, contours)` | رسم یک Bounding Box برای هر شیء تشخیص‌داده‌شده به‌همراه عدد کل شمارش روی تصویر |

حلقه اصلی فقط هر تصویر رو می‌خونه، سه تابع بالا رو به ترتیب صدا می‌زنه، و نتیجه رو ذخیره می‌کنه.



## 📂 Project Structure

Simple_Object_Counting/
├── data/                    # Input images (.jpg)
├── output/                  # Processed comparison images
├── main.py                  # Main script
├── README.md                # Project documentation
└── soc_requirements.txt     # Required libraries



## 📦 Requirements

Install dependencies:

pip install -r soc_requirements.txt



## 🚀 Usage

Run the main script:

python main.py



## 🔍 Pipeline Details

**English:**

- **Adaptive Threshold (Gaussian)** was used instead of a simple global threshold, because the images had uneven shadows/lighting.
- **Opening** with a soft kernel `(3, 3)` removes small noise without erasing the object edges.
- **Dilation** with a more aggressive kernel `(7, 7)` is applied afterward to reconnect and thicken the object shapes before contour detection.
- **Contours** are found with `RETR_EXTERNAL` (only outer boundaries).
- **Contour Filtering:** Contours are filtered by a minimum area threshold (`min_areas = 50000`), tuned manually per test image until the number of surviving contours matched the real object count in several sample images; that value was then applied as a fixed standard across all images.
- **Drawing:** For each surviving contour, a bounding box (`cv2.boundingRect`) is drawn on a copy of the original image, along with a text label showing the total detected count.
- **Note:** A conditional `CLAHE` branch is computed on low-contrast images (std below `50`) but is currently not fed into the thresholding step; it is kept in the code but has no effect yet on the final result.

**فارسی:**

- به‌جای Threshold ساده سراسری، از **Adaptive Threshold (نوع Gaussian)** استفاده شد، چون تصاویر سایه و نور نامتقارن داشتن.
- **Opening** با کرنل نرم `(3, 3)` نویزهای ریز رو حذف می‌کنه، بدون اینکه حاشیه اشیاء از بین بره.
- بعدش **Dilation** با کرنل تهاجمی‌تر `(7, 7)` اعمال می‌شه تا شکل اشیاء قبل از Contour Detection ضخیم‌تر و یکپارچه‌تر بشه.
- کانتورها با `RETR_EXTERNAL` پیدا می‌شن (فقط مرز بیرونی).
- **فیلتر کانتورها:** کانتورها با یک آستانه حداقل مساحت (`min_areas = 50000`) فیلتر می‌شن؛ این آستانه به‌صورت دستی و روی چند تصویر نمونه تنظیم شد تا تعداد کانتورهای باقی‌مانده با تعداد واقعی اشیاء برابر بشه، سپس همین عدد به‌عنوان استاندارد ثابت برای همه تصاویر اعمال شد.
- **رسم:** برای هر کانتور باقی‌مانده، یک Bounding Box (با `cv2.boundingRect`) روی یک کپی از تصویر اصلی رسم می‌شه، به‌همراه یک متن که تعداد کل تشخیص‌داده‌شده رو نشون می‌ده.
- **نکته:** یک شاخه شرطی `CLAHE` برای تصاویر کم‌کنتراست (انحراف معیار زیر ۵۰) محاسبه می‌شه، ولی فعلاً وارد مرحله Threshold نمی‌شه؛ در کد نگه داشته شده ولی فعلاً روی نتیجه نهایی تاثیری نداره.



## 📊 Analysis & Findings

**English:**

Overall, the pipeline correctly counted objects in about **70%** of the tested images.

Tuning the minimum area threshold manually was the most time-consuming and error-prone step: too low → dozens of spurious small contours; too high → real objects get filtered out.

In the remaining **~30%** of images, the following issues appeared:

- Touching objects were merged into a single contour, causing **undercounting**.
- Some objects were surrounded by two separate contours instead of one, causing **overcounting**.
- A few images produced no valid contour at all, so no box was drawn for those objects.
- In some cases the contour count was numerically correct, but the underlying contour did not cleanly follow the object's outer edge — it drifted into the object's internal details, which can make the resulting bounding box loosely fit the actual object shape.

Given that the objects in this dataset are fairly large and visually distinct, a **70% success rate** is considered a modest result rather than a strong one. The main issue is not the generalization of the area threshold itself, but that the contour does not always outline the object cleanly.

**فارسی:**

در مجموع، پایپ‌لاین برای حدود **۷۰٪** از تصاویر تست‌شده، شمارش درستی از اشیاء ارائه داد.

تنظیم دستی آستانه حداقل مساحت، وقت‌گیرترین و خطاپذیرترین مرحله کل پایپ‌لاین بود: خیلی پایین → ده‌ها کانتور کاذب و ریز؛ خیلی بالا → حذف شدن اشیاء واقعی از فیلتر.

در حدود **۳۰٪** باقی‌مانده تصاویر، این مشکلات دیده شد:

- اشیاء چسبیده به هم در یک کانتور واحد ادغام شدن و باعث **شمارش کمتر از واقعی (Undercounting)** شدن.
- بعضی اشیاء به‌جای یک کانتور، با دو کانتور جدا احاطه شده بودن که باعث **شمارش بیشتر از واقعی (Overcounting)** می‌شد.
- چند تصویر اصلاً هیچ کانتور معتبری تولید نکردن، پس برای اون اشیاء هیچ Bounding Box‌ای رسم نشد.
- در برخی موارد، تعداد کانتور از نظر عددی درست بود ولی خود کانتور به‌طور تمیز دور شیء رو دنبال نمی‌کرد و به جزئیات داخلی شیء می‌خزید، که باعث می‌شه Bounding Box نهایی به‌درستی روی شکل واقعی شیء منطبق نباشه.

با توجه به اینکه اشیاء این دیتاست نسبتاً بزرگ و از نظر بصری واضح هستن، نتیجه **۷۰٪** چندان قوی ارزیابی نمی‌شه. مشکل اصلی از تعمیم آستانه مساحت نیست، بلکه اینه که کانتور همیشه دور شیء رو تمیز رسم نمی‌کنه.



## ⚠️ Known Limitations

**English:**

- This pipeline relies entirely on classical thresholding and contour detection; it has no mechanism to separate objects that are touching or overlapping.
- The minimum-area filtering threshold is manually tuned and dataset-specific; it is not an adaptive or automatically generalizing parameter.
- The `CLAHE` branch in `preprocess` is currently computed but unused; contrast enhancement has no effect on the final thresholding step yet.

**فارسی:**

- این پایپ‌لاین کاملاً بر پایه Threshold و Contour کلاسیک است؛ هیچ مکانیزمی برای جدا کردن اشیاء چسبیده یا روی‌هم‌افتاده نداره.
- آستانه فیلتر حداقل مساحت به‌صورت دستی و مخصوص همین دیتاست تنظیم شده؛ یک پارامتر تطبیقی یا خودکار-تعمیم‌پذیر نیست.
- شاخه `CLAHE` در `preprocess` فعلاً محاسبه می‌شه ولی استفاده نمی‌شه؛ بهبود کنتراست فعلاً روی مرحله نهایی Threshold تاثیری نداره.



## 📄 License

This project is licensed under the **MIT License**.
