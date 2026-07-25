# Month-01
# Week-04
# Day-05
# -------------------------------------
# تمرین :
# روی چند تصویر
# canny
# را با مقادیر مختلف اجرا کن و بهترین حالت رو پیدا کن
# ---------------------------------
p = print
import cv2
from pathlib import Path
# from cvtools import cvt
import numpy as np

folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Data"
)
paths = [str(i) for i in folder.glob("*.jpg")]  #پز مسیر های تصاویر
# -------------------------------------
for i in paths:     #فیلتر تصاویر نامناسب احتمالی
    img = cv2.imread(i,0)
    if img is None:
        continue
    if np.std(img) > 50:   #فیلتر تصاویر بر حسب انحراف معیار (کنتراست)
        # ----------------------------------
        # لیست آستانه های بالا و پایین برای تشخیص لبه
        thresholds = [
            (50, 100),
            (50, 150),
            (100, 200),
            (100, 300),
            (150, 300)
        ]
        for minval,maxval in thresholds:    #حلقه زدن روی لیست آستانه ها
            edge = cv2.Canny(img,minval,maxval)
            # -----------------------------------
            cv2.imshow(f"{minval}_{maxval}_edge",edge)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
# تقریبا تمام تاپل های آستانه ای انتخاب شده مناسب هستند ولی در دو مورد آخر جزئیات بیشتری نسبت به بقیه از بین میرود و حتی در بسیاری از موارد لبه ها قطع میشوند
