"""
cvtools module — Personal Computer Vision Toolbox

این ماژول مجموعه‌ای از توابع و ابزارهای کمکی برای پروژه‌های اپن سیوی را ارائه می‌دهد و کدهای تکراری و طولانی را کاهش می‌دهد.

هدف: تمرکز بر مفاهیم اصلی بینایی کامپیوتر بدون درگیر شدن با کدهای تکراری.

Current Features:
• cvt.imshow()   → Display image with keyboard zoom (+ - q)
• cvt.rotate()   → Rotate image without cropping corners (auto 4-step)
• cv2.imwrite()  → Auto-save image to the calling script's directory (patched)
• cvt.resize()   → Resize by providing only one dimension
• cvt.search_path() → Search for files or folders in the entire project and insert their paths as hashtagged comments
• cvt.auto_comp() → Auto-complete code from all project files
• cvt.venv.*     → Interactive Virtual Environment Cheat Sheet (hover for commands)

نحوه استفاده:
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
cvt.auto_comp("key_word")
مثال:
cvt.auto_comp(".drop")
# ------------------
# Virtual Environment Cheat Sheet:
cvt.venv.create       # هاور: python -m venv venv
cvt.venv.activate     # هاور: venv\Scripts\activate
cvt.venv.freeze       # هاور: pip freeze > requirements.txt
cvt.venv.check        # هاور: pip -V
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

# ==============================================
# Patch cv2.imwrite to save in the correct directory
# ==============================================

_original_imwrite = cv2.imwrite

"""
ذخیره کننده تصویر خروجی در همان پوشه ای که اسکریپ در آن است
مثال: cv2.imwrite("output.jpg", rotated)
"""


def _new_imwrite(filename, img, *args, **kwargs):
    if not os.path.isabs(filename):
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename
        script_dir = os.path.dirname(os.path.abspath(caller_file))
        filename = os.path.join(script_dir, filename)
    return _original_imwrite(filename, img, *args, **kwargs)


cv2.imwrite = _new_imwrite


# ==============================================
# VenvCheatSheet Class: Interactive Virtual Environment Reference
# ==============================================

class VenvCheatSheet:
    """
    چیت‌شیت تعاملی محیط مجازی.
    با نوشتن cvt.venv. تمام دستورات در Pylance ظاهر می‌شوند و با هاور، دستور کامل ترمینال نمایش داده می‌شود.

    مثال:
        cvt.venv.create       ← هاور: python -m venv venv
        cvt.venv.activate     ← هاور: venv\\Scripts\\activate
        cvt.venv.freeze       ← هاور: pip freeze > requirements.txt
    """

    @property
    def create(self):
        """python -m venv venv  |  با اسم متفاوت: python -m venv tqdm_venv  |  ساخت محیط مجازی جدید"""
        return 'python -m venv venv'

    @property
    def cd_project(self):
        """cd "E:\\python\\INTPCode\\5_Month_Computer_Vision_Roadmap"  |  رفتن به ریشه پروژه قبل از ساخت venv"""
        return 'cd "E:\\python\\INTPCode\\5_Month_Computer_Vision_Roadmap"'

    @property
    def activate(self):
        """venv\\Scripts\\activate  |  مک/لینوکس: source venv/bin/activate  |  فعال‌سازی محیط مجازی"""
        return 'venv\\Scripts\\activate'

    @property
    def deactivate(self):
        """deactivate  |  یا بستن ترمینال  |  غیرفعال‌سازی محیط مجازی"""
        return 'deactivate'

    @property
    def install(self):
        """pip install -r requirements.txt  |  نصب همه کتابخونه‌ها از فایل قفل"""
        return 'pip install -r requirements.txt'

    @property
    def install_single(self):
        """pip install نام_کتابخانه  |  مثال: pip install tqdm  |  نصب یک کتابخانه خاص"""
        return 'pip install نام_کتابخانه'

    @property
    def install_cv(self):
        """pip install opencv-python numpy matplotlib pillow pandas scikit-image scikit-learn jupyter  |  کتابخونه‌های ضروری Computer Vision"""
        return 'pip install opencv-python numpy matplotlib pillow pandas scikit-image scikit-learn jupyter'

    @property
    def freeze(self):
        """pip freeze > requirements.txt  |  ذخیره نسخه‌های دقیق همه کتابخونه‌ها در فایل requirements.txt"""
        return 'pip freeze > requirements.txt'

    @property
    def list_packages(self):
        """pip list  |  نمایش تمام کتابخونه‌های نصب‌شده در محیط فعال"""
        return 'pip list'

    @property
    def outdated(self):
        """pip list --outdated  |  نمایش کتابخونه‌هایی که نسخه جدیدتر دارند"""
        return 'pip list --outdated'

    @property
    def upgrade(self):
        """pip install --upgrade نام_کتابخانه  |  مثال: pip install --upgrade numpy  |  آپدیت یک کتابخانه خاص"""
        return 'pip install --upgrade numpy'

    @property
    def uninstall(self):
        """pip uninstall نام_کتابخانه  |  مثال: pip uninstall numpy  |  حذف یک کتابخانه"""
        return 'pip uninstall numpy'

    @property
    def restore(self):
        """pip install -r requirements.txt  |  برگشت به نسخه‌های قفل‌شده در requirements.txt"""
        return 'pip install -r requirements.txt'

    @property
    def check(self):
        """pip -V  |  یا: python -c "import sys; print(sys.prefix)"  |  تست سلامت: آیا محیط مجازی فعال است؟"""
        return 'pip -V'

    @property
    def delete_env(self):
        """rmdir /s venv  |  حذف کامل پوشه محیط مجازی (ابتدا deactivate کن)"""
        return 'rmdir /s venv'

    @property
    def rebuild(self):
        """python -m venv venv  |  ساخت دوباره محیط مجازی بعد از حذف"""
        return 'python -m venv venv'

    @property
    def requirements_sample(self):
        """opencv-python==4.12.0  |  نمونه محتوای فایل requirements.txt با نسخه دقیق"""
        return 'opencv-python==4.12.0'

    @property
    def pip_meaning(self):
        """pip = Package Installer for Python  |  مدیر بسته‌های پایتون"""
        return 'pip = Package Installer for Python'

    @property
    def venv_meaning(self):
        """venv = Virtual Environment  |  محیط مجازی: پوشه‌ای با کپی سبک از پایتون و pip"""
        return 'venv = Virtual Environment'


# ==============================================
# CVTools Class: Image display with zoom & rotation
# ==============================================


class CVTools:

    def __init__(self):
        self.venv = VenvCheatSheet()

    # ------------------------------------------
    # Display image with keyboard zoom
    # ------------------------------------------
    def imshow(self, winname, img):
        """
        نمایش تصویر با قابلیت خودکار تنظیم پنجره تصویر با کیبورد
        مثال: cvt.imshow("win", rotated)
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
            elif cv2.getWindowProperty(winname, cv2.WND_PROP_VISIBLE) < 1:
                break

    # ------------------------------------------
    # Rotate image without cropping corners
    # ------------------------------------------
    def rotate(self, img, angle):
        """
        چرخش خودکار تصویر  تنها با پارامتر درجه
        مثال : rotated = cvt.rotate(img, 45)
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

    # ============================================================
    # Resize: ریسایز با حفظ نسبت اتوماتیک ابعاد
    # ============================================================
    @staticmethod
    def resize(img, new_h=None, new_w=None, interpolation=None):
        """
        تغییر اندازه تصویر با حفظ نسبت ابعاد یا با استفاده از ابعاد سفارشی.

        Parameters:
            img: تصویر اولیه
            new_h: ارتفاع جدید (optional — اگر ندهیم، محاسبه از روی عرض جدید)
            new_w: عرض جدید (optional — اگر ندهیم محاسبه از روی ارتفاع جدید)
            یکی از این دو اجباری و دومی اختیاری است
            interpolation: Interpolation method (اختیاری)
                پیشفرض: cv2.INTER_AREA برای کوچک سازی
                , cv2.INTER_CUBIC برای بزرگنمایی

        Examples:
            cvt.resize(img, new_w=800)
            cvt.resize(img, new_h=600)
            cvt.resize(img, new_w=800, new_h=600)
            cvt.resize(img, new_w=400, interpolation=cv2.INTER_LINEAR)
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

    # ============================================================
    # جستجوی فایل یا پوشه در کل پروژه و درج مسیر به صورت هشتگ‌شده
    # ============================================================
    def search_path(self, names):
        """
        جستجوی فایل یا پوشه در کل پروژه و درج مسیر کامل آن‌ها به صورت هشتگ‌شده در فایل جاری.

        قابلیت‌ها:
        - جستجوی case-insensitive
        - جستجوی فایل‌ها و پوشه‌هایی که حاوی عبارت مورد نظر باشند
        - پشتیبانی از جستجوی همزمان چند نام

        پارامترها:
            names: نام فایل/پوشه (رشته) یا لیستی از نام‌ها برای جستجو

        مثال‌ها:
            cvt.search_path("pandas")
            cvt.search_path("cow")
            cvt.search_path(["utils", "data", "model"])
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

        hashtag_lines = []
        hashtag_lines.append(f"# ----------------------------------------")
        hashtag_lines.append(f"# Path search results")
        hashtag_lines.append(f"# ----------------------------------------")

        total_found = len(found_paths)
        total_not_found = len(not_found)

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

        hashtag_lines.append(f"# ----------------------------------------")
        hashtag_lines.append(
            f"# Summary: Found {total_found} | Not found {total_not_found}"
        )
        hashtag_lines.append(f"# ----------------------------------------")

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

    # ============================================================
    # اتوکامپلیت کد از تمام فایل‌های پروژه
    # ============================================================
    def auto_comp(self, keyword):
        """
        اتوکامپلیت هوشمند کد: جستجوی کدهای مرتبط با کلیدواژه در تمام فایل‌های پایتون پروژه.

        پارامترها:
            keyword: کلمه کلیدی برای جستجوی کد

        مثال‌ها:
            cvt.auto_comp("fig")
            cvt.auto_comp("axs")
        """
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename

        project_root = _self_dir.parent.resolve()
        module_file = os.path.abspath(__file__)

        search_files = []

        for root, dirs, files in os.walk(project_root):
            dirs[:] = [
                d
                for d in dirs
                if not d.startswith(".")
                and d not in ["__pycache__", "venv", "env", "node_modules"]
            ]

            for file_name in files:
                if file_name.endswith(".py"):
                    file_path = os.path.join(root, file_name)
                    if os.path.abspath(file_path) != module_file:
                        search_files.append(file_path)

        if not search_files:
            print(f"No Python files found in project.")
            return

        keyword_lower = keyword.lower()
        all_code_blocks = []

        for file_path in search_files:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                code_lines = self._extract_code_from_docstrings(content)
                regular_lines = self._extract_regular_code_lines(content)
                code_lines.extend(regular_lines)

                matching_indices = []
                for i, line in enumerate(code_lines):
                    if keyword_lower in line.lower():
                        matching_indices.append(i)

                if matching_indices:
                    blocks = self._group_consecutive_lines(code_lines, matching_indices)
                    for block in blocks:
                        all_code_blocks.append({"lines": block, "file": file_path})

            except Exception as e:
                print(f"Warning: Could not read file '{file_path}': {e}")

        unique_blocks = []
        seen_blocks = set()

        for block in all_code_blocks:
            block_key = "\n".join(block["lines"])
            if block_key not in seen_blocks:
                seen_blocks.add(block_key)
                unique_blocks.append(block)

        hashtag_lines = []
        hashtag_lines.append(f"# ----------------------------------------")
        hashtag_lines.append(f"# Auto-complete results for: '{keyword}'")
        hashtag_lines.append(f"# ----------------------------------------")

        if unique_blocks:
            current_file = None
            block_num = 0

            for block in unique_blocks:
                if block["file"] != current_file:
                    if current_file is not None:
                        hashtag_lines.append("#")
                    file_name = os.path.basename(block["file"])
                    hashtag_lines.append(f"# From: {file_name}")
                    current_file = block["file"]
                    block_num = 0

                block_num += 1
                if len(unique_blocks) > 1:
                    hashtag_lines.append(f"# Block {block_num}:")

                for line in block["lines"]:
                    hashtag_lines.append(f"# {line}")
                hashtag_lines.append("#")

            hashtag_lines.append(f"# ----------------------------------------")
            hashtag_lines.append(f"# Found {len(unique_blocks)} code block(s)")
        else:
            hashtag_lines.append(f"# No code snippets found for '{keyword}'")

        hashtag_lines.append(f"# ----------------------------------------")

        try:
            with open(caller_file, "a", encoding="utf-8") as f:
                f.write("\n".join(hashtag_lines) + "\n")

            if unique_blocks:
                print(
                    f"Auto-complete for '{keyword}' -> Found {len(unique_blocks)} block(s):"
                )
                for block in unique_blocks[:2]:
                    print(f"  {block['lines'][0][:80]}")
                    if len(block["lines"]) > 1:
                        print(f"  ... ({len(block['lines'])} lines)")
            else:
                print(f"Auto-complete for '{keyword}' -> No results found")

            print(f"Results appended to: {caller_file}")

        except Exception as e:
            print(f"Error writing to file '{caller_file}': {e}")

    def _extract_code_from_docstrings(self, content):
        code_lines = []
        triple_pattern = re.compile(r'("""|\'\'\')(.*?)\1', re.DOTALL)

        for match in triple_pattern.finditer(content):
            doc_content = match.group(2)
            lines = doc_content.split("\n")

            for line in lines:
                stripped = line.strip()

                if not stripped:
                    continue

                if stripped.startswith("#"):
                    continue

                if self._looks_like_code(stripped):
                    if "#" in stripped:
                        code_part = stripped.split("#")[0].rstrip()
                        if code_part:
                            code_lines.append(code_part)
                    else:
                        code_lines.append(stripped)

        return code_lines

    def _extract_regular_code_lines(self, content):
        code_lines = []
        no_docstrings = re.sub(r'("""|\'\'\')(.*?)\1', "", content, flags=re.DOTALL)

        lines = no_docstrings.split("\n")
        for line in lines:
            stripped = line.strip()

            if not stripped or stripped.startswith("#"):
                continue

            if self._looks_like_code(stripped):
                if "#" in stripped:
                    code_part = stripped.split("#")[0].rstrip()
                    if code_part:
                        code_lines.append(code_part)
                else:
                    code_lines.append(stripped)

        return code_lines

    def _looks_like_code(self, line):
        code_indicators = [
            "=",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
            ":",
            ".",
            ",",
            "import ",
            "from ",
            "def ",
            "class ",
            "return ",
            "plt.",
            "cv2.",
            "np.",
            "pd.",
            "tf.",
            "torch.",
            "axs",
            "fig",
            "ax.",
            "print(",
            "len(",
            "range(",
            "+",
            "-",
            "*",
            "/",
            "==",
            "!=",
            "<",
            ">",
            "True",
            "False",
            "None",
            "self",
            "lambda",
        ]

        if len(line) > 100 and not any(
            ind in line for ind in ["=", "(", ".", "import"]
        ):
            return False

        for indicator in code_indicators:
            if indicator in line:
                return True

        if len(line) < 30 and " " not in line:
            return True

        return False

    def _group_consecutive_lines(self, all_lines, matching_indices):
        if not matching_indices:
            return []

        blocks = []
        current_block = [all_lines[matching_indices[0]]]

        for i in range(1, len(matching_indices)):
            if matching_indices[i] == matching_indices[i - 1] + 1:
                current_block.append(all_lines[matching_indices[i]])
            else:
                blocks.append(current_block)
                current_block = [all_lines[matching_indices[i]]]

        blocks.append(current_block)

        return blocks


cvt = CVTools()