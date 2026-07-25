# Month-01
# Week-04
# Day-01

# 📝 تمرین
# 1) یک تصویر بخوان، با فیلتر گاوسین در سه حالت کرنل
# (کرنل کوچک، متوسط، بزرگ)
import cv2
from cvtools import cvt
p = print
path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-01\Data\The man.png"
img = cv2.imread(path)
# -----------------------
small_blur = cv2.GaussianBlur(img,(3,3),sigmaX=0)
medium_blur = cv2.GaussianBlur(img,(5,5),sigmaX=0)
extra_blur = cv2.GaussianBlur(img,(9,9),sigmaX=0)

# 2) تفاوت‌ها را بررسی کن
cv2.imshow("small blur",small_blur)
cv2.imshow("medium blur", medium_blur)
cv2.imshow("extra blur", extra_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
# -------------------------------
from pathlib import Path
output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-01\Output"
)
output.mkdir(parents=True, exist_ok=True)
# ---------------------------------
cv2.imwrite(output/"man_small_blur.jpg",small_blur)
cv2.imwrite(output/"man_medium_blur.jpg", medium_blur)
cv2.imwrite(output/"man_extra_blur.jpg", extra_blur)
