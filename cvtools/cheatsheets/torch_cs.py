class TorchUtils:
    """
    🏷️ [Utils]

    📌 چیت‌شیت تعاملی PyTorch.

    📌 با نوشتن cvt.torch.<name> می‌توانید فرمول و پارامترهای آن را هاور کنید.
    """

    # ------------------------------------------
    # torch.utils.data
    # ------------------------------------------
    @property
    def dataloader(self):
        """
        🏷️ [Data]

        📌 فرمول رایج:
        train_loader = DataLoader(
            train_dataset,
            batch_size=64,
            shuffle=True,
            generator=torch.Generator().manual_seed(2)
        )

        📌 پارامترها:
        - dataset: دیتاست (مثل خروجی torchvision.datasets.MNIST)
        - batch_size (اختیاری): تعداد نمونه در هر دسته - پیش‌فرض: 1
            رایج: 32, 64, 128
        - shuffle (اختیاری): به‌هم‌ریختن ترتیب داده‌ها در هر epoch - پیش‌فرض: False
            رایج: True (برای Train), False (برای Test/Validation)
        - num_workers (اختیاری): تعداد پردازش‌های موازی برای آماده‌سازی داده - پیش‌فرض: 0
            رایج: 0 (ساده), 2, 4 (برای CPU چند هسته‌ای)
        - generator (اختیاری): تولیدکننده اعداد تصادفی برای تکرارپذیری shuffle - پیش‌فرض: None
            رایج: torch.Generator().manual_seed(42)
        - pin_memory (اختیاری): انتقال سریع‌تر داده به GPU - پیش‌فرض: False
            رایج: True (اگر GPU دارید)
        - drop_last (اختیاری): حذف آخرین دسته ناقص - پیش‌فرض: False
            رایج: True (در آموزش)

        📌 برمی‌گردونه: شیء قابل پیمایش (Iterable) از دسته‌های [images, labels]
        """
        return "DataLoader"

    @property
    def dataset(self):
        """
        🏷️ [Data]

        📌 کلاس پایه برای ساخت دیتاست سفارشی.

        📌 فرمول رایج:
        from torch.utils.data import Dataset

        class MyDataset(Dataset):
            def __init__(self, ...):
                ...
            def __len__(self):
                return len(self.data)
            def __getitem__(self, idx):
                return self.data[idx], self.labels[idx]

        📌 متدهای اجباری:
        - __len__: تعداد نمونه‌ها
        - __getitem__: برگرداندن یک نمونه بر اساس ایندکس

        📌 برمی‌گردونه: کلاس پایه دیتاست
        """
        return "Dataset"

    @property
    def subset(self):
        """
        🏷️ [Data]

        📌 انتخاب زیرمجموعه‌ای از ایندکس‌های دیتاست.

        📌 فرمول رایج:
        from torch.utils.data import Subset
        subset = Subset(train_dataset, list(range(100)))

        📌 پارامترها:
        - dataset: دیتاست اصلی
        - indices: لیست ایندکس‌های موردنظر

        📌 برمی‌گردونه: زیرمجموعه‌ای از دیتاست اصلی
        """
        return "Subset"

    @property
    def random_split(self):
        """
        🏷️ [Data]

        📌 تقسیم دیتاست به چند زیرمجموعه تصادفی (مثل Train/Validation).

        📌 فرمول رایج:
        from torch.utils.data import random_split
        train_set, val_set = random_split(dataset, [0.8, 0.2])

        📌 پارامترها:
        - dataset: دیتاست اصلی
        - lengths: لیست طول‌ها یا نسبت‌ها
        - generator (اختیاری): برای تکرارپذیری - پیش‌فرض: None

        📌 برمی‌گردونه: لیستی از زیرمجموعه‌ها
        """
        return "random_split"

    # ------------------------------------------
    # torch.optim
    # ------------------------------------------
    @property
    def adam(self):
        """
        🏷️ [Optim]

        📌 فرمول رایج:
        optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

        📌 پارامترها:
        - params: پارامترهای مدل (model.parameters())
        - lr (اختیاری): نرخ یادگیری - پیش‌فرض: 1e-3
            رایج: 1e-3, 1e-4
        - betas (اختیاری): ضرایب میانگین متحرک - پیش‌فرض: (0.9, 0.999)
        - eps (اختیاری): مقدار کوچک - پیش‌فرض: 1e-8
        - weight_decay (اختیاری): جریمه L2 - پیش‌فرض: 0
            رایج: 1e-4, 1e-5
        - amsgrad (اختیاری): استفاده از AMSGrad - پیش‌فرض: False

        📌 برمی‌گردونه: بهینه‌ساز Adam
        """
        return "torch.optim.Adam"

    @property
    def sgd(self):
        """
        🏷️ [Optim]

        📌 فرمول رایج:
        optimizer = torch.optim.SGD(
            model.parameters(),
            lr=0.01,
            momentum=0.9
        )

        📌 پارامترها:
        - params: پارامترهای مدل
        - lr (اختیاری): نرخ یادگیری - پیش‌فرض: 1e-2
        - momentum (اختیاری): مومنتوم - پیش‌فرض: 0
            رایج: 0.9
        - weight_decay (اختیاری): جریمه L2 - پیش‌فرض: 0
        - dampening (اختیاری): میراکننده مومنتوم - پیش‌فرض: 0
        - nesterov (اختیاری): استفاده از Nesterov - پیش‌فرض: False

        📌 برمی‌گردونه: بهینه‌ساز SGD
        """
        return "torch.optim.SGD"

    @property
    def rmsprop(self):
        """
        🏷️ [Optim]

        📌 فرمول رایج:
        optimizer = torch.optim.RMSprop(model.parameters(), lr=0.01)

        📌 پارامترها:
        - params: پارامترهای مدل
        - lr (اختیاری): نرخ یادگیری - پیش‌فرض: 1e-2
        - alpha (اختیاری): ضریب هموارسازی - پیش‌فرض: 0.99
        - eps (اختیاری): مقدار کوچک - پیش‌فرض: 1e-8
        - weight_decay (اختیاری): جریمه L2 - پیش‌فرض: 0
        - momentum (اختیاری): مومنتوم - پیش‌فرض: 0

        📌 برمی‌گردونه: بهینه‌ساز RMSprop
        """
        return "torch.optim.RMSprop"

    @property
    def lr_scheduler_step(self):
        """
        🏷️ [Optim]

        📌 فرمول رایج:
        scheduler = torch.optim.lr_scheduler.StepLR(
            optimizer,
            step_size=10,
            gamma=0.1
        )

        📌 پارامترها:
        - optimizer: بهینه‌ساز
        - step_size: هر چند epoch کاهش یابد
        - gamma: ضریب کاهش

        📌 برمی‌گردونه: زمان‌بند نرخ یادگیری
        """
        return "StepLR"

    # ------------------------------------------
    # torch.nn (Losses)
    # ------------------------------------------
    @property
    def cross_entropy(self):
        """
        🏷️ [Loss]

        📌 فرمول رایج:
        criterion = torch.nn.CrossEntropyLoss()

        📌 پارامترها:
        - weight (اختیاری): وزن کلاس‌ها - پیش‌فرض: None
        - ignore_index (اختیاری): ایندکسی که نادیده گرفته می‌شود - پیش‌فرض: -100
        - reduction (اختیاری): نحوه کاهش - پیش‌فرض: "mean"
            رایج: "mean", "sum", "none"
        - label_smoothing (اختیاری): هموارسازی برچسب - پیش‌فرض: 0.0

        📌 برمی‌گردونه: تابع خطای CrossEntropy (برای طبقه‌بندی چندکلاسه)
        """
        return "nn.CrossEntropyLoss"

    @property
    def bce_loss(self):
        """
        🏷️ [Loss]

        📌 فرمول رایج:
        criterion = torch.nn.BCELoss()

        📌 پارامترها:
        - weight (اختیاری): وزن - پیش‌فرض: None
        - reduction (اختیاری): نحوه کاهش - پیش‌فرض: "mean"

        📌 برمی‌گردونه: تابع خطای Binary Cross Entropy (برای طبقه‌بندی دودویی)
        """
        return "nn.BCELoss"

    @property
    def bce_with_logits(self):
        """
        🏷️ [Loss]

        📌 فرمول رایج:
        criterion = torch.nn.BCEWithLogitsLoss()

        📌 برمی‌گردونه: نسخه پایدارتر BCE با سیگموئید داخلی
        """
        return "nn.BCEWithLogitsLoss"

    @property
    def mse_loss(self):
        """
        🏷️ [Loss]

        📌 فرمول رایج:
        criterion = torch.nn.MSELoss()

        📌 پارامترها:
        - reduction (اختیاری): نحوه کاهش - پیش‌فرض: "mean"

        📌 برمی‌گردونه: تابع خطای Mean Squared Error (برای رگرسیون)
        """
        return "nn.MSELoss"

    @property
    def l1_loss(self):
        """
        🏷️ [Loss]

        📌 فرمول رایج:
        criterion = torch.nn.L1Loss()

        📌 برمی‌گردونه: تابع خطای Mean Absolute Error
        """
        return "nn.L1Loss"

    # ------------------------------------------
    # torch.nn (Layers)
    # ------------------------------------------
    @property
    def linear(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.Linear(in_features=128, out_features=10)

        📌 پارامترها:
        - in_features: تعداد ورودی
        - out_features: تعداد خروجی
        - bias (اختیاری): استفاده از بایاس - پیش‌فرض: True

        📌 برمی‌گردونه: لایه خطی (Fully Connected)
        """
        return "nn.Linear"

    @property
    def conv2d(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.Conv2d(
            in_channels=3,
            out_channels=16,
            kernel_size=3,
            stride=1,
            padding=1
        )

        📌 پارامترها:
        - in_channels: تعداد کانال ورودی
        - out_channels: تعداد کانال خروجی
        - kernel_size: اندازه فیلتر
        - stride (اختیاری): گام - پیش‌فرض: 1
        - padding (اختیاری): پدینگ - پیش‌فرض: 0
        - dilation (اختیاری): دیلیشن - پیش‌فرض: 1
        - groups (اختیاری): تعداد گروه‌ها - پیش‌فرض: 1
        - bias (اختیاری): استفاده از بایاس - پیش‌فرض: True
        - padding_mode (اختیاری): حالت پدینگ - پیش‌فرض: "zeros"

        📌 برمی‌گردونه: لایه کانولوشن دوبعدی
        """
        return "nn.Conv2d"

    @property
    def maxpool2d(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.MaxPool2d(kernel_size=2, stride=2)

        📌 پارامترها:
        - kernel_size: اندازه پنجره
        - stride (اختیاری): گام - پیش‌فرض: None (برابر kernel_size)
        - padding (اختیاری): پدینگ - پیش‌فرض: 0
        - dilation (اختیاری): دیلیشن - پیش‌فرض: 1
        - return_indices (اختیاری): برگرداندن ایندکس‌ها - پیش‌فرض: False
        - ceil_mode (اختیاری): حالت سقف - پیش‌فرض: False

        📌 برمی‌گردونه: لایه MaxPooling دوبعدی
        """
        return "nn.MaxPool2d"

    @property
    def avgpool2d(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.AvgPool2d(kernel_size=2, stride=2)

        📌 برمی‌گردونه: لایه Average Pooling دوبعدی
        """
        return "nn.AvgPool2d"

    @property
    def batchnorm2d(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.BatchNorm2d(num_features=16)

        📌 پارامترها:
        - num_features: تعداد کانال‌ها
        - eps (اختیاری): مقدار کوچک - پیش‌فرض: 1e-5
        - momentum (اختیاری): مومنتوم - پیش‌فرض: 0.1
        - affine (اختیاری): پارامترهای قابل یادگیری - پیش‌فرض: True
        - track_running_stats (اختیاری): ردیابی آمار - پیش‌فرض: True

        📌 برمی‌گردونه: لایه BatchNorm دوبعدی
        """
        return "nn.BatchNorm2d"

    @property
    def dropout(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.Dropout(p=0.5)

        📌 پارامترها:
        - p (اختیاری): احتمال حذف - پیش‌فرض: 0.5
        - inplace (اختیاری): انجام درجا - پیش‌فرض: False

        📌 برمی‌گردونه: لایه Dropout
        """
        return "nn.Dropout"

    @property
    def flatten(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        layer = torch.nn.Flatten()

        📌 پارامترها:
        - start_dim (اختیاری): بعد شروع - پیش‌فرض: 1
        - end_dim (اختیاری): بعد پایان - پیش‌فرض: -1

        📌 برمی‌گردونه: لایه صاف‌کننده
        """
        return "nn.Flatten"

    @property
    def relu(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        activation = torch.nn.ReLU()

        📌 برمی‌گردونه: تابع فعال‌سازی ReLU
        """
        return "nn.ReLU"

    @property
    def sigmoid(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        activation = torch.nn.Sigmoid()

        📌 برمی‌گردونه: تابع فعال‌سازی Sigmoid
        """
        return "nn.Sigmoid"

    @property
    def softmax(self):
        """
        🏷️ [Layer]

        📌 فرمول رایج:
        activation = torch.nn.Softmax(dim=1)

        📌 برمی‌گردونه: تابع فعال‌سازی Softmax
        """
        return "nn.Softmax"

    # ------------------------------------------
    # torchvision.models
    # ------------------------------------------
    @property
    def resnet18(self):
        """
        🏷️ [Model]

        📌 فرمول رایج:
        model = torchvision.models.resnet18(pretrained=True)
        model.fc = torch.nn.Linear(512, 10)  # تغییر لایه آخر

        📌 پارامترها:
        - pretrained (اختیاری): استفاده از وزن‌های ImageNet - پیش‌فرض: False

        📌 برمی‌گردونه: مدل ResNet-18
        """
        return "torchvision.models.resnet18"

    @property
    def resnet50(self):
        """
        🏷️ [Model]

        📌 فرمول رایج:
        model = torchvision.models.resnet50(pretrained=True)
        model.fc = torch.nn.Linear(2048, 10)

        📌 برمی‌گردونه: مدل ResNet-50
        """
        return "torchvision.models.resnet50"

    @property
    def vgg16(self):
        """
        🏷️ [Model]

        📌 فرمول رایج:
        model = torchvision.models.vgg16(pretrained=True)

        📌 برمی‌گردونه: مدل VGG-16
        """
        return "torchvision.models.vgg16"

    @property
    def mobilenet_v2(self):
        """
        🏷️ [Model]

        📌 فرمول رایج:
        model = torchvision.models.mobilenet_v2(pretrained=True)

        📌 برمی‌گردونه: مدل MobileNet-V2
        """
        return "torchvision.models.mobilenet_v2"

    @property
    def efficientnet_b0(self):
        """
        🏷️ [Model]

        📌 فرمول رایج:
        model = torchvision.models.efficientnet_b0(pretrained=True)

        📌 برمی‌گردونه: مدل EfficientNet-B0
        """
        return "torchvision.models.efficientnet_b0"

    # ------------------------------------------
    # torch.utils (Misc)
    # ------------------------------------------
    @property
    def manual_seed(self):
        """
        🏷️ [Utils]

        📌 فرمول رایج:
        torch.manual_seed(42)

        📌 پارامترها:
        - seed: بذر تصادفی

        📌 برمی‌گردونه: Generator با بذر تنظیم‌شده
        """
        return "torch.manual_seed"

    @property
    def save(self):
        """
        🏷️ [Utils]

        📌 فرمول رایج:
        torch.save(model.state_dict(), "model.pth")

        📌 پارامترها:
        - obj: شیء موردنظر برای ذخیره
        - f: مسیر فایل
        """
        return "torch.save"

    @property
    def load(self):
        """
        🏷️ [Utils]

        📌 فرمول رایج:
        state = torch.load("model.pth")

        📌 پارامترها:
        - f: مسیر فایل

        📌 برمی‌گردونه: شیء بارگذاری‌شده
        """
        return "torch.load"

    @property
    def cuda_is_available(self):
        """
        🏷️ [Utils]

        📌 فرمول رایج:
        torch.cuda.is_available()

        📌 برمی‌گردونه: True اگر GPU موجود باشد
        """
        return "torch.cuda.is_available"

    @property
    def device(self):
        """
        🏷️ [Utils]

        📌 فرمول رایج:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        📌 برمی‌گردونه: دستگاه محاسباتی (CPU یا GPU)
        """
        return "torch.device"

    @property
    def no_grad(self):
        """
        🏷️ [Utils]

        📌 فرمول رایج:
        with torch.no_grad():
            output = model(input)

        📌 کاربرد: غیرفعال کردن محاسبه گرادیان در زمان ارزیابی
        """
        return "torch.no_grad"
