# Month-01
# Week-03
# Day-05

# 1-تصویر را با زاویه ۳۰ درجه بچرخان

import cv2
import matplotlib.pyplot as plt
import numpy as np
p= print
path = r'e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-05\Data\40.jpg'

# ابتدا نمایش تصویر اولیه با متپلاتلیب
img = cv2.imread(path)
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.show()
p("----------------------------------------")
# ساخت ماتریس چرخش
angle = 30
h,w = img.shape[:2]
center = (w//2 , h//2)
M = cv2.getRotationMatrix2D(center,angle,1)
p("----------------------------------------")
# تغییر ابعاد تصویر برای جلوگیری از بریدگی گوشه های عکس بعد از چرخش
theta = np.radians(angle)
new_w = int(h*np.sin(theta) + w*np.cos(theta))
new_h = int(h*np.cos(theta) + w*np.sin(theta))

# اصلاح مرکز چرخش تصویر
M[0,2] += (new_w - w) //2
M[1,2 ] += (new_h - h) //2

p("----------------------------------------")
# اعمال چرخش تصویر
rotated = cv2.warpAffine(img,M,(new_w,new_h))
scale = 0.4

# کوچک کردن پنجره تصویر برای نمایش درست تصویر چرخیده شده
cv2.namedWindow("my image",cv2.WINDOW_NORMAL)
cv2.resizeWindow("my image",int(scale*new_w),int(scale*new_h))
cv2.imshow("my image",rotated)
cv2.waitKey(0)

# 2-نتیجه را ذخیره و بررسی کن
cv2.imwrite("Rotated img.jpg",rotated)
