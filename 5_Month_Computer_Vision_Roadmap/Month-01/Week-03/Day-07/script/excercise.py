# Month-01
# Week-03
# Day-07

# 1-  سه تصویر دلخواه انتخاب کن و  برای هر کدام،
# حداقل ۳ نسخه با این تغییرات ( تغییر اندازه، برش، چرخش) بساز و ذخیره کن

path1 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\input\cow.jpg"

path2 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\input\duck.jpg"

path3 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\Data\input\rooster.jpg"

import cv2
p = print

def Change_pictures(pathes,resize_name,flip_name,rotate_name,crop_name,crop_area):
    img = cv2.imread(pathes)    #reading pictures
    #-------------------------------------
    resized = cv2.resize(img,None, fx=0.6,fy = 0.6,interpolation= cv2.INTER_AREA)    #resizing pictures
    #-----------------------------------------
    fliped = cv2.flip(img,1)   #fliping pictures
    #-----------------------------------------
    h,w = img.shape[:2]       #roatating pictures
    center = (w//2,h//2)
    M = cv2.getRotationMatrix2D(center,15,0.8)
    rotated = cv2.warpAffine(img,M,(w,h))
    #-----------------------------------------
    w1,h1,w2,h2 = crop_area         #crapping pictures
    croped = img[h1:h2,w1:w2]
    #-----------------------------------------
    cv2.imwrite(resize_name,resized)    #writing pictures
    cv2.imwrite(flip_name,fliped)
    cv2.imwrite(rotate_name,rotated)
    cv2.imwrite(crop_name,croped)   
    #-----------------------------------------
# ساخت یک تاپل برای حلقه زدن روی آن و 
# قراردهی تابع فراخوانی درون این حلقه برای
# ورودی گرفتن اتوماتیک از عناصر تاپل  

tuples = [(path1,"cow_resized.jpg","cow_fliped.jpg","cow_rotated.jpg","cow_croped.jpg",(29,189 ,513 ,647)),(path2,"duck_resized.jpg","duck_fliped.jpg","duck_rotated.jpg","duck_croped.jpg",(39,194 ,550 ,730 )),(path3,"rooster_resized.jpg","rooster_fliped.jpg","rooster_rotated.jpg","rooster_croped.jpg",(167,164 ,400 ,443))]

for i,j,f,g,k,m in tuples:
    Change_pictures(i,j,f,g,k,m)
# 2-بررسی کن که تصاویر آماده برای پروژه شده باشند
'''
تصاویر برای انجام پروژه مناسب نیستند زیرا هدف اولیه این تمرین 
صرفا اعمال تغییرات دلخواه روی تصاویر بوده و نه تغییرات مناسب برای پروژه 
مثلا تصاویر مربعی نیستند و ابعاد متفاوتی دارند که برای پروژه ها معمولا باید همگی ابعاد و شکل هندسی یکسانی داشته باشند

در تمرین پایانی هفته این مشکل برطرف خواهد شد
'''
p("-------------------------------------------------------")
