# Month-01
# Week-04
# Day-02

# تمرین: یک تصویر نویزی پیدا کن یا بساز
# با medianBlur
# نویز را حذف کن و نتیجه را با
# Gaussian
# مقایسه کن
# -------------------------------------
path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-02\Data\Chaplin.jpg"
import cv2
# from cvtools import cvt
from pathlib import Path
p = print

img = cv2.imread(path)
# ------------------------
ksizes = [3,5,9]
for i in ksizes:
    gaussian = cv2.GaussianBlur(img,(i,i),sigmaX=0)
    median_blur = cv2.medianBlur(img,i)
    # -------------------------------
    output = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-02\Output"
    )
    output.mkdir(parents=True,exist_ok=True)
    # ----------------------------
    cv2.imwrite(output / "chaplin_orginal.jpg", img)
    cv2.imwrite(output/f"chapline_gaussian_{i}.jpg",gaussian)
    cv2.imwrite(output / f"chapline_median_blur_{i}.jpg", median_blur)
