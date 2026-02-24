# تمرین ساخت تابع برای تغییر مقادیر داتافریم 

p=print
import pandas as pd
df=pd.DataFrame(index=range(0,21),columns=["id","primary_quantity","sold_number","intime_quantity"])
# p(df)
import random
random.seed(2)
primary_quantity=random.choices(range(40,2000),k=len(df))
sold_number=[0 for i in range(len(df))]
# p(sold_number)

id=random.sample(range(10000,100000),k=len(df))
df["primary_quantity"] = primary_quantity
df["sold_number"] = sold_number
df["id"] = id

#یکساله اینه که ما اگر مقداری از هر کلا فروختیم 
# آن مقدار بلافاصله به میزان فروش منتقل بشه 
# و اتوماتیک موجودی از روی این فروش ها محاسبه بشه

# یک راه حل اینه که ایندکس هر محصول رو از روی آیدی اون دربیاریم
'''
p(df.query("id == 76868").index)
# ایندکس رو درآوردیم

df.at[17,"sold_number"]= 45+80
# سپس این ایندکس را به همراه نام ستون 
# برای پیدا کردن سلولی که باید تغییر دهیم استفاده کنیم

df.at[19,"sold_number"] = 63
df.at[8,"sold_number"] = 50
df.at[8,"sold_number"] = df.at[8,"sold_number"]+ 50
df.at[8,"sold_number"] = df.at[8,"sold_number"] +1
df.at[8,"sold_number"] = df.at[8,"sold_number"] +80
p("-------------------------------------")
df["intime_quantity"] = df["primary_quantity"] - df["sold_number"]
# البته باید ستون موجودی فعلی رو زیر این محاسبات بسازیم تا تغییرات بر آن اعمال شوند


# این راه حل کد را طولانی میکند و چندان حرفه ای نیست <<<<<<<<
# مشکل دیگری که دارد این است که اگر محصولات زیاد باشند و بیش از یک بار یک محصول رو به این شکل و به اشتباه  درج کنیم آخرین فروش جایگزین کل فروش های قبلی میشود و درنتیجه موجودی به هم میریزد
'''
p("-------------------------------------")
# راه حل بهتر، داشتن تابعی است برای درج خرده فروشی در داتافریم
# p(df["id"].tolist())
id_list=[13597, 57712, 70934, 51741, 59809, 65523, 78911, 31559, 83467, 33256, 40949, 40225, 13127, 33163, 52617, 32752, 27917, 76868, 76876, 57145, 77336]

def register_sold(df,new_sold,id):
    indx = df.query("id == @id").index[0]
    # برای پی بردن به اینکه هر آیدی کجاست بهتر است ایندکس آن آیدی را بدست بیاوریم
    # @id :مقدار آیدی 
    # @ در تابع کوئری کاربرد دارد و اسم ستون را در شرط با مقدار یک متغیر یا یک ستون قرار میدهد
    # و id : ستون آیدی در داتافریم
    # index[0] : اولین ایندکس از مجموعه ایندکس عبارت زیر را انتخاب میکند
    # df.query("id == @id") این عبارت میگوید، ردیف هایی که آیدی آنها برابر فلان است را به من بده
    # df.query("id == @id").index[0] میگوید ایندکس اولین ردیف از ردیف های داده شده رو بده
    df.at[indx,"sold_number"] = df.at[indx,"sold_number"] + new_sold
    # df.at[indx,"sold_number"] سلولی را که قرار است تغییر کند مشخص 
    # df.at[indx,"sold_number"] = df.at[indx,"sold_number"] سلف اساینمنت برای حذف نشدن مقدار قبلی سلول
    df["intime_quantity"] = df["primary_quantity"] - df["sold_number"]
    # ساخت مجدد کل ستون موجودی بر اساس تفاضل موجودی اولیه و مقادیر فروش رفته
    # این کد، تغییرات فروش را بر ستون موجودی فعلی اعمال می کند
register_sold(df,60,40949)

register_sold(df,45,70934)
register_sold(df,45,32752)
p(df)

    

    


