# Pretrained Inference with ResNet18

A minimal, reusable inference pipeline that classifies images using a pretrained ResNet18 model and reports the top-k ImageNet predictions with probabilities — no training, no fine-tuning, no custom dataset required.

پایپ‌لاینی مینیمال و قابل استفاده‌ی مجدد برای طبقه‌بندی تصویر با مدل از پیش آموزش‌دیده‌ی ResNet18 و گزارش k کلاس برتر ImageNet همراه با احتمال — بدون آموزش، بدون fine-tune و بدون نیاز به دیتاست اختصاصی.

## 📁 Dataset

**English:**
No dataset was collected for this project. The pipeline runs on **any arbitrary `.jpg` images** placed in the `data/` folder. The model was pretrained on **ImageNet-1K** (1000 classes), so predictions are only meaningful for images whose content falls within the ImageNet domain (everyday objects, animals, vehicles, etc.).

**فارسی:**
برای این پروژه دیتاستی جمع‌آوری نشد. پایپ‌لاین روی **هر تصویر `.jpg` دلخواه** که در پوشه `data/` قرار بگیره اجرا می‌شه. مدل روی **ImageNet-1K** (۱۰۰۰ کلاس) از پیش آموزش دیده، بنابراین پیش‌بینی‌ها فقط برای تصاویری معنا دارن که محتواشون داخل دامنه‌ی ImageNet باشه (اشیاء روزمره، حیوانات، خودروها و…).

## 🔧 Pipeline

Read Image → RGB Conversion → Resize(256) → CenterCrop(224) → ToTensor → Normalize → ResNet18 → Softmax → Top-k → Report / Visualize / Save

## 🧱 Code Structure

**English:**
The project is written in a function-based style with a clear separation of concerns:

| Function | Description |
|-|-|
| `preprocessing(pil_img)` | Resize, CenterCrop, ToTensor, Normalize, and move to the active device |
| `model_predict(input_batch, model, k)` | Runs the model, applies softmax, and returns top-k probabilities and indices |
| `show_image(img, top_p, top_i)` | Displays the image with the top-1 class as title |
| `read_img(path)` | Reads an image from disk and converts BGR to RGB PIL |
| `save_image(img, top_p, top_i, name, output)` | Saves the annotated image as `.png` in the output folder |
| `resnet18_predict(folder, k, show_images, save_images, output)` | Main pipeline function — iterates over all images and chains all steps |

The `resnet18_predict` function is the reusable entry point of the pipeline. It receives a folder and configuration flags, and reports, displays, and/or saves the annotated results — making it easy to use the pipeline on new images outside the main block.

**فارسی:**
کد به‌صورت تابع‌محور با جداسازی واضح وظایف نوشته شده:

| تابع | توضیح |
|-|-|
| `preprocessing(pil_img)` | Resize، CenterCrop، ToTensor، Normalize و انتقال به دستگاه فعال |
| `model_predict(input_batch, model, k)` | اجرای مدل، اعمال softmax و برگرداندن k احتمال و ایندکس برتر |
| `show_image(img, top_p, top_i)` | نمایش تصویر همراه با کلاس top-1 به‌عنوان عنوان |
| `read_img(path)` | خواندن تصویر از دیسک و تبدیل BGR به PIL در فضای RGB |
| `save_image(img, top_p, top_i, name, output)` | ذخیره‌ی تصویر حاشیه‌نویسی‌شده به‌صورت `.png` در پوشه خروجی |
| `resnet18_predict(folder, k, show_images, save_images, output)` | تابع اصلی پایپ‌لاین — پیمایش روی همه‌ی تصاویر و زنجیر کردن تمام مراحل |

تابع `resnet18_predict` نقطه ورود قابل استفاده‌ی مجدد پایپ‌لاین است. یک پوشه و پرچم‌های تنظیمات می‌گیرد و نتایج حاشیه‌نویسی‌شده را گزارش، نمایش و/یا ذخیره می‌کند؛ بنابراین استفاده از پایپ‌لاین روی تصاویر جدید خارج از بلاک اصلی راحت است.

## 📂 Project Structure

```
Pretrained_Inference_with_ResNet18/
├── data/                  # Input images (.jpg)
├── output/                # Annotated output images
├── main.py                # Main script with pipeline functions
└── README.md              # Project documentation
```

## 📦 Requirements

This mini-project has **no separate `requirements.txt`**. It shares the virtual environment and dependencies of the parent `dl-mini-projects/` directory:

```
For installation and setup instructions, please refer to the main README in the parent directory.
```

Dependencies used: `torch`, `torchvision`, `opencv-python`, `Pillow`, `matplotlib`.

## 🚀 Usage

Run the main script:

```
python main.py
```

Example call:

```python
resnet18_predict(folder, k=3, show_images=False, save_images=False, output=output)
```

## 🔍 Pipeline Details

**English:**

- **ResNet18** with `IMAGENET1K_V1` weights is used as-is — no fine-tuning, no custom head. It is the standard torchvision reference model.
- **Device selection** is automatic: `cuda` if available, otherwise `cpu`. Both the model and every input tensor are moved to the active device before inference.
- **Preprocessing** follows the official ImageNet recipe: `Resize(256) → CenterCrop(224) → ToTensor → Normalize` with ImageNet mean `[0.485, 0.456, 0.406]` and std `[0.229, 0.224, 0.225]`. This is required for the pretrained weights to behave as intended.
- **Top-k extraction** uses `torch.topk` on the softmax output, returning both the top-k probabilities and their class indices. `k` is configurable per call (default `3`).
- **Reporting** prints each of the top-k classes in the format `rank_class_name    probability`. The label list is pulled from `weights.meta["categories"]`, so class names always match the loaded weights.
- **Visualization and saving** are independent flags (`show_images`, `save_images`). Saving creates the output directory automatically and writes each annotated figure as `.png`.
- **Robust I/O:** unreadable or corrupted images are skipped with a `was skipped` message rather than crashing the loop.

**فارسی:**

- از **ResNet18** با وزن‌های `IMAGENET1K_V1` بدون تغییر استفاده می‌شه — بدون fine-tune و بدون سر سفارشی. این همون مدل مرجع استاندارد torchvision است.
- **انتخاب دستگاه** خودکار است: در صورت وجود `cuda`، وگرنه `cpu`. هم مدل و هم هر تنسور ورودی قبل از استنتاج به دستگاه فعال منتقل می‌شن.
- **پیش‌پردازش** از دستور رسمی ImageNet پیروی می‌کنه: `Resize(256) → CenterCrop(224) → ToTensor → Normalize` با میانگین `[0.485, 0.456, 0.406]` و انحراف‌معیار `[0.229, 0.224, 0.225]`. این برای رفتار درست وزن‌های از پیش آموزش‌دیده ضروری است.
- **استخراج top-k** با `torch.topk` روی خروجی softmax انجام می‌شه و هم k احتمال برتر و هم ایندکس کلاس‌هاشون رو برمی‌گردونه. `k` در هر فراخوانی قابل تنظیم است (پیش‌فرض `3`).
- **گزارش** هر یک از k کلاس برتر رو با فرمت `رتبه_نام‌کلاس    احتمال` چاپ می‌کنه. لیست برچسب‌ها از `weights.meta["categories"]` گرفته می‌شه، بنابراین اسم کلاس‌ها همیشه با وزن‌های لودشده هماهنگن.
- **نمایش و ذخیره** پرچم‌های مستقلی هستن (`show_images`، `save_images`). ذخیره‌سازی پوشه خروجی رو خودکار می‌سازه و هر فیگور حاشیه‌نویسی‌شده رو به‌صورت `.png` می‌نویسه.
- **I/O مقاوم:** تصاویر غیرقابل‌خواندن یا خراب با پیام `was skipped` رد می‌شن، بدون اینکه حلقه کرش کنه.

## 📊 Analysis & Findings

**English:**

Overall, the pipeline produced **top-1 predictions that looked reasonable** for standard ImageNet-like photos (pets, vehicles, everyday objects, food). For images outside the ImageNet domain — screenshots, text, medical images, satellite imagery, or heavily stylized art — the top-1 class was frequently nonsensical, which is expected behavior for a model with no domain adaptation.

The most noticeable limitations observed during testing:

- **CenterCrop discards information** for images with unusual aspect ratios (very wide or very tall). Important content near the edges of the original image is cut off before inference.
- **Low-confidence predictions are reported as if reliable.** There is no minimum-probability threshold, so a top-1 prediction with `12%` probability is printed exactly like one with `95%`.
- **Only the top-1 class is visualized.** Even when `k=5`, the saved/displayed title always shows `top_p[0]` / `top_i[0]`. The remaining k−1 predictions appear only in the terminal.
- **Per-image inference** (no batching). Each image is passed through the model separately, which is slower than batched inference and underutilizes the GPU when available.
- **No preprocessing augmentation** (no test-time augmentation, no multi-crop). This is intentional for a minimal reference pipeline, but it caps accuracy on borderline images.

Given that the model is used **entirely out of the box** with no fine-tuning and no domain adaptation, the results are **as good as the pretrained weights allow** — the pipeline is not the bottleneck; the model's domain is.

**فارسی:**

در مجموع، پایپ‌لاین برای عکس‌های استاندارد شبیه ImageNet (حیوانات خانگی، خودروها، اشیاء روزمره، غذا) **پیش‌بینی‌های top-1 معقولی** ارائه داد. برای تصاویر خارج از دامنه‌ی ImageNet — اسکرین‌شات، متن، تصاویر پزشکی، تصاویر ماهواره‌ای یا هنرهای بسیار سبک‌دار — کلاس top-1 اغلب بی‌معنی بود، که رفتار مورد انتظار برای مدلی بدون انطباق دامنه است.

قابل‌توجه‌ترین محدودیت‌های مشاهده‌شده در تست:

- **CenterCrop اطلاعات را حذف می‌کند** برای تصاویر با نسبت ابعاد غیرمعمول (خیلی پهن یا خیلی بلند). محتوای مهم نزدیک لبه‌های تصویر اصلی قبل از استنتاج بریده می‌شود.
- **پیش‌بینی‌های کم‌اطمینان طوری گزارش می‌شن که انگار مطمئنن.** آستانه‌ی حداقل احتمال وجود نداره، بنابراین پیش‌بینی top-1 با احتمال `۱۲٪` دقیقاً مثل یکی با احتمال `۹۵٪` چاپ می‌شه.
- **فقط کلاس top-1 نمایش داده می‌شه.** حتی وقتی `k=5` باشه، عنوان ذخیره/نمایش همیشه `top_p[0]` / `top_i[0]` رو نشون می‌ده. بقیه‌ی k−1 پیش‌بینی فقط توی ترمینال ظاهر می‌شن.
- **استنتاج تک‌تصویری** (بدون batching). هر تصویر جداگانه از مدل عبور می‌کنه، که از استنتاج بچ‌شده کندتره و در صورت وجود GPU، ازش به‌درستی استفاده نمی‌شه.
- **بدون augmentation در پیش‌پردازش** (بدون test-time augmentation، بدون multi-crop). این برای یک پایپ‌لاین مرجع مینیمال عمدیه، ولی دقت رو روی تصاویر مرزی محدود می‌کنه.

با توجه به اینکه مدل **کاملاً out of the box** و بدون fine-tune و بدون انطباق دامنه استفاده می‌شه، نتایج **به‌اندازه‌ی چیزی که وزن‌های از پیش آموزش‌دیده اجازه می‌دن** خوبن — گلوگاه، پایپ‌لاین نیست؛ دامنه‌ی مدل است.

## ⚠️ Known Limitations

**English:**

- The pipeline is **pure inference on ImageNet-pretrained weights**; it has no fine-tuning, no domain adaptation, and no calibration on custom data.
- **No confidence threshold** is applied, so low-confidence predictions are reported without any warning or filtering.
- **Only the top-1 class is visualized**, even when `k > 1`; the remaining top-k classes appear only in the terminal output.
- **No batching** is implemented; each image goes through the model in a separate forward pass.
- **CenterCrop** may discard important content for images with non-standard aspect ratios.
- The pipeline assumes `.jpg` inputs by default; other formats require editing the glob pattern.

**فارسی:**

- پایپ‌لاین **صرفاً استنتاج روی وزن‌های از پیش آموزش‌دیده‌ی ImageNet** است؛ بدون fine-tune، بدون انطباق دامنه و بدون کالیبراسیون روی داده‌ی اختصاصی.
- **هیچ آستانه‌ی اطمینانی** اعمال نمی‌شه، بنابراین پیش‌بینی‌های کم‌اطمینان بدون هیچ هشدار یا فیلتری گزارش می‌شن.
- **فقط کلاس top-1 نمایش داده می‌شه**، حتی وقتی `k > 1` باشه؛ بقیه‌ی کلاس‌های top-k فقط در خروجی ترمینال ظاهر می‌شن.
- **بدون batching** پیاده‌سازی شده؛ هر تصویر در یک forward pass جداگانه از مدل عبور می‌کنه.
- **CenterCrop** ممکنه برای تصاویر با نسبت ابعاد غیراستاندارد، محتوای مهم رو حذف کنه.
- پایپ‌لاین به‌صورت پیش‌فرض ورودی `.jpg` فرض می‌کنه؛ فرمت‌های دیگه نیاز به تغییر الگوی glob دارن.

## 📄 License

This project is licensed under the **MIT License**.
