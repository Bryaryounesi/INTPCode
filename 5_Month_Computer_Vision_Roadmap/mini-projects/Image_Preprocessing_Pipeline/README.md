# Image Preprocessing Pipeline

**A complete image preprocessing pipeline that applies contrast enhancement and morphological operations to prepare images for further analysis.**


## 📌 Pipeline (As Actually Implemented)

Image Reading → Gray → Adaptive Threshold (on raw gray) → Opening → Closing → Save Output

> **Note:** CLAHE is computed and compared against the raw grayscale threshold, but is **NOT** part of the final pipeline (see *Analysis* section below for why).

## 📁 Outputs

For each input image, a **4-panel comparison figure** (saved as one stacked image):

| Panel | Description |
|-|-|
| 1 | Grayscale |
| 2 | CLAHE Result *(comparison only — not used downstream)* |
| 3 | Opening Result *(on raw-gray threshold)* |
| 4 | Closing Result *(on raw-gray threshold)* |



## 🗂️ Project Structure


image-preprocessing-pipeline/
├── src/
│   └── main.py
├── data/
├── outputs/
├── IPP_dependencies.txt
└── README.md




## ⚙️ Requirements

Install dependencies:


pip install -r IPP_dependencies.txt




## 🚀 Usage

Run the main script:

python src/main.py


## 📝 Notes

- Run the pipeline on **at least 3 different images**
- Analyze **which stage has the most impact**
- Determine whether **all images require the same pipeline**



## 🔍 Analysis — Q1: Which Stage Has the Most Impact?

### English
- No single morphological stage (**Opening** or **Closing**) can be called the most impactful *in general* — the effect is **image-dependent**.
- The clearest impact found in testing was a **negative one**: using the **CLAHE-enhanced image** as the basis for adaptive thresholding introduced **excessive noise** into the binary result, compared to thresholding the **raw grayscale image** directly.
- For this reason, **CLAHE was excluded** from the final pipeline; only the raw grayscale image is used as the threshold input.

### فارسی
- در مورد عملیات مورفولوژی (**Opening** یا **Closing**) نمی‌توان به‌طور کلی گفت کدام مرحله بیشترین تاثیر مثبت را داشته، چون این موضوع به تصویر بستگی دارد.
- واضح‌ترین تاثیری که در تست پیدا شد، تاثیری **منفی** بود: استفاده از تصویر **CLAHE شده** به‌عنوان مبنای ترشهولد تطبیقی، نویز **بیش‌ازحدی** به تصویر باینری اضافه می‌کرد، در مقایسه با ترشهولد مستقیم روی تصویر خاکستری خام.
- به همین دلیل **CLAHE از پایپلاین نهایی حذف شد** و فقط تصویر خاکستری خام به‌عنوان ورودی ترشهولد استفاده می‌شود.



## 🔍 Analysis — Q2: Do All Images Need the Same Pipeline?

### English
- The current pipeline performs **acceptably** on all selected test images, but it is **not the optimal** morphological pipeline.
- Noise remains visible in the **Opened** image, and especially in the **Closed-on-Opened** image; object edges are **broken or holed** in several images.
- A better pipeline would be:


img reading → gray (without CLAHE) → threshold → opening (soft kernel) → dilating on opened (aggressive kernel) → finding the largest contour from the binary image → drawing mask based on that largest contour → masked = bitwise_and(binary, dilated)


- **Conclusion:** A single fixed pipeline can work reasonably well across images, but the specific **kernel sizes** and **morphological steps** likely need **per-image** or **per-dataset tuning** rather than one fixed sequence for everything.

### فارسی
- پایپلاین فعلی روی تمام تصاویر آزمایش‌شده عملکرد **قابل‌قبولی** داشته، اما **بهترین پایپلاین مورفولوژی ممکن نیست**.
- نویز همچنان در تصویر **Opened** و به‌خصوص در تصویر **Closed-on-Opened** قابل مشاهده است؛ حاشیه اشیاء هم در چند تصویر **شکسته یا سوراخ‌دار (Hole)** است.
- پایپلاین بهتر پیشنهادی:


img reading → gray (without CLAHE) → threshold → opening (soft kernel) → dilating on opened (aggressive kernel) → finding the largest contour from the binary image → drawing mask based on that largest contour → masked = bitwise_and(binary, dilated)


- **نتیجه‌گیری:** یک پایپلاین ثابت می‌تواند روی چند تصویر نسبتاً خوب کار کند، اما اندازه دقیق **کرنل‌ها** و **مراحل مورفولوژی** احتمالاً نیاز به تنظیم جداگانه بر اساس **هر تصویر** یا **هر دیتاست** دارند، نه یک توالی ثابت برای همه.



## 🔮 Future Improvement
The mask-based pipeline above (soft-kernel **Opening**, followed by aggressive **Dilation**, then masking the original binary image via `bitwise_and`) is a candidate for a future revision, as it should better preserve object boundaries while still suppressing noise.



## 📄 License
MIT