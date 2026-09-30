# Week-08
# Day-03
# ------------------------------
# 📝 تمرین:
# یک دیتاست آماده مانند
# MNIST یا CIFAR-10
# را دانلود و بارگذاری کن. چند نمونه تصویر و برچسب آن‌ها را نمایش بده
# ----------------
import torchvision
from torchvision import transforms
from pathlib import Path
import matplotlib.pyplot as plt
import cv2
import numpy as np
import random
p = print
# ----------------
root = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\datasets\MNIST")
# هر پوشه ای رو به روت بدهیم یک پوشه
# mnist > raw
# در آن ساخته میشود و سپس فایل های داتاست در پوشه داو قرار میگرند

outputs = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\Week-08\Day-03\script\output"
)
outputs.mkdir(parents=True, exist_ok=True)
# ------------------------
transform = transforms.ToTensor()  # PIL -> tensor [0,1]

train_dataset = torchvision.datasets.MNIST(
    root=root,
    train=True,
    transform=transform,
    download=True,  # اگه نبود دانلود کن
)

random.seed(2)
choices = random.choices(range(1,len(train_dataset)),k = 10)
# ساخت لیستی از 10 سمپل تصادفی
for i in choices:
    # اگربخواهیم همه تصاویر داتاست رو نمایش دهیم حلقه رو روی رنج سایز داتاست میزنیم
    # به دلیل مدیریت حافظه نمیتوان مستقیم و مثل لیست ها  روی خود دیتاست حلقه زد
    # for i in range(len(train_dataset)):
    img , label = train_dataset[i]
    # حذف ابعاد برابر با عدد یک و تبدیل تنسور به آرایه نامپی
    img_np = img.squeeze().numpy()
    # --------------------
    # نمایش و ذخیره تصاویر با مت پلات لیب
    plt.imshow(img_np, cmap="gray")
    # plt.title(f"sample_{i} label_{label}")
    plt.axis("off")
    plt.savefig(
        outputs / f"sample_{i} label_{label}.jpg",
        dpi=300,
        bbox_inches="tight",
        pad_inches=0
    )
    # plt.show()
    # --------------------
    # نمایش و ذخیره با اپن سیوی
    '''
    جلوگیری از سیاه شدن تصاویر حاصل از اپن سیوی
    img_np = (img_np * 255).astype("uint8")

    img_np_resized = cv2.resize(img_np,(1000,800),cv2.INTER_CUBIC)
    cv2.imwrite(outputs / f"sample_{i} label_{label}.png",img_np_resized)
    cv2.imshow(f"label:{label}",img_np)
    cv2.waitKey()
    cv2.destroyAllWindows()
    '''
    # ----------------------------
    # نتیجه حاصل از مت پلات لیب بهتر و کم دردسر تر بود ولی حاشیه سفید تصاویر در متپلات لیب ممکن است مشکل ایجاد کند
    # پس پارامتر
    # pad_inches=0
    # رو هم درج کردیم در تابع
    # plt.savefig
