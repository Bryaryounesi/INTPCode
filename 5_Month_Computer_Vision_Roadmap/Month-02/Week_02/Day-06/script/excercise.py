# Month-02
# Week-02
# Day-06
# ----------------------
# تمرین :
# روی همان تصاویر روز قبل، کلِی را اجرا کن و خروجی را با
# equalizeHist
# مقایسه کن
# --------------
import cv2
from pathlib import Path
from cvtools import cvt
import numpy as np
p = print
# ----------------------------------
folder = Path(r"Week_02/Data/Day_05_Data_Shared")
output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-06\output")
output.mkdir(parents=True , exist_ok= True)
paths = [str(i) for i in folder.glob("*.jpg")]
# --------------------------------------
for i in paths:
    gray= cv2.imread(i,0)
    clahe = cv2.createCLAHE(clipLimit=3,tileGridSize=(8,8))
    clahe_img = clahe.apply(gray)
    # ----------------
    equalized = cv2.equalizeHist(gray)
    # ----------------
    comparision = np.hstack([equalized , clahe_img])
    name = Path(i).stem
    cv2.imwrite(output/f"{name}_equalizeHist_VS_CLAHE_comparision.jpg",comparision)

# در مورد هر سه تصویر، کلِی بهتر از اکوالایزهیست عمل کرده و پس زمینه را خراب نکرده است
