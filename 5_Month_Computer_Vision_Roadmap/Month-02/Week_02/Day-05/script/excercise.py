# Month-02
# Week-02
# Day-05
# ---------------------------
# 📝 تمرین:
#  سه تصویر کم‌نور پیدا کن و
# Histogram Equalization
# را روی آن‌ها اجرا کن. تصاویر قبل و بعد را مقایسه کن
# -----------------
'''
در این تمرین، گفته تصاویر کم نور به جای کم کنتراست و این دو دقیقا یکی نیستن. ما هم تصاویر کم نور پیدا نکردیم و در نهایت از کم کنتراست
یعن با انحراف معیار کمتر از 50 استفاده شد.

هیستوگرام اکولایزیشن برای تصاویر کم نور زیاد خوب نیست و اگرچه آنها رو روشنتر میکند ولی جلوه ای مصنوعی و نویزی به آنها میدهد.
'''
# ---------------
# from cvtools import cvt
import cv2
import numpy as np
from pathlib import Path

# --------------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-05\Data")
output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-05\output"
)
output.mkdir(parents=True, exist_ok = True)
paths = [str(i) for i in folder.glob("*.jpg")]

# ----------------------------
for i in paths:
    img = cv2.imread(i)
    if np.std(img) < 50:
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equalized = cv2.equalizeHist(gray)
    # ----------------------------
    name = Path(i).stem
    comparision = np.hstack([gray, equalized])
    # cv2.imwrite(output/f"{name}_gray_VS_equalized_comparision.jpg",comparision)

# اکوالایز هیست، انگار با رنگی خاکستری، شیء درون تصویر را رنگ میکند
# ولی  چون کل تصویر رو یکجا پردازش میکند  علاوه بر شیء، بخشی از پس زمینه رو هم خراب میکند(مخصوصا در تصاویر با پس زمینه سفید) بنابراین شاید برای تصاویرِ با پس زمینه سفید، مناسب نباشد
