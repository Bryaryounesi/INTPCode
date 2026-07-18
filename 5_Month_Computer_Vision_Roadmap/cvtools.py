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
# مثال برای جستجوی مسیر فایل و پوشه ها
cvt.search_path("pandas_cheatsheet.py")
cvt.search_path("my_image")  # finds my_image.jpg, my_image.png, etc.
cvt.search_path(["utils.py", "data/", "models"])
# ------------------
cvt.auto_comp("key_word")
مثال:
cv.auto_comp(".drop")
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
# CVTools Class: Image display with zoom & rotation
# ==============================================


class CVTools:

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
    # ریسایز تنها با یک بعد از تصویر و بدون تناسب گیری بعد دیگر
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
            # -----------------------------------
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
                interpolation = cv2.INTER_AREA  # downscaling
            else:
                interpolation = cv2.INTER_CUBIC  # upscaling

        return cv2.resize(img, (new_w, new_h), interpolation=interpolation)

    # ============================================================
    # جستجوی فایل یا پوشه در کل پروژه و درج پَز به صورت هشتگ‌شده
    # ============================================================
    def search_path(self, names):
        """
        جستجوی فایل یا پوشه در کل پروژه و درج مسیر کامل آن‌ها به صورت هشتگ‌شده در فایل جاری.

        قابلیت‌ها:
        - جستجوی case-insensitive (بدون حساسیت به حروف بزرگ/کوچک)
        - جستجوی فایل‌ها و پوشه‌هایی که حاوی عبارت مورد نظر باشند
        - پشتیبانی از جستجوی همزمان چند نام

        پارامترها:
            names: نام فایل/پوشه (رشته) یا لیستی از نام‌ها برای جستجو

        مثال‌ها:
            cvt.search_path("pandas")  # همه فایل‌ها/پوشه‌های حاوی "pandas"
            cvt.search_path("cow")  # Cow, COW, cow_images و غیره
            cvt.search_path(["utils", "data", "model"])  # ترکیبی
        """
        # Get the path of the calling script (the current file)
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename

        # Get the project root directory (parent of cvtools module)
        project_root = _self_dir.parent.resolve()

        # Convert names to a list if a string is provided
        if isinstance(names, str):
            names = [names]

        # Collect all found paths
        found_paths = {}
        not_found = []

        for name in names:
            name_found = False
            name_lower = name.lower()

            # Walk through the entire project directory
            for root, dirs, files in os.walk(project_root):
                # Skip hidden directories and common non-project folders
                dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', 'env', 'node_modules']]

                # Check for directory matches (case-insensitive contains)
                for dir_name in dirs:
                    if name_lower in dir_name.lower():
                        full_path = os.path.join(root, dir_name)
                        if name not in found_paths:
                            found_paths[name] = []
                        found_paths[name].append(full_path)
                        name_found = True

                # Check for file matches (case-insensitive contains)
                for file_name in files:
                    if name_lower in file_name.lower():
                        full_path = os.path.join(root, file_name)
                        if name not in found_paths:
                            found_paths[name] = []
                        found_paths[name].append(full_path)
                        name_found = True

            if not name_found:
                not_found.append(name)

        # Prepare hashtagged output in the exact requested format
        hashtag_lines = []
        hashtag_lines.append(f"# ----------------------------------------")
        hashtag_lines.append(f"# Path search results")
        hashtag_lines.append(f"# ----------------------------------------")

        total_found = len(found_paths)
        total_not_found = len(not_found)

        for name, paths in found_paths.items():
            hashtag_lines.append(f"# Search: '{name}' → Found {len(paths)} match(es)")
            hashtag_lines.append("")
            for path in paths:
                hashtag_lines.append(f"# path: {path}")

        if not_found:
            if found_paths:
                hashtag_lines.append("")
            for name in not_found:
                hashtag_lines.append(f"# Search: '{name}' → Not found")

        hashtag_lines.append(f"# ----------------------------------------")
        hashtag_lines.append(f"# Summary: Found {total_found} | Not found {total_not_found}")
        hashtag_lines.append(f"# ----------------------------------------")

        # Append results to the end of the current file
        try:
            with open(caller_file, 'a', encoding='utf-8') as f:
                f.write('\n'.join(hashtag_lines) + '\n')

            # Print summary to console
            if found_paths:
                for name, paths in found_paths.items():
                    print(f"'{name}' → Found {len(paths)} match(es):")
                    for path in paths:
                        print(f"  + {path}")

            if not_found:
                for name in not_found:
                    print(f"'{name}' → Not found")

            print(f"\nResults appended to: {caller_file}")

        except Exception as e:
            print(f"Error writing to file '{caller_file}': {e}")

        # ============================================================
    # اتوکامپلیت کد از تمام فایل‌های پروژه
    # ============================================================
    def auto_comp(self, keyword):
        """
        اتوکامپلیت هوشمند کد: جستجوی کدهای مرتبط با کلیدواژه در تمام فایل‌های پایتون پروژه.

        این متد تمام فایل‌های py. در کل پروژه (workspace) را جستجو کرده،
        سپس خطوط کدی که حاوی کلیدواژه هستند را استخراج می‌کند.
        خطوط کد پشت سر هم مرتبط را به صورت بلوک‌های مجزا و هشتگ‌شده نمایش می‌دهد.

        پارامترها:
            keyword: کلمه کلیدی برای جستجوی کد (مثلاً "fig", "plt.plot", "cv2.imread")

        مثال‌ها:
            >>> fig
            >>> cvt.auto_comp("fig")

            >>> cvt.auto_comp("axs")
            # بلوک‌های مجزا برای axs[0] و axs[1] و fig, axs = plt.subplots
        """
        # Get the path of the calling script (the current file)
        caller_frame = inspect.stack()[1]
        caller_file = caller_frame.filename

        # Get the project root directory
        project_root = _self_dir.parent.resolve()

        # Get the path of this module file to exclude it
        module_file = os.path.abspath(__file__)

        # Step 1: Find all Python files in the entire project workspace
        search_files = []

        for root, dirs, files in os.walk(project_root):
            # Only skip hidden and cache directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', 'env', 'node_modules']]

            for file_name in files:
                if file_name.endswith('.py'):
                    file_path = os.path.join(root, file_name)
                    # Skip the cvtools module file itself
                    if os.path.abspath(file_path) != module_file:
                        search_files.append(file_path)

        if not search_files:
            print(f"No Python files found in project.")
            return

        # Step 2: Search for the keyword and extract code blocks
        keyword_lower = keyword.lower()
        all_code_blocks = []

        for file_path in search_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract code from triple-quoted strings (docstrings)
                code_lines = self._extract_code_from_docstrings(content)

                # Also get regular code lines (outside docstrings)
                regular_lines = self._extract_regular_code_lines(content)
                code_lines.extend(regular_lines)

                # Find lines containing the keyword
                matching_indices = []
                for i, line in enumerate(code_lines):
                    if keyword_lower in line.lower():
                        matching_indices.append(i)

                # Group consecutive lines into blocks
                if matching_indices:
                    blocks = self._group_consecutive_lines(code_lines, matching_indices)
                    for block in blocks:
                        all_code_blocks.append({
                            'lines': block,
                            'file': file_path
                        })

            except Exception as e:
                print(f"Warning: Could not read file '{file_path}': {e}")

        # Step 3: Remove duplicate blocks
        unique_blocks = []
        seen_blocks = set()

        for block in all_code_blocks:
            block_key = '\n'.join(block['lines'])
            if block_key not in seen_blocks:
                seen_blocks.add(block_key)
                unique_blocks.append(block)

        # Step 4: Prepare hashtagged output
        hashtag_lines = []
        hashtag_lines.append(f"# ----------------------------------------")
        hashtag_lines.append(f"# Auto-complete results for: '{keyword}'")
        hashtag_lines.append(f"# ----------------------------------------")

        if unique_blocks:
            current_file = None
            block_num = 0

            for block in unique_blocks:
                if block['file'] != current_file:
                    if current_file is not None:
                        hashtag_lines.append("#")
                    file_name = os.path.basename(block['file'])
                    hashtag_lines.append(f"# From: {file_name}")
                    current_file = block['file']
                    block_num = 0

                block_num += 1
                if len(unique_blocks) > 1:
                    hashtag_lines.append(f"# Block {block_num}:")

                # All code lines are hashtagged to avoid linter errors
                for line in block['lines']:
                    hashtag_lines.append(f"# {line}")
                hashtag_lines.append("#")

            hashtag_lines.append(f"# ----------------------------------------")
            hashtag_lines.append(f"# Found {len(unique_blocks)} code block(s)")
        else:
            hashtag_lines.append(f"# No code snippets found for '{keyword}'")

        hashtag_lines.append(f"# ----------------------------------------")

        # Step 5: Append results to the current file
        try:
            with open(caller_file, 'a', encoding='utf-8') as f:
                f.write('\n'.join(hashtag_lines) + '\n')

            if unique_blocks:
                print(f"Auto-complete for '{keyword}' -> Found {len(unique_blocks)} block(s):")
                for block in unique_blocks[:2]:
                    print(f"  {block['lines'][0][:80]}")
                    if len(block['lines']) > 1:
                        print(f"  ... ({len(block['lines'])} lines)")
            else:
                print(f"Auto-complete for '{keyword}' -> No results found")

            print(f"Results appended to: {caller_file}")

        except Exception as e:
            print(f"Error writing to file '{caller_file}': {e}")

    def _extract_code_from_docstrings(self, content):
        """
        Extract only code lines from triple-quoted docstrings.
        Ignores Persian text, explanations, and comment lines.
        """
        code_lines = []

        # Find all triple-quoted strings
        triple_pattern = re.compile(r'("""|\'\'\')(.*?)\1', re.DOTALL)

        for match in triple_pattern.finditer(content):
            doc_content = match.group(2)
            lines = doc_content.split('\n')

            for line in lines:
                stripped = line.strip()

                # Skip empty lines
                if not stripped:
                    continue

                # Skip comment lines (start with #)
                if stripped.startswith('#'):
                    continue

                # Check if it looks like code (contains Python syntax)
                if self._looks_like_code(stripped):
                    # Remove inline comments
                    if '#' in stripped:
                        code_part = stripped.split('#')[0].rstrip()
                        if code_part:
                            code_lines.append(code_part)
                    else:
                        code_lines.append(stripped)

        return code_lines

    def _extract_regular_code_lines(self, content):
        """
        Extract code lines that are not inside docstrings.
        """
        code_lines = []

        # Remove docstrings first
        no_docstrings = re.sub(r'("""|\'\'\')(.*?)\1', '', content, flags=re.DOTALL)

        lines = no_docstrings.split('\n')
        for line in lines:
            stripped = line.strip()

            # Skip empty lines and comments
            if not stripped or stripped.startswith('#'):
                continue

            # Skip lines that look like plain text (Persian or English sentences)
            if self._looks_like_code(stripped):
                # Remove inline comments
                if '#' in stripped:
                    code_part = stripped.split('#')[0].rstrip()
                    if code_part:
                        code_lines.append(code_part)
                else:
                    code_lines.append(stripped)

        return code_lines

    def _looks_like_code(self, line):
        """
        Check if a line looks like Python code rather than plain text.
        Returns True if it looks like code.
        """
        # Must contain Python-specific characters or patterns
        code_indicators = [
            '=', '(', ')', '[', ']', '{', '}', ':', '.', ',',
            'import ', 'from ', 'def ', 'class ', 'return ',
            'plt.', 'cv2.', 'np.', 'pd.', 'tf.', 'torch.',
            'axs', 'fig', 'ax.', 'print(', 'len(', 'range(',
            '+', '-', '*', '/', '==', '!=', '<', '>',
            'True', 'False', 'None', 'self', 'lambda'
        ]

        # If line is too long and has no code indicators, probably text
        if len(line) > 100 and not any(ind in line for ind in ['=', '(', '.', 'import']):
            return False

        # Check if it contains any code indicators
        for indicator in code_indicators:
            if indicator in line:
                return True

        # If line is short and has no spaces, might be a variable name
        if len(line) < 30 and ' ' not in line:
            return True

        return False

    def _group_consecutive_lines(self, all_lines, matching_indices):
        """
        Group consecutive matching lines into blocks.
        Lines that are consecutive (index difference of 1) are grouped together.
        """
        if not matching_indices:
            return []

        blocks = []
        current_block = [all_lines[matching_indices[0]]]

        for i in range(1, len(matching_indices)):
            if matching_indices[i] == matching_indices[i-1] + 1:
                # Consecutive line, add to current block
                current_block.append(all_lines[matching_indices[i]])
            else:
                # New block starts
                blocks.append(current_block)
                current_block = [all_lines[matching_indices[i]]]

        # Don't forget the last block
        blocks.append(current_block)

        return blocks

cvt = CVTools()
