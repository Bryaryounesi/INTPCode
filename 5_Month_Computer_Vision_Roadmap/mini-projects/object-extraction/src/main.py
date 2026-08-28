p = print
import cv2
import numpy as np
from pathlib import Path
# from cvtools import cvt
# --------------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\object-extraction\data"
)
outputs = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\object-extraction\outputs"
)
outputs.mkdir(parents=True,exist_ok=True)
paths = [str(i) for i in folder.glob("*.jpg")]
# ----------------------------
for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,th = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)
    contours,_ = cv2.findContours(th,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # ------------------------------
    # Bounding - box
    bigest = max(contours,key = cv2.contourArea)
    x, y, w, h = cv2.boundingRect(bigest)
    boxes = img.copy()
    cv2.rectangle(boxes,(x,y),(x+w,y+h),(0,255,0),10)
    # -----------------------------
    # crop
    roi = img[y:y+h, x:x+w]
    # -------------------------
    # mask
    mask = np.zeros(gray.shape , dtype= np.uint8)
    cv2.drawContours(mask,[bigest],-1,255,-1)
    masked = cv2.bitwise_and(img , img ,mask = mask)
    # ---------------------------------------
    name = Path(i).stem
    processing_senarios = {"roi":roi, "mask": masked, "bounding_box":boxes}
    for key, values in processing_senarios.items():
        cv2.imwrite(outputs/f"{name}_{key}.jpg",values)