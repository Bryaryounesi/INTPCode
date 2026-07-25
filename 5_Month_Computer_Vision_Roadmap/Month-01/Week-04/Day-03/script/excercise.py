# Month-01
# Week-04
# Day-03
# ----------------------------
# تمرین:
# یک تصویر خاکستری بگیر
# چند مقدار ترشهولد مختلف را روی آن تست کن
# و خروجی ها را مقایسه کن

import cv2
from pathlib import Path
from cvtools import cvt
p = print
path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-03\Data\huawei.jpg"
tresh_list = [50,127,200]
for i in tresh_list:
    img = cv2.imread(path)
    grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #تصویر را تبدیل به خاکستری کردیم
    ret, th= cv2.threshold(grey , thresh = i , maxval = 255 , type=cv2.THRESH_BINARY)
    # -------------------------------
    output = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-03\Output"
    )
    output.mkdir(parents=True,exist_ok=True)
    # -------------------------
    cv2.imwrite(output/f"huwawei_thresh_{i}.jpg",th)
