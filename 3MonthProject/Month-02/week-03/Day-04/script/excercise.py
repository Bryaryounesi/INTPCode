# month-02
# week-03
# Day-04

# 1-یک داتافریم واقعی یا مصنوعی بساز (مثلاً نمره دانش‌آموزان در چند درس)
import numpy as np
import pandas as pd
np.random.seed(2)
p=print

m=np.random.uniform(6,20,500).astype(int).reshape(100,5)
df=pd.DataFrame(m)
df.columns=["math","biology","chemistry","physics","geology"]

from faker import Faker
Faker.seed(2)
fake = Faker()
names=[fake.name_male() for i in range(len(df))]
df["names"] =names
# ساخت یک ستون جدید با فیکر


# جابجا کردن ستون جدید به اول داتافریم(این یک مبحث برش لیست است)
# ابتدا نام کل ستون ها رو تبدیل به یک لیست می کنیم
cols=df.columns.tolist()
# سپس لیست رو به دوتیکه برش می دهیم :آخرین عنصر و کل لیست به غیر از آخرین عنصر
# آخرین عنصر رو از اول به لیست اضافه میکنیم فقط باید دقت کنیم که عنصر تکی درون دو کروشه باشد
cols= [cols[-1]] + cols[:-1]

# اضافه کردن مجدد ستون ها به داتافریم
df=df[cols]

# 2-میانگین، بیشینه، کمینه، واریانس، انحراف معیار هر ستون را محاسبه کن
numcols= df.select_dtypes(include="number")
p("df columns max:",numcols.max())
p("df columns min:",numcols.min())
p("df columns mean:",numcols.mean())
p("df columns std:",numcols.std().round(2))
p("df columns var:",numcols.var().round(2))

# 3-از describe() برای خلاصه کامل داده‌ها استفاده کن
p(numcols.describe().round(2))