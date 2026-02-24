# Month-01
# Week-03
# Day-07

# 1-  سه تصویر دلخواه انتخاب کن و  برای هر کدام،
# حداقل ۳ نسخه با این تغییرات ( تغییر اندازه، برش، چرخش) بساز و ذخیره کن
import cv2
import matplotlib.pyplot as plt
import numpy as np
p = print
path1 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\cow.jpg"

path2 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\duck.jpg"

path3 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\rooster.jpg"
p("-------------------------------------")
# خواندن و آرجی بی کردن تصاویر
cow_img = cv2.imread(path1)
cow_rgb = cv2.cvtColor(cow_img,cv2.COLOR_BGR2RGB)

duck_img = cv2.imread(path2)
duck_rgb = cv2.cvtColor(duck_img,cv2.COLOR_BGR2RGB)

rooster_img = cv2.imread(path3)
rooster_rgb = cv2.cvtColor(rooster_img,cv2.COLOR_BGR2RGB)
p("-------------------------------------")
# ریسایز تصاویر
resize_cow = cv2.resize(cow_rgb,dsize=None ,fx=0.8, fy = 0.8,interpolation=cv2.INTER_AREA)
resize_duck = cv2.resize(duck_rgb,dsize=None ,fx=0.7, fy = 0.7,interpolation=cv2.INTER_AREA)

resize_rooster = cv2.resize(rooster_rgb,dsize=None ,fx=1.3, fy = 1.3,interpolation=cv2.INTER_CUBIC)
# دو تصویر با مقیاس، کوچک سازی و یکی بزرگ سازی شد
p("-------------------------------------")
# برش تصاویر
cow_crop = cow_rgb[189:647,29:513]
duck_crop = duck_rgb[194:730,38:550]
rooster_crop = rooster_rgb[156:443,167:400]
p("-------------------------------------")
# چرخش تصاویر

cow_horizontal_flip = cv2.flip(cow_rgb,1)
duck_180_flip = cv2.flip(duck_rgb,-1)
rooster_vertical_flip = cv2.flip(rooster_rgb,0)
p("-------------------------------------")
# ذخیره تصاویر با تابع
def save_pictures(img,img_name):
    plt.imshow(img)
    plt.axis("off")
    plt.savefig(img_name,dpi = 300,bbox_inches ="tight")
    plt.close()
save_pictures(resize_cow,"resize_cow.jpg")
save_pictures(resize_duck,"resize_duck.jpg")                
save_pictures(resize_rooster,"resize_rooster.jpg")   
save_pictures(cow_crop,"cow_crop.jpg")   
save_pictures(duck_crop,"duck_crop.jpg")     
save_pictures(rooster_crop,"rooster_crop.jpg")
save_pictures(rooster_vertical_flip,"rooster_vertical_flip.jpg")
save_pictures(cow_horizontal_flip,"cow_horizontal_flip.jpg")
save_pictures(duck_180_flip,"duck_180_flip.jpg")


# 2-بررسی کن که تصاویر آماده برای پروژه شده باشند


# 🎯 مأموریت پایان هفته
# مجموعه‌ای از تصاویر آماده شده داشته باش
# برای هر تصویر تغییرات انجام شده را یادداشت کن
# بررسی کن که آیا کیفیت تصویر حفظ شده و مناسب برای پروژه است

