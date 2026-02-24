# Month-01
# Week-02
# Day-04

# 1- یک ستون عددی انتخاب کن

p = print
import pandas as pd
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-02\Data\3m_pro_m2_w4_students_exam_scores_copy.xlsx"

df = pd.read_excel(path)
# p(df.columns)
'''ستون 
writing score
انتخاب شد'''

# 2- سطرهای بزرگتر و کوچکتر از 
# میانگینِ ستون منتخب را جداگانه استخراج کن

df.rename(columns={"writing score":"writing_score"},inplace=True)
# نام ستون منتخب را تغییر دادیم
# تا تابع کوٍثری به دلیل فاصله بین نام ارور ندهد

writing_score_mean = df["writing_score"].mean()
# میانگین ستون منتخب را حساب و آن را در یک متغیر ذخیره کردیم

biger = df.query("writing_score > @writing_score_mean").reset_index(drop=True)
smaller = df.query("writing_score < @writing_score_mean").reset_index(drop=True)
# با علامتِ ات مقدار متغیر میانگین را وارد شرط کوئری کردیم
# ِایندکس ها را نیز دوباره مرتب کردیم
# تا ردیف های خروجی به ترتیب ایندکسی جدید نمایش داده شوند

p("writing_score rows that are biger than writing_score_mean: ")
p(biger)
p("------------------------------")
p("writing_score rows that are smaller than writing_score_mean: ")
p(smaller)
