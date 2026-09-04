import cv2
import numpy as np
from pathlib import Path

folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\Simple_Object_Counting\data"
)

outputs = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\mini-projects\Simple_Object_Counting\output"
)

outputs.mkdir(parents=True, exist_ok=True)

min_areas = 50000
kernel_light = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
kernel_agressive = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
