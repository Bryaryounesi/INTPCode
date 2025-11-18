# month-01
# week-04
# Day-05

# 1- داده‌ی تمیز و خلاصه‌شده از روز قبل را بخوان
import pandas as pd
path=r"e:\python\INTPCode\3MonthProject\Month-01\Week-04\Day-05\data\merged_share.xlsx"
df= pd.read_excel(path)
p=print
del path
# p(df)
# 2- یک نمودار ستونی از میانگین یا مجموع داده‌ها رسم کن
numcols=df.select_dtypes(include="number").columns

grouped= df.groupby("country",as_index=False)[numcols].mean().round()
p(grouped)
import matplotlib.pyplot as plt
# نمودار ستونی از ستون میانگین نمره شیمی
# ستون ایگریک بیانگر  عدد  میانگین میله هاست
# ستون ایکس بیانگر ایندکس ستون هاست  که در اینجا ناخواسته اعشاری شده
plt.bar(range(len(grouped["chemistry"])),grouped["chemistry"],color="green",edgecolor="black",width=0.3,label="chemistry mean")
# 3- عنوان، محور X و Y، و رنگ‌ها را مشخص کن
# رنگ در سوال 2 مشخص شد 
plt.xlabel("indexes")
plt.ylabel("scores means")
plt.title("mean scores chart")
# 4- دو نمودار مختلف رسم کن (مثلاً یکی خطی، یکی ستونی)
# نمودار دوم یک نمودار خطی از ستون میانگین ریاضی
plt.plot(grouped["math"],marker="*",linestyle="--",color="black",label="math mean")
plt.legend(loc="best")
# 5- نمودار را با plt.savefig() در فایل تصویری ذخیره کن
# plt.savefig(fname="chart.png",dpi=300)
plt.show()
