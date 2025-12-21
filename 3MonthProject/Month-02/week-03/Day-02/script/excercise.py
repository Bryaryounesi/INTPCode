# month-02
# week-03
# Day-02

# 1-یک array 100تایی از اعداد تصادفی بساز
import numpy as np
import random
np.random.seed(1)
p=print
a=np.random.randint(-15,40,100)
# یک آرایه یک بعدی (بردار) ساخته شد

# 2-واریانس و انحراف معیار آن را محاسبه کن
a_variance=np.var(a)
a_std=np.std(a)
p("Array variance:",a_variance.round(3))
p("Array std:",a_std.round(3))

# 3-مقادیر را با تابع Pandas روی DataFrame بررسی کن

# برای تبدیل این آرایه به داتافریم بهتر است آن را به ماتریس reshape کنیم
m=a.reshape(10,10)

import pandas as pd

df=pd.DataFrame(m)
p("df cols variance:",df.var().round(3).tolist())
p("df rows variance:",df.var(axis=1).round(3).tolist())
p("df cols std:",df.std().round(3).tolist())
p("df rows std:",df.std(axis=1).round(3).tolist())
# برای خوانایی بیشتر، سری واریانس و انحراف معیارِ
# ستون ها و ردیف ها را تبدیل به لیست کردیم

dfa=pd.DataFrame(a)
# اگر خود بردار را به داتافریم تبدیل کنیم یک داتافریم یک ستونه طویل به ما میده
p("one_col_df variance:",dfa.iloc[:,0].var().round(3))
# از iloc  استفاده شد تا دقیقا ردیف داتا انتخاب شود و نه به همراه ردیف ایندکس
p("one_col_df std:",dfa.std())
# به دلیل تفاوت در مبنای محاسبه توابع آماری 
# خروجی توابع آماری در پانداس و نامپی، کمی و در حد اعشار با هم متفاوتند
