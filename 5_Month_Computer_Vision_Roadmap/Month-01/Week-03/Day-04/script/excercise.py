# Month-01
# Week-03
# Day-04
# 1-  یک بخش مشخص از تصویر (مثلاً یک چهره یا شیء) برش بده

import cv2
p=print
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-04\Data\jimmy_lenister.jpg"
img = cv2.imread(path)
cv2.imshow("my image",img)
cv2.waitKey(0)

roi = img[42:366,301:534]

# 2- آن بخش را نمایش بده و ذخیره کن
cv2.imshow("my image",roi)
cv2.waitKey(0)

# cv2.imwrite("face_crop.jpg",roi)
cv2.destroyAllWindows()
