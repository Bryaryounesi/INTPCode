# Month-01
# Week-03
# Day-02
# 1-تصویر خوانده شده را ذخیره کن

import cv2
p = print
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-02\Data\simorgh.jpg"
img = cv2.imread(path)
# تصویر خوانده شد

img_resized = cv2.resize(img,(800,600),interpolation=cv2.INTER_AREA)
# کوچک سازی تصویر 

cv2.imshow("my image",img_resized)
cv2.waitKey(0)
# نمایش تصویر ریسایز شده

# cv2.imwrite("simorgh_resized.jpg",img_resized)
# تصویر جدید ذخیره شد

# 2-نسخه خاکستری (Grayscale) و RGB آن را بساز و ذخیره کن

img_grey = cv2.cvtColor(img_resized,cv2.COLOR_BGR2GRAY)
cv2.imshow("my image",img_grey)
cv2.waitKey(0)
# cv2.imwrite("simorgh_resized_RGB.jpg",img_grey)
# نسخه خاکستری ساخته، نمایش داده و در نهایت ذخیره شد

img_rgb = cv2.cvtColor(img_resized,cv2.COLOR_BGR2RGB)
cv2.imshow("my image",img_rgb)
cv2.waitKey(0)

'''
نسخه آرجی بی ساخته و نمایش داده شد ولی ذخیره نکردیم
چون اغلب، تصاویر اینگونه صرفا برای نمایش اند و 
اگر ذخیره شوند باید دوباره به جی بی آر تبدیل شوند 
 و بعد ذخیره شوند وگرنه ترکیب رنگ آنها به صورت غلط در می آید
'''
cv2.destroyAllWindows()
