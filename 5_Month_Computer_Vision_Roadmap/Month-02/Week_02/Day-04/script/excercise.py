# Month-02
# Week-02
# Day-04
# ----------------------------
#  تمرین:
# یک تصویر نویزی انتخاب کن ، اپنینگ و سپس کلوزینگ رو اجرا و خروجی ها رو مقایسه کن

# --------------------------
import cv2
import numpy as np
# from cvtools import cvt
from pathlib import Path

path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-04\Data\40.jpg"

output = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-02\Week_02\Day-04\output"
)
output.mkdir(parents =True, exist_ok=True)
# ------------------------------------
img = cv2.imread(path,0)
thresh_adapt = cv2.adaptiveThreshold(img,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 37, 7)
# چون پس زمینه سفید نبود و سایه داشت ترشهولد معمولی چندان موفق نبود

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
opened = cv2.morphologyEx(thresh_adapt,cv2.MORPH_OPEN,kernel)
closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, kernel)
# comparision = np.hstack([thresh_adapt,opened,closed])
# --------------------------
import matplotlib.pyplot as plt
fig , axes = plt.subplots(1,3,constrained_layout=True)
axes[0].imshow(thresh_adapt,cmap = "gray")
axes[0].set_title("thresh_adapt")
axes[0].axis("off")

axes[1].imshow(opened, cmap="gray")
axes[1].set_title("opened")
axes[1].axis("off")

axes[2].imshow(closed, cmap="gray")
axes[2].set_title("closed")
axes[2].axis("off")

# fig.savefig(output/"comparision_th_VS_opening_AND_closing.png", dpi=300, bbox_inches="tight")
plt.show()

# برای نمایش و ذخیره از مت پلات لیب استفاده شد چون کنترل پنجره برای مقایسه سه تصویر با ایمشو در اپن سیوی درست کار نمیکرد

# ------------------
# کلوز روی اپن با یک کرنل واحد برای هر دو، چندان موفق به نظر نمیرسد چون اگر چه اپن در حذف نویز موفق است ولی چهارچوب شی را نیز خراب میکند و کلوز با سعی در ترمیم این وضعیت، نویز را به شکلی دیگر برمیگرداند
