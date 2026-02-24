# Month-01
# Week-02
# Day-06

p = print
import pandas as pd
path = r"e:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Month-01\Week-02\Data\3m_pro_m2_w4_students_exam_scores_copy.xlsx"
df = pd.read_excel(path)

# 1- دو ستون مرتبط از داتافریم انتخاب کن
# p(df.columns.tolist())
selected_cols_names = ["writing score","parental level of education"]
'''
یکی از ستون ها، دسته ای و دیگری عددی است 
معمولا ستون های دسته ای و عددی در نمودار، مجزا رسم میشوند
و رسم آنها در کنار هم، متپلاتلیب را دچار ارور میکند
چون ایندکس ستون دسته ای با ستون عددی همخوانی ندارد
راه حل، گروهبندی آنها و ساخت یک سری یا داتافریم جدید با هم است. 
'''

# 2-یک نمودار میله ای بساز

grouped= df.groupby(by="parental level of education")["writing score"].mean()
'''
متغیر گروپد، یک سری است چون پارامتر از ایندکس گروپ بای را نگذاشته ایم
پس خود ستون دسته ای مبنای گروهبندی یعنی 
parental level of education
تبدیل به ایندکس سری میشود

(اگر پارامتر مذکور را درج می کردیم 
یعنی :
df.groupby(by="parental level of education",as_index=False)
آن وقت یک داتافریم داشتیم)

میانگین ستون دیگر هم یعنی
["writing score"].mean()
تبدیل به والیوی این سری میشود
'''
import matplotlib.pyplot as plt
fig1 , axs1 = plt.subplots(constrained_layout=True)
grouped.plot(kind="bar",x= grouped.index,y=grouped.values ,ax=axs1,edgecolor="black",color="green",title="Parental Level Of Education by Writing Score Bar Chart",xlabel="Education levels",ylabel="Math score")
# سری پلات ستونی دو ستون منتخب رسم شد
# fig1.savefig(fname="Education_level_by_Writing_Score_Bar_Chart.png",dpi=300)

# 3- یک نمودار پراکندگی برای همان داده ها بساز
fig2 , axs2 = plt.subplots(constrained_layout=True)
df_grouped = df.groupby(by="parental level of education",as_index=False)["writing score"].mean()
# چون اسکتر، سری پلات ندارد یک داتافریم براش ساختیم

df_grouped.iloc[:,0] = ["asso degree", "bach dg", 'h sch', "master dg", 's colg', 's h sch']
'''
نام ستون ها رو خلاصه کردیم چون پارامتر زیر هم نمیتوانست در این 
نوع نمودار این به هم ریختگی را درست کند
constrained_layout=True
'''

df_grouped.plot(kind="scatter",x= df_grouped.columns[0],y=df_grouped.columns[1] ,ax=axs2,color="green",title="Parental Level Of Education by Writing Score Scatter Chart",xlabel="Education levels",ylabel="Math score",s=40)
# fig2.savefig(fname="Education_level_by_Writing_Score_Scatter.png",dpi=300)
plt.show()