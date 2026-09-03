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
• cvt.venv.*     → Interactive Virtual Environment Cheat Sheet (hover for commands)
• cvt.find_level() → Find the processing level (Config, Preprocess, Analyze, Visualize, Main) of OpenCV functions

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
# ------------------
# Virtual Environment Cheat Sheet:
cvt.venv.create       # hover: python -m venv venv
cvt.venv.activate     # hover: venv\Scripts\activate
cvt.venv.freeze       # hover: pip freeze > requirements.txt
cvt.venv.check        # hover: pip -V
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
import re
import shutil
import hashlib
import string
import pandas as pd


# ==============================================
# VenvCheatSheet Class
# ==============================================


class VenvCheatSheet:

    @property
    def create(self):
        """python -m venv venv  |  Create new virtual environment"""
        return "python -m venv venv"

    @property
    def cd_project(self):
        """cd "E:\\python\\INTPCode\\5_Month_Computer_Vision_Roadmap"  |  Go to project root"""
        return 'cd "E:\\python\\INTPCode\\5_Month_Computer_Vision_Roadmap"'

    @property
    def activate(self):
        """venv\\Scripts\\activate  |  Mac/Linux: source venv/bin/activate"""
        return "venv\\Scripts\\activate"

    @property
    def deactivate(self):
        """deactivate  |  Deactivate virtual environment"""
        return "deactivate"

    @property
    def install(self):
        """pip install -r requirements.txt  |  Install all packages"""
        return "pip install -r requirements.txt"

    @property
    def install_single(self):
        """pip install package_name  |  Install a specific package"""
        return "pip install package_name"

    @property
    def install_cv(self):
        """pip install opencv-python numpy matplotlib pillow pandas scikit-image scikit-learn jupyter"""
        return "pip install opencv-python numpy matplotlib pillow pandas scikit-image scikit-learn jupyter"

    @property
    def freeze(self):
        """pip freeze > requirements.txt"""
        return "pip freeze > requirements.txt"

    @property
    def list_packages(self):
        """pip list"""
        return "pip list"

    @property
    def outdated(self):
        """pip list --outdated"""
        return "pip list --outdated"

    @property
    def upgrade(self):
        """pip install --upgrade package_name"""
        return "pip install --upgrade numpy"

    @property
    def uninstall(self):
        """pip uninstall package_name"""
        return "pip uninstall numpy"

    @property
    def restore(self):
        """pip install -r requirements.txt"""
        return "pip install -r requirements.txt"

    @property
    def check(self):
        """pip -V  |  Check virtual environment health"""
        return "pip -V"

    @property
    def delete_env(self):
        """rmdir /s venv"""
        return "rmdir /s venv"

    @property
    def rebuild(self):
        """python -m venv venv"""
        return "python -m venv venv"

    @property
    def requirements_sample(self):
        """opencv-python==4.12.0"""
        return "opencv-python==4.12.0"

    @property
    def pip_meaning(self):
        """pip = Package Installer for Python"""
        return "pip = Package Installer for Python"

    @property
    def venv_meaning(self):
        """venv = Virtual Environment"""
        return "venv = Virtual Environment"


# ==============================================
# CVTools Class
# ==============================================


class CVTools:

    def __init__(self):
        self.venv = VenvCheatSheet()
        self._last_data_dir = None
        self._level_df = self._create_level_dataframe()

    # ------------------------------------------
    # _create_level_dataframe (private)
    # ------------------------------------------
    def _create_level_dataframe(self):
        """ساخت دیتافریم سطح‌بندی توابع OpenCV"""
        data = {
            'Config': [
                'folder', 'outputs', 'paths', 'th_area', 'kernel',
                'Path', 'mkdir', 'glob', 'stem'
            ],
            'Preprocess': [
                'imread', 'cvtColor', 'threshold', 'adaptiveThreshold', 'createCLAHE',
                'GaussianBlur', 'medianBlur', 'bilateralFilter', 'erode', 'dilate',
                'morphologyEx', 'getStructuringElement', 'Canny', 'Sobel', 'Laplacian',
                'resize', 'rotate', 'flip', 'warpAffine', 'getRotationMatrix2D',
                'getAffineTransform', 'getPerspectiveTransform', 'warpPerspective',
                'MORPH_OPEN', 'MORPH_CLOSE', 'MORPH_TOPHAT', 'COLOR_BGR2GRAY',
                'COLOR_BGR2RGB', 'COLOR_GRAY2BGR', 'INTER_AREA', 'INTER_LINEAR',
                'INTER_CUBIC', 'INTER_NEAREST', 'bitwise_not', 'np.std'
            ],
            'Analyze': [
                'findContours', 'contourArea', 'arcLength', 'moments', 'boundingRect',
                'minAreaRect', 'minEnclosingCircle', 'fitEllipse', 'approxPolyDP',
                'convexHull', 'isContourConvex', 'matchTemplate', 'HoughLines',
                'HoughLinesP', 'HoughCircles', 'goodFeaturesToTrack', 'cornerHarris',
                'calcHist', 'equalizeHist', 'watershed', 'minMaxLoc',
                'THRESH_BINARY', 'THRESH_BINARY_INV', 'THRESH_TRUNC', 'THRESH_TOZERO',
                'THRESH_OTSU', 'ADAPTIVE_THRESH_MEAN_C', 'ADAPTIVE_THRESH_GAUSSIAN_C',
                'RETR_EXTERNAL', 'RETR_LIST', 'RETR_TREE', 'RETR_CCOMP',
                'CHAIN_APPROX_SIMPLE', 'CHAIN_APPROX_NONE'
            ],
            'Visualize': [
                'drawContours', 'rectangle', 'circle', 'line', 'ellipse',
                'polylines', 'putText', 'hist', 'drawKeypoints', 'imshow',
                'waitKey', 'destroyAllWindows', 'namedWindow', 'resizeWindow',
                'imwrite', 'plt.figure', 'plt.imshow', 'plt.title', 'plt.axis',
                'plt.show', 'plt.subplots', 'plt.tight_layout', 'plt.legend',
                'plt.plot', 'plt.colorbar', 'fig.savefig', 'np.hstack', 'np.vstack',
                'bitwise_and', 'np.zeros', 'np.zeros_like'
            ],
            'Main': [
                'preprocess', 'find_objects', 'draw_result', 'for', 'if',
                'product', 'permutations', 'combinations', 'chain'
            ]
        }

        # تبدیل به دیتافریم
        return pd.DataFrame(dict([(k, pd.Series(v)) for k, v in data.items()]))

    # ------------------------------------------
    # find_level
    # ------------------------------------------
    def find_level(self, func_name):
        """
        پیدا کردن سطح پردازشی یک تابع OpenCV

        Parameters:
        - func_name: str - نام تابع مورد جستجو

        Returns:
        - لیست نتایج یا 'Not Found'

        Example:
        cvt.find_level('drawContours')
        cvt.find_level('CLAHE')
        cvt.find_level('threshold')
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
        return 'Not Found'

    # ------------------------------------------
    # imshow
    # ------------------------------------------
    def imshow(self, winname, img):
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
    def rename_data(self, folder_path, prefix="", start=1, mode='numeric', extensions=None):
        """
        Rename all images in a folder with sequential numbers or alphabetical names

        Parameters:
        - folder_path: Path to the folder containing images
        - prefix: Prefix before the number/letter (default: empty)
        - start: Starting number for numeric mode (default: 1)
        - mode: 'numeric' for numbers (1, 2, 3...) or 'alpha' for letters (a, b, c...)
        - extensions: List of allowed extensions (default: jpg, jpeg, png, bmp, tiff)

        Example:
        cvt.rename_data("images/")                    # 1.jpg, 2.jpg, 3.jpg
        cvt.rename_data("images/", "img_")            # img_1.jpg, img_2.jpg
        cvt.rename_data("images/", start=0)           # 0.jpg, 1.jpg, 2.jpg
        cvt.rename_data("images/", mode='alpha')      # a.jpg, b.jpg, c.jpg
        cvt.rename_data("images/", "img_", mode='alpha')  # img_a.jpg, img_b.jpg
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

        if mode == 'numeric':
            # نام‌گذاری عددی
            names = [f"{prefix}{i}" for i in range(start, start + len(image_files))]
        elif mode == 'alpha':
            # نام‌گذاری الفبایی (a, b, c, ..., z, aa, ab, ...)
            names = []
            for i in range(len(image_files)):
                # تبدیل عدد به حروف الفبا (مثل Excel columns)
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

            # اگر فایل مقصد وجود دارد و با فایل مبدا یکی نیست
            if os.path.exists(new_path) and old_path != new_path:
                # پیدا کردن نام جایگزین
                counter = 1
                while os.path.exists(new_path):
                    if mode == 'numeric':
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
        Scan and separate bad images into subfolders

        Parameters:
        - folder_path: Path to the data folder
        - contrast: Contrast threshold (default: 50)

        Output subfolders:
        - bad_data/ → None, too small, bad ratio, duplicate, noisy images
        - low_contrast/ → Images with contrast below threshold

        Example:
        cvt.scan_data("dataset/")
        cvt.scan_data("dataset/", contrast=30)
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
        Display image with interactive sliders for various processing tasks

        Parameters:
        - thresh: 'simple', 'otsu', 'adapt', None
        - edge: 'canny', None
        - blur: 'gaussian', 'median', None
        - contour: True/False (default: False) - Save contour image alongside threshold

        Keys:
        - +/- : Zoom
        - s : Save processed image as jpg (press 's' only, not Ctrl+S)
        - q/ESC : Quit
        - n : Next image

        Example:
        cvt.slider("win", img, edge='canny')
        cvt.slider("win", img, thresh='simple', contour=True)
        """

        if img is None:
            print("Error: Invalid image")
            return

        h, w = img.shape[:2]
        scale = 1.0
        step = 0.1
        min_scale = 0.1

        # Extract filename from window title
        original_name = winname
        # Remove extension if present
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
            # Slider from 0 to 30 corresponds to actual C from -10 to 20
            cv2.createTrackbar("C", winname, 12, 30, lambda x: None)

        if edge == "canny":
            cv2.createTrackbar("Low", winname, 50, 255, lambda x: None)
            cv2.createTrackbar("High", winname, 150, 255, lambda x: None)

        if blur == "gaussian":
            cv2.createTrackbar("Kernel", winname, 3, 21, lambda x: None)
            cv2.createTrackbar("Sigma", winname, 0, 20, lambda x: None)
        elif blur == "median":
            cv2.createTrackbar("Kernel", winname, 3, 21, lambda x: None)

        # Save directory: "slider" subfolder next to the calling script — always auto-created
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        script_dir = os.path.dirname(os.path.abspath(caller_file))
        save_dir = os.path.join(script_dir, "slider")

        # If contour is True, create a "contour" subfolder inside "slider"
        if contour:
            contour_dir = os.path.join(save_dir, "contour")
            os.makedirs(contour_dir, exist_ok=True)
            print(f"Contour save directory: {contour_dir}")

        os.makedirs(save_dir, exist_ok=True)
        print(f"Save directory: {save_dir}")
        print(
            "Press 's' to save (not Ctrl+S, as that is a Windows/OpenCV dialog unrelated to this code)."
        )

        # Initialize with first frame
        # Create initial result to display
        processed = gray
        result_save = processed  # تصویر اصلی برای ذخیره
        # نمایش اولیه - اگر تک کاناله است به BGR تبدیل کن
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
            threshold_result = None  # Store threshold result for contour extraction
            thresh_type_name = None  # Store threshold type name for contour filename

            if thresh == "simple":
                t = cv2.getTrackbarPos("T", winname)
                thresh_t = t
                _, result_save = cv2.threshold(processed, t, 255, cv2.THRESH_BINARY)
                threshold_result = result_save
                thresh_type_name = f"simple_T{t}"
                # تبدیل به BGR فقط برای نمایش
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)
            elif thresh == "otsu":
                _, result_save = cv2.threshold(
                    processed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
                )
                threshold_result = result_save
                thresh_type_name = "otsu"
                # تبدیل به BGR فقط برای نمایش
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)
            elif thresh == "adapt":
                block = cv2.getTrackbarPos("Block", winname)
                block = block if block % 2 == 1 else block + 1
                if block < 3:
                    block = 3

                # Convert slider value (0-30) to actual C (-10 to 20)
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
                # تبدیل به BGR فقط برای نمایش
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)

            elif edge == "canny":
                low = cv2.getTrackbarPos("Low", winname)
                high = cv2.getTrackbarPos("High", winname)
                edge_low = low
                edge_high = high
                result_save = cv2.Canny(processed, low, high)
                # تبدیل به BGR فقط برای نمایش
                result_display = cv2.cvtColor(result_save, cv2.COLOR_GRAY2BGR)
            else:
                # فقط blur یا بدون پردازش
                result_save = processed
                # اگر تک کاناله است به BGR تبدیل کن برای نمایش
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
                # Build filename with processing parameters
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

                # Save as jpg - ذخیره تصویر اصلی بدون تغییر
                filename = f"{'_'.join(parts)}.jpg"
                filepath = os.path.join(save_dir, filename)

                # If file exists, add number suffix
                counter = 1
                while os.path.exists(filepath):
                    filename = f"{'_'.join(parts)}_{counter}.jpg"
                    filepath = os.path.join(save_dir, filename)
                    counter += 1

                cv2.imwrite(filepath, result_save, [cv2.IMWRITE_JPEG_QUALITY, 95])
                print(f"Saved: {filename}")

                # If contour=True and we have a threshold result, save contour
                if contour and threshold_result is not None and thresh_type_name is not None:
                    # Find contours on the binary threshold result
                    contours, _ = cv2.findContours(
                        threshold_result,
                        cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE
                    )

                    # Create a copy of the original image to draw contours (raw image untouched)
                    contour_img = img.copy()

                    # Draw all contours on the original image
                    if len(contours) > 0:
                        cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)

                        # Build contour filename: imageName_thresholdInfo_contour.jpg
                        contour_parts = [original_name]

                        if blur == "gaussian":
                            contour_parts.append(f"Gaussian_k{blur_k}_s{blur_s}")
                        elif blur == "median":
                            contour_parts.append(f"Median_k{blur_k}")

                        # Add threshold type info
                        contour_parts.append(thresh_type_name)

                        # Add contour suffix at the end
                        contour_filename = f"{'_'.join(contour_parts)}_contour.jpg"
                        contour_filepath = os.path.join(contour_dir, contour_filename)

                        # If file exists, add number suffix
                        counter = 1
                        while os.path.exists(contour_filepath):
                            contour_filename = f"{'_'.join(contour_parts)}_contour_{counter}.jpg"
                            contour_filepath = os.path.join(contour_dir, contour_filename)
                            counter += 1

                        cv2.imwrite(contour_filepath, contour_img, [cv2.IMWRITE_JPEG_QUALITY, 95])
                        print(f"Contour saved: {contour_filename} (Found {len(contours)} contours)")
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