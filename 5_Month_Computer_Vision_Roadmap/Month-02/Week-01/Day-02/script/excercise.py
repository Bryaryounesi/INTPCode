# Month-02
# Week-01
# Day-02
# ---------------
# تمرین :
# یک تصویر را با سیفت پردازش کن و نقاط کلیدی آن را نمایش بده
import cv2
from cvtools import cvt
p = print
path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week-01\Day-02\Data\Tee glass.jpg"

img = cv2.imread(path,0)
sift = cv2.SIFT_create()
keypoints,descripter = sift.detectAndCompute(img,None)
sift_result = cv2.drawKeypoints(img,keypoints,None)
# cvt.imshow("sift result", sift_result)

cv2.imshow("sift result",sift_result)
cv2.waitKey(0)
cv2.destroyAllWindows()
