# Month-01
# Week-04
# Day-04
# ----------------------------
# تمرین:
#  یک تصویر با نور متفاوت انتخاب کن
#  بر روی آن threshold معمولی و adaptive رو اعمال و با هم مقایسه کن
# ----------------------------------
import cv2
from pathlib import Path
# from cvtools import cvt
p = print

path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-04\Data\panther.jpg"
img = cv2.imread(path,0)  #خواندن تصویر به صورت خاکستری

_,simple_treshold = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
adaptive_threshold = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY, 21, 3)
# برای ساخت تصویری نرم تر بلاک سایز رو برابر 21 گرفتیم
# --------------------------------------------
output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-04\Output"
)
output.mkdir(parents=True,exist_ok=True)
# -------------------------------------------
cv2.imwrite(output/"simple_threshold_panther.jpg",simple_treshold)
cv2.imwrite(output/"adaptive_threshold_panther.jpg",adaptive_threshold)

