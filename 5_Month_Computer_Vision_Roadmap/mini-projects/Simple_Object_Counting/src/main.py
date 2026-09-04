import cv2
import numpy as np
from pathlib import Path
from config import folder , outputs , min_areas , kernel_light , kernel_agressive

p = print
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
def find_contours(dilated):
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    biggest_closed_contours = [
        c
        for c in contours
        if len(c) >= 3 and cv2.contourArea(c) > min_areas and cv2.arcLength(c, True) > 0
    ]
    return biggest_closed_contours

# --------------Virsualize-----------------
def draw_and_count_contours(img, biggest_closed_contours):
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
def object_detect(img):
    dilated = preprocess(img)
    best_contours = find_contours(dilated)
    result = draw_and_count_contours(img,best_contours)
    return result

paths = [str(i) for i in folder.glob("*.jpg")]
for i in paths:
    img = read_img(i)
    if img is None:
        continue
    dilated = preprocess(img)
    best_contours = find_contours(dilated)
    result = draw_and_count_contours(img,best_contours)
    name = Path(i).stem
    title = f"{name}_object_detected"
    save_img(outputs / f"{title}.jpg", result)