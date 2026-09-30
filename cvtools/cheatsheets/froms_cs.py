class FromsCheatSheet:
    """
    🏷️ [Froms]

    📌 چیت‌شیت تعاملی `from xxx import yyy` برای کتابخانه‌های کامپیوتر ویژن.

    📌 با نوشتن cvt.froms.<name> کد ایمپورت را هاور کنید.

    📌 مثال:
        cvt.froms.pathlib_path         → from pathlib import Path
        cvt.froms.torchvision_transforms → from torchvision import transforms
    """

    # ------------------------------------------
    # pathlib
    # ------------------------------------------
    @property
    def pathlib_path(self):
        """
        🏷️ [From] [pathlib]

        📌 from pathlib import Path

        📌 کاربرد: کار شیءگرا با مسیر فایل‌ها
        """
        return "from pathlib import Path"

    # ------------------------------------------
    # torch
    # ------------------------------------------
    @property
    def torch_nn(self):
        """
        🏷️ [From] [torch]

        📌 from torch import nn

        📌 کاربرد: لایه‌ها، lossها، ماژول‌های شبکه
        """
        return "from torch import nn"

    @property
    def torch_optim(self):
        """
        🏷️ [From] [torch]

        📌 from torch import optim

        📌 کاربرد: بهینه‌سازها (Adam, SGD, ...)
        """
        return "from torch import optim"

    @property
    def torch_utils_data_dataloader(self):
        """
        🏷️ [From] [torch.utils.data]

        📌 from torch.utils.data import DataLoader

        📌 کاربرد: بارگذاری دسته‌ای داده در آموزش
        """
        return "from torch.utils.data import DataLoader"

    @property
    def torch_utils_data_dataset(self):
        """
        🏷️ [From] [torch.utils.data]

        📌 from torch.utils.data import Dataset

        📌 کاربرد: کلاس پایه برای دیتاست سفارشی
        """
        return "from torch.utils.data import Dataset"

    @property
    def torch_utils_data_random_split(self):
        """
        🏷️ [From] [torch.utils.data]

        📌 from torch.utils.data import random_split

        📌 کاربرد: تقسیم دیتاست به train/val
        """
        return "from torch.utils.data import random_split"

    @property
    def torch_utils_data_subset(self):
        """
        🏷️ [From] [torch.utils.data]

        📌 from torch.utils.data import Subset

        📌 کاربرد: انتخاب زیرمجموعه‌ای از دیتاست
        """
        return "from torch.utils.data import Subset"

    @property
    def torch_nn_functional(self):
        """
        🏷️ [From] [torch.nn]

        📌 from torch.nn import functional as F

        📌 کاربرد: توابع بدون state (relu, softmax, conv2d, ...)
        """
        return "from torch.nn import functional as F"

    # ------------------------------------------
    # torchvision
    # ------------------------------------------
    @property
    def torchvision_transforms(self):
        """
        🏷️ [From] [torchvision]

        📌 from torchvision import transforms

        📌 کاربرد: پیش‌پردازش و data augmentation
        """
        return "from torchvision import transforms"

    @property
    def torchvision_datasets(self):
        """
        🏷️ [From] [torchvision]

        📌 from torchvision import datasets

        📌 کاربرد: دیتاست‌های آماده (MNIST, CIFAR10, ...)
        """
        return "from torchvision import datasets"

    @property
    def torchvision_models(self):
        """
        🏷️ [From] [torchvision]

        📌 from torchvision import models

        📌 کاربرد: مدل‌های pretrained (ResNet, VGG, ...)
        """
        return "from torchvision import models"

    @property
    def torchvision_transforms_functional(self):
        """
        🏷️ [From] [torchvision]

        📌 from torchvision.transforms import functional as TF

        📌 کاربرد: توابع transform روی tensor/PIL
        """
        return "from torchvision.transforms import functional as TF"

    # ------------------------------------------
    # OpenCV
    # ------------------------------------------
    @property
    def cv2_data(self):
        """
        🏷️ [From] [cv2]

        📌 from cv2 import data

        📌 کاربرد: مسیر فایل‌های haarcascade
        """
        return "from cv2 import data"

    # ------------------------------------------
    # PIL
    # ------------------------------------------
    @property
    def PIL_image(self):
        """
        🏷️ [From] [PIL]

        📌 from PIL import Image

        📌 کاربرد: باز کردن و ذخیره تصویر
        """
        return "from PIL import Image"

    @property
    def PIL_imageops(self):
        """
        🏷️ [From] [PIL]

        📌 from PIL import ImageOps

        📌 کاربرد: عملیات رایج روی تصویر (grayscale, flip, ...)
        """
        return "from PIL import ImageOps"

    # ------------------------------------------
    # matplotlib
    # ------------------------------------------
    @property
    def matplotlib_pyplot(self):
        """
        🏷️ [From] [matplotlib]

        📌 from matplotlib import pyplot as plt

        📌 کاربرد: رسم و نمایش تصویر
        """
        return "from matplotlib import pyplot as plt"

    # ------------------------------------------
    # sklearn
    # ------------------------------------------
    @property
    def sklearn_metrics(self):
        """
        🏷️ [From] [sklearn]

        📌 from sklearn import metrics

        📌 کاربرد: معیارهای ارزیابی (accuracy, f1, ...)
        """
        return "from sklearn import metrics"

    @property
    def sklearn_model_selection_train_test_split(self):
        """
        🏷️ [From] [sklearn]

        📌 from sklearn.model_selection import train_test_split

        📌 کاربرد: تقسیم داده به train/test
        """
        return "from sklearn.model_selection import train_test_split"

    # ------------------------------------------
    # transformers
    # ------------------------------------------
    @property
    def transformers_auto_model(self):
        """
        🏷️ [From] [transformers]

        📌 from transformers import AutoModel

        📌 کاربرد: بارگذاری خودکار مدل pretrained
        """
        return "from transformers import AutoModel"

    @property
    def transformers_auto_processor(self):
        """
        🏷️ [From] [transformers]

        📌 from transformers import AutoProcessor

        📌 کاربرد: پیش‌پردازش خودکار برای مدل
        """
        return "from transformers import AutoProcessor"

    # ------------------------------------------
    # typing
    # ------------------------------------------
    @property
    def typing_list_dict_optional(self):
        """
        🏷️ [From] [typing]

        📌 from typing import List, Dict, Optional

        📌 کاربرد: type hints رایج
        """
        return "from typing import List, Dict, Optional"

    @property
    def typing_union(self):
        """
        🏷️ [From] [typing]

        📌 from typing import Union

        📌 کاربرد: نوع چندگانه برای یک متغیر
        """
        return "from typing import Union"

    # ------------------------------------------
    # collections
    # ------------------------------------------
    @property
    def collections_counter(self):
        """
        🏷️ [From] [collections]

        📌 from collections import Counter

        📌 کاربرد: شمارش عناصر (مثلاً تعداد کلاس‌ها)
        """
        return "from collections import Counter"

    @property
    def collections_ordereddict(self):
        """
        🏷️ [From] [collections]

        📌 from collections import OrderedDict

        📌 کاربرد: دیکشنری با ترتیب حفظ‌شده
        """
        return "from collections import OrderedDict"

    # ------------------------------------------
    # functools
    # ------------------------------------------
    @property
    def functools_partial(self):
        """
        🏷️ [From] [functools]

        📌 from functools import partial

        📌 کاربرد: ساخت تابع با آرگومان‌های پیش‌فرض
        """
        return "from functools import partial"
