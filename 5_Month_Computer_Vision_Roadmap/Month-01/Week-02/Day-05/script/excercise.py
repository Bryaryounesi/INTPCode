# Month-01
# Week-02
# Day-05

# 1- یک ستون عددی از داتافریم انتخاب کن
p = print
import pandas as pd
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-02\Data\3m_pro_m2_w4_students_exam_scores_copy.xlsx"


df = pd.read_excel(path)
# p(df.select_dtypes(include="number"))

''' ستون 
math score 
انتخاب شد'''

# 2-تغییرات آن را با نمودار خطی رسم کن
import matplotlib.pyplot as plt

fig1,axs1 = plt.subplots()
df.iloc[::50,5].plot(kind="line",ax=axs1,marker="*",linestyle="-.",color="black",title="Math Score Line Chart",xlabel="Data",ylabel="frequency")
# یک نموداری سری پلات خطی رسم شد

'''به دلیل تعداد زیاد و نوسان بیش از حد داده ها 
هر 50 ردیف را در رسم نمودار میله ای
با گذاشتن استپ برای ردیف ها یکی کردیم 
'''
# fig1.savefig(fname="Math Score Line Chart.png",dpi=300)
