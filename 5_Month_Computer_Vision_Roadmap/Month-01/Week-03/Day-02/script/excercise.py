# Month-01
# Week-03
# Day-02

# 1-تصویر خوانده شده را ذخیره کن

import cv2
from cvtools import cvt
p = print
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-02\Data\44.jpg"
# ------------------------------
img = cv2.imread(path)
cvt.imshow("win",img)
# تصویر خوانده شد

cv2.imwrite("new_44.jpg",img)
# تصویر جدید ذخیره شد

# 2-نسخه خاکستری (Grayscale) و RGB آن را بساز و ذخیره کن

grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# تبدیل تصویر در پروژه های آموزشی،
# بهینه تر از چند بار خواندن با فلگ متفاوت


cv2.imwrite("grey_44.jpg",grey)
cv2.imwrite("rgb_44.jpg",img)
'''
تصویر اورجینال اولیه به صورت جی بی آر است و تنها کافیست آن را ذخیره کنیم تا تصویر خروجی تبدیل به آر جی بی شود. نیازی به تبدیل نیست چون در هنگام ذخیره، این تبدیل به صورت اتوماتیک در اپی سی وی رخ میدهد
اگر تبدیل کنیم دوباره تبدیل رخ می دهد و تصویر به حالت بی جی آر ذخیره میشود
'''
