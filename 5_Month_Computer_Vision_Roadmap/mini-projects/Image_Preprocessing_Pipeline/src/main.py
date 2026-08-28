p = print
from pathlib import Path
import numpy as np
import cv2
from cvtools import cvt
# -------------------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\Image_Preprocessing_Pipeline\Data"
)
output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\Image_Preprocessing_Pipeline\outputs"
)
output.mkdir(parents=True, exist_ok=True)
paths = [str(i) for i in folder.glob("*.jpg")]
# -----------------------------
for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
    clahe_img = clahe.apply(gray)
    # -------------------------------
    thresh_adapt_gray_base = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        21,
        3,
    )
    thresh_adapt_clahe_base = cv2.adaptiveThreshold(
        clahe_img,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        21,
        3,
    )
    # -----------------------------
    thresh_comparision = np.hstack([thresh_adapt_gray_base, thresh_adapt_clahe_base])
    # cvt.imshow("win", thresh_comparision)

    # چرا از CLAHE در پایپلاین نهایی استفاده نشد؟
    # → توضیح کامل در README، بخش Analysis Q1
    # -----------------------------------
    kernel_soft = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opened = cv2.morphologyEx(thresh_adapt_gray_base, cv2.MORPH_OPEN, kernel_soft)
    closed = cv2.morphologyEx(thresh_adapt_gray_base, cv2.MORPH_CLOSE, kernel_soft)
    # ------------------------------
    name = Path(i).stem
    comparision = np.hstack([gray, clahe_img, opened, closed])
    cv2.imwrite(
        output / f"{name}_gray_clahe_opened_closeed_comparision.jpg", comparision
    )
# ---------------------------
# تحلیل کامل نتایج:
# - تاثیر مراحل
# - نیاز به پایپلاین یکسان
# - پیشنهاد بهبود
# → README، بخش Analysis
