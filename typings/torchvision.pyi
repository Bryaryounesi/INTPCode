from typing import Any, Tuple, Optional, Union, List, Dict

# ============================================================
# ماژول مجازی: torchvision.datasets
# ============================================================
class datasets:
    """
    🏷️ [I/O] [Data]

    📌 ماژول دیتاست‌های آماده در torchvision.
    """

    @staticmethod
    def MNIST(
        root: str,
        train: bool = True,
        download: bool = False,
        transform: Any = None,
    ) -> Any:
        """
        🏷️ [I/O] [Data]

        📌 دیتاست MNIST: ۷۰,۰۰۰ تصویر دست‌نویس سیاه‌وسفید (۲۸×۲۸) از رقم‌های ۰ تا ۹.

        📌 فرمول رایج:
        train_dataset = torchvision.datasets.MNIST(
            root="./data",
            train=True,
            download=True,
            transform=transforms.ToTensor()
        )

        📌 پارامترها:
        - root: مسیر پوشه‌ای که ساختار دیتاست در آن ساخته می‌شود
            رایج: "./data", "./datasets", path
        - train (اختیاری): بخش آموزشی یا تست - پیش‌فرض: True
            رایج: True (Train), False (Test)
        - download (اختیاری): دانلود خودکار - پیش‌فرض: False
            رایج: True, False
        - transform (اختیاری): تبدیل روی تصویر - پیش‌فرض: None
            رایج: transforms.ToTensor()

        📌 برمی‌گردونه: شیء شبیه لیست تنبل از تاپل‌های (image, label)
        """
        ...

    @staticmethod
    def CIFAR10(
        root: str,
        train: bool = True,
        download: bool = False,
        transform: Any = None,
    ) -> Any:
        """
        🏷️ [I/O] [Data]

        📌 دیتاست CIFAR-10: ۶۰,۰۰۰ تصویر رنگی (۳۲×۳۲) در ۱۰ کلاس.

        📌 فرمول رایج:
        train_dataset = torchvision.datasets.CIFAR10(
            root="./data",
            train=True,
            download=True,
            transform=transforms.ToTensor()
        )

        📌 پارامترها:
        - root: مسیر دیتاست - رایج: "./data"
        - train (اختیاری): بخش آموزشی یا تست - پیش‌فرض: True
        - download (اختیاری): دانلود خودکار - پیش‌فرض: False
        - transform (اختیاری): تبدیل روی تصویر - پیش‌فرض: None

        📌 برمی‌گردونه: شیء شبیه لیست تنبل از تاپل‌های (image, label)
        """
        ...

    @staticmethod
    def ImageFolder(root: str, transform: Any = None) -> Any:
        """
        🏷️ [I/O] [Data]

        📌 فرمول رایج:
        dataset = torchvision.datasets.ImageFolder(
            root='./data/train',
            transform=transform
        )

        📌 پارامترها:
        - root: مسیر پوشه داده (هر کلاس یک زیرپوشه) - رایج: './data/train'
        - transform (اختیاری): توابع preprocessing - پیش‌فرض: None

        📌 برمی‌گردونه: Dataset با کلاس‌های خودکار از نام پوشه‌ها

        📌 نکته: ساختار پوشه: root/class1/img1.jpg, root/class2/img2.jpg, ...
        """
        ...


# ============================================================
# ماژول مجازی: torchvision.transforms
# ============================================================
class transforms:
    """
    🏷️ [Preprocess] [Data]

    📌 ماژول ترنسفورم‌های تصویری در torchvision.
    """

    @staticmethod
    def Compose(transforms_list: List[Any]) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        📌 پارامترها:
        - transforms_list: لیست transformهای متوالی
            رایج: [ToTensor(), Resize(256), CenterCrop(224), Normalize(...)]

        📌 برمی‌گردونه: Callable که transformها را به ترتیب اعمال می‌کند

        📌 نکته: ترتیب مهم است! برای ورودی NumPy (OpenCV) اول ToTensor بیاید،
            چون بقیه transformها روی تنسور کار می‌کنند.
        📌 نکته: در training معمولاً ترتیب: Resize/Crop → ToTensor → Normalize
            ولی برای ورودی NumPy خام، ToTensor باید اول باشد.
        """
        ...

    @staticmethod
    def Resize(size: Union[int, Tuple[int, int]]) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.Resize((224, 224))
        transforms.Resize(256)

        📌 پارامترها:
        - size: ابعاد خروجی - رایج: (224, 224), 256

        📌 برمی‌گردونه: Transform برای تغییر اندازه

        📌 نکته: اگر یک عدد بدهی (مثل 256)، ضلع کوتاه‌تر به آن می‌رسد و
            نسبت تصویر حفظ می‌شود. (شبیه resize با حفظ نسبت در OpenCV)
        """
        ...

    @staticmethod
    def CenterCrop(size: Union[int, Tuple[int, int]]) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.CenterCrop(224)
        transforms.CenterCrop((224, 224))

        📌 پارامترها:
        - size: ابعاد crop

        📌 برمی‌گردونه: Transform برای برش مرکزی

        📌 نکته: مدل‌های ImageNet روی 224×224 آموزش دیده‌اند، پس قبل از
            استنتاج لازم است. (شبیه برش ROI با slicing)
        """
        ...

    @staticmethod
    def RandomHorizontalFlip(p: float = 0.5) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.RandomHorizontalFlip(p=0.5)

        📌 پارامترها:
        - p (اختیاری): احتمال flip - پیش‌فرض: 0.5

        📌 برمی‌گردونه: Transform برای flip افقی تصادفی

        📌 نکته: فقط در training استفاده کن (data augmentation).
        """
        ...

    @staticmethod
    def RandomRotation(degrees: Union[int, Tuple[int, int]]) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.RandomRotation(30)
        transforms.RandomRotation((-15, 15))

        📌 پارامترها:
        - degrees: محدوده چرخش - رایج: 30, 45, (-15, 15)

        📌 برمی‌گردونه: Transform برای چرخش تصادفی

        📌 نکته: فقط در training استفاده کن.
        """
        ...

    @staticmethod
    def ColorJitter(
        brightness: float = 0,
        contrast: float = 0,
        saturation: float = 0,
        hue: float = 0,
    ) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1)

        📌 پارامترها:
        - brightness (اختیاری): تغییر روشنایی - پیش‌فرض: 0
        - contrast (اختیاری): تغییر کنتراست - پیش‌فرض: 0
        - saturation (اختیاری): تغییر اشباع - پیش‌فرض: 0
        - hue (اختیاری): تغییر رنگ - پیش‌فرض: 0

        📌 برمی‌گردونه: Transform برای تغییر رنگ تصادفی

        📌 نکته: فقط در training استفاده کن.
        """
        ...

    @staticmethod
    def ToTensor() -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.ToTensor()

        📌 برمی‌گردونه: Transform برای تبدیل PIL Image / NumPy به Tensor

        📌 نکته: آرایه NumPy (H,W,C) با نوع uint8 را به تنسور (C,H,W) با نوع
            float32 و مقادیر 0 تا 1 تبدیل می‌کند. همان جابه‌جایی ابعاد
            که در جزوه‌ی NumPy دیدی.
        📌 نکته: برای ورودی NumPy (OpenCV)، این باید اولین transform باشد.
        """
        ...

    @staticmethod
    def Normalize(mean: List[float], std: List[float]) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])

        📌 پارامترها:
        - mean: میانگین هر کانال - رایج: [0.485, 0.456, 0.406] (ImageNet)
        - std: انحراف معیار هر کانال - رایج: [0.229, 0.224, 0.225] (ImageNet)

        📌 برمی‌گردونه: Transform برای نرمال‌سازی

        📌 نکته: از هر کانال میانگین کم و بر انحراف معیار تقسیم می‌کند.
        📌 نکته: اعداد ImageNet ثابت‌اند؛ اگر نرمال نکنی، مدل بدون ارور
            ولی با دقت پایین جواب می‌دهد؛ چون با همین اعداد آموزش دیده.
        """
        ...

    @staticmethod
    def Grayscale(num_output_channels: int = 1) -> Any:
        """
        🏷️ [Preprocess] [Data]

        📌 فرمول رایج:
        transforms.Grayscale(num_output_channels=1)

        📌 پارامترها:
        - num_output_channels (اختیاری): تعداد کانال خروجی - پیش‌فرض: 1

        📌 برمی‌گردونه: Transform برای خاکستری کردن
        """
        ...


# ============================================================
# ماژول مجازی: torchvision.models
# ============================================================
class models:
    """
    🏷️ [Analyze/Detect] [Model]

    📌 ماژول مدل‌های آماده در torchvision.
    """

    @staticmethod
    def resnet18(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.resnet18(weights="DEFAULT")
        model = torchvision.models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
        model = torchvision.models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
        model = torchvision.models.resnet18()   # بدون وزن (خام)

        📌 پارامترها:
        - weights (اختیاری): وزن‌های پیش‌آموزش‌دیده - پیش‌فرض: None
            رایج: "DEFAULT", models.ResNet18_Weights.DEFAULT,
                  models.ResNet18_Weights.IMAGENET1K_V1
            None = مدل خام (وزن‌های تصادفی، پیش‌بینی بی‌معنی)
            "DEFAULT" = بهترین وزن‌های موجود (معمولاً IMAGENET1K_V1)

        📌 برمی‌گردونه: مدل ResNet-18 (شیء nn.Module)

        📌 نکته: سبک (~۴۵ مگابایت)، مناسب شروع و اجرا روی CPU.
        📌 نکته: برای ساخت مدل با وزن آماده، بار اول نیاز به اینترنت دارد
            (بعد از آن در پوشه‌ی کش ذخیره می‌شود).
        """
        ...

    @staticmethod
    def resnet50(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.resnet50(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل ResNet-50 (~۱۰۰ مگابایت)

        📌 نکته: سنگین‌تر از resnet18، دقت بالاتر، مناسب GPU.
        """
        ...

    @staticmethod
    def vgg16(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.vgg16(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل VGG-16 (~۵۲۸ مگابایت - سنگین)

        📌 نکته: برای CPU مناسب نیست (کند و پرحجم).
        """
        ...

    @staticmethod
    def mobilenet_v2(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.mobilenet_v2(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل MobileNet-V2 (~۱۴ مگابایت - سبک‌ترین)

        📌 نکته: مناسب CPU، گوشی و لبه (edge).
        """
        ...

    @staticmethod
    def mobilenet_v3(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.mobilenet_v3(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل MobileNet-V3 (نسخه جدید V2)

        📌 نکته: بهینه‌تر از V2 برای دستگاه‌های لبه.
        """
        ...

    @staticmethod
    def efficientnet_b0(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.efficientnet_b0(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل EfficientNet-B0

        📌 نکته: تعادل خوب بین دقت و سرعت روی CPU.
        """
        ...

    @staticmethod
    def efficientnet_b3(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.efficientnet_b3(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل EfficientNet-B3

        📌 نکته: دقت بالاتر، مناسب GPU.
        """
        ...

    @staticmethod
    def vit_b_16(weights: Any = None) -> Any:
        """
        🏷️ [Analyze/Detect] [Model]

        📌 فرمول رایج:
        model = torchvision.models.vit_b_16(weights="DEFAULT")

        📌 پارامترها:
        - weights (اختیاری): وزن‌های ImageNet - پیش‌فرض: None

        📌 برمی‌گردونه: مدل Vision Transformer (ViT-B/16)

        📌 نکته: معماری جدید (Transformer به‌جای CNN). آموزش روی ImageNet-21k.
        """
        ...

    # ============================================================
    # شیء وزن‌ها (weights enum) — به عنوان attribute کلاس models
    # ============================================================
    # 📌 هر مدل معروف، یک کلاس enum از وزن‌هایش دارد، مثل ResNet18_Weights.
    # 📌 این شیء سه کاربرد اصلی دارد:
    #     ۱. ساخت مدل:   model = resnet18(weights=ResNet18_Weights.DEFAULT)
    #     ۲. اسم کلاس‌ها: class_names = ResNet18_Weights.DEFAULT.meta["categories"]
    #     ۳. transform آماده: transform = ResNet18_Weights.DEFAULT.transforms()
    # ============================================================

    class ResNet18_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.ResNet18_Weights.DEFAULT
        model = models.resnet18(weights=weights)
        class_names = weights.meta["categories"]
        transform = weights.transforms()

        📌 مقادیر رایج:
        - DEFAULT: بهترین وزن‌های موجود (معمولاً IMAGENET1K_V1)
        - IMAGENET1K_V1: وزن‌های آموزش‌دیده روی ImageNet-1K (نسخه ۱)

        📌 attribute ها:
        - meta: دیکشنری شامل متادیتای وزن‌ها
            meta["categories"] = لیست ۱۰۰۰ اسم کلاس به ترتیب خروجی مدل
        - transforms(): پایپلاین آماده‌ی همان مدل

        📌 نکته: class_names[predicted_class.item()] اسم واقعی کلاس
            را می‌دهد (مثلاً "tabby cat").
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any:
            """
            🏷️ [Preprocess] [Data]

            📌 فرمول رایج:
            transform = weights.transforms()
            input_tensor = transform(tensor)

            📌 برمی‌گردونه: پایپلاین transforms آماده برای همان مدل

            📌 نکته: ورودی این transform تنسور [C,H,W] است (نه آرایه NumPy خام).
                پس اگر ورودی NumPy/OpenCV داری، اول با ToTensor یا
                torch.from_numpy + permute به تنسور تبدیل کن.
            """
            ...

    class ResNet50_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.ResNet50_Weights.DEFAULT
        model = models.resnet50(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1, IMAGENET1K_V2

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"] = لیست ۱۰۰۰ اسم کلاس)
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        IMAGENET1K_V2: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...

    class VGG16_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.VGG16_Weights.DEFAULT
        model = models.vgg16(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"])
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...

    class MobileNet_V2_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.MobileNet_V2_Weights.DEFAULT
        model = models.mobilenet_v2(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1, IMAGENET1K_V2

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"])
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        IMAGENET1K_V2: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...

    class MobileNet_V3_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.MobileNet_V3_Weights.DEFAULT
        model = models.mobilenet_v3(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"])
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...

    class EfficientNet_B0_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.EfficientNet_B0_Weights.DEFAULT
        model = models.efficientnet_b0(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"])
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...

    class EfficientNet_B3_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.EfficientNet_B3_Weights.DEFAULT
        model = models.efficientnet_b3(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"])
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...

    class ViT_B_16_Weights:
        """
        🏷️ [Config] [Model]

        📌 فرمول رایج:
        weights = models.ViT_B_16_Weights.DEFAULT
        model = models.vit_b_16(weights=weights)

        📌 مقادیر: DEFAULT, IMAGENET1K_V1, IMAGENET1K_SWAG_E2E_V1,
                   IMAGENET1K_SWAG_LINEAR_V1

        📌 attribute ها:
        - meta: دیکشنری متادیتا (meta["categories"])
        - transforms(): پایپلاین آماده
        """

        DEFAULT: Any
        IMAGENET1K_V1: Any
        meta: Dict[str, Any]

        @staticmethod
        def transforms() -> Any: ...