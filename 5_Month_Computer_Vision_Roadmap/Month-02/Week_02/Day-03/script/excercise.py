# Month-02
# Week-02
# Day-03
# ----------------------------
#  تمرین:
# خروجی Dilation را با Erosion مقایسه کن و تفاوت‌ها را یادداشت کن
# ---------------------------
import cv2
from pathlib import Path
import numpy as np
# from cvtools import cvt
from itertools import product
p = print
# -------------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Data\Day_02_Data_Shared"
)
paths = [str(i) for i in folder.glob("*.jpg")]
# ---------------------
for i in paths:
    img = cv2.imread(i)
    if img is None:
        continue
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _ , th = cv2.threshold(gray, 190,255 ,cv2.THRESH_BINARY_INV)
    # -------------------------------------------
    ksizes = [3,5,7]
    shapes = [cv2.MORPH_RECT , cv2.MORPH_CROSS,cv2.MORPH_ELLIPSE]
    iterations = [1,2,3]

    for k, shape,itr in product(ksizes,shapes , iterations):
        kernel = cv2.getStructuringElement(shape , (k,k))
        eroded = cv2.erode(th, kernel, itr)
        dilated = cv2.dilate(th , kernel , itr)
        # -----------------------
        if shape == cv2.MORPH_RECT:
            shape_name = "RECT"
        elif shape == cv2.MORPH_CROSS:
            shape_name = "CROSS"
        elif shape == cv2.MORPH_ELLIPSE:
            shape_name = "ELLIPSE"
            # ------------------------------
        name = Path(i).stem
        comparisons = np.hstack([eroded,dilated])
        cv2.imshow(f"{name}_{(k,k)}_{shape_name}_iteration{(itr)}_erosion_VS_dilated",comparisons)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
# ------------------------------------------
# انجام نمایش و مقایسه با مت پلات لیب خالص
'''
        import matplotlib.pyplot as plt
        fig,axes = plt.subplots(1,2,constrained_layout=True)
        axes[0].imshow(eroded, cmap = "gray")
        axes[0].set_title(f"{name}_{(k,k)}_{shape_name}_iter{itr}_erosion")
        axes[0].axis("off")
        # --------------------------
        axes[1].imshow(dilated,cmap = "gray")
        axes[1].set_title(f"{name}_{(k,k)}_{shape_name}_iter{itr}_dilation")
        axes[1].axis("off")
        plt.show()
    '''
# ------------------------------------------
# با کرنل ها، ایتریشن ها و کی سایز های مختلف اروشن و دیلیشن روی تصاویر روی قبل اعمال و  با هم مقایسه شدند.

# در دیلیشن تصاویر باینری با پس زمینه سیاه ،قلمرو شی درون تصویر وسیع تر میشود و سیاهی درون شی کمتر و کمتر میشوند. حفره های سیاه پر میشوند.
