# Month-01
# Week-02
# Day-01

# 1- یک داتاست واقعی پیدا کن
import pandas as pd
p=print
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-02\Data\3m_pro_m2_w4_students_exam_scores_copy.xlsx"

df = pd.read_excel(path)
# از داتافریمی مربوط به هفته آخر برنامه سه ماهه استفاده شد

# 2- یک ستون عددی انتخاب کن
numcols = df.select_dtypes(include ="number")
# کل ستون های عددی را جدا کردیم
p(numcols.iloc[:,1])
# با ایلوک دومین ستون را از بین ستون های منتخب ، برگذیدیم

p("--------------------------------")
# 3- آن ستون را به صورت سری انتخاب کن
our_serie = numcols.iloc[:,1]
# خود ستونی که انتخاب شده چون از یک داتافریم بوده در واقع یک سری است

# 4- نوع داده و طول آن را بررسی کن 
p("selected column Data type: ",type(our_serie))
p("selected column Data length: ",len(our_serie))
