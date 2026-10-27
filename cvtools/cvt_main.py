"""
cvtools module — Personal Computer Vision Toolbox

This module provides a collection of helper functions and utilities for OpenCV projects,
reducing repetitive and lengthy code.

Goal: Focus on core computer vision concepts without getting bogged down in boilerplate.

Current Features:
• cvt.imshow()   → Display image with keyboard zoom (+ - q n)
• cvt.rotate()   → Rotate image without cropping corners (auto 4-step)
• cvt.resize()   → Resize by providing only one dimension
• cvt.search_path() → Search for files or folders in the entire project and insert their paths as hashtagged comments
• cvt.rename_data() → Rename all images in a folder with sequential numbers or alphabetical names
• cvt.scan_data() → Scan and separate bad images (corrupt, small, bad ratio, duplicate, noisy, low contrast)
• cvt.slider()   → Interactive slider window for threshold, edge detection, and blur
• cvt.find_level() → Find the processing level (Config, Preprocess, Analyze, Visualize, Main) of OpenCV functions
• cvt.torch.*    → Interactive PyTorch Cheat Sheet (hover for DataLoader, optimizers, losses, models, etc.)
• cvt.imports.*  → Interactive Import Cheat Sheet (hover for `import xxx` statements)
• cvt.froms.*    → Interactive From-Import Cheat Sheet (hover for `from xxx import yyy` statements)
• cvt.h.*        → Interactive Python & CV Hints Cheat Sheet (hover for patterns, operators, conventions)

Usage:
import cv2
from cvtools import cvt
img = cv2.imread("image.jpg")
# ------------------
rotated = cvt.rotate(img, 45)
# ------------------
cvt.imshow("win", rotated)
# ------------------
cv2.imwrite("output.jpg", rotated)
# ------------------
resized = cvt.resize(img, new_w=800)
# ------------------
cvt.search_path("pandas_cheatsheet.py")
cvt.search_path("my_image")
cvt.search_path(["utils.py", "data/", "models"])
# ------------------
cvt.rename_data("dataset/train/")
cvt.rename_data("dataset/train/", prefix="cat_", start=100)
cvt.rename_data("dataset/train/", mode='alpha', prefix="img_")
# ------------------
cvt.scan_data("dataset/")
cvt.scan_data("dataset/", contrast=30)
# ------------------
cvt.slider("win", img)
cvt.slider("win", img, thresh='simple')
cvt.slider("win", img, thresh='otsu')
cvt.slider("win", img, thresh='adapt')
cvt.slider("win", img, edge='canny')
cvt.slider("win", img, blur='gaussian', edge='canny')
cvt.slider("win", img, thresh='simple', blur='median')
cvt.slider("win", img, thresh='simple', contour=True)
# ------------------
# Find level of OpenCV functions:
cvt.find_level('drawContours')
cvt.find_level(['CLAHE', 'threshold', 'SIFT'])
cvt.find_level(['draw', 'contour', 'hough'])
# -------------------------
# PyTorch Cheat Sheet:
cvt.torch.dataloader       # hover: DataLoader formula & params
cvt.torch.dataset          # hover: Dataset base class
cvt.torch.adam             # hover: Adam optimizer
cvt.torch.sgd              # hover: SGD optimizer
cvt.torch.cross_entropy    # hover: CrossEntropyLoss
cvt.torch.linear           # hover: nn.Linear
cvt.torch.conv2d           # hover: nn.Conv2d
cvt.torch.resnet18         # hover: ResNet-18 model
# -------------------------
# Import Cheat Sheet:
cvt.imports.numpy          # hover: import numpy as np
cvt.imports.torch          # hover: import torch
cvt.imports.cv2            # hover: import cv2
cvt.imports.pandas         # hover: import pandas as pd
# -------------------------
# From-Import Cheat Sheet:
cvt.froms.pathlib_path     # hover: from pathlib import Path
cvt.froms.torchvision_transforms  # hover: from torchvision import transforms
cvt.froms.torch_utils_data_dataloader  # hover: from torch.utils.data import DataLoader
# -------------------------
# Python & CV Hints Cheat Sheet:
cvt.h.if_conf          # hover: الگوی شرط روی confidence
cvt.h.if_none          # hover: بررسی None در خواندن تصویر
cvt.h.for_enum         # hover: پیمایش دیتاست با ایندکس
cvt.h.for_batch        # hover: پردازش دسته‌ای (batch)
cvt.h.with_open        # hover: باز کردن فایل با context manager
cvt.h.try_file         # hover: خواندن ایمن فایل
cvt.h.f_2f             # hover: فرمت اعشار در f-string
cvt.h.f_pad            # hover: شماره‌گذاری با صفر
cvt.h.lc_filter        # hover: فیلتر با list comprehension
cvt.h.lc_nested        # hover: کامپرهنشن تودرتو برای تصویر
cvt.h.dc_transform     # hover: dict comprehension
cvt.h.sort_key         # hover: مرتب‌سازی با کلید سفارشی
cvt.h.op_gt            # hover: اپراتور بزرگ‌تر
cvt.h.op_walrus        # hover: عملگر والرس
cvt.h.naming           # hover: قراردادهای نام‌گذاری
cvt.h.main_guard       # hover: if __name__ == "__main__"
cvt.h.slice_syntax     # hover: برش در پایتون
cvt.h.unpacking        # hover: unpacking
# -------------------------
Future: Any frequently used utility requiring repetitive code
will be added to this module.
"""

# --------------------------------------------------------
# Module Code
# --------------------------------------------------------

import sys
from pathlib import Path

_self_dir = Path(__file__).parent.resolve()
if str(_self_dir) not in sys.path:
    sys.path.insert(0, str(_self_dir))

import cv2
import os
import inspect
import numpy as np
import shutil
import hashlib
import string
import pandas as pd

from .cheatsheets.imports_cs import ImportsCheatSheet
from .cheatsheets.froms_cs import FromsCheatSheet
from .cheatsheets.hints_cs import HintsCheatSheet
from .cheatsheets.torch_cs import TorchUtils

# ==============================================
# CVTools Class
# ==============================================


class CVTools:

    def __init__(self):
        self.torch = TorchUtils()
        self.imports = ImportsCheatSheet()
        self.froms = FromsCheatSheet()
        self.h = HintsCheatSheet()
        self._last_data_dir = None
        self._level_df = self._create_level_dataframe()

    # ------------------------------------------
    # _create_level_dataframe (private)
    # ------------------------------------------
    def _create_level_dataframe(self):
        """ساخت دیتافریم سطح‌بندی توابع OpenCV"""
        data = {
            "Config": [
                "folder",
                "outputs",
                "paths",
                "th_area",
                "kernel",
                "Path",
                "mkdir",
                "glob",
                "stem",
            ],
            "Preprocess": [
                "imread",
                "cvtColor",
                "threshold",
                "adaptiveThreshold",
                "createCLAHE",
                "GaussianBlur",
                "medianBlur",
                "bilateralFilter",
                "erode",
                "dilate",
                "morphologyEx",
                "getStructuringElement",
                "Canny",
                "Sobel",
                "Laplacian",
                "resize",
                "rotate",
                "flip",
                "warpAffine",
                "getRotationMatrix2D",
                "getAffineTransform",
                "getPerspectiveTransform",
                "warpPerspective",
                "MORPH_OPEN",
                "MORPH_CLOSE",
                "MORPH_TOPHAT",
                "COLOR_BGR2GRAY",
                "COLOR_BGR2RGB",
                "COLOR_GRAY2BGR",
                "INTER_AREA",
                "INTER_LINEAR",
                "INTER_CUBIC",
                "INTER_NEAREST",
                "bitwise_not",
                "np.std",
            ],
            "Analyze": [
                "findContours",
                "contourArea",
                "arcLength",
                "moments",
                "boundingRect",
                "minAreaRect",
                "minEnclosingCircle",
                "fitEllipse",
                "approxPolyDP",
                "convexHull",
                "isContourConvex",
                "matchTemplate",
                "HoughLines",
                "HoughLinesP",
                "HoughCircles",
                "goodFeaturesToTrack",
                "cornerHarris",
                "calcHist",
                "equalizeHist",
                "watershed",
                "minMaxLoc",
                "THRESH_BINARY",
                "THRESH_BINARY_INV",
                "THRESH_TRUNC",
                "THRESH_TOZERO",
                "THRESH_OTSU",
                "ADAPTIVE_THRESH_MEAN_C",
                "ADAPTIVE_THRESH_GAUSSIAN_C",
                "RETR_EXTERNAL",
                "RETR_LIST",
                "RETR_TREE",
                "RETR_CCOMP",
                "CHAIN_APPROX_SIMPLE",
                "CHAIN_APPROX_NONE",
            ],
            "Visualize": [
                "drawContours",
                "rectangle",
                "circle",
                "line",
                "ellipse",
                "polylines",
                "putText",
                "hist",
                "drawKeypoints",
                "imshow",
                "waitKey",
                "destroyAllWindows",
                "namedWindow",
                "resizeWindow",
                "imwrite",
                "plt.figure",
                "plt.imshow",
                "plt.title",
                "plt.axis",
                "plt.show",
                "plt.subplots",
                "plt.tight_layout",
                "plt.legend",
                "plt.plot",
                "plt.colorbar",
                "fig.savefig",
                "np.hstack",
                "np.vstack",
                "bitwise_and",
                "np.zeros",
                "np.zeros_like",
            ],
            "Main": [
                "preprocess",
                "find_objects",
                "draw_result",
                "for",
                "if",
                "product",
                "permutations",
                "combinations",
                "chain",
            ],
        }

        return pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

    # ------------------------------------------
    # find_level
    # ------------------------------------------
    def find_level(self, func_name):
        """
        📌 [Tool] پیدا کردن سطح پردازشی یک تابع OpenCV.

        📌 سطوح موجود: Config, Preprocess, Analyze, Visualize, Main

        📌 Parameters:
        - func_name: نام تابع (str) یا لیست نام‌ها (list)

        📌 Returns:
        - لیست نتایج، یا 'Not Found' اگه پیدا نشد

        📌 Example:
        cvt.find_level('drawContours')
        # → ['Visualize: [drawContours]']

        cvt.find_level('CLAHE')
        # → ['Preprocess: [createCLAHE]']

        cvt.find_level(['CLAHE', 'threshold', 'SIFT'])
        # → نتایج برای هر سه

        📌 کاربرد: تشخیص اینکه یه تابع OpenCV توی کدوم مرحله پایپ‌لاین قرار می‌گیره.
        """
        results = []
        for col in self._level_df.columns:
            matches = self._level_df[col][
                self._level_df[col].str.contains(func_name, case=False, na=False)
            ]
            if not matches.empty:
                results.append(f"{col}: {list(matches)}")

        if results:
            return results
        return "Not Found"

    # ------------------------------------------
    # imshow
    # ------------------------------------------
    def imshow(self, winname, img):
        """
        📌 [Tool] نمایش تصویر با قابلیت زوم با کیبورد.

        📌 کلیدها:
        - + یا = : بزرگ‌نمایی
        - - یا _ : کوچک‌نمایی
        - q یا ESC : بستن پنجره
        - n : بستن پنجره و رفتن به تصویر بعدی

        📌 Parameters:
        - winname: نام پنجره نمایش
        - img: تصویر ورودی (BGR یا خاکستری)

        📌 Example:
        cvt.imshow("win", img)

        📌 نکته: این تابع تا زمانی که کلید q یا n زده نشه، اجرا متوقف می‌مونه.
        """
        if img is None:
            print("Error: Invalid image")
            return

        h, w = img.shape[:2]
        scale = 1.0
        step = 0.1
        min_scale = 0.1

        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)
        cv2.imshow(winname, img)
        cv2.resizeWindow(winname, w, h)

        while True:
            key = cv2.waitKey(0) & 0xFF
            if key == ord("+") or key == ord("="):
                scale += step
                cv2.resizeWindow(winname, int(w * scale), int(h * scale))
            elif key == ord("-") or key == ord("_"):
                scale = max(min_scale, scale - step)
                cv2.resizeWindow(winname, int(w * scale), int(h * scale))
            elif key == ord("q") or key == 27:
                cv2.destroyAllWindows()
                break
            elif key == ord("n"):
                cv2.destroyAllWindows()
                break
            elif cv2.getWindowProperty(winname, cv2.WND_PROP_VISIBLE) < 1:
                break

    # ------------------------------------------
    # rotate
    # ------------------------------------------
    def rotate(self, img, angle):
        """
        📌 [Tool] چرخش تصویر با زاویه دلخواه بدون بریدگی گوشه‌ها.

        📌 Parameters:
        - img: تصویر ورودی
        - angle: زاویه چرخش (درجه)
            - مثبت → پادساعتگرد
            - منفی → ساعتگرد

        📌 Returns:
        - تصویر چرخیده‌شده با ابعاد جدید

        📌 Example:
        rotated = cvt.rotate(img, 45)
        rotated = cvt.rotate(img, -30)

        📌 نکته: ابعاد تصویر خروجی بزرگ‌تر از ورودی می‌شه تا گوشه‌ها
        بریده نشن. برای چرخش‌های ۹۰/۱۸۰ درجه از cv2.rotate استفاده کن
        که سریع‌تره.
        """
        if img is None:
            print("Error: Invalid image")
            return None

        h, w = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1)
        theta = np.radians(angle)
        new_w = int(h * np.sin(theta) + w * np.cos(theta))
        new_h = int(h * np.cos(theta) + w * np.sin(theta))
        M[0, 2] += (new_w - w) // 2
        M[1, 2] += (new_h - h) // 2
        return cv2.warpAffine(img, M, (new_w, new_h))

    # ------------------------------------------
    # resize
    # ------------------------------------------
    @staticmethod
    def resize(img, new_h=None, new_w=None, interpolation=None):
        """
        📌 [Tool] تغییر اندازه تصویر با دادن فقط یک بُعد.

        📌 Parameters:
        - img: تصویر ورودی
        - new_h: ارتفاع جدید (اختیاری)
        - new_w: عرض جدید (اختیاری)
        - interpolation: روش درون‌یابی (اختیاری)
            - None (پیش‌فرض): کوچک‌سازی → INTER_AREA، بزرگ‌نمایی → INTER_CUBIC
            - cv2.INTER_NEAREST: سریع، برای ماسک و باینری
            - cv2.INTER_LINEAR: پیش‌فرض OpenCV
            - cv2.INTER_CUBIC: برای بزرگ‌نمایی بهتر
            - cv2.INTER_AREA: برای کوچک‌سازی بهتر

        📌 Returns:
        - تصویر تغییر اندازه یافته

        📌 Example:
        resized = cvt.resize(img, new_w=800)              # عرض 800، ارتفاع خودکار
        resized = cvt.resize(img, new_h=600)              # ارتفاع 600، عرض خودکار
        resized = cvt.resize(img, new_w=800, interpolation=cv2.INTER_LINEAR)

        📌 نکته: نسبت ابعاد تصویر حفظ می‌شه.
        """
        h, w = img.shape[:2]

        if new_h is None and new_w is None:
            return img

        if new_h is None:
            ratio = new_w / w
            new_h = int(h * ratio)
        elif new_w is None:
            ratio = new_h / h
            new_w = int(w * ratio)

        if interpolation is None:
            if new_h * new_w < h * w:
                interpolation = cv2.INTER_AREA
            else:
                interpolation = cv2.INTER_CUBIC

        return cv2.resize(img, (new_w, new_h), interpolation=interpolation)

    # ------------------------------------------
    # rename_data
    # ------------------------------------------
    def rename_data(
        self, folder_path, prefix="", start=1, mode="numeric", extensions=None
    ):
        """
        📌 [Tool] تغییر نام تمام تصاویر یک پوشه با شماره یا حرف ترتیبی.

        📌 Parameters:
        - folder_path: مسیر پوشه حاوی تصاویر
        - prefix: پیشوند قبل از شماره/حرف — پیش‌فرض: "" (خالی)
        - start: شماره شروع در حالت numeric — پیش‌فرض: 1
        - mode: 'numeric' برای شماره (1, 2, 3...) یا 'alpha' برای حرف (a, b, c...)
        - extensions: لیست پسوندهای مجاز — پیش‌فرض: jpg, jpeg, png, bmp, tiff

        📌 Returns:
        - تعداد فایل‌های تغییرنام‌یافته

        📌 Example:
        cvt.rename_data("images/")                    # 1.jpg, 2.jpg, 3.jpg
        cvt.rename_data("images/", "img_")            # img_1.jpg, img_2.jpg
        cvt.rename_data("images/", start=0)           # 0.jpg, 1.jpg, 2.jpg
        cvt.rename_data("images/", mode='alpha')      # a.jpg, b.jpg, c.jpg
        cvt.rename_data("images/", "img_", mode='alpha')  # img_a.jpg, img_b.jpg

        📌 نکته: اگه اسم جدید از قبل وجود داشته باشه، شماره اضافه می‌شه
        (مثلاً 1_1.jpg). فایل‌ها اول بر اساس نام مرتب می‌شن، بعد تغییرنام.
        """
        if extensions is None:
            extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"]

        extensions = [
            ext.lower() if ext.startswith(".") else f".{ext.lower()}"
            for ext in extensions
        ]

        image_files = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                ext = os.path.splitext(file)[1].lower()
                if ext in extensions:
                    image_files.append(file_path)

        image_files.sort()

        if mode == "numeric":
            names = [f"{prefix}{i}" for i in range(start, start + len(image_files))]
        elif mode == "alpha":
            names = []
            for i in range(len(image_files)):
                n = i
                alpha_name = ""
                while n >= 0:
                    alpha_name = string.ascii_lowercase[n % 26] + alpha_name
                    n = n // 26 - 1
                names.append(f"{prefix}{alpha_name}")
        else:
            print(f"Error: mode '{mode}' not supported. Use 'numeric' or 'alpha'")
            return 0

        renamed_count = 0
        for i, old_path in enumerate(image_files):
            ext = os.path.splitext(old_path)[1]
            new_name = f"{names[i]}{ext}"
            new_path = os.path.join(folder_path, new_name)

            if os.path.exists(new_path) and old_path != new_path:
                counter = 1
                while os.path.exists(new_path):
                    if mode == "numeric":
                        new_name = f"{names[i]}_{counter}{ext}"
                    else:
                        new_name = f"{names[i]}_{counter}{ext}"
                    new_path = os.path.join(folder_path, new_name)
                    counter += 1

            try:
                os.rename(old_path, new_path)
                renamed_count += 1
            except Exception as e:
                pass

        return renamed_count

    # ------------------------------------------
    # scan_data
    # ------------------------------------------
    def scan_data(self, folder_path, contrast=50):
        """
        📌 [Tool] اسکن پوشه و جدا کردن تصاویر خراب به زیرپوشه‌ها.

        📌 Parameters:
        - folder_path: مسیر پوشه حاوی تصاویر
        - contrast: آستانه کنتراست — پیش‌فرض: 50 (پایین‌تر = حساس‌تر)

        📌 Returns:
        - None (فایل‌ها رو جابه‌جا می‌کنه)

        📌 زیرپوشه‌های خروجی:
        - bad_data/ → تصاویر None، خیلی کوچک، نسبت ابعاد بد، تکراری، نویزی
        - low_contrast/ → تصاویر با کنتراست زیر آستانه

        📌 معیارهای تشخیص:
        - img is None: فایل خراب
        - ابعاد < 50x50: خیلی کوچک
        - نسبت ابعاد > 5 یا < 0.2: نسبت غیرطبیعی
        - MD5 تکراری: تصویر تکراری
        - std لپلاسین > 200: نویز زیاد
        - var لپلاسین < contrast: کنتراست کم

        📌 Example:
        cvt.scan_data("dataset/")
        cvt.scan_data("dataset/", contrast=30)

        📌 کاربرد: قبل از آموزش مدل، برای پاک‌سازی دیتاست.
        """

        folder_path = Path(folder_path)

        bad_dir = folder_path / "bad_data"
        low_contrast_dir = folder_path / "low_contrast"
        bad_dir.mkdir(exist_ok=True)
        low_contrast_dir.mkdir(exist_ok=True)

        exts = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".tif"]
        all_paths = []
        for ext in exts:
            all_paths.extend(folder_path.glob(f"*{ext}"))
            all_paths.extend(folder_path.glob(f"*{ext.upper()}"))

        all_paths = list(set(all_paths))

        hash_store = {}

        for img_path in all_paths:
            try:
                img = cv2.imread(str(img_path))

                if img is None:
                    shutil.move(str(img_path), str(bad_dir / img_path.name))
                    continue

                h, w = img.shape[:2]

                if w < 50 or h < 50:
                    shutil.move(str(img_path), str(bad_dir / img_path.name))
                    continue

                ratio = w / h
                if ratio > 5 or ratio < 0.2:
                    shutil.move(str(img_path), str(bad_dir / img_path.name))
                    continue

                img_hash = hashlib.md5(img.tobytes()).hexdigest()
                if img_hash in hash_store:
                    shutil.move(str(img_path), str(bad_dir / img_path.name))
                    continue
                hash_store[img_hash] = img_path

                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                laplacian = cv2.Laplacian(gray, cv2.CV_64F)

                if laplacian.std() > 200:
                    shutil.move(str(img_path), str(bad_dir / img_path.name))
                    continue

                if laplacian.var() < contrast:
                    shutil.move(str(img_path), str(low_contrast_dir / img_path.name))
                    continue

            except Exception:
                try:
                    shutil.move(str(img_path), str(bad_dir / img_path.name))
                except Exception:
                    pass

    # ------------------------------------------
    # slider
    # ------------------------------------------
    def slider(self, winname, img, thresh=None, edge=None, blur=None, contour=False):
        """
        📌 [Tool] نمایش تعاملی تصویر با اسلایدر برای threshold، edge و blur.

        📌 Parameters:
        - winname: نام پنجره
        - img: تصویر ورودی (BGR یا خاکستری)
        - thresh: نوع آستانه‌گذاری
            - 'simple': آستانه ساده با اسلایدر T
            - 'otsu': آستانه خودکار Otsu
            - 'adapt': آستانه تطبیقی با اسلایدر Block و C
            - None: بدون آستانه
        - edge: تشخیص لبه
            - 'canny': Canny با اسلایدر Low و High
            - None: بدون لبه
        - blur: نوع بلور
            - 'gaussian': بلور گاوسی با اسلایدر Kernel و Sigma
            - 'median': بلور میانه با اسلایدر Kernel
            - None: بدون بلور
        - contour: True برای ذخیره تصویر کانتور همراه آستانه — پیش‌فرض: False

        📌 کلیدها:
        - +/- : زوم
        - s : ذخیره تصویر پردازش‌شده (فقط s، نه Ctrl+S)
        - q یا ESC : خروج
        - n : تصویر بعدی

        📌 Example:
        cvt.slider("win", img, edge='canny')
        cvt.slider("win", img, thresh='simple', contour=True)
        cvt.slider("win", img, blur='gaussian', edge='canny')

        📌 نکته: تصاویر ذخیره‌شده توی پوشه 'slider/' کنار فایل caller
        ذخیره می‌شن. اگه contour=True باشه، تصاویر کانتور توی
        'slider/contour/' ذخیره می‌شن.
        """

        if img is None:
            print("Error: Invalid image")
            return

        h, w = img.shape[:2]
        scale = 1.0
        step = 0.1
        min_scale = 0.1

        original_name = winname
        if "." in original_name:
            original_name = original_name.rsplit(".", 1)[0]

        if len(img.shape) == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        cv2.namedWindow(winname, cv2.WINDOW_NORMAL)

        if thresh == "simple":
            cv2.createTrackbar("T", winname, 127, 255, lambda x: None)
        elif thresh == "adapt":
            cv2.createTrackbar("Block", winname, 11, 51, lambda x: None)
            cv2.createTrackbar("C", winname, 12, 30, lambda x: None)

        if edge == "canny":
            cv2.createTrackbar("Low", winname, 50, 255, lambda x: None)
            cv2.createTrackbar("High", winname, 150, 255, lambda x: None)

        if blur == "gaussian":
            cv2.createTrackbar("Kernel", winname, 3, 21, lambda x: None)
            cv2.createTrackbar("Sigma", winname, 0, 20, lambda x: None)
        elif blur == "median":
            cv2.createTrackbar("Kernel", winname, 3, 21, lambda x: None)

        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        script_dir = os.path.dirname(os.path.abspath(caller_file))
        save_dir = os.path.join(script_dir, "slider")

        if contour:
            contour_dir = os.path.join(save_dir, "contour")
            os.makedirs(contour_dir, exist_ok=True)
            print(f"Contour save directory: {contour_dir}")

        os.makedirs(save_dir, exist_ok=True)
        print(f"Save directory: {save_dir}")
        print(
            "Press 's' to save (not Ctrl+S, as that is a Windows/OpenCV dialog unrelated to this code)."
        )

        processed = gray
        result_save = processed
        if len(processed.shape) == 2:
            result_display = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
        else:
            result_display = processed
        cv2.imshow(winname, result_display)
        cv2.resizeWindow(winname, w, h)

        while True:
            blur_k = None
            blur_s = None

            if blur == "gaussian":
                k = cv2.getTrackbarPos("Kernel", winname)
                k = k if k % 2 == 1 else k + 1
                s = cv2.getTrackbarPos("Sigma", winname)
                blur_k = k
                blur_s = s
                processed = cv2.GaussianBlur(gray, (k, k), s)
            elif blur == "median":
                k = cv2.getTrackbarPos("Kernel", winname)
                k = k if k % 2 == 1 else k + 1
                blur_k = k
                processed = cv2.medianBlur(gray, k)
            else:
                processed = gray

            thresh_t = None
            thresh_block = None
            thresh_c = None
            edge_low = None
            edge_high = None
            threshold_result = None
            thresh_type_name = None

            if thresh == "simple":
                t = cv2.getTrackbarPos("T", winname)
                thresh_t = t
                _, result_save = cv2.threshold(processed, t, 255, cv2.THRESH_BINARY)
                threshold_result = result_save
                thresh_type_name = f"simple_T{t}"
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)
            elif thresh == "otsu":
                _, result_save = cv2.threshold(
                    processed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
                )
                threshold_result = result_save
                thresh_type_name = "otsu"
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)
            elif thresh == "adapt":
                block = cv2.getTrackbarPos("Block", winname)
                block = block if block % 2 == 1 else block + 1
                if block < 3:
                    block = 3

                c_slider = cv2.getTrackbarPos("C", winname)
                c = c_slider - 10

                thresh_block = block
                thresh_c = c

                result_save = cv2.adaptiveThreshold(
                    processed,
                    255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,
                    block,
                    c,
                )
                threshold_result = result_save
                thresh_type_name = f"adapt_blocksize{block}_c{c}"
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)

            elif edge == "canny":
                low = cv2.getTrackbarPos("Low", winname)
                high = cv2.getTrackbarPos("High", winname)
                edge_low = low
                edge_high = high
                result_save = cv2.Canny(processed, low, high)
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)
            else:
                result_save = processed
                if len(processed.shape) == 2:
                    result_display = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)
                else:
                    result_display = processed

            cv2.imshow(winname, result_display)

            key = cv2.waitKey(30) & 0xFF
            if key == ord("+") or key == ord("="):
                scale += step
                cv2.resizeWindow(winname, int(w * scale), int(h * scale))
            elif key == ord("-") or key == ord("_"):
                scale = max(min_scale, scale - step)
                cv2.resizeWindow(winname, int(w * scale), int(h * scale))
            elif key == ord("s"):
                parts = [original_name]

                if blur == "gaussian":
                    parts.append(f"Gaussian_k{blur_k}_s{blur_s}")
                elif blur == "median":
                    parts.append(f"Median_k{blur_k}")

                if thresh == "simple":
                    parts.append(f"simple_T{thresh_t}")
                elif thresh == "otsu":
                    parts.append("otsu")
                elif thresh == "adapt":
                    parts.append(f"adapt_blocksize{thresh_block}_c{thresh_c}")

                if edge == "canny":
                    parts.append(f"canny_L{edge_low}_H{edge_high}")

                if len(parts) == 1:
                    parts.append("original")

                filename = f"{'_'.join(parts)}.jpg"
                filepath = os.path.join(save_dir, filename)

                counter = 1
                while os.path.exists(filepath):
                    filename = f"{'_'.join(parts)}_{counter}.jpg"
                    filepath = os.path.join(save_dir, filename)
                    counter += 1

                cv2.imwrite(filepath, result_save, [cv2.IMWRITE_JPEG_QUALITY, 95])
                print(f"Saved: {filename}")

                if (
                    contour
                    and threshold_result is not None
                    and thresh_type_name is not None
                ):
                    contours, _ = cv2.findContours(
                        threshold_result, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
                    )

                    contour_img = img.copy()

                    if len(contours) > 0:
                        cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

                        contour_parts = [original_name]

                        if blur == "gaussian":
                            contour_parts.append(f"Gaussian_k{blur_k}_s{blur_s}")
                        elif blur == "median":
                            contour_parts.append(f"Median_k{blur_k}")

                        contour_parts.append(thresh_type_name)

                        contour_filename = f"{'_'.join(contour_parts)}_contour.jpg"
                        contour_filepath = os.path.join(contour_dir, contour_filename)

                        counter = 1
                        while os.path.exists(contour_filepath):
                            contour_filename = (
                                f"{'_'.join(contour_parts)}_contour_{counter}.jpg"
                            )
                            contour_filepath = os.path.join(
                                contour_dir, contour_filename
                            )
                            counter += 1

                        cv2.imwrite(
                            contour_filepath,
                            contour_img,
                            [cv2.IMWRITE_JPEG_QUALITY, 95],
                        )
                        print(
                            f"Contour saved: {contour_filename} (Found {len(contours)} contours)"
                        )
                    else:
                        print("No contours found to save")

            elif key == ord("q") or key == 27:
                cv2.destroyAllWindows()
                break
            elif key == ord("n"):
                cv2.destroyAllWindows()
                break
            elif cv2.getWindowProperty(winname, cv2.WND_PROP_VISIBLE) < 1:
                break

    # ------------------------------------------
    # search_path
    # ------------------------------------------
    def search_path(self, names):
        """
        📌 [Tool] جستجوی فایل یا پوشه در کل پروژه و درج مسیرش به شکل کامنت.

        📌 Parameters:
        - names: نام فایل/پوشه (str) یا لیستی از نام‌ها (list)

        📌 Returns:
        - None (نتیجه رو به فایل caller اضافه می‌کنه + چاپ در کنسول)

        📌 Example:
        cvt.search_path("pandas_cheatsheet.py")
        cvt.search_path("my_image")
        cvt.search_path(["utils.py", "data/", "models"])

        📌 نکته: پوشه‌های مخفی، __pycache__، venv، env و node_modules
        نادیده گرفته می‌شن. نتیجه به شکل کامنت با # به آخر فایلی که
        تابع رو صدا زده اضافه می‌شه.
        """
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        project_root = _self_dir.parent.resolve()

        if isinstance(names, str):
            names = [names]

        found_paths = {}
        not_found = []

        for name in names:
            name_found = False
            name_lower = name.lower()

            for root, dirs, files in os.walk(project_root):
                dirs[:] = [
                    d
                    for d in dirs
                    if not d.startswith(".")
                    and d not in ["__pycache__", "venv", "env", "node_modules"]
                ]

                for dir_name in dirs:
                    if name_lower in dir_name.lower():
                        full_path = os.path.join(root, dir_name)
                        if name not in found_paths:
                            found_paths[name] = []
                        found_paths[name].append(full_path)
                        name_found = True

                for file_name in files:
                    if name_lower in file_name.lower():
                        full_path = os.path.join(root, file_name)
                        if name not in found_paths:
                            found_paths[name] = []
                        found_paths[name].append(full_path)
                        name_found = True

            if not name_found:
                not_found.append(name)

        hashtag_lines = [
            "# ----------------------------------------",
            "# Path search results",
            "# ----------------------------------------",
        ]
        for name, paths in found_paths.items():
            hashtag_lines.append(f"# Search: '{name}' -> Found {len(paths)} match(es)")
            hashtag_lines.append("")
            for path in paths:
                hashtag_lines.append(f"# path: {path}")
        if not_found:
            if found_paths:
                hashtag_lines.append("")
            for name in not_found:
                hashtag_lines.append(f"# Search: '{name}' -> Not found")
        hashtag_lines.append("# ----------------------------------------")
        hashtag_lines.append(
            f"# Summary: Found {len(found_paths)} | Not found {len(not_found)}"
        )
        hashtag_lines.append("# ----------------------------------------")

        try:
            with open(caller_file, "a", encoding="utf-8") as f:
                f.write("\n".join(hashtag_lines) + "\n")
            if found_paths:
                for name, paths in found_paths.items():
                    print(f"'{name}' -> Found {len(paths)} match(es):")
                    for path in paths:
                        print(f"  + {path}")
            if not_found:
                for name in not_found:
                    print(f"'{name}' -> Not found")
            print(f"\nResults appended to: {caller_file}")
        except Exception as e:
            print(f"Error writing to file '{caller_file}': {e}")


cvt = CVTools()
