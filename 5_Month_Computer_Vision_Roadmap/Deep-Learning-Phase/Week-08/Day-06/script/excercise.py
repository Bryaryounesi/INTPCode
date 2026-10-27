# Week-08
# Day-06

import torch
import cv2
import torch
import torchvision
from torchvision import models

p = print
# ---------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  #ساخت شی دیوایس
p(device)
path = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\Week-08\Day-06\Data"
img = cv2.imread(path)                      # خواندن یک تصویر (ساخت یک آرایه نامپی)

p(type(img))
tensor = torch.from_numpy(img)          #تبدیل آرایه به تنسور
tensor = tensor.to(device)
# انتقال تنسور روی دیوایس(برای خوانا کردن کد در سیستم های دارای جی پی یو)
p(type(tensor))

model = models.resnet18(weights="DEFAULT")
model.to(device)                                # انتقال مدل روی دیوایس
