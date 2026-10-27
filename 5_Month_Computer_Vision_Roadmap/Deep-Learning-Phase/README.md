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

### 📂 Important Note for Mini-Projects

All mini-projects inside the **`dl-mini-projects/`** directory share the same virtual environment and dependencies.

You **do not** need to install packages separately for each project. Just follow the installation guide above **once** to set up your environment. After that, you are ready to run any project inside the `dl-mini-projects/` folder.

*(If you are writing a README for a specific mini-project, simply mention: "For installation and setup instructions, please refer to the main README in the parent directory.")*

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

### 📂 نکته مهم درباره مینی‌پروژه‌ها

تمام مینی‌پروژه‌های موجود در پوشه **`dl-mini-projects/`** از همین محیط مجازی (Virtual Environment) و همین کتابخانه‌های نصب‌شده استفاده می‌کنند.

شما **نیازی نیست** برای هر پروژه جداگانه کتابخانه نصب کنید. فقط **یک بار** مراحل نصب بالا را طی کنید تا محیط شما آماده شود. بعد از آن، می‌توانید هر پروژه‌ای در پوشه `dl-mini-projects/` را به راحتی اجرا کنید.
