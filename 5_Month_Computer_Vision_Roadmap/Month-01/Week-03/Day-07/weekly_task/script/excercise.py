# Month-01
# Week-03
# weekly task

# 🎯 مأموریت پایان هفته

# 1- مجموعه‌ای از تصاویر آماده شده داشته باش

import cv2
p = print
path1 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\weekly_task\Data\input\flower.jpg"

path2 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\weekly_task\Data\input\horses.jpg"

path3 = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-07\weekly_task\Data\input\phoenix.jpg"

# برای هر تصویر تغییرات انجام شده را یادداشت کن
def chenge_pictures(pathes,resized_name,rotated_name,fliped_name):
    img = cv2.imread(pathes)
    # --------------------------------------------
    resized = cv2.resize(img,(256,256), interpolation = cv2.INTER_AREA)
    # --------------------------------------------
    h,w = img.shape[:2]
    center= (w//2 , h//2)
    M = cv2.getRotationMatrix2D(center,90,1)
    rotated = cv2.warpAffine(img,M,(256,256))
    # --------------------------------------------
    fliped = cv2.flip(resized,1)
    # --------------------------------------------
    cv2.imwrite(resized_name,resized)
    cv2.imwrite(rotated_name,rotated)
    cv2.imwrite(fliped_name,fliped)

params = [(path1,"flower_resized.jpg","flower_rotated.jpg","flower_fliped.jpg"),(path2,"horses_resized.jpg", "horses_rotated.jpg", "horses_fliped.jpg"),(path3,"phoenix_resized.jpg", "phoenix_rotated.jpg", "phoenix_fliped.jpg")] 
for i,j,k,m in params:
    chenge_pictures(i,j,k,m)
    
    
# بررسی کن که آیا کیفیت تصویر حفظ شده و مناسب برای پروژه است