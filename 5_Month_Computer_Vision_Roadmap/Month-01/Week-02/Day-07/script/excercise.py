# Month-01
# Week-02
# Day-07

# 1-یک دیتاست کوچک انتخاب کن

import pandas as pd
p=print
path=r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-02\Day-07\Data\BMW_Data.csv"

df=pd.read_csv(path)

# 2-خواندن داده
# p(df)
p("DataFame 10 rows for sample:",df.sample(5))
# به جای خواندن کل داتافریم 
# یک نمونه 5 ردیفی تصادفی را از آن خواندیم
p("---------------------------------")
# 3- بررسی ساختار داده

p("DataFrame Shape:",df.shape)

'''
ابعاد داده (Shape)
# داتافریم هفت ستون و هزاران سطر دارد
p("---------------------------------")

p("DataFrame columns names:",df.columns.tolist())
'''
'''
ستون ها و مفهوم آنها(columns)
date تاریخ , adj_close قیمت پایانی تعدیل شده,close قیمت پایانی در هر روز
open قیمت آغازین, high بالاترین قیمت روزانه,low پایین ترین قیمت روزانه
volume حجم معاملات روزانه به دلار
'''
p("---------------------------------")
# نوع داده ها (data type)
p("DataFrame other info",df.info())
'''
با تابع اینفو متوجه میشویم که به غیر از ستون تاریخ
بقیه ستون ها عددی هستند. ستون تاریخ آبجکت است و معمولا باید به 
datetime 
تبدیل شود
داده ها فاقد مقادیر خالی و کاملا مرتب شده هستند
'''
p("---------------------------------")
# بررسی نمونه 
p(df.head(10))
# متوجه میشویم که داده ها از 8 نوامبر 1996 شروع شده اند
p("Dataframe min:",df.min())
# برخی از روزها حجم معاملات صفر بوده 
# سال اول فقط 38 روز ثبت شده دارد 
# این دو را باید با شرط، فیلتر کنیم
p("---------------------------------")

# 3-یک فیلتر مهم
# میخواهیم فیلتر رو بر ستون تاریخ و ستون حجم اعمال کنیم پس ابتدا آن را 
# از object 
# به datetime تبدیل می کنیم
df["Date"] = pd.to_datetime(df["Date"])
p(df["Date"].dtype)
# ستون تاریخ را تبدیل کردیم
df_filtered = df.query("Date.dt.year.gt(1996) and Volume.gt(0)").reset_index(drop=True)
# سال 1996 و روزهایی که حجم معاملاتشان صفر بود را حذف کردیم
p("---------------------------------")

# 4-رسم حداقل دو نمودار
grouped_df = df_filtered.groupby(df_filtered["Date"].dt.year,as_index=False)["Volume"].agg(["sum","mean","max","min"]).astype(int)
p(grouped_df)
'''
یک داتافریم ساختیم بر اساس گروهبندی داده های زمانی 
با چند ستون حاصل از اعمال توابع آماری 
روی ستون حجم 
'''

import matplotlib.pyplot as plt
fig1,axs1= plt.subplots(2,1,constrained_layout=True)
grouped_df.plot(kind="bar",color="green",edgecolor="black",ax=axs1[0],x= "Date", y = "sum",title="Manually Sumation Of Trade Volume",xlabel="Years",ylabel="Volume Sum(Million $)")

grouped_df.plot(kind="bar",color="grey",edgecolor="black",ax=axs1[1],x="Date",y="mean",title="Manually Average Of Trade Volume",xlabel="Years",ylabel="Valume Mean(Million $)")
'''
دو دی اف پلات میله ای در یک فیگور رسم شد
یکی برای میانگین حجم معملاتی سالانه 
و یکی برای مجموع حجم معاملاتی سالانه
'''
# fig1.savefig(fname="Manually Sum & Manually Avg Of Trade Volume bar Chart.png",dpi=300)
plt.show()

# 5-در چند خط نتیجه‌گیری کن
'''
سال‌های 2007 و 2008 بیشترین فعالیت معاملاتی را داشته‌اند. بیشترین مجموع حجم معاملات سالانه در سال 2008 و بیشترین میانگین حجم معاملات روزانه در سال 2007 ثبت شده است. نمودارهای رسم‌شده این روند را به وضوح نشان می‌دهند.
'''
# -----------------------------------
# 🎯 مأموریت پایان هفته
#  یک گزارش کوتاه بنویس شامل موارد زیر :

# دیتاست چه بود؟ <<<<

# دیتاست مربوط به اطلاعات کندل روزانۀ
# چارت قیمت - سهام شرکت بی ام دبلیو بود

# چند ستون و چند ردیف داشت؟ <<<<
# هفت ستون و بیش از هفت هزار ردیف داشت در ابتدا

# مهم‌ترین ستون از نظر تو کدام بود و چرا؟ <<<<
# مهمترین ستون، ستون تاریخ بود که کل داده های قیمتی و حجم معاملات بر
# اساس آن مرتب شده بود

# کدام نمودار بیشترین کمک را به درک داده کرد؟ <<<<
# نمودار میانگین حجم سالانه معاملات ذهنیت خوبی به ما داد
# '''
