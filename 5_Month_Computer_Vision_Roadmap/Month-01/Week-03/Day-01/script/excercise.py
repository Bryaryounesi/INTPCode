# Month-01
# Week-03
# Day-01

# 1-یک تصویر دلخواه دانلود کن
path= r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-01\Data\deers.jpg"
# لینک بالا، مسیر تصویر منتخب ماست

# 2-آن را با OpenCV بخوان
import cv2
p = print
img = cv2.imread(path,cv2.IMREAD_UNCHANGED)

# 3-نمایش بده و بررسی کن که تصویر درست لود شده باشد
# شرط بررسی درست لود شدن تصویر:
if img is None :
    p("incorrect Loaded")
else:
    p("correcr Loaded")
# تصویر درست لود شده بود
p("------------------------------")
# نمایش تصویر:
cv2.imshow("win" ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()


