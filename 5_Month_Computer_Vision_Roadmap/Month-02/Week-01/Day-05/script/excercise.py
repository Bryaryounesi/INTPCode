# Month-02
# Week-01
# Day-05
# تمرین :
# یک تصویر باینری رو پردازش کن و همه کانتورهای آن را رسم کن
# ----------------------------------
import cv2
from pathlib import Path
from cvtools import cvt
import numpy as np
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week-01\Day-05\Data"
)
paths = [str(i) for i in folder.glob("*.jpg")]

output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week-01\Day-05\output"
)
# ---------------------------
for i in paths:
    img = cv2.imread(i)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # ------------------
    thresh_adapt = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 23,-8)
    # از ترشهولد آداپتیو و سی منفی استفاده شد تا خطی سفید دور شی بسازد
    # تصویر چندین شی داشت و تصور شد این یکی از بهترین روش هاست
    # ----------------
    name = Path(i).name
    contours, _ = cv2.findContours(
        thresh_adapt, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # -------------------
    copied = img.copy()
    # ساخت یک کپی از تصاویر خام
    greatest_contours = sorted(contours , key = cv2.contourArea ,reverse=True)[:15]
    # مرتب کردن لیست آرایه های کانتور(کانتورها) بر حسب بزرگترین مساحت ها، سپس جدا کردن 15 مورد از آرایه هایی با بزرگترین مساحت
    # فقط بزرگترین کانتورها رو بر تصویر اعمال کردیم
    # -------------------------
    areas = [cv2.contourArea(c) for c in contours]
    # لیست مساحت های همه کانتورها
    perimeters = [cv2.arcLength(c,True) for c in contours]
    # لیست محیط  های همه کانتورها
    # این دو کاربرد چندانی در این مثال نداشتند
    # -------------------------------
    cv2.drawContours(copied,greatest_contours,-1,(0,255,0),3)
    cv2.imwrite(output/f"{name}_contours.jpg",copied)

# در این مبحث، نداشتن تصاویر مناسب سبب اتلاف وقت شد