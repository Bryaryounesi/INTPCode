# Month-02
# Week-02
# Day-02
# --------------------------------
# تمرین :
# 📝 روی چند تصویر، کرنل‌ها و
# Iteration
# های مختلف
# Erosion
# را آزمایش کن

import cv2
from pathlib import Path
from cvtools import cvt
import numpy as np
from itertools import product
# ----------------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-02\Data"
)

# -----------------------------------------
paths = [str(i) for i in folder.glob("*.jpg")]
for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _ ,th = cv2.threshold(gray, 190,255,cv2.THRESH_BINARY_INV)
    # -----------------------------------------
    ksizes = [3,5,7]
    shapes = [cv2.MORPH_ELLIPSE ,cv2.MORPH_RECT , cv2.MORPH_CROSS]
    iterations= [1,2,3]
    for shape , k, itr  in product(shapes,ksizes,iterations):
        # از کتابخانه ایترتولز و تابع پروداکت به جای لوپ تودرتوی دوم و سوم استفاده کردیم
        # ابتدا شیپ و بعد کی سایز رو در حلقه تعریف کردیم
        # تا ابتدا هر شیپ با تمام کی سایزهایش روی تصویر اعمال بشه بعد بره تصویر بعدی
        kernel = cv2.getStructuringElement(shape,(k,k))
        eroded = cv2.erode(th , kernel , itr)
        name = Path(i).stem
        # ---------------------------
        if shape == cv2.MORPH_ELLIPSE:
            shape_name = "ELLIPSE"
        elif shape == cv2.MORPH_CROSS:
            shape_name = "CROSS"
        elif shape == cv2.MORPH_RECT:
            shape_name = "RECT"
        # -------------------------------
        comparision = np.hstack([th,eroded])
        cv2.imshow(f"{name}_Binary_VS_{(k,k)}_{shape_name}_iteration{(itr)}_Eroded",comparision)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

'''
سه کرنل، هر کدام با سه کی سایز و سه ایتریشن روی چند تصویر باینری تست شدند
به دلیل پرتعداد بودن پارامترها و حالت های تصویر،بررسی با مشاهده تصاویر و نه ذخیره آنها انجام شد.

تصاویری که در مرحله باینری شدن دچار نقص بودند
(مثلا دچار تله تونال بودند)
با اعمال کرنل هم نقصشان برطرف نشد.

اعمال اروشن  در تصاویر باینری با پس زمینه سیاه، سبب باریک تر شدن اشیا و نفوذ سیاهی پس زمینه به درون شی میشود. تصویر با افزایش کی سایز و ایتریشن سیاه و سیاه تر میشود و شاید کلا در سیاهی پس زمینه از بین برود
'''
