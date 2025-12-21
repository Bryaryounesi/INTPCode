# month-02
# week-03
# Day-01

# 1- یک array NumPy بساز و np.mean(), np.sum() محاسبه کن
import numpy as np
import pandas as pd
import random
np.random.seed(1)
p=print
m=np.random.randint(-30,50,size=(10,10))
# به جای یک آرایه تک بعدی، یک ماتریس ساختیم
sumation=np.sum(m,axis=0)
average= np.mean(m,axis=1)

p("matrix cols sumation:",sumation)
p("matrix rows mean:",average)

# 2-یک DataFrame ساده بساز و میانگین هر ستون عددی را با df.mean() محاسبه کن

df= pd.DataFrame(m)
# از ماتریس بالا یک داتافریم ساختیم

df_cols_means= df.mean()
p("DataFrame Columns means:",df_cols_means.tolist())
# برای نمایش بهتر میانگین هر ستون،
# میانگین ها را از یک سری، تبدیل به یک لیست کردیم

