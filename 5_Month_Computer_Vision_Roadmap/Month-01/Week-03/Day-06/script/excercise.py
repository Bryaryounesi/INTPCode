# Month-01
# Week-03
# Day-06

# 1-تصویر را افقی و عمودی وارونه کن
import cv2
import matplotlib.pyplot as plt
p = print
path = r'e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-03\Day-06\Data\the fox.jpg'
img = cv2.imread(path)
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(rgb_img)
plt.title("orginal_rgb picture")
plt.show()
p("-------------------------------------")
horizontal_fliped = cv2.flip(rgb_img,1)
plt.imshow(horizontal_fliped)
plt.title("horizontal_fliped picture")
plt.axis("off")
# axis("off") یعنی حذف اعداد و خطوط کنار تصویر
# plt.savefig("horizontal_fliped.jpg",dpi = 300)
plt.show()
p("-------------------------------------")
vertiacal_fliped = cv2.flip(rgb_img,0)
plt.imshow(vertiacal_fliped)
plt.title("vertical_fliped picture")
plt.axis("off")
# plt.savefig("vertical_fliped.jpg",dpi = 300 ,bbox_inches ="tight",pad_inches = 0 )

# bbox_inches="tight" یعنی بریدن فضای اضافی اطراف تصویر
# pad_inches=0 یعنی حذف فاصله سفید دور تصویر
plt.show()

# 2-نتیجه را ذخیره و با تصویر اصلی مقایسه کن
# ذخیره هر سه تصویر در یک فیگور با سابپلات برای مقایسه
fig, axes = plt.subplots(1,3, figsize=None,constrained_layout=True)
axes[0].imshow(rgb_img)
axes[0].set_title("orginal")
axes[0].axis("off")
p("---------------------------------")
axes[1].imshow(horizontal_fliped)
axes[1].set_title("horizontal_fliped")
axes[1].axis("off")
p("---------------------------------")
axes[2].imshow(vertiacal_fliped)
axes[2].set_title("vertiacal_fliped")
axes[2].axis("off")
# fig.savefig(fname="pictures comparision.png",dpi=300,bbox_inches ="tight")

# نکته مهم : این تمرین با متپلات لیب انجام شده و
# بیشتر بر روی نمایش دادن تصاویر تمرکز کرده است.