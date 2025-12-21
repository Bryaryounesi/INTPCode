# month-02
# week-03
# Day-03

# 1-یک array 1000تایی با توزیع نرمال بساز و میانگین/انحراف معیار آن را محاسبه کن

import numpy as np
np.random.seed(1)
p=print

a_normal=np.random.normal(50,5,1000).astype(int)
# آرایه رو ساختیم
# حالا وقتی میگه میانگین و انحراف معیار رو محاسبه کن منظور مطابقت 
# این دو با مقادیر استفاده شده برای ساخت توزیع است
p("normal array std:",np.std(a_normal).round())
p("normal array mean:",np.mean(a_normal))
# تقریبا میانگین و انحراف معیار به آنچه 
# برای ساخت توزیع نرمال استفاده شده نزدیک و برابر هستند


# 2- یک array 1000تایی یکنواخت بساز و مقایسه کن
a_uniform=np.random.uniform(-20,50,1000).astype(int)
p("uniform array std:",np.std(a_uniform).round())
p("uniform array mean:",np.mean(a_uniform))

# 3-تفاوت پراکندگی داده‌ها را بررسی کن

import matplotlib.pyplot as plt
plt.figure(1)
plt.subplot(2,1,1)
plt.hist(a_uniform,edgecolor="black",color="green",bins=30)
plt.title("a_uniform chart")

plt.subplot(2,1,2)
plt.hist(a_normal,edgecolor="black",color="green",bins=30)
plt.title("a_normal chart")
plt.tight_layout()
plt.show()
# تفاوت پراکندگی دو نوع توزیع رو از روی نمودار بررسی کردیم
# در توزیع نرمال اغلب پراکندگی در اطراف میانگین است 
# در حالی که در توزیع یکنواخت، داده ها 
# به صورت یکنواخت همه جا پراکنده هستند

