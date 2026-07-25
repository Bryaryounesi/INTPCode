# Month-01
# Week-04
# Day-06

# 📝 تمرین:
# یک تصویر را بدون فیلتر و سپس با
# Gaussian
# بلور کن، سپس با
# Canny
# اجرا کن و نتایج را مقایسه کن
# -------------------------------
import cv2
# from cvtools import cvt
from pathlib import Path
import numpy as np

# از همان تصاویر روز قبل استفاده می کنیم پس دیتای دیروز رو تبدیل کردیم به دیتای هفتگی

folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Data"
)
paths = [str(i) for i in folder.glob("*.jpg")]
# ---------------------------
for i in paths:
    img = cv2.imread(i, 0)
    if img is None:
        continue
    if np.std(img) > 50:
        blurred = cv2.GaussianBlur(img, (5, 5), 0)
        # ------------------------------------------
        thresholds = [(50, 150), (100, 200), (150, 300)]
        for minval, maxval in thresholds:
            edge_with_blur = cv2.Canny(blurred, minval, maxval)
            edge_without_blur = cv2.Canny(img, minval, maxval)
            # -------------------------------------
            output = Path(
                r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-04\Day-06\Output"
            )
            output.mkdir(parents=True, exist_ok=True)
            # -------------------------------------
            name = Path(i).stem
            # اگر نیم رو در نام ایمرایت درج نکنیم عملیات تنها روی یک تصویر انجام میشود
            cv2.imwrite(
                output / f"{name}_{minval}_{maxval}_edge(blurred).jpg", edge_with_blur
            )
            cv2.imwrite(output /  f"{name}_{minval}_{maxval}_edge(unblurred).jpg", edge_without_blur)
# بعد از بررسی مشخص شد تصاویر بلورشده و تشخیص لبه شده با آستانه
# 50 , 150
# بهترین جزئیات و لبه ها رو دارند
# -------------
# تصاویر بلور نشده که تشخیص لبه شده اینطور به نظر میرسند
# که شن ریزه یا براده چوب روی آنها ریخته باشیم
