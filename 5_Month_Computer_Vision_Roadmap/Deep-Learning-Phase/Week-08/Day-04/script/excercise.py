# Week-08
# Day-04
# ---------------
# 📝 تمرین:
# دیتاست روز قبل را با دیتالودر، بارگذاری کن و اندازه هر بچ را چاپ کن

import numpy as np
import torch
import torchvision
from torchvision import transforms, datasets
from pathlib import Path
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader
p = print
# -----------------------
root = r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\datasets\MNIST"
train_dataset = torchvision.datasets.MNIST(root = root, train=True,download=False,transform=transforms.ToTensor())

train_loader = DataLoader(
    train_dataset,batch_size= 64 , shuffle=True,generator=torch.Generator().manual_seed(2))
batch_sizes = []
for i , (img,label) in enumerate(train_loader):
    batch_sizes.append(img.shape[0])
p(batch_sizes)
