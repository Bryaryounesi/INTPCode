import cv2
from cvtools import cvt
import numpy as np
from pathlib import Path

p = print
# ----------------config-----------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\Simple_Object_Counting\data"
)
outputs = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\Simple_Object_Counting\output"
)
outputs.mkdir(parents=True, exist_ok=True)
paths = [str(i) for i in folder.glob("*.jpg")]
min_areas = 50000
kernel_light = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
kernel_agressive = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))


# ----------------preprocess------------------
def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if np.std(gray) < 50:
        clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8, 8))
        clahe_img = clahe.apply(gray)
    else:
        clahe_img = gray
    thresh_adapt = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 39, -1
    )
    opened = cv2.morphologyEx(thresh_adapt, cv2.MORPH_OPEN, kernel_light)
    dilated = cv2.dilate(opened, kernel_agressive, 1)
    return dilated


# -------------------analyze------------------------
def find_objects(dilated):
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    biggest_closed_contours = [
        c
        for c in contours
        if len(c) >= 3 and cv2.contourArea(c) > min_areas and cv2.arcLength(c, True) > 0
    ]
    return biggest_closed_contours

# --------------Virsualize-----------------
def draw_boxes(img, biggest_closed_contours):
    boxes = img.copy()
    for contour in biggest_closed_contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(boxes, (x, y), (x + w, y + h), (0, 0, 0), 5)
    cv2.putText(
        boxes,
        f"detected_objects: {len(biggest_closed_contours)}",
        (10, 50),
        cv2.FONT_HERSHEY_COMPLEX,
        2,
        (0, 0, 0),
        2,
    )
    return boxes

# ---------------I/O------------------------
def read_img(path):
    img = cv2.imread(path)
    return img

def save_img(path, img):
    cv2.imwrite(str(path), img)
# --------------main----------------------------
for i in paths:
    img = read_img(i)
    if img is None:
        continue
    dilated = preprocess(img)
    detected_object = find_objects(dilated)
    boxes = draw_boxes(img, detected_object)
    name = Path(i).stem
    title = f"{name}_object_detected"
    save_img(outputs / f"{title}.jpg", boxes)
