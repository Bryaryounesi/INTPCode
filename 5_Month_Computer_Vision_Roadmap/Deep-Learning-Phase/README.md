# Project Installation Guide | راهنمای نصب پروژه

## 🇬🇧 English

### Method 1: Automatic Installation (Recommended for Windows 64-bit + Python 3.12)

1. Make sure `install.bat` and `wheels` folder are in the same directory.
2. Double-click `install.bat`.
3. All packages (including PyTorch) will be installed offline. No internet needed.

### Method 2: Manual Installation (For Other Systems)

If your Python version or operating system is different:

1. Install PyTorch separately:


pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cpu


2. Install other packages:


pip install -r requirements.txt


---

## 🇮🇷 فارسی

### روش اول: نصب خودکار (پیشنهادی برای ویندوز ۶۴ بیتی + پایتون ۳.۱۲)

۱. مطمئن شو `install.bat` و پوشه `wheels` کنار هم هستن.
۲. روی `install.bat` دابل‌کلیک کن.
۳. همه کتابخانه‌ها (شامل پایتورچ) به صورت آفلاین نصب می‌شن. اینترنت لازم نیست.

### روش دوم: نصب دستی (برای سیستم‌های دیگه)

اگه پایتون یا سیستم‌عاملت فرق داره:

۱. پایتورچ رو جداگانه نصب کن:


pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cpu


۲. بقیه کتابخانه‌ها رو نصب کن:


pip install -r requirements.txt
