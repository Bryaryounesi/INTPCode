p = print
'''
نمونه ساخت لیست دیکشنری ها با لیست  کامپرهنشن از توابع فیکر
از این لیست برای ساخت داتافریم استفاده میشود

data = [{"name":fake.name() if random.random()<0.9 else None,
         "country":fake.country()if random.random()<0.8 else None,
         "city": fake.city()if random.random()<0.7 else None,
          "age": fake.random_int(min=18, max=60) if random.random()<0.9 else None,
          "math": fake.random_int(min=7, max=20) if random.random()<0.80 else None,
          "biology": fake.random_int(min=6, max=20) if random.random()<0.8 else None,
          "chemistry": fake.random_int(min=8, max=20) if random.random()<0.9 else None} for i in range(70)]
'''

# برای ساخت داتافریم ها و فایل های اکسل جدید طبق الگوی زیر عمل کنید
p("-------------new dfs pattern-------------------")
# import pandas as pd
# from faker import Faker
# import random

# 1- creat new seed
# X = عددی دلخواه به ایکس بدهید
# random.seed(X)
# Faker.seed(X)

# 2 - creat new fake object
# fakeX = Faker()

# 3- copy above list and chang it
# dataX =[]

# 4- creat new dataframe
# dfX = pd.DataFrame(dataX)
# p(dfX)

# 5- add new remainig colomns
# افزودن ستون های جامانده
# cell_numbers = [fakeX.cell_phone() for i in range(len(dfX))]

# 6- import new df to excel
# pathX = r""
# with pd.ExcelWriter(pathX,mode="a",if_sheet_exists="error")as writer:
    # dfX.to_excel(writer,sheet_name="shX",index=False)

# 7- read new created sheet from excel
# dfallX = pd.read_excel(pathX,sheet_name = "shX")

p(" copy above pattern in new py file and  create new df and excel--")
