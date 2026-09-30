# Project Installation Guide | راهنمای نصب پروژه

## 🇬🇧 English

### Method 1: Automatic Installation (Recommended for Windows 64-bit + Python 3.12)

1. Download the ZIP file from [Releases](https://github.com/Bryaryounesi/INTPCode/releases/tag/v1.0.0).
2. Extract the ZIP file. You'll get a `wheels` folder.
3. Put the `wheels` folder next to `install.bat`.
4. Double-click `install.bat`.
5. All packages (including PyTorch) will be installed offline. No internet needed.

**Note:** The filename of the ZIP might be different. It doesn't matter. Just extract it and find the `wheels` folder inside.

### Method 2: Manual Installation (For Other Systems)

If your Python version or operating system is different:

1. Install PyTorch separately:


pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cpu


2. Install other packages:


pip install -r requirements.txt


---

## 🇮🇷 فارسی

### روش اول: نصب خودکار (پیشنهادی برای ویندوز ۶۴ بیتی + پایتون ۳.۱۲)

۱. فایل ZIP رو از [Releases](https://github.com/Bryaryounesi/INTPCode/releases/tag/v1.0.0) دانلود کن.
۲. فایل ZIP رو Extract کن. یه پوشه `wheels` به دست میاری.
۳. پوشه `wheels` رو کنار `install.bat` بذار.
۴. روی `install.bat` دابل‌کلیک کن.
۵. همه کتابخانه‌ها (شامل پایتورچ) به صورت آفلاین نصب می‌شن. اینترنت لازم نیست.

**نکته:** اسم فایل ZIP ممکنه فرق کنه. مهم نیست. فقط Extractش کن و پوشه `wheels` رو از داخلش پیدا کن.

### روش دوم: نصب دستی (برای سیستم‌های دیگه)

اگه پایتون یا سیستم‌عاملت فرق داره:

۱. پایتورچ رو جداگانه نصب کن:


pip install torch torchaudio torchvision --index-url https://download.pytorch.org/whl/cpu


۲. بقیه کتابخانه‌ها رو نصب کن:


pip install -r requirements.txt
