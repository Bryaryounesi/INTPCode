# setup.py
# ============================================================
# مراحل راه‌اندازی ماژول cvtools برای استفاده در همه پوشه‌ها:
#
# ۱. pip install setuptools    ← اگر نصب نیست، یکبار اجرا شود
# ۲. pip install -e .          ← در ترمینال همین پوشه اجرا شود
#    (حالا from cvtools import cvt در هر پوشه‌ای کار می‌کند)
#
# ۳. تنظیمات VSCode برای Pylance:
#    Ctrl+Shift+P ← Open Workspace Settings (JSON)
#    اضافه کردن مسیر پوشه cvtools به extraPaths:
#    "python.analysis.extraPaths": ["مسیر/پوشه/حاوی/cvtools"]
# ============================================================

from setuptools import setup

setup(
    name="cvtools",
    py_modules=["cvtools"],
)
