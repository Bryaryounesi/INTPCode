# Month-01
# Week-03
# Day-03

# 1-تصویر را به ابعاد جدید تغییر بده (مثلاً نصف اندازه اصلی)

p = print
import cv2
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-03\Data\lamborghini.jpg"
img = cv2.imread(path)
# -------------------------------------
h,w = img.shape[:2]
new_h = int(h/2)
# ارتفاع را نصف کردیم و عدد ارتفاع را اینتیجر ساختیم تا
# تابع ریسایز ارور ندهد
new_w = int((w*new_h)/h)
# تناسب گیری برای ایجاد ابعاد جدید تصویر برای مرحله ریسایز
img_resized = cv2.resize(img,(new_w,new_h),interpolation = cv2.INTER_AREA)
# ریسایز تصویر با کمترین افت کیفیت

# 2- تصویر جدید را نمایش بده
cv2.imshow("my image resized",img_resized)
cv2.waitKey(0)

cv2.imwrite("lambo_resized.jpg",img_resized)
# ذخیره تصویر ریسایز شده
cv2.destroyAllWindows()
