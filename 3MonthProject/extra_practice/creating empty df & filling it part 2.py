# ساخت داتافریم خالی بدون ساختار
import pandas as pd
p = print
df = pd.DataFrame()
p(df)
# مشخص کردن تعداد ردیف ها با افزودن یک ستون بازه ای به داتافریم
id = [i for i in range(30)]
# p(id)
df["id"] = id
# افزودن چند ستون خالی به داتافریم
df[["name","age","country","gender","job"]] = None

# حذف ستون بازه ای که دیگر کاربردی برای ما ندارد
df.drop("id",inplace=True,axis=1)

# داتافریم خالی و چهارچوب دار ما آماده است
# p(df)

# پرکردن ستون جنسیت و کشور با کتابخانه رندوم
import random
random.seed(1)

gender = random.choices(population=["M","F",None], k=30,weights=[0.4,0.5,0.1])
# p(gender)
df["gender"] = gender

country = random.choices(population=["China","USA","Japan","India","Kurdistan","Netherland","England","Germany",None], k=30,weights=None)
df["country"] = country

# پرکردن بقیه ستون ها با فیکر
from faker import Faker
fake = Faker()
Faker.seed(1)

name = [fake.first_name() if random.random() <0.9 else None for i in range(30)]
# p(name)
df["name"] = name

job = [fake.job() if random.random() <0.8 else None for i in range(30)]
df["job"] = job

age = [fake.random_int(min=19,max=65) if random.random() <0.7 else None for i in range(30)]
df["age"] = age

# p(df)
'''
path = r"e:\python\INTPCode\pandas\to_excel.xlsx"
with pd.ExcelWriter(path,mode="a",if_sheet_exists="new") as writer:
    df.to_excel(writer,sheet_name="sh7",index = False)
'''




