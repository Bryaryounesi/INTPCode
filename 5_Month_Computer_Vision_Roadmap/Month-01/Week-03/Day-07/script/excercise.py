# Month-01
# Week-03
# Day-07
# weekly task
# ----------------------

# 1-  سه تصویر دلخواه انتخاب کن و  برای هر کدام،
# حداقل ۳ نسخه با این تغییرات ( تغییر اندازه، برش، چرخش) بساز و ذخیره کن
import cv2
from pathlib import Path
# from cvtools import cvt
p = print
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data")
pathes = [str(i) for i in folder.glob("*.jpg")]
# چون تصاویر بیش از یک مورد بودند به جای وارد کردن تک تک مسیر ها، با پزلیب یک لیست از کل مسیر های تصاویر ساختیم و حالا باید برای سرعت کار روی این لیست حلقه بزنیم
# ---------------------------------------------
for i in pathes:
    img = cv2.imread(i)     #خواندن تصویر
    if img is None:         #کد جلوگیری از ارور در صورت مشکل دار بودن تصاویر
        p(f"error in reading: {i}")
        continue
    # ----------------------------
    resized = cv2.resize(img,dsize=None,fx=0.7,fy = 0.7,interpolation=cv2.INTER_LINEAR)  #ریسایز
    # ----------------------
    h,w = img.shape[:2]
    roi = img[h//4:3*h//4,w//4:3*w//4]      #برش تصویر
    # -------------------------
    rotated = cv2.rotate(img,cv2.ROTATE_90_COUNTERCLOCKWISE)       #چرخش تصویر
    # cvt.imshow("win",rotated)
    # -------------------------
    # ساخت نام بدون پسوند تصاویر از مسیر آنها برای نام گذاری نهایی تصاویر در هنگام ذخیره سازی
    name = Path(i).stem
    # name = i.split("\\")[-1].split(".")[0]   کد معادل
    # --------------------------------------
    # ساخت مسیر خروجی :
    output = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Output"
    )
    output.mkdir(parents= True,exist_ok=True)
    # کد ایمنی در برابر نبود احتمالی پوشه خروجی
    # --------------------------------
    # خواندن تصویر:
    # cv2.imwrite(output / f"resized_{name}.jpg",resized)
    # cv2.imwrite(output / f"roi_{name}.jpg", roi)
    # cv2.imwrite(output / f"rotated_{name}.jpg", rotated)

# تمام عملیات ها و ذخیره آنها درون یک حلقه انجام شد تا از تکرار بیهوده کد جلوگیری شود
# ---------------------------------------
# 2- بررسی کن که تصاویر برای پروژه آماده شده(آمادگی فنی تصاویر )
# Image processing ready
# این نوع آمادگی با آمادگی برای آموزش مدل فرق میکند و سطحی ابتدایی تر از آمادگی است

# چک لیست آمادگی فنی:
# ✅ تصویر خوانده می‌شود
# ✅ تغییر اندازه انجام می‌شود
# ✅ برش انجام می‌شود
# ✅ چرخش انجام می‌شود
# ✅ ذخیره خروجی انجام می‌شود
# پس بله تصاویر، این مرحله از آمادگی را دارند
