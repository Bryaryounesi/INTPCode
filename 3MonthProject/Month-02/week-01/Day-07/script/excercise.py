# month-02
# week-01
# Day-07

# 1. یک ماتریس 4×4 بساز
import numpy as np
import random
np.random.seed(1)
random.seed(1)
p=print
m=np.random.randint(-9,9,size=(4,4))
p(m)
# 2. مجموع ردیف‌ها و ستون‌ها را حساب کن
p("columns sumations:",np.sum(m,0))
p("rows sumations:",np.sum(m,1))

# 3. دترمینان را به‌دست بیاور
m_det= np.linalg.det(m)
p(m_det)
# 4. اگر معکوس‌پذیر بود، معکوس را حساب کن
m_inv=np.linalg.inv(m)
p(m_inv)
# 5. یک دستگاه ۴ معادله با ۴ مجهول تعریف کن و حلش کن
b= random.choices(population=range(-9,9),k=4)
# بردار بی ساخته شد

# خودمان از قبل یک ماتریس داشتیم به اسم ام
# تنها کاری که لازم بود انجام شود ساخت یک بردار بود تا باقیمانده های دستگاه معادلات را با آن بسازیم
x= np.linalg.solve(m,b)
# معادله مربعی است پس با سولف حل شد

# 6. نتایج را چاپ و تحلیل کن
p("solvation:",x)