# month-02
# week-01
# Day-04

# یک ماتریس 3×3 بساز
import numpy as np
import random
np.random.seed(3)
random.seed(3)
p=print
m=np.random.randint(-7,9,size=(3,3))
p("matrix:",m)
# دترمینان آن را حساب کن
m_det=np.linalg.det(m)
p("matrix determinant:",m_det)
# اگر دترمینان صفر نبود، معکوسش را محاسبه کن
if m_det!=0:
    m_inv=np.linalg.inv(m).round(3)
    # عددهای فلوت حاصل از معکوس سازی طولانی بودند
    # پس آنها را رند کردیم
    p("matrix inverse:",m_inv)
else:
    p("matrix not inversable")
    # اگر دترمینان، برابر با صفر باشد این پرینتِ آخر نمایش داده میشود 