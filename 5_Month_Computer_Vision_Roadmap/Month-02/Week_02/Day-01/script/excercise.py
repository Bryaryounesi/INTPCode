# Month-02
# Week-02
# Day-01

# تمرین :
# برای یک تصویر باینری، کرنل های 5*5 ، 3*3 و 7*7 بساز و تفاوت آنها را مشاهده کن
# --------------------------------
p = print
import cv2
import numpy as np
from pathlib import Path
# -------------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-01\Data"
)

paths = [str(i) for i in folder.glob("*.jpg")]
# ----------------------------------
for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(gray,238,255,cv2.THRESH_BINARY)
    # ------------------------------
    ksizes = [3,5,7]
    shapes= [cv2.MORPH_ELLIPSE,cv2.MORPH_CROSS,cv2.MORPH_RECT]
    for shape in shapes:   #لوپ دوم،اشکال کرنل
        for k in ksizes:        #لوپ سوم اندازه کرنل
            # میتوان به جای این دو لوپِ تودرتو از کتابخانه ایترتول و یک لوپ استفاده کرد
            kernel = cv2.getStructuringElement(shape,(k,k))
            if shape == cv2.MORPH_ELLIPSE:
                shape_name = "ELLIPSE"
            elif shape == cv2.MORPH_CROSS:
                shape_name = "CROSS"
            elif shape == cv2.MORPH_RECT:
                shape_name ="RECT"
                # ساخت یک متغیر جدید در لوپ پایانی به نام شیپ نیم برای استفاده بعدی
                # -------------------------------------
            name = Path(i).stem
            p(f"{name}_{(k,k)}_{shape_name}:")
            p(kernel)
            p("---------------------")
