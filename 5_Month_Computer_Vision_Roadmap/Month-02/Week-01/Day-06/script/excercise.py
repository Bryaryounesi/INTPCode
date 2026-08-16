# Month-02
# Week-01
# Day-06

# --------------------------------
# تمرین :
# یک شی مشخص را از تصویر جدا کن و فقط همان شی را ذخیره کن
# ----------------------------------------
p = print
from cvtools import cvt
import cv2
from pathlib import Path
import numpy as np
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week-01\Day-06\Data"
)
paths = [str(i) for i in folder.glob("*.jpg")]
output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week-01\Day-06\output"
)

# -----------------------------------
for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(th , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    # copied = img.copy()
    # cv2.drawContours(copied,contours,-1,(0,255,0),15)
    # کانتور ساخته شد حالا باید به سه روش شی را از تصویر جدا کنیم
    # ------------------------------------
    # 1
    bigest = max(contours,key = cv2.contourArea)
    x, y ,w , h = cv2.boundingRect(bigest)
    boxes = img.copy()
    cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 255, 0), 15)
    # --------------------------
    # 2
    roi = img[y : y + h, x : x + w]
    # ----------------------------------------
    # 3
    mask = np.zeros(gray.shape,dtype = np.uint8)
    cv2.drawContours(mask,[bigest],-1,255,-1)
    masked = cv2.bitwise_and(img,img,mask=mask)
    # -------------------------------
    name = Path(i).stem
    processing_scenarios = {"roi":roi,"masked":masked,"boxes":boxes}
    for key,values in processing_scenarios.items():
        cv2.imwrite(output/f"{name}_{key}.jpg",values)
