# Week-08
# Day-01
# --------------------------
#  📝 تمرین:
#  پایتورچ را نصب کن. یک تنزور یک‌بعدی، دوبعدی و سه‌بعدی ایجاد کن و اندازه هرکدام را چاپ کن

p = print
import torch
import numpy as np


np.random.seed(2)
m1 = np.random.randint(-15,45,5)
m2 = np.random.randint(-15, 45, (4,5))
m3 = np.random.randint(-15, 45, (4,4,5))
# -----------------------------
t1 = torch.tensor(m1,dtype = float)
t2 = torch.tensor(m2, dtype=float)
t3 = torch.tensor(m3, dtype=float)
# -----------------------------
p("D1 Tensor :", t1)
p("D1 Tensor size :" , t1.size())
p("------------------------------")
p("D2 Tensor :", t2)
p("D2 Tensor size :", t2.size())
p("------------------------------")
p("D3 Tensor :", t3)
p("D3 Tensor size :", t3.size())

