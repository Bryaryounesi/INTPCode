from typing import Any, Tuple, Optional, Union, List, Dict
import numpy as np
import torch
# ============================================================
# 🏷️ سطح‌بندی موضوعی توابع (مطابق با cvt.find_level):
# [Config] = تنظیمات | [Preprocess] = پیش‌پردازش
# [Analyze/Detect] = تحلیل/تشخیص | [Visualize/Build Output] = نمایش/ساخت خروجی
# [I/O] = ورودی/خروجی | [Main] = اصلی
#
# 🏷️ برچسب دوم (دیپ‌لرنینگ):
# [Data] | [Model] | [Train] | [Evaluate] | [Deploy] | [Visualize]
# ============================================================

# ============================================================
# ۱. ساخت Tensor
# ============================================================
def tensor(
    data: Any,
    dtype: Any = None,
    device: Any = None,
    requires_grad: bool = False,
) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.tensor([1, 2, 3])
    x = torch.tensor(np.array([1, 2, 3]))
    x = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
    x = torch.tensor(data, device='cuda', requires_grad=True)

    📌 پارامترها:
    - data: داده ورودی (لیست، tuple، آرایه NumPy)
        رایج: [1, 2, 3], [[1, 2], [3, 4]], np.array(...)
    - dtype (اختیاری): نوع داده - پیش‌فرض: استنتاج خودکار
        رایج: torch.float32, torch.float64, torch.int64, torch.uint8
    - device (اختیاری): محل ذخیره‌سازی
        رایج: None (پیش‌فرض: cpu), 'cuda', 'cuda:0', 'mps'
    - requires_grad (اختیاری): محاسبه گرادیان - پیش‌فرض: False
        رایج: False, True

    📌 برمی‌گردونه: Tensor با مشخصات داده شده

    📌 نکته: برای تصاویر معمولاً از torch.from_numpy() یا transforms استفاده کن
    """
    ...

def from_numpy(ndarray: Any) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.from_numpy(np.array([1, 2, 3]))
    img_tensor = torch.from_numpy(img_numpy)  # HWC → CHW نیاز به permute دارد

    📌 پارامترها:
    - ndarray: آرایه NumPy
        رایج: np.array([1, 2, 3]), img_numpy

    📌 برمی‌گردونه: Tensor (هم‌حافظه با NumPy - تغییر یکی، دیگری را تغییر می‌دهد)

    📌 نکته: dtype آرایه NumPy حفظ می‌شود (معمولاً float64 برای float)
    📌 برای تبدیل تصویر: tensor = torch.from_numpy(img).permute(2, 0, 1).float() / 255.0
    """
    ...

def zeros(*size: int, dtype: Any = None, device: Any = None) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.zeros(3, 224, 224)
    x = torch.zeros((batch_size, channels, height, width))
    mask = torch.zeros(img.shape[1:], dtype=torch.uint8)

    📌 پارامترها:
    - *size: ابعاد tensor (جداگانه یا تاپل)
        رایج: (3, 224, 224), (batch, 3, 224, 224), (10, 10)
    - dtype (اختیاری): نوع داده - پیش‌فرض: torch.float32
        رایج: torch.float32, torch.uint8, torch.long
    - device (اختیاری): محل ذخیره‌سازی
        رایج: None, 'cuda', 'cpu'

    📌 برمی‌گردونه: Tensor پر از صفر

    📌 کاربرد: ساخت ماسک، initializer، placeholder
    """
    ...

def ones(*size: int, dtype: Any = None, device: Any = None) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.ones(1, 3, 224, 224)
    x = torch.ones(batch_size, num_classes)

    📌 پارامترها:
    - *size: ابعاد - رایج: (1, 3, 224, 224), (batch, num_classes)
    - dtype (اختیاری): پیش‌فرض: torch.float32
    - device (اختیاری): پیش‌فرض: None (cpu)

    📌 برمی‌گردونه: Tensor پر از یک
    """
    ...

def randn(*size: int, dtype: Any = None, device: Any = None) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.randn(3, 224, 224)  # توزیع نرمال (میانگین 0، واریانس 1)
    x = torch.randn(batch_size, latent_dim)

    📌 پارامترها:
    - *size: ابعاد - رایج: (3, 224, 224), (100, 100)
    - dtype (اختیاری): پیش‌فرض: torch.float32
    - device (اختیاری): پیش‌فرض: None

    📌 برمی‌گردونه: Tensor با مقادیر تصادفی نرمال
    """
    ...

def arange(
    start: int, end: Optional[int] = None, step: int = 1, device: Any = None
) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.arange(10)
    x = torch.arange(0, 10, 2)
    indices = torch.arange(batch_size)

    📌 پارامترها:
    - start: شروع (اگر end مشخص نشود، به عنوان end عمل می‌کند)
        رایج: 0, 10
    - end (اختیاری): پایان - رایج: 10, 100
    - step (اختیاری): گام - رایج: 1, 2
    - device (اختیاری): پیش‌فرض: None

    📌 برمی‌گردونه: Tensor بازه‌بندی شده
    """
    ...

def manual_seed(seed: int) -> Any:
    """
    🏷️ [Config]

    📌 فرمول رایج:
    torch.manual_seed(42)
    torch.cuda.manual_seed_all(42)

    📌 پارامترها:
    - seed: عدد تصادفی

    📌 نکته: برای تکرارپذیری نتایج در آموزش استفاده می‌شود.
    📌 نکته: قبل از هر چیز (ساخت مدل، shuffle در DataLoader) صدا بزن.
    """
    ...

# ============================================================
# ۲. عملیات Tensor
# ============================================================
def reshape(input: Any, shape: Tuple[int, ...]) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = x.reshape(batch_size, -1)  # flatten
    x = x.reshape(1, 3, 224, 224)  # add batch dimension
    x = x.reshape(-1, 28 * 28)  # for MLP

    📌 پارامترها:
    - input: tensor ورودی
        رایج: x, img, features
    - shape: شکل جدید (تاپل)
        رایج: (batch, -1), (-1, 28*28), (1, 3, 224, 224)
    - "-1": یعنی خودش حساب کن

    📌 برمی‌گردونه: Tensor با شکل جدید (View - اگر ممکن باشد)

    📌 نکته: reshape سعی می‌کند View بسازد، اگر نشد کپی می‌کند
    """
    ...

def view(input: Any, shape: Tuple[int, ...]) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = x.view(batch_size, -1)
    x = x.view(-1, 3, 224, 224)

    📌 پارامترها: مشابه reshape
    - input: tensor ورودی
    - shape: شکل جدید

    📌 برمی‌گردونه: View از tensor (بدون کپی، فقط اگر contiguous باشد)

    📌 نکته: اگر error داد از x.contiguous().view() یا x.reshape() استفاده کن
    """
    ...

def squeeze(input: Any, dim: Optional[int] = None) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = x.squeeze()  # حذف همه ابعاد ۱
    x = x.squeeze(0)  # حذف batch dimension
    loss = loss.squeeze()  # برای scaler کردن loss

    📌 پارامترها:
    - input: tensor ورودی
    - dim (اختیاری): بعد مشخص - پیش‌فرض: همه ابعاد ۱

    📌 برمی‌گردونه: Tensor با ابعاد ۱ حذف شده
    """
    ...

def unsqueeze(input: Any, dim: int) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = x.unsqueeze(0)  # اضافه کردن batch dimension
    x = img.unsqueeze(0)  # (3, 224, 224) → (1, 3, 224, 224)
    x = x.unsqueeze(-1)  # اضافه کردن بعد آخر

    📌 پارامترها:
    - input: tensor ورودی
    - dim: محل بعد جدید
        رایج: 0 (ابتدای shape), -1 (انتهای shape)

    📌 برمی‌گردونه: Tensor با بعد اضافه
    """
    ...

def transpose(input: Any, dim0: int, dim1: int) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = x.transpose(0, 1)  # جابجایی دو بعد
    img = img.transpose(0, 2).transpose(1, 2)  # HWC → CHW

    📌 پارامترها:
    - input: tensor ورودی
    - dim0: بعد اول - رایج: 0, 1
    - dim1: بعد دوم - رایج: 1, 2

    📌 برمی‌گردونه: Tensor با ابعاد جابجا شده
    """
    ...

def permute(input: Any, dims: Tuple[int, ...]) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = x.permute(2, 0, 1)  # HWC → CHW برای تصویر
    x = x.permute(0, 2, 3, 1)  # NCHW → NHWC

    📌 پارامترها:
    - input: tensor ورودی
    - dims: ترتیب جدید ابعاد
        رایج: (2, 0, 1) برای HWC→CHW، (0, 2, 3, 1) برای NCHW→NHWC

    📌 برمی‌گردونه: Tensor با ترتیب ابعاد جدید

    📌 نکته: برای تبدیل تصویر NumPy به Tensor حتماً استفاده کن:
    img_tensor = torch.from_numpy(img_numpy).permute(2, 0, 1).float() / 255.0
    """
    ...

def to(input: Any, dtype: Any = None, device: Any = None) -> Any:
    """
    🏷️ [Config] [Data]

    📌 فرمول رایج:
    x = x.to('cuda')
    x = x.to(torch.float32)
    model = model.to(device)
    img = img.to(device)

    📌 پارامترها:
    - input: tensor یا model
    - dtype (اختیاری): نوع داده - رایج: torch.float32, torch.float16
    - device (اختیاری): محل - رایج: 'cuda', 'cpu', device

    📌 برمی‌گردونه: tensor/model منتقل شده

    📌 الگوی استاندارد:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    inputs = inputs.to(device)
    """
    ...

def cat(tensors: Any, dim: int = 0) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.cat([x1, x2], dim=0)  # چسباندن در batch
    x = torch.cat([img1, img2], dim=1)  # چسباندن در channel
    features = torch.cat([f1, f2], dim=-1)  # چسباندن feature

    📌 پارامترها:
    - tensors: لیست یا tuple از tensorها
        رایج: [x1, x2], (a, b), [img1, img2]
    - dim: بعد چسباندن
        رایج: 0 (batch), 1 (channel), -1 (feature)

    📌 برمی‌گردونه: Tensor چسبانده شده
    """
    ...

def stack(tensors: Any, dim: int = 0) -> Any:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    x = torch.stack([x1, x2], dim=0)  # ساخت batch از تصاویر
    batch = torch.stack([transform(img) for img in imgs], dim=0)

    📌 پارامترها:
    - tensors: لیست tensorها با shape یکسان
        رایج: [img1_tensor, img2_tensor, ...]
    - dim: بعد جدید
        رایج: 0

    📌 برمی‌گردونه: Tensor با بعد جدید

    📌 تفاوت با cat: stack بعد جدید اضافه می‌کند، cat روی بعد موجود می‌چسباند
    """
    ...

def device(obj: Any = None) -> Any:
    """
    🏷️ [Config]

    📌 فرمول رایج:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    device = torch.device('mps')  # برای Mac Apple Silicon
    device = torch.device('cpu')

    📌 پارامترها:
    - obj: نام دستگاه
        رایج: 'cuda', 'cuda:0', 'cpu', 'mps'

    📌 برمی‌گردونه: شیء device

    📌 الگوی استاندارد در همه پروژه‌ها:
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"Using device: {device}")

    📌 انتخاب دستگاه بر اساس سرعت:
    GPU (CUDA) → برای training مدل‌های CNN
    MPS (Mac) → برای Mac با Apple Silicon
    CPU → برای inference ساده و پروژه‌های کوچک
    """
    ...

def cuda_is_available() -> bool:
    """
    🏷️ [Config]

    📌 فرمول رایج:
    if torch.cuda.is_available():
        device = 'cuda'
    else:
        device = 'cpu'

    📌 برمی‌گردونه: True اگر GPU با CUDA موجود باشد

    📌 نکته: همیشه قبل از استفاده از cuda بررسی کن
    """
    ...

def topk(input: Any, k: int = 5, dim: int = 1) -> Tuple[Any, Any]:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    top_p, top_i = torch.topk(probs, k=5, dim=1)
    values, indices = torch.topk(output, k=3)

    📌 پارامترها:
    - input: tensor امتیازها یا احتمالات
    - k (اختیاری): تعداد مقادیر برتر - پیش‌فرض: 5
        رایج: 3, 5, 10
    - dim (اختیاری): بعد محاسبه - پیش‌فرض: 1
        رایج: 1 (بعد کلاس‌ها)

    📌 برمی‌گردونه: جفت (values, indices) - هر کدام تنسور هم‌شکل

    📌 نکته: تفاوت با max این است که max فقط ۱ مقدار برتر می‌دهد
        ولی topk چندتای برتر.
    """
    ...

def item(input: Any) -> Any:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    predicted_class = torch.argmax(output).item()
    confidence = probs[0, idx].item()
    loss_value = loss.item()

    📌 پارامترها:
    - input: تنسور با یک عضو

    📌 برمی‌گردونه: عدد پایتونی (int یا float)

    📌 نکته: اگر تنسور بیش از یک عضو داشته باشد، ارور می‌دهد.
    """
    ...

def tolist(input: Any) -> List[Any]:
    """
    🏷️ [Preprocess] [Data]

    📌 فرمول رایج:
    ids = top_i[0].tolist()
    probs_list = probs[0].tolist()

    📌 پارامترها:
    - input: تنسور

    📌 برمی‌گردونه: لیست پایتونی

    📌 نکته: برای تنسورهای چندبعدی، لیست تو در تو برمی‌گرداند.
    """
    ...

# 📌 attribute های تنسور (نه تابع، فقط مستندسازی):
# x.shape   → torch.Size([1, 3, 224, 224])   🏷️ [Analyze/Detect] [Evaluate]
# x.dtype   → torch.float32                  🏷️ [Analyze/Detect] [Evaluate]
# x.device  → device(type='cpu')             🏷️ [Analyze/Detect] [Evaluate]

# ============================================================
# ۳. Dataset و DataLoader
# ============================================================
def TensorDataset(*tensors: Any) -> Any:
    """
    🏷️ [I/O] [Data]

    📌 فرمول رایج:
    dataset = torch.utils.data.TensorDataset(images, labels)
    dataset = torch.utils.data.TensorDataset(x_train, y_train)

    📌 پارامترها:
    - *tensors: tensorهای هم‌طول (مثلاً تصاویر و برچسب‌ها)
        رایج: (images, labels), (x, y)

    📌 برمی‌گردونه: Dataset قابل استفاده در DataLoader

    📌 نکته: برای داده‌های NumPy اول تبدیل به tensor کن
    """
    ...

def DataLoader(
    dataset: Any,
    batch_size: int = 1,
    shuffle: bool = False,
    num_workers: int = 0,
    pin_memory: bool = False,
) -> Any:
    """
    🏷️ [I/O] [Data]

    📌 فرمول رایج:
    loader = torch.utils.data.DataLoader(
        dataset,
        batch_size=32,
        shuffle=True,
        num_workers=2
    )

    📌 پارامترها:
    - dataset: Dataset (TensorDataset, ImageFolder, custom)
        رایج: train_dataset, val_dataset
    - batch_size: تعداد نمونه در هر batch
        رایج: 16, 32, 64, 128 (بستگی به حافظه)
    - shuffle: مخلوط‌کردن داده - رایج: True برای train، False برای val/test
    - num_workers: تعداد worker برای loading - رایج: 0 (ساده), 2, 4
    - pin_memory: کپی سریع‌تر به GPU - رایج: True اگر از GPU استفاده می‌کنی

    📌 برمی‌گردونه: Iterator از batchها

    📌 الگوی استاندارد حلقه:
    for images, labels in train_loader:
        images = images.to(device)
        labels = labels.to(device)
        # ... train step

    📌 نکته: num_workers=0 برای Windows پیشنهاد می‌شود (جلوگیری از خطا)
    """
    ...

# ============================================================
# ۴. ساخت مدل
# ============================================================
class nn_Linear:
    def __init__(self, in_features: int, out_features: int, bias: bool = True):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.Linear(784, 128)
        layer = nn.Linear(128, 10)
        layer = nn.Linear(in_features=512, out_features=256)

        📌 پارامترها:
        - in_features: تعداد ورودی
            رایج: 784 (28×28 MNIST), 512, 2048
        - out_features: تعداد خروجی
            رایج: 128, 256, 10 (تعداد کلاس‌ها)
        - bias (اختیاری): بایاس داشته باشد یا نه - پیش‌فرض: True

        📌 نکته: Fully Connected Layer - برای MLP استفاده می‌شود
        """
        ...

    def forward(self, x: Any) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        x = layer(x)
        x = self.fc1(x)
        """
        ...

class nn_Conv2d:
    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: Union[int, Tuple[int, int]],
        stride: Union[int, Tuple[int, int]] = 1,
        padding: Union[int, Tuple[int, int]] = 0,
    ):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        layer = nn.Conv2d(1, 32, kernel_size=5)
        layer = nn.Conv2d(64, 128, kernel_size=3, stride=2, padding=1)

        📌 پارامترها:
        - in_channels: کانال ورودی
            رایج: 3 (RGB), 1 (grayscale), 64, 128
        - out_channels: کانال خروجی (تعداد فیلتر)
            رایج: 32, 64, 128, 256, 512
        - kernel_size: اندازه کرنل
            رایج: 3, 5, 7, (3, 3), (5, 5)
        - stride (اختیاری): گام - پیش‌فرض: 1
            رایج: 1, 2
        - padding (اختیاری): حاشیه - پیش‌فرض: 0
            رایج: 1 (برای kernel=3 حفظ ابعاد), 2 (برای kernel=5)

        📌 نکته: padding=1 با kernel=3 ابعاد را حفظ می‌کند (same convolution)
        """
        ...

class nn_MaxPool2d:
    def __init__(
        self,
        kernel_size: Union[int, Tuple[int, int]],
        stride: Optional[Union[int, Tuple[int, int]]] = None,
        padding: Union[int, Tuple[int, int]] = 0,
    ):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.MaxPool2d(kernel_size=2, stride=2)
        layer = nn.MaxPool2d(2, 2)

        📌 پارامترها:
        - kernel_size: اندازه پنجره pooling
            رایج: 2, (2, 2)
        - stride (اختیاری): گام - پیش‌فرض: kernel_size
            رایج: 2
        - padding (اختیاری): پیش‌فرض: 0

        📌 برمی‌گردونه: لایه MaxPooling

        📌 کاربرد: کاهش ابعاد feature map و افزایش receptive field
        """
        ...

class nn_AvgPool2d:
    def __init__(
        self,
        kernel_size: Union[int, Tuple[int, int]],
        stride: Optional[Union[int, Tuple[int, int]]] = None,
        padding: Union[int, Tuple[int, int]] = 0,
    ):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.AdaptiveAvgPool2d((1, 1))  # Global Average Pooling
        layer = nn.AvgPool2d(kernel_size=2, stride=2)

        📌 کاربرد: کاهش ابعاد، Global Average Pooling قبل از Fully Connected
        """
        ...

class nn_AdaptiveAvgPool2d:
    def __init__(self, output_size: Union[int, Tuple[int, int]]):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.AdaptiveAvgPool2d((1, 1))  # Global Average Pooling
        layer = nn.AdaptiveAvgPool2d((7, 7))

        📌 پارامترها:
        - output_size: ابعاد خروجی
            رایج: (1, 1), (7, 7)

        📌 برمی‌گردونه: Adaptive Pooling (بدون نیاز به محاسبه اندازه ورودی)
        """
        ...

class nn_Dropout:
    def __init__(self, p: float = 0.5):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.Dropout(p=0.5)
        layer = nn.Dropout(0.3)

        📌 پارامترها:
        - p: احتمال حذف نورون
            رایج: 0.5 (قبل از آخرین FC), 0.2, 0.3

        📌 نکته: فقط در training فعال است، در eval خاموش می‌شود
        """
        ...

class nn_BatchNorm2d:
    def __init__(self, num_features: int):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        layer = nn.BatchNorm2d(64)
        layer = nn.BatchNorm2d(128)

        📌 پارامترها:
        - num_features: تعداد کانال‌های ورودی
            رایج: 64, 128, 256

        📌 کاربرد: نرمال‌سازی feature map در طول training
        """
        ...

class nn_ReLU:
    def __init__(self):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        activation = nn.ReLU()
        activation = nn.ReLU(inplace=True)

        📌 برمی‌گردونه: تابع فعال‌سازی ReLU
        """
        ...

class nn_Softmax:
    def __init__(self, dim: int = 1):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        activation = nn.Softmax(dim=1)  # برای output مدل classification

        📌 پارامترها:
        - dim: بعد softmax - رایج: 1 (بعد کلاس‌ها در batch)

        📌 نکته: معمولاً در loss (CrossEntropyLoss) داخلی است، دستی اضافه نکن
        """
        ...

class nn_Sequential:
    def __init__(self, *layers: Any):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = nn.Sequential(
            nn.Conv2d(3, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Flatten(),
            nn.Linear(32*16*16, 10)
        )

        📌 پارامترها:
        - *layers: لایه‌ها به ترتیب

        📌 برمی‌گردونه: مدل sequential
        """
        ...

class nn_Module:
    def __init__(self):
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج (کلاس سفارشی):
        class MyModel(nn.Module):
            def __init__(self, num_classes=10):
                super().__init__()
                self.conv1 = nn.Conv2d(3, 32, 3, padding=1)
                self.pool = nn.MaxPool2d(2, 2)
                self.fc = nn.Linear(32*8*8, num_classes)

            def forward(self, x):
                x = self.pool(F.relu(self.conv1(x)))
                x = x.view(x.size(0), -1)
                x = self.fc(x)
                return x

        model = MyModel(num_classes=10)

        📌 ساختار ضروری:
        - __init__: تعریف لایه‌ها
        - forward: تعریف مسیر data
        """
        ...

    def forward(self, *args, **kwargs) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        def forward(self, x):
            x = self.conv1(x)
            return x

        📌 نکته: هیچ‌وقت forward را مستقیم صدا نزن! از model(x) استفاده کن
        """
        ...

    def to(self, device: Any) -> Any:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        model = model.to(device)
        model.to('cuda')

        📌 پارامترها:
        - device: محل انتقال
            رایج: device, 'cuda', 'cpu'
        """
        ...

    def train(self) -> None:
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        model.train()  # قبل از training loop

        📌 نکته: Dropout و BatchNorm را در حالت training فعال می‌کند
        """
        ...

    def eval(self) -> None:
        """
        🏷️ [Analyze/Detect] [Evaluate]

        📌 فرمول رایج:
        model.eval()  # قبل از validation/test

        📌 نکته: Dropout را خاموش و BatchNorm را به inference mode می‌برد
        """
        ...

    def parameters(self) -> Any:
        """
        🏷️ [Config] [Train]

        📌 فرمول رایج:
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

        📌 برمی‌گردونه: iterator از همه پارامترهای trainable
        """
        ...

    def state_dict(self) -> Dict[str, Any]:
        """
        🏷️ [I/O] [Deploy]

        📌 فرمول رایج:
        torch.save(model.state_dict(), 'model_weights.pth')
        checkpoint = model.state_dict()

        📌 برمی‌گردونه: dictionary از وزن‌ها و بایاس‌ها
        """
        ...

    def load_state_dict(self, state_dict: Dict[str, Any]) -> Any:
        """
        🏷️ [I/O] [Deploy]

        📌 فرمول رایج:
        model.load_state_dict(torch.load('model_weights.pth'))

        📌 پارامترها:
        - state_dict: dictionary وزن‌ها

        📌 نکته: قبل از load، مدل باید همان architecture را داشته باشد
        """
        ...

# ============================================================
# ۵. Loss Functions
# ============================================================
class nn_CrossEntropyLoss:
    def __init__(self):
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        criterion = nn.CrossEntropyLoss()
        loss = criterion(outputs, labels)

        📌 پارامترها:
        - outputs: خروجی model (logits - بدون softmax)
            رایج: shape (batch_size, num_classes)
        - labels: برچسب‌ها (index کلاس - نه one-hot)
            رایج: shape (batch_size,)

        📌 برمی‌گردونه: scalar loss

        📌 نکته: CrossEntropyLoss = Softmax + NLLLoss (softmax داخلش است)
        📌 نکته: labels باید long tensor باشند (torch.long)
        """
        ...

class nn_MSELoss:
    def __init__(self):
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        criterion = nn.MSELoss()
        loss = criterion(predictions, targets)

        📌 کاربرد: رگرسیون، reconstruction
        """
        ...

class nn_BCEWithLogitsLoss:
    def __init__(self):
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        criterion = nn.BCEWithLogitsLoss()
        loss = criterion(outputs, labels.float())

        📌 کاربرد: طبقه‌بندی باینری (خروجی یک عدد، نه دو کلاس)
        """
        ...

# ============================================================
# ۶. Optimizer ها
# ============================================================
class optim_Adam:
    def __init__(self, params: Any, lr: float = 0.001, weight_decay: float = 0):
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
        optimizer = torch.optim.Adam(model.parameters(), lr=0.0001, weight_decay=1e-5)

        📌 پارامترها:
        - params: پارامترهای مدل
            رایج: model.parameters()
        - lr: نرخ یادگیری
            رایج: 0.001, 0.0001, 0.01
        - weight_decay (اختیاری): L2 regularization - رایج: 1e-4, 1e-5

        📌 نکته: Adam پرکاربردترین optimizer برای CNN است
        """
        ...

    def zero_grad(self) -> None:
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        optimizer.zero_grad()  # صفر کردن گرادیان‌ها در ابتدای هر batch

        📌 نکته: اگر صفر نکنی، گرادیان‌ها جمع می‌شوند!
        """
        ...

    def step(self) -> None:
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        optimizer.step()  # به‌روزرسانی وزن‌ها بعد از backward
        """
        ...

    def state_dict(self) -> Dict[str, Any]:
        """
        🏷️ [I/O] [Deploy]

        📌 فرمول رایج:
        torch.save(optimizer.state_dict(), 'optimizer_state.pth')
        """
        ...

    def load_state_dict(self, state_dict: Dict[str, Any]) -> None:
        """
        🏷️ [I/O] [Deploy]

        📌 فرمول رایج:
        optimizer.load_state_dict(torch.load('optimizer_state.pth'))
        """
        ...

class optim_SGD:
    def __init__(
        self,
        params: Any,
        lr: float = 0.01,
        momentum: float = 0.9,
        weight_decay: float = 0,
    ):
        """
        🏷️ [Analyze/Detect] [Train]

        📌 فرمول رایج:
        optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

        📌 پارامترها:
        - params: model.parameters()
        - lr: نرخ یادگیری - رایج: 0.01, 0.001
        - momentum: مومنتوم - رایج: 0.9
        - weight_decay: رایج: 5e-4
        """
        ...

def lr_scheduler_StepLR(optimizer: Any, step_size: int, gamma: float = 0.1) -> Any:
    """
    🏷️ [Config] [Train]

    📌 فرمول رایج:
    scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)

    📌 پارامترها:
    - optimizer: optimizer مورد استفاده
    - step_size: هر چند epoch لر را کم کن - رایج: 10, 20, 30
    - gamma: ضریب کاهش - رایج: 0.1, 0.5

    📌 برمی‌گردونه: scheduler که lr را مدیریت می‌کند

    📌 استفاده:
    for epoch in range(num_epochs):
        train(...)
        scheduler.step()  # بعد از هر epoch
    """
    ...

def lr_scheduler_ReduceLROnPlateau(
    optimizer: Any, mode: str = "min", factor: float = 0.1, patience: int = 10
) -> Any:
    """
    🏷️ [Config] [Train]

    📌 فرمول رایج:
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.1, patience=5
    )

    📌 پارامترها:
    - optimizer: optimizer
    - mode: 'min' برای loss، 'max' برای accuracy
    - factor: ضریب کاهش - رایج: 0.1
    - patience: چند epoch صبر کن اگر بهتر نشد - رایج: 5, 10

    📌 استفاده:
    scheduler.step(val_loss)  # باید مقدار metric را بدهی
    """
    ...
# ============================================================
# ۷. عملیات Training
# ============================================================
def backward(loss: Any) -> None:
    """
    🏷️ [Analyze/Detect] [Train]

    📌 فرمول رایج:
    loss.backward()  # محاسبه گرادیان‌ها با Backpropagation

    📌 پارامترها:
    - loss: مقدار loss (scalar tensor)
        رایج: loss

    📌 نکته: ترتیب در حلقه training:
    1. optimizer.zero_grad()  # صفر کردن گرادیان
    2. outputs = model(inputs)  # forward
    3. loss = criterion(outputs, labels)  # محاسبه loss
    4. loss.backward()  # backward
    5. optimizer.step()  # به‌روزرسانی
    """
    ...

def no_grad() -> Any:
    """
    🏷️ [Analyze/Detect] [Train]

    📌 فرمول رایج:
    with torch.no_grad():
        outputs = model(images)
        predictions = torch.argmax(outputs, dim=1)

    📌 کاربرد: در validation/test که نیاز به گرادیان نداریم
    📌 مزیت: کاهش مصرف حافظه و افزایش سرعت
    """
    ...

def save(obj: Any, f: str) -> None:
    """
    🏷️ [I/O] [Deploy]

    📌 فرمول رایج:
    torch.save(model.state_dict(), 'model_weights.pth')
    torch.save(checkpoint, 'checkpoint.pth')
    torch.save(model, 'full_model.pth')

    📌 پارامترها:
    - obj: شیء برای ذخیره (state_dict, checkpoint, model)
        رایج: model.state_dict(), {'epoch': epoch, 'model_state_dict': ..., 'optimizer_state_dict': ...}
    - f: مسیر فایل
        رایج: 'model_weights.pth', 'best_model.pth', 'checkpoint_epoch10.pth'

    📌 الگوی checkpoint کامل:
    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss,
        'accuracy': accuracy
    }
    torch.save(checkpoint, 'checkpoint.pth')

    📌 نکته: پسوند .pth یا .pt استاندارد است
    """
    ...

def load(f: str, map_location: Any = None) -> Any:
    """
    🏷️ [I/O] [Deploy]

    📌 فرمول رایج:
    state_dict = torch.load('model_weights.pth')
    model.load_state_dict(state_dict)

    # وقتی روی CPU لود می‌کنی ولی با GPU ذخیره شده:
    state_dict = torch.load('model_weights.pth', map_location='cpu')

    # لود checkpoint کامل:
    checkpoint = torch.load('checkpoint.pth')
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])

    📌 پارامترها:
    - f: مسیر فایل
    - map_location (اختیاری): محل لود - رایج: None, 'cpu', device

    📌 برمی‌گردونه: شیء ذخیره شده
    """
    ...

def argmax(input: Any, dim: int = 1) -> Any:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    predictions = torch.argmax(outputs, dim=1)
    predicted_class = torch.argmax(output, dim=0)

    📌 پارامترها:
    - input: tensor خروجی مدل (logits یا probabilities)
        رایج: outputs
    - dim: بعد کلاس‌ها
        رایج: 1 (برای batch), 0 (برای تک نمونه)

    📌 برمی‌گردونه: index کلاس پیش‌بینی شده
    """
    ...

def max(input: Any, dim: int = 1) -> Tuple[Any, Any]:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    probabilities, predictions = torch.max(outputs, dim=1)
    confidence, predicted = torch.max(probs, dim=0)

    📌 پارامترها:
    - input: tensor
    - dim: بعد محاسبه

    📌 برمی‌گردونه: (مقادیر حداکثر, indexها)
    """
    ...

def softmax(input: Any, dim: int = 1) -> Any:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    probabilities = torch.softmax(outputs, dim=1)
    probs = F.softmax(logits, dim=1)

    📌 پارامترها:
    - input: logits خروجی مدل
    - dim: بعد کلاس‌ها - رایج: 1

    📌 برمی‌گردونه: احتمالات (جمع هر سطر = 1)
    """
    ...

# ============================================================
# ۸. ارزیابی و Metric
# ============================================================
def accuracy_score(y_true: Any, y_pred: Any) -> float:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    acc = accuracy_score(labels, predictions)
    # یا دستی:
    correct = (predictions == labels).sum().item()
    accuracy = correct / len(labels)

    📌 پارامترها:
    - y_true: برچسب‌های واقعی
    - y_pred: پیش‌بینی‌ها

    📌 برمی‌گردونه: دقت (0 تا 1 یا 0 تا 100)

    📌 الگوی حلقه validation:
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in val_loader:
            images = images.to(device)
            labels = labels.to(device)
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    accuracy = 100 * correct / total
    """
    ...

def confusion_matrix(y_true: Any, y_pred: Any) -> Any:
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    cm = confusion_matrix(all_labels, all_predictions)
    print(cm)

    📌 پارامترها:
    - y_true: برچسب‌های واقعی
    - y_pred: پیش‌بینی‌ها

    📌 برمی‌گردونه: ماتریس درهم‌ریختگی

    📌 برای جمع‌آوری در کل validation:
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images.to(device))
            _, preds = torch.max(outputs, 1)
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.numpy())
    cm = confusion_matrix(all_labels, all_preds)
    """
    ...

def classification_report(
    y_true: Any, y_pred: Any, target_names: Optional[List[str]] = None
) -> str:
    ...
    """
    🏷️ [Analyze/Detect] [Evaluate]

    📌 فرمول رایج:
    print(classification_report(all_labels, all_preds, target_names=class_names))

    📌 پارامترها:
    - y_true: برچسب‌های واقعی
    - y_pred: پیش‌بینی‌ها
    - target_names: نام کلاس‌ها - رایج: ['cat', 'dog'], class_names

    📌 برمی‌گردونه: گزارش کامل (precision, recall, f1-score)
    """
    ...

# ============================================================
# ۹. Visualization
# ============================================================
def tensor_to_numpy(tensor: Any) -> Any:
    """
    🏷️ [Visualize/Build Output] [Visualize]

    📌 فرمول رایج:
    img_numpy = img_tensor.cpu().numpy()
    img_numpy = img_tensor.detach().cpu().numpy()

    📌 پارامترها:
    - tensor: tensor که باید تبدیل شود
        رایج: img_tensor, output_tensor

    📌 برمی‌گردونه: آرایه NumPy

    📌 نکته: اگر requires_grad=True است، حتماً detach() بزن
    📌 نکته: اگر روی GPU است، اول cpu() کن
    """
    ...

def tensor_to_image(tensor: Any) -> Any:
    """
    🏷️ [Visualize/Build Output] [Visualize]

    📌 فرمول رایج:
    img = tensor_to_image(img_tensor)  # برای نمایش با matplotlib/cv2

    📌 تبدیل کامل:
    # CHW Tensor (normalized) → HWC NumPy (0-255 uint8)
    img = tensor.detach().cpu().numpy()  # (C, H, W)
    img = img.transpose(1, 2, 0)  # (H, W, C)
    img = (img * 255).astype(np.uint8)

    📌 پارامترها:
    - tensor: تصویر tensor (CHW, normalized)

    📌 برمی‌گردونه: تصویر NumPy (HWC, uint8)

    📌 برای unnormalize با mean/std خاص:
    img = img * std + mean  # اول unnormalize کن
    """
    ...

def plot_training_history(history: Dict[str, List[float]]) -> None:
    """
    🏷️ [Visualize/Build Output] [Visualize]

    📌 فرمول رایج:
    plt.plot(train_losses, label='Train Loss')
    plt.plot(val_losses, label='Val Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

    📌 پارامترها:
    - history: دیکشنری شامل loss و accuracy تاریخچه
        رایج: {'train_loss': [...], 'val_loss': [...], 'train_acc': [...], 'val_acc': [...]}

    📌 الگوی ذخیره تاریخچه:
    train_losses = []
    val_losses = []
    for epoch in range(num_epochs):
        # ... training
        train_losses.append(train_loss)
        val_losses.append(val_loss)
    """
    ...

# ============================================================
# ۱۰. ثابت‌ها و تنظیمات
# ============================================================
# --- Device --- [Config]
CUDA: str = 'cuda'
CPU: str = 'cpu'
MPS: str = 'mps'

# --- dtype --- [Config]
FLOAT32: Any = torch.float32
FLOAT64: Any = torch.float64
INT64: Any = torch.int64
INT32: Any = torch.int32
UINT8: Any = torch.uint8
LONG: Any = torch.long

# --- مقادیر متداول --- [Config]
NUM_CLASSES: int = 10
BATCH_SIZE: int = 32
LEARNING_RATE: float = 0.001
NUM_EPOCHS: int = 10
IMAGE_SIZE: int = 224

# --- model حالت --- [Config] [Train]
TRAIN_MODE: str = 'train'
EVAL_MODE: str = 'eval'

# ============================================================
# ۱۱. الگوهای کامل (Templates)
# ============================================================
def template_training_loop(
    model: Any,
    train_loader: Any,
    val_loader: Any,
    criterion: Any,
    optimizer: Any,
    num_epochs: int,
    device: Any,
) -> None:
    """
    🏷️ [Main] [Train]

    📌 الگوی کامل training loop:

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = model.to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    train_losses = []
    val_losses = []

    for epoch in range(num_epochs):
        # ===== Training =====
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images = images.to(device)
            labels = labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        train_loss = running_loss / len(train_loader.dataset)
        train_acc = 100 * correct / total
        train_losses.append(train_loss)

        # ===== Validation =====
        model.eval()
        val_loss = 0.0
        correct = 0
        total = 0

        with torch.no_grad():
            for images, labels in val_loader:
                images = images.to(device)
                labels = labels.to(device)

                outputs = model(images)
                loss = criterion(outputs, labels)

                val_loss += loss.item() * images.size(0)
                _, predicted = torch.max(outputs, 1)
                total += labels.size(0)
                correct += (predicted == labels).sum().item()

        val_loss = val_loss / len(val_loader.dataset)
        val_acc = 100 * correct / total
        val_losses.append(val_loss)

        # ===== Print =====
        print(f'Epoch [{epoch+1}/{num_epochs}]')
        print(f'  Train Loss: {train_loss:.4f}, Train Acc: {train_acc:.2f}%')
        print(f'  Val   Loss: {val_loss:.4f}, Val   Acc: {val_acc:.2f}%')

    📌 نکات مهم:
    - model.train() قبل از training، model.eval() قبل از validation
    - optimizer.zero_grad() در ابتدای هر batch
    - loss.backward() بعد از محاسبه loss
    - optimizer.step() بعد از backward
    - با torch.no_grad() در validation
    """
    ...

def template_inference(model: Any, image_tensor: Any, device: Any) -> Tuple[int, float]:
    """
    🏷️ [Main] [Deploy]

    📌 الگوی inference تک تصویر:

    model.eval()
    with torch.no_grad():
        image_tensor = image_tensor.unsqueeze(0).to(device)  # اضافه کردن batch
        outputs = model(image_tensor)
        probabilities = torch.softmax(outputs, dim=1)
        confidence, predicted = torch.max(probabilities, 1)

    predicted_class = predicted.item()
    confidence_score = confidence.item()

    📌 پارامترها:
    - model: مدل آموزش دیده
    - image_tensor: تصویر preprocessed (CHW tensor)
    - device: cuda یا cpu

    📌 برمی‌گردونه: (کلاس پیش‌بینی شده, confidence)

    📌 نکته: حتماً model.eval() و torch.no_grad()
    """
    ...

def template_transfer_learning(num_classes: int, freeze_backbone: bool = True) -> Any:
    """
    🏷️ [Main] [Model]

    📌 الگوی Transfer Learning با ResNet:

    model = torchvision.models.resnet18(weights="DEFAULT")

    # Freeze backbone
    if freeze_backbone:
        for param in model.parameters():
            param.requires_grad = False

    # تغییر لایه آخر
    num_features = model.fc.in_features
    model.fc = nn.Linear(num_features, num_classes)

    # فقط لایه آخر trainable است
    optimizer = torch.optim.Adam(model.fc.parameters(), lr=0.001)

    📌 پارامترها:
    - num_classes: تعداد کلاس‌های پروژه
    - freeze_backbone: فریز کردن لایه‌های pretrained

    📌 برمی‌گردونه: مدل آماده آموزش

    📌 دو رویکرد:
    1. Feature Extraction: فریز همه، فقط train لایه آخر (داده کم)
    2. Fine-tuning: فریز نکن، train کل مدل با lr پایین (داده زیاد)

    # Fine-tuning:
    for param in model.parameters():
        param.requires_grad = True
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0001)  # lr پایین

    📌 نکته: از weights="DEFAULT" استفاده کن، نه pretrained=True (منسوخ شده)
    """
    ...

def template_save_checkpoint(
    model: Any,
    optimizer: Any,
    epoch: int,
    loss: float,
    accuracy: float,
    filepath: str,
) -> None:
    """
    🏷️ [Main] [Deploy]

    📌 الگوی ذخیره checkpoint:

    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'loss': loss,
        'accuracy': accuracy
    }
    torch.save(checkpoint, filepath)

    # لود برای ادامه آموزش:
    checkpoint = torch.load(filepath)
    model.load_state_dict(checkpoint['model_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']

    📌 پارامترها:
    - model: مدل
    - optimizer: optimizer
    - epoch: شماره epoch فعلی
    - loss: مقدار loss
    - accuracy: مقدار accuracy
    - filepath: مسیر ذخیره - رایج: 'best_model.pth', 'checkpoint.pth'
    """
    ...
# ============================================================
# dtype ها (ثابت‌های ماژول torch)
# ============================================================
float32: Any = ...
float64: Any = ...
float16: Any = ...
int64: Any = ...
int32: Any = ...
int16: Any = ...
int8: Any = ...
uint8: Any = ...
long: Any = ...
