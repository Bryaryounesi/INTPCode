class ImportsCheatSheet:
    """
    🏷️ [Imports]

    📌 چیت‌شیت تعاملی `import xxx` برای کتابخانه‌های کامپیوتر ویژن.

    📌 با نوشتن cvt.imports.<name> کد ایمپورت را هاور کنید.

    📌 مثال:
        cvt.imports.numpy   → import numpy as np
        cvt.imports.cv2     → import cv2
        cvt.imports.torch   → import torch
    """

    # ------------------------------------------
    # پایه‌ای و محاسباتی
    # ------------------------------------------
    @property
    def numpy(self):
        """
        🏷️ [Base] [Numerical]

        📌 import numpy as np

        📌 کاربرد: محاسبات عددی، آرایه‌ها، عملیات ماتریسی
        📌 نصب: pip install numpy
        """
        return "import numpy as np"

    @property
    def math(self):
        """
        🏷️ [Base] [Built-in]

        📌 import math

        📌 کاربرد: توابع ریاضی پایه (sin, cos, sqrt, ...)
        📌 نصب: built-in
        """
        return "import math"

    @property
    def random(self):
        """
        🏷️ [Base] [Built-in]

        📌 import random

        📌 کاربرد: اعداد و انتخاب‌های تصادفی
        📌 نصب: built-in
        """
        return "import random"

    @property
    def scipy(self):
        """
        🏷️ [Base] [Scientific]

        📌 import scipy

        📌 کاربرد: محاسبات علمی، فیلترها، بهینه‌سازی
        📌 نصب: pip install scipy
        """
        return "import scipy"

    # ------------------------------------------
    # پردازش تصویر
    # ------------------------------------------
    @property
    def cv2(self):
        """
        🏷️ [Image] [OpenCV]

        📌 import cv2

        📌 کاربرد: پردازش تصویر و ویدیو (قلب کامپیوتر ویژن)
        📌 نصب: pip install opencv-python
        """
        return "import cv2"

    @property
    def PIL(self):
        """
        🏷️ [Image] [Pillow]

        📌 import PIL
        📌 یا: from PIL import Image

        📌 کاربرد: باز کردن، تبدیل و ذخیره تصاویر
        📌 نصب: pip install Pillow
        """
        return "import PIL"

    @property
    def skimage(self):
        """
        🏷️ [Image] [scikit-image]

        📌 import skimage

        📌 کاربرد: الگوریتم‌های پیشرفته پردازش تصویر
        📌 نصب: pip install scikit-image
        """
        return "import skimage"

    @property
    def imageio(self):
        """
        🏷️ [Image] [IO]

        📌 import imageio

        📌 کاربرد: خواندن/نوشتن فرمت‌های مختلف تصویر و ویدیو
        📌 نصب: pip install imageio
        """
        return "import imageio"

    # ------------------------------------------
    # یادگیری عمیق
    # ------------------------------------------
    @property
    def torch(self):
        """
        🏷️ [DL] [PyTorch]

        📌 import torch

        📌 کاربرد: تنسورها، autograd، شبکه‌های عصبی
        📌 نصب: pip install torch
        """
        return "import torch"

    @property
    def torchvision(self):
        """
        🏷️ [DL] [PyTorch]

        📌 import torchvision

        📌 کاربرد: دیتاست‌ها، مدل‌های pretrained، transforms
        📌 نصب: pip install torchvision
        """
        return "import torchvision"

    @property
    def tensorflow(self):
        """
        🏷️ [DL] [TensorFlow]

        📌 import tensorflow as tf

        📌 کاربرد: فریمورک یادگیری عمیق گوگل
        📌 نصب: pip install tensorflow
        """
        return "import tensorflow as tf"

    @property
    def keras(self):
        """
        🏷️ [DL] [Keras]

        📌 import keras

        📌 کاربرد: API سطح‌بالا برای ساخت شبکه‌های عصبی
        📌 نصب: pip install keras
        """
        return "import keras"

    @property
    def sklearn(self):
        """
        🏷️ [ML] [scikit-learn]

        📌 import sklearn

        📌 کاربرد: الگوریتم‌های کلاسیک یادگیری ماشین
        📌 نصب: pip install scikit-learn
        """
        return "import sklearn"

    @property
    def transformers(self):
        """
        🏷️ [DL] [HuggingFace]

        📌 import transformers

        📌 کاربرد: مدل‌های Transformer (ViT, CLIP, ...)
        📌 نصب: pip install transformers
        """
        return "import transformers"

    @property
    def timm(self):
        """
        🏷️ [DL] [PyTorch Image Models]

        📌 import timm

        📌 کاربرد: مجموعه بزرگی از مدل‌های تصویری pretrained
        📌 نصب: pip install timm
        """
        return "import timm"

    @property
    def ultralytics(self):
        """
        🏷️ [DL] [YOLO]

        📌 import ultralytics

        📌 کاربرد: مدل‌های YOLO برای تشخیص اشیاء
        📌 نصب: pip install ultralytics
        """
        return "import ultralytics"

    # ------------------------------------------
    # نمایش و رسم
    # ------------------------------------------
    @property
    def matplotlib(self):
        """
        🏷️ [Viz] [Matplotlib]

        📌 import matplotlib
        📌 یا: import matplotlib.pyplot as plt

        📌 کاربرد: رسم نمودار و نمایش تصویر
        📌 نصب: pip install matplotlib
        """
        return "import matplotlib"

    @property
    def seaborn(self):
        """
        🏷️ [Viz] [Seaborn]

        📌 import seaborn as sns

        📌 کاربرد: نمودارهای آماری زیبا
        📌 نصب: pip install seaborn
        """
        return "import seaborn as sns"

    @property
    def plotly(self):
        """
        🏷️ [Viz] [Plotly]

        📌 import plotly

        📌 کاربرد: نمودارهای تعاملی
        📌 نصب: pip install plotly
        """
        return "import plotly"

    # ------------------------------------------
    # داده و جداول
    # ------------------------------------------
    @property
    def pandas(self):
        """
        🏷️ [Data] [Pandas]

        📌 import pandas as pd

        📌 کاربرد: کار با DataFrame و تحلیل داده
        📌 نصب: pip install pandas
        """
        return "import pandas as pd"

    @property
    def h5py(self):
        """
        🏷️ [Data] [HDF5]

        📌 import h5py

        📌 کاربرد: خواندن/نوشتن فایل‌های HDF5 (مدل‌های Keras)
        📌 نصب: pip install h5py
        """
        return "import h5py"

    @property
    def json(self):
        """
        🏷️ [Data] [Built-in]

        📌 import json

        📌 کاربرد: خواندن/نوشتن JSON (annotationها، config)
        📌 نصب: built-in
        """
        return "import json"

    @property
    def yaml(self):
        """
        🏷️ [Data] [YAML]

        📌 import yaml

        📌 کاربرد: خواندن/نوشتن فایل‌های YAML (config)
        📌 نصب: pip install pyyaml
        """
        return "import yaml"

    @property
    def xml(self):
        """
        🏷️ [Data] [Built-in]

        📌 import xml

        📌 کاربرد: خواندن annotationهای XML (Pascal VOC)
        📌 نصب: built-in
        """
        return "import xml"

    # ------------------------------------------
    # فایل و مسیر
    # ------------------------------------------
    @property
    def os(self):
        """
        🏷️ [File] [Built-in]

        📌 import os

        📌 کاربرد: کار با فایل‌ها، مسیرها، متغیرهای محیطی
        📌 نصب: built-in
        """
        return "import os"

    @property
    def glob(self):
        """
        🏷️ [File] [Built-in]

        📌 import glob

        📌 کاربرد: جستجوی فایل با الگو (مثل *.jpg)
        📌 نصب: built-in
        """
        return "import glob"

    @property
    def shutil(self):
        """
        🏷️ [File] [Built-in]

        📌 import shutil

        📌 کاربرد: کپی، انتقال، حذف فایل و پوشه
        📌 نصب: built-in
        """
        return "import shutil"

    # ------------------------------------------
    # ابزارهای کمکی
    # ------------------------------------------
    @property
    def tqdm(self):
        """
        🏷️ [Util] [Progress]

        📌 import tqdm

        📌 کاربرد: نوار پیشرفت برای حلقه‌ها
        📌 نصب: pip install tqdm
        """
        return "import tqdm"

    @property
    def logging(self):
        """
        🏷️ [Util] [Built-in]

        📌 import logging

        📌 کاربرد: لاگ‌گیری حرفه‌ای
        📌 نصب: built-in
        """
        return "import logging"

    @property
    def warnings(self):
        """
        🏷️ [Util] [Built-in]

        📌 import warnings

        📌 کاربرد: مدیریت و فیلتر هشدارها
        📌 نصب: built-in
        """
        return "import warnings"

    @property
    def time(self):
        """
        🏷️ [Util] [Built-in]

        📌 import time

        📌 کاربرد: اندازه‌گیری زمان اجرا
        📌 نصب: built-in
        """
        return "import time"

    @property
    def datetime(self):
        """
        🏷️ [Util] [Built-in]

        📌 import datetime

        📌 کاربرد: کار با تاریخ و زمان
        📌 نصب: built-in
        """
        return "import datetime"

    @property
    def typing(self):
        """
        🏷️ [Util] [Built-in]

        📌 import typing

        📌 کاربرد: type hints (List, Dict, Optional, ...)
        📌 نصب: built-in
        """
        return "import typing"

    @property
    def dataclasses(self):
        """
        🏷️ [Util] [Built-in]

        📌 import dataclasses

        📌 کاربرد: ساخت کلاس‌های داده‌ای ساده
        📌 نصب: built-in
        """
        return "import dataclasses"

    @property
    def functools(self):
        """
        🏷️ [Util] [Built-in]

        📌 import functools

        📌 کاربرد: decoratorها و ابزارهای تابعی
        📌 نصب: built-in
        """
        return "import functools"

    @property
    def collections(self):
        """
        🏷️ [Util] [Built-in]

        📌 import collections

        📌 کاربرد: ساختارهای داده خاص (deque, Counter, ...)
        📌 نصب: built-in
        """
        return "import collections"

    @property
    def copy(self):
        """
        🏷️ [Util] [Built-in]

        📌 import copy

        📌 کاربرد: کپی سطحی و عمیق
        📌 نصب: built-in
        """
        return "import copy"

    # ------------------------------------------
    # GPU و محاسبات سریع
    # ------------------------------------------
    @property
    def cupy(self):
        """
        🏷️ [GPU] [CuPy]

        📌 import cupy

        📌 کاربرد: NumPy روی GPU (CUDA)
        📌 نصب: pip install cupy-cuda12x
        """
        return "import cupy"

    @property
    def numba(self):
        """
        🏷️ [GPU] [Numba]

        📌 import numba

        📌 کاربرد: JIT کامپایل کد پایتون برای سرعت
        📌 نصب: pip install numba
        """
        return "import numba"
