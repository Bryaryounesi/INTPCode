#  --------چیت شیت پایتورچ-------
# ----------pytorch cheatsheet-----------
"""

# پایپلاین استتنتاج از مدل resnet18

----levels ---                                                           ---  levels output---
مسیر فایل (path)
  → خواندن (img = cv2.imread(path))                         → آرایه NumPy (BGR)
  → BGR→RGB + NumPy→PIL                                 → تصویر PIL (RGB)
  → transform (Resize→CenterCrop→ToTensor→Normalize) → تنسور (C,H,W)
  → unsqueeze(0)                                                    → بچ(1,C,H,W)
  → eval + inference_mode                                        → مدل و محیط آماده
  → forward                                                             → logits (1,1000)
  → softmax                                                             → احتمالات (1,1000)
  → max/argmax                                          → top_p, top_i (هر کدام (1,))
  → [0]                                                          → احتمال و اندیس (اسکالر)
  → labels[idx]                                                  → نام کلاس (رشته)
  → درصد                                                → رشته‌ی درصدی
  → نمایش                                                  → چاپ در ترمینال

# ============================================================
# مراحل استتنتاج از رسنت 18
# ============================================================
# ۱. خواندن تصویر از دیسک

def read_img(path):
    img = cv2.imread(path)  # خروجی: آرایه NumPy در فضای رنگی BGR
    return img


# ============================================================
# ۲. آماده‌سازی برای transform  (BGR → RGB → PIL)
# ============================================================
# میتوان این مرحله را در زیر مجموعه مرحله اول نوشت

def prepare_for_transform(img):
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    return img_pil

# ============================================================
# ۳. اعمال transformها  (Resize → CenterCrop → ToTensor → Normalize)
# ============================================================
# این مرحله چون همیشه محتوایش ثابت است میتوان به صورت اسنیپت آماده تعریف شود
transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


# ============================================================
# ۴. افزودن بُعد بچ به تنزور حاصل ار ترانسفورم ( با Unsqueeze)
# ============================================================
# این مرحله و مرحله سوم رو میتوان با هم ادغامل کرد به عنوان مرحله پریپروسس

def add_batch_dim(tensor):
    input_batch = tensor.unsqueeze(0)  # (C,H,W) → (1,C,H,W)
    return input_batch


# ============================================================
# ۵ + ۶ + ۷. eval + no_grad + Forward Pass
# مرحله اعمال مدل روی اینپوت بچ
# ============================================================
# مراحل 8 ، 9 ، 11 ، 12 ، 13 رو هم میشود زیرمجموعه همین مرحله نوشت (بدون تابع مجزا)

def model_impacting(input_batch, model):
    model.eval()  # ۵. حالت ارزیابی
    with torch.inference_mode()/torch.no_grade():  # ۶. خاموش‌کردن autograd
        output = model(input_batch)  # ۷. تنسور خروجی خام کلاس ها (logits)
    return output


# ============================================================
# ۸. تبدیل logits به احتمال (Softmax)
# ============================================================
def to_probabilities(output):
    probabilities = torch.softmax(output, dim=1)
    return probabilities  #تنسور احتمال کلاس ها


# ============================================================
# ۹. استخراج کلاس برنده (Max / Argmax)
# ============================================================
def top1(probabilities):
    top_p, top_i = probabilities.max(dim=1)   # احتمال و ایندکس کلاس دارای بالاترین احتمال
    return top_p, top_i


# ============================================================
# ۱۰. (اختیاری) استخراج top-k
# ============================================================
استخراج احتمال و ایندکس 5 تا از محتمل ترین کلاس ها
def topk(probabilities, k=5):
    top_p, top_i = probabilities.topk(k, dim=1)  # (B,k), (B,k)
    return top_p, top_i


# ============================================================
# ۱۱. جدا کردن نمونه از بچ
# ============================================================
def take_first(top_p, top_i):
    prob = top_p[0]  # tensor scalar
    idx = top_i[0]  # tensor scalar
    return prob, idx

# ============================================================
# ۱۲. تبدیل اندیس به برچسب متنی
# ============================================================
def idx_to_label(idx, labels):
    class_name = labels[idx]
    return class_name


# ============================================================
# ۱۳. تبدیل احتمال به درصد
# ============================================================
item() تبدیل تنسور اسکالر احتمال کلاس منتخب به یک عدد پایتونی با

def to_percent(prob):
    return f"{prob.item():.2%}"


# ============================================================
# ۱۴. نمایش یا ذخیره‌ی نتیجه
# ============================================================
این مرحله را هم میشود جزو مرحله لوپ ماین نوشت(بدون تابع مجزا)
def show_result(image_name, label_name, percent_str):
    p(f"image name:{image_name}")
    p(f"{label_name}... {percent_str}")
    p("----------------------------------------")

# 15. ساخت لوپ ماین (لوپ فراخوانی توابع مراحل قبل)
# ------------------------------Main-------------------
for i in pathes:
    # ۱
    img = read_img(i)

    # ۲
    img_pil = prepare_for_transform(img)

    # ۳
    tensor = transform(img_pil)

    # ۴
    input_batch = add_batch_dim(tensor)

    # ۵ + ۶ + ۷
    output = forward(input_batch, model)

    # ۸
    probabilities = to_probabilities(output)

    # ۹
    top_p, top_i = top1(probabilities)

    # ۱۰ (اختیاری)
    # top_p_k, top_i_k = topk(probabilities, k=5)

    # ۱۱
    prob, idx = take_first(top_p, top_i)

    # ۱۲
    class_name = idx_to_label(idx, labels)

    # ۱۳
    prob_percent = to_percent(prob)

    # ۱۴
    name = Path(i).stem
    show_result(name, class_name, prob_percent)
----------------------------------------------------------
----------------------------------------------------------
یک مثال کامل از استنتاج مدل رسنت 18:

import numpy as np
import torchvision
from torchvision import transforms, models
from pathlib import Path
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import torch

p = print
# ------------------------model info-----------------------
weights = models.ResNet18_Weights.IMAGENET1K_V1
labels = weights.meta["categories"]
model = models.resnet18(weights=weights)
# ------------------------transforms---------------------
transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)


# ------------------------model impacting----------------------
def model_inpacting(input_batch, model, k=5):
    # تابع بدون پارامتر مدل هم کار میکنه ولی با مدل بهتر
    # تعریف پارامتر کی در این تابع سبب انعطاف بیشتر در لوپ ماین میشود
    model.eval()  # گذاشتن مدل روی استنتاج
    with torch.inference_mode():  # خاموش سازی گرادیان
        # معادل with torch.no_grade():
        outputs = model(input_batch)  # اعمال مدل روی بچ ، آوتپوت تنسور خام مدل
        probabilities = torch.softmax(
            outputs, dim=1
        )  # تبدیل تنسور خام به تنسور احتمالات
        top_p, top_i = probabilities.topk(k, dim=1)  # تاپ کی منعطف تر از مکس است
        # استخراج احتمال و ایندکس کی عدد از محتمل  ترین کلاس ها
        return (
            top_p[0],
            top_i[0],
        )  # جدا کردن بچ از تنسورِ کی احتمال و تنسور ایندکس های اینها


# همه موارد ریترن شده هنوز تنسور هستن
# -----------------preprocess-----------
def preprocessing(img_pil):
    tensor = transform(img_pil)
    input_batch = tensor.unsqueeze(0)
    return input_batch


# --------------------virsualize---------------------
def _make_fig(img, class_name, prob):  # تابع کمکی سازنده فیگ
    fig, axs = plt.subplots(constrained_layout=True)
    # ساخت فیگور و قاب های عکس درون آن(در اینجا یک قاب عکس در هر فیگور)
    axs.imshow(img)  # گذاشتن تصویر در قاب عکس
    axs.set_title(f"{class_name}_{prob:.2%}")
    # تعیین عنوان برای هر قاب عکس از محتمل ترین کلاس
    axs.axis("off")  # خاموش کردن گرید هر قاب عکس
    return fig  # بازگرداندن فیگور با قاب پر از تصویر


def showing(img, class_name, prob):
    fig = _make_fig(img, class_name, prob)
    plt.show()  # نمایش فیگ از قبل ساخته شده و تصاویر درون آن
    plt.close(fig)


# -----------I/O-------------
def read_img(path):
    img = cv2.imread(path)
    if img is None:
        return None
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_pil = Image.fromarray(img_rgb)
    return img_pil


def save_img(output, name, class_name, prob, img):
    fig = _make_fig(img, class_name, prob)
    fig.savefig(output / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)


# ---------------------main loop------------
folder = Path(r"E:/BEAUTIFULL/beautifull")
pathes = [str(i) for i in folder.glob("*.jpg")]
output = Path(r"C:/Users/venous pc/Desktop/test")
output.mkdir(parents=True, exist_ok=True)

for i in pathes:
    name = Path(i).stem
    img = read_img(i)
    if img is None:
        p(f"{name} was skipped")
        continue
    input_batch = preprocessing(img)
    top_p, top_i = model_inpacting(input_batch, model, k=3)
    prob = top_p[0].item()
    # (عدد شده با آیتم)جدا کردن بالاترین احتمال از بقیه کی احتمال برتر)
    idx = top_i[0].item()
    # ایندکس محتمل ترین کلاس (با ایتم از تنسور به عدد تبدیل میشود)
    class_name = labels[idx]  # نام محتمل ترین کلاس

    for j in range(len(top_p)):
        # برای نمایش همه کی احتمال باید روی اندازه تنسور محتمل ها لوپ مجزا بزنیم
        p(f"{j+1}_{labels[top_i[j].item()]:<30}{top_p[j].item():.2%}")
        # آیتم تنسور ها رو تبدیل به عدد می کند که ایمن تر است
    p(f"image name : {name} ")
    p("-------------------")
    showing(img, class_name, prob)  # نمایش
    # save_img(output, name, class_name, prob, img)       #ذخیره
    # نمایش و ذخیره تکی تصاویر بهتر از دردسر نمایش سابپلات

    # p(f"image name: {name}")    #چاپ
    # p(f"recognized as {class_name} with {prob.item():.2%}")
    # تبدیل احتمال به درصد در خود اف استرینگ
    # p("----------------------------------")
# ---------------------------------------------------------------------------------------
ادامه چیت شیت :

# ۰.  نحوه نصب کتابخانه‌های پایتورچ
# ==============================================================
# pip install torch torchvision torchaudio
# pip install --no-index --find-links=C:/wheels torch torchvision torchaudio

# torch        → هسته تنسور و autograd
# torchvision  → مدل‌های آماده، دیتاست‌ها، ترانسفورم‌ها
# torchaudio   → پردازش صدا
# ==============================================================================
# ۱. ایمپورت‌های رایج برای کد های پایتورچ
# ==============================================================================
import torch
import torchvision
from torchvision import transforms, models
from torch.utils.data import DataLoader
from pathlib import Path
import numpy as np
import cv2
from PIL import Image
import matplotlib.pyplot as plt

p = print


# ==============================================================================
# ۲. توابع سازنده Tensor
# ==============================================================================
# ✅ torch.tensor()
# ساخت Tensor از لیست یا آرایه NumPy
#
# 🧩 شکل رایج:
# torch.tensor(data, dtype=torch.float32)
#
# 📌 پارامترها:
# - data:   لیست، لیست تودرتو، یا ndarray
# - dtype:  نوع عناصر — رایج: torch.float32 / torch.int64 — پیش‌فرض: None ❌ → float32
# - device: دستگاه اجرا — پیش‌فرض: cpu ✅
#
# 📌 برمی‌گردونه: torch.Tensor (همیشه کپی مستقل)
#
# ✅ torch.rand()
# ساخت Tensor با مقادیر تصادفی در بازه [0,1)
# 🧩 شکل رایج: torch.rand(*size)
# 📌 مثال: x = torch.rand(3, 3)
# 📌 برمی‌گردونه: torch.Tensor
#
# ✅ torch.from_numpy()
# تبدیل ndarray به Tensor با اشتراک حافظه
# 🧩 شکل رایج: torch.from_numpy(ndarray)
# 📌 برمی‌گردونه: torch.Tensor (اشتراک حافظه با آرایه اصلی)
#
# ✅ torch.as_tensor()
# تبدیل انعطاف‌پذیر (لیست یا ndarray) به Tensor
# 🧩 شکل رایج: torch.as_tensor(data)
#
# ✅ torch.device()
# ساخت شیء دستگاه (cpu یا cuda)
# 🧩 شکل رایج: torch.device("cuda" if torch.cuda.is_available() else "cpu")
# 📌 برمی‌گردونه: torch.device

# --- نمونه‌های عملی ---
x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
r = torch.rand(3, 3)
arr = np.array([[1.0, 2.0], [3.0, 4.0]])
t_np = torch.from_numpy(arr)          # اشتراک حافظه
t_as = torch.as_tensor(arr)           # انعطاف‌پذیر
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ==============================================================================
# ۳. متدهای Tensor
# ==============================================================================
# ✅ t.shape
# ویژگی شکل تنسور (بدون پرانتز)
# 📌 برمی‌گردونه: torch.Size([...])
#
# ✅ t.size()
# تابع شکل تنسور (انعطاف‌پذیرتر از shape)
# 🧩 شکل رایج: t.size()
# 📌 برمی‌گردونه: torch.Size([...])
#
# ✅ t.dtype
# ویژگی نوع داده
# 📌 برمی‌گردونه: torch.float32 / torch.int64 / ...
#
# ✅ t.device
# ویژگی دستگاه فعلی تنسور
# 📌 برمی‌گردونه: cpu / cuda
#
# ✅ t.numpy()
# تبدیل Tensor به ndarray با اشتراک حافظه
# 🧩 شکل رایج: t.cpu().numpy()
# 📌 برمی‌گردونه: numpy.ndarray
# 📌 نکته: اگر requires_grad=True باشد، اول .detach() بزن
#
# ✅ t.clone()
# کپی مستقل از تنسور
# 🧩 شکل رایج: t.clone()
# 📌 برمی‌گردونه: torch.Tensor (کپی مستقل)
#
# ✅ t.to()
# انتقال تنسور یا مدل به دستگاه
# 🧩 شکل رایج: t = t.to(device)   |   model.to(device)
# 📌 برمی‌گردونه: torch.Tensor (برای تنسور) / None (برای مدل، in-place)
# 📌 نکته: برای تنسور باید = بگذاری
#
# ✅ t.item()
# تبدیل تنسور اسکالر به عدد پایتونی
# 🧩 شکل رایج: t.item()
# 📌 برمی‌گردونه: int / float
#
# ✅ t.unsqueeze()
# افزودن بعد جدید
# 🧩 شکل رایج: t.unsqueeze(dim)
# 📌 پارامترها: - dim: موقعیت بعد جدید — رایج: 0 (ابتدا)، -1 (انتها)
# 📌 برمی‌گردونه: torch.Tensor
#
# ✅ t.squeeze()
# حذف ابعاد با اندازه ۱
# 🧩 شکل رایج: t.squeeze()
# 📌 برمی‌گردونه: torch.Tensor
#
# ✅ t.permute()
# جابجایی ابعاد
# 🧩 شکل رایج: t.permute(1, 2, 0)
# 📌 برمی‌گردونه: torch.Tensor

# --- نمونه‌های عملی ---
t = torch.rand(3, 4)
t.shape          # torch.Size([3, 4])
t.size()         # torch.Size([3, 4])
t.dtype          # torch.float32
t.device         # cpu
t_np = t.cpu().numpy()
t_copy = t.clone()
t = t.to(device)
scalar = torch.tensor(3.14).item()   # float
t_u = t.unsqueeze(0)                 # (1, 3, 4)
t_s = t_u.squeeze()                  # (3, 4)
t_p = torch.rand(3, 224, 224).permute(1, 2, 0)   # (224, 224, 3)


# ==============================================================================
# ۴. توابع CUDA
# ==============================================================================
# توابع کودا برای چی؟ برای بررسی و مدیریت GPU سازگار با CUDA
# (پردازش موازی روی کارت گرافیک)
#
# ✅ torch.cuda.is_available()
# بررسی وجود GPU سازگار با CUDA
# 🧩 شکل رایج: torch.cuda.is_available()
# 📌 برمی‌گردونه: bool
#
# ✅ torch.cuda.device_count()
# تعداد GPUهای موجود
# 🧩 شکل رایج: torch.cuda.device_count()
# 📌 برمی‌گردونه: int

print(torch.cuda.is_available())
print(torch.cuda.device_count())


# ==============================================================================
# ۵. Dataset
# ==============================================================================
# کلاس‌های آماده برای دانلود و بارگذاری دیتاست‌های استاندارد
#
# ✅ torchvision.datasets.MNIST()
# دانلود و بارگذاری دیتاست MNIST
# 🧩 شکل رایج:
# torchvision.datasets.MNIST(root, train=True, transform=transforms.ToTensor())
# 📌 پارامترها:
# - root:      مسیر پوشه ذخیره دیتاست
# - train:     بخش آموزش یا تست — True/False — پیش‌فرض: True ✅
# - download:  دانلود خودکار در صورت نبود — True/False — پیش‌فرض: False ❌ → True (بار اول)
# - transform: تبدیل روی هر تصویر — رایج: transforms.ToTensor() — پیش‌فرض: None ❌ → بده
# 📌 برمی‌گردونه: شیء Dataset
# 📌 نکته: len(dataset) → تعداد کل، dataset[i] → (image, label)
#
# ✅ torchvision.datasets.CIFAR10()
# دانلود و بارگذاری دیتاست CIFAR-10
# 🧩 شکل رایج:
# torchvision.datasets.CIFAR10(root, train=True, transform=transforms.ToTensor())

# --- نمونه‌های عملی ---
# train_ds = torchvision.datasets.MNIST(
#     root="./data", train=True, transform=transforms.ToTensor(), download=True
# )
# test_ds = torchvision.datasets.CIFAR10(
#     root="./data", train=False, transform=transforms.ToTensor(), download=True
# )
# len(train_ds)       # تعداد نمونه
# train_ds[0]         # (image, label)


# ==============================================================================
# ۶. DataLoader
# ==============================================================================
# بارگذاری Dataset به صورت دسته‌ای (batch)
#
# ✅ DataLoader()
# 🧩 شکل رایج:
# DataLoader(dataset, batch_size=64, shuffle=True,
#            generator=torch.Generator().manual_seed(2))
# 📌 پارامترها:
# - dataset:     شیء Dataset
# - batch_size:  اندازه هر دسته — رایج: 32/64 — پیش‌فرض: 1 ❌
# - shuffle:     بُر زدن ترتیب — True (آموزش) / False (ارزیابی) — پیش‌فرض: False ❌
# - generator:   seed برای تکرارپذیری — پیش‌فرض: None ❌ → torch.Generator().manual_seed(2)
# - num_workers: تعداد پردازشگر — پیش‌فرض: 0 ✅
# - drop_last:   حذف دسته ناقص آخر — پیش‌فرض: False ✅
# 📌 برمی‌گردونه: torch.utils.data.DataLoader
# 📌 نکته: len(loader) → تعداد دسته، next(iter(loader)) → بچ بعدی

# --- نمونه عملی ---
# train_loader = DataLoader(
#     train_ds, batch_size=64, shuffle=True,
#     generator=torch.Generator().manual_seed(2)
# )
# images, labels_b = next(iter(train_loader))

# ==============================================================================
# ۷. transforms
# ==============================================================================
# تبدیل‌های آماده روی تصاویر برای پیش‌پردازش
#
# ✅ transforms.Compose()
# ترکیب چند تبدیل پشت سر هم
# 🧩 شکل رایج: transforms.Compose([transform1, transform2, ...])

در اغلب مثال ها ترانسفورم ها یکجا و به شکل زیر اعمال میشوند:

مثلا :transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)
# ----------------------------------
شکل رایج تکی ترانسفورم ها :

# ✅ transforms.ToTensor()
# تبدیل PIL/ndarray به Tensor با مقادیر [0,1]
#
# ✅ transforms.Resize()
# تغییر اندازه تصویر
# 🧩 شکل رایج: transforms.Resize(256)
#
# ✅ transforms.CenterCrop()
# برش مرکزی تصویر
# 🧩 شکل رایج: transforms.CenterCrop(224)
#
# ✅ transforms.Normalize()
# نرمال‌سازی با میانگین و انحراف معیار

# 🧩 شکل رایج:
# transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

# ==============================================================================
# ۸. مدل‌های Pretrained(پیش آموزش دیده )
# ==============================================================================
# ✅ models.resnet18()
# بارگذاری مدل ResNet18 با وزن‌های آماده
# 🧩 شکل رایج:
# model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
# 📌 پارامترها:
# - weights: وزن‌های آماده — models.ResNet18_Weights.IMAGENET1K_V1 / "DEFAULT" / None — پیش‌فرض: None ❌
# 📌 برمی‌گردونه: nn.Module
# 📌 نکته: labels = weights.meta["categories"] → لیست ۱۰۰۰ کلاس
#
# ✅ models.ResNet18_Weights.IMAGENET1K_V1
# شیء وزن‌ها و متادیتای مدل
#
# ✅ model.eval()
# بردن مدل به حالت استنتاج
# 🧩 شکل رایج: model.eval()
#
# ✅ model.to()
# انتقال مدل به دستگاه
# 🧩 شکل رایج: model.to(device)

# ==============================================================================
# ۹. مدل‌های رایج دیگر
# ==============================================================================
models.resnet50(weights="DEFAULT")
models.mobilenet_v2(weights="DEFAULT")
models.efficientnet_b0(weights="DEFAULT")
models.vgg16(weights="DEFAULT")
models.vit_b_16(weights="DEFAULT")

# ==============================================================================
# ۱۰. توابع استنتاج
برای درک بهتر نحوه استفاده یا پس و پیش بودن توابع زیر به الگوی استنتاج  رسنت 18 و پایپلاین استنتاج رسنت 18 مراجعه کنید
# ==============================================================================
# ✅ torch.inference_mode()
# خاموش کردن گرادیان برای استنتاج (سریع‌تر)
# 🧩 شکل رایج:
# with torch.inference_mode():
#     output = model(input_batch)
#
# ✅ torch.no_grad()
# خاموش کردن گرادیان (معادل قدیمی تر inference_mode)
# 🧩 شکل رایج:
# with torch.no_grad():
#     output = model(input_batch)
#
# ✅ torch.softmax()
# تبدیل logits به احتمال
# 🧩 شکل رایج: torch.softmax(output, dim=1)
# 📌 برمی‌گردونه: torch.Tensor (احتمالات)
#
# ✅ t.topk()
# استخراج k مقدار بزرگ‌تر و ایندکس‌هایشان
# 🧩 شکل رایج: top_p, top_i = probabilities.topk(k, dim=1)
# 📌 برمی‌گردونه: دو torch.Tensor
# 📌 نکته: top_p[0].item() → احتمال اسکالر، top_i[0].item() → ایندکس اسکالر
#
# ✅ t.max()
# استخراج بزرگ‌ترین مقدار و ایندکس
# 🧩 شکل رایج: top_p, top_i = probabilities.max(dim=1)
#
# ✅ torch.argmax()
# ایندکس بزرگ‌ترین مقدار
# 🧩 شکل رایج: torch.argmax(output, dim=1)


# ==============================================================================
# ۱۱. الگوی رایج Inference (ResNet18)
الگوی استنتاج رسنت 18
# ==============================================================================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

weights = models.ResNet18_Weights.IMAGENET1K_V1
labels = weights.meta["categories"]
model = models.resnet18(weights=weights)
model.to(device)
model.eval()

transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]
        ),
    ]
)

# img     = cv2.imread(path)
# img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_pil = Image.fromarray(img_rgb)
#
# tensor      = transform(img_pil)
# input_batch = tensor.unsqueeze(0).to(device)
#
# with torch.inference_mode():
#     output = model(input_batch)
#
# probs = torch.softmax(output, dim=1)
# top_p, top_i = probs.topk(5, dim=1)
#
# prob = top_p[0].item()
# idx  = top_i[0].item()
# name = labels[idx]

# ==============================================================================
# ۱۲. حلقه آموزش پایه
اگر مدل روی استنتاج باشد نیازی به حلقه آموزش مدل نیست
# ==============================================================================
# for epoch in range(epoch_num):
#     for j, (images, labels_b) in enumerate(train_loader, start=1):
#         if j % 300 == 0 or j == len(train_loader):
#             p(f"epoch {epoch+1} | iter {j}/{len(train_loader)} | batch {images.shape[0]}")
# ==============================================================================
# ۱۳. نکات کلی
# ==============================================================================
# - tensor.size() و tensor.shape تقریباً یکی هستند (size تابع است)
# - اولین عدد در shape یک بچ = batch_size
# - len(loader) = تعداد دسته، len(dataset) = تعداد نمونه
# - loader[0] کار نمی‌کند → next(iter(loader))
# - for tensor:   x = x.to(device)   |   for model:   model.to(device)
# - مدل و تنسور ورودی باید روی یک device باشند
# - از torch.from_numpy و .numpy() اگر کپی مستقل می‌خواهی استفاده نکن (clone بزن)
# - torch.tensor(arr) همیشه کپی مستقل می‌سازد
# - در استنتاج: model.eval() + torch.inference_mode() را فراموش نکن
# - labels = weights.meta["categories"] → لیست اسم کلاس‌ها
# - مدل Pretrained فقط ۱۰۰۰ کلاس ImageNet را می‌شناسد
# - برای ارزیابی: shuffle=False، برای آموزش: shuffle=True
# - torch.inference_mode() سریع‌تر از torch.no_grad() است
# - model.eval() روی Dropout و BatchNorm اثر می‌گذارد (حالت train را خاموش می‌کند)

# ==============================================================================
# ۱۴. کد نهایی پروژه (استنتاج رسنت 18 روی پوشه تصاویر دلخواه)
پروژه به صورت تابع محور و قابل استفاده مجدد نوشته شده

برای استفاده مجدد تنها کافیست یک اسکریپت جدید در کنار این نسخه از کد(کد ماین) باز کرده و
کد ماین رو به درون آن ایمپورت کرده و تابع اصلی ماین رو همراه با پارامتر های لازم روی تصاویر جدید فرابخوانیم
# ==============================================================================
import cv2
import matplotlib.pyplot as plt
import torch
import torchvision
from torchvision import transforms, models
from PIL import Image
from pathlib import Path

p = print

# --------------model info------------------
weights = models.ResNet18_Weights.IMAGENET1K_V1
labels = weights.meta["categories"]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(weights=weights)
model.to(device)

transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

# -----------------------preprocess----------------------
def preprocessing(pil_img):
    tensor = transform(pil_img)
    tensor = tensor.to(device)
    input_batch = tensor.unsqueeze(0)
    return input_batch

# -------------------------model_predict------------------
def model_predict(input_batch, model, k=5):
    model.eval()
    with torch.no_grad():
        outputs = model(input_batch)
        probabilities = torch.softmax(outputs, dim=1)
        top_p, top_i = probabilities.topk(k, dim=1)
        return top_p[0], top_i[0]

# -------------------virsualize-------------------------
def show_image(img, top_p, top_i):
    plt.imshow(img)
    plt.title(f" best class: {labels[top_i[0].item()]}(prob:{top_p[0].item():.2%})")
    plt.axis("off")
    plt.pause(0.5)

# -------------------I/O-------------------------
def read_img(path):
    img = cv2.imread(path)
    if img is None:
        return None
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    return pil_img

def save_image(img, top_p, top_i, name, output):
    output.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.imshow(img)
    ax.axis("off")
    ax.set_title(f" best class: {labels[top_i[0].item()]}(prob:{top_p[0].item():.2%})")
    fig.savefig(output / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

# -----------------------------main--------------------------
def resnet18_predict(folder, k=3, show_images=True, save_images=True, output=None):
    folder = Path(folder)
    paths = [str(i) for i in folder.glob("*.jpg")]
    for i in paths:
        name = Path(i).stem
        img = read_img(i)
        if img is None:
            p(f"{name} was skipped")
            continue
        input_batch = preprocessing(img)
        top_p, top_i = model_predict(input_batch, model, k)
        # -----------------------report-----------
        for j in range(len(top_p)):
            p(f"{j+1}_{labels[top_i[j].item()]:<40}{top_p[j].item():.2%}")
        p(f"image name: {name}")
        p("------------------------------")
        # -------------------------show_images--------------
        if show_images:
            show_image(img, top_p, top_i)
        # ---------------------------save_images--------------
        if save_images:
            save_image(img, top_p, top_i, name, output)

if __name__ == "__main__":
    folder = Path(
        r"E:/python/INTPCode/5_Month_Computer_Vision_Roadmap/Deep-Learning-Phase/dl-mini-projects/Pretrained_Inference/data"
    )
    output = Path(
        r"E:/python/INTPCode/5_Month_Computer_Vision_Roadmap/Deep-Learning-Phase/dl-mini-projects/Pretrained_Inference/output"
    )
    resnet18_predict(
        folder, k=3, show_images=False, save_images=False, output=output
    )


# ------------------------------------------------------------------
نحوه  استفاده مجدد از کد استنتاج رسنت 18 روی تصاویر
# -------------------------------
import ....
from main import resnet18_predict
output = r"...."
folder = r"..."
resnet18_predict(folder, k=5, show_images=False, save_images=True, output=output)



# نکته ۱: اگر save_images=True باشد ولی output=None بماند، در save_image خطا می‌دهد
# نکته ۲: در main فراخوانی نهایی با show_images=False و save_images=False انجام شده
# نکته ۳: مسیرها مطلق و مخصوص سیستم نویسنده‌اند؛ در سیستم خودتان تغییر دهید
# نکته ۴: model.eval() هر بار داخل model_predict صدا زده می‌شود (بی‌ضرر)
# نکته ۵: در model_predict از torch.no_grad() استفاده شده؛ inference_mode سریع‌تر است
# نکته ۶: در show_image از plt.pause استفاده شده که برای نمایش تعاملی مناسب است
# نکته ۷: len(top_p) تعداد k است چون top_p از قبل برای یک نمونه جدا شده
# نکته ۸: labels[top_i[j].item()] چون top_i روی device است، item() آن را به عدد تبدیل می‌کند
# نکته ۹: تابع read_img در صورت خرابی فایل None برمی‌گرداند و در main با continue رد می‌شود
# نکته ۱۰: فقط فایل‌های *.jpg پیمایش می‌شوند؛ برای png الگو را تغییر دهید
"""
