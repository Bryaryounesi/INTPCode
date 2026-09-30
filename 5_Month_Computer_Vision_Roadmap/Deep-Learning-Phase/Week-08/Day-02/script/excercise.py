# Week-08
# Day-02
# ------------------------------
# تمرین :
# چند آرایه نامپی را به تنسور تبدیل کن سپس دوباره به نامپی برگردان
# ------------
p = print
import numpy as np
import torch
# ساخت آرایه های نامپی
np.random.seed(3)
m1 = np.random.randint(-15, 45, 10)
m2 = np.linspace(-10, 35, 30).reshape(5, 6).round(2)
m3 = np.random.rand(3, 2, 2).round(3)
# --------------
# ساخت تنسور ها از روی آرایه ها
t1 = torch.tensor(m1)
t2 = torch.from_numpy(m2)
t3 = torch.as_tensor(m3)

# نمایش تنسور ها و تبدیل دوباره آنها به آرایه و نمایش آرایه های بازیافتی
tensors = {"t1": t1, "t2": t2, "t3": t3}
for key, value in tensors.items():
    arr = value.numpy()
    p(f"{key}_tensor:")
    p(f"{value}")
    p("----------------------------")
    p(f"{key}_to_numpy:")
    p(arr)
    p("------------------")
