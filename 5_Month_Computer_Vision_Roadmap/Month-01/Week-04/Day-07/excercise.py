# Month-01
# Week-04
# Day-07
# weekly task:

# تمرین :
# یک پایپلاین تشخیص لبه بنویس و آن را روی چند تصویر اعمال کن
# -----------------------------
# pipeline (اولیه):
# img >>  blur >> gray >> threshold  >> edge(canny) >> save
"""
این پایپ لاین دو ایراد دارد:
1- بهتر است تبدیل به گری، قبل از بلور باشد تا از پردازش اضافه پرهیز شود

2- اغلب، تشخیص لبه روی بلور است و نه ترشهولد
زیرا هدف ترشهولد متفاوت از تشخیص لبه است پس اگر در یک پایپ لاین:
blur >> threshold >> Canny
ترشهولد، مخصوصا ترشهولد آداپتیو، نویز تصعیف شده توسط بلور را تشدید میکند و خروجی تشخیص لبه با حالتی شبیه به آغشتگی شدید تصویر با براده چوب مواجه میشود
---------------
blur >> Canny >> threshold
اگر هم روی بلور کنی بزنیم و بعد ترشهولد، ترشهولد کاری نسبتا بی تاثیر خواهد بود
زیرا خود کنی نوعی از ترشهولد را نیز در خود دارد
پس در کل، بهتر است ترشهولد و کنی در یک پایپلاین نباشند ولی میتوانند دو انشعاب از یک پایپلاین واحد باشند

"""

# pipeline (صلاح‌شده):
# img >> gray >> blur  >> branch a)  threshold >> save
#                                  >> branch b) edge(canny) >> save

import cv2
from pathlib import Path
import numpy as np
from cvtools import cvt

# ------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Data"
)
paths = [str(i) for i in folder.glob("*.jpg")]
# -----------------
# read img(grey)
for i in paths:
    img = cv2.imread(i, 0)
    # -----------------
    if img is None:
        continue
    if np.std(img) > 50:
        # ---------------------
        # blurring
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        # از مدیان بلور استفاده نشد چون تصاویر نویز فلفل نمکی نداشتند
        # -------------------------
        # branch a (threshold om blur)
        _,simple_th =cv2.threshold(blurred,100,255,cv2.THRESH_BINARY)
        adaptive_th = cv2.adaptiveThreshold(blurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,7)
        # هرچه پارامتر سی بزرگتر، پیوستگی خطوط بیشتر
        # هرچه پارامتر بلوک سایز کوچکتر(حتی کوچکتر از 11) خطوط باریکتر
        # پس در برخی تصاویر، ترشهولد آداپتیو با سی بالا و بلوک سایز پایین، عملکردی مشابه کنی دارد
        # --------------------------
        # branch b)  edge detection on blur (نه روی threshold!)

        thresholds = [(50, 150),(80,200),(80,240)]
        # این سه ترشهولد، بهترین ترشهولدهای کنی هستند
        for minval, maxval in thresholds:
            edge = cv2.Canny(blurred, minval, maxval)
            # ----------------------------
            output = Path(
                r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-07\Output"
            )
            output.mkdir(parents=True ,exist_ok=True)
            # -------------------------------
            # writing
            name = Path(i).stem
            cv2.imwrite(output/f"{name}_simple_threshold.jpg", simple_th)
            cv2.imwrite(output/f"{name}_adaptive_threshold.jpg", adaptive_th)
            cv2.imwrite(output/f"{name}_{minval}_{maxval}_canny_raw.jpg", edge)
