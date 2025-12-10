# month-02
# week-02
# Day-03

# 1- یک array تصادفی 100تایی تولید کن و تمام مقادیر زیر  را محاسبه کن
# np.mean ،np.median، np.std، np.var، np.max ، np.min

import numpy as np
import random
random.seed(1)
p=print
L100= random.choices(population=range(-15,30),k=100)
L100.sort()
p("mean:",np.mean(L100))
p("median:",np.median(L100))
p("std:",np.std(L100).round(3))
p("var:",np.var(L100))

# 2- بیشترین و کمترین مقدار را پیدا کن
p("max:",np.max(L100))
p("min:",np.min(L100))

# 3- std و var را با هم مقایسه کن و تفاوت مفهومی را یادداشت کن

# انحراف معیار جذر واریانس است پس 
# اگر انحراف معیار رو به توان دو برسانیم واریانس به دست می آید.
STD= np.std(L100)
VAR= np.var(L100)
# STD=np.sqrt(VAR)
# انحراف معیار = جذر واریانس 

# VAR= STD**2
# واریانس = توان دوم انحراف معیار

