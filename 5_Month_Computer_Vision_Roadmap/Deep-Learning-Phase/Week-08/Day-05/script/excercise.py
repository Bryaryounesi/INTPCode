# Week-08
# Day-05

# تمرین: یک مدل آماده را بارگذاری کن و روی یک تصویر آزمایشی اجرا کن. فقط نتیجه را نمایش بده (وارد جزئیات مدل نشو)


import numpy as np
import torch
import torchvision
from torchvision import transforms, models
from pathlib import Path
import matplotlib.pyplot as plt
import cv2
from PIL import Image
p = print
# ------------------model info-----------
weights = models.ResNet18_Weights.IMAGENET1K_V1
labels = weights.meta["categories"]
model = models.resnet18(weights= weights)
transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)
# --------------preprocess---------------
def preprocessing(pil_img):
    tensor = transform(pil_img)
    input_batch = tensor.unsqueeze(0)
    return input_batch
# -----------------model_impacting------------------
def model_inpacting(input_batch,model,k = 5):
    model.eval()
    with torch.no_grad():
        outputs = model(input_batch)
        probabilites = torch.softmax(outputs, dim = 1)
        top_p , top_i = probabilites.topk(k , dim =1)
        return top_p[0] , top_i[0]
# --------------I/O----------------
def read_img(path):
    img = cv2.imread(path)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    return pil_img
# ----------------------main-----------------------
folder = Path(
    r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\Week-08\Day-05\Data"
)

paths = [str(i) for i in folder.glob("*.jpg")]
for i in paths:
    img = read_img(i)
    input_batch = preprocessing(img)
    top_p , top_i = model_inpacting(input_batch,model , k= 3)
    name = Path(i).stem
    # --------------------
    # پرینت محتمل ترین ها برای هر تصویر
    for j in range(len(top_p)):
        p(f"{j+1}_{labels[top_i[j].item()]:<40}{top_p[j].item():.2%}")
    p(f"image name: {name}")
    p("------------------------")
    # نمایش تصویر با محتمل ترین کلاس برای عنوان
    prob = top_p[0].item()
    idx = top_i[0].item()
    plt.imshow(img)
    plt.title(f"{labels[idx]:<40}{prob:.2%}")
    plt.axis("off")
    plt.show()
